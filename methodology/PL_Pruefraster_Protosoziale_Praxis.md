# PL-Prüfraster: Mechanik, Imitation, Koordination oder protosoziale Praxis?

Das Raster dient **vor der Implementierung** zur Auswahl eines Begegnungssettings und später zur Interpretation beobachteter Muster.

Es soll verhindern, dass ein mechanisch lösbares Koordinationsspiel nachträglich als protosoziale Dynamik gelesen wird.

---

## 1. Vier konkurrierende Erklärungen

### M0 — Mechanische Reaktion

Das Verhalten wird durch die aktuelle Umweltlage hinreichend erklärt.

```text
Situation → Handlung
```

Beispiele:

- Abstand unterschritten → ausweichen
- Weg blockiert → warten
- sichtbare Bewegung links → Bewegung rechts

Vergangene Begegnungen und die Reaktion des Partners sind nicht notwendig.

### M1 — Imitation oder unmittelbare Reizübernahme

Der Agent übernimmt sichtbares Verhalten des Gegenübers.

```text
Partner tut A → Agent tut A
```

Auch verzögerte oder probabilistische Imitation zählt zunächst hierzu.

Das Verhalten ist sozial ausgelöst, aber noch nicht gemeinsam hervorgebracht.

### M2 — Individuelle Gewohnheit oder Verstärkung

Der Agent lernt aus eigenen Folgen, ohne dass eine spezifische gemeinsame Praxis erforderlich ist.

```text
eigene Handlung → private Folge → erhöhte Wiederholungswahrscheinlichkeit
```

Zwei Agenten können dadurch kompatibel werden, ohne einander wechselseitig geprägt zu haben.

### M3 — Koordination

Mehrere Agenten wählen kompatible Handlungen, weil Übereinstimmung oder Ergänzung vorteilhaft ist.

```text
kompatible Handlungen → gemeinsamer Vorteil
```

Koordination ist sozial, aber noch nicht automatisch protosoziale Praxis. Eine allgemeine optimale Policy könnte sie vollständig erklären.

### M4 — Protosoziale Praxis

Eine protosoziale Praxis ist eine:

> **historisch kontingente, durch wiederholte wechselseitige Begegnung entstandene Verhaltensordnung, an deren Entstehung und Aufrechterhaltung mehrere Agenten kausal beteiligt sind.**

Sie muss M0 bis M3 als einfachere Erklärungen übertreffen.

---

## 2. Harte Zulassungskriterien für ein Begegnungssetting

Ein Setting erhält nur dann Explorationsressourcen, wenn alle folgenden Kriterien erfüllbar sind.

### G1 — Mehrere gleichwertige Stabilitätspunkte

Koordination muss vorteilhaft sein, ohne dass die Umwelt eine bestimmte Lösung bevorzugt.

```text
Praxis A funktioniert.
Praxis B funktioniert ebenfalls.
Mischformen funktionieren schlechter.
A und B sind funktional gleichwertig.
```

**Verwerfen**, wenn:

- nur eine optimale Lösung existiert,
- eine Lösung durch Geometrie, Timing oder Payoff bevorzugt wird,
- überhaupt kein Vorteil aus Abstimmung entsteht.

### G2 — Echte Wechselseitigkeit

Das aktuelle Verhalten eines Agenten muss die nächste Entscheidungslage des anderen verändern.

Es reicht nicht, dass beide dieselbe Umwelt beobachten.

**Prüffrage:**

> Könnte ein Agent dieselbe Policy erfolgreich gegen eine aufgezeichnete, nicht reagierende Verhaltensspur verwenden?

Wenn ja, ist das Setting wahrscheinlich nur mechanisch oder imitativ.

### G3 — Historische Kontingenz

Unter identischen Umwelt- und Startbedingungen müssen verschiedene Begegnungslinien unterschiedliche stabile Praktiken hervorbringen können.

**Verwerfen**, wenn alle Populationen zuverlässig zur gleichen Lösung konvergieren.

### G4 — Verteilte Kausalität

Die Praxis darf nicht nur auf der Gewohnheit eines führenden Agenten beruhen.

Beide oder mehrere Beteiligte müssen durch ihre Reaktionen zur Stabilisierung beitragen.

**Prüffrage:**

> Verändert sich die Praxis, wenn nur die Lernhistorie eines Beteiligten ausgetauscht wird?

