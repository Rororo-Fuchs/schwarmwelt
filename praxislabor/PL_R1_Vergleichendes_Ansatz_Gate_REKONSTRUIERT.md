# PL-01 — Vergleichendes Ansatz-Gate

**Stand:** 11. Juli 2026  
**Geprüfte Menge:** Kandidaten 2–5  
**Nicht enthalten:** Kandidat 1; als PL-Kandidat bereits verworfen  
**Zweck:** Auswahl von höchstens einem Begegnungssetting vor Agentenarchitektur, Freeze und Simulation

---

## 1. Entscheidungsregel

Ein Kandidat wird nur als **PL-Kandidat** zugelassen, wenn:

1. alle Gates G1–G6 erfüllbar sind;
2. konkrete gemeinsame Geschichte gegenüber aktueller Beobachtung und individuellen Summen einen notwendigen Zusatzbeitrag leisten kann;
3. mehrere Agenten kausal an der Stabilisierung beteiligt sein müssen;
4. Ghost-Replay, Responsivitäts-Knockout, Geschichts-Shuffle und einfache Vergleichsmodelle den behaupteten Unterschied tatsächlich angreifen können;
5. die relevante Verhaltensordnung vor der Exploration formal beschreibbar ist.

Ein Setting wird nicht deshalb zugelassen, weil es „sozialer“ wirkt. Entscheidend ist die Trennbarkeit von M0 bis M3:

- mechanische Reaktion,
- unmittelbare Reaktion oder Imitation,
- individuelle Gewohnheit,
- allgemeine Koordination.

Nur ein Setting, das darüber hinaus historische Kontingenz und verteilte Kausalität prüfen kann, rechtfertigt den Praxislabor-Build.

---

## 2. Vergleichsmatrix

Legende:

- **Ja:** strukturell erfüllt
- **Offen:** grundsätzlich möglich, aber noch nicht nachgewiesen
- **Nein:** der Kandidat trägt das Gate in seiner gegenwärtigen Form nicht

| Gate | Kandidat 2: Initiationsfolge | Kandidat 3: Freigabe | Kandidat 4: gemeinsamer Körper | Kandidat 5: Kontaktintensität |
|---|---:|---:|---:|---:|
| **G1 Mehrere gleichwertige Stabilitätspunkte** | Ja | Nein | Offen | Offen |
| **G2 Echte Wechselseitigkeit** | Offen | Ja | Ja | Ja |
| **G3 Historische Kontingenz** | Offen | Offen | Offen | Offen |
| **G4 Verteilte Kausalität** | Nein | Offen | Offen | Offen |
| **G5 Verlauf statt Einzelhandlung** | Ja | Ja | Ja | Ja |
| **G6 Kein versteckter sozialer Zustand** | Ja | gefährdet | Ja | formal ja, konzeptuell gefährdet |
| **Starker Angriff durch einfaches Modell** | privater Taktgeber | private Bilanzregel | adaptiver Zustandsregler | privater Komfortregler |
| **Vorläufiges Verdikt** | Koordinationspilot | Verwerfen | einziger weiter prüfbarer Kandidat | nur mechanischer Pilot |

---

# 3. Einzelverdikte

## Kandidat 2 — Sequenzielle Rollenkoordination

### Ergebnis

**Koordinationspilot. Kein PL-Kandidat.**

### Warum er nicht trägt

Die unterschiedlichen Folgen — Alternation, Zweierblöcke oder längere Motive — sehen historisch kontingent aus. Sie können jedoch vollständig durch gekoppelte private Zustandsautomaten erzeugt werden:

```text
eigene letzte Rolle
+ privater Phasenzustand
+ gegebenenfalls Partner-ID
→ nächste Rolle
```

Die konkrete gemeinsame Geschichte wird dabei nur zur anfänglichen Phasensynchronisation benötigt. Anschließend können beide Agenten ihr Programm offen weiterführen.

Auch eine Störung mit anschließender Resynchronisation rettet den Kandidaten nicht zwingend. Ein endlicher Zustandsautomat kann eine solche Reparaturregel enthalten, ohne dass beide Agenten die Praxis fortlaufend gemeinsam hervorbringen.

### Entscheidend gescheitertes Gate

**G4 — verteilte Kausalität**

