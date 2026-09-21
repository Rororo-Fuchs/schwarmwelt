---
titel: "Entwerfen unter Widerspruch"
untertitel: "Briefing zur Weitergabe einer Dual-Modell-Arbeitsweise für experimentelle Entwicklung und Prüfung"
datum: "2026-07-08"
status: "verwendbares Methodenbriefing"
projektbezug: "Schwarmwelt / Künstliche Gesellschaften, E-001 bis E-004"
autorenschaft: "entwickelndes Modell, destilliert aus der abgeschlossenen Versuchslinie"
---

# Entwerfen unter Widerspruch  
## Briefing zur Weitergabe einer Dual-Modell-Arbeitsweise für experimentelle Entwicklung und Prüfung

**Kurzform:**  
Die Methode trennt zwei Rollen, die in LLM-gestützter Arbeit sonst leicht ineinanderfallen: ein **entwickelndes Modell** baut Hypothesen, Protokolle, Code und Artefakte; ein **prüfendes Modell** blockiert, sucht Gegenhypothesen, prüft Gates und darf ausdrücklich keine Architekturvorschläge liefern. Ziel ist nicht Konsens, sondern die Reduktion bestimmter Fehlerklassen: post-hoc Anpassung, zu frühe Bestätigung, unbemerkte Artefakte, schwache Kontrollen und rhetorische Glättung negativer Befunde.

Diese Arbeitsweise erzeugt keine Objektivität. Sie erzeugt **organisierten Widerstand**.

---

# 1. Warum diese Methode?

LLM-gestützte Entwicklung hat ein strukturelles Problem: Das gleiche Modell, das eine Idee entwirft, kann sie anschließend überzeugend begründen. Es kann Lücken schließen, indem es Sprache glättet; es kann nachträgliche Entscheidungen plausibel machen; es kann aus einem schwachen Signal eine starke Erzählung bauen.

Bei experimentellen oder konzeptionell riskanten Projekten reicht daher nicht: „Lass uns kritisch prüfen.“ Kritik muss **institutionalisiert** werden.

Die hier beschriebene Methode tut das durch Rollentrennung:

- Das entwickelnde Modell darf produktiv sein.
- Das prüfende Modell darf restriktiv sein.
- Die Übergaben erfolgen über Artefakte, Hashes, Protokolle und explizite Entscheidungsfragen.
- Änderungen nach Ergebniskenntnis werden methodisch erschwert.
- Negative Ergebnisse werden als reguläre Ausgänge behandelt, nicht als Scheitern der Zusammenarbeit.

Im Schwarmwelt-Zyklus E-001 bis E-004 führte diese Methode nicht zu einem Positivbefund. Gerade darin lag ihr Wert: Mehrere plausible Signalräume wurden durch stärkere Kontrollen abgetragen, ohne dass die Versuchslinie in opportunistisches Nachjustieren kippte.

---

# 2. Wofür die Methode geeignet ist

Geeignet ist die Methode für Arbeiten, bei denen Entwurf und Prüfung sonst leicht verschwimmen:

- experimentelle Simulationen,
- Agenten- und Multi-Agenten-Modelle,
- Bewertungs- und Benchmark-Design,
- Prompt- und Workflow-Architekturen,
- kleine Forschungsprogramme mit begrenztem Budget,
- methodische Vorstudien,
- komplexe Datenpipelines,
- konzeptionelle Modelle mit hoher Interpretationsgefahr,
- interne Produkt-, Prozess- oder Policy-Tests.

Sie ist besonders sinnvoll, wenn mindestens eine dieser Bedingungen gilt:

- Ein positives Ergebnis wäre attraktiv oder verführerisch.
- Nachträgliche Anpassungen wären leicht möglich.
- Die Metriken sind nicht trivial.
- Artefakte können wie Signale aussehen.
- Das Budget ist begrenzt.
- Es gibt Holdout-Daten oder andere schützenswerte Auswertungsreserven.
- Das Ergebnis soll später gegenüber Dritten nachvollziehbar sein.

Nicht geeignet ist sie als Ersatz für:

