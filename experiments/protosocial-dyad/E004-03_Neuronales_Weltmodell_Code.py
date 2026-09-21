from __future__ import annotations

import argparse, json, math, os, random, time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, Tuple

import numpy as np
import pandas as pd
import torch
from torch import nn
from torch.utils.data import Dataset, DataLoader

ROOT = Path(__file__).resolve().parent
DATA = ROOT / 'data'
CKPT = ROOT / 'checkpoints'
RESULTS = ROOT / 'results'
for p in (DATA, CKPT, RESULTS): p.mkdir(parents=True, exist_ok=True)

torch.set_num_threads(2)

@dataclass(frozen=True)
class Config:
    seeds: int = 20
    train_seeds: tuple = tuple(range(0,12))
    val_seeds: tuple = tuple(range(12,16))
    test_seeds: tuple = tuple(range(16,20))
    train_ticks: int = 3600
    stable_ticks: int = 1200
    intervention_ticks: int = 1000
    seq_len: int = 96
    stride: int = 48
    batch_size: int = 64
    max_epochs: int = 14
    patience: int = 3
    learning_rate: float = 0.003
    beta_kl: float = 0.0025
    hidden_dim: int = 16
    latent_dims: tuple = (0,2,4)
    transient_width: int = 8
    base_seed: int = 17000

CFG = Config()
N = CFG.train_ticks + CFG.stable_ticks + CFG.intervention_ticks
CONDITIONS = [
    'calibration_positive','calibration_negative',
    'persistent_reactive','playback','reactive_memoryless',
    'autonomous_persistent','random_process','identity_switch'
]
MODELS = {'M0':0,'M1':2,'M2':4}


def set_seed(seed:int):
    random.seed(seed); np.random.seed(seed); torch.manual_seed(seed)


def structured_actions(rng: np.random.Generator, n: int) -> np.ndarray:
    a = np.zeros(n, dtype=np.float32)
    cur = float(rng.choice([-1,0,1]))
    for t in range(n):
        if rng.random() < 0.18: cur = float(rng.choice([-1,0,1]))
        a[t] = cur
    return a


def generate(seed:int, condition:str, override_action_at:int|None=None, playback_from_baseline:bool=False) -> Dict[str,np.ndarray]:
    rng = np.random.default_rng(CFG.base_seed + seed)
    a = structured_actions(rng, N)
    if condition == 'calibration_positive':
        a = rng.choice([-1,0,1], size=N).astype(np.float32)
    if override_action_at is not None:
        old = a[override_action_at]
        a[override_action_at] = -old if old != 0 else 1.0
    obs = np.zeros((N,3), dtype=np.float32)
    h_arr = np.zeros(N, dtype=np.float32)
    rule_arr = np.zeros(N, dtype=np.float32)
    source = np.zeros(N, dtype=np.int64)
    passive = np.zeros(3, dtype=np.float32)
    state = float(rng.normal(0,.45))
    rule = float(rng.choice([-.9,-.65,.65,.9]))
    regime = float(rng.choice([-1,1]))
    switch_tick = CFG.train_ticks + CFG.stable_ticks + CFG.intervention_ticks//2
    transient_tick = CFG.train_ticks + CFG.stable_ticks + CFG.intervention_ticks//4
    delay = 20 if condition == 'calibration_positive' else 8

    # Playback is generated from an independent persistent-reactive history but paired marginally.
    if condition == 'playback':
        base = generate(seed+10000, 'persistent_reactive')
        return {'obs':base['obs'].copy(),'actions':a[:,None],'hidden':np.full(N,np.nan,np.float32),
                'rule':np.full(N,np.nan,np.float32),'source':source,'switch_tick':np.array([switch_tick]),
                'transient_tick':np.array([transient_tick])}

    # Deterministic exogenous innovations permit paired causal forks.
    noise_passive = rng.normal(0,.05,size=(N,3)).astype(np.float32)
    noise_state = rng.normal(0,.10,size=N).astype(np.float32)
    obs_noise_sd = .65 if condition == 'calibration_positive' else .07
    noise_obs = rng.normal(0,obs_noise_sd,size=(N,3)).astype(np.float32)

    for t in range(1,N):
        passive = noise_passive[t] if condition in ('calibration_negative','calibration_positive') else .91*passive + noise_passive[t]
        lag_action = a[max(0,t-delay)]

        if condition == 'calibration_positive':
            # Long-lived hidden regime; next observation depends on delayed action under that regime.
            if t % 900 == 0: regime *= -1
            state = regime
            rule = regime
        elif condition == 'calibration_negative':
            state = noise_state[t]
            rule = 0.0
        elif condition in ('persistent_reactive','identity_switch'):
            if condition == 'identity_switch' and t == switch_tick:
                state = float(rng.normal(0,.45)); rule = -rule; source[t:] = 1
            state = .95*state + .30*rule*lag_action + noise_state[t]
        elif condition == 'reactive_memoryless':
            state = rule*lag_action + noise_state[t]
        elif condition == 'autonomous_persistent':
            state = .975*state + noise_state[t]
        elif condition == 'random_process':
            state = float(rng.normal(0,.75)); rule = 0.0
        else:
            raise ValueError(condition)

        own = np.zeros(3,dtype=np.float32) if condition == 'calibration_positive' else np.array([.35*a[t-1],-.15*a[t-1],.12*a[t-1]],dtype=np.float32)
        if condition == 'calibration_positive':
            hidden = np.array([1.0*regime,.8*regime,-.9*regime],dtype=np.float32)
        elif condition == 'calibration_negative':
            hidden = np.array([.03*state,0,-.02*state],dtype=np.float32)
        else:
            hidden = np.array([.52*np.tanh(state),.34*np.sin(state),-.27*np.tanh(.7*state)],dtype=np.float32)
        cross = np.zeros(3,dtype=np.float32) if condition == 'calibration_positive' else np.array([.10*lag_action*np.tanh(state),0,.08*lag_action*np.sin(state)],dtype=np.float32)
        ar = 0.0 if condition in ('calibration_negative','calibration_positive') else 0.33
        obs[t] = ar*obs[t-1] + passive + own + hidden + cross + noise_obs[t]
        h_arr[t] = state; rule_arr[t] = rule

    if condition not in ('calibration_negative','playback'):
        obs[transient_tick:transient_tick+CFG.transient_width] += np.array([1.5,-1.25,1.0],dtype=np.float32)
    return {'obs':obs,'actions':a[:,None],'hidden':h_arr,'rule':rule_arr,'source':source,
            'switch_tick':np.array([switch_tick]),'transient_tick':np.array([transient_tick])}


