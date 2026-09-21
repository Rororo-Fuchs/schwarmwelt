# Externer Prüfvermerk — E-004-PRG v2 Stufe-A-Implementierung

**Datum:** 2026-07-08  
**Prüfinstanz:** anbieterfremde Prüfinstanz  
**Gegenstand:** Technischer Implementierungsfreeze Stufe A

## Verdikt

**Support with reservations.** Technischer Freeze und Kontrollauswertung sind freigegeben. Die verbleibende Reservation betrifft ausschließlich die spätere BIND-Auswertung: Vor ihrer Befundwertung muss die unabhängige Prüfumgebung die numba-kompilierten Pfade mit der gehashten Umgebung reproduzieren können.

## Verifizierte Punkte

- Manifest-Selbsthash konsistent.
- `quantile_higher` bit-identisch zu NumPy `method="higher"`.
- Leave-one-out-Median bei n=999 unabhängig geprüft.
- ACTION-PLACEBO trennt archivierte reale Handlung für A3 und Pseudohandlung für das r-Update korrekt.
- Kontrollrunner enthält keinen BIND-Pfad; Threshold-File setzt `bind_values_computed: false` und ist hashgesperrt.
- Replay-Nachweis ist angesichts nicht archivierter interner Zellarrays angemessen und nicht überdehnt.
- ADDRESS-SHAM- und Placebo-Fidelitätsgates bestehen.
- Die r-Kanal-/M7-Reservation bleibt korrekt als harter Stufe-B-Blocker geführt.

## Freigabegrenze

Freigegeben sind:

1. technischer Implementierungsfreeze,
2. instrumentierte Tape-Erzeugung,
3. ausschließlich Kontrollauswertung,
4. Fixierung und Hashing von `tau_AP` und `tau_AS`.

Nicht freigegeben ist die Befundwertung einer BIND-Auswertung ohne zuvor bereitgestellte und gehashte echte Numba-Prüfumgebung.
