# PL-R2 — Phase 5: PL-Gate für K06 v1.0

**Datum:** 2026-07-11  
**Grundlagen:**
- `PL_R2_Suchprozess_Freeze_v1.0.md`
- `PL_R2_Rohkandidaten_v1.0.md`
- `PL_R2_Phase2_Entdoppelung_v1.0.md`
- `PL_R2_Phase3_Blinder_Sofortfilter_v1.0.md`
- `PL_R2_Phase4_Neun_Fragen_v1.0.md`
- `PL_Pruefraster_Protosoziale_Praxis.md`
- verbindliches PL-Handoff

**Prüfgegenstand:** `PL-R2-K06 — Komplementäre Vervollständigung einer offenen Handlung`  
**Nicht zulässig:** Reparatur, zusätzliche Reaktionsschritte, neue Zustandswirkungen, Agentenarchitektur oder Lernmethode

---

## 1. Unveränderter Kandidatenkern

Eine sichtbare, unvollständige Handlung eines Initiators lässt zwei physisch mögliche Endpunkte offen. Der Partner stellt durch eine komplementäre Handlung Endpunkt `X` oder `Y` her. Der Initiator setzt anschließend mit `X1` oder `Y1` fort, kehrt um oder bricht ab.

Mögliche erfolgreiche Verläufe:

```text
offene Handlung → X → X1 → Abschluss
offene Handlung → Y → Y1 → Abschluss
```

Gefährlichstes einfaches Vollmodell:

```text
vervollständigender Agent:
offene Handlung + Partner-ID → X oder Y

initiierender Agent:
sichtbarer Endpunkt → X1 oder Y1
```

---

# 2. Ergebnisübersicht G1–G6

| Gate | Verdikt | Kernbegründung |
|---|---|---|
| **G1 — mehrere gleichwertige Stabilitätspunkte** | **nicht bestanden** | X/X1 und Y/Y1 sind möglich, aber Gleichwertigkeit und schlechtere Mischformen sind nicht Bestandteil des Kandidaten |
| **G2 — echte Wechselseitigkeit** | **nicht bestanden** | Nach der Vervollständigung ist keine weitere Partnerreaktion erforderlich; Ghost-Replay kann den Partner prinzipiell ersetzen |
| **G3 — historische Kontingenz** | **nicht bestanden** | Verschiedene Endpunkte können aus fester Partnerpräferenz oder Seed-Unterschieden entstehen; gemeinsame Geschichte ist nicht notwendig |
| **G4 — verteilte Kausalität** | **nicht bestanden** | Der vervollständigende Partner kann die Variante unilateral auswählen; der Initiator kann nur zustandsabhängig folgen |
| **G5 — Verlauf statt Einzelhandlung** | **bestanden** | Die Einheit umfasst Initiation, Vervollständigung, Fortsetzung und Abschluss beziehungsweise Abbruch |
| **G6 — kein versteckter sozialer Zustand** | **bestanden** | Keine Norm-, Gruppen-, Reputations- oder Konventionsvariable ist vorgesehen |

**Zwischenergebnis:** Vier der sechs harten Gates sind nicht geschlossen; zwei davon — G2 und G4 — scheitern bereits strukturell.

---

# 3. Prüfung der harten Gates

## G1 — Mehrere gleichwertige Stabilitätspunkte

### Anforderung

Mindestens zwei Praktiken müssen:

- jeweils funktionieren,
- funktional gleichwertig sein,
- gegenüber Mischformen einen Vorteil besitzen,
- ohne Umweltpräferenz offenbleiben.

### Prüfung

K06 enthält zwei physisch mögliche Verläufe:

```text
X → X1
Y → Y1
```

Daraus folgt noch nicht:

- dass beide dieselbe Abschlusswahrscheinlichkeit besitzen;
- dass sie denselben Aufwand oder dieselben privaten Zustandsfolgen haben;
- dass gekreuzte Verläufe `X → Y1` beziehungsweise `Y → X1` schlechter funktionieren;
- dass eine stabile dyadische Zuordnung gegenüber unmittelbarer Zustandsreaktion vorteilhaft ist.