Ein Agent kann eine Phase oder Folge vorgeben; der andere muss sich nur komplementär einstellen. Die Praxis ist nicht notwendig in beiden Dispositionen verteilt.

### Verbleibender Nutzen

Kandidat 2 eignet sich als kontrollierbarer Pilot für:

- episodisches Gedächtnis;
- private Phasendispositionen;
- Partnerwechsel;
- Geschichts-Shuffle;
- Abgrenzung von offenem Skript und geschlossener Reaktion.

Er rechtfertigt aber keinen protosozialen Interpretationsrahmen.

---

## Kandidat 3 — Reziproke Freigabe einer knappen Gelegenheit

### Ergebnis

**Verwerfen.**

### Hauptproblem

Der Kandidat besitzt keine stabile neutrale Mitte zwischen zwei unbrauchbaren Varianten.

#### Ohne eingebauten Ausgleichsdruck

Wenn ein Agent dauerhaft zugreift und der andere dauerhaft freigibt, ist die Begegnung:

- kollisionsfrei;
- mechanisch stabil;
- für mindestens einen Agenten vorteilhaft.

Damit ist eine einseitige Ordnung ein zusätzlicher Stabilitätspunkt. Reziprozität ist nicht notwendig.

#### Mit eingebautem Ausgleichsdruck

Soll dauerhafte einseitige Nutzung nachteilig werden, müsste die Architektur etwa enthalten:

- Sättigung;
- anwachsenden privaten Bedarf des leer ausgehenden Agenten;
- abnehmenden Grenznutzen;
- Ausgleichskosten;
- eine längerfristige Nutzungsbilanz.

Dann erklärt aber eine einfache private Bilanzregel das Verhalten:

```text
eigener bisheriger Mangel hoch
→ zugreifen

eigener bisheriger Überschuss hoch
→ freigeben
```

Die gewünschte Reziprozität würde damit entweder nicht erforderlich oder durch die private Zustandsökonomie nahegelegt.

### Entscheidend gescheitertes Gate

**G1 — mehrere gleichwertige Stabilitätspunkte**

Die behauptete Gleichwertigkeit von unmittelbarer Teilung und zeitversetztem Austausch gilt nur über einen künstlich festgelegten Bilanzhorizont. Sie ist keine robuste Eigenschaft der einzelnen Begegnung.

Zudem sind Mischungen der beiden Praktiken nicht notwendig schlechter. Eine Dyade kann ohne Kollision zwischen Teilung, Blockaustausch und einseitiger Nutzung wechseln.

### Weiteres Risiko

Begriffe wie „Erwidern“, „Kompensieren“ und „Reziprozität“ würden leicht mehr Interpretation einführen, als die sichtbare Aktionsfolge trägt.

---

## Kandidat 4 — Ko-adaptive Stabilisierung eines gemeinsamen Körpers

### Ergebnis

**Einziger weiter prüfbarer Kandidat, aber noch kein zugelassener PL-Kandidat.**

Bis zum Bestehen eines gesonderten formalen Machbarkeitsgates lautet das offizielle Verdikt:

> **Koordinationspilot mit möglichem Upgrade zum PL-Kandidaten**

### Hauptstärke

Kandidat 4 besitzt die stärkste strukturelle Wechselseitigkeit:

- Jede Handlung verändert den gemeinsamen Körper.
- Dadurch verändert sie die Entscheidungslage des Partners.
- Dessen Reaktion verändert wiederum, ob die eigene begonnene Handlung noch angemessen ist.
- Ein nichtreaktiver Ghost sollte bei unvorhergesehenen Störungen erkennbar schlechter funktionieren.

Im Unterschied zu Kandidat 2 genügt daher kein bloßer privater Takt. Eine laufende Begegnung kann tatsächliche Gegenreaktion verlangen.

### Hauptschwäche

Zwei gemeinsam regelnde Agenten sind zunächst nur zwei gekoppelte Regler.

Ein allgemeiner adaptiver Controller könnte vollständig erklären:

- Partnerantizipation;
- Dämpfung;
- wechselnde Führung;
- Anpassung nach Partnerwechsel;
- Stabilisierung nach Störungen.

Historisch entstandene Partnerkalibrierung wäre zwar dyadisch, aber nicht automatisch mehr als motorische Koordination.

