from __future__ import annotations

import json
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from typing import Any

from ..core.controller import LabController
from .world_canvas import WorldCanvas


class MainWindow(tk.Tk):
    def __init__(self, scenario_directory: Path) -> None:
        super().__init__()
        self.title("Schwarmwelt Labor")
        self.geometry("1220x790")
        self.minsize(920, 620)
        self.scenario_directory = scenario_directory
        self.scenarios = {path.stem: path for path in sorted(scenario_directory.glob("*.json"))}
        if not self.scenarios:
            raise RuntimeError(f"Keine Szenarien in {scenario_directory}")
        first_name = "ritual_baseline" if "ritual_baseline" in self.scenarios else next(iter(self.scenarios))
        self.controller = LabController(self.scenarios[first_name])
        self.playing = False
        self.selected_agent: int | None = None
        self._build_ui(first_name)
        self._render(self.controller.snapshot())
        self.after(60, self._animation_loop)

    def _build_ui(self, first_name: str) -> None:
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        toolbar = ttk.Frame(self, padding=(8, 6))
        toolbar.grid(row=0, column=0, sticky="ew")
        toolbar.columnconfigure(8, weight=1)

        ttk.Label(toolbar, text="Szenario").grid(row=0, column=0, padx=(0, 4), sticky="w")
        self.scenario_var = tk.StringVar(value=first_name)
        scenario_box = ttk.Combobox(toolbar, textvariable=self.scenario_var, values=list(self.scenarios), state="readonly", width=25)
        scenario_box.grid(row=0, column=1, padx=(0, 10), sticky="w")
        scenario_box.bind("<<ComboboxSelected>>", lambda _event: self._load_selected_scenario())

        ttk.Label(toolbar, text="Seed").grid(row=0, column=2, padx=(0, 4))
        self.seed_var = tk.StringVar(value=str(self.controller.config.seed))
        ttk.Entry(toolbar, textvariable=self.seed_var, width=8).grid(row=0, column=3, padx=(0, 10))

        self.view_var = tk.StringVar(value="Oberfläche")
        view_box = ttk.Combobox(toolbar, textvariable=self.view_var, values=["Oberfläche", "Diagnose", "Galerie"], state="readonly", width=12)
        view_box.grid(row=0, column=4, padx=(0, 8))
        view_box.bind("<<ComboboxSelected>>", lambda _event: self._change_view())

        self.record_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(toolbar, text="Aufzeichnen", variable=self.record_var, command=self._toggle_recording).grid(row=0, column=5, padx=(0, 4))
        ttk.Button(toolbar, text="Lauf speichern", command=self._save_recording).grid(row=0, column=6, padx=2)
        ttk.Button(toolbar, text="Replay öffnen", command=self._load_replay).grid(row=0, column=7, padx=2)

        self.play_button = ttk.Button(toolbar, text="Start", command=self._toggle_play)
        self.play_button.grid(row=1, column=0, pady=(6, 0), padx=2, sticky="w")
        ttk.Button(toolbar, text="Ein Tick", command=lambda: self._manual_step(1)).grid(row=1, column=1, pady=(6, 0), padx=2, sticky="w")
        ttk.Button(toolbar, text="Reset", command=self._reset).grid(row=1, column=2, pady=(6, 0), padx=2, sticky="w")
        ttk.Label(toolbar, text="Ticks/Bild").grid(row=1, column=3, pady=(6, 0), padx=(8, 4), sticky="e")
        self.speed_var = tk.IntVar(value=1)
        ttk.Scale(toolbar, from_=1, to=12, orient="horizontal", variable=self.speed_var, length=180).grid(row=1, column=4, columnspan=2, pady=(6, 0), sticky="w")

        self.paned = ttk.Panedwindow(self, orient="horizontal")
        self.paned.grid(row=1, column=0, sticky="nsew")
        self.world_frame = ttk.Frame(self.paned)
        self.side_frame = ttk.Frame(self.paned, width=360)
        self.paned.add(self.world_frame, weight=4)
        self.paned.add(self.side_frame, weight=1)

        self.world_canvas = WorldCanvas(self.world_frame, on_select=self._select_agent)
        self.world_canvas.pack(fill="both", expand=True)

        notebook = ttk.Notebook(self.side_frame)
        notebook.pack(fill="both", expand=True, padx=(0, 8), pady=(0, 8))
        self.inspector = tk.Text(notebook, wrap="word", font=("TkFixedFont", 10), padx=8, pady=8)
        self.metrics = tk.Text(notebook, wrap="word", font=("TkFixedFont", 10), padx=8, pady=8)
        self.event_log = tk.Text(notebook, wrap="word", font=("TkFixedFont", 9), padx=8, pady=8)
        notebook.add(self.inspector, text="Agent")
        notebook.add(self.metrics, text="Metriken")
        notebook.add(self.event_log, text="Ereignisse")

        self.bind("<space>", lambda _event: self._toggle_play())
        self.bind("<n>", lambda _event: self._manual_step(1))
        self.bind("<r>", lambda _event: self._reset())
        self.bind("<d>", lambda _event: self._set_view("Diagnose" if self.view_var.get() != "Diagnose" else "Oberfläche"))
        self.protocol("WM_DELETE_WINDOW", self.destroy)

    def _set_text(self, widget: tk.Text, content: str) -> None:
        widget.configure(state="normal")
        widget.delete("1.0", "end")
        widget.insert("1.0", content)
        widget.configure(state="disabled")

    def _load_selected_scenario(self) -> None:
        name = self.scenario_var.get()
        try:
            seed = int(self.seed_var.get())
        except ValueError:
            seed = 1
            self.seed_var.set("1")
        self.playing = False
        self.play_button.configure(text="Start")
        self.controller.load_scenario(self.scenarios[name], seed=seed)
        self.record_var.set(False)
        self.selected_agent = None
        self._render(self.controller.snapshot())

    def _reset(self) -> None:
        try:
            seed = int(self.seed_var.get())
        except ValueError:
            messagebox.showerror("Seed", "Der Seed muss eine ganze Zahl sein.")
            return
        self.playing = False
        self.play_button.configure(text="Start")
        self.controller.reset(seed)
        self.record_var.set(False)
        self._render(self.controller.snapshot())

    def _toggle_play(self) -> None:
        self.playing = not self.playing
        self.play_button.configure(text="Pause" if self.playing else "Start")

    def _manual_step(self, count: int) -> None:
        snapshot = self.controller.step(count)
        self._render(snapshot)

    def _animation_loop(self) -> None:
        if self.playing:
            count = max(1, int(self.speed_var.get()))
            snapshot = self.controller.step(count)
            self._render(snapshot)
        self.after(60, self._animation_loop)

    def _change_view(self) -> None:
        mode = self.view_var.get()
        self.controller.diagnostic = mode == "Diagnose"
        if mode == "Galerie":
            try:
                self.paned.forget(self.side_frame)
            except tk.TclError:
                pass
        else:
            panes = [str(item) for item in self.paned.panes()]
            if str(self.side_frame) not in panes:
                self.paned.add(self.side_frame, weight=1)
        self._render(self.controller.snapshot())

    def _set_view(self, mode: str) -> None:
        self.view_var.set(mode)
        self._change_view()

    def _toggle_recording(self) -> None:
        try:
            self.controller.toggle_recording(self.record_var.get(), interval=1)
        except Exception as exc:
            self.record_var.set(False)
            messagebox.showerror("Aufzeichnung", str(exc))

    def _save_recording(self) -> None:
        if self.controller.recorder is None:
            messagebox.showinfo("Aufzeichnung", "Zuerst »Aufzeichnen« aktivieren und einige Ticks ausführen.")
            return
        target = filedialog.asksaveasfilename(
            title="Lauf speichern",
            defaultextension=".jsonl.gz",
            filetypes=[("Schwarmwelt-Aufzeichnung", "*.jsonl.gz"), ("Alle Dateien", "*.*")],
        )
        if target:
            try:
                self.controller.save_recording(target)
            except Exception as exc:
                messagebox.showerror("Speichern", str(exc))

    def _load_replay(self) -> None:
        source = filedialog.askopenfilename(
            title="Replay öffnen",
            filetypes=[("Schwarmwelt-Aufzeichnung", "*.jsonl.gz"), ("Alle Dateien", "*.*")],
        )
        if source:
            try:
                self.controller.load_replay(source)
                self.playing = False
                self.play_button.configure(text="Start")
                self._render(self.controller.snapshot())
            except Exception as exc:
                messagebox.showerror("Replay", str(exc))

    def _select_agent(self, agent_id: int) -> None:
        self.selected_agent = agent_id
        self.world_canvas.set_selected(agent_id)
        self._render_inspector()

    def _render(self, snapshot: dict[str, Any]) -> None:
        self.world_canvas.update_snapshot(snapshot)
        metrics = snapshot.get("metrics", {})
        lines = [
            f"Tick: {snapshot.get('tick')}",
            f"Begegnungen: {metrics.get('encounters', '–')}",
            f"Turnover: {metrics.get('turnovers', '–')}",
            f"Ø Valenz a: {metrics.get('mean_valence_a', '–')}",
            f"Ø Valenz b: {metrics.get('mean_valence_b', '–')}",
            "",
            "Soziales Gedächtnis:",
            json.dumps(metrics.get("memory", {}), ensure_ascii=False, indent=2),
            "",
            "Häufige sichtbare Folgen:",
        ]
        for sequence, count in metrics.get("frequent_sequences", {}).items():
            lines.append(f"{count:>4}  {sequence}")
        self._set_text(self.metrics, "\n".join(lines))

        event_lines = []
        for event in reversed(snapshot.get("events", [])):
            event_lines.append(f"[{event.get('tick'):>6}] {event.get('text')}")
        self._set_text(self.event_log, "\n".join(event_lines))
        self._render_inspector()

    def _render_inspector(self) -> None:
        if self.selected_agent is None:
            self._set_text(self.inspector, "Agent anklicken, um seine sichtbaren Daten und – im Diagnosemodus – verborgenen Zustände zu prüfen.")
            return
        try:
            details = self.controller.agent_details(self.selected_agent)
        except Exception as exc:
            details = {"Fehler": str(exc)}
        self._set_text(self.inspector, json.dumps(details, ensure_ascii=False, indent=2))
