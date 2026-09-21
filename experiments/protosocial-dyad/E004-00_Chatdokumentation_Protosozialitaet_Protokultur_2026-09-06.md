# E-004 – Chatdokumentation: Protosozialität, Protokultur und minimale Agentensysteme

**Dokumentationsdatum:** 2026-09-06  
**Chatinterne Versuchsläufe:** überwiegend 2026-07-27 bis 2026-07-29  
**Status:** Forschungsstrang dokumentiert; kein positiver proto-sozialer oder proto-kultureller Befund; Dyaden-Hauptversuch nicht erreicht, weil Gate 0 an der Modellkalibrierung scheiterte.

## 1. Gegenstand des Chats

Der Chat entwickelte aus einer allgemeinen Frage nach kultureller Emergenz in künstlichen Agentensystemen ein schrittweise verschärftes Forschungsprogramm. Ausgangspunkt war die Beobachtung, dass frühere Versuche trotz mehrerer Generationen, Valenzen, privater Zustände, Interpretation fremden Verhaltens, unvollständiger Weitergabe und fehlendem kollektivem Gedächtnis keine überzeugenden kulturellen Strukturen erzeugt hatten.

Die leitende Frage wurde deshalb zurückverlagert: Bevor man Kultur erwartet, müsste vielleicht zunächst überhaupt eine soziale Gegenüber-Struktur entstehen. Daraus entstand die Hypothese, dass nicht ein sozialer Reward, sondern ein allgemeiner epistemischer Bias relevant sein könnte:

> Ein lernendes System bevorzugt die einfachste interne Modellstruktur, die seine sensorische Welt hinreichend erklärt.

Die zentrale Analogie war die frühe kindliche Entwicklung: Ein System muss nicht von vornherein wissen, was ein Mensch oder ein Agent ist. Es könnte zunächst nur entdecken, dass bestimmte Umweltursachen persistent, teilweise autonom und auf eigenes Verhalten kontingent reagieren.

## 2. Forschungsrahmen

Über den gesamten Chat wurden folgende Bedingungen als verbindlich geschärft:

- keine vorgegebenen Agentenidentitäten;
- keine Sender-/Empfängerrollen;
- kein expliziter Kommunikationskanal;
- keine gemeinsame Belohnung;
- keine Belohnung für Kooperation oder sozialen Einfluss;
- keine zentralisierte Policy oder zentraler Critic;
- keine geteilten Gewichte zwischen Agenten;
- lokale, mehrdeutige Sensorik;
- getrennte prädiktive Weltmodelle;
- kausale Interventionen statt bloßer Korrelationsmessung;
- statistisch gematchte Kontrollen;
- Train-/Validierungs-/Holdout-Trennung;
- checkpointbares neuronales Training;
- positive und negative Kalibrierung vor jedem stärkeren Interpretationsschritt.

Ein Effekt sollte ausdrücklich **nicht** als proto-sozial gelten, wenn er vollständig durch bekannte Paradigmen erklärt werden kann, insbesondere:

- Standard-Multi-Agent-Reinforcement-Learning;
- emergente Kommunikation bei vorgegebenem Kommunikationskanal;
- Social-Influence-Reward;
- Imitations- oder soziales Lernen in vorstrukturierten Settings;
- Konventionsspiele mit explizitem Koordinationsziel;
- Agency Detection;
- Sensorimotor Contingency;
- allgemeine Umweltkontrolle.

## 3. Begriffliche Staffelung

Der Chat entwickelte folgende Stufenlogik:

1. **Persistente Ursache:** Eine verborgene Umweltursache wird über Zeit als zusammengehörig modelliert.
2. **Adaptive Ursache:** Das Modell erfasst, dass sich die Dynamik der Ursache selbst verändert.
3. **Reziproke Kopplung:** Zwei lernende Systeme verändern sich wechselseitig.
4. **Endogene Praxis:** Eine von mehreren möglichen Interaktionsformen stabilisiert sich ohne explizite Vorgabe.
5. **Reparatur:** Nach einer Störung wird spezifisch die zuvor etablierte Praxis wiederhergestellt.
6. **Tradierung:** Eine kontingente Praxis überlebt den Austausch der ursprünglichen Träger.