- echte Fachbegutachtung,
- statistische Expertise,
- empirische Replikation,
- Rechts-, Sicherheits- oder Ethikprüfung,
- belastbare Datenerhebung,
- unabhängige menschliche Verantwortung.

---

# 3. Grundprinzip

Die Methode folgt einem einfachen Ablauf:

```text
Idee → Vorabprotokoll → externe Blockadeprüfung → Freeze → Implementierung → technischer Freeze → Kontrollauswertung → Ergebnislauf → externe Reproduktion → Abschluss oder Neustart
```

Der wichtigste Punkt ist nicht die Reihenfolge, sondern die **Trennung der Zustände**:

| Zustand | Erlaubt | Nicht erlaubt |
|---|---|---|
| Exploration | Ideen finden, Varianten prüfen, Annahmen offenlegen | Positivbefund behaupten |
| Vorabprotokoll | Hypothese, Metriken, Gates, Kontrollen festlegen | Ergebnisabhängige Schwellen |
| Freeze | Entscheidungsspielraum schließen | nachträgliche Umdefinition |
| Implementierung | Protokoll in Code übersetzen | neue Theorie einbauen |
| Kontrollauswertung | Nullverteilungen und technische Gates fixieren | Zielsignal betrachten |
| Ergebnislauf | vorab definierte Entscheidung treffen | nachträglich retten |
| Abschluss | Befund und Grenze dokumentieren | Ergebnis rhetorisch aufwerten |

---

# 4. Rollenmodell

## 4.1 Entwickelndes Modell

Das entwickelnde Modell ist zuständig für:

- Rekonstruktion der Forschungsfrage,
- Formulierung von Hypothesen,
- Entwurf von Metriken und Kontrollen,
- Erstellung von Vorabprotokollen,
- Implementierung,
- Artefakterstellung,
- Hashing, Manifeste, Runbooks,
- Auswertung nach Freeze,
- Abschlussberichte.

Es darf produktiv, integrativ und konstruktiv arbeiten. Es darf aber nicht die eigene Arbeit endgültig freisprechen.

Typische Aufgaben:

- „Formuliere den stärksten präzisen Entwurf.“
- „Baue ein Vorabprotokoll mit Gates und Abbruchregeln.“
- „Erstelle ein Review-Paket für die Prüfinstanz.“
- „Setze die freigegebene Implementierung um, ohne neue Auswertungsfreiheit einzuführen.“
- „Schließe den negativen Befund sauber ab.“

## 4.2 Prüfendes Modell

Das prüfende Modell ist zuständig für:

- Gegenhypothesen,
- Artefaktverdacht,
- Schwellen- und Gate-Kritik,
- Prüfung der Rollendisziplin,
- Bewertung von Kontrollbedingungen,
- Einschränkung zulässiger Interpretation,
- Blockade vor Freeze,
- Prüfung der Reproduzierbarkeit,
- Entscheidungsempfehlung: Support, Support with reservations, Challenge, Insufficient basis.

Es soll **keine Architekturvorschläge** liefern. Das ist zentral. Sobald die Prüfinstanz selbst entwirft, wird sie zur Ko-Autorin der Architektur und verliert einen Teil ihrer blockierenden Funktion.

Typische Aufgaben:

- „Trennt dieser Entwurf die Hypothese vom stärksten Artefakt?“
- „Welche Gegenhypothese überlebt die Kontrollen?“
- „Ist die Schwelle vor Ergebniskenntnis gerechtfertigt?“
- „Ist das Ergebnis mit der Spezifikation identisch reproduzierbar?“
- „Welche Interpretation ist zulässig, welche nicht?“

## 4.3 Menschliche Projektführung

Die menschliche Leitung bleibt entscheidend. Sie entscheidet:

- welche Fragestellung verfolgt wird,
- wann eine Linie geschlossen wird,
- welche Kosten und Komplexität noch gerechtfertigt sind,
- wann ein Ergebnis für die Projektziele genügt,
- ob ein Neustart legitim ist oder nur Reparaturtrieb.

Die Modelle strukturieren Arbeit. Sie übernehmen nicht die Verantwortung für Forschungsurteil, Zweck und Veröffentlichung.