### Noch offene harte Gates

#### G1 — gleichwertige Regelungsstile

Es wurde bisher nur behauptet, dass etwa alternierende und parallele Dämpfung gleichwertig konstruiert werden könnten.

Noch fehlt der Nachweis, dass sie tatsächlich übereinstimmen in:

- Stabilisierungsqualität;
- Zeit;
- Handlungsaufwand;
- privaten Zustandsfolgen;
- Ausfallwahrscheinlichkeit.

#### G3 — historische Kontingenz

Unterschiedliche Paare müssen unter gleichen Bedingungen verschiedene stabile Regelungsweisen ausbilden können. Unterschiede dürfen nicht bloß aus bleibenden individuellen Parametern oder zufälliger Agentenheterogenität stammen.

#### G4 — verteilte Kausalität

Ein einzelner Agent darf den Körper nicht hinreichend kontrollieren können. Ebenso wenig darf eine feste Leader-Follower-Policy ausreichen.

### Warum der Kandidat dennoch weiterlebt

Bei Kandidat 4 können die offenen Punkte durch eine kleine formale Begegnungsanalyse angegriffen werden, ohne bereits eine lernende Agentenarchitektur zu bauen.

Das unterscheidet ihn von Kandidat 2 und 3: Dort ist die einfache Gegenhypothese bereits strukturell in der Aufgabenform enthalten. Bei Kandidat 4 ist noch offen, ob die Begegnungsdynamik so konstruiert werden kann, dass eine allgemeine Einzel- oder Markov-Regel nicht ausreicht.

---

## Kandidat 5 — Dyadische Kalibrierung einer Kontaktintensität

### Ergebnis

**Nur mechanischer Pilot. Kein PL-Kandidat.**

### Hauptproblem

Der Kandidat entfernt zwar das externe gemeinsame Objekt, ersetzt es aber durch eine abstrakte „Kontaktintensität“ und private Verträglichkeitsgrenzen.

Dadurch entstehen zwei Schwierigkeiten.

#### 1. Der Koordinationsvorteil ist nicht unabhängig definiert

Warum ein Kontakt fortgesetzt, intensiviert oder in einer bestimmten Form beendet werden soll, ergibt sich erst aus den konstruierten privaten Zustandswirkungen.

Die Umwelt enthält keinen externen Erfolg. Deshalb wird die Definition eines „tragfähigen Verlaufs“ fast vollständig durch die privaten Dynamiken bestimmt.

#### 2. Eine allgemeine private Regelung liegt sehr nahe

```text
eigener Zustand zu stark verändert
→ Intensität reduzieren

eigener Zustand zu schwach verändert
→ Intensität erhöhen

Partner reagiert stark
→ eigene Änderung abschwächen
```

Ein solcher Regler kann mehrere äußerlich verschiedene Verläufe hervorbringen, ohne eine konkrete gemeinsame Geschichte zu benötigen.

### Konzeptuelles Risiko

„Kontaktintensität“, „Verträglichkeit“ und „Akkommodation“ liegen bereits nahe an einer sozialen Deutung. Es wäre schwer zu zeigen, dass nicht ein gewünschtes Begegnungsphänomen in die Zustandsdynamik hineindefiniert wurde.

### Verbleibender Nutzen

Das Setting könnte prüfen:

- partielle Beobachtbarkeit privater Zustände;
- wechselseitige Zustandsregulation;
- Latenzlernen;
- Partnerkalibrierung.

Es ist aber schlechter falsifizierbar als Kandidat 4, weil Erfolg, Belastung und soziale Interpretation aus derselben konstruierten Zustandsdynamik stammen.

---

# 4. Gesamtentscheidung

## Kein Kandidat erhält jetzt die volle PL-Zulassung

Das Ergebnis des Ansatz-Gates lautet:

| Kandidat | Endverdikt |
|---|---|
| **2** | Koordinationspilot |
| **3** | Verwerfen |
| **4** | Koordinationspilot; einziger Kandidat für ein vorgeschaltetes Machbarkeitsgate |
| **5** | nur mechanischer Pilot |

Damit trägt derzeit **keiner** der vier Kandidaten unmittelbar den Praxislabor-Build.

