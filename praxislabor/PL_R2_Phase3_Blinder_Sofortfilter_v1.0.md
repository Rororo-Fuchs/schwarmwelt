# PL-R2 — Phase 3: Blinder Sofortfilter v1.0

**Datum:** 2026-07-11  
**Grundlagen:** `PL_R2_Suchprozess_Freeze_v1.0.md`, `PL_R2_Rohkandidaten_v1.0.md`, `PL_R2_Phase2_Entdoppelung_v1.0.md`  
**Status:** Phase 3 abgeschlossen  
**Prüfgegenstand:** ausschließlich die zehn vorab eingefrorenen Sofort-Verwerfungskriterien  
**Nicht zulässig:** Reparatur, Verbesserung, Verteidigung, Agentenarchitektur oder vollständige Prüfung nach G1–G6

---

## 1. Entscheidungsregel

Ein Kandidat wird sofort verworfen, wenn mindestens eines der im Suchprozess-Freeze festgelegten Kriterien bereits aus seiner Rohbeschreibung folgt.

Verdikte:

- `bestehen`
- `verwerfen`
- `unentscheidbar`

`Unentscheidbar` bedeutet nicht, dass der Kandidat positiv bewertet ist. Es bedeutet nur, dass aus der knappen Rohbeschreibung noch kein Sofort-Verwerfungskriterium sicher folgt. Solche Kandidaten gehen in Phase 4.

---

## 2. Ergebnisübersicht

| ID | Prozessklasse | Verdikt | Ausschlaggebender Punkt |
|---|---|---|---|
| **PL-R2-K01** | verzweigte gemeinsame Fortsetzung | **verwerfen** | kurze Markov-Historie und plausible offene Sequenz genügen |
| **PL-R2-K03** | gemeinsam erzeugter Begegnungsabschluss | **verwerfen** | privater Timer beziehungsweise feste Abschlussroutine; unilaterales Beenden |
| **PL-R2-K04** | dyadische Bildung funktionaler Äquivalenzen | **unentscheidbar** | möglicherweise nur partnerbezogene Reaktionstabelle oder Kalibrierung |
| **PL-R2-K05** | Übergabe gemeinsamer Orientierung | **verwerfen** | aktuelle Ereignissalienz und unmittelbares Folgen genügen |
| **PL-R2-K06** | komplementäre Vervollständigung einer offenen Handlung | **unentscheidbar** | möglicherweise nur Partner-ID-Zuordnung zu Endpunkt und Fortsetzung |
| **PL-R2-K08** | selektive Aufnahme in einer dichten Handlungsfolge | **verwerfen** | privater Positionszähler, Salienzgewicht oder kurze Markov-Historie genügen |

---

## 3. Einzelprüfungen

### PL-R2-K01 — Verzweigte gemeinsame Fortsetzung

**Verdikt:** `verwerfen`

Die beschriebenen Verlaufsformen sind kurze Folgen aus drei sichtbaren Aktionen. Welche Handlung anschlussfähig ist, kann durch die letzten ein bis zwei öffentlich sichtbaren Handlungen bestimmt werden. Der Rohkandidat benennt selbst einen endlichen Zustandsautomaten aus genau dieser kurzen Historie als stärksten einfachen Gegner.

Eine plausible aufgezeichnete Sequenz kann die beschriebenen Schleifen ebenfalls erzeugen, solange der reale Agent ihr folgt. Für den Kandidaten ist nicht spezifiziert, dass eine unerwartete Abweichung eine historisch spezifische, geschlossene Gegenreaktion verlangt.

**Ausgelöste Sofortkriterien:**

- **Kriterium 2:** aktuelle Beobachtung plus kurze Markov-Historie genügt;
- **Kriterium 8:** eine aufgezeichnete plausible Partnersequenz kann die beschriebene Ordnung prinzipiell ersetzen.

---

### PL-R2-K03 — Gemeinsam erzeugter Begegnungsabschluss

**Verdikt:** `verwerfen`

Die Folge aus Fortsetzen, Abschwächen und Lösen kann durch eine feste private Abschlussroutine oder einen privaten Timer erzeugt werden. Zwei kompatible Routinen können einen parallelen oder versetzten Abschluss hervorbringen, ohne dass konkrete gemeinsame Geschichte nötig ist.

Zusätzlich kann ein einzelner Agent die Begegnung durch einseitiges Lösen abrupt beenden. Damit ist die Begegnungsgrenze zumindest in einer zentralen Form unilateral festlegbar.

**Ausgelöste Sofortkriterien:**

- **Kriterium 3:** ein Agent kann die Grenze unilateral festlegen;
- **Kriterium 4:** privater Timer oder feste endliche Abschlussroutine genügt.

---

### PL-R2-K04 — Dyadische Bildung funktionaler Äquivalenzen

**Verdikt:** `unentscheidbar`

Die Ordnung ist formal beobachtbar: Verschiedene Aktionsindizes erhalten gleiche oder verschiedene Anschlussverteilungen. Damit wird kein semantischer Begriff benötigt.

