# Schwarmgedächtnis-Prüfraster — Entwurf v0.1

## 0. Zweck

Das Prüfraster dient dazu, einen möglichen Befund von Schwarmgedächtnis von einfacheren Formen individueller, redundanter oder zentral rekonstruierbarer Speicherung zu unterscheiden.

Es wird angewendet, bevor:

- eine konkrete Versuchswelt ausgewählt wird;
- Populationsgrößen festgelegt werden;
- Tickbudgets bestimmt werden;
- Lern-, Gedächtnis- oder Valenzmechanismen implementiert werden;
- ein Batchversuch eingefroren wird.

Ein negatives Ergebnis ist zulässig. Insbesondere darf eine Population nicht deshalb als erinnernd bezeichnet werden, weil ihre Mitglieder einzeln Erinnerungen besitzen oder weil ein externer Beobachter deren Inhalte zusammenführen kann.

---

# 1. Vorläufige Arbeitsdefinition

> **Schwarmgedächtnis liegt vor, wenn Information aus vergangenen Ereignissen ausschließlich verteilt in privaten Zuständen mehrerer Agenten fortbesteht und durch spätere lokale Interaktion der Population so wirksam rekonstruiert oder genutzt wird, dass kein einzelner Agent, kein aktueller Umweltzustand und keine einfache Aggregation unabhängiger Einzelgedächtnisse die Leistung vollständig erklären kann.**

Die Definition enthält fünf notwendige Komponenten:

1. **Vergangenheitsbezug**  
   Die relevante Information stammt aus einem früheren Ereignis oder Ereigniszusammenhang.

2. **Verteilte Speicherung**  
   Kein einzelner Agent besitzt alle zur späteren Leistung erforderlichen Informationen.

3. **Keine persistente externe Ablage**  
   Die relevante Information besteht nicht in der Umwelt, einem Blackboard, einer globalen Variable oder einem gemeinsamen Speicher fort.

4. **Interne kollektive Nutzbarmachung**  
   Die Population selbst muss die verteilte Information durch ihre Interaktionen wirksam machen. Ein externer Auswerter genügt nicht.

5. **Kausale Irreduzibilität**  
   Die kollektive Leistung hängt spezifisch von der Verteilung und Kopplung der Gedächtnisanteile ab.

---

# 2. Stufenmodell

Das Raster unterscheidet zunächst sechs Befundstufen.

## SG0 — Kein persistentes Gedächtnis

Frühere Ereignisse beeinflussen spätere Leistungen nicht nachweisbar.

Mögliche Erklärungen:

- unmittelbare Reaktion;
- Umweltspur;
- aktueller Zustand;
- Zufall;
- fest verdrahtete Policy.

## SG1 — Individuelles Gedächtnis

Einzelne Agenten speichern vergangene Ereignisse und können daraus später handeln.

Der Populationskontext ist dafür nicht notwendig.

## SG2 — Redundantes Populationsgedächtnis

Mehrere Agenten speichern dieselbe Information.

Die Gruppe ist robuster gegen den Ausfall einzelner Agenten, aber jeder verbleibende Träger kann die relevante Leistung grundsätzlich allein erbringen.

## SG3 — Verteilte Speicherung

Verschiedene Agenten besitzen unterschiedliche Teilinformationen. Ein externer Beobachter oder zentraler Aggregator kann sie zusammenführen.

Die Population selbst muss dies noch nicht können.

## SG4 — Funktionales Schwarmgedächtnis

Die Population kann durch lokale Interaktion eine Leistung erbringen, für die verteilte Gedächtnisanteile aus früheren Ereignissen kausal zusammenwirken müssen.

Kein einzelner Agent und kein zentral nichtinteragierendes Summenmodell erklärt den Befund vollständig.

## SG5 — Rekonstruktives und robustes Schwarmgedächtnis

Zusätzlich zu SG4 kann die Population:

- fehlende oder beschädigte Gedächtnisanteile teilweise rekonstruieren;
- auf wechselnde Träger zurückgreifen;
- sich nach lokalen Ausfällen reorganisieren;
- die relevante Erinnerung über längere Zeiträume und mehrere Begegnungsketten erhalten.