def prepare():
    meta = asdict(CFG)
    meta['conditions'] = CONDITIONS
    meta['models'] = MODELS
    meta['research_rule'] = 'No reward; next-observation prediction plus information-complexity penalty.'
    (ROOT/'protocol_frozen.json').write_text(json.dumps(meta,indent=2),encoding='utf-8')
    for cond in CONDITIONS:
        for seed in range(CFG.seeds):
            d=generate(seed,cond)
            np.savez_compressed(DATA/f'{cond}_seed{seed:02d}.npz',**d)
    print('prepared',len(CONDITIONS)*CFG.seeds,'trajectories')


def load_condition(cond:str):
    ds=[]
    for seed in range(CFG.seeds):
        x=np.load(DATA/f'{cond}_seed{seed:02d}.npz')
        ds.append({k:x[k] for k in x.files})
    # standardize from training seeds and training phase only
    train_obs=np.concatenate([ds[s]['obs'][:CFG.train_ticks] for s in CFG.train_seeds],axis=0)
    mu=train_obs.mean(0); sd=train_obs.std(0)+1e-6
    for d in ds: d['obs_z']=((d['obs']-mu)/sd).astype(np.float32)
    return ds,mu,sd


class WindowDataset(Dataset):
    def __init__(self, trajectories, seeds, phase='train'):
        self.items=[]; self.tr=trajectories
        if phase=='train': lo,hi=0,CFG.train_ticks-1
        elif phase=='val': lo,hi=0,CFG.train_ticks-1
        else: lo,hi=CFG.train_ticks,N-1
        for s in seeds:
            for st in range(lo,max(lo,hi-CFG.seq_len+1),CFG.stride):
                self.items.append((s,st))
    def __len__(self): return len(self.items)
    def __getitem__(self,i):
        s,st=self.items[i]; d=self.tr[s]
        obs=d['obs_z'][st:st+CFG.seq_len+1]
        act=d['actions'][st:st+CFG.seq_len]
        return torch.from_numpy(obs[:-1]),torch.from_numpy(act),torch.from_numpy(obs[1:]),s,st


