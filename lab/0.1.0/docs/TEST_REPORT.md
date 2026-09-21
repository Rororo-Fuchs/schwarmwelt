# Testbericht 0.1.0

## Automatisierte Tests

Ausgeführt mit:

```text
PYTHONPATH=src python -m unittest discover -s tests -v
```

Geprüft wurden:

- deterministische Wiederholung desselben Seeds,
- Trennung von Oberflächen- und Diagnosesnapshot,
- Austausch des Sozialgedächtnisses ausschließlich über Konfiguration,
- Ausschluss von Ground Truth aus `ObservableContext`,
- Recording-/Replay-Roundtrip,
- Turnover und Reset eines Agenten,
- Startfähigkeit aller mitgelieferten Szenarien.

Ergebnis: **7/7 Tests bestanden**.

## GUI-Smoke-Test

Die Tkinter-Anwendung wurde in einer virtuellen X11-Umgebung gestartet, zwölf Ticks ausgeführt und als Screenshot erfasst. Dabei traten keine Start- oder Renderfehler auf.

## Leistungsprüfung

Auf der Ausführungsumgebung benötigten 1.000 Ticks der Baseline mit 48 Agenten ungefähr 4,7 Sekunden im Headless-Betrieb. Die GUI begrenzt die Geschwindigkeit deshalb auf zwölf Ticks pro Bild.

## Noch nicht getestet

- lange Mehrstundenläufe,
- Windows-spezifisches Tkinter-Verhalten auf dem Zielrechner,
- numerische Übereinstimmung mit dem früheren Numba-Batchmodell,
- wissenschaftliche Aussagekraft des experimentellen Sozialgedächtnisses,
- externe Drittanbieter-Plugins jenseits des Ladevorgangs.
