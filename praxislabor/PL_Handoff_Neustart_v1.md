# Übergabebriefing — Schwarmwelt / Praxislabor (PL)

**Stand:** 11. Juli 2026  
**Status:** konzeptueller Neustart; noch kein Begegnungssetting ausgewählt, keine neue Implementierung begonnen  
**Zweck:** vollständige Übergabe in einen neuen Chat, ohne die aktive PL-Linie mit der abgeschlossenen E-Reihe zu vermischen  
**Verbindliche Begleitdatei:** `PL_Pruefraster_Protosoziale_Praxis.md` wird separat mitgenommen

---

## 0. Kurzanweisung für den neuen Chat

Dieses Briefing ist als verbindlicher Arbeitsstand zu behandeln.

Der neue Chat soll:

1. **nicht** mit einem Experimententwurf oder Code beginnen;
2. die aktive Linie ausschließlich als **Praxislabor (PL)** führen;
3. die Grundsätze aus dem Neustart-Briefing und dem separaten PL-Prüfraster ständig mitdenken;
4. zunächst **zwei bis vier minimale Begegnungssituationen** entwickeln;
5. jeden Kandidaten vor Ressourceneinsatz gegen das PL-Prüfraster prüfen;
6. in kurzen, abgeschlossenen Diskussionsabschnitten arbeiten, damit frühe Einwände nicht lange Folgeausführungen obsolet machen.

Ein zulässiges Ergebnis der Kandidatenprüfung ist ausdrücklich: **Keiner trägt.**

---

## 1. Projektstatus und harte Zäsur

Die Versuchslinie E-001 bis E-004 ist wissenschaftlich-methodisch abgeschlossen.

Der stärkste letzte Mechanismus wurde vor dem Kernblock verworfen. Der negative Befund wurde von der externen Prüfinstanz in einer eigenen CPython-3.12-/Numba-Umgebung mit selbst gebauten Tapes bit-exakt reproduziert.

Formaler Abschlussstand:

- E-004-Core-Admission: `False`
- Kernläufe E-004: `0`
- Budgetstand der alten Linie: `39/60`
- Holdout: geschlossen
- Stufe B: nicht autorisiert
- kein weiterer Prüfschritt an E-004 erforderlich

Die alte Reihe wird **nicht** als E-005 fortgesetzt. Die neue Linie erhält das Präfix:

> **PL — Praxislabor**

Vorläufig denkbare Bezeichnungen:

- `PL-01 Begegnungsarchitektur`
- `PL-02 Agentenarchitektur`
- `PL-03 Terrarium-Pilot`

Diese Nummerierung ist noch kein Versuchsfreeze.

### Trennregel

Aktive PL-Entwurfsdokumente sollen die E-Reihe möglichst nicht als argumentative Stütze führen. Die historischen Erkenntnisse werden in abstrakte Designregeln übersetzt. Dadurch soll vermieden werden, dass der Neustart unbemerkt zur Reparatur eines alten Mechanismus wird.

Die E-Reihe bleibt nur:

- Provenienz,
- methodischer Lernhintergrund,
- Nachweis der abgeschlossenen negativen Linie,
- Quelle übertragbarer Prüf- und Freeze-Verfahren.

---

## 2. Die konzeptuelle Neuausrichtung

Die bisherige Arbeit hatte zwei Fragen vermischt:

### Frage A

> Was geschieht mit dem Verhalten künstlicher Agenten, wenn sie intrinsische Valenz und private Erfahrungsgeschichte besitzen?

### Frage B

> Kann sich ein über Agenten und Turnover stabiles, gruppengeteiltes Gedächtnis beziehungsweise eine proto-kulturelle Überlieferung bilden?

Die frühere Grundarchitektur war eher für Frage A gebaut. Spätere Mechanismen versuchten, Frage B durch angelegte Bindungen, Adressierungen oder geteilte Spuren daran anzusetzen.

Der Neustart kehrt die Reihenfolge um:

```text
individuelle Erfahrung
→ revidierbare Verhaltensdisposition
→ wiederkehrende soziale Praxis
→ mögliche soziale Übertragung
→ erst dann mögliche traditionsähnliche Kontinuität
```

Die Leitfrage lautet jetzt:

> **Welche Agentenarchitektur kann wiederkehrende soziale Praxis hervorbringen, ohne Normen, Symbole, Gruppenwissen oder kollektives Gedächtnis bereits einzubauen?**

Nicht Kultur wird implementiert. Zunächst werden nur Bedingungen geschaffen, unter denen eigene Erfahrungen späteres Verhalten prägen und Begegnungen möglicherweise eine gemeinsame Praxis hervorbringen können.

---

## 3. Gestufte Erkenntnisziele

Die Ebenen dürfen nicht zusammengezogen werden.

### 3.1 Individuelle Erfahrungsbildung

Können Agenten aus eigenen Begegnungen stabile, aber revidierbare Verhaltensdispositionen entwickeln?

Zulässige Aussage bei Erfolg:

> erfahrungsabhängige individuelle Verhaltensentwicklung

Noch keine soziale Praxis.

### 3.2 Wiederkehrende soziale Praxis

Können wiederholt interagierende Agenten Verhaltensformen ausbilden, die sich wechselseitig aufeinander beziehen und innerhalb einer Begegnungslinie stabilisieren?

Arbeitsdefinition:

> Eine wiederkehrende soziale Praxis ist eine formal beschreibbare Verhaltensfolge, deren Auftreten durch frühere gemeinsame Begegnungen wahrscheinlicher wird, deren Fortbestand von wechselseitigen Reaktionen abhängt und die nicht ebenso gut durch private Eigendynamik, Umweltzwang, Imitation, bloße Kontaktmenge oder eine allgemeine Koordinationspolicy erklärt wird.

### 3.3 Übertragung

Können später hinzukommende oder neu gekoppelte Agenten solche Praktiken ausschließlich durch Begegnung aufnehmen?

Erst hier beginnt die Frage nach sozialer Transmission.

### 3.4 Traditionsähnliche Kontinuität

Kann eine Praxis den Austausch einzelner Träger teilweise überstehen, sich verändern, konkurrieren oder verzweigen?

Erst auf dieser Ebene wird eine proto-kulturelle Interpretation erwogen.

---

## 4. Verbindliche Architekturgrundsätze

### 4.1 Kein kollektiver Zustand

Es gibt keinen:

- Gruppenspeicher,
- Blackboard,
- gemeinsamen Episodenpool,
- globalen Traditionsvektor,
- dyadischen Konventionsspeicher,
- Zugriff auf fremde Erinnerungen,
- vorab angelegten Gruppencharakter,
- globale Norm- oder Kulturvariable.

Alles, was später geteilt erscheint, muss verteilt in privaten Zuständen und Verhaltensdispositionen einzelner Agenten vorliegen und durch Begegnungen entstanden sein.

Ein „kollektives Gedächtnis“ wäre ausschließlich ein **späterer Beobachtungsbefund**: private Geschichten haben sich durch Interaktion teilweise aneinander angenähert. Es ist kein Modul.

### 4.2 Private Perspektive

Jeder Agent darf ausschließlich verarbeiten:

- den eigenen inneren Zustand,
- die eigene Erinnerung,
- eigene frühere Handlungen und Folgen,
- aktuell öffentlich beobachtbares Verhalten anderer,
- öffentlich beobachtbare Folgen der Begegnung.

Nicht zugänglich sind:

- innere Zustände anderer Agenten,
- deren Valenz,
- Gedächtnis,
- Policy,
- Handlungsabsicht,
- objektive Gruppen- oder Rolleninformation,
- eine allwissende Beschreibung der Begegnung.

Technisch ist später eine harte Beobachtungsschnittstelle erforderlich. Ein Agent darf keine Referenz auf das interne Partnerobjekt erhalten.

### 4.3 Kein Symbolkanal im ersten Build

