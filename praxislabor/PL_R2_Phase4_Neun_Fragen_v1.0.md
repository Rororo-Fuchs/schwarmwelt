# PL-R2 — Phase 4: Neun-Fragen-Prüfung v1.0

**Datum:** 2026-07-11  
**Grundlagen:**  
- `PL_R2_Suchprozess_Freeze_v1.0.md`  
- `PL_R2_Rohkandidaten_v1.0.md`  
- `PL_R2_Phase2_Entdoppelung_v1.0.md`  
- `PL_R2_Phase3_Blinder_Sofortfilter_v1.0.md`  
- verbindliches PL-Handoff

**Prüfgegenstand:** ausschließlich die neun im Handoff festgelegten Fragen  
**Kandidaten:** `PL-R2-K04`, `PL-R2-K06`  
**Nicht zulässig:** Reparatur, Zusatzregel, Agentenarchitektur, Lernmethode oder vorgezogene vollständige Prüfung nach G1–G6

---

## 1. Entscheidungslogik dieser Phase

Die neun Fragen werden für die unveränderten Rohkandidaten beantwortet. Nicht spezifizierte Eigenschaften werden als offen oder fehlend markiert und nicht ergänzt.

Mögliche Phase-4-Ergebnisse:

- **verwerfen:** Bereits die Neun-Fragen-Prüfung zeigt ein strukturelles Ausschlussproblem.
- **unentscheidbar; weiter zu Phase 5:** Der Kandidat ist noch nicht tragfähig, aber die offenen Punkte gehören in die vorgesehene Prüfung nach G1–G6 und M0–M3.

---

# 2. PL-R2-K04 — Dyadische Bildung funktionaler Äquivalenzen

## Rohkern

Vier sichtbar verschiedene Handlungen besitzen dieselbe unmittelbare Umweltwirkung. Verschiedene Dyaden können die vier Handlungen in unterschiedlichen Paaren ähnlich behandeln, erkennbar an gleichen oder verschiedenen Anschlussfolgen. Die Umwelt enthält weder Kategorien noch gespeicherte Zuordnungen.

---

## Frage 1 — Welche Handlungen sind öffentlich beobachtbar?

Öffentlich beobachtbar sind:

- die Auswahl einer von vier Handlungen `A0` bis `A3`;
- die Antwort des Partners;
- die anschließende Fortsetzung des ersten Agenten;
- Substitution einer Handlung;
- Beendigung der Folge;
- die zeitliche Reihenfolge dieser Ereignisse.

Nicht öffentlich gegeben sind:

- eine Kategoriezugehörigkeit der Handlungen;
- eine Bedeutung der Handlungen;
- eine private Erwartung oder Klassifikation;
- ein gemeinsamer Zuordnungszustand.

Die behauptete Äquivalenz ist daher nur indirekt über vergleichbare Anschlussverteilungen beobachtbar.

**Befund:** formal beobachtbar, aber nur als statistische Relation zwischen Handlungsindizes und Folgehandlungen.

---

## Frage 2 — Welche mehreren Verhaltensverläufe sind möglich?

In der Rohbeschreibung sind mindestens drei Verlaufsfamilien enthalten:

1. `{A0,A1}` werden ähnlich fortgesetzt und von `{A2,A3}` unterschieden;
2. `{A0,A2}` werden ähnlich fortgesetzt und von `{A1,A3}` unterschieden;
3. die Zuordnungen wechseln, ohne eine stabile Paarbildung zu ergeben.

Zusätzlich können einzelne Folgen durch Fortsetzung, Substitution oder Abbruch enden.

Die verschiedenen Paarbildungen sind wegen identischer unmittelbarer Umweltwirkung der vier Handlungen grundsätzlich symmetrisch.

**Befund:** mehrere formal unterscheidbare Varianten sind vorhanden.

---

## Frage 3 — Wie wirken die Handlungen wechselseitig?