Der Kandidat definiert zwar mehrere Möglichkeiten, aber noch keine mehreren gleichwertigen **Stabilitätspunkte**. Eine entsprechende Erfolgs- oder Zustandsstruktur dürfte in dieser Phase nicht ergänzt werden.

### Verdikt

**Nicht bestanden.**

Das Problem ist nicht nur fehlende Parametrisierung. Der Koordinationsvorteil der dyadisch stabilisierten Variante ist im unveränderten Kandidaten nicht formal enthalten.

---

## G2 — Echte Wechselseitigkeit

### Anforderung

Das aktuelle Verhalten jedes Agenten muss die nächste Entscheidungslage des anderen verändern. Eine aufgezeichnete plausible Partnersequenz darf die reale Interaktion nicht gleichwertig ersetzen.

### Prüfung

Die Folge besitzt drei kausale Schritte:

```text
Initiator öffnet
→ Partner vervollständigt
→ Initiator setzt fort
```

Die Partnerhandlung verändert tatsächlich die Entscheidungslage des Initiators. Danach endet der relevante Verlauf jedoch bereits mit Fortsetzung, Umkehr oder Abbruch. Der Partner muss nicht erneut auf diese Reaktion antworten.

Ein Ghost kann deshalb:

1. bei Begegnungsbeginn eine aufgezeichnete Vervollständigung `X` oder `Y` ausführen;
2. damit denselben sichtbaren Endpunkt herstellen;
3. dem Initiator dieselbe zustandsabhängige Fortsetzung ermöglichen.

Da die offene Anfangshandlung in der Rohbeschreibung gleich bleibt, muss der Ghost nicht zwischen unterschiedlichen aktuellen Initiationen unterscheiden. Die Verteilung der Endpunkte kann aus realen Begegnungen übernommen werden.

### Verdikt

**Nicht bestanden.**

K06 enthält komplementäre Kausalität, aber keine geschlossene Wechselseitigkeit. Die reale Responsivität des Partners ist für den vollständigen relevanten Verlauf nicht notwendig.

---

## G3 — Historische Kontingenz

### Anforderung

Unter gleichen äußeren Bedingungen müssen verschiedene tatsächliche Begegnungslinien unterschiedliche stabile Praktiken hervorbringen können. Unterschiede dürfen nicht vollständig durch aktuelle Lage, Startparameter oder feste individuelle Präferenzen erklärt sein.

### Prüfung

Getrennte Dyaden könnten äußerlich unterschiedliche Verläufe zeigen:

- Dyade A stabilisiert `X → X1`;
- Dyade B stabilisiert `Y → Y1`.

Dafür ist jedoch keine gemeinsame Geschichte erforderlich. Dasselbe Ergebnis entsteht, wenn:

- Partner A eine feste Präferenz für `X` besitzt;
- Partner B eine feste Präferenz für `Y` besitzt;
- der Initiator allgemein auf den sichtbaren Endpunkt reagiert;
- oder die Zuordnung einmal gelernt und anschließend als Partner-ID-Tabelle offen ausgeführt wird.

Die konkrete Episodenfolge ist nach Ausbildung der Zuordnung nicht kausal erforderlich. Ein Begegnungsgeschichts-Shuffle, der dieselben Endpunkt- und Fortsetzungshäufigkeiten erhält, zerstört daher keinen im Kandidaten spezifizierten Zusatzmechanismus.

### Verdikt

**Nicht bestanden.**

Mögliche Variation zwischen Dyaden ist noch keine historische Kontingenz. K06 trennt gemeinsame Geschichte nicht von individueller Präferenz oder Partnerkalibrierung.

---

## G4 — Verteilte Kausalität

### Anforderung

Mehrere Agenten müssen die konkrete Praxis durch ihre lern- und verlaufsabhängigen Reaktionen aufrechterhalten. Ein Agent darf die Variante nicht allein diktieren.

### Prüfung

Für den physischen Abschluss sind beide Agenten beteiligt:

- Der Initiator erzeugt die offene Lage.
- Der Partner stellt `X` oder `Y` her.
- Der Initiator führt `X1` oder `Y1` aus.

Für die **Auswahl der stabilen Variante** genügt jedoch der vervollständigende Partner. Er kann bei derselben offenen Handlung stets `X` wählen. Der Initiator benötigt nur:

