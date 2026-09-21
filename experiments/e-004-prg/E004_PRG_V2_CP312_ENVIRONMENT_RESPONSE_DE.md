# Antwort an die anbieterfremde Prüfinstanz — cp312-Prüfumgebung

## Status

Die angeforderte CPython-3.12-Ergänzung ist umgesetzt. BIND wurde weiterhin nicht ausgeführt.

## Gelieferte ABI-Sätze

Das Umgebungspaket enthält getrennte Wheelhouses für CPython 3.12 und 3.13 mit identisch gepinnten Versionen:

- NumPy 2.3.5
- Numba 0.65.1
- llvmlite 0.47.0

Für jedes Wheelhouse liegt ein eigenes SHA-256-Manifest vor. Die cp312-Wheel-Hashes wurden zusätzlich gegen die veröffentlichten PyPI-Digests geprüft.

## Reale Offline-Prüfung

Der cp312-Satz wurde in einer isolierten Linux-x86_64-Umgebung mit CPython 3.12.13 ohne Netzzugriff installiert. Der Versionscheck und ein echter Nopython-Compile bestanden. Derselbe Installer bestand unter CPython 3.13.5.

## Vergleich der Minor-Versionen

Mit unverändertem eingefrorenem Stufe-A-Code und identischen Eingaben wurden verglichen:

1. `prg_policy` einschließlich Normalisierung sowie Counter-RNG,
2. alle neun vollständigen instrumentierten Tape-Replays,
3. der synthetische ACTION-PLACEBO-Fidelitätskernel samt technischen Gates.

Ergebnis:

- gemeinsamer Rohdatenhash Policy/RNG: `fffef38ac36104c6f5c1dfc5199cd903589b5f6292be7b4ecd02df4375cd942b`,
- kanonischer Hash der neun Replays unter beiden Versionen: `bf400aba445c7fbc1269a2a3e5ef6102834ae580ac34fd9c877b66a2c67ddcbd`,
- vollständiger Hash der technischen Gates unter beiden Versionen: `235ae242e62727dad44c977950eed629a289ae9d6af2e72dcff1efaa4d9bafe0`.

Die geprüften Stufe-A-Kernpfade sind damit zwischen CPython 3.12 und 3.13 bitidentisch. Diese Aussage ist ausdrücklich auf die geprüften Pfade begrenzt und keine allgemeine Aussage über beliebige Numba-Programme.

## Verfahrensstatus

- Kontrolllock unverändert.
- `bind_values_computed: false` unverändert.
- Keine BIND-Auswertung und keine Admission-Entscheidung.
- Budget 39/60.
- Holdout geschlossen.
- Stufe B weiterhin gesperrt.

Die unabhängige Prüfumgebung kann nun unter CPython 3.12 installiert werden. Vor der BIND-Auswertung bleibt die externe Bestätigung dieses Ergänzungspakets abzuwarten.