class M0Short(nn.Module):
    """Capacity-matched neural baseline with memory strictly limited to four ticks."""
    def __init__(self):
        super().__init__()
        self.gru=nn.GRU(4,CFG.hidden_dim,batch_first=True)
        self.head=nn.Sequential(nn.Linear(CFG.hidden_dim,24),nn.Tanh(),nn.Linear(24,3))
    def forward(self,obs,act,sample=True):
        x=torch.cat([obs,act],-1)
        B,T,D=x.shape
        xp=torch.cat([torch.zeros(B,3,D,device=x.device,dtype=x.dtype),x],dim=1)
        windows=torch.stack([xp[:,i:i+T] for i in range(4)],dim=2)
        wf=windows.reshape(B*T,4,D)
        _,h=self.gru(wf)
        mean=self.head(h[-1]).reshape(B,T,3)
        kl=torch.zeros(B,T,device=mean.device)
        z=torch.zeros(B,T,0,device=mean.device)
        return mean,kl,z


class LatentWorld(nn.Module):
    def __init__(self,zdim:int):
        super().__init__(); self.zdim=zdim
        self.gru=nn.GRU(4,CFG.hidden_dim,batch_first=True)
        self.qmu=nn.Linear(CFG.hidden_dim,zdim)
        self.qlogvar=nn.Linear(CFG.hidden_dim,zdim)
        self.prior=nn.Sequential(nn.Linear(zdim+1,12),nn.Tanh(),nn.Linear(12,2*zdim))
        self.decoder=nn.Sequential(nn.Linear(4+zdim,24),nn.Tanh(),nn.Linear(24,3))
    def forward(self,obs,act,sample=True):
        x=torch.cat([obs,act],-1)
        h,_=self.gru(x)
        mu=self.qmu(h); logv=torch.clamp(self.qlogvar(h),-5,2)
        z=mu + (torch.randn_like(mu)*torch.exp(.5*logv) if sample else 0)
        zprev=torch.cat([torch.zeros_like(z[:,:1]),z[:,:-1]],1)
        pout=self.prior(torch.cat([zprev,act],-1)); pmu,plogv=pout.chunk(2,-1); plogv=torch.clamp(plogv,-5,2)
        kl=.5*torch.sum(plogv-logv+(torch.exp(logv)+(mu-pmu)**2)/torch.exp(plogv)-1,dim=-1)
        mean=self.decoder(torch.cat([obs,act,z],-1))
        return mean,kl,z


def make_model(name:str):
    return M0Short() if name=='M0' else LatentWorld(MODELS[name])


def ckpt_path(cond,model): return CKPT/f'{cond}_{model}.pt'

def train(cond:str,model_name:str,epochs_chunk:int=3):
    set_seed(9000 + CONDITIONS.index(cond)*100 + list(MODELS).index(model_name))
    trajectories,_,_=load_condition(cond)
    train_ds=WindowDataset(trajectories,CFG.train_seeds,'train')
    val_ds=WindowDataset(trajectories,CFG.val_seeds,'val')
    train_dl=DataLoader(train_ds,batch_size=CFG.batch_size,shuffle=True)
    val_dl=DataLoader(val_ds,batch_size=CFG.batch_size,shuffle=False)
    model=make_model(model_name)
    opt=torch.optim.Adam(model.parameters(),lr=CFG.learning_rate)
    start_epoch=0; best=float('inf'); bad=0; history=[]; best_state=None
    cp=ckpt_path(cond,model_name)
    if cp.exists():
        st=torch.load(cp,map_location='cpu',weights_only=False)
        model.load_state_dict(st['model']); opt.load_state_dict(st['opt'])
        start_epoch=st['epoch']; best=st['best']; bad=st['bad']; history=st['history']; best_state=st.get('best_state')
    target_epoch=min(CFG.max_epochs,start_epoch+epochs_chunk)
    for epoch in range(start_epoch,target_epoch):
        model.train(); trloss=[]
        for obs,act,y,_,_ in train_dl:
            mean,kl,z=model(obs,act,sample=True)
            mse=((mean-y)**2).mean()
            loss=mse+CFG.beta_kl*kl.mean()
            opt.zero_grad(); loss.backward(); nn.utils.clip_grad_norm_(model.parameters(),2.0); opt.step()
            trloss.append(float(loss.detach()))
        model.eval(); vals=[]
        with torch.no_grad():
            for obs,act,y,_,_ in val_dl:
                mean,kl,z=model(obs,act,sample=False)
                vals.append(float((((mean-y)**2).mean()+CFG.beta_kl*kl.mean()).detach()))
        val=float(np.mean(vals)); trainloss=float(np.mean(trloss))
        history.append({'epoch':epoch+1,'train':trainloss,'val':val})
        if val < best-1e-4:
            best=val; bad=0; best_state={k:v.detach().cpu().clone() for k,v in model.state_dict().items()}
        else: bad+=1
        payload={'model':model.state_dict(),'opt':opt.state_dict(),'epoch':epoch+1,'best':best,'bad':bad,
                 'history':history,'best_state':best_state}
        tmp=cp.with_suffix('.tmp')
        torch.save(payload,tmp)
        os.replace(tmp,cp)
        print(cond,model_name,'epoch',epoch+1,'train',round(trainloss,5),'val',round(val,5),'bad',bad,flush=True)
        if bad>=CFG.patience: break
    return history[-1]


