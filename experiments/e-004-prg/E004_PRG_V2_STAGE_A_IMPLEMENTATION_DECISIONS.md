# E-004-PRG v2 — result-sensitive Implementierungsfestlegungen für Stufe A

**Status:** technischer Freeze-Kandidat; vor der ersten formalen Kontrollauswertung extern zu prüfen  
**Datum:** 2026-07-08  
**Stufe A ausgeführt:** nein  
**BIND-Werte aus realen Trajektorien berechnet:** nein  
**Stufe B:** weiterhin gesperrt

## 1. Zweck dieses Dokuments

Die eingefrorene Stufe-A-Spezifikation legt Mechanismus, Kontrollen und Gates fest,
aber nicht jede algorithmische Einzelentscheidung. Dieses Dokument macht alle
resultatsensitiven Konkretisierungen vor Kenntnis eines realen BIND-Werts explizit.
Eine Änderung nach externer Freigabe hebt den technischen Implementierungsfreeze auf.

## 2. Rekonstruktion des Ereignistapes

Für jede der neun archivierten Trajektorien wird die eingefrorene Numba-Engine
noch einmal ausgeführt. Die Instrumentierung schreibt zusätzlich, ohne Rückwirkung:

- Basislogits ohne numerische Dauerzellen,
- den fünfdimensionalen Vektor der aktuell lesbaren Dauerzellbeiträge,
- Zell-ID und Zellgeneration je Handlungsadresse,
- Puls, Zellfamilie und den bereits verbrauchten originalen Handlungszufallswert.

Die Basislogits enthalten private Policy und temporäre soziale Spuren. Der
Dauerzellvektor enthält ausschließlich die aktuell policywirksamen numerischen
Dauerzellen. Bei E-003-D2 wird eine Zelle bei nicht passendem Link als nicht lesbar
behandelt und mit Beitrag null in den Shadow-Tape geschrieben.

Eine Abfrage besteht immer aus genau den fünf Handlungsadressen derselben
Agenten-, Zellfamilien- und Kontextabfrage. ADDRESS-SHAM permutiert nur innerhalb
dieser Abfrage; Familien, Agenten, Kontext, Lebenszeit und Beitragsmasse bleiben fest.

## 3. Zellidentität und Lebenszeit

Es gibt 2.400 feste Zellslots:

- Sequenzzellen: Agent × vorheriges Partnersymbol × Handlung,
- Kontextzellen: Agent × inferierter Partnerzustand × Handlung,
- Valenzzellen: Agent × Handlung.

Eine Generation wird beim Übergang eines numerischen Zellwerts von null zu
ungleich null erhöht. Der zugehörige `r`-Wert wird beim ersten späteren Lesen einer
neuen Generation auf null gesetzt. Pruning und Turnover entfernen die numerische
Zelle; ein verbliebener Shadow-Wert kann bis zur nächsten Geburt nicht wirken und
wird bei dieser Geburt über den Generationswechsel gelöscht.

Aktiv für Policy, Score und Wirksamkeitszählung ist eine Adresse genau dann, wenn
`|d| > 1e-15`. Nicht lesbare D2-Zellen und numerisch leere Zellen sind inaktiv.

## 4. PRG-Policy

Für jede aktive Adresse `s`:

`m_s = 1 + 0,5 r_s`, mit `r_s ∈ [-1,1]`.

Der gewichtete Dauerzellvektor wird anschließend mit einem gemeinsamen Faktor
so normiert, dass seine L1-Masse exakt der L1-Masse des ungewichteten
Dauerzellvektors entspricht. Der so gewichtete Vektor geht mit dem bereits
gefrorenen Faktor `0,80 / 3` in die Policylogits ein.

Bei `r=0` ist der Dauerzellvektor bitgleich unverändert. Leere Dauerzellvektoren
bleiben leer; es wird kein künstlicher Beitrag erzeugt.

## 5. Score und Aktualisierung

Für jede aktive Adresse `s`:

