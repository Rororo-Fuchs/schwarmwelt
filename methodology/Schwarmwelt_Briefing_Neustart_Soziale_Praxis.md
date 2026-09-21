# Schwarmwelt — Briefing für den Neustart

**Status:** konzeptueller Neustart vor Architektur- und Experimententwurf  
**Zweck:** Festlegung des Erkenntnisinteresses, der minimalen Agentenarchitektur und der Prüfkriterien, bevor Explorationsressourcen eingesetzt werden  
**Nicht enthalten:** konkrete Parameter, Implementierung, Metrikfreeze, Kernlaufplan oder Positivclaim

---

## 1. Ausgangspunkt

Der Neustart setzt nicht bei der Frage an, wie sich „Kultur“ technisch erzeugen oder in vorhandenen Trajektorien nachweisen lässt.

Die vorgelagerte Frage lautet:

> **Welche Agentenarchitektur kann wiederkehrende soziale Praxis hervorbringen, ohne Normen, Symbole, Gruppenwissen oder kollektives Gedächtnis bereits einzubauen?**

„Soziale Praxis“ bezeichnet hier zunächst nur beobachtbares Verhalten:

- Verhaltensweisen treten in Begegnungen wiederholt auf.
- Beteiligte Agenten passen ihre Reaktionen an frühere Begegnungen an.
- Die entstehenden Muster sind nicht allein durch identische Startbedingungen, Umweltzwang oder eine globale Optimallösung erklärt.
- Unterschiedliche Begegnungslinien können unterschiedliche, funktional gleichwertige Praktiken hervorbringen.

Eine spätere Frage nach Tradition oder Proto-Kultur bleibt möglich. Sie wird aber nicht zur Voraussetzung des ersten Builds gemacht.

---

## 2. Erkenntnisinteresse

Der erste Neustart soll drei Ebenen auseinanderhalten.

### 2.1 Individuelle Erfahrungsbildung

Können Agenten aus eigenen Begegnungen stabile, aber revidierbare Verhaltensdispositionen entwickeln?

Das ist noch kein soziales Phänomen. Es prüft, ob episodisches Erleben überhaupt in längerfristige Handlungspraxis überführt wird.

### 2.2 Wiederkehrende soziale Praxis

Können wiederholt interagierende Agenten Verhaltensformen ausbilden, die sich aufeinander beziehen und innerhalb einer Begegnungslinie stabilisieren?

Eine Praxis wäre mehr als die Summe zweier privater Gewohnheiten, wenn ihr Fortbestand von der wechselseitigen Reaktion der Beteiligten abhängt.

### 2.3 Übertragung

Können später hinzukommende oder neu gekoppelte Agenten solche Praktiken ausschließlich durch Begegnung aufnehmen?

Erst hier beginnt die Frage nach traditionsähnlicher Kontinuität. Sie gehört nicht in den ersten Implementierungsschritt, muss aber als spätere Prüfmöglichkeit architektonisch offenbleiben.

---

## 3. Grundentscheidungen

### 3.1 Kein kollektiver Zustand

Es gibt keinen:

- Gruppenspeicher,
- Blackboard,
- gemeinsamen Episodenpool,
- globalen Traditionsvektor,
- Zugriff auf Erinnerungen anderer Agenten,
- vorab definierten Gruppencharakter.

Alles, was später geteilt erscheint, muss in den privaten Zuständen und Verhaltensdispositionen einzelner Agenten verteilt vorliegen und durch Begegnungen entstanden sein.

### 3.2 Keine vorab eingebaute Kultursemantik

Die Agenten kennen keine Begriffe wie:

- Norm,
- Ritual,
- Tradition,
- Kooperation,
- Gruppe,
- Status,
- Symbolbedeutung.

Auch die Implementierung soll diese Kategorien nicht als versteckte Variablen führen.

### 3.3 Beobachtbares Verhalten vor Zeichenkommunikation