Wenn nicht, könnte ein einzelner Agent das Verhalten diktieren.

### G5 — Verlauf statt Einzelhandlung

Die interessante Einheit muss mindestens eine Reaktionsfolge enthalten.

Beispielsweise:

```text
Initiation → Antwort → Korrektur → Abschluss
```

Ein einzelner Akt wie „links gehen“ ist zu leicht durch Mechanik oder Imitation erklärbar.

### G6 — Kein versteckter sozialer Zustand

Das Setting darf keine eingebaute Variable besitzen wie:

- gemeinsame Norm,
- Gruppenpolicy,
- dyadischer Konventionsspeicher,
- Reputation,
- vorgegebene Rollen,
- globales Begegnungsgedächtnis.

Die gemeinsame Ordnung muss verteilt in den Agenten liegen.

---

## 3. Mindestkontrollen

### C0 — Umweltkontrolle

Gleiche Umwelt, aber kein reaktiver Partner.

**Zweck:**

> Reicht die Situation selbst aus, um das Verhalten hervorzubringen?

### C1 — Ghost-Replay

Ein Agent trifft auf eine aufgezeichnete Verhaltenssequenz eines realen Partners. Die Sequenz reagiert nicht auf ihn.

**Zweck:**

> Reichen Beobachtung und Imitation aus, oder ist geschlossene Wechselseitigkeit erforderlich?

Ein protosozialer Kandidat sollte im Ghost-Replay wenigstens teilweise zerfallen oder deutlich verändert werden.

### C2 — Begegnungsgeschichts-Shuffle

Agenten erhalten dieselbe Menge von Begegnungen und sichtbaren Verhaltensereignissen, aber die Zuordnung zu tatsächlichen Begegnungslinien wird permutiert.

**Zweck:**

> Ist die konkrete gemeinsame Geschichte relevant?

### C3 — Gleichwelt-Replikation

Mehrere Populationen starten mit:

- identischen Parametern,
- gleicher Umwelt,
- gleicher Aktionsmenge,
- symmetrischen Payoffs,
- getrennten Zufallsströmen.

**Zweck:**

> Entstehen unterschiedliche lokale Praktiken unter denselben äußeren Bedingungen?

### C4 — Partnerwechsel

Agenten mit stabilisierter Praxis werden neu gepaart.

Mögliche Befunde:

- Praxis bleibt vollständig unverändert: möglicherweise bloße individuelle Gewohnheit.
- Praxis verschwindet sofort: möglicherweise reine dyadische Anpassung.
- Agenten handeln zunächst nach alter Praxis und entwickeln anschließend eine neue gemeinsame Ordnung: interessanter Kandidat.

### C5 — Responsivitäts-Knockout

Der Partner handelt weiterhin plausibel, seine Handlungen hängen aber nicht mehr vom aktuellen Verhalten des anderen ab.

**Zweck:**

> Ist Kontingenz der Reaktion nötig oder nur die Verhaltensverteilung?

### C6 — Einfachmodell-Konkurrenz

Das beobachtete Verhalten wird gegen einfache Erklärungsmodelle geprüft:

- feste Reiz-Reaktions-Tabelle,
- Copy-last-action,
- individuelle Reinforcement-Policy,
- partnerunabhängige Markov-Policy,
- optimale Koordinationspolicy ohne Gedächtnis,
- Policy mit Partner-ID, aber ohne Episodenfolge.

Ein protosozialer Claim ist erst zulässig, wenn diese Modelle die relevanten Verlaufsmerkmale nicht hinreichend erklären.

---

## 4. Diagnosefragen

Für jedes beobachtete Muster werden diese Fragen in Reihenfolge gestellt:

1. **Erzwingt die Umwelt das Verhalten?**  
   Falls ja: mechanische Reaktion.

2. **Reicht das aktuelle sichtbare Verhalten des Partners?**  
   Falls ja: Imitation oder unmittelbare Reaktion.

3. **Reicht die private Folge eigener Handlungen?**  
   Falls ja: individuelle Gewohnheit.

4. **Reicht eine allgemeine partnerunabhängige Koordinationspolicy?**  
   Falls ja: Koordination, aber keine historisch gewachsene Praxis.

5. **Ist die konkrete Begegnungsgeschichte notwendig?**  
   Falls nein: kein protosozialer Kandidat.