Erst die Stufen 3–5 sollten als ernsthafte Kandidaten für **protosoziales Verhalten** gelten. Eine **protokulturelle** Interpretation sollte zusätzlich Tradierung, populationsspezifische Varianten und Fortbestand nach Agentenersetzungen verlangen.

## 4. Einordnung in bestehende Forschungsfelder

Der Chat ordnete die Fragestellung in mehrere benachbarte Forschungsfelder ein:

- emergente Kommunikation;
- Social Influence und Empowerment;
- soziales Lernen;
- Norm- und Konventionsbildung;
- Rollen- und Arbeitsteilung;
- Causal Multi-Agent Reinforcement Learning;
- Agency Detection und sensomotorische Kontingenz;
- tierische Kultur und soziale Tradierung.

Die wiederkehrende Beobachtung aus diesen Feldern wurde so zusammengefasst: Funktionale Codes, Konventionen, Rollen oder Kooperation entstehen relativ leicht, sobald Aufgabe, Kommunikationskanal, soziale Beobachtbarkeit oder Belohnung die Sozialität bereits funktional vorbereiten. Die radikalere Vorfrage – ob ein System überhaupt eine reaktionsfähige Ursache als besonderes Gegenüber differenziert – ist deutlich weniger direkt untersucht.

## 5. Versuchsreihe E004-01: Ringwelt-Vorversuch

### Aufbau

Vier ortsfeste Agenten/Prozesse interagierten über lokale ternäre Kanäle. Die Architektur vermied explizite Kommunikation und nutzte private Zustandsregulation als Lernziel.

Ausgewertet wurden unter anderem:

- Live-Kopplung;
- Playback;
- Entkopplung;
- Kantenblockade;
- Agentenersatz.

### Ergebnis

Die Live-Umwelt wurde geringfügig besser genutzt als eine entkoppelte Umwelt. Dieser Effekt ließ sich jedoch durch gewöhnliche Umweltkontrolle erklären.

Besonders wichtig:

- Agentenersatz verschlechterte die Leistung kaum;
- Kantenblockaden erzeugten kein stabiles Reparaturverhalten;
- die ursprüngliche Playback-Kontrolle war methodisch zu schwach, weil eine aufgezeichnete Sequenz bei deterministischer Auswertung dieselbe Handlungsgeschichte reproduzieren konnte.

### Interpretation

Kein Nachweis sozialer Adressierung. Der Versuch war technisch nützlich, zeigte aber, dass bloße Muster- und Kontingenzverarbeitung nicht ausreichen.

## 6. Versuchsreihe E004-02: Latente Ursachen und MDL

### Fragestellung

Kann ein Modell mit persistenter latenter Ursache eine sensorische Folge einfacher erklären als ein kurzfristiges reaktives Modell?

Verglichen wurden:

- M0: rein reaktives Modell;
- M1: kleine persistente latente Ursache;
- M2: größere latente Struktur.

### Ergebnis

In einem linearen MDL-Ansatz gewann M0 in allen Bedingungen. Die Auswertung wurde jedoch methodisch nicht als starker Nullbefund akzeptiert, weil die Komplexitätsstrafe die latenten Modelle wahrscheinlich zu stark benachteiligte. Die PCA-Projektionsstruktur wurde als zu viele formale Parameter gezählt.

### Interpretation

Der Lauf wurde als fehlgeschlagene Operationalisierung von „einfachstem erklärenden Modell“ gewertet, nicht als Beleg gegen latente Ursachenbildung.

## 7. Versuchsreihe E004-03: neuronales Weltmodell

### Aufbau

Die lineare Variante wurde durch kleine neuronale sequenzielle Modelle ersetzt. Wesentliche Merkmale:

- GRU-basierte Weltmodelle;
- kurze gegen persistente Gedächtnisstruktur;
- neuronale Latentrepräsentationen;
- Train/Validierung/Holdout;
- checkpointbare Ausführung;
- kausale Forks;
- Interventionen;
- keine soziale oder gemeinsame Belohnung.

### Kalibrierung

Positive Kontrollen zeigten, dass die neuronalen Modelle eine persistente verborgene Ursache intern zuverlässig repräsentieren konnten. In klaren Kontrollfällen war der verborgene Zustand teilweise nahezu vollständig aus der latenten Repräsentation decodierbar.