Der erste Build arbeitet nicht mit frei erzeugten Zeichenketten als primärem Kommunikationskanal.

Grund: Eine Zeichenkette ist nur dann sozial lesbar, wenn ihre Verwendung bereits an Situationen, Verhalten oder Konsequenzen gekoppelt ist. Wird diese Kopplung vorgegeben, ist die kommunikative Funktion teilweise eingebaut; fehlt sie, entsteht zunächst vor allem Rauschen.

Primär beobachtbar sind deshalb Handlungen und Reaktionsfolgen mit Konsequenzen für die beteiligten Agenten.

Ein expliziter Symbolkanal kann später zurückkehren, wenn geprüft werden soll, ob sich auf Grundlage bestehender Praxis konventionelle Zeichenverwendungen bilden. Er ist kein Bestandteil des Minimalbuilds.

---

## 4. Minimale Agentenarchitektur

Jeder Agent besitzt ausschließlich private Zustände und lernt nur aus der eigenen Perspektive.

### 4.1 Intrinsischer Zustand

Der Agent hat einen mehrdimensionalen inneren Zustand. Dieser darf nicht bloß als versteckte Belohnungszahl fungieren.

Er sollte mindestens ermöglichen:

- Zustandsverbesserung und Zustandsverschlechterung,
- Spannungs- oder Unsicherheitsveränderung,
- unterschiedliche Empfindlichkeit gegenüber gleichen Ereignissen,
- zeitliche Nachwirkung von Begegnungen.

Die Dimensionen bleiben für den Agenten operative Größen, nicht semantische Gefühle.

### 4.2 Episodisches Gedächtnis

Gespeichert werden eigene Erlebnisse, etwa:

- wahrgenommene Situation,
- beobachtbares Verhalten des Gegenübers,
- eigene Handlung,
- unmittelbare Folge,
- Veränderung des eigenen inneren Zustands,
- zeitlicher und relationaler Kontext aus Ich-Perspektive.

Das Gedächtnis enthält keine objektive Gesamtsicht der Begegnung und keine privaten Zustände anderer Agenten.

Episoden müssen:

- begrenzt,
- vergessbar,
- unterschiedlich stark konsolidierbar,
- bei ähnlichen Situationen teilweise reaktivierbar

sein.

### 4.3 Prozedurales Gedächtnis

Aus wiederholten und hinreichend bedeutsamen Episoden entstehen langsam veränderliche Handlungsdispositionen.

Prozedurales Gedächtnis speichert keine explizite Regel wie „Bei Agent X tue Y“. Es verändert, welche Reaktionsformen:

- leichter verfügbar,
- schneller ausgelöst,
- stabiler ausgeführt,
- eher variiert oder vermieden

werden.

Eine Praxis muss revidierbar bleiben. Vollständig eingefrorene Routinen würden nur Gewohnheit konservieren.

### 4.4 Generalisierung

Agenten dürfen nicht nur identische Situationen wiedererkennen. Episoden müssen anhand formaler Ähnlichkeit wirksam werden können.

Die Generalisierung darf jedoch keine soziale Kategorie vorwegnehmen. Sie kann sich etwa beziehen auf:

- ähnliche Abfolge beobachteter Handlungen,
- ähnliche eigene Zustandslage,
- ähnliche Begegnungsdynamik,
- ähnliche Konsequenzen.

Partneridentität kann als Teil einer eigenen Begegnungsgeschichte vorkommen, soll aber nicht automatisch Gruppenzugehörigkeit oder Reputation erzeugen.

### 4.5 Variation

Agenten benötigen begrenzte Verhaltensvariation. Ohne Variation können unterschiedliche Praktiken weder entstehen noch miteinander konkurrieren.

Variation darf nicht nur zufälliges Rauschen sein. Sie sollte von privaten Faktoren beeinflusst werden können, etwa:

- Unsicherheit,
- geringer prozeduraler Festigkeit,
- widersprüchlichen Episoden,
- hoher Neuartigkeit einer Situation.

