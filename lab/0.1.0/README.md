# Schwarmwelt Labor 0.1.0

Lokale Visualisierungs- und Experimentierumgebung für das künstlerische Multi-Agenten-Projekt **Schwarmwelt**.

## Status

Dies ist eine **lauffähige erste Laborversion** mit 48 Agenten, vier durchlässigen Zonen, intrinsischer zweidimensionaler Valenz, metrikfreien Symbolen, privaten paarbezogenen Zustandsschätzungen, mehrpulsigen Begegnungen, Ritualfolgen, Turnover, Diagnoseansicht, Aufzeichnung und Replay.

Die Software ist **keine numerisch identische Portierung** des zuvor getesteten Numba-Batchmodells. Sie rekonstruiert dessen entscheidende Architektur als schrittweise Simulation. Bevor Ergebnisse aus dieser Anwendung als Forschungsbefunde verwendet werden, muss die neue Engine in einer eigenen Kontrollserie kalibriert und getestet werden.

## Start

### Windows

`start_windows.bat` doppelklicken.

Alternativ im Terminal:

```text
py run.py
```

### Linux

```text
./start_linux.sh
```

oder:

```text
python3 run.py
```

Die erste Version benötigt nur Python 3.11+ mit Tkinter. Es müssen keine zusätzlichen Python-Pakete installiert werden.

## Bedienung

- **Start/Pause**: Simulation laufen lassen
- **Ein Tick**: kontrollierter Einzelschritt
- **Ticks/Bild**: Geschwindigkeit
- **Oberfläche**: nur sichtbare Positionen, Symbole und Folgen
- **Diagnose**: zusätzlich Valenzfarben, private Schätzungen und Decoy-Zustände
- **Galerie**: reduzierte Weltansicht ohne Seitenpanel
- **Aufzeichnen / Speichern**: einen Lauf als komprimiertes JSONL-Replay sichern
- **Replay öffnen**: eine Aufzeichnung unabhängig von der Simulation wiedergeben
- Agent anklicken: Detailansicht öffnen

Tastatur:

- Leertaste: Start/Pause
- `N`: ein Tick
- `R`: Reset
- `D`: Oberfläche/Diagnose wechseln

## Mitgelieferte Szenarien

- `ritual_baseline`: zustandsgebundene Rituale ohne Gruppengedächtnis
- `social_memory_trace`: experimentelles verteiltes Sozialgedächtnis
- `sequence_imitation_control`: sichtbare Sequenzimitation
- `no_sequence_control`: Zustand ohne sichtbare Sequenz
- `full_mixing_control`: vollständige geografische Durchmischung

## Headless-Betrieb

```text
python run_headless.py scenarios/ritual_baseline.json --ticks 2000 --seed 23
```

Mit Aufzeichnung:

```text
python run_headless.py scenarios/social_memory_trace.json --ticks 2000 --record lauf.jsonl.gz
```

## Erweiterung

Parameter und vorhandene Module werden ausschließlich in den JSON-Szenarien kombiniert. Neue Mechanismen können als einzelne Python-Datei in `plugins/` ergänzt werden. Der Simulationskern und die Oberfläche müssen dafür nicht umgebaut werden.

Siehe:

- `ARCHITECTURE_DE.md`
- `EXTENDING_DE.md`
- `DESIGN_DECISIONS_DE.md`
- `MODEL_STATUS_DE.md`

## Szenario-/Seed-Matrix

```text
python run_matrix.py --ticks 1000 --seeds 20,21,22
```

Der Runner schreibt Prozesskennzahlen und deterministische Digests in `matrix_results.csv`. Er ist eine technische Regressionshilfe, keine Kulturmetrik.

## Beispielaufzeichnung und Screenshots

- `example_run.jsonl.gz` kann über **Replay öffnen** geladen werden.
- `SCREENSHOT.png` zeigt die Oberflächenansicht.
- `SCREENSHOT_DIAGNOSTIC.png` zeigt die Diagnoseansicht mit ausgewähltem Agenten.