Der erste PL-Build verwendet **keine frei erzeugten Zeichenketten, Aussagen oder Symbolhandlungen** als primären Kommunikationskanal.

Primärmaterial sind:

- beobachtbare Handlungen,
- Reaktionsfolgen,
- Timing,
- Rollen- oder Initiationswechsel,
- Abbruch- und Korrekturmuster,
- öffentlich sichtbare Folgen.

Der Symbolkanal ist nicht grundsätzlich verworfen. Er kann später als zusätzliche, zunächst bedeutungsfreie Handlungsmöglichkeit zurückkehren, wenn bereits eine soziale Praxis nachgewiesen ist und geprüft werden soll, ob daraus konventionelle Zeichenverwendung entsteht.

### 4.4 Wichtige Unterscheidung: kein Symbolkanal ≠ keine bedeutungsfreien Indizes

Bedeutungsfreie Symbol- oder Aktionsindizes bleiben als **operatorseitige Abstraktionsschicht** zulässig und erwünscht.

Sie verhindern, dass das ausführende Modell an semantischen Namen Abkürzungen nimmt.

Beispiel:

```text
A0, A1, A2, A3
```

Diese Labels sind technische Namen beobachtbarer Optionen, keine Nachrichten und keine vorgegebene Bedeutung.

### 4.5 Keine vorab eingebaute Kultursemantik

Agenten und Implementierung kennen keine versteckten Variablen wie:

- Norm,
- Ritual,
- Tradition,
- Kooperation,
- Gruppenzugehörigkeit,
- Status,
- Symbolbedeutung,
- soziale Rolle.

Auch die spätere Auswertung darf solche Begriffe erst verwenden, wenn formale Verhaltenskriterien erfüllt sind.

---

## 5. Minimale Agentenarchitektur

Noch kein technischer Entwurf, aber folgende Komponenten gelten als Ausgangshypothese.

### 5.1 Intrinsischer Zustand

Mehrdimensionaler privater Zustand mit:

- möglichen Verbesserungen und Verschlechterungen,
- Spannung beziehungsweise Unsicherheit,
- unterschiedlichen Empfindlichkeiten,
- zeitlicher Nachwirkung von Begegnungen.

Die Dimensionen sind operative Größen, keine benannten Gefühle.

### 5.2 Episodisches Gedächtnis

Gespeichert werden eigene Erlebnisse aus Ich-Perspektive:

- wahrgenommene Situation,
- beobachtbares Verhalten des Gegenübers,
- eigene Handlung,
- öffentlich sichtbare Folge,
- eigene Zustandsveränderung,
- zeitlicher und relationaler Kontext.

Episoden müssen:

- begrenzt,
- vergessbar,
- unterschiedlich konsolidierbar,
- durch formale Ähnlichkeit teilweise reaktivierbar

sein.

Episodisches Gedächtnis hat Priorität. Ein nur kurzfristiges Turn-Memory wird ausdrücklich nicht als ausreichend betrachtet.

### 5.3 Prozedurales Gedächtnis

Aus wiederholten und hinreichend gewichteten Episoden entstehen langsam veränderliche Handlungsdispositionen.

Prozedurales Gedächtnis soll keine expliziten sozialen Regeln speichern. Es verändert nur, welche Reaktionsformen:

- leichter verfügbar,
- schneller ausgelöst,
- stabiler ausgeführt,
- eher variiert oder vermieden

werden.

Die Dispositionen müssen revidierbar bleiben.

### 5.4 Assoziatives und soziales Gedächtnis

Diese werden **nicht** als primäre Module priorisiert.

Assoziative Strukturen oder sozial differenzierte Erwartungen dürfen sich eventuell aus episodischem und prozeduralem Gedächtnis entwickeln. Sie sollen nicht vorab als eigene Wissenssysteme eingebaut werden.

Partneridentität darf Teil der eigenen Begegnungsgeschichte sein. Sie darf aber nicht automatisch Reputation, Gruppenwissen oder eine objektive soziale Kategorie erzeugen.

### 5.5 Generalisierung