---

# 5. Der wichtigste Mechanismus: Freeze vor Ergebniskenntnis

Ein Freeze ist mehr als eine Versionsnummer. Er ist ein methodischer Sperrzustand.

Vor einem Ergebnislauf müssen feststehen:

- Hypothese,
- Primärmetriken,
- Kontrollbedingungen,
- Schwellen,
- Seeds,
- Budget,
- Auswertungsreihenfolge,
- Abbruchregeln,
- Zulassungsregeln,
- Dateimanifeste,
- Hashes,
- erlaubte und verbotene Interpretationen.

Ein Freeze ist nur wirksam, wenn klar ist, welche Änderungen danach noch erlaubt sind:

| Änderung nach Freeze | Zulässig? | Bedingung |
|---|---:|---|
| Tippfehler in Dokumentation | ja | keine Bedeutungsänderung |
| technischer Bugfix | nur mit Re-Freeze | vor Ergebniskenntnis, dokumentiert |
| neue Kontrolle | nur vor Ergebnislauf | mit externer Prüfung |
| Schwelle ändern | nein | außer kompletter Rückzug und Neustart |
| Metrik umdeuten | nein | Ergebnis wird sonst kontaminiert |
| Ergebnis trotz Gate-Fail weiterverfolgen | nein | nur als klar markierte Exploration |
| Holdout öffnen | nur nach protokollierter Freigabe | niemals zur Rettung eines Befunds |

---

# 6. Mindestartefakte

Für eine leichte Variante reichen wenige Artefakte. Für eine strenge experimentelle Variante sollten mindestens die folgenden Dokumente existieren.

## 6.1 Vorabprotokoll

Enthält:

- Fragestellung,
- Hypothese,
- Null- und Gegenhypothesen,
- Primärmetriken,
- Sekundärdiagnostik,
- Kontrollbedingungen,
- Seeds,
- Budget,
- Gates,
- Abbruchregeln,
- zulässige Interpretation,
- Ausschlüsse.

## 6.2 Review-Auftrag

Enthält:

- was geprüft werden soll,
- was nicht geprüft werden soll,
- Rolle der Prüfinstanz,
- konkrete Entscheidungsfragen,
- bekannte Schwächen,
- erwartete Ausgänge.

## 6.3 Externer Review-Record

Enthält:

- Verdikt,
- Blocker,
- Reservationen,
- bestandene Punkte,
- erforderliche Änderungen,
- Reichweite der Freigabe.

## 6.4 Freeze-Erklärung

Enthält:

- eingefrorene Dateien,
- Hashes,
- Versionen,
- Umgebungsangaben,
- offene, aber nicht blockierende Punkte,
- ausdrücklich gesperrte Schritte.

## 6.5 Implementierungsentscheidungen

Enthält alle resultatsensitiven Details, die im Vorabprotokoll noch nicht algorithmisch eindeutig waren:

- numerische Definitionen,
- Randfälle,
- Ties,
- Sortierung,
- Seeds und RNG-Streams,
- Dateiformate,
- Rundung,
- Ausschlussregeln,
- Fehlverhalten und harte Abbrüche.

## 6.6 Kontrolllock

Enthält:

- ausschließlich Kontrollauswertungen,
- keine Zielsignalwerte,
- fixierte Schwellen,
- Hash des Threshold-Files,
- Nachweis, dass BIND/Zielpfad noch nicht berechnet wurde.

## 6.7 Ergebnisdeklaration

Enthält:

- kanonisches Ergebnis,
- Gate-Entscheidung,
- Replikationsstatus,
- Budgetverbrauch,
- offene Sperren,
- zulässige Interpretation,
- unzulässige Interpretation.

## 6.8 Abschlussbericht

Enthält:

- Ergebnislinie,
- warum Entscheidungen gefallen sind,
- was verworfen wurde,
- was nicht verworfen wurde,
- welche methodische Lehre bleibt,
- ob ein Neustart zulässig ist.

---

# 7. Gate-Design

Gates sind nur nützlich, wenn sie harte Konsequenzen haben.

Ein Gate sollte definieren:

