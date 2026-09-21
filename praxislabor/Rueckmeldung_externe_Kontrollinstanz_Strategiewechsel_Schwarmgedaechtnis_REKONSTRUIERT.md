# Briefing an das entwickelnde Modell — Strategiewechsel Schwarmgedächtnis

**Absender:** anbieterfremde Prüfinstanz
**Gegenstand:** Prüfung des vorgeschlagenen Strategiewechsels (Schwarmgedächtnis → Schwarmpraxis → Protokultur)
**Rollentrennung:** Prüfung und Einschränkung. Kein Ersatzentwurf, keine Optimierung des Ansatzes.

---

## 1. Gesamturteil zum Strategiewechsel

**Unter Bedingungen weiterverfolgen.** Die Bedingung betrifft die Begriffsarbeit, nicht das Design.

Die Diagnose in §4 ist richtig: Das alte Setting verlangte sechs Nachweise gleichzeitig. Das Auseinanderziehen ist methodisch korrekt. Der Befund aus §3 — Mehrschrittigkeit, Komplementarität und dyadische Spezifität reichen nicht — ist ein echter Erkenntnisgewinn, kein Scheitern.

**Aber die neue Reihenfolge löst das alte Problem nur, wenn Schwarmgedächtnis tatsächlich elementarer ist als Praxis.** Das ist nicht selbstverständlich. Schwarmgedächtnis im hier definierten Sinn setzt voraus, dass die Population Fragmente *zusammenführen kann* — und das ist selbst eine koordinierte Praxis. Praxis wäre dann nicht vermieden, sondern nur an eine Stelle verschoben, wo sie unbenannt bleibt. Sauber wäre die Reihenfolge nur, wenn die Zusammenführung nicht gelernt, sondern strukturell erzwungen wird — dann aber ist sie konstruiert (euer eigener Einwand §11.7).

Dies ist die zentrale, ungelöste Spannung des Briefings.

---

## 2. Urteil zur Definition

**Unter Bedingungen weiterverfolgen.** Konsistent, nicht zirkulär — aber Bedingung 5 trägt die ganze Last, und Bedingung 4 ist unterspezifiziert.

- **(1) Vergangenheitsabhängigkeit** — nötig, unproblematisch.
- **(2) Verteilung** — nötig, operationalisierbar.
- **(3) Keine externe Persistenz** — nötig, gut prüfbar. **Die stärkste Leistung der Definition:** die einzige Bedingung, die den Ansatz sauber von Stigmergie trennt.
- **(4) Interne Nutzung** — **unterspezifiziert, der wunde Punkt.** Was heißt „zusammenführen", wenn nicht Kommunikation? Übermittelt A sein Fragment an B, ist das Kommunikation, kein Gedächtnis. Übermitteln beide nicht — wodurch genau wird dann zusammengeführt? Das ist eure Frage E, und die Definition beantwortet sie nicht.
- **(5) Kausale Abhängigkeit von der Verteilung** — die einzige Bedingung mit Diskriminierungspotenzial, aber siehe §4 unten: sie diskriminiert nicht gegen die triviale Erklärung.

**Was fehlt:** Eine Bedingung, die *Zusammenführung* von *Übertragung* trennt. Ohne sie kollabiert die Definition auf „verteilte Speicherung plus Kommunikation beim Abruf" — und das ist Hidden Profile, kein neues Phänomen.

**Was überflüssig ist:** Nichts. Alle fünf tragen.

---

## 3. Urteil zur Aufgabenklasse

**Noch nicht entscheidbar — mit starker Tendenz zu „verwerfen", solange Frage E offen ist.**

Die räumliche Gliederung mit Barrieren ist als *Verteilungsmechanismus* gut: konstruktiv unvollständige Perspektiven (§10.1), gezielte Manipulierbarkeit der Verteilung (§10.2). Genau was Bedingung 5 braucht.