Die Handlung des ersten Agenten wird vom Partner beantwortet; dessen Antwort beeinflusst, ob der erste Agent fortsetzt, substituiert oder beendet.

Die Rohbeschreibung legt jedoch nicht fest, dass:

- eine Handlung des Partners die aktuellen Handlungsmöglichkeiten des ersten Agenten verändert;
- der Partner seine eigene Antwort aufgrund der vorausgehenden Reaktion revidieren muss;
- eine geschlossene Folge aus Handlung, Gegenhandlung und erneuter Gegenreaktion erforderlich ist.

Die Wechselseitigkeit kann daher vollständig als Abfolge zweier privater Reaktionstabellen realisiert werden. Eine echte kausale Schließung der Begegnung ist nicht beschrieben.

**Befund:** sequenzielle Reaktion ist vorhanden; starke Wechselseitigkeit ist nicht nachgewiesen.

---

## Frage 4 — Warum könnte Wiederholung individuelle Dispositionen und eine gemeinsame Praxis stabilisieren?

Wiederholung könnte dazu führen, dass beide Agenten bestimmte Handlungen des Partners ähnlich beantworten und dadurch dyadenspezifische Anschlussmuster erzeugen.

Eine mögliche verteilte Ordnung wäre:

- Agent A behandelt `A0` und `A1` von B ähnlich;
- B erwartet diese Behandlung und setzt beide Handlungen entsprechend fort;
- beide Seiten reproduzieren dadurch dieselbe Paarbildung.

Die Rohbeschreibung zeigt jedoch nicht, warum beide Dispositionen für die Stabilität notwendig wären. Ebenso möglich ist:

- ein Agent entwickelt eine partnerbezogene Zuordnungstabelle;
- der andere erzeugt nur die Handlungen, auf die diese Tabelle angewendet wird.

**Befund:** gemeinsame Stabilisierung ist denkbar, aber von individueller Klassifikation oder Reaktionstabelle nicht getrennt.

---

## Frage 5 — Wie könnte Valenz Episoden gewichten, ohne direkt Handlungen zu steuern?

Prinzipiell könnten vollständige Episoden mit stabiler Fortsetzung, wechselnder Zuordnung oder Abbruch unterschiedliche private Zustandsfolgen besitzen und dadurch unterschiedlich konsolidiert werden. Die Gewichtung müsste nach Abschluss der Episode erfolgen und dürfte keine der Handlungen `A0` bis `A3` unmittelbar positiv oder negativ markieren.

Der Rohkandidat enthält jedoch keine private Zustandsfolge, aus der ein solcher Valenzunterschied hervorgeht. Alle vier Handlungen haben ausdrücklich dieselbe unmittelbare Umweltwirkung. Auch ein Nutzen stabiler gegenüber instabiler Paarbildung ist nicht definiert.

Eine systematische Valenz für „kohärente“ oder „gemeinsam behandelte“ Folgen müsste daher zusätzlich eingeführt werden und würde leicht genau die gesuchte Ordnung belohnen.

**Befund:** keine nicht willkürliche Valenzgrundlage im unveränderten Kandidaten.

---

## Frage 6 — Welche einfachere nichtsoziale Erklärung ist zu erwarten?

Das kleinste naheliegende Modell ist eine partnerbezogene Reaktionstabelle:

```text
Partner-ID
+ sichtbarer Aktionsindex
→ eigene Antwort oder Fortsetzung
```

Eine Variante davon clustert Handlungsindizes anhand ähnlicher beobachteter Übergänge. Beide Modelle können dyadenspezifische Paarbildungen erzeugen, ohne:

- einen gemeinsamen Äquivalenzbegriff;
- verteilte Stabilisierung;
- fortlaufend notwendige konkrete Begegnungsgeschichte.

Die historische Erfahrung dient dann nur zum Schätzen oder Aktualisieren einer privaten Tabelle.