`z_s = sign(d_s) [1(A=s) − p_s]`.

Aktualisierung:

`r_s ← clip((1−0,025) r_s + 0,025 z_s, −1, 1)`.

### 5.1 BIND

Die archivierte Handlung wird unter der eigenen BIND-Policy bewertet und erzeugt
auch das Update des zu ihrer Zellidentität gehörenden `r`.

### 5.2 ACTION-PLACEBO

Die archivierte Handlung wird nur für Log-Score und A3-Zielwert bewertet. Das
Update entsteht aus einer unabhängig gezogenen Pseudo-Handlung derselben
Placebo-Policy. Der vor dem Ereignis vorhandene Placebo-`r`-Wert ist der A3-Regressor;
der A3-Zielwert ist der Score der archivierten Handlung unter der Placebo-Policy.
Damit prüft A3 Vorhersage der real beobachteten Handlung, während die
Placebo-Selbstverstärkung ausschließlich durch die Pseudo-Handlung fortgeschrieben wird.

### 5.3 ADDRESS-SHAM

Vor der Policyabfrage werden die vorhandenen `r`-Werte der aktiven Adressen
zyklisch derangiert. Die Reihenfolge wird je Replikation und Ereignis durch
unabhängige Zufallsprioritäten bestimmt; bei mindestens zwei aktiven Adressen
ändert jede Identitätszuordnung ihr Ziel. Das Update aus der archivierten Handlung
wird danach auf die wahre Zellidentität geschrieben. Für A3 ist der vor der
Handlung abgefragte, permutiert zugewiesene `r`-Wert der Regressor.

Die Wirksamkeit wird nicht nur als Identitätswechsel gezählt. Eine Zuordnung gilt
für das 40%-Gate erst dann als effektiv verändert, wenn sich der numerische
`r`-Wert um mehr als `1e-15` ändert. Das 60%-Massengate verwendet die L1-Masse der
Abfragen mit mindestens zwei aktiven Adressen.

## 6. Zufallsströme

Alle neuen Zufallszahlen werden durch einen stateless Counter-RNG auf Basis von
SplitMix64 erzeugt. Schlüssel sind:

- gehashter Namensraum,
- Replikationsindex,
- Ereignisindex,
- typisierte Lane.

Damit hängt kein Ergebnis von Schleifenabbruch, Threadplanung oder vorherigem
Zufallsverbrauch ab. Verwendete Namensräume:

- `prg_placebo_actions`,
- `prg_address_permutations`,
- `synthetic-placebo-fidelity`,
- getrennte Namensräume für Monte-Carlo- und Seed-Paarungen.

Die numerischen Namespace-Seeds werden in den Ausgabemanifesten gespeichert.

## 7. Kontrollinterne Nullverteilung

Für 999 Kontrollreplikationen wird je Ereignis der exakte Median der jeweils
anderen 998 Replikationen verwendet. Dafür genügen die Ordnungsstatistiken 499,
500 und 501 der vollständigen 999 Werte. Sie werden deterministisch per Partition
bestimmt; die Tie-Behandlung entspricht exakt `median(delete(values, j))`.

Die technische Prüfung umfasst 4.060 direkte Vergleiche einschließlich starker
Bindungsfälle und besteht bitgleich.

Das 97,5%-Quantil wird konservativ mit NumPy `method="higher"` bestimmt. Die
Schwelle ist der Maximalwert der drei primären Seed-Quantile.

## 8. Seed-Paarung und gepoolte Monte-Carlo-Werte

Seed 1086 dient als Referenzreihenfolge. Für 1047 und 1031 werden zwei vorab aus
dem Kontrollnamensraum erzeugte, feste Permutationen der 999 Replikationsindizes
verwendet. Dieselben Paarungen gelten für AP, AS und A3. Gepoolt wird stets mit
der Zahl der Ereignisse je Seed als Gewicht.

Der einseitige Monte-Carlo-Wert lautet:

`p = (1 + Anzahl[Nullwert ≥ Beobachtung]) / 1000`.

## 9. A3-Konkretisierung

Die gewichtete lineare Steigung wird aus den Summen
`Σw, Σwr, Σwz, Σwr², Σwrz` berechnet; `w=|d|`. Es gibt keinen Interaktions-,
Nichtlinearitäts- oder Regularisierungsterm.

A3 besteht nur, wenn:

- BIND in mindestens zwei Primärseeds positive Steigung hat,
- BIND in mindestens zwei Primärseeds die mediane AP-Steigung übertrifft,
- BIND in mindestens zwei Primärseeds die mediane AS-Steigung übertrifft,
- beide gepoolten einseitigen Monte-Carlo-Werte höchstens 0,025 sind.

AUC und Quartiltrennung sind in diesem Kandidaten nicht implementiert, weil sie
laut Freeze rein diagnostisch und nicht admission-relevant sind. Sie dürfen vor
der formalen Ausführung ergänzt werden, sofern Definition und Code vorher extern
geprüft und gehasht werden; andernfalls werden sie nicht nachträglich berechnet.

## 10. Replikationsgate

Für die sechs D2-Trajektorien werden A1 und A2 separat geprüft. Bestehen verlangt:

- beide gepoolten Mittelwerte positiv,
- je Vergleich mindestens vier von sechs Einzeltrajektorien positiv,
- für beide Vergleiche einen positiven Mittelwert innerhalb D2-BIND,
- für beide Vergleiche einen positiven Mittelwert innerhalb D2-SHAM.

Die Primärschwellen werden nicht aus D2-Daten neu bestimmt.

## 11. Trennung von Kontroll- und BIND-Lauf

`run_stage_a_controls.py` kann ausschließlich Kontrollprozesse berechnen. Es
schreibt anschließend `STAGE_A_NULL_THRESHOLDS.json` und einen Hash-Sidecar mit
`bind_values_computed=false`.

`run_stage_a_bind.py` verweigert die Ausführung, wenn:

- der Schwellen-Hash nicht stimmt,
- Implementierungs-, Tape- oder Kontrollmanifest verändert wurden,
- ein Kontrollfile nicht seinem Manifest entspricht,
- Replay, technisches Fidelity-Gate oder ADDRESS-SHAM-Gate nicht bestanden sind.

Ein synthetischer Pipeline-Selbsttest bestätigt, dass ein nachträglich verändertes
Schwellenfile zurückgewiesen wird und der Schwellenhash während der BIND-Auswertung
unverändert bleibt.

## 12. Replay-Reichweite und verbleibende Grenze

Für alle neun Trajektorien reproduzieren sowohl die unveränderte eingefrorene
Engine als auch die instrumentierte Numba-Engine alle 21 archivierten
Ereignisfelder bitgenau. Für E-003-D2 stimmen zusätzlich die archivierten
Endzählungen aktiver, verlinkter, verwaister und ungültiger Zellen exakt.

Die Archive enthalten jedoch keine vollständigen historischen Snapshots jeder
numerischen Dauerzelle. Für E-002R kann daher die interne Zelltrajektorie nicht
gegen ein unabhängig archiviertes Zellarray verglichen werden. Ihre Rekonstruktion
ist durch die bitgenaue Reproduktion der gesamten handlungs- und zustandswirksamen
Ereignisfolge, die unveränderte eingefrorene Numba-Engine und die getrennt gehashte
write-only Instrumentierung abgesichert. Dieser Punkt darf nicht als Vergleich
mit nicht vorhandenen internen Archivsnapshots dargestellt werden.

## 13. Nicht Gegenstand dieses Freeze-Kandidaten

- keine reale Kontroll-Nullverteilung,
- keine reale Schwellenbestimmung,
- kein realer BIND-Wert,
- keine Admission-Entscheidung,
- keine Stufe-B-Ausführung,
- keine Lösung der r-Kanal-/M7-Reservation,
- kein Holdout-Zugriff.