Ungeklärt bleibt jedoch, ob die entstehenden Äquivalenzklassen tatsächlich gemeinsam und verteilt stabilisiert werden oder nur eine partnerbezogene Reaktionstabelle beziehungsweise eine formale Clusterung abbilden. Eine solche Tabelle könnte nach Partner-ID dieselben Fortsetzungen erzeugen, ohne dass die konkrete Episodenfolge weiter erforderlich ist.

Aus der Rohbeschreibung folgt noch nicht sicher, dass Geschichte ausschließlich Partnerkalibrierung leistet; ebenso wenig ist ausgeschlossen, dass dies die vollständige Erklärung ist.

**Gefährdete, aber noch nicht sicher ausgelöste Sofortkriterien:**

- **Kriterium 2:** kurze Reaktionstabelle könnte genügen;
- **Kriterium 7:** Geschichte könnte nur Partnerkalibrierung leisten.

Der Kandidat geht unverändert in Phase 4.

---

### PL-R2-K05 — Übergabe gemeinsamer Orientierung

**Verdikt:** `verwerfen`

Aktuelle Ereignispositionen, deren verbleibende Sichtbarkeit und die sichtbare Orientierung des Partners liefern alle Informationen, die eine einfache Blickfolge- oder Salienzpolicy benötigt. Initiation, Folgen, Halten und Umlenken lassen sich als unmittelbare Reaktionen auf den aktuellen Fokus erzeugen.

Eine aufgezeichnete plausible Orientierungsfolge kann dieselben gemeinsamen Fokusphasen herstellen. Die Rohbeschreibung verlangt keine Abweichung, auf die der Partner historisch spezifisch reagieren müsste.

**Ausgelöste Sofortkriterien:**

- **Kriterium 2:** aktuelle Beobachtung und kurze Reaktionshistorie genügen;
- **Kriterium 8:** plausibles Ghost-Replay kann die beschriebene Interaktion prinzipiell ersetzen.

---

### PL-R2-K06 — Komplementäre Vervollständigung einer offenen Handlung

**Verdikt:** `unentscheidbar`

Der Partnerbeitrag ist physisch konstitutiv: Ohne ihn entsteht keiner der beiden Endpunkte. Damit kann der Initiator die vollständige Handlung nicht offensichtlich allein herstellen.

Der beschriebene Unterschied zwischen Endpunkt X und Y könnte jedoch vollständig durch eine Partner-ID-basierte Zuordnung getragen werden:

`offene Anfangshandlung + Partner-ID → Endpunkt und Fortsetzung`

Dann würde Geschichte nur dazu dienen, die Präferenz oder Policy des Partners zu identifizieren. Ob beide Agenten die Zuordnung gemeinsam verändern und aufrechterhalten müssen, ist in der Rohbeschreibung nicht entschieden.

**Gefährdete, aber noch nicht sicher ausgelöste Sofortkriterien:**

- **Kriterium 2:** eine kompakte Zuordnungstabelle könnte genügen;
- **Kriterium 7:** Geschichte könnte nur Partnerkalibrierung oder Systemidentifikation leisten.

Der Kandidat geht unverändert in Phase 4.

---

### PL-R2-K08 — Selektive Aufnahme in einer dichten Handlungsfolge

**Verdikt:** `verwerfen`

Zwei der drei angegebenen Verlaufsformen sind unmittelbar durch einfache private Mechanismen erzeugbar:

- „jede zweite Handlung“ durch einen Positionszähler;
- „nach einer Zweierfolge“ durch eine kurze Markov-Historie.

Auch verzweigte Aufnahme kann durch gelernte Salienzgewichte über die letzten wenigen Aktionen erzeugt werden. Die Rohbeschreibung enthält keine zusätzliche Bedingung, durch die konkrete gemeinsame Episodenlinien gegenüber diesen Mechanismen notwendig werden.

Eine plausible aufgezeichnete Sequenz kann außerdem dieselben Antwort- und Nichtantwortpositionen reproduzieren.

**Ausgelöste Sofortkriterien:**

- **Kriterium 2:** kurze Markov-Historie beziehungsweise Salienzregel genügt;
- **Kriterium 4:** privater Positionszähler genügt;
- **Kriterium 8:** plausible aufgezeichnete Partnerfolge kann die Muster prinzipiell ersetzen.

---

## 4. Phase-3-Register

### Verworfen

- `PL-R2-K01`
- `PL-R2-K03`
- `PL-R2-K05`
- `PL-R2-K08`

Diese Kandidaten werden in den Phasen 4 bis 7 nicht weiter geprüft und innerhalb der laufenden Runde nicht repariert.

### Unentscheidbar; verbleiben für Phase 4

- `PL-R2-K04`
- `PL-R2-K06`

### Bestanden

- kein Kandidat

Das Fehlen eines Verdikts `bestehen` ist kein Abbruchgrund. Phase 4 prüft die beiden nicht sofort widerlegten Kandidaten detailliert gegen die neun Fragen.

---

## 5. Nächster zulässiger Schritt

**Phase 4 — Neun-Fragen-Prüfung**, ausschließlich für:

1. `PL-R2-K04`
2. `PL-R2-K06`

Beide Kandidaten bleiben in ihrer Rohfassung unverändert. Insbesondere werden keine Zusatzregeln eingeführt, um partnerbezogene Reaktionstabellen, Partnerkalibrierung oder Systemidentifikation nachträglich auszuschließen.