**Befund:** starke vollständige M3-nahe Konkurrenz durch Partnerkalibrierung.

---

## Frage 7 — Welche minimale Kontrolle trennt diese Erklärung ab?

Die unmittelbar notwendige Baseline ist ein Modell mit:

- Partner-ID;
- aktuellem Handlungsindex;
- kurzer Übergangshistorie;
- frei lernbarer privater Reaktionstabelle.

Zusätzlich wäre ein einseitiger Austausch der Lernhistorie bei unveränderter Partner-ID und identischer aktueller Folge nötig. Eine gemeinsam getragene Ordnung müsste auf den Geschichtsbruch anders reagieren als ein Modell, das nur die aktuelle Tabelle anwendet.

Der Rohkandidat enthält jedoch keine vorab bestimmte Verhaltensvorhersage für diesen Fall. Dieselben beobachtbaren Anschlussverteilungen definieren sowohl die behauptete funktionale Äquivalenz als auch die einfache Reaktionstabelle. Eine reine Verhaltenskontrolle kann beide daher in der bisherigen Fassung nicht sicher trennen.

**Befund:** notwendige Baseline benennbar; diskriminierende Minimalkontrolle im Rohkandidaten nicht operationalisiert.

---

## Frage 8 — Woran wird der Kandidat vor Implementierung verworfen?

Der Kandidat ist vor Implementierung zu verwerfen, wenn mindestens einer der folgenden Punkte gilt:

1. Eine partnerbezogene Reaktionstabelle reproduziert sämtliche Paarbildungen und Anschlussfolgen.
2. Die behauptete Äquivalenz ist nur eine nachträgliche Beschreibung ähnlicher Übergangswahrscheinlichkeiten.
3. Einseitiger Historienaustausch hat keine vorab ableitbare, von der Tabellenbaseline verschiedene Wirkung.
4. Für stabile Zuordnungen lässt sich keine private Valenzgrundlage angeben, ohne Stabilität oder Übereinstimmung selbst zu belohnen.
5. Ein plausibles Ghost-Replay erzeugt dieselben Anschlussverteilungen.
6. Ein Agent kann die Zuordnung praktisch vorgeben, während der andere sie nur registriert.

Die Punkte 1, 2 und 4 sind in der Rohfassung bereits nicht ausgeräumt.

---

## Frage 9 — Hat Koordination einen Vorteil, ohne dass die Situation festlegt, welche Koordination entsteht?

Die zweite Hälfte ist erfüllt: Die Situation bevorzugt keine bestimmte Paarbildung der vier Handlungen.

Die erste Hälfte ist nicht erfüllt. Die Rohbeschreibung benennt keinen Vorteil daraus, dass beide Agenten dieselben funktionalen Äquivalenzen stabilisieren. Da alle Handlungen dieselbe unmittelbare Umweltwirkung besitzen, ist weder ein erfolgreicher Abschluss noch ein geringerer Aufwand, eine vermiedene Störung oder eine sonstige private Folge an abgestimmte Paarbildung gebunden.

Ohne Koordinationsvorteil kann jede beobachtete Paarbildung durch Drift, zufällige Korrelation oder private Clusterbildung entstehen.

**Befund:** Nagelprobe nicht bestanden.

---

## Phase-4-Verdikt zu K04

**Verwerfen.**

K04 besitzt mehrere symmetrische Varianten und eine formal beobachtbare relationale Ordnung. Der Rohkandidat enthält aber keinen definierten Vorteil gemeinsamer Stabilisierung und keine nicht willkürliche Grundlage für episodische Valenz. Zugleich fällt die behauptete Ordnung beobachtungsseitig mit einer partnerbezogenen Reaktionstabelle zusammen.

K04 wird in Phase 5 nicht weitergeführt.

---

# 3. PL-R2-K06 — Komplementäre Vervollständigung einer offenen Handlung

## Rohkern

