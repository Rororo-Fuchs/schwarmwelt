# Briefing an die externe Kontrollinstanz

## Schwarmwelt / Praxislabor

**Gegenstand:** Prüfung eines möglichen Strategiewechsels: vom unmittelbaren Nachweis proto-sozialer Praxis zur vorgelagerten Untersuchung eines verteilten Schwarmgedächtnisses

**Status:** konzeptionelle Vorprüfung vor Definition, Kandidatenentwicklung, Architektur und Implementierung

**Rolle der Kontrollinstanz:** Prüfung und Einschränkung. Kein Ersatzentwurf und keine Optimierung des vorgeschlagenen Ansatzes.

---

## 0. Gewünschtes Prüfresultat

Die Prüfung soll drei Ebenen getrennt beurteilen:

1. **Forschungsreihenfolge**  
   Ist es methodisch sinnvoll, zunächst Schwarmgedächtnis und erst danach gemeinsame Praxis beziehungsweise Protokultur zu untersuchen?

2. **Begriff und Nachweislogik**  
   Ist die vorläufige Definition von Schwarmgedächtnis konsistent und experimentell von einfacheren Gedächtnis- und Koordinationsformen unterscheidbar?

3. **Aktuelle Aufgabenklasse**  
   Ist eine räumlich gegliederte Population mit fragmentierter Umwelt- und Begegnungsgeschichte grundsätzlich geeignet, einen solchen Nachweis zu führen?

Für jede Ebene wird um eines der folgenden Urteile gebeten:

- **verwerfen**
- **noch nicht entscheidbar**
- **unter Bedingungen weiterverfolgen**
- **weiterverfolgen**

Ein positives Urteil auf einer Ebene soll nicht automatisch als Zustimmung zu den anderen Ebenen gelten.

---

# 1. Ursprüngliches Erkenntnisinteresse

Das Projekt untersucht langfristig die Bedingungen, unter denen Populationen künstlicher Agenten proto-soziale und möglicherweise später protokulturelle Strukturen ausbilden können.

Die bisherigen Leitplanken waren:

- lokale Wahrnehmung;
- lokale Begegnungen;
- private persistente Memories;
- keine zentrale Steuerung;
- kein Blackboard;
- kein gemeinsamer Gedächtnisspeicher;
- keine vorgegebenen Rollen, Normen oder Konventionen;
- keine symbolische Kommunikation im ersten Aufbau;
- keine persistente Umweltspur, die die gesuchte Ordnung bereits speichert.

Das langfristige Ziel ist nicht der Nachweis bloßer Koordination, sondern historisch entstandener und verteilt stabilisierter Ordnung.

---

# 2. Bisheriger Untersuchungsweg

Es wurden zwei konzeptionelle Kandidatenrunden zu minimalen Begegnungssituationen durchgeführt.

Gesucht wurden Settings, in denen durch wiederholte Begegnungen gemeinsame Praxis entstehen könnte. Die Kandidaten wurden unter anderem geprüft auf:

- mehrere gleichwertige Verhaltensordnungen;
- notwendige Wechselseitigkeit;
- historische Kontingenz;
- verteilte Kausalität;
- Abhängigkeit von mehrschrittigen Verläufen;
- Abwesenheit eines versteckten sozialen Zustands.

Zusätzlich wurden einfache Konkurrenzmodelle betrachtet, insbesondere:

- kurze Markov-Regeln;
- private Zustandsautomaten;
- private Zähler und Routinen;
- Partnerkalibrierung;
- allgemeine adaptive Koordination;
- einseitige Führung;
- Partner-ID-basierte Policies.

Die zweite Runde wurde mit einem vorab festgelegten Such- und Prüfprozess durchgeführt. Kriterien wurden nach Beginn der Kandidatengenerierung nicht an einzelne Kandidaten angepasst.

---

# 3. Ergebnis der bisherigen Kandidatenrunden

Kein Kandidat wurde für Freeze, Architektur oder Simulation freigegeben.

Die Kandidaten fielen wiederholt auf einfachere Erklärungstypen zurück:

- aktuelle Beobachtung plus kurze Handlungshistorie;
- private Gewohnheit;
- Partner- oder Systemidentifikation;
- mechanische Koordination;
- unilaterale Festlegung durch einen Agenten;
- offen ausgeführte Partner-ID-Policy.

Der gemeinsame Befund lautete:

> Mehrschrittigkeit, Komplementarität und dyadische Spezifität reichen nicht aus, um eine proto-soziale Praxis von Koordination und privaten Policies zu unterscheiden.