Das ist kein Abbruch des Neustarts. Es verhindert, dass ein interessant wirkendes, aber mechanistisch erklärbares Setting vorschnell eingefroren wird.

---

# 5. Enges Machbarkeitsgate für Kandidat 4

Kandidat 4 darf nur dann zum PL-Kandidaten aufsteigen, wenn vor Agentenarchitektur und Lernsimulation alle folgenden Punkte geschlossen werden.

## F1 — Exakte Begegnungsdynamik

Eine minimale Dynamik wird vollständig angegeben:

- Zustandsgrößen des gemeinsamen Körpers;
- Beobachtung jedes Agenten;
- drei oder höchstens vier Aktionen;
- Störungsprozess;
- Abschluss- und Abbruchbedingungen.

Noch keine lernenden Agenten, kein Gedächtnis und keine Valenz.

## F2 — Zwei nachweislich gleichwertige Praktiken

Mindestens zwei Regelungsfamilien müssen vorab definiert werden.

Für beide muss gelten:

```text
gleiche Stabilisierungsleistung
gleicher erwarteter Aufwand
gleiche Dauer
gleiche Zustandswirkung
gleiche Ausfallwahrscheinlichkeit
```

Inkompatible Kreuzungen der beiden Familien müssen schlechter funktionieren als jeweils übereinstimmende Ausführung.

## F3 — Keine unilaterale Lösung

Es muss rechnerisch gezeigt werden:

- Kein einzelner Agent kann den Körper zuverlässig allein stabilisieren.
- Passivität des Partners ist keine robuste Lösung.
- Ein fester Leader kann nicht alle zulässigen Störungen abfangen.
- Beide Reaktionsketten sind kausal erforderlich.

## F4 — Geschichte kann einen notwendigen Unterschied machen

Es müssen zwei Begegnungslinien konstruierbar sein, bei denen:

- der aktuell sichtbare Körperzustand gleich ist;
- die aktuell sichtbare Partnerhandlung gleich ist;
- die geeignete nächste Handlung dennoch wegen unterschiedlich ausgebildeter Partnerdispositionen verschieden ist.

Ohne einen solchen Fall kann die aktuelle Lage plus letzte Handlung wahrscheinlich alles erklären.

## F5 — Konkurrenzmodelle stehen vorab fest

Mindestens:

1. gedächtnisloser Zustandsregler;
2. Copy-last-action;
3. Opposite-last-action;
4. kurzer Markov-Regler;
5. partnerunabhängiger adaptiver Controller;
6. Controller mit Partner-ID, aber ohne Episodenfolge;
7. fester Leader-Follower-Regler.

## F6 — Geschlossene Beobachtungseinheiten

Vor Exploration werden wenige mögliche Einheiten festgelegt, etwa:

```text
Störung
→ erste Korrektur
→ Partnerreaktion
→ Gegenkorrektur
→ Stabilisierung oder Abbruch
```

Keine nachträgliche freie Auswahl attraktiver Kurvenformen.

---

# 6. Automatische Entscheidung nach dem Machbarkeitsgate

### Zulassung als PL-Kandidat

Nur wenn F1–F6 vollständig geschlossen sind.

Danach darf Phase 3 beginnen:

- minimaler Agent;
- episodisches Gedächtnis;
- prozedurale Konsolidierung;
- intrinsische Valenz;
- Kontrollen;
- Freeze.

### Rückstufung

Wenn mehrere Regelungsstile existieren, aber aktuelle Zustandsregulation ausreicht:

> Kandidat 4 bleibt Koordinationspilot.

### Verwerfung

Wenn:

- nur eine optimale Regelungsweise existiert;
- ein Agent allein stabilisieren kann;
- ein einfacher Markov-Regler alle relevanten Verläufe erzeugt;
- die behauptete Gleichwertigkeit nur durch nachträgliche Parametertuning entsteht.

Dann lautet das Gesamtresultat der ersten Kandidatenrunde:

> **Keiner trägt.**

Eine neue Kandidatenrunde müsste anschließend nicht einfach einen fünften Koordinationstyp suchen, sondern gezielt das gemeinsame Defizit der bisherigen Ansätze bearbeiten: Geschichte muss für die aktuelle Reaktion notwendig sein, ohne als Takt, Bilanz, Sollwert oder externe Dynamik bereits vorstrukturiert zu werden.