```text
sichtbares X → X1
sichtbares Y → Y1
```

Diese Anschlussregel kann partnerunabhängig und gedächtnislos sein.

Ein einseitiger Austausch der Lernhistorie des Initiators muss daher die Endpunktwahl nicht verändern. Ein Austausch der Partnerhistorie kann die Variante vollständig umstellen. Damit liegt die bestimmende Kausalität auf einer Seite.

### Verdikt

**Nicht bestanden.**

Physische Beteiligung beider Agenten ist vorhanden; verteilte Stabilisierung der Praxis ist es nicht.

---

## G5 — Verlauf statt Einzelhandlung

### Prüfung

Die relevante Beobachtungseinheit ist mindestens:

```text
Initiation
→ Partnervervollständigung
→ Fortsetzung, Umkehr oder Abbruch
→ Abschluss
```

Damit ist K06 nicht auf eine einzelne Aktion reduzierbar.

### Verdikt

**Bestanden.**

Dieses Gate allein trennt den Kandidaten jedoch nicht von einem kurzen Zustandsautomaten.

---

## G6 — Kein versteckter sozialer Zustand

### Prüfung

Der Kandidat enthält keinen:

- dyadischen Konventionsspeicher;
- öffentlichen Geltungszustand;
- Rollen- oder Gruppenlabel;
- Reputationswert;
- gemeinsamen Episodenpool;
- persistenten Umweltzustand.

Die Endpunkte sind flüchtige physische Zustände der aktuellen Begegnung.

### Verdikt

**Bestanden.**

Eine spätere Implementierung müsste weiterhin verhindern, dass „für diese Dyade gilt X“ als expliziter gemeinsamer Zustand gespeichert wird. Im unveränderten Kandidaten ist ein solcher Zustand aber nicht vorgesehen.

---

# 4. Prüfung gegen M0–M3

## M0 — Mechanische Reaktion

Ein vollständiger Ablauf kann durch aktuelle sichtbare Zustände erzeugt werden:

```text
offene Lage → Partner stellt X her
sichtbares X → Initiator führt X1 aus
```

Mit einer festen Regel für den vervollständigenden Partner ist keine Episodengeschichte nötig.

**Befund:** M0 kann mindestens eine vollständige stabile Variante reproduzieren.

---

## M1 — Imitation oder unmittelbare Reizübernahme

Die Agenten kopieren einander nicht notwendig. Eine unmittelbare komplementäre Reizregel genügt jedoch:

```text
offene Handlung gesehen → komplementiere zu X
X gesehen → führe X1 aus
```

Das ist keine Imitation im engen Sinn, bleibt aber unmittelbare partnerausgelöste Reaktion ohne gemeinsame historische Hervorbringung.

**Befund:** M1 ist nicht die stärkste Erklärung, aber eine kurze unmittelbare Reaktionskette bleibt hinreichend.

---

## M2 — Individuelle Gewohnheit oder Verstärkung

Beide Agenten können getrennte private Routinen ausbilden:

- Partner wiederholt seine bevorzugte Vervollständigung;
- Initiator wiederholt die für den sichtbaren Endpunkt passende Fortsetzung.

Die Routinen können kompatibel werden, ohne dass eine spezifische gemeinsame Praxis in beiden Historien liegt.

**Befund:** M2 kann den relevanten Verlauf vollständig erklären.

---

## M3 — Koordination

K06 kann als Koordination gelesen werden:

- komplementäre Handlungen ermöglichen einen Abschluss;
- `X/X1` und `Y/Y1` können kompatible Folgen sein.

Eine optimale gedächtnislose Koordinationspolicy oder eine Partner-ID-Policy ohne Episodenfolge kann den Ablauf jedoch vollständig tragen.

**Befund:** K06 erreicht höchstens Stufe C — Koordination. M3 wird nicht übertroffen.

---

# 5. Mindestkontrollen C0–C6

## C0 — Umweltkontrolle

**Aufbau:** gleiche offene Lage ohne reaktiven Partner.

**Erwartung:** Der Initiator kann allein keinen Endpunkt herstellen.