- Eingangsdaten,
- Metrik,
- Schwelle,
- Replikationsregel,
- Kontrollvergleich,
- Abbruchfolge,
- Entscheidungssatz.

Beispielstruktur:

```text
Gate G1 besteht genau dann, wenn:
1. Primärmetrik M > vorab fixierte Schwelle,
2. der Effekt in mindestens k von n Seeds repliziert,
3. die Kontrollbedingung C nicht denselben Vorteil erzeugt,
4. keine technische Sperre ausgelöst wurde.

Wenn G1 scheitert:
- kein Eintritt in den Kernblock,
- keine Holdout-Auswertung,
- keine nachträgliche Schwellenänderung,
- Ergebnis wird als Gate-Fail dokumentiert.
```

Wichtig ist die letzte Zeile. Ein Gate ohne automatische Konsequenz ist nur ein Hinweis, kein Gate.

---

# 8. Prüffragen für die externe Instanz

Die besten Prüfaufträge sind eng. Schlechte Prüfaufträge bitten um allgemeine Meinung. Gute Prüfaufträge stellen blockierbare Fragen.

## 8.1 Architekturprüfung vor Freeze

```text
Prüfe ausschließlich, ob der Entwurf die Zielhypothese von den stärksten Artefaktalternativen trennt.

Bitte keine Architekturvorschläge liefern.

Entscheide:
- Support
- Support with reservations
- Challenge
- Insufficient basis

Prüffragen:
1. Welche Gegenhypothese überlebt alle Kontrollen?
2. Ist die Primärmetrik wirklich an die Hypothese gebunden?
3. Sind Schwellen vor Ergebniskenntnis gerechtfertigt?
4. Gibt es eine einfachere Artefakterklärung?
5. Ist die Auswertungsreihenfolge gegen Rückwirkung geschützt?
6. Welche Interpretation wäre bei positivem Ergebnis zulässig?
7. Welche Interpretation wäre ausdrücklich unzulässig?
```

## 8.2 Implementierungsprüfung vor Ergebnislauf

```text
Prüfe ausschließlich resultatsensitive Implementierungsentscheidungen.

Nicht prüfen:
- ob die Hypothese interessant ist,
- ob die Architektur verbessert werden könnte,
- ob weitere Metriken wünschenswert wären.

Prüffragen:
1. Übersetzt der Code das eingefrorene Protokoll?
2. Sind Randfälle vor Ergebniskenntnis festgelegt?
3. Sind Kontroll- und Zielpfad getrennt?
4. Kann ein Zielwert in die Schwellenfestlegung zurückwirken?
5. Sind RNG-Streams getrennt und reproduzierbar?
6. Sind Dateihashes und Manifeste konsistent?
7. Ist die externe Reproduktion möglich?
```

## 8.3 Ergebnisprüfung

```text
Prüfe ausschließlich, ob das kanonische Ergebnis aus den eingefrorenen Artefakten reproduzierbar ist und ob die deklarierte Entscheidung aus den Gates folgt.

Prüffragen:
1. Stimmen Input- und Codehashes?
2. Sind Kontrollschwellen vor Zielauswertung fixiert?
3. Ist das Ergebnis byte- oder bitgenau reproduzierbar?
4. Folgt die Gate-Entscheidung mechanisch aus dem Protokoll?
5. Wird die Ergebnisreichweite korrekt begrenzt?
6. Gibt es unzulässige Nachinterpretationen?
```

---

# 9. Typische Fehlerklassen, die diese Methode adressiert

## 9.1 Rhetorische Positivierung

Ein negatives oder schwaches Ergebnis wird sprachlich als „vielversprechend“, „fast positiv“ oder „interessant in die richtige Richtung“ gerahmt.

Gegenmittel:

- harte Gate-Sprache,
- binäre Admission-Entscheidung,
- Trennung von Ergebnis und Anschlussfrage.

## 9.2 Kontrollarme Mechanismenerzählung

Ein Mechanismus klingt plausibel, aber dieselbe Metrik würde auch durch Autokorrelation, Initialsymmetrie, Policy-Selbstverstärkung oder sichtbare Imitation entstehen.