Agenten müssen ähnliche, nicht nur identische Situationen auf frühere Erfahrungen beziehen können.

Zulässige Ähnlichkeiten können betreffen:

- Handlungsabfolgen,
- eigene Zustandslagen,
- Begegnungsdynamiken,
- Folgen.

Die Generalisierung darf keine soziale Semantik vorwegnehmen.

### 5.6 Variation

Ohne begrenzte Variation können keine unterschiedlichen Praktiken entstehen.

Variation sollte nicht nur unstrukturiertes Zufallsrauschen sein. Sie darf von privaten Faktoren abhängen, etwa:

- Unsicherheit,
- geringer prozeduraler Festigkeit,
- widersprüchlichen Episoden,
- Neuartigkeit.

---

## 6. Intrinsische Valenz: enge Rolle und Codegrenze

Valenz bleibt ein wichtiger Teil des PL-Ansatzes, ist aber kein Kulturmotor und kein sozialer Befund.

### 6.1 Was Valenz nicht ist

Keine:

- externe Belohnung,
- Punktzahl für „richtiges“ Verhalten,
- Norm,
- Nachricht,
- Garantie für Kooperation,
- soziale oder kulturelle Variable,
- aktionsspezifische Q-Funktion.

### 6.2 Zulässige Funktion

Valenz bewertet aus der Innenperspektive, wie eine Begegnung den eigenen Zustand verändert.

Sie darf beeinflussen:

- Stärke und Dauer episodischer Konsolidierung,
- Vergessen,
- Aufmerksamkeit,
- Reaktivierungswahrscheinlichkeit einer Episode,
- Stärke, mit der eine Episode prozedurales Lernen anstößt.

### 6.3 Verbindliche Pfadregel

> **Zwischen Valenzberechnung und aktueller Handlungswahl besteht kein direkter Pfad. Valenz darf zukünftiges Verhalten ausschließlich vermittelt über gespeicherte Episoden und deren Konsolidierung beziehungsweise prozedurale Verarbeitung beeinflussen.**

Insbesondere verboten:

- Valenz direkt auf Policy-Logits addieren,
- aktuelle Handlung durch einen Valenzwert gewichten,
- aktionsspezifische Werte aus Valenz fortschreiben,
- Handlungslabels positiv oder negativ markieren.

Auch reine Gedächtnisgewichtung kann funktional reinforcement-artig wirken. Das wird nicht geleugnet. Die Grenze lautet nicht „kein indirekter Verstärkungseffekt“, sondern:

> Gewichtung von Erfahrung, nicht direkte Richtung der Handlung.

Vor Implementierungsphase 3 muss diese Grenze code-scharf spezifiziert und prüfbar gemacht werden.

---

## 7. Koordination: notwendige Präzisierung, aber keine Gesamtdefinition

Koordination ist **nicht** die Definition sozialer Praxis.

Sie ist eine besonders kontrollierbare Kandidatenstruktur für erste Begegnungssituationen.

Eine geeignete Situation soll:

- einen Vorteil aus Abstimmung besitzen,
- aber nicht vorschreiben, welche Abstimmung gewählt wird,
- mehrere funktional gleichwertige Stabilitätspunkte erlauben,
- Misch- oder inkompatible Formen gegenüber abgestimmten Formen benachteiligen,
- keinen Stabilitätspunkt durch Geometrie, Timing oder Payoff bevorzugen.

Nagelprobe:

> Hat Koordination einen Vorteil, ohne dass die Situation festlegt, welche Koordination entsteht?

Wenn es nur eine optimale Lösung gibt, misst das Setting individuelle oder kollektive Optimierung. Wenn Abstimmung keinen Vorteil hat, bleibt nur Drift.

### Noch wichtiger

Auch bestandene Koordination ist noch kein protosozialer Befund.

Sie muss später getrennt werden von:

- mechanischer Reiz-Reaktion,
- Imitation,
- individueller Gewohnheit,
- allgemeiner partnerunabhängiger Koordinationspolicy.

---