SG5 ist ein stärkerer Befund, aber keine Voraussetzung für den ersten Nachweis von Schwarmgedächtnis.

---

# 3. Harte Gates

Ein Kandidat für Schwarmgedächtnis muss alle Gates SG-G1 bis SG-G7 prinzipiell schließen.

## SG-G1 — Vergangenheit ist notwendig

Die spätere Leistung muss von einem früheren Ereignis abhängen.

### Zu zeigen

Bei identischer aktueller Umwelt und identischer aktueller Beobachtung führen unterschiedliche frühere Ereignislinien zu systematisch unterschiedlichen kollektiven Leistungen.

### Ausschluss

Wenn die aktuelle Situation allein genügt, liegt kein Gedächtnisbefund vor.

---

## SG-G2 — Kein vollständiger Einzelträger

Kein einzelner Agent darf die gesamte relevante Information besitzen.

### Zu zeigen

- Einzelagentenleistung liegt unter der für die Aufgabe erforderlichen Schwelle.
- Kein einzelnes Memory enthält nach dem Kodierungsereignis alle notwendigen Bestandteile.
- Die spätere Leistung benötigt mindestens zwei getrennte Gedächtnisanteile.

### Ausschluss

Wenn ein einzelner Agent die Aufgabe zuverlässig allein lösen kann, liegt höchstens SG1 oder SG2 vor.

---

## SG-G3 — Keine externe Gedächtnisspur

Die relevante Information darf nicht persistent in der Umwelt oder in einem gemeinsamen Speicher erhalten bleiben.

### Auszuschließen

- Marker oder Artefakte;
- unveränderte Objektpositionen;
- persistente Felder;
- globale Historienvariablen;
- gemeinsame Register;
- versteckte Zustände der Welt;
- reproduzierbare Umweltasymmetrien;
- Zeit- oder Positionscodes, aus denen die Vergangenheit rekonstruiert werden kann.

### Kontrollforderung

Die Umwelt muss zwischen Kodierung und Abruf zurückgesetzt oder durch eine gleichverteilte Kontrollwelt ersetzt werden können.

---

## SG-G4 — Die Population führt die Integration selbst aus

Es genügt nicht, dass ein externer Beobachter private Memories ausliest und zusammenführt.

### Zu zeigen

Durch lokale Agenteninteraktion entsteht eine Handlung, Entscheidung oder Rekonstruktion, die die verteilten Gedächtnisanteile gemeinsam nutzt.

### Ausschluss

Wenn nur ein zentraler Auswerter die Information rekonstruieren kann, liegt SG3, aber noch kein Schwarmgedächtnis vor.

---

## SG-G5 — Relationale Verteilung ist kausal

Nicht nur die Menge gespeicherter Information, sondern ihre Verteilung und Kopplung zwischen Agenten muss für die Leistung relevant sein.

### Zu zeigen

Mindestens eine Kontrolle erhält:

- dieselben individuellen Gedächtnisinhalte;
- dieselbe Zahl von Agenten;
- dieselben Aktionsmöglichkeiten;
- dieselbe Gesamtinformation;

zerstört aber:

- die ursprüngliche Zuordnung der Gedächtnisanteile zu Agenten;
- relevante Begegnungslinien;
- oder die Kopplung komplementärer Teilinformationen.

Die kollektive Leistung muss sich dadurch gezielt verändern.

### Ausschluss

Bleibt die Leistung bei beliebiger Neuverteilung unverändert, genügt möglicherweise eine einfache Aggregation unabhängiger Erinnerungen.

---

## SG-G6 — Mehrere Gedächtnisträger sind kausal beteiligt

Die Leistung darf nicht durch einen informierten Agenten erzeugt werden, dem die übrigen lediglich folgen.

### Zu zeigen

- Entfernung verschiedener relevanter Träger beeinträchtigt unterschiedliche Teile der Leistung.
- Austausch nur eines Gedächtnisanteils verändert das Populationsergebnis.
- Kein einzelner Agent kann die Population dauerhaft in die richtige Lösung führen.