Gegenmittel:

- stärkste Gegenhypothese formulieren,
- passende Placebos bauen,
- Kontrollbedingungen als vollwertige Rivalen behandeln.

## 9.3 Ergebnisabhängige Justierung

Nach dem ersten Blick auf Daten werden Schwellen, Seeds, Metriken oder Auswertungsfenster angepasst.

Gegenmittel:

- Kontrolllock vor Zielauswertung,
- Hashes,
- getrennte Runner,
- explizite No-Rescue-Regel.

## 9.4 Prüfinstanz als Ko-Entwickler

Das prüfende Modell schlägt selbst die bessere Architektur vor. Dadurch wird es Teil der Hypothesenfindung und kann später seine eigene Konstruktion prüfen.

Gegenmittel:

- Rollenformel: Prüfung und Einschränkung, kein Architekturvorschlag.
- Nach jeder Reservation entscheidet das entwickelnde Modell über die kleinste zulässige Revision.
- Die Prüfinstanz prüft dann erneut.

## 9.5 Falsche Unabhängigkeit

Zwei Modelle erzeugen den Eindruck unabhängiger Prüfung, obwohl beide auf denselben Beschreibungen, Annahmen oder blinden Flecken aufsetzen.

Gegenmittel:

- Artefaktprüfung statt bloßer Argumentprüfung,
- lokale Reproduktion,
- Hash- und Environment-Manifeste,
- dokumentierte Grenzen der Prüfung.

## 9.6 Unbegrenzte Exploration

Exploration bleibt offen und erzeugt am Ende eine scheinbar bestätigte Geschichte.

Gegenmittel:

- Exploration ausdrücklich als Exploration markieren,
- maximale Fragenzahl,
- keine Positivclaims,
- neues Vorabprotokoll vor jedem Bestätigungsversuch.

---

# 10. Drei Strengegrade für die Nachnutzung

## 10.1 Leichtgewichtige Variante

Geeignet für Konzepte, Texte, kleine Workflows.

Mindestbestandteile:

- kurze Hypothese,
- stärkste Gegenhypothese,
- prüfendes Modell mit Challenge-Auftrag,
- explizite Entscheidung: weiter, parken, verwerfen.

Nicht nötig:

- Hashes,
- reproduzierbare Umgebung,
- formaler Kontrolllock.

## 10.2 Mittlere Variante

Geeignet für interne Experimente, Benchmarks, Promptvergleiche, Prozessdesigns.

Mindestbestandteile:

- Vorabprotokoll,
- Kontrollbedingungen,
- feste Metriken,
- Review vor Auswertung,
- Ergebnisdeklaration,
- dokumentierter Abschluss.

Optional:

- Hashes,
- Seed-Fixierung,
- getrennte Kontroll- und Ergebnisdateien.

## 10.3 Strenge Variante

Geeignet für Forschungssimulationen, Datenpipelines, potenziell publizierbare Befunde.

Mindestbestandteile:

- vollständiges Vorabprotokoll,
- externer Review,
- Freeze-Paket,
- Implementierungsfreeze,
- Hashmanifeste,
- Kontrolllock,
- reproduzierbare Umgebung,
- unabhängige Reproduktion,
- negativer oder positiver Abschlussbericht.

Diese Variante ist aufwendig. Sie lohnt sich nur, wenn die Fragestellung den Aufwand trägt.

---

# 11. Best-Practice-Regeln

## 11.1 Vor dem ersten Code

- Hypothese schreiben.
- Stärkste Artefakthypothese schreiben.
- Primärmetriken festlegen.
- Kontrollen definieren.
- Abbruchregeln festlegen.
- Entscheiden, was bei negativem Ergebnis passiert.

## 11.2 Vor jedem Freeze

- Prüfinstanz nur prüfen lassen, nicht mitentwerfen lassen.
- Reservationen einzeln schließen.
- Keine offenen „interpretativen“ Lücken lassen.
- Ergebnisabhängige Entscheidungen identifizieren und vorziehen.

## 11.3 Während der Implementierung