## 8. Abgrenzung des gewünschten Befunds

Das separate PL-Prüfraster unterscheidet:

```text
M0 mechanische Reaktion
M1 Imitation / unmittelbare Reizübernahme
M2 individuelle Gewohnheit / Verstärkung
M3 Koordination
M4 protosoziale Praxis
```

Arbeitsdefinition für M4:

> Eine protosoziale Praxis ist eine historisch kontingente, durch wiederholte wechselseitige Begegnung entstandene Verhaltensordnung, an deren Entstehung und Aufrechterhaltung mehrere Agenten kausal beteiligt sind.

Dafür müssen insbesondere gelten:

- konkrete gemeinsame Geschichte ist notwendig;
- geschlossene Wechselseitigkeit ist notwendig;
- mehrere Agenten tragen kausal zur Stabilisierung bei;
- unter gleichen äußeren Bedingungen können unterschiedliche stabile Varianten entstehen;
- einfachere Vergleichsmodelle erklären die relevanten Verläufe nicht hinreichend.

### Evidenzleiter

- **A:** Wiederholung
- **B:** individuelle Gewohnheit
- **C:** Koordination
- **D:** historisch kontingente soziale Praxis
- **E:** soziale Übertragung
- **F:** traditionsähnliche Kontinuität

Die Begriffe dürfen nicht vorgezogen werden.

---

## 9. Beobachtung und Messdisziplin

Die primäre Beobachtungseinheit ist noch offen.

Mögliche formale Einheiten:

- kurze Handlungssequenzen,
- Übergänge,
- Initiation–Antwort–Korrektur–Abschluss,
- Reaktionslatenzen,
- Rollenwechsel,
- Synchronisationsmuster,
- Abbruchmuster,
- Wiederkehr von Verlaufsformen.

### Verbindliche Regel vor dem Terrarium-Pilot

Vor Phase 4 muss:

1. die **geschlossene Kandidatenmenge** möglicher Beobachtungseinheiten vorregistriert werden;
2. die Auswahl der Einheit ausschließlich auf Explorationsdaten erfolgen;
3. die gewählte Einheit auf getrennten Bestätigungsdaten geprüft werden;
4. nach Sichtung der Explorationsdaten keine neue Kandidateneinheit ergänzt werden.

Der Terrarium-Pilot ist explorativ, aber keine freie Metriksuche.

---

## 10. Prüf- und Kontrolllogik

Das vollständige Raster wird separat mitgenommen. Für die Übergabe sind folgende Kernkontrollen wichtig:

- **Umweltkontrolle:** gleiche Umwelt ohne reaktiven Partner
- **Ghost-Replay:** aufgezeichnete, nicht reagierende Partnersequenz
- **Begegnungsgeschichts-Shuffle:** gleiche Menge sichtbarer Ereignisse, falsche Begegnungslinie
- **Gleichwelt-Replikation:** gleiche äußere Bedingungen, getrennte Entwicklung
- **Partnerwechsel:** Trennung von individueller Gewohnheit und dyadischer Praxis
- **Responsivitäts-Knockout:** plausible Partnerhandlungen ohne aktuelle Kontingenz
- **Einfachmodell-Konkurrenz:** Reiz-Reaktion, Copy-last, individuelles Reinforcement, partnerunabhängige Markov-Policy, optimale Gedächtnislose Koordination, Partner-ID ohne Episodenfolge
- **Valenzkontrast:** aktiv, neutralisiert, eventuell zeitlich oder episodisch falsch gebunden
- **Gedächtniskontrast:** episodisch + prozedural versus gezielt getrennte Komponenten

Ein protosozialer Claim ist nur zulässig, wenn einfachere Erklärungen systematisch ausscheiden.

---

## 11. Historische Erkenntnisse — nur als Provenienz

Diese Punkte sollen im neuen Design mitgedacht, aber nicht als alte Experimentlogik importiert werden.

### 11.1 Der frühere Symbolkanal war nicht zufällig