### Hauptbefund

Die latenten Modelle kodierten verborgene Prozesse, waren aber in den Hauptwelten nicht das einfachste oder beste Vorhersagemodell. Ein starkes Vier-Tick-Modell sagte die Beobachtungen häufig besser voraus.

Beispielhafte Holdout-MSE aus dem dokumentierten Hauptlauf:

| Bedingung | M0 – 4 Ticks | M1 – latent 2D | M2 – latent 4D |
|---|---:|---:|---:|
| persistent und reaktionsfähig | 0,071842 | 0,085572 | 0,083638 |
| Playback | 0,101000 | 0,107157 | 0,105989 |
| reaktiv ohne Gedächtnis | 0,167622 | 0,189325 | 0,185830 |
| autonom persistent | 0,112994 | 0,129522 | 0,124996 |
| Zufallsprozess | 0,411780 | 0,420459 | 0,435557 |
| Identitätswechsel | 0,071066 | 0,087839 | 0,078919 |

Der Kausalfork zeigte, dass die Modelle durchaus lernten, dass eigene Handlungen den weiteren Umweltverlauf beeinflussen. Dieser Effekt war aber gerade im kurzfristigen M0 am stärksten. Reaktionsfähigkeit war also lokal erkennbar, ohne eine persistente Gegenüber-Repräsentation zu benötigen.

### Interpretation

Die entscheidende Unterscheidung lautete:

1. Eine verborgene Ursache existiert.
2. Ein Netz kann sie intern abbilden.
3. Diese Abbildung ist die einfachste und nützlichste Erklärung.

In den Hauptwelten waren 1 und teilweise 2 erfüllt; 3 nicht.

## 8. Methodischer Audit: Scheinsignal „lernend-reaktiver Prozess“

Zwischenzeitlich erschien ein Effekt vielversprechend: Persistente Modellierung war bei einem als „lernend-reaktiv“ behandelten Gegenprozess stärker als bei Playback und einem reaktiven Automaten.

Der anschließende Audit zeigte jedoch, dass der Gegenprozess gar kein lernender Agent war. Er hatte:

- eine feste autoregressive Zustandsdynamik;
- eine feste Reaktionsregel;
- keinen Optimierer;
- keine Policy-Aktualisierung;
- kein eigenes Weltmodell.

Auch der untersuchte Agent lernte zunächst nur sein Weltmodell; seine Aktionen wurden extern erzeugt.

Damit konnte die Architektur strukturell keine echte wechselseitige Anpassung oder Reparatur einer gemeinsam stabilisierten Kopplung hervorbringen.

Der Effekt wurde deshalb korrekt als **Agency Detection / sensorimotorische Kontingenzerkennung** verworfen.

## 9. Übergang zur Dyade

Aus diesem Audit folgte die zentrale Architekturentscheidung: Für einen echten proto-sozialen Test braucht es mindestens zwei unabhängig lernende Agenten.

Zwei Agenten verändern qualitativ die Dynamik:

- A passt sich an B an und B gleichzeitig an A;
- die Umwelt wird durch gegenseitiges Lernen nichtstationär;
- eine gemeinsame Interaktionsgeschichte wird möglich;
- mehrere stabile Praktiken können pfadabhängig entstehen;
- gezielte Reparatur nach Störung wird überhaupt erst sinnvoll messbar;
- spätere Tradierung über Generationenwechsel wird möglich.

## 10. Geplantes Dyaden-Gateprogramm

Die Dyade sollte aus zwei strukturell gleichen, aber vollständig getrennten neuronalen Agenten bestehen. Beide sollten indirekt über ein träges gemeinsames Medium aufeinander wirken. Kein Agent sollte sensorisch darüber informiert werden, dass ein anderer Agent existiert.

### Gate 0 – Kalibrierung

Voraussetzungen:

- positive Kontrolle mit klarer persistenter verborgener Ursache;
- negative Kontrolle ohne persistente Ursache;
- kurzfristig reaktive Kontrolle;
- Nachweis, dass epistemische Aktionswahl zwischen nichtsozialen Kausalmodellen unterscheiden kann.

### Gate A – adaptive Ursache

