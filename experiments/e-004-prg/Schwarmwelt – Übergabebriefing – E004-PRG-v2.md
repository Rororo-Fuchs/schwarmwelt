# Übergabebriefing: Schwarmwelt / Künstliche Gesellschaften

**Übergabestand:** E-004-PRG v2 entworfen, vor externer Freeze-Prüfung  
**Datum:** 8. Juli 2026  
**Budgetstand:** 39 von 60 Kernläufen verbraucht  
**Holdout:** geschlossen  
**Nächste zulässige Aktion:** Rückmeldung der anbieterfremden Prüfinstanz zu E-004-PRG v2 auswerten

---

## 1. Zweck dieser Übergabe

Dieser Text soll einen neuen Hauptchat in die Lage versetzen, die methodisch kontrollierte Schwarmwelt-Forschung ohne Rückgriff auf den alten Chat fortzuführen.

Der neue Chat soll zunächst:

1. dieses Briefing und die beigefügten Pakete lesen,
2. den unten festgehaltenen Status als verbindlichen Arbeitsstand übernehmen,
3. anschließend die vom Nutzer eingebrachte Rückmeldung von Claude zu E-004-PRG v2 prüfen,
4. vor einer ausdrücklichen Freeze-Freigabe weder Stufe A implementieren noch einen Kernlauf starten.

Fragen des Nutzers sind nicht automatisch Änderungsaufträge. Architektur, Code oder Versuchstexte werden nur verändert, wenn dies ausdrücklich verlangt wird oder unmittelbar aus einem übermittelten Prüfbriefing folgt.

---

## 2. Forschungsfrage

Das Projekt untersucht, unter welchen Bedingungen künstliche Agentensysteme proto-kulturelles Verhalten ausbilden können.

Gesucht werden nicht menschliche Stile oder symbolische Bedeutungen, sondern minimale Bedingungen für:

- sozial übertragene Praktiken,
- gruppenspezifische Unterschiede,
- zustandsabhängige Handlungen,
- intrinsische Bewertung,
- Persistenz über Agentenwechsel,
- Rekonstruktion durch neue Gruppenmitglieder.

Ein sichtbares gruppenspezifisches Sequenzmuster allein gilt nicht als Protokultur-Kandidat. Erforderlich ist eine sozial rekonstruierbare Verbindung zwischen:

- geschätztem innerem Zustand,
- sichtbarer Praxis,
- intrinsischer Bewertung.

---

## 3. Innere Zustände

Jeder Agent besitzt zwei kontinuierliche intrinsische Dimensionen:

1. Valenz im engeren Sinn: negativ/aversiv bis positiv/attraktiv
2. Aktivierung beziehungsweise Erregung: niedrig bis hoch

Für die soziale Inferenz werden beide Dimensionen zu vier groben Zuständen kombiniert.

Andere Agenten erhalten keinen Ground-Truth-Zugriff. Sie können den Zustand nur aus bedeutungslosen sichtbaren Symbolen fehlbar erschließen.

Ein kausal wirkungsloser Decoy-Zustand dient als Kontrolle.

Terminologisch ist künftig sauber zu unterscheiden:

- **Valenz** = eine intrinsische Dimension,
- **Aktivierung/Erregung** = zweite intrinsische Dimension,
- **intrinsischer Zustand** = Oberbegriff,
- **geschätzter Zustand** = private Inferenz eines anderen Agenten.

---

## 4. Verbindliche Methodik

Das Vorabprotokoll v1.2.0 und die technische Kalibrierung sind eingefroren.

Verbindlich gelten:

- Vorabprotokoll vor Code und Lauf,
- klare Trennung von Exploration und Bestätigung,
- festgelegte Metriken, Schwellen, Seeds, Budgets und Abbruchregeln,
- gleiche-Lauf-, Decoy-, Identity- und Sham-Kontrollen,
- getrennte reproduzierbare Zufallsströme,
- automatische Gates,
- vollständige Persistenz aller Fehlversuche,
- append-only Amendments statt Überschreiben historischer Freeze-Dateien,
- keine Holdout-Reparatur,
- unabhängige Prüfung vor Interpretation,
- Sprache erklärt die automatische Entscheidung, erzeugt sie aber nicht.

Bei einem möglichen Positivbefund ist eine unabhängige bit-exakte Reproduktion mit echtem Numba erforderlich. Ein Python-Fallback genügt dafür nicht.

---

## 5. Eingefrorene Metriken

Zentral sind:

- **M1:** echter Zustand erklärt Ausdruck besser als Decoy
- **M2:** private Einschätzung verfolgt echten Zustand besser als Decoy
- **M3:** Einschätzung beeinflusst Handlung zusätzlich zur sichtbaren Vorgeschichte
- **M4:** rekonstruierter Kontext liefert zusätzlichen Vorhersagegewinn
- **M5:** Newcomer übernimmt zustandsgebundene Gruppenpraxis
- **M6:** Praxis bleibt nach Entfernung ursprünglicher Träger erhalten
- **M7:** zustandsgebundene Gruppendivergenz übertrifft sichtbare Tradition und Kontrollen
- **M8:** Effekt bleibt von stabiler Identität beziehungsweise Dyadenkontinuität unabhängig
- **M9:** echte ereignisspezifische Valenzbindung übertrifft falsch gebundene Kontrolle
- **M10:** Topologieeinordnung

Wichtige technische Schwellen:

- M1: 0,001 Bit
- M2: 0,001 Bit
- M3: 0,003667 Bit
- M4: 0,008760 Bit/Ereignis
- M5: 0,008760 Bit/Ereignis
- M7: 0,002241 Bit
- M9: 0,010351

M4 und M5 müssen sowohl Kontrollen schlagen als auch absolut über ihrer Nachweisschwelle liegen.

---

## 6. Ergebnislinie bis E-002R

### E-001

Drei getrennte Fragmenttypen:

- Sequenz,
- Kontext,
- Valenz.

Ergebnis:

- sichtbare lokale Traditionen entstanden,
- private Zustandseinschätzung blieb funktionslos,
- M2 und M3 waren null.

E-001 wurde verworfen.

### E-002R

Nach Verlust des ursprünglichen E-002-Ausführungscodes wurde die Architektur als E-002R vorab dokumentiert rekonstruiert.

Neu:

- gemeinsamer, aber bedeutungsloser Ausdruckskanal,
- Selbstbeobachtung als Bootstrap,
- getrennte dauerhafte Sequenz-, Kontext- und Valenzspuren.

Belastbar erreicht:

- M1 positiv,
- M2 positiv,
- M3 überwiegend positiv.

Damit funktioniert:

> intrinsischer Zustand → Ausdruck → private Einschätzung → Einfluss auf Handlung

Nicht erreicht:

- M4 in 0/3 Seeds über Schwelle,
- M5 in 1/3 Seeds über Schwelle,
- reine sichtbare Sequenztradition C1 stärker als C2 bei M7.

E-002R wurde extern validiert und verworfen.

K2 gilt ausdrücklich als **verletzt**, nicht als „fast bestanden“.

---

## 7. Diagnosen nach E-002R

### Keine destruktive Mittelung

Kontext- und Valenzspur verwässerten die Sequenzspur nicht. Die kombinierte Politik erzeugte mehr Divergenz als die Sequenzkomponente allein.

### Kein Turnover- oder Zerfallsproblem

- Zellen fortbestehender Träger blieben nahezu vollständig aktiv.
- Vorzeichen blieben nahezu vollständig stabil.
- Gruppenabdeckung und innerfamiliäre Redundanz waren hoch.

### Erster E-003-Überlappungsentwurf zurückgezogen

Zwei-von-drei-Familien je Agent hätten die Kapazität pro Familie halbiert. Das hätte etwa ein Viertel der Speichermasse und rund ein Drittel der Gruppenabdeckung vernichtet. Überlappung und Kapazitätsverlust wären untrennbar gewesen.

### E-003-D1 zurückgezogen

Vollständige Querverweise hätten bei Sequenz- und Kontextträgern lokal vollständige Tripel `(prev, action, inferred)` erzeugt.

Eine Diagnose zeigte, dass rund 99,994 Prozent der linkaktivierten Masse informationell nichtredundant gewesen wären. D1 hätte die gesuchte Dreierbeziehung konstruktiv lokal eingebaut.

---

## 8. E-003-D2

D2 verwendete eine partielle binäre Adresse:

- Zustandsprojektion als Paritätsklasse aus Valenzvorzeichen und Aktivierungsstufe,
- Symbolprojektion in zwei grobe Klassen,
- gleiche numerische Kapazität in BIND und SHAM,
- keine vollständigen lokalen Tripel.

Die Projektionsprovenienz wurde vor Freeze korrigiert:

- keine behauptete kryptographische Ableitung,
- explizite Designwahl,
- nicht vollständig semantikfrei,
- empirisch keine relevante Korrelation mit Valenzachse, Aktivierungsachse oder signierter Valenzspur.

Claude gab D2 zum Freeze frei.

### Durchführung

- Implementierungsfreeze geschlossen,
- 15 formale Kernläufe,
- Bedingungen C0, C1, D2-BIND, D2-SHAM, C8,
- drei Seeds 1086, 1047, 1031,
- sämtliche technischen Gates bestanden.

### Ergebnis

D2 wurde extern validiert und zwingend verworfen:

- M4: 0/3 Seeds über Schwelle,
- M5: 1/3 Seeds über Schwelle,
- BIND schlägt SHAM bei M5 nur in 1/3 Seeds,
- M7-Vorteil gegenüber stärkster Kontrolle: ungefähr −0,13 Bit,
- C1 bleibt stärkste sichtbare Gruppentradition.

### Match-Rate-Diagnose

- BIND-Link-Match-Rate: ungefähr 0,519
- SHAM-Link-Match-Rate: ungefähr 0,503
- lesbare dauerhafte Masse BIND: ungefähr 0,555
- lesbare dauerhafte Masse SHAM: ungefähr 0,546

Schluss:

> Das historische Adressbit hatte beim späteren Zugriff praktisch keine Diskriminierungskraft. Die Konjunktion blendete etwa 45 Prozent der dauerhaften Masse nahezu zufällig aus.

Verworfen ist nur die konkrete harte Ein-Bit-Teiladressierung. Nicht widerlegt ist familienübergreifende Bindung allgemein.

Budget nach D2: **39/60**.

---

## 9. E-004-PRG v1

Arbeitstitel:

**Predictive Relevance Gating**

Hypothese:

> Dauerhafte Zellen könnten anhand ihrer früheren handlungsprädiktiven Zuverlässigkeit gewichtet werden, ohne Masse zu entfernen oder zusätzliche semantische Koordinaten zu speichern.

Neue Zustandsgröße je aktiver Dauerzelle:

`r ∈ [−1,+1]`

Score:

`z = sign(d) × [1(A=a) − p(a)]`

Update:

`r_neu = (1−0,025)r_alt + 0,025z`

Abfragegewicht:

`m = 1 + 0,5r`, also `[0,5;1,5]`

Danach familienweise L1-Normalisierung, sodass die absolute dauerhafte Gesamtmasse exakt erhalten bleibt.

Claude bewertete v1 mit **Challenge**.

Priorisierte Blockade:

> Das vorgeschaltete Gate trennte zeitliche Vorhersagegüte nicht sicher von einer geschlossenen Policy-Selbstverstärkung.

Eine Zelle kann die Policy beeinflussen, dadurch häufiger zu einer gezogenen Handlung beitragen und anschließend weiter aufgewertet werden. Die bisherige ADDRESS-SHAM zerstörte nur die Zellzuordnung und fing diese Erklärung nicht ab.

---

## 10. Aktueller Entwurf E-004-PRG v2

E-004-PRG v2 verändert nicht die Architekturhypothese, sondern ergänzt eine zweite Kontrolle.

### PRG-BIND

- zellgebundenes `r`,
- Gewichtung der Policy,
- Update aus der tatsächlich gezogenen und sozial wirksamen Handlung.

### PRG-ADDRESS-SHAM

- gleiche `r`-Werte und Updates,
- vor der Abfrage maximal verändernd unter aktiven Zellen derselben Familie permutiert,
- prüft die korrekte Zellzuordnung.

### PRG-ACTION-PLACEBO

Bei jedem Ereignis:

1. Placebo-`r` gewichtet die aktuelle Policy.
2. Die reale Handlung `A` wird aus dieser Policy gezogen und verändert die Welt.
3. Unabhängig wird eine Pseudo-Handlung `Ã` aus derselben Policy gezogen.
4. Nur `Ã` aktualisiert Placebo-`r`.

Damit bleibt die vollständige Rückkopplung erhalten:

`r_placebo → Policy → Pseudo-Handlung → r_placebo`

Entfernt wird nur die Kopplung des Lernsignals an die tatsächlich sozial wirksame Handlung.

Unter reiner Selbstverstärkung sollte PRG-BIND ACTION-PLACEBO nicht robust schlagen.

---

## 11. Vorgesehene Stufe A

Stufe A ist eine verhaltensneutrale Diagnose auf archivierten Trajektorien.

Primär:

- E-002R-C2, drei Seeds.

Replikation:

- E-003-D2-BIND, drei Seeds,
- E-003-D2-SHAM, drei Seeds.

Voraussetzung:

- bit-exakter Numba-Replay jeder verwendeten Trajektorie.

Shadow-Prozesse:

- realer Score,
- 999 ACTION-PLACEBO-Ströme,
- 999 ADDRESS-SHAM-Permutationen.

Primäre Gates:

### A1: Log-Score gegen ACTION-PLACEBO

`ΔL_AP ≥ 0,003667 Bit/Ereignis`

- in mindestens 2/3 primären Seeds,
- gepoolt einseitig `p ≤ 0,025`.

### A2: Log-Score gegen ADDRESS-SHAM

`ΔL_AS ≥ 0,003667 Bit/Ereignis`