Dieses Ergebnis widerlegt nicht die Möglichkeit proto-sozialer Praxis. Es zeigt zunächst nur, dass die bisher verwendete Aufgabenklasse und Suchstrategie keinen hinreichend diskriminierenden Kandidaten hervorgebracht hat.

---

# 4. Anlass des Strategiewechsels

Während der Auswertung entstand die Vermutung, dass die bisherige Forschungsreihenfolge zu viele Nachweise gleichzeitig verlangt hat.

Ein einzelnes Begegnungssetting sollte implizit zugleich leisten:

1. persistente Wirkung vergangener Begegnungen;
2. verteilte Speicherung dieser Geschichte;
3. gemeinsame spätere Nutzung;
4. Stabilisierung einer Praxis;
5. historische Variation;
6. Abgrenzung gegen allgemeine Koordination.

Daraus entstand der Vorschlag, diese Ebenen auseinanderzuziehen.

Vorläufige Reihenfolge:

```text
Schwarmgedächtnis
→ Schwarmpraxis
→ protokulturelle Ausprägungen
```

Der erste Schritt würde noch keine soziale oder kulturelle Interpretation beanspruchen.

---

# 5. Neue Grundfrage

Die zunächst zu untersuchende Frage wäre:

> Kann eine Population vergangene Information ausschließlich verteilt in privaten Agentengedächtnissen erhalten und später durch eigene lokale Interaktion funktional nutzen, obwohl kein einzelner Agent die vollständige relevante Information besitzt?

Damit verschiebt sich der erste Gegenstand von gemeinsamer Praxis zu einer elementareren Gedächtnisleistung.

---

# 6. Vorläufige Definition von Schwarmgedächtnis

Die derzeitige Arbeitsdefinition lautet:

> Ein funktionales Schwarmgedächtnis liegt vor, wenn Information aus vergangenen Ereignissen ausschließlich verteilt in privaten Zuständen mehrerer Agenten fortbesteht und durch spätere lokale Interaktion der Population so wirksam genutzt oder rekonstruiert wird, dass weder ein einzelner Agent noch der aktuelle Umweltzustand noch eine bloße externe Zusammenführung unabhängiger Einzelgedächtnisse die Leistung vollständig erklärt.

Die Definition enthält fünf vorläufige Bedingungen:

1. **Vergangenheitsabhängigkeit**  
   Die spätere Leistung hängt von einem früheren Ereignis ab.

2. **Verteilung**  
   Kein einzelner Agent besitzt alle notwendigen Informationen.

3. **Keine externe Persistenz**  
   Die relevante Information bleibt nicht in der Umwelt oder einem gemeinsamen Speicher erhalten.

4. **Interne Nutzung**  
   Die Population selbst führt die verteilten Anteile funktional zusammen.

5. **Kausale Abhängigkeit von der Verteilung**  
   Gezielte Veränderung der Gedächtnisträger, ihrer Zuordnung oder ihrer Kontaktstruktur verändert die Gruppenleistung.

Diese Definition ist nicht eingefroren und ausdrücklich Gegenstand der Prüfung.

---

# 7. Abzugrenzende Befunde

Folgende Befunde sollen zunächst nicht als Schwarmgedächtnis gelten:

- ein einzelner Agent erinnert die vollständige relevante Information;
- mehrere Agenten besitzen redundante vollständige Kopien;
- ein externer Auswerter kann private Erinnerungen zusammenführen, die Population selbst aber nicht;
- ein informierter Agent führt, während die übrigen nur folgen;
- die aktuelle Umwelt enthält weiterhin die Lösung;
- beim Abruf wird die vollständige Information neu übertragen;
- Agenten erkennen lediglich Gruppen- oder Partneridentitäten und wählen eine fertige Policy;
- die Gruppenleistung entsteht aus festen Wahrscheinlichkeiten, Mehrheitsbildung oder einem kollektiven Attraktor ohne relevanten Vergangenheitsbezug.

Die Kontrollinstanz wird gebeten zu prüfen, ob diese Abgrenzungen sinnvoll, vollständig und operational trennbar sind.

---

# 8. Aktuelle Aufgabenklasse

Der derzeit diskutierte Ausgangspunkt ist noch kein Versuchsdesign, sondern eine Aufgabenklasse:

> Eine räumlich gegliederte Population erlebt eine vergangene Umwelt- und Begegnungsgeschichte nur fragmentiert. Begrenzte Wahrnehmung, begrenzte Mobilität und Barrieren unterschiedlicher Permeabilität verhindern, dass ein einzelner Agent die vollständige Ereignisstruktur erwerben kann. Die Fragmente bleiben ausschließlich in privaten Memories erhalten. Nach einer Verzögerung wird geprüft, ob die Population die frühere Struktur durch lokale Interaktion funktional nutzen kann.