### Ausschluss

Wenn ein Agent die Erinnerung vorgibt und andere nur reagieren, liegt keine verteilte Gedächtnisleistung vor.

---

## SG-G7 — Verzögerung und Interferenz werden überstanden

Der Effekt muss eine nichttriviale Zeitspanne zwischen Kodierung und späterer Nutzung überdauern.

### Zu zeigen

Zwischen Kodierung und Abruf liegen:

- mehrere Ticks;
- andere Begegnungen;
- oder neutrale beziehungsweise störende Episoden.

### Ausschluss

Wenn die Leistung nur bei unmittelbarer Fortsetzung bestehen bleibt, handelt es sich möglicherweise um Arbeitszustand oder kurzfristige Aktivierung, nicht um persistentes Schwarmgedächtnis.

Die notwendige Dauer wird erst im konkreten Versuch festgelegt.

---

# 4. Konkurrenzmodelle

Jeder spätere Kandidat muss mindestens gegen folgende Modelle geprüft werden.

## M-SG0 — Aktuelle Umweltinformation

Die Lösung kann vollständig aus dem aktuellen Weltzustand abgeleitet werden.

## M-SG1 — Einzelagentengedächtnis

Mindestens ein Agent besitzt alle erforderlichen Informationen.

## M-SG2 — Redundante Speicherung

Mehrere Agenten besitzen vollständige Kopien derselben Information.

Die Robustheit entsteht nur durch Redundanz.

## M-SG3 — Unabhängige Teilinformationen

Agenten besitzen verschiedene Teilinformationen, führen sie aber nicht selbst funktional zusammen.

Ein externer Aggregator könnte die Lösung rekonstruieren.

## M-SG4 — Informierter Führungsagent

Ein Agent verfügt über die entscheidende Information; andere folgen oder verstärken lediglich seine Handlung.

## M-SG5 — Aktuelle Informationsweitergabe

Die Information wird während der Abrufphase vollständig von Agent zu Agent übertragen. Persistentes verteiltes Gedächtnis wäre nicht nötig; ein temporärer Kommunikationskanal genügt.

## M-SG6 — Partner- oder Gruppenidentifikation

Agenten erkennen nur, mit wem sie interagieren, und wenden eine gespeicherte Gruppen- oder Partnerpolicy an.

## M-SG7 — Populationsstatistik ohne Gedächtnis

Die richtige Gruppenleistung entsteht aus festen Verhaltenswahrscheinlichkeiten oder aus Mehrheitsbildung, obwohl kein relevantes vergangenes Ereignis gespeichert wurde.

---

# 5. Mindestkontrollen

## C-SG0 — No-history-Kontrolle

Die Abrufsituation bleibt gleich, aber es findet kein relevantes Kodierungsereignis statt.

Zweck:

- Nachweis, dass die spätere Leistung tatsächlich aus Geschichte stammt.

## C-SG1 — Einzelagententest

Jeder Gedächtnisträger wird separat in dieselbe Abrufsituation gesetzt.

Zweck:

- Ausschluss eines vollständigen Einzelgedächtnisses.

## C-SG2 — Umweltreset

Zwischen Kodierung und Abruf wird die Umwelt vollständig auf einen kontrollierten Zustand zurückgesetzt.

Zweck:

- Ausschluss persistenter Umweltspuren.

## C-SG3 — Gedächtnis-Shuffle

Private Memories werden zwischen Agenten permutiert, während die Gesamtmenge gespeicherter Information erhalten bleibt.

Varianten:

- zufälliger Shuffle;
- innerhalb lokaler Gruppen;
- zwischen Gruppen;
- nur komplementäre Teilinformationen vertauschen.

Zweck:

- Prüfung relationaler Verteilung.

## C-SG4 — Gedächtnisablation

Gezielte Entfernung einzelner Erinnerungsanteile oder Träger.

Varianten:

- zufällige Agenten;
- hochgradig vernetzte Agenten;
- seltene Informationsträger;
- redundante Informationsträger.