- in mindestens 2/3 primären Seeds,
- gepoolt einseitig `p ≤ 0,025`.

### A3: zukünftige Zellnützlichkeit

Positive vorab festgelegte Kalibrierungssteigung von `r` gegen späteren Score `z`.

BIND muss:

- in mindestens 2/3 Seeds positiv sein,
- ACTION-PLACEBO schlagen,
- ADDRESS-SHAM schlagen,
- gepoolt `p ≤ 0,025` erreichen.

Zusätzlich:

- synthetischer Placebo-Fidelitätstest,
- identische Scoreverteilung unter sozial informationslosem Nullfall,
- korrekte Autokorrelation,
- gleiche Zelllebenszeiten und Löschungen,
- mindestens 40 Prozent effektiv veränderte ADDRESS-SHAM-Zuordnungen,
- mindestens 60 Prozent der aktiven Masse in permutierbaren Abfragen.

Nur bei vollständig bestandenem Gate:

`E004_core_admission = true`

Bei Scheitern:

- kein Kernlauf,
- kein Kernbudgetverbrauch,
- keine nachträgliche Änderung von Score, Lernrate, Placebo, Strata oder Schwellen,
- E-004-PRG v2 gilt vor dem Kernblock als verworfen.

---

## 12. Vorgesehener formaler E-004-Block

Nur bei bestandener Stufe A:

- C0
- C1
- PRG-BIND
- PRG-ADDRESS-SHAM
- PRG-ACTION-PLACEBO
- C8

Drei Seeds:

- 1086
- 1047
- 1031

Gesamt:

- 18 Kernläufe
- Budget danach 57/60
- drei Kernläufe technische Reserve

PRG-BIND müsste bei M4, M5, M7 und den PRG-Diagnosen sowohl ADDRESS-SHAM als auch ACTION-PLACEBO schlagen.

---

## 13. Aktueller exakter Status

- Vorabprotokoll v1.2.0: eingefroren
- technische Kalibrierung: eingefroren
- E-001: verworfen
- E-002R: extern validiert und verworfen
- E-003 erster Überlappungsentwurf: zurückgezogen
- E-003-D1: zurückgezogen
- E-003-D2: extern validiert und verworfen
- E-004-PRG v1: von Claude challenged
- E-004-PRG v2: als Reaktion entworfen
- externe Prüfung von E-004-PRG v2: ausstehend
- E-004-Implementierung: nicht begonnen
- Stufe A: nicht ausgeführt
- E-004-Kernläufe: 0
- Budgetstand: 39/60
- Holdout: geschlossen

---

## 14. Nächster zulässiger Schritt im neuen Chat

Der Nutzer wird die Rückmeldung von Claude zu E-004-PRG v2 einfügen.

Dann:

1. Claudes Argument exakt rekonstruieren.
2. Prüfen, ob ACTION-PLACEBO die beanstandete zeitstabile Selbstverstärkung tatsächlich kontrolliert.
3. Keine Architekturänderung vornehmen, die Claude nicht verlangt oder die nicht aus einer klar benannten Blockade folgt.
4. Bei Support:
   - Freeze-Text finalisieren,
   - Stufe-A-Implementierung und synthetischen Placebo-Fidelitätstest einfrieren,
   - echte Numba-Umgebung und Hashes dokumentieren,
   - Stufe A ausführen,
   - Kernblock nur bei automatischem Admission.
5. Bei Support with reservations oder Challenge:
   - genau die verbleibende Blockade bearbeiten,
   - keine Kernläufe.
6. Holdout unter allen Umständen geschlossen halten.

Es darf nicht behauptet werden, dass Prozesse im Hintergrund weiterlaufen. Jeder Lauf muss in der aktiven Sitzung ausgeführt und sofort persistiert werden.

---

## 15. Relevante Dateien

### Minimal für die unmittelbare Claude-Rückmeldung

- `Schwarmwelt_Uebergabebriefing_E004_PRG_v2.md`
- `06_E004_PRG_V2_REVIEW_PACKAGE.zip`

### Zusätzlich vor Implementierung von Stufe A erforderlich

- `01_PREREGISTRATION_FREEZE_v1_2_0.zip`
- `02_CALIBRATION_FREEZE_v1_2_0.zip`
- `03_E002R_COMPLETE.zip`
- `04_E003_D2_IMPLEMENTATION_FREEZE.zip`
- `05_E003_D2_COMPLETE.zip`

Das E-002R-Paket enthält die primären archivierten Trajektorien.  
Das E-003-D2-Paket enthält die sechs vorgesehenen Replikationstrajektorien.  
Der D2-Implementierungsfreeze ist als reproduzierbare technische Ausgangsbasis aufzubewahren.