Als mögliches minimales Erinnerungsobjekt wurde eine vergangene Reihenfolge transienter Ereignisse in verschiedenen Regionen diskutiert.

Beispiel:

```text
R2 → R1 → R3
```

Verschiedene Teilpopulationen oder Brückenagenten könnten nur einzelne Ereignisse oder Relationen beobachten:

```text
R2 vor R1
R1 vor R3
```

Kein einzelner Agent dürfte die vollständige Kette besitzen.

Zum Abrufzeitpunkt wäre die Umwelt für verschiedene vergangene Ereignisfolgen identisch und von allen externen Spuren bereinigt.

---

# 9. Noch nicht festgelegt

Folgende Punkte sind ausdrücklich offen:

- konkretes Erinnerungsobjekt;
- genaue Form der lokalen Gedächtnisfragmente;
- episodisches oder assoziatives Memory;
- Rolle von Valenz;
- erlaubte Interaktion während des Abrufs;
- Populationsgröße;
- Kontaktgraph;
- Barrieren und Permeabilität;
- Tick- und Laufbudgets;
- Abrufaufgabe;
- Metriken;
- Agentenarchitektur;
- Lernverfahren.

Insbesondere wurde noch nicht entschieden, ob der erste Versuch diskrete Erinnerungsfragmente direkt speichert oder ob diese erst aus reicheren lokalen Episoden gelernt werden müssen.

---

# 10. Grund für die Wahl dieser Aufgabenklasse

Die Aufgabenklasse wurde aus zwei Überlegungen abgeleitet.

## 10.1 Strukturell unvollständige individuelle Perspektiven

Bei ausreichend großer und räumlich gegliederter Population können Wahrnehmung, Lebenszeit und Kontaktwege so begrenzt sein, dass kein Agent die gesamte relevante Umwelt- und Ereignisgeschichte erwerben kann.

Damit wäre die Information nicht nur zufällig, sondern konstruktiv verteilt.

## 10.2 Kontrollierbare Verteilung und Kopplung

Barrieren und Begegnungswege erlauben es prinzipiell, bei gleicher Gesamtinformation gezielt zu verändern:

- welche Agenten welche Fragmente tragen;
- welche Teilpopulationen verbunden sind;
- welche Brückenagenten existieren;
- wie redundant einzelne Fragmente gespeichert sind;
- ob komplementäre Fragmente später zusammenwirken können.

Die Aufgabenklasse soll daher nicht nur die Menge gespeicherter Information, sondern auch deren relationale Verteilung prüfbar machen.

---

# 11. Stärkste bisher erkennbare Gegenargumente

Die Aufgabenklasse könnte trotz dieser Struktur lediglich eines der folgenden bekannten Probleme realisieren:

1. **Distributed Mapping**  
   Die Population verteilt nur Teile einer Umweltkarte.

2. **Hidden Profile**  
   Mehrere Akteure besitzen Teilinformationen und müssen sie für eine Entscheidung zusammenführen.

3. **Transaktives Gedächtnis**  
   Die Gruppe lernt, bei wem welche Information liegt.

4. **Aktuelle Informationsweitergabe**  
   Das Gedächtnis liegt zwar privat vor, wird beim Abruf aber lediglich wie in einem Kommunikationsnetz übertragen.

5. **Führungs- oder Brückenagentenmodell**  
   Wenige zentrale Agenten tragen die relevante Leistung.

6. **Aggregation ohne Emergenz**  
   Die Gesamtinformation ist verteilt vorhanden, aber nur ein externer Auswerter kann sie sinnvoll zusammensetzen.

7. **Durch Architektur erzwungene Verteilung**  
   Der positive Befund könnte trivial werden, wenn die Aufgabe bereits so konstruiert ist, dass Teilinformationen nur addiert werden müssen.

Die Kontrollinstanz wird gebeten, die stärkste dieser oder eine andere konkurrierende Erklärung zu formulieren.

---

# 12. Forschungsanschluss

Als mögliche Bezugspunkte wurden bisher identifiziert:

- Transactive Memory Systems;
- Distributed Cognition;
- Hidden-Profile-Forschung;
- kollektives Lernen;
- kollektives Gedächtnis in Tiergruppen;
- dezentrale Informationsintegration;
- Swarm Robotics;
- Stigmergie und externe kollektive Speicher.

Noch ungeklärt ist:

- ob die vorgeschlagene Definition bereits durch eines dieser Felder hinreichend abgedeckt ist;
- ob „Schwarmgedächtnis“ hier nur eine Umbenennung bekannter verteilter Kognition wäre;
- welche etablierten Operationalisierungen, Kontrollen oder Metriken übernommen werden sollten;
- ob der Ausschluss persistenter Umweltspuren einen sinnvollen eigenständigen Untersuchungsraum schafft oder lediglich eine etablierte Architektur unnötig beschränkt.