**Aussagekraft:** Zeigt nur, dass ein komplementärer Beitrag physisch nötig ist. Es trennt soziale Praxis nicht von mechanischer Ergänzung.

---

## C1 — Ghost-Replay

**Aufbau:** Ein Ghost spielt reale Vervollständigungen `X` oder `Y` mit derselben Häufigkeit und zeitlichen Lage ab, reagiert aber nicht auf den Initiator.

**Vorhersage aus K06:** Der Initiator kann nach dem sichtbaren Endpunkt weiterhin `X1` oder `Y1` ausführen.

**Aussagekraft:** Der Ghost kann den relevanten Partnerbeitrag prinzipiell ersetzen.

**Gate-Folge:** Diese strukturelle Ghost-Festigkeit ist ein negativer Befund für G2.

---

## C2 — Begegnungsgeschichts-Shuffle

**Aufbau:** Gleiche offene Handlungen, Endpunkte und Fortsetzungen; die Zuordnung zu tatsächlichen Begegnungslinien wird permutiert.

**Vorhersage des Einfachmodells:** Solange die Übergangshäufigkeiten beziehungsweise Partner-ID-Zuordnungen erhalten bleiben, bleibt das Verhalten unverändert.

**Problem:** Die Rohfassung enthält keine längere relationale Abhängigkeit, die durch den Shuffle zerstört würde.

**Gate-Folge:** K06 liefert keine vorab begründete, vom Tabellenmodell verschiedene Shuffle-Vorhersage.

---

## C3 — Gleichwelt-Replikation

**Aufbau:** identische Umwelt, Aktionsmenge und Startverteilungen; getrennte Zufallsströme.

**Möglicher Befund:** Manche Replikationen stabilisieren `X/X1`, andere `Y/Y1`.

**Problem:** Dieser Unterschied kann vollständig aus zufälliger früher Partnerwahl, fester individueller Präferenz oder einer einmaligen Symmetriebrechung entstehen.

**Aussagekraft:** Unterschiedliche Replikationen allein würden G3 nicht schließen.

---

## C4 — Partnerwechsel

**Aufbau:** Initiatoren und vervollständigende Partner aus verschieden stabilisierten Dyaden werden neu gekoppelt.

**Vorhersage des Einfachmodells:**

- Der neue Partner stellt seinen bevorzugten Endpunkt her.
- Der Initiator reagiert unmittelbar auf den sichtbaren Endpunkt.
- Es muss keine spezifische Inkompatibilität oder gemeinsame Neujustierung entstehen.

**Aussagekraft:** Ein glatter Wechsel wäre mit M0–M3 vollständig vereinbar. Eine vorübergehende Störung könnte wiederum bloße Partnererwartung oder Kalibrierung zeigen.

---

## C5 — Responsivitäts-Knockout

**Aufbau:** Der Partner erzeugt weiterhin plausible Endpunkte, seine Wahl hängt aber nicht vom aktuellen Verhalten des Initiators ab.

**Vorhersage aus K06:** Da die Anfangshandlung in der Rohbeschreibung dieselbe offene Lage erzeugt, kann der Knockout-Partner weiterhin erfolgreiche Endpunkte herstellen.

**Gate-Folge:** Aktuelle Kontingenz ist für den relevanten Ablauf nicht notwendig.

---

## C6 — Einfachmodell-Konkurrenz

Mindestens zu prüfende Modelle:

1. feste Reiz-Reaktions-Tabelle;
2. feste komplementäre Antwort auf die offene Handlung;
3. Copy-last-action als Negativbaseline;
4. individuelle Reinforcement-Policy;
5. partnerunabhängige Markov-Policy;
6. optimale gedächtnislose Koordinationspolicy;
7. Policy mit Partner-ID, aber ohne Episodenfolge.

Das kleinste hinreichende Vollmodell ist:

```text
P(endpunkt = X | offene Handlung, Partner-ID)

P(fortsetzung = X1 | sichtbarer Endpunkt X)
P(fortsetzung = Y1 | sichtbarer Endpunkt Y)
```

Dieses Modell reproduziert:

- dyadenspezifische Endpunktverteilungen;
- stabile X- oder Y-Verläufe;
- passende Fortsetzungen;
- erfolgreiche Abschlüsse;
- Unterschiede zwischen Dyaden;
- unmittelbare Anpassung nach Partnerwechsel.

Es benötigt weder gemeinsame Episodenfolge noch verteilte Praxis.

**Befund:** C6 liefert bereits ein plausibles einfaches Vollmodell.

---

# 6. Pflichtfelder des Phase-5-Gates

## Hauptstärke

K06 erzwingt einen realen komplementären Beitrag: Der Initiator kann die offene Handlung nicht allein vervollständigen. Die relevante Einheit ist mehrschrittig und formal beobachtbar.

## Hauptschwäche

Die Folge ist zu kurz und asymmetrisch. Der vervollständigende Partner kann die Variante auswählen; danach genügt eine allgemeine Reaktion des Initiators auf den sichtbaren Endpunkt.

## Gefährlichste Gegenhypothese

> Der Partner wählt anhand einer festen oder partnerbezogenen privaten Zuordnung Endpunkt X oder Y. Der Initiator verwendet eine gedächtnislose Anschlussregel für den sichtbaren Endpunkt. Die beobachtete Ordnung ist deshalb mechanische beziehungsweise erlernte Koordination, nicht gemeinsam historisch hervorgebrachte Praxis.

## Notwendige Kontrolle

Die schärfste unmittelbare Kontrolle wäre ein marginal- und zeitabgeglichenes Ghost-Replay beziehungsweise ein Responsivitäts-Knockout der Vervollständigung.

K06 hat jedoch keine vorab begründete Erwartung, unter dieser Kontrolle zu zerfallen. Der Ghost stellt denselben physischen Endpunkt her, auf den der Initiator reagieren kann. Die Kontrolle trennt daher nicht nur eine mögliche Gegenhypothese ab, sondern legt das strukturelle Defizit des Kandidaten offen.

## Vorab-Verwerfungskriterium

K06 ist vor Implementierung zu verwerfen, wenn ein Modell aus:

```text
offene Handlung + Partner-ID → Endpunkt
sichtbarer Endpunkt → Fortsetzung
```

alle relevanten Verläufe reproduzieren kann oder wenn Ghost-Replay beziehungsweise Responsivitäts-Knockout den erfolgreichen Ablauf nicht notwendig verändert.

Beide Bedingungen sind für die unveränderte Rohfassung bereits plausibel erfüllt.

---

# 7. Phase-5-Verdikt

## Verwerfen

K06 erfüllt G5 und G6. Es scheitert aber an mindestens zwei strukturell harten Gates:

- **G2:** keine notwendige geschlossene Wechselseitigkeit;
- **G4:** keine notwendige verteilte Kausalität.

Zusätzlich sind:

- **G1** nicht formal hergestellt;
- **G3** nicht von individueller Präferenz oder Partnerkalibrierung getrennt.

Die Konkurrenzmodelle M0, M2 und M3 können den vollständigen relevanten Befund plausibel reproduzieren. Das Partner-ID-Modell ohne Episodenfolge ist bereits ein hinreichender nichtsozialer beziehungsweise bloß koordinativer Vollerklärer.

K06 wird daher nicht in Phase 6 als verbleibender Kandidat weitergeführt.

---

# 8. Phase-5-Register

| Kandidat | Phase-5-Ergebnis |
|---|---|
| **PL-R2-K06** | **verwerfen** |

## Verbleibende Kandidaten nach Phase 5

**Keine.**

Das zulässige Zwischenergebnis der zweiten Kandidatenrunde lautet damit:

> Kein Kandidat hat alle harten Gates prinzipiell geschlossen.

---

# 9. Nächster formaler Schritt

Phase 6 besitzt nach dem Phase-5-Verdikt keine verbleibenden Kandidaten für einen adversarialen Angriff. Sie kann nur noch als formale Leerprüfung dokumentieren:

```text
Menge der Phase-6-Kandidaten = ∅
```

Danach folgt Phase 7 als vergleichendes Ansatz-Gate der geschlossenen Kandidatenmenge. Dort ist insbesondere festzuhalten, dass kein Kandidat aufgrund relativer Überlegenheit oder als letzter Überlebender ausgewählt wird.