Die früheren Zeichen waren schwach an den eigenen verborgenen Zustand gekoppelt. Agenten konnten durch Selbstbeobachtung eine private Zuordnung lernen und diese fehlbar auf andere anwenden.

Daraus entstand tatsächlich:

```text
eigener Zustand
→ eigener Ausdruck
→ private Einschätzung fremden Zustands
→ teilweise Handlungswirkung
```

Die Kommunikation war also nicht bloß Rauschen.

### 11.2 Dennoch war der Symbolkanal kein frei entstandenes soziales Zeichensystem

Die Zustandskopplung war populationsweit angelegt. Der Kanal funktionierte eher als schwacher Sensor für verborgenen Zustand als als historisch entstandene Konvention.

Daher gilt für PL:

- keine Schlussfolgerung „Symbole funktionieren nicht“;
- sondern: ein bereits geerdeter Symbolkanal beantwortet eine andere Frage als die Entstehung sozialer Praxis oder Konvention.

### 11.3 Beobachtbare Sequenzen waren der interessanteste alte Hinweis

In der alten Reihe zeigten sichtbare Sequenzstrukturen stärkere soziale Differenzierung als komplexere Gedächtnis- und Adressmechanismen.

Aber:

- Gruppenunterschiede waren keine Übertragung;
- Newcomer-Transmission blieb schwach;
- ein Stil- oder Divergenzbefund allein rechtfertigt keinen Traditionsclaim.

Abstrakte PL-Regel:

> Verhalten und Sequenzen zuerst; Übertragung später separat prüfen.

### 11.4 Angelegte geteilte Spuren trugen nicht

Sobald konstruierte Bindungen fair gegen marginalgleiche oder kausal passende Kontrollen geprüft wurden, verschwand ihr Vorteil.

Abstrakte PL-Regel:

> Keine soziale Spur als Mechanismus vorgeben. Eine geteilte Spur darf erst nach beobachtetem Verhalten als mögliche emergente Struktur gemessen werden.

### 11.5 Methodischer Apparat bleibt erhalten

Übertragbar sind:

- Vorabprotokolle,
- Exploration/Bestätigung-Trennung,
- faire Sham- und Placebo-Kontrollen,
- harte Gates,
- automatische Abbruchregeln,
- Hashes und Manifeste,
- unabhängige Reproduktion,
- Bereitschaft zum negativen Abschluss.

Nicht übertragen werden ohne neue Begründung:

- alte Metriken,
- Schwellen,
- Parameter,
- Zell- oder Adresslogiken,
- Gruppenzuweisungen,
- frühere Versuchsnummern.

---

## 12. Erwogene und derzeit nicht übernommene Richtungen

### 12.1 Gruppengedächtnis / kollektiver Zustand

Verworfen als Startarchitektur.

Grund:

- Blackboard-Gefahr,
- Kollektivität wäre eingebaut,
- spätere Gruppenstabilität würde nur Funktion des Speichers zeigen.

### 12.2 Externe Artefaktspuren

Interessant, aber für den ersten PL-Build geparkt.

Sie könnten:

- flüchtig,
- veränderbar,
- gemeinsam zugänglich

sein, bergen aber die Gefahr eines eingebauten Zeichen- oder Steuerkanals. Der Nutzer bevorzugt zunächst beobachtbares Verhalten.

### 12.3 Lokale Sedimentation außerhalb der Agenten

Nicht übernommen.

Auch eine schwache Begegnungs- oder Raumspur wäre ein externer kollektiver Zustand. Alles Soziale soll zunächst ausschließlich in Agenten und ihren privaten Erfahrungsgeschichten liegen.

### 12.4 Bewegungs-/Engpasssetting

Nur als erste Skizze diskutiert, **nicht ausgewählt**.

Vorteil:

- mehrere symmetrische Koordinationsmöglichkeiten,
- gut beobachtbare Reaktionsfolgen.

Hauptproblem:

- möglicherweise vollständig als mechanische Reiz-Reaktion,
- Imitationsspiel,
- oder triviales Koordinationslernen erklärbar.