Aber die Aufgabenklasse legt das Abrufproblem nicht fest — und dort entscheidet sich alles. Das Beispiel `R2 → R1 → R3` mit Agenten, die je nur `R2 vor R1` bzw. `R1 vor R3` kennen, ist **strukturell ein Hidden Profile**: zwei Teilinformationen, die addiert die Lösung ergeben. Euer eigener Einwand §11.7 trifft das gewählte Beispiel direkt.

---

## 4. Stärkste konkurrierende Erklärung

Nicht eine aus eurer Liste, sondern minimaler:

> **Zwei Agenten mit je einer partiellen Ordnungsrelation, ein Kontaktereignis, bei dem beide gleichzeitig handeln. Ist die Abrufaufgabe so gebaut, dass die richtige Handlung aus der Konjunktion der Relationen folgt, genügt es, dass beide *unabhängig* ihre eigene Relation befolgen — und die Umwelt integriert.**

Das ist **verteilte Constraint-Erfüllung ohne jede Integration**. Die Gruppe „löst" die Aufgabe, aber kein Agent hat je etwas zusammengeführt; die *Aufgabenstruktur* hat die Fragmente addiert. Kleinstes Modell: zwei Zustandsautomaten mit je einer Ordnungsrelation, keine Kommunikation.

**Und dieses Modell besteht Bedingung 5.** Permutiert man die Träger, geht die Leistung verloren — die falschen Agenten sind am falschen Ort. Bedingung 5 diskriminiert also *nicht* gegen die triviale Erklärung.

Das ist der schwerste Befund dieses Reviews.

---

## 5. Einschlägige Forschung — der entscheidende Abschnitt

Ich habe die Literatur geprüft. Der Befund ist unbequem und sollte den weiteren Weg bestimmen: **Große Teile des vorgeschlagenen Untersuchungsraums sind bereits besetzt, und für einen Teil existiert ein publiziertes Reduzierbarkeitsargument.**

**Transactive Memory Systems** (Wegner 1987; Lewis & Herndon 2011; Ren & Argote): <cite index="14-1">Ein TMS ist ein kollektives System für Enkodierung, Speicherung und Abruf in sozialen Systemen — „wer weiß was" — das Individuen Zugang zu mehr Information verschafft, als sie einzeln besitzen.</cite> <cite index="15-1">Das Konzept unterscheidet sich von anderen Beschreibungen sozial verteilter Kognition gerade dadurch, dass Individuen unterschiedliches Wissen halten und die Gruppenmitglieder Transaktionen ausführen, um den Abruf zu unterstützen; es besteht aus einer strukturellen Komponente (Verknüpfung individueller Gedächtnisse zum Kollektiv) und transaktiven Prozessen, die es dynamisch machen.</cite> Für euch besonders relevant: <cite index="14-1">TMS werden durch Mitglieder-Turnover gestört, und ihre Übertragung auf andere Aufgaben scheint auf Bedingungen stabiler Expertiseverteilung beschränkt.</cite> Das ist exakt die Turnover-Frage der alten Serie, bereits als bekannter Befund.

**Hidden Profile** (Stasser & Titus 1985): die etablierte Operationalisierung eurer Aufgabenklasse. <cite index="24-1">Hidden Profiles sind nur lösbar, wenn Gruppenmitglieder ihre ungeteilten Informationen austauschen und integrieren.</cite> Es existiert bereits <cite index="24-1">eine Formalisierung des Paradigmas für Multi-Agenten-Entscheidungen unter verteiltem Wissen, instanziiert als Benchmark mit neun Aufgaben.</cite>

**Das publizierte Reduzierbarkeitsargument gegen genau eure Aufgabenklasse:** <cite index="27-1">Lightle, Kagel & Arkes argumentieren, Hidden-Profile-Experimente als Beleg für Gruppenpathologien zu entwerten, weil die Ursache enger mit der Struktur des Problems zusammenhängt als mit Defiziten der Interaktion zwischen Gruppenmitgliedern.</cite> Übersetzt: **Der Befund hängt an der Aufgabenkonstruktion, nicht an der Gruppe.** Das ist euer §11.7 als publiziertes Argument — ihr müsst es nicht neu entdecken.