Zweck:

- Bestimmung kausaler Trägerstruktur und Robustheit.

## C-SG5 — Begegnungslinien-Shuffle

Die individuellen Memories bleiben erhalten, aber die späteren Begegnungspartner oder Kontaktpfade werden verändert.

Zweck:

- Prüfung, ob die Nutzung von einer historisch gewachsenen relationalen Struktur abhängt.

## C-SG6 — Zentralaggregator-Baseline

Ein externer Auswerter erhält dieselben privaten Gedächtnisinhalte.

Zweck:

- Trennung zwischen grundsätzlich vorhandener verteilter Information und der Fähigkeit der Population, sie selbst zu integrieren.

Die Population muss nicht besser als der ideale Aggregator sein. Sie muss aber eine relevante Leistung ohne ihn erbringen.

## C-SG7 — Kommunikationsersatz

Agenten erhalten während des Abrufs eine direkte, aktuelle Übertragung der relevanten Information, jedoch keine gespeicherte Geschichte.

Zweck:

- Trennung zwischen persistentem Gedächtnis und bloßem Informationsaustausch zum Abrufzeitpunkt.

## C-SG8 — Identitätskontrolle

Agentenidentitäten werden maskiert oder neu zugeordnet, während Memories und aktuelle Informationen kontrolliert werden.

Zweck:

- Ausschluss einfacher Partner-ID- oder Gruppen-ID-Policies.

## C-SG9 — Verzögerungs- und Interferenzkurve

Abruf nach unterschiedlichen Verzögerungen und mit unterschiedlich starker Zwischeninterferenz.

Zweck:

- Messung von Persistenz, Zerfall und möglicher kollektiver Rekonstruktion.

---

# 6. Messdimensionen

Die genauen Metriken werden erst mit einem konkreten Versuch festgelegt. Das Raster verlangt jedoch Messungen in mindestens sechs Dimensionen.

## 6.1 Individuelle Informationsvollständigkeit

Wie viel der relevanten Vergangenheit kann aus dem Memory eines einzelnen Agenten rekonstruiert werden?

## 6.2 Populationsweite Informationsverfügbarkeit

Wie viel Information ist in der Gesamtheit aller privaten Memories enthalten?

## 6.3 Kollektive Nutzungsleistung

Wie gut kann die Population die vergangene Information ohne externen Auswerter in einer späteren Aufgabe nutzen?

## 6.4 Integrationsgewinn

Differenz zwischen:

- bester Einzelagentenleistung;
- erwarteter Leistung unabhängiger Agenten;
- tatsächlicher Populationsleistung.

## 6.5 Ablationssensitivität

Wie verändert sich die Leistung bei zufälliger und gezielter Entfernung von Gedächtnisanteilen?

## 6.6 Persistenz

Wie verändert sich die Leistung mit zunehmendem Abstand zwischen Kodierung und Abruf?

## 6.7 Rekonstruktionsfähigkeit

Kann die Population nach Verlust eines Anteils eine funktional ausreichende Erinnerung wiederherstellen?

## 6.8 Trägerverteilung

Wie konzentriert oder verteilt liegt die kausale Gedächtnisleistung in der Population?

---

# 7. Positive Befundmuster

Ein erster positiver SG4-Befund würde mindestens folgendes Muster verlangen:

1. Unterschiedliche vergangene Ereignisse führen bei identischer Abrufwelt zu unterschiedlichen Gruppenleistungen.
2. Kein einzelner Agent kann die Aufgabe zuverlässig lösen.
3. Die Gesamtheit der privaten Memories enthält die benötigte Information.
4. Die Population kann diese Information durch lokale Interaktion nutzen.
5. Umweltreset beseitigt den Effekt nicht.
6. Gedächtnisablation oder gezielter Shuffle schwächt die Leistung vorhersagbar.
7. Ein einfaches Führungs-, Mehrheits- oder Partner-ID-Modell erklärt den Befund nicht vollständig.
8. Der Effekt bleibt über eine vorab definierte Verzögerung bestehen.