Es darf im neuen Chat nicht als beschlossener Kandidat behandelt werden.

---

## 13. Aktueller offener Designpunkt

Die nächste Aufgabe ist **nicht** Agentencode.

Zu entwickeln sind zwei bis vier minimale Begegnungssituationen. Sie sollten nicht alle derselben Koordinationsklasse angehören, damit soziale Praxis nicht von vornherein mit einem einzigen Spieltyp gleichgesetzt wird.

Jeder Kandidat muss knapp beantworten:

1. Welche Handlungen sind öffentlich beobachtbar?
2. Welche mehreren Verhaltensverläufe sind möglich?
3. Wie wirken die Handlungen wechselseitig?
4. Warum könnte Wiederholung individuelle Dispositionen und eine gemeinsame Praxis stabilisieren?
5. Wie könnte Valenz Episoden gewichten, ohne direkt Handlungen zu steuern?
6. Welche einfachere nichtsoziale Erklärung ist zu erwarten?
7. Welche minimale Kontrolle trennt diese Erklärung ab?
8. Woran wird der Kandidat vor Implementierung verworfen?
9. Hat Koordination einen Vorteil, ohne dass die Situation festlegt, welche Koordination entsteht?

Zusätzliche harte Fragen aus dem PL-Raster:

- Benötigt das Setting eine mehrschrittige Reaktionsfolge statt einer Einzelhandlung?
- Kann ein Ghost-Replay die echte Interaktion imitieren?
- Ist die konkrete Begegnungsgeschichte kausal notwendig?
- Können gleiche Welten unterschiedliche stabile Varianten hervorbringen?
- Tragen mehrere Agenten zur Aufrechterhaltung bei?
- Gibt es einen versteckten gemeinsamen Zustand?
- Kann ein einfacheres Modell den gesamten relevanten Befund reproduzieren?

### Auswahlverdikte

- Verwerfen
- nur mechanischer Pilot
- Koordinationspilot
- PL-Kandidat

Nur ein PL-Kandidat rechtfertigt den eigentlichen Praxislabor-Build.

---

## 14. Noch offene Architekturfragen nach der Kandidatenauswahl

Diese Fragen sind bewusst noch nicht entschieden:

- genaue Dimensionen des intrinsischen Zustands;
- Speicherform und Kapazität episodischen Gedächtnisses;
- Mechanismus der prozeduralen Konsolidierung;
- formale Ähnlichkeitsfunktion für Generalisierung;
- Rolle von Partneridentität;
- Variation und Explorationsdynamik;
- konkrete Valenzberechnung;
- Aktions- und Beobachtungsraum;
- Kandidatenmenge der Beobachtungseinheiten;
- Explorations-/Bestätigungssplit;
- Laufzeit, Agentenzahl, Netzwerk oder Begegnungsplan;
- späterer Turnover und Transfer.

Diese Punkte dürfen nicht vorgezogen werden, solange kein tragfähiges Begegnungsproblem gewählt ist.

---

## 15. Empfohlene Arbeitsfolge

### Phase 1 — Begegnungskandidaten

Zwei bis vier minimale Situationen entwickeln.

### Phase 2 — Ansatz-Gate

Alle Kandidaten gegen Neustart-Briefing und PL-Prüfraster prüfen. Höchstens einen auswählen.

### Phase 3 — Minimaler Agent

Erst danach spezifizieren:

- intrinsischen Zustand,
- episodisches Gedächtnis,
- prozedurale Konsolidierung,
- Generalisierung,
- Variation,
- harte Beobachtungsschnittstelle,
- code-scharfe Valenzpfade.

Keine Symbolkommunikation, kein Turnover, keine Gruppenstruktur, keine Traditionsmetrik.

### Phase 4 — Terrarium-Pilot

Zunächst nur:

> Was verändert intrinsische Valenz an individueller und dyadischer Verhaltensentwicklung?

Mit Valenz-, Begegnungs- und Gedächtniskontrasten. Noch kein Proto-Kultur-Claim.

