# E-004-PRG v2 — Stufe-A-Kontrolllock

**Datum:** 2026-07-08  
**Status:** CONTROL-ONLY LOCKED  
**BIND ausgeführt:** nein  
**Admission entschieden:** nein  
**Budget:** 39/60  
**Holdout:** geschlossen  
**Stufe B:** gesperrt

## Ausgeführter Umfang

- neun instrumentierte Tapes bitgenau aus den eingefrorenen Quellen erzeugt,
- je Trajektorie 999 ACTION-PLACEBO-Kontrollen,
- je Trajektorie 999 ADDRESS-SHAM-Kontrollen,
- alle formalen ADDRESS-SHAM-Wirksamkeitsgates bestanden,
- Schwellen ausschließlich aus den drei primären E-002R-C2-Kontrollnullen bestimmt,
- Threshold-File und vollständiger Kontrollbestand gehasht gesperrt.

## Fixierte Schwellen

- `tau_AP = 8.143114595001919e-05` Bit/Ereignis,
- `tau_AS = 8.514540963067646e-05` Bit/Ereignis.

Quantil: 97,5 %, Methode `higher`, absoluter Leave-one-out-Kontrollwert,
Maximum über die drei Seeds.

## Harte Grenze

`bind_values_computed` ist im gehashten Threshold-File `false`. Es wurde weder
ein realer BIND-Wert berechnet noch eine Admission-Entscheidung getroffen.

Vor BIND ist die separat bereitgestellte echte Numba-Prüfumgebung extern auf
Installierbarkeit und Nopython-Ausführung zu prüfen. Ein späterer BIND-Befund gilt
erst nach unabhängiger Reproduktion.
