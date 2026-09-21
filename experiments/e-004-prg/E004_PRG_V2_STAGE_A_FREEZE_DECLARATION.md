# E-004-PRG v2 — Freeze-Erklärung Stufe A

**Freeze-Datum:** 2026-07-08  
**Freeze-Gegenstand:** ausschließlich Stufe-A-Diagnose  
**Externe Freigabe:** Support with reservations; Stufe A freezefähig und implementierbar  
**Implementierung:** noch nicht begonnen  
**Stufe A:** noch nicht ausgeführt  
**Kernläufe:** 0  
**Budget:** 39/60  
**Holdout:** geschlossen

## Eingefroren

- Datenbasis und veröffentlichte Seeds,
- bit-exaktes Replay-Gate mit echtem Numba,
- PRG-BIND-, ACTION-PLACEBO- und ADDRESS-SHAM-Shadow-Prozesse,
- 999 Kontrollreplikationen je Kontrollfamilie,
- kontrollinterne Leave-one-out-Nullschwellen,
- Hash-Reihenfolge vor Freischaltung der BIND-Auswertung,
- A1-, A2- und A3-Gates,
- synthetisches exogenes Placebo-Fidelitäts-Harness,
- Replikationsregeln,
- automatische Admission-Entscheidung,
- Interpretation von Stufe A ausschließlich als Admission-Screen.

## Nicht eingefroren oder freigegeben

- Ausführung einer Online-E-004-Kernbedingung,
- endgültige Stufe-B-M7-Regel,
- Behandlung der r-Kanal-/M7-Initialkorrelationsreservation,
- jede Holdout-Auswertung.

## Änderungsregel

Jede Änderung an einem eingefrorenen Stufe-A-Bestandteil hebt diesen Freeze auf
und verlangt vor Ausführung eine neue externe Prüfung. Die Schließung der
Stufe-B-Reservation darf den eingefrorenen Stufe-A-Mechanismus nicht nachträglich
an ein beobachtetes Stufe-A-Ergebnis anpassen.