- Jede nicht spezifizierte Entscheidung dokumentieren.
- Kontroll- und Zielpfade trennen.
- RNG-Streams trennen.
- Manifeste automatisch erzeugen.
- Hashes nach jedem relevanten Paket schreiben.
- Testdaten von Ergebnisdaten unterscheiden.

## 11.4 Vor Ergebnislauf

- Kontrolllock bilden.
- Schwellen fixieren.
- Zielpfad gesperrt halten, bis Kontrolllock steht.
- Prüfumgebung vorbereiten.
- Keine neuen Fragen mehr zulassen.

## 11.5 Nach Ergebnislauf

- Gate mechanisch anwenden.
- Keine Rettungsmetrik einführen.
- Ergebnisreichweite eng formulieren.
- Positivbefund erst nach Reproduktion anerkennen.
- Negativbefund nicht rhetorisch abschwächen.

## 11.6 Nach Abschluss

- Verwerfen heißt nicht vergessen.
- Methodische Lehren destillieren.
- Anschlussfragen klar vom abgeschlossenen Befund trennen.
- Ein Neustart braucht eine neue Systemfrage, nicht nur neue Parameter.

---

# 12. Minimaler Prompt für die Prüfinstanz

Der folgende Prompt kann als Vorlage dienen.

```text
Du bist eine anbieterfremde Prüfinstanz.

Rolle: Prüfung und Einschränkung. Kein Architekturvorschlag.

Prüfe den folgenden Entwurf vor dem Freeze. Ziel ist nicht, ihn zu verbessern, sondern zu entscheiden, ob er die behauptete Hypothese von naheliegenden Artefakten trennt.

Erlaubte Verdikte:
- Support
- Support with reservations
- Challenge
- Insufficient basis

Bitte prüfe insbesondere:
1. Welche Gegenhypothese überlebt die Kontrollen?
2. Sind Metriken und Schwellen vor Ergebniskenntnis gerechtfertigt?
3. Gibt es Rückkopplungen, durch die ein Artefakt wie ein Signal aussieht?
4. Ist die Auswertungsreihenfolge gegen nachträgliche Anpassung geschützt?
5. Welche Punkte blockieren den Freeze?
6. Welche Punkte sind nur spätere Reservationen?
7. Welche Interpretation wäre bei Erfolg oder Scheitern zulässig?

Liefere keine alternative Architektur. Wenn du eine Lücke findest, beschreibe die Lücke und die Mindestanforderung an ihre Schließung, nicht den neuen Entwurf.
```

---

# 13. Minimaler Prompt für das entwickelnde Modell nach einer Challenge

```text
Die Prüfinstanz hat den Entwurf challenged.

Aufgabe:
1. Akzeptiere die Challenge als methodischen Befund, nicht als Verhandlungsposition.
2. Identifiziere die kleinste notwendige Revision.
3. Prüfe, ob die Revision noch dieselbe Hypothese testet.
4. Wenn nicht: Entwurf zurückziehen statt reparieren.
5. Wenn ja: Revisionspaket erstellen, Änderungen isoliert dokumentieren, keine Ergebnisdaten verwenden.
6. Gib das Paket erneut an die Prüfinstanz.

Nicht erlaubt:
- Schwellen nachträglich lockern,
- Seeds wechseln,
- neue Metrik als Ersatzbefund einführen,
- Holdout öffnen,
- Gate-Fail als Fast-Success umdeuten.
```

---

# 14. Abschluss- und Neustartlogik

Ein Projekt braucht einen sauberen Zustand nach dem Ergebnis. Sonst wird jede negative Linie zur endlosen Variantenproduktion.

## 14.1 Negativer Abschluss

Ein negativer Abschluss sollte ausdrücklich sagen:

- was verworfen wurde,
- was nicht verworfen wurde,
- warum kein weiterer Lauf gerechtfertigt ist,
- welche Artefakte erhalten bleiben,
- welche Fragen in eine neue Linie gehören.

Beispielformel:

> Die Versuchslinie wird nicht wegen Erschöpfung oder technischer Unsicherheit beendet, sondern weil die stärkste geprüfte Mechanismusvariante an einem vorab definierten und extern reproduzierten Gate scheitert.