Eine sichtbare unvollständige Handlung lässt zwei physisch mögliche Endpunkte offen. Der Partner stellt durch eine komplementäre Handlung einen Endpunkt her; der Initiator setzt von dort fort, kehrt um oder bricht ab. Dieselbe Anfangshandlung kann in verschiedenen Begegnungslinien unterschiedlich vervollständigt werden.

---

## Frage 1 — Welche Handlungen sind öffentlich beobachtbar?

Öffentlich beobachtbar sind:

- die Initiation einer unvollständigen Handlung;
- die beiden physisch offenen Endpunkte;
- die komplementäre Handlung des Partners;
- der dadurch realisierte Endpunkt `X` oder `Y`;
- Fortsetzung, Umkehr oder Abbruch durch den Initiator;
- Abschluss der Folge.

Nicht öffentlich gegeben sind:

- die Erwartung des Initiators;
- die Auswahlabsicht des Partners;
- ein Label für den „geltenden“ Endpunkt;
- eine gespeicherte Zuordnung über Begegnungen hinweg.

**Befund:** die vollständige mehrschrittige Folge ist unmittelbar beobachtbar.

---

## Frage 2 — Welche mehreren Verhaltensverläufe sind möglich?

Die Rohbeschreibung enthält mindestens:

1. offene Handlung → Endpunkt `X` → Fortsetzung `X1` → Abschluss;
2. offene Handlung → Endpunkt `Y` → Fortsetzung `Y1` → Abschluss;
3. Vervollständigung → Umkehr;
4. Vervollständigung → Abbruch.

Die Endpunkte `X` und `Y` sind zunächst beide physisch möglich. Eine öffentliche Markierung, welcher Endpunkt gewählt werden soll, existiert nicht.

**Befund:** mehrere alternative Fortsetzungs- und Abschlussverläufe sind vorhanden.

---

## Frage 3 — Wie wirken die Handlungen wechselseitig?

Die Initiation des ersten Agenten schafft eine offene physische Lage, in der der Partner einen von zwei Endpunkten herstellen kann. Die komplementäre Handlung des Partners verändert damit den realen Zustand, von dem aus der Initiator fortsetzt, umkehrt oder abbricht.

Der Initiator ist für die Eröffnung und die Folgehandlung kausal beteiligt; der Partner ist für die konkrete Vervollständigung kausal beteiligt.

Die Wechselseitigkeit bleibt jedoch asymmetrisch:

- Der Partner wählt den Endpunkt.
- Der Initiator reagiert anschließend auf den bereits realisierten Endpunkt.
- Eine erneute Reaktion des Partners auf die Fortsetzung ist in der Rohbeschreibung nicht enthalten.

**Befund:** starke komplementäre Kausalität über drei Schritte, aber mögliche einseitige Festlegung des Verlaufs durch den vervollständigenden Partner.

---

## Frage 4 — Warum könnte Wiederholung individuelle Dispositionen und eine gemeinsame Praxis stabilisieren?

Wiederholte Begegnungen könnten komplementäre Erwartungen hervorbringen:

- Der Partner vervollständigt dieselbe offene Handlung bei dieser Dyade regelmäßig zu `X`.
- Der Initiator setzt danach mit `X1` fort.
- In einer anderen Dyade stabilisieren sich `Y` und `Y1`.

Eine gemeinsame Praxis läge nur dann vor, wenn beide Dispositionen zusammen nötig sind:

- die Vervollständigungsdisposition des Partners;
- die passende Fortsetzungsdisposition des Initiators.

Die Rohbeschreibung lässt aber ebenfalls eine einfachere Form zu:

```text
offene Handlung + Partner-ID
→ Partner wählt Endpunkt

sichtbarer Endpunkt
→ Initiator wählt passende Fortsetzung
```

Dann ist nur die erste Zuordnung partnerbezogen; die Fortsetzung ist eine allgemeine Reaktion auf den aktuellen physischen Zustand.