---

## 5. Rolle der intrinsischen Valenz

Intrinsische Valenz bleibt im Neustart zentral, aber in enger begrenzter Funktion.

### 5.1 Was Valenz nicht ist

Valenz ist keine:

- externe Belohnung,
- Punktzahl für „richtiges“ Verhalten,
- soziale Norm,
- direkt übertragene Botschaft,
- Garantie für Kooperation,
- Kulturvariable.

### 5.2 Was Valenz zunächst leisten soll

Valenz bewertet aus der Innenperspektive des Agenten, wie eine Begegnung seinen eigenen Zustand verändert.

Sie beeinflusst vor allem:

1. **Episodische Konsolidierung**  
   Bedeutsamere Episoden werden stärker oder länger erinnert.

2. **Prozedurale Anpassung**  
   Episoden mit deutlichen Folgen verändern Handlungsdispositionen stärker als indifferente Episoden.

3. **Aufmerksamkeit und Reaktivierung**  
   Ähnliche Situationen können abhängig von früherer Valenz unterschiedlich salient werden.

Damit bestimmt Valenz nicht unmittelbar, was der Agent tut. Sie bestimmt, welche Erfahrungen für sein weiteres Verhalten Gewicht bekommen.

### 5.3 Offene Forschungsfrage

Valenz kann individuelle Gewohnheit fördern, ohne soziale Praxis hervorzubringen.

Der Build muss deshalb unterscheiden können zwischen:

- zwei Agenten, deren private Routinen zufällig kompatibel werden,
- einer wechselseitig stabilisierten Praxis,
- bloßer Anpassung an dieselbe Umwelt,
- einer Praxis, die sich durch Begegnung auf weitere Agenten überträgt.

Valenz ist ein möglicher Motor der Erfahrungsgewichtung, nicht bereits die Erklärung des sozialen Phänomens.

---

## 6. Begegnungsarchitektur

Die Begegnungssituation ist wichtiger als ein zusätzlicher Gedächtnismechanismus.

Sie muss mehrere Voraussetzungen erfüllen.

### 6.1 Mehrere mögliche Verhaltensverläufe

Es darf nicht nur eine offensichtlich optimale Lösung geben. Mindestens zwei oder mehr Verhaltensfolgen müssen:

- grundsätzlich tragfähig,
- nicht vollständig gleichzeitig ausführbar,
- anfänglich ähnlich wahrscheinlich

sein.

Sonst misst das System nur individuelle Optimierung.

### 6.2 Wechselseitige Konsequenzen

Das Verhalten eines Agenten muss die nächste Situation des anderen verändern. Reine Parallelhandlungen reichen nicht.

Dabei sollen Konsequenzen nicht von einer eingebauten sozialen Bewertung abhängen, sondern aus der Begegnungsdynamik entstehen.

### 6.3 Wiederholung mit Variation

Agenten müssen sich wiederholt begegnen können, aber nicht ausschließlich denselben Partnern.

Nur so lassen sich später unterscheiden:

- dyadische Gewohnheit,
- lokale Praxis,
- Übertragung auf andere Begegnungslinien.

### 6.4 Beobachtbarkeit

Die primäre Analyseeinheit ist nicht notwendig die Einzelhandlung. In Betracht kommen:

- kurze Handlungssequenzen,
- Übergänge zwischen Handlungen,
- Reaktionslatenzen,
- Rollenwechsel,
- Synchronisations- und Abbruchmuster,
- Wiederkehr bestimmter Verlaufsformen.

Welche Einheit tragfähig ist, muss vor einem Bestätigungsversuch festgelegt werden. In der Exploration dürfen mehrere formale Beschreibungen verglichen werden, solange daraus noch kein Positivclaim entsteht.

---

## 7. Was als wiederkehrende soziale Praxis gelten könnte

Eine erste Arbeitsdefinition lautet:

> Eine wiederkehrende soziale Praxis ist eine formal beschreibbare Verhaltensfolge, deren Auftreten durch frühere gemeinsame Begegnungen wahrscheinlicher wird, deren Fortbestand von wechselseitigen Reaktionen abhängt und die nicht ebenso gut durch private Eigendynamik, Umweltzwang oder bloße Kontaktmenge erklärt wird.

Für einen späteren traditionsähnlichen Befund wären zusätzlich erforderlich:

- Übernahme durch zunächst naive Agenten,
- partielle Stabilität über den Austausch einzelner Träger hinaus,
- Abhängigkeit von tatsächlicher Expositionsgeschichte,
- Möglichkeit konkurrierender lokaler Varianten.

Diese stärkeren Kriterien gehören noch nicht zum ersten Explorationsziel.

---

## 8. Vorbedingungen für Explorationsressourcen

Ein konkreter Ansatz wird erst implementiert, wenn folgende Fragen beantwortbar sind.

### 8.1 Mechanische Plausibilität

1. Welche beobachtbare Begegnungssituation wird modelliert?
2. Welche mehreren Verhaltensverläufe sind möglich?
3. Wie verändert das Verhalten eines Agenten die Lage des anderen?
4. Warum kann Wiederholung die privaten Dispositionen beider Agenten verändern?
5. Welche Rolle spielt Valenz dabei, ohne Handlungen direkt zu belohnen?

### 8.2 Trennbarkeit

6. Woran lässt sich individuelle Gewohnheit von wechselseitiger Praxis unterscheiden?
7. Wie wird dieselbe Umwelt ohne wiederholte soziale Exposition kontrolliert?
8. Wie wird bloße Kontaktmenge von passender Begegnungsgeschichte getrennt?
9. Wie werden Initialähnlichkeit und identische Agentenarchitektur kontrolliert?
10. Welche Beobachtung würde zeigen, dass gar keine soziale Praxis entstanden ist?

### 8.3 Architektonische Redlichkeit

11. Ist irgendwo ein kollektiver Zustand oder ein indirektes Blackboard verborgen?
12. Werden soziale Kategorien, Bedeutungen oder optimale Konventionen vorgegeben?
13. Erhält ein Agent Informationen, die er aus eigener Wahrnehmung und Geschichte nicht haben dürfte?
14. Ist jede zusätzliche Komponente für die Fragestellung notwendig?
15. Kann der Ansatz in einer kleineren Architektur dieselbe Frage beantworten?

Ein Ansatz, der diese Fragen nicht sauber beantwortet, erhält kein Explorationsbudget.

---

## 9. Mindestkontrollen eines späteren Piloten

Noch vor Parameterwahl muss der Ansatz folgende Kontraste grundsätzlich erlauben.

### 9.1 Valenzkontrast

Identische Architektur mit:

- wirksamer intrinsischer Valenz,
- neutralisierter Valenz,
- gegebenenfalls zeitlich oder episodisch falsch zugeordneter Valenz.

Der Kontrast soll zeigen, was Valenz am Verhalten verändert. Er ist zunächst kein Kultur-Gate.

### 9.2 Begegnungskontrast

Gleiche Agenten und gleiche Umwelt bei:

- wiederholter Begegnung,
- gleicher Kontaktmenge ohne stabile Begegnungslinie,
- permutierter Begegnungsgeschichte.

### 9.3 Gedächtniskontrast

Vergleich von:

- episodischem plus prozeduralem Gedächtnis,
- episodischem Gedächtnis ohne prozedurale Konsolidierung,
- prozeduraler Anpassung mit zerstörter Episodenzuordnung.

### 9.4 Späterer Transferkontrast

Erst nach einem belastbaren Praxisbefund:

- Einführung naiver Agenten,
- Austausch einzelner Träger,
- neue Paarungen,
- Exposition gegenüber fremden lokalen Praktiken.

---

## 10. Verwerfungskriterien

Der Ansatz wird vor weiterer Skalierung verworfen oder grundlegend zurückgestellt, wenn:

- wiederkehrende Muster ebenso ohne soziale Wiederholung entstehen,
- eine einzige Umweltlösung alle Agenten zwangsläufig konvergieren lässt,
- Valenz nur individuelles Optimieren verstärkt,
- prozedurales Gedächtnis Verhalten unabhängig vom Gegenüber fixiert,
- vermeintliche Praxis vollständig an einzelnen Partner-IDs hängt,
- der Befund nur mit semantischen Etiketten plausibel erscheint,
- die Analyse erst nach vielen nachträglich gewählten Metriken ein Signal findet,
- kollektive Stabilität nur durch einen versteckten gemeinsamen Zustand entsteht,
- ein kleineres Modell dieselbe Dynamik vollständig erklärt.

Ein negativer Pilot führt nicht automatisch zu Parameterjustierung. Zuerst wird entschieden, ob der Mechanismus überhaupt die richtige Frage adressiert.

---

## 11. Empfohlene Arbeitsfolge

### Phase 1 — Begegnungsproblem entwerfen

Noch ohne Code werden zwei bis vier minimale Begegnungssituationen formuliert. Jede muss mehrere gleichwertige Verhaltensverläufe und wechselseitige Konsequenzen erlauben.

### Phase 2 — Ansatz-Gate

Die Situationen werden gegen die Fragen und Verwerfungskriterien dieses Briefings geprüft. Nur ein Ansatz wird für den ersten Build ausgewählt.

### Phase 3 — Minimaler Agent

Implementiert werden ausschließlich:

- intrinsischer Zustand,
- episodisches Gedächtnis,
- prozedurale Konsolidierung,
- formale Generalisierung,
- begrenzte Variation,
- beobachtbare Handlungsmöglichkeiten.

Keine Symbolkommunikation, kein Turnover, keine Gruppenstruktur und keine Traditionsmetrik.

### Phase 4 — Terrarium-Pilot

Ziel ist zunächst die vergleichende Beobachtung:

> Was verändert intrinsische Valenz an individueller und dyadischer Verhaltensentwicklung?

Valenz- und Begegnungskontraste laufen parallel. Es gibt noch keinen Proto-Kultur-Claim.

### Phase 5 — Entscheidung über soziale Praxis

Nur wenn der Pilot wiederkehrende, wechselseitig stabilisierte Praxis nahelegt, wird ein eigener Prüfentwurf für soziale Praxis erstellt.

### Phase 6 — Übertragung und Tradition

Turnover, naive Agenten, Traditionslinien oder ein späterer Symbolkanal werden erst in einer neuen, getrennten Phase erwogen.

---

## 12. Nächste konkrete Aufgabe

Der Neustart beginnt nicht mit Gedächtniscode.

Als Nächstes sind **zwei bis vier minimale Begegnungssituationen** zu entwickeln und gegeneinander zu prüfen.

Jede Situation muss knapp beantworten:

1. Welche Handlungen sind beobachtbar?
2. Welche mehreren Verläufe sind möglich?
3. Wie wirken Handlungen wechselseitig?
4. Warum könnte Wiederholung eine Praxis stabilisieren?
5. Wie könnte Valenz Episoden unterschiedlich gewichten?
6. Welche einfachere nichtsoziale Erklärung ist zu erwarten?
7. Welche minimale Kontrolle trennt diese Erklärung ab?
8. Woran würde der Ansatz vor Implementierung verworfen?

Erst nach dieser Auswahl beginnt der technische Entwurf.

---

## 13. Arbeitsformel

> **Nicht Kultur implementieren.**  
> Agenten so ausstatten, dass eigene Erfahrungen ihr späteres Verhalten prägen können.  
> Begegnungen so gestalten, dass mehrere gemeinsame Praktiken möglich sind.  
> Erst beobachten, ob sich wiederkehrende soziale Praxis bildet.  
> Übertragung und Tradition erst prüfen, wenn dafür ein Verhaltensbefund vorliegt.
