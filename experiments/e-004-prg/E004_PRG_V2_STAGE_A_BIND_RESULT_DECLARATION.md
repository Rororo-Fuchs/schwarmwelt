# E-004-PRG v2 — Stufe-A-BIND-Ergebnis

**Datum:** 2026-07-08  
**Status:** BIND-Auswertung ausgeführt; externe Reproduktion ausstehend.  
**Stufe B:** nicht autorisiert und weiterhin gesperrt.

## 1. Ergebnis

Die Stufe-A-Admission wurde nicht bestanden.

- `stage_a_pass`: `false`
- `E004_core_admission`: `false`
- `stage_b_authorized`: `false`

Damit ist der E-004-Kernblock nicht freigegeben. Ein Stufe-A-Positivbefund liegt nicht vor.

## 2. Primärgates

| Gate | Wert | p-Wert | Status |
|---|---:|---:|---|
| A1 gegen ACTION-PLACEBO | `4.034598104170218077e-05` | `0.233` | failed |
| A2 gegen ADDRESS-SHAM | `3.827772573841001420e-05` | `0.726` | failed |
| A3 gegen AP | `-6.535428657997409407e-02` | `0.181` | failed |
| A3 gegen AS | `-6.535428657997409407e-02` | `0.804` | failed |

Schwellen:

- `tau_AP`: `8.143114595001918737e-05`
- `tau_AS`: `8.514540963067646431e-05`

## 3. Seedwerte

### A1 — Δ gegenüber ACTION-PLACEBO

| Seed | Δ_AP | Seed-Schwelle bestanden |
|---:|---:|---|
| 1031 | `3.197659199985283265e-05` | `false` |
| 1047 | `1.368497015399428782e-05` | `false` |
| 1086 | `7.537638097125942693e-05` | `false` |

### A2 — Δ gegenüber ADDRESS-SHAM

| Seed | Δ_AS | Seed-Schwelle bestanden |
|---:|---:|---|
| 1031 | `1.610375834762385467e-05` | `false` |
| 1047 | `2.218231824923317527e-05` | `false` |
| 1086 | `7.654710061837301943e-05` | `false` |

## 4. Replikationsdiagnostik

- `replication.pass`: `false`
- A1 positive Trajektorien: `2`
- A2 positive Trajektorien: `2`
- A1 D2-BIND mean positive: `false`
- A1 D2-SHAM mean positive: `true`
- A2 D2-BIND mean positive: `false`
- A2 D2-SHAM mean positive: `true`

## 5. Reproduktion

Die BIND-Auswertung wurde einmal in CPython 3.13.5 und einmal in CPython 3.12.13 ausgeführt. Beide Ergebnisdateien sind byte-identisch.

- `STAGE_A_RESULT.json` SHA-256: `b89e4c98f862a19688e8d1c7fb0ff562d5485456db08acdde9575a0ae0fc7957`
- `STAGE_A_RESULT_CP312.json` SHA-256: `b89e4c98f862a19688e8d1c7fb0ff562d5485456db08acdde9575a0ae0fc7957`
- Byte-identisch: `true`

## 6. Verfahrensgrenze

Diese Auswertung erzeugt keine Stufe-B-Freigabe. Auch ein bestandener Stage-A-Lauf hätte die r-Kanal/M7-Reservation nicht aufgehoben; im tatsächlichen Ergebnis entfällt der Kernblock bereits an Stufe A.

Bis zur externen Reproduktion ist der Befund als reproduktionsbereit, aber noch nicht unabhängig bestätigt zu führen.