### Phase 5 — Eigener Prüfentwurf soziale Praxis

Nur bei belastbarem Verhaltensbefund.

### Phase 6 — Übertragung und Tradition

Naive Agenten, Trägeraustausch, Turnover oder Symbolkanal erst in einer getrennten späteren Phase.

---

## 16. Arbeitsweise im neuen Chat

Der Nutzer bevorzugt kurze Diskussionsabschnitte.

Daher:

- pro Antwort möglichst nur ein Designproblem;
- Annahmen nicht über viele Abschnitte fortschreiben, bevor sie bestätigt sind;
- Kritik früh aufnehmen;
- keine langen Komplettarchitekturen aus einer unbestätigten Anfangsannahme ableiten.

Die bewährte Rollentrennung bleibt:

### Entwickelndes Modell

- formuliert Kandidaten,
- rekonstruiert stärkste Version,
- prüft Vereinfachungen,
- erstellt Spezifikationen und später Implementierung.

### Externe Prüfinstanz

- prüft und beschränkt,
- sucht Gegenhypothesen und Kontrolllücken,
- darf blockieren,
- soll grundsätzlich keinen Ersatzentwurf liefern.

Das Prüfmodell ist keine Wahrheitsinstanz, sondern organisierter Widerstand. Technische Positivbefunde benötigen weiterhin unabhängige Reproduktion.

---

## 17. Begleitdateien

### Im Übergabepaket enthalten

1. `00_PL_Handoff_Neustart_v1.md`  
   Dieses Dokument.

2. `01_Schwarmwelt_Briefing_Neustart_Soziale_Praxis.md`  
   Grundbriefing vor der Präzisierung durch die externe Prüfinstanz. Die Ergänzungen zu Koordination, Beobachtungseinheiten und Valenz sind in diesem Handoff verbindlich fortgeschrieben.

3. `02_Schwarmwelt_Richtungsnotiz_nach_E004.md`  
   Konzeptuelle Neuausrichtung mit der Unterscheidung Frage A / Frage B und Terrarium / emergente Überlieferungsspur.

4. `03_Schwarmwelt_Methodenbriefing_Dualmodell_Arbeitsweise.md`  
   Übertragbares Arbeitsverfahren mit entwickelndem und prüfendem Modell.

5. `04_Schwarmwelt_E001_bis_E004_Methodischer_Abschlussbericht.md`  
   Historischer Abschluss der alten Reihe.

### Separat mitzunehmen

`PL_Pruefraster_Protosoziale_Praxis.md`

SHA-256:

```text
2c3fee68978dea527ee8dd4d69694e44b7abe1d55ae3862fd840162e3033525d
```

Das Raster ist die verbindliche Auswahl- und Interpretationsgrundlage für Begegnungskandidaten.

---

## 18. Empfohlene erste Nachricht im neuen Chat

> Hier ist das Übergabepaket für Schwarmwelt / Praxislabor (PL) sowie separat das PL-Prüfraster. Behandle das Handoff als verbindlichen Stand. Die alte E-Reihe ist abgeschlossen und darf nicht als Reparaturlinie fortgeführt werden. Nächste Aufgabe: Entwickle in kurzen Chunks zwei bis vier minimale Begegnungssituationen, die unterschiedliche Klassen abdecken könnten. Beginne zunächst nur mit Kandidat 1 und prüfe ihn gegen die neun Fragen und das PL-Raster, bevor du Kandidat 2 formulierst.

---

## 19. Kompakte Arbeitsformel

> Kein kollektiver Zustand.  
> Keine Kultursemantik.  
> Keine Symbolkommunikation im ersten Build.  
> Private episodische Erfahrung und revidierbare prozedurale Dispositionen.  
> Valenz gewichtet Erfahrung, nicht aktuelle Handlung.  
> Beobachtbares Verhalten und geschlossene Wechselseitigkeit zuerst.  
> Koordination ist noch keine protosoziale Praxis.  
> Übertragung und Tradition erst nach einem belastbaren Verhaltensbefund.