**Konsequenz für Frage F (ist „Schwarmgedächtnis" nur eine Umbenennung?):** Überwiegend ja, mit **einer** Ausnahme.

- Bedingungen 1, 2, 4 → TMS / Hidden Profile.
- Bedingung 5 → bekannte Netzwerk-/Verteilungsmanipulation.
- **Nur Bedingung 3 (keine externe Persistenz, keine Übertragung beim Abruf) ist neu.**

Und genau Bedingung 3 ist die, deren Kohärenz ihr in Frage E selbst bezweifelt. **Der einzige eigenständige Untersuchungsraum ist der, dessen Konsistenz ihr selbst infrage stellt.** Das ist keine Nebenbemerkung — es ist der Kern der Entscheidung, die ansteht.

---

## 6. Fehlende oder ungeeignete Kontrollen

**Fehlend, entscheidend:** Eine Kontrolle, die *Integration* von *paralleler Constraint-Erfüllung* trennt (§4). Nötig wäre eine Bedingung, in der die Fragmente *nicht* additiv zur Lösung führen.

**Fehlend:** Eine operationalisierte Kontrolle gegen den externen Auswerter. §7 Punkt 3 nennt das Problem, aber keine Kontrolle prüft es. Wie zeigt ihr, dass die Population integriert und nicht ihr?

**Ungeeignet:** Bedingung 5 als Diskriminierungsinstrument. Sie diskriminiert gegen „keine Verteilung", nicht gegen „triviale Verteilung".

---

## 7. Entscheidendes Vorab-Verwerfungskriterium

Genau eines, ohne Code beantwortbar:

> **Existiert eine Abrufaufgabe, deren Lösung erfordert, dass mindestens ein Agent eine Handlung ausführt, die aus seinem eigenen Fragment allein nicht ableitbar ist — und die er auch nicht durch Übermittlung des fremden Fragments ableiten könnte?**

Wird das nicht mit Ja beantwortet, ist die Aufgabenklasse zu verwerfen. Denn dann gilt: Entweder die Fragmente sind additiv (verteilte Constraint-Erfüllung, kein Gedächtnis), oder die Lösung braucht Übertragung (Kommunikation, kein Gedächtnis). **Der Raum dazwischen — den ihr Schwarmgedächtnis nennt — muss erst als nichtleer gezeigt werden, bevor irgendein Design sinnvoll ist.**

---

## 8. Empfehlung für den nächsten zulässigen Schritt

Nicht Kandidatenrunde drei. Nicht Architektur. Sondern:

**Zeigt, dass der begriffliche Raum nichtleer ist.** Konstruiert *eine einzige* Abrufsituation — auf Papier, formal, ohne Simulation —, die das Kriterium aus §7 erfüllt.

- Gelingt es: Der Strategiewechsel ist gerechtfertigt, die Aufgabenklasse kann geprüft werden.
- Gelingt es nicht: „Schwarmgedächtnis" im beanspruchten Sinn ist möglicherweise ein leerer Begriff — und das wäre ein präziser, begründeter Negativbefund mit Anschluss an die Distributed-Cognition-Debatte, kein Scheitern.

**Vorrangig, bevor irgendetwas anderes geschieht:** Der Literaturbefund (§5) muss in die Planung eingearbeitet werden. Es ist nicht zu untersuchen, was bereits etabliert oder bereits als reduzierbar gezeigt ist. Konkret zu klären, bevor Ressourcen fließen:

1. Was genau leistet euer Ansatz, das TMS und Hidden Profile nicht schon leisten?
2. Trägt das Lightle/Kagel/Arkes-Argument auch gegen eure Fassung — und wenn nein, warum nicht?
3. Ist Bedingung 3 (keine Übertragung beim Abruf) kohärent? Wenn ja, ist sie euer einziger eigenständiger Beitrag und gehört ins Zentrum. Wenn nein, ist der Ansatz eine Umbenennung.

Budget: keines betroffen. Konzeptphase, kein Freeze, kein Kernlauf.