Vergleich:

- zwei mitlernende Agenten;
- Playback;
- reaktiver Automat;
- eingefrorener ehemals lernender Agent;
- Gedächtnisreset-Kontrolle.

### Gate B – reziproke Kopplung

Nachweis bidirektionaler kausaler Wirkung A→B→A durch gepaarte do-Forks aus identischem Zustand.

### Gate C – endogene Praxis

Suche nach stabilen, nicht vollständig funktional erzwungenen Varianten, die innerhalb einer Population stabiler sind als zwischen Populationen.

### Gate D – Reparatur

Gezielte Störung einer etablierten Praxis. Positiv nur, wenn bevorzugt die frühere Variante wiederhergestellt wird und dies häufiger als nach Neustart oder Kontrollstörung geschieht.

### Gate E – Tradierung

Erst nach repliziertem Gate-D-Befund. Schrittweiser Ersatz der ursprünglichen Agenten durch naive Agenten ohne Übertragung von Gewichten, Gedächtnis oder Replay-Speicher.

## 11. Autonome Ausführungslogik

Das Programm wurde als streng begrenztes Gate-System geplant. Die autonome Steuerung durfte nur vorab erlaubte Parameterreihen untersuchen:

- Sensorrauschen: 0,05 / 0,12 / 0,25 / 0,45;
- Reaktionsverzögerung: 1 / 3 / 6 / 10;
- Persistenz des Mediums: 0,80 / 0,92 / 0,97 / 0,995;
- epistemisches Aktionsgewicht: 0 / 0,05 / 0,15 / 0,30;
- anschließend begrenzte Gedächtniskapazität.

Pro Serie sollte nur eine Dimension verändert werden. Kombinationen waren erst nach einem replizierten Kandidaten erlaubt.

Die technische Ausführung war checkpointbar mit kleinen Trainingsblöcken, atomarem Speichern, getrenntem Training und Auswertung sowie einem kumulativen Manifest.

## 12. Dyaden-Gate-0: dokumentierte Kalibrierungsserie

Die späteren Dyaden-Rohdateien sind in der aktuellen Sitzung nicht mehr verfügbar. Die folgenden Resultate sind daher **aus dem Chat rekonstruiert** und werden nicht als erhaltene Primärdaten ausgegeben.

### 12.1 Erster Gate-0-Lauf

- positive persistente Kontrolle: intern gut repräsentiert;
- negative Kontrolle: bestanden;
- kurzfristige reaktive Kontrolle: nicht bestanden;
- epistemische Unterscheidung zweier nichtsozialer Kausalmodelle: technisch bestanden.

Problem: M0 und M1 waren nicht hinreichend kapazitätsgleich.

### 12.2 Reparatur mit kapazitätsgleichen GRUs

M0 und M1 erhielten dieselbe GRU- und Decoderarchitektur; nur die Gedächtnisdauer unterschied sich.

Ergebnisse:

- langfristig persistente Ursache: M1-Vorteil ca. 0,02236; 4/4 Seeds; bestanden;
- kurzfristig reaktiv: praktisch Gleichstand; bestanden;
- weißes Rauschen: kleiner M1-Vorteil; eingefrorenes Negativkriterium nicht bestanden.

### 12.3 Replikation der negativen Kontrolle

Über 12 Holdout-Seeds und vier Initialisierungen, 48 Paarvergleiche:

- mittlerer M1-Vorteil ca. 0,000342;
- Bootstrap-95-%-Intervall ca. −0,000029 bis 0,000698;
- M0 gleich gut oder besser nur 39,6 %.

Das Negativgate blieb geschlossen.

### 12.4 Modellselektionsprüfung

Nach längerer Ausbildung verschwand der mittlere M1-Vorteil praktisch:

- M1-Vorteil ca. −0,000063;
- Bootstrap-95-%-Intervall ca. −0,000412 bis 0,000272.

Das eingefrorene Richtungs-Kriterium blieb dennoch unerfüllt. Eine nachträgliche Umdefinition des Gates wurde ausdrücklich verworfen.

### 12.5 Probabilistisches Zustandsraummodell

M0 und M1 sagten Mittelwert und Unsicherheit voraus; Primärmaß war held-out Gaussian NLL.