def evaluate(cond:str,model_name:str):
    trajectories,mu,sd=load_condition(cond)
    model=make_model(model_name); st=torch.load(ckpt_path(cond,model_name),map_location='cpu',weights_only=False)
    model.load_state_dict(st['best_state'] if st.get('best_state') is not None else st['model']); model.eval()
    out=[]; latent_dir=RESULTS/'latents'; latent_dir.mkdir(exist_ok=True)
    for seed in CFG.test_seeds:
        d=trajectories[seed]; obs=torch.from_numpy(d['obs_z']).unsqueeze(0); act=torch.from_numpy(d['actions']).unsqueeze(0)
        with torch.no_grad(): mean,kl,z=model(obs[:,:-1],act[:,:-1],sample=False)
        y=obs[:,1:]; err=((mean-y)**2).mean(-1).squeeze(0).numpy(); klv=kl.squeeze(0).numpy(); zn=z.squeeze(0).numpy()
        hold=slice(CFG.train_ticks,N-1)
        base={'condition':cond,'model':model_name,'seed':seed,'latent_dim':MODELS[model_name],
              'holdout_mse':float(err[hold].mean()),'holdout_kl':float(klv[hold].mean()),
              'holdout_objective':float(err[hold].mean()+CFG.beta_kl*klv[hold].mean()),
              'val_best':float(st['best']),'epochs':int(st['epoch'])}
        if MODELS[model_name]>0:
            # Ablation/permutation sensitivity on holdout: decoder only, preserving inferred posterior.
            with torch.no_grad():
                o=obs[:,:-1]; a=act[:,:-1]; zfull=z
                zero=torch.zeros_like(zfull)
                perm=zfull[:,torch.randperm(zfull.shape[1])]
                pred0=model.decoder(torch.cat([o,a,zero],-1))
                predp=model.decoder(torch.cat([o,a,perm],-1))
                e0=((pred0-y)**2).mean(-1).squeeze(0).numpy()
                ep=((predp-y)**2).mean(-1).squeeze(0).numpy()
            base['ablation_delta']=float(e0[hold].mean()-err[hold].mean())
            base['permutation_delta']=float(ep[hold].mean()-err[hold].mean())
            # Diagnostic linear decoder, fitted on train, tested on held-out test phase.
            valid=np.isfinite(d['hidden'][:-1])
            tr=np.arange(N-1)<CFG.train_ticks; te=np.arange(N-1)>=CFG.train_ticks
            Xtr=np.c_[np.ones((tr&valid).sum()),zn[tr&valid]]; yy=d['hidden'][:-1][tr&valid]
            if len(yy)>10:
                coef=np.linalg.pinv(Xtr)@yy
                yh=np.c_[np.ones((te&valid).sum()),zn[te&valid]]@coef; yt=d['hidden'][:-1][te&valid]
                base['decoder_r2_hidden']=float(1-np.sum((yt-yh)**2)/(np.sum((yt-yt.mean())**2)+1e-9))
            else: base['decoder_r2_hidden']=np.nan
            def persistent_shift(t,w=32):
                pre=zn[t-w:t].mean(0); short=zn[t:t+w].mean(0); late=zn[t+2*w:t+3*w].mean(0)
                return float(np.linalg.norm(late-pre)),float(np.linalg.norm(short-pre))
            sw_late,sw_short=persistent_shift(int(d['switch_tick'][0])); tr_late,tr_short=persistent_shift(int(d['transient_tick'][0]))
            base.update({'switch_late_shift':sw_late,'switch_short_shift':sw_short,
                         'transient_late_shift':tr_late,'transient_short_shift':tr_short,
                         'switch_specificity':sw_late-tr_late})
            np.savez_compressed(latent_dir/f'{cond}_{model_name}_seed{seed}.npz',z=zn,error=err,kl=klv)
        out.append(base)
    pd.DataFrame(out).to_csv(RESULTS/f'eval_{cond}_{model_name}.csv',index=False)
    print(pd.DataFrame(out).to_string(index=False))


