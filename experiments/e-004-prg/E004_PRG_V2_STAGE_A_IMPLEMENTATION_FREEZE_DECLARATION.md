# E-004-PRG v2 — technischer Implementierungsfreeze Stufe A

**Datum:** 2026-07-08  
**Status:** FROZEN  
**Externe Freigabe:** Support with reservations  
**Reale BIND-Werte beim Freeze:** keine  
**Kernläufe:** 0  
**Budget:** 39/60  
**Holdout:** geschlossen  
**Stufe B:** gesperrt

## Eingefrorener Bestand

Eingefroren werden:

- unveränderte E-002R- und E-003-D2-Engines und Quellen,
- instrumentierte Numba-Replay- und Tape-Engine,
- PRG-BIND-, ACTION-PLACEBO- und ADDRESS-SHAM-Shadow-Code,
- getrennte Kontroll- und BIND-Runner,
- resultatsensitive Implementierungsfestlegungen,
- technische Testresultate,
- Eingabe-, Implementierungs- und Umgebungsmanifeste.

## Zulässiger nächster Schritt

Nach diesem Freeze ist ausschließlich zulässig:

1. die neun instrumentierten Tapes zu erzeugen und zu hashen,
2. je Trajektorie 999 ACTION-PLACEBO- und 999 ADDRESS-SHAM-Kontrollen auszuführen,
3. `tau_AP` und `tau_AS` kontrollintern zu bestimmen,
4. Threshold- und Kontrollbestand unverändert zu archivieren.

Bis dahin und währenddessen darf kein realer BIND-Wert berechnet werden.

## Verbleibende Sperren

- Vor BIND-Befundwertung: unabhängige echte Numba-Prüfumgebung bereitstellen und hashen.
- Vor Stufe B: r-Kanal-/M7-Reservation extern klären und einfrieren.
- Kein Holdout-Zugriff.