6. **Sind mehrere Agenten kausal an der Stabilisierung beteiligt?**  
   Falls nein: individuelle Dominanz oder Führungslernen.

7. **Entstehen unter gleichen Bedingungen unterschiedliche stabile Varianten?**  
   Falls nein: wahrscheinlich Umwelt- oder Optimierungsdruck.

8. **Zerfällt oder verändert sich das Muster bei zerstörter Wechselseitigkeit?**  
   Falls nein: vermutlich Playback-, Reiz- oder Imitationseffekt.

Nur wenn die Fragen 5 bis 8 positiv beantwortet werden, sollte der Begriff **protosoziale Praxis** überhaupt als Arbeitshypothese verwendet werden.

---

## 5. Evidenzstufen

### Stufe A — Wiederholung

Eine Verhaltensfolge tritt mehrfach auf.

**Zulässige Aussage:** wiederkehrendes Verhalten.

### Stufe B — Individuelle Gewohnheit

Ein Agent zeigt aufgrund eigener Erfahrung stabile Verhaltensdispositionen.

**Zulässige Aussage:** erfahrungsabhängige Verhaltensentwicklung.

### Stufe C — Koordination

Mehrere Agenten stabilisieren kompatible Handlungen.

**Zulässige Aussage:** koordinierte Praxis.

### Stufe D — Historisch kontingente soziale Praxis

Die Praxis:

- unterscheidet sich zwischen getrennten Begegnungslinien,
- hängt von tatsächlicher gemeinsamer Geschichte ab,
- benötigt geschlossene Wechselseitigkeit,
- ist nicht durch einfache Vergleichsmodelle erklärt.

**Zulässige Aussage:** protosozialer Praxiskandidat.

### Stufe E — Übertragung

Naive oder neu gekoppelte Agenten übernehmen eine Praxis durch Begegnung.

**Zulässige Aussage:** soziale Übertragung.

### Stufe F — Traditionsähnliche Kontinuität

Die Praxis bleibt über den Austausch einzelner Träger hinaus erhalten und kann sich verändern, konkurrieren oder verzweigen.

**Erst hier** wird eine traditionsähnliche oder proto-kulturelle Interpretation geprüft.

---

## 6. Vorab-Verdikt für Begegnungskandidaten

Jeder Kandidat erhält einen dieser vier Ausgänge.

### Verwerfen

Mindestens eines der harten Gates G1 bis G6 ist nicht erfüllbar.

### Nur mechanischer Pilot

Das Setting eignet sich zum Test der Agentenarchitektur, aber nicht zur Untersuchung sozialer Praxis.

### Koordinationspilot

Das Setting kann Koordination untersuchen, trennt diese aber noch nicht überzeugend von einfacher Regelbildung.

### PL-Kandidat

Das Setting erlaubt:

- mehrere gleichwertige Praktiken,
- geschlossene Wechselseitigkeit,
- historische Kontingenz,
- verteilte Stabilisierung,
- starke Ghost-, Shuffle- und Einfachmodell-Kontrollen.

Nur ein **PL-Kandidat** sollte den ersten eigentlichen Praxislabor-Build tragen.

---

## 7. Verwerfung während der Exploration

Der Kandidat wird zurückgestellt, wenn:

- das einfachste Vergleichsmodell dieselben Verläufe erzeugt,
- Unterschiede nur aus unterschiedlichen Seeds oder Initialzuständen stammen,
- Partnergeschichte keinen Zusatznutzen gegenüber aktueller Beobachtung liefert,
- eine einzelne Aktion die gesamte Koordination erklärt,
- Ghost-Replay und echte Begegnung nicht unterscheidbar sind,
- stabile Praxis nur bei direkter Policy-Belohnung entsteht,
- die relevante Beobachtungseinheit erst nach freier Metriksuche gefunden wird,
- die Interpretation semantische Begriffe benötigt, die im Verhalten nicht formal abgebildet sind.

---

## Arbeitsformel

> **Wiederholung ist keine Praxis.**  
> **Imitation ist keine gemeinsame Geschichte.**  
> **Koordination ist noch keine protosoziale Ordnung.**  
> Ein PL-Kandidat muss zeigen, dass mehrere Agenten durch fortgesetzte wechselseitige Reaktion eine historisch kontingente Verhaltensordnung gemeinsam hervorbringen und aufrechterhalten.