def causal_fork():
    # Use the trained persistent-reactive models. Pair baseline, live override, and disconnected playback.
    rows=[]
    fork=CFG.train_ticks+CFG.stable_ticks+150
    for model_name in MODELS:
        trajectories,mu,sd=load_condition('persistent_reactive')
        model=make_model(model_name); st=torch.load(ckpt_path('persistent_reactive',model_name),map_location='cpu',weights_only=False)
        model.load_state_dict(st['best_state'] if st.get('best_state') is not None else st['model']); model.eval()
        for seed in CFG.test_seeds:
            baseline=generate(seed,'persistent_reactive')
            live=generate(seed,'persistent_reactive',override_action_at=fork)
            playback={k:(v.copy() if hasattr(v,'copy') else v) for k,v in baseline.items()}
            playback['actions']=live['actions'].copy()  # changed action, but baseline observations continue
            for label,d in [('live',live),('causal_playback',playback)]:
                oz=((d['obs']-mu)/sd).astype(np.float32)
                obs=torch.from_numpy(oz).unsqueeze(0); act=torch.from_numpy(d['actions']).unsqueeze(0)
                with torch.no_grad(): mean,kl,z=model(obs[:,:-1],act[:,:-1],sample=False)
                err=((mean-obs[:,1:])**2).mean(-1).squeeze(0).numpy()
                window=slice(fork,min(N-1,fork+24))
                rows.append({'model':model_name,'seed':seed,'branch':label,'fork_tick':fork,
                             'postfork_mse':float(err[window].mean()),
                             'postfork_kl':float(kl.squeeze(0).numpy()[window].mean())})
    df=pd.DataFrame(rows); df.to_csv(RESULTS/'causal_fork.csv',index=False); print(df.to_string(index=False))


def aggregate():
    files=list(RESULTS.glob('eval_*.csv'))
    df=pd.concat([pd.read_csv(f) for f in files],ignore_index=True)
    df.to_csv(RESULTS/'all_evaluations.csv',index=False)
    best=df.sort_values('holdout_objective').groupby(['condition','seed'],as_index=False).first()
    best.to_csv(RESULTS/'best_model_by_holdout_seed.csv',index=False)
    counts=best.groupby(['condition','model']).size().unstack(fill_value=0)
    counts.to_csv(RESULTS/'selection_counts.csv')
    agg=df.groupby(['condition','model'],as_index=False).agg(
        mean_mse=('holdout_mse','mean'),sd_mse=('holdout_mse','std'),
        mean_objective=('holdout_objective','mean'),mean_kl=('holdout_kl','mean'),
        mean_ablation_delta=('ablation_delta','mean'),mean_permutation_delta=('permutation_delta','mean'),
        mean_decoder_r2=('decoder_r2_hidden','mean'),mean_switch_specificity=('switch_specificity','mean'))
    agg.to_csv(RESULTS/'aggregate.csv',index=False)
    print('selection\n',counts); print('\naggregate\n',agg.to_string(index=False))


def main():
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest='cmd',required=True)
    sub.add_parser('prepare')
    t=sub.add_parser('train'); t.add_argument('--condition',required=True,choices=CONDITIONS); t.add_argument('--model',required=True,choices=MODELS); t.add_argument('--epochs',type=int,default=3)
    e=sub.add_parser('evaluate'); e.add_argument('--condition',required=True,choices=CONDITIONS); e.add_argument('--model',required=True,choices=MODELS)
    sub.add_parser('causal-fork'); sub.add_parser('aggregate')
    args=ap.parse_args()
    if args.cmd=='prepare': prepare()
    elif args.cmd=='train': train(args.condition,args.model,args.epochs)
    elif args.cmd=='evaluate': evaluate(args.condition,args.model)
    elif args.cmd=='causal-fork': causal_fork()
    elif args.cmd=='aggregate': aggregate()

if __name__=='__main__': main()