**Befund:** verteilte Stabilisierung ist möglich, aber noch nicht von unilateral gewähltem Endpunkt plus allgemeiner Anschlussregel getrennt.

---

## Frage 5 — Wie könnte Valenz Episoden gewichten, ohne direkt Handlungen zu steuern?

Vollständige Episoden könnten anhand ihrer privaten Zustandsfolgen unterschiedlich konsolidiert werden:

- Vervollständigung mit anschließender Fortsetzung und Abschluss;
- Vervollständigung mit Umkehr;
- Vervollständigung mit Abbruch.

Valenz dürfte erst die gespeicherte Gesamtepisode gewichten. Sie dürfte weder Endpunkt `X` noch `Y` als solchen bevorzugen und keine passende Fortsetzung direkt verstärken.

Damit mehrere Praktiken offenbleiben, müssten erfolgreiche `X/X1`- und `Y/Y1`-Verläufe für beide Agenten funktional gleichwertige private Folgen haben. Die Rohbeschreibung spezifiziert diese Zustandsfolgen noch nicht.

**Befund:** episodische Valenz ist grundsätzlich anschließbar, aber Gleichwertigkeit und private Grundlage sind offen.

---

## Frage 6 — Welche einfachere nichtsoziale Erklärung ist zu erwarten?

Das kleinste naheliegende Vollmodell besteht aus zwei Regeln:

```text
vervollständigender Agent:
offene Anfangshandlung + Partner-ID
→ Endpunkt X oder Y

initiierender Agent:
sichtbarer Endpunkt
→ passende Fortsetzung X1 oder Y1
```

Die erste Regel ist Partnerkalibrierung oder eine feste partnerbezogene Präferenz. Die zweite ist eine aktuelle Zustandsreaktion. Konkrete gemeinsame Episodengeschichte ist nach Erlernen der Zuordnung nicht mehr notwendig.

Eine noch einfachere Variante lässt den Partner stets denselben Endpunkt wählen und den Initiator nur folgen.

**Befund:** starke Konkurrenz durch unilateral gewählte partnerbezogene Zuordnung plus Markov-Anschlussregel.

---

## Frage 7 — Welche minimale Kontrolle trennt diese Erklärung ab?

Das minimale Kontrollpaket muss drei Dinge auseinanderhalten:

1. **Partner-ID-Baseline:**  
   `Anfangshandlung + Partner-ID → Endpunkt`, anschließend `Endpunkt → Fortsetzung`.

2. **Einseitiger Historienaustausch:**  
   Partner-ID, aktuelle offene Handlung und sichtbarer Zustand bleiben gleich; nur die private Begegnungsgeschichte eines Agenten wird ausgetauscht.

3. **Ghost-Replay nach Abweichung:**  
   Eine aufgezeichnete Vervollständigungsfolge wird abgespielt, kann aber auf eine unerwartete Fortsetzung oder Umkehr des Initiators nicht reagieren.

Eine gemeinsam getragene Praxis müsste bei nur einseitig ausgetauschter Geschichte eine spezifische Inkompatibilität zeigen, die weder Partner-ID noch aktueller Endpunkt erklären. Zudem müsste eine reale weitere Partnerreaktion für Wiederherstellung oder Fortführung nötig sein.

Die letzte Voraussetzung ist in der Rohbeschreibung nicht enthalten, weil die Folge nach der Reaktion des Initiators bereits enden kann. Deshalb ist der Ghost-Test in der aktuellen Fassung nur eingeschränkt diskriminierend.

**Befund:** eine relevante Kontrollstruktur ist benennbar; ihre Trennschärfe bleibt wegen der kurzen und asymmetrischen Folge offen.

---

## Frage 8 — Woran wird der Kandidat vor Implementierung verworfen?

Der Kandidat ist vor Implementierung zu verwerfen, wenn mindestens einer der folgenden Punkte gilt:

1. Das Partner-ID-Vollmodell reproduziert Endpunktwahl, Fortsetzung und Abschluss vollständig.
2. Der vervollständigende Partner kann die stabile Variante unilateral festlegen.
3. Der Initiator benötigt nach sichtbarem Endpunkt keine dyadenspezifische Geschichte.
4. `X/X1` und `Y/Y1` sind nicht funktional gleichwertig.
5. Eine allgemeine Regel `Endpunkt → passende Fortsetzung` genügt.
6. Ein Ghost-Replay der Vervollständigung funktioniert ebenso gut wie ein responsiver Partner.
7. Einseitiger Historienaustausch erzeugt keine von aktuellen Zuständen und Partner-ID unabhängige Störung.

Die Punkte 1 bis 3 sind die zentralen offenen Angriffe.

---

## Frage 9 — Hat Koordination einen Vorteil, ohne dass die Situation festlegt, welche Koordination entsteht?

Grundsätzlich kann ein Vorteil bestehen:

- Nur durch komplementären Partnerbeitrag entsteht überhaupt ein Endpunkt.
- Eine passende Fortsetzung kann zum Abschluss führen.
- Umkehr oder Abbruch stellen alternative, nicht abgeschlossene Verläufe dar.

Die Situation legt zunächst nicht fest, ob `X/X1` oder `Y/Y1` entsteht.

Nicht geklärt ist jedoch:

- ob beide Endpunkte tatsächlich gleichwertig sind;
- ob der Partner allein die Variante auswählt;
- ob der Initiator nur auf einen bereits vollständig bestimmten Zustand reagiert;
- ob abgestimmte Geschichte gegenüber unmittelbarer Anpassung einen Zusatzvorteil hat.

**Befund:** Nagelprobe prinzipiell erfüllbar, aber im Rohkandidaten noch nicht geschlossen.

---

## Phase-4-Verdikt zu K06

**Unentscheidbar; weiter zu Phase 5.**

K06 besitzt im Unterschied zu K04 einen erkennbaren möglichen Koordinationsvorteil und eine physisch konstitutive Beteiligung beider Agenten. Seine zentrale Schwäche ist nicht fehlende Interaktion, sondern die mögliche Reduktion auf:

- unilaterale Endpunktwahl durch den Partner;
- allgemeine Reaktion des Initiators auf den sichtbaren Endpunkt;
- partnerbezogene Zuordnung ohne fortlaufend notwendige gemeinsame Geschichte.

Phase 5 muss insbesondere G2 bis G4 sowie die Konkurrenzmodelle M2 und M3 angreifen. Eine positive Vorentscheidung ist damit nicht verbunden.

---

# 4. Phase-4-Register

| ID | Phase-4-Verdikt | Hauptgrund |
|---|---|---|
| **PL-R2-K04** | **verwerfen** | kein definierter Koordinationsvorteil; keine nicht willkürliche Valenzgrundlage; Reaktionstabelle beobachtungsäquivalent |
| **PL-R2-K06** | **unentscheidbar; weiter zu Phase 5** | komplementäre Kausalität vorhanden, aber unilaterale Auswahl und Partner-ID-Zuordnung können vollständig genügen |

## Verbleibende Kandidaten für Phase 5

- `PL-R2-K06`

## Ausgeschieden in Phase 4

- `PL-R2-K04`

K04 wird innerhalb dieser Runde nicht repariert.

---

# 5. Nächster zulässiger Schritt

**Phase 5 — PL-Gate für `PL-R2-K06`:**

- Prüfung G1 bis G6;
- Prüfung gegen M0 bis M3;
- Bestimmung der minimalen Kontrollen;
- Festhalten von Hauptstärke, Hauptschwäche, gefährlichster Gegenhypothese, notwendiger Kontrolle und Vorab-Verwerfungskriterium.

K06 darf nicht deshalb ausgewählt werden, weil er als einziger Kandidat verblieben ist.