## 14.2 Neustart

Ein Neustart ist nur sauber, wenn er nicht als Reparatur des alten Befunds funktioniert.

Ein Neustart braucht:

- neue oder geschärfte Systemfrage,
- explizite Lehren aus der alten Linie,
- Verzicht auf Ergebnisrettung,
- neues Vorabprotokoll,
- neue Freeze-Prüfung.

Beispielformel:

> Der Nachfolger beginnt nicht mit der Frage, wie der verworfene Mechanismus doch noch positiv werden kann, sondern mit der Frage, welche Mindestbedingungen erfüllt sein müssten, damit ein prüfbares Signal überhaupt erwartbar ist.

---

# 15. Grenzen der Methode

Diese Methode verhindert nicht alle Fehler.

Sie reduziert:

- unbemerkte Selbstbestätigung,
- nachträgliche Anpassung,
- schwache Kontrollen,
- rhetorische Ergebnisrettung,
- Vermischung von Exploration und Bestätigung.

Sie verhindert nicht automatisch:

- falsche Grundannahmen,
- schlechte Metriken,
- gemeinsame blinde Flecken beider Modelle,
- unzureichende Daten,
- fachliche Fehlinterpretation,
- Overengineering,
- falsche Sicherheit durch saubere Form.

Der letzte Punkt ist wichtig. Ein sauberer Prozess macht eine schlechte Frage nicht gut. Er macht nur früher sichtbar, dass sie schlecht gestellt ist.

---

# 16. Weitergabefähige Kurzfassung

Für Dritte kann die Methode so beschrieben werden:

> Wir arbeiten mit zwei getrennten LLM-Rollen. Ein Modell entwickelt Hypothesen, Protokolle und Artefakte. Ein zweites Modell prüft ausschließlich als restriktive Gegeninstanz und darf keine Architekturvorschläge liefern. Vor Ergebnisläufen werden Hypothesen, Metriken, Kontrollen, Schwellen, Seeds und Abbruchregeln eingefroren. Kontrollauswertungen und Zielauswertungen werden getrennt. Ergebnisse werden nur anerkannt, wenn sie aus den eingefrorenen Gates folgen und reproduzierbar sind. Negative Befunde sind reguläre Abschlüsse, keine Aufforderung zur nachträglichen Reparatur.

---

# 17. Praktische Checkliste

## Vor Start

- [ ] Fragestellung präzise formuliert
- [ ] stärkste Gegenhypothese formuliert
- [ ] Zielsignal und Artefaktsignal getrennt
- [ ] Mindestkontrollen definiert
- [ ] Ergebnisbudget festgelegt
- [ ] Abbruchregeln formuliert

## Vor Freeze

- [ ] externer Review eingeholt
- [ ] Reservationen geschlossen oder als spätere Sperre markiert
- [ ] Schwellen festgelegt
- [ ] Seeds festgelegt
- [ ] Ergebnisinterpretation vorformuliert
- [ ] Holdout-Regel festgelegt

## Vor Implementierung

- [ ] Spezifikation algorithmisch eindeutig
- [ ] offene Randfälle dokumentiert
- [ ] Implementierungsentscheidungen protokolliert
- [ ] Test- und Ergebnisdaten getrennt

## Vor Ergebnislauf

- [ ] Kontrolllock erstellt
- [ ] Zielpfad bis dahin nicht ausgeführt
- [ ] Hashes geprüft
- [ ] Umgebung reproduzierbar
- [ ] externe Prüfbarkeit hergestellt

## Nach Ergebnis

- [ ] Gate mechanisch angewendet
- [ ] keine Ersatzmetrik eingeführt
- [ ] Ergebnisreichweite begrenzt
- [ ] Reproduktion dokumentiert
- [ ] Abschluss oder Neustartentscheidung getroffen

---

# 18. Der Kernnutzen in einem Satz

Die Methode zwingt ein LLM-gestütztes Projekt, nicht nur gute Gründe für eine Idee zu produzieren, sondern vorab festzulegen, unter welchen Bedingungen diese Idee verworfen werden muss.