Ein SG5-Befund würde zusätzlich erfordern:

- partielle Robustheit gegen zufällige Ausfälle;
- spezifische Empfindlichkeit gegen relationale Ablationen;
- Wiederherstellung nach begrenzter Störung;
- eventuell Wechsel der konkreten Gedächtnisträger bei erhaltener Funktion.

---

# 8. Red Flags

Ein Versuch ist nicht als Schwarmgedächtnis interpretierbar, wenn:

- alle Agenten dieselbe Information vollständig erhalten;
- ein einzelner Agent die spätere Lösung trägt;
- relevante Information in der Umwelt bestehen bleibt;
- der externe Analysecode die Teilinformationen zusammenführt, nicht die Population;
- aktuelle Kommunikation die gesamte Vergangenheit neu übermittelt;
- nur die Zahl informierter Agenten gemessen wird;
- größere Populationen automatisch als stärkeres Gedächtnis gelten;
- Robustheit nur durch identische Kopien entsteht;
- Agenten-IDs eine fertige Antwortpolicy auswählen;
- nachträglich attraktive kollektive Muster ausgewählt werden;
- der Abruf unmittelbar nach der Kodierung stattfindet;
- Populationsleistung nicht mit der besten Einzelagenten- und Aggregatorbaseline verglichen wird.

---

# 9. Vorab-Verwerfung eines Versuchskandidaten

Ein konkreter Versuchskandidat ist vor Implementierung zu verwerfen, wenn:

1. die relevante Information nicht eindeutig operationalisiert werden kann;
2. ein einzelner Agent sie vollständig speichern darf;
3. die Umwelt die Information persistent trägt;
4. kein klarer Abruf oder keine spätere Nutzung definiert ist;
5. die Population die Teilinformationen nicht selbst integrieren muss;
6. ein einfacher Führungsagent die Leistung erzeugen kann;
7. Gedächtnis-Shuffle und Ablation keine unterschiedliche Vorhersage liefern;
8. aktuelle Kommunikation die gesamte Leistung erklären kann;
9. keine klare Abgrenzung zwischen SG1, SG2, SG3 und SG4 möglich ist;
10. der positive Befund nur aus einer höheren Erfolgsquote größerer Gruppen besteht.

---

# 10. Skalierung erst nach bestandenem Identifizierbarkeitsgate

Population, Tickzahl und Läufe werden erst festgelegt, wenn ein Kandidat dieses Raster prinzipiell schließen kann.

Die spätere Skalierung muss getrennt begründet werden:

- **Population:** ausreichende Verteilung und mehrere Träger;
- **Ticks:** Persistenz und Interferenz;
- **Läufe:** Robustheit gegenüber Seed, Kontaktgraph und Ablationsmuster.

Mehr Größe ersetzt keine Identifizierbarkeit.

---

# 11. Offene Grundsatzfragen

Vor einer Kandidatensuche sind insbesondere folgende Punkte zu klären:

1. Muss Schwarmgedächtnis eine konkrete frühere Information rekonstruieren oder genügt eine später wirksame verteilte Disposition?
2. Muss kein einzelner Agent die vollständige Information **zu irgendeinem Zeitpunkt** besitzen oder nur zum Abrufzeitpunkt?
3. Darf Information während des Abrufs zwischen Agenten übertragen werden, und wenn ja, wie viel?
4. Ist dyadisch verteiltes Gedächtnis bereits Schwarmgedächtnis oder wird eine Population mit mehreren lokalen Trägergruppen verlangt?
5. Wie unterscheiden wir Rekonstruktion von aktueller Neuentscheidung?
6. Welche Robustheit ist für SG4 notwendig und welche erst für SG5?
7. Wann ist Memory-Shuffle eine legitime Kontrolle und wann erzeugt er unnatürliche Agentenzustände?
8. Muss die relevante Information diskret formulierbar sein oder kann sie in einer verteilten Verhaltensdisposition bestehen?

Diese Fragen sind vor dem Freeze eines konkreten Experimentierrraums zu beantworten.