Dokumentierte Ergebnisse:

- langfristig persistente Ursache: M1-Vorteil ca. 0,01174; 8/8 Seeds; bestanden;
- kurzfristig reaktiv: mittlerer Unterschied praktisch null; nur 4/8 in der geforderten Richtung;
- weißes Rauschen: mittlerer Unterschied praktisch null; ebenfalls 4/8.

Auch hier blieb Gate 0 formal geschlossen.

### 12.6 Abschließende Replikation

Mit 32 Holdout-Seeds und vier Initialisierungen zeigte sich schließlich, dass das persistente Modell selbst in Kontrollen ohne theoretischen Langzeitnutzen einen systematischen Vorteil hatte:

- kurzfristig reaktiv: mittlere NLL-Differenz M0−M1 ca. 0,002747; 95-%-Intervall 0,001841 bis 0,003655; M0 nur 29,7 % gleich gut oder besser;
- weißes Rauschen: mittlere NLL-Differenz ca. 0,000321; 95-%-Intervall 0,000105 bis 0,000533; M0 nur 38,3 % gleich gut oder besser.

### Ergebnis von Gate 0

Die probabilistische GRU-Modellfamilie wurde verworfen. Gate A wurde nicht geöffnet.

Dies ist ausdrücklich:

- **kein Nullbefund zu Protosozialität**;
- **kein Nullbefund zu Protokultur**;
- **kein Test der eigentlichen Zwei-Agenten-Dyade**;
- sondern ein geschlossener Architektur- und Kalibrierungsabbruch.

## 13. Aktueller belastbarer Stand

1. Persistente verborgene Ursachen können neuronal repräsentiert werden.
2. Kausale Reaktionsfähigkeit kann erkannt werden.
3. Weder 1 noch 2 reichen für einen sozial interpretierbaren Befund.
4. Ein einzelner lernender Agent plus fester Gegenprozess kann strukturell keine reziproke Praxis hervorbringen.
5. Zwei unabhängig lernende Agenten sind deshalb für den nächsten echten Test notwendig.
6. Die bisher verwendeten GRU-Modellfamilien sind für den erforderlichen feinen Vergleich von kurzfristiger und persistenter Weltmodellierung nicht sauber genug kalibriert.
7. Die eigentliche Dyade wurde daher aus methodischen Gründen **nicht** gestartet.

## 14. Nächster methodisch zulässiger Schritt

Eine Fortsetzung müsste als neues, formal eingefrorenes Versuchsprogramm beginnen. Empfohlen wurde eine andere Modellselektionsarchitektur, beispielsweise:

- explizites probabilistisches generatives Zustandsraummodell;
- klare Trennung von Null-, Kurzzeit- und Langzeitmodell innerhalb derselben Modellfamilie;
- Evidenz- oder held-out-Likelihood-basierter Modellvergleich;
- Kalibrierung gegen positive, negative und kurzfristige Kontrollen vor jeder Dyadeninterpretation;
- erst danach zwei unabhängig lernende Agenten mit eigener epistemischer Aktionswahl.

Die zentrale offene Forschungsfrage lautet weiterhin:

> Unter welchen Minimalbedingungen entsteht aus allgemeiner prädiktiver Weltmodellierung nicht nur die Repräsentation einer persistenten Ursache, sondern eine wechselseitig stabilisierte, reparierbare und schließlich tradierbare Praxis?

## 15. Integritätsnotiz zu den Dateien

Im Drive-Paket werden zwei Dateitypen unterschieden:

### Erhaltene Primärartefakte

- Ringwelt-Vorversuch, vollständiges Paket;
- MDL-/Latent-Ursachen-Versuch, vollständiges Paket;
- neuronales Weltmodell, vollständiges Paket, Code, eingefrorenes Protokoll, Bericht und Aggregatdaten.

### Rekonstruierte Sekundärartefakte

- Dyaden-Gate-0-Chronik;
- zusammenfassende Gate-Tabelle;
- methodische Abbruchentscheidung.

Diese Dateien werden ausdrücklich als „rekonstruiert aus Chat“ bezeichnet, weil die späteren Rohdateien im aktuellen Sitzungsspeicher nicht mehr vorhanden sind.
