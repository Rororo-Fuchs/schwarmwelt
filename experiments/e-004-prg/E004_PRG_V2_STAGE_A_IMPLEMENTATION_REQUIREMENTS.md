# E-004-PRG v2 — Anforderungen an die Stufe-A-Implementierung

**Status:** verbindlich vor der ersten Stufe-A-Ausführung

## 1. Implementierungsumfang

Zulässig ist ausschließlich die Implementierung der eingefrorenen
Stufe-A-Diagnose einschließlich Replay-, Nullschwellen-, Placebo-Fidelitäts- und
Integritätsgates. Keine Online-Kernbedingung darf ausgeführt werden.

## 2. Reproduzierbarkeit

Vor jeder inhaltlichen Ausgabe müssen vorliegen und gehasht werden:

- vollständiger Quellcode,
- Eingabemanifest aller archivierten Trajektorien,
- Python-, NumPy-, Numba- und llvmlite-Version,
- Betriebssystem-, CPU- und Numba-Systeminformationen,
- RNG-Namensräume und Seeds,
- Replay-Prüfbericht.

Die Prüfumgebung muss echtes Numba enthalten. Ein Python-Fallback gilt nicht als
unabhängige bit-exakte Reproduktion.

## 3. Reihenfolge

1. Code und Umgebung einfrieren.
2. Bit-exakten Replay aller verwendeten Trajektorien bestätigen.
3. Synthetische Placebo-Fidelität und ADDRESS-SHAM-Wirksamkeit prüfen.
4. Ausschließlich Kontroll-Nullverteilungen berechnen.
5. `STAGE_A_NULL_THRESHOLDS.json` schreiben und hashen.
6. Erst danach BIND-Werte freischalten.
7. Automatische Admission-Entscheidung erzeugen.

## 4. Verbotene Änderungen

Nach Anzeige eines BIND-Werts dürfen insbesondere nicht geändert werden:

- Lernrate oder r-Grenzen,
- Multiplikator oder Massennormalisierung,
- Kontrollstrata,
- Zahl der Replikationen,
- Quantilregel,
- Ereignisgewichtung,
- A1/A2/A3-Gates,
- Replay-Toleranz.

## 5. Folgeentscheidung

Ein Bestehen von Stufe A erlaubt nur die Bearbeitung der offenen
r-Kanal-/M7-Reservation. Es ist noch keine Freigabe für Stufe B.