---

# 13. Prüfauftrag

## A. Forschungsreihenfolge

Ist die Trennung

```text
Schwarmgedächtnis
→ Schwarmpraxis
→ Protokultur
```

methodisch sinnvoll?

Oder werden hier Phänomene getrennt, die theoretisch oder empirisch nicht unabhängig voneinander untersucht werden können?

---

## B. Definition

Ist die vorläufige Definition von Schwarmgedächtnis:

- konsistent;
- nicht zirkulär;
- operationalisierbar;
- von verteilter Speicherung und aktueller Kommunikation unterscheidbar?

Welche Bedingung ist überflüssig, zu stark oder fehlt?

---

## C. Aufgabenklasse

Kann die räumlich gegliederte, nur partiell verbundene Population grundsätzlich einen diskriminierenden Test ermöglichen?

Oder ist bereits absehbar, dass sie lediglich Distributed Mapping, Hidden Profile oder transaktives Gedächtnis reproduziert?

---

## D. Irreduzibilität

Ist die Forderung sinnvoll, dass weder Einzelagent noch aktueller Umweltzustand noch externe Aggregation die Leistung vollständig erklären dürfen?

Wie müsste „nicht durch einfache Aggregation erklärbar“ präzisiert werden, ohne einen prinzipiell unbeweisbaren Emergenzanspruch einzuführen?

---

## E. Kommunikation beim Abruf

Ist es methodisch konsistent, lokale Interaktion zu erlauben, aber explizite Übertragung vollständiger Erinnerungsinhalte auszuschließen?

Wo verläuft eine belastbare Grenze zwischen:

- Nutzung eines verteilten Gedächtnisses;
- Abrufkommunikation;
- und vollständiger Neurekonstruktion beim Abruf?

---

## F. Bekannte Forschung

Welche einschlägigen theoretischen, empirischen oder simulationsbasierten Arbeiten sollten zwingend berücksichtigt werden?

Insbesondere erbeten sind Hinweise auf:

- bereits etablierte Definitionen;
- etablierte Evidenzstufen;
- geeignete Kontrollbedingungen;
- bekannte Unmöglichkeits- oder Reduzierbarkeitsargumente;
- vergleichbare Multi-Agenten- oder Schwarmexperimente.

---

## G. Stärkste Gegenhypothese

Welches ist das kleinste bekannte oder plausible Modell, das einen positiven Befund der vorgeschlagenen Aufgabenklasse erzeugen könnte, ohne ein Schwarmgedächtnis im beanspruchten Sinn zu besitzen?

---

## H. Entscheidender Test

Welche einzelne Kontrolle oder welches formale Kriterium wäre am ehesten geeignet, die Aufgabenklasse vor einer aufwendigen Implementierung zu verwerfen?

---

# 14. Nicht erbeten

Nicht erbeten sind:

- konkrete Agentenarchitektur;
- konkrete Memoryimplementierung;
- Parameterwerte;
- Populationsgröße;
- Tickzahl;
- Code;
- nachträgliche Reparatur der Aufgabenklasse;
- ein alternatives vollständiges Experiment.

Falls der Ansatz nur durch wesentliche Zusatzmechanismen tragfähig würde, soll dies als Einwand dokumentiert und nicht in einen Ersatzentwurf überführt werden.

---

# 15. Erwünschte Antwortstruktur

1. **Gesamturteil zum Strategiewechsel**
2. **Urteil zur Definition**
3. **Urteil zur Aufgabenklasse**
4. **stärkste konkurrierende Erklärung**
5. **einschlägige Forschung**
6. **fehlende oder ungeeignete Kontrollen**
7. **entscheidendes Vorab-Verwerfungskriterium**
8. **Empfehlung für den nächsten zulässigen Schritt**

Ein negatives oder unentscheidbares Urteil ist ausdrücklich zulässig.

---

# 16. Beizufügende Unterlagen

1. dieses Briefing;
2. das bisherige PL-Prüfraster;
3. der Abschlussvermerk der zweiten Kandidatenrunde;
4. optional das Schwarmgedächtnis-Prüfraster als klar gekennzeichneter, noch nicht eingefrorener Arbeitsentwurf.

Die verworfenen Einzelkandidaten sollten nur auf Nachfrage beigefügt werden. Der Abschlussvermerk genügt zunächst, um die wiederkehrenden Verwerfungsgründe und die Herleitung des Strategiewechsels nachvollziehbar zu machen.
