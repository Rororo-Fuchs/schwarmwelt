# Neuronaler Versuch zur Emergenz persistenter verborgener Ursachen

## Gesamturteil

**Der neuronal angepasste Versuch liefert keinen positiven Nachweis dafür, dass eine persistente reaktionsfähige Ursache in den Hauptwelten das einfachste und beste interne Modell wird.**

Der Nullbefund ist diesmal wesentlich informativer als im linearen MDL-Versuch:

- Die neuronale Architektur bestand die positive Kalibrierung.
- Sie bildete dort einen tatsächlich genutzten latenten Zustand.
- In der negativen Kalibrierung blieb diese Nutzung aus.
- Trotzdem gewann in sämtlichen sechs Hauptbedingungen und bei allen vier unbekannten Holdout-Seeds das auf vier Ticks begrenzte Modell M0.

Die latenten Modelle konnten den verborgenen Prozess teilweise sehr gut **dekodierbar repräsentieren**, aber diese Repräsentation verbesserte die ökonomische Vorhersage nicht. Das ist der zentrale Befund.

## Ausgeführtes Protokoll

- 20 Umwelt-Seeds je Bedingung
  - 12 Training
  - 4 Validierung
  - 4 vollständig unbekannter Holdout
- 5.800 Ticks je Trajektorie
  - 3.600 Training
  - 1.200 stabile Beobachtung
  - 1.000 Intervention
- Sequenzfenster: 96 Ticks
- keine instrumentelle, soziale oder Kooperationsbelohnung
- feste, zeitlich strukturierte Explorationsaktionen
- Training mit Checkpoints und atomarem Speichern
- maximal 14 Epochen je Modell

### Modelle

- **M0:** kapazitätsangepasste GRU, deren Gedächtnis nach vier Ticks zwingend endet
- **M1:** GRU-Weltmodell mit 16 verborgenen Einheiten und zweidimensionalem stochastischem Latentzustand
- **M2:** gleiche Architektur mit vierdimensionalem Latentzustand

Für M1 und M2 wurde optimiert:

\[
L = L_{Vorhersage} + 0,0025\,L_{KL}
\]

Die KL-Komponente begrenzt, wie viel Information der persistente Zustand speichern darf.

## Kalibrierung

### Positive Kontrolle

Eine lang persistente, stark verrauscht beobachtete Ursache konnte nur durch Integration über längere Zeit zuverlässig geschätzt werden.

| Modell | Holdout-Zielfunktion | Decoder-R² | Ablationsschaden |
|---|---:|---:|---:|
| M0 | 0.360543 | – | – |
| M1 | 0.359174 | 0.990 | 0.164 |
| M2 | 0.359216 | 0.990 | 0.181 |

Der rohe Vorhersagevorteil war klein, aber die Funktionsdiagnostik eindeutig:

- Der verborgene Zustand war mit \(R^2 \approx 0,99\) aus dem Latentzustand rekonstruierbar.
- Nullsetzen oder zeitliches Permutieren des Latentzustands verschlechterte die Vorhersage stark.

Damit ist belegt, dass die neuronale Architektur eine persistente verborgene Ursache bilden und tatsächlich verwenden kann.

### Negative Kontrolle

| Modell | Holdout-Zielfunktion | Decoder-R² | Ablationsschaden |
|---|---:|---:|---:|
| M0 | 0.286593 | – | – |
| M1 | 0.286814 | -0.002 | 0.006 |
| M2 | 0.286489 | -0.001 | 0.000 |

Die Zielfunktionen waren praktisch gleich. Decoderleistung und Ablationswirkung lagen um null. Ein formal vorhandener Latentzustand wurde also nicht als stabile Ursache benutzt.

## Hauptresultate

| Bedingung | M0 | M1 | M2 | Gewinner in Holdout-Seeds |
|---|---:|---:|---:|---|
| Persistent und reaktionsfähig | 0.071842 | 0.085572 | 0.083638 | M0: 4/4 |
| Playback | 0.101000 | 0.107157 | 0.105989 | M0: 4/4 |
| Reaktiv ohne Gedächtnis | 0.167622 | 0.189325 | 0.185830 | M0: 4/4 |
| Autonom persistent | 0.112994 | 0.129522 | 0.124996 | M0: 4/4 |
| Zufallsprozess | 0.411780 | 0.420459 | 0.435557 | M0: 4/4 |
| Identitätswechsel | 0.071066 | 0.087839 | 0.078919 | M0: 4/4 |

Niedrigere Werte sind besser. Die Rangfolge war auf allen Holdout-Seeds gleichgerichtet, nicht nur im Mittel.

### Persistenter reaktionsfähiger Prozess

M1 und M2 kodierten den tatsächlichen inneren Zustand durchaus:

- M1: Decoder-\(R^2 = 0.631\)
- M2: Decoder-\(R^2 = 0.780\)

Trotzdem waren ihre Vorhersagen schlechter als die von M0. Das bedeutet:

> Der verborgene Prozess war neuronal repräsentierbar, aber für die konkrete Sensorwelt keine notwendige erklärende Entität.

Die jüngsten vier Beobachtungen enthielten bereits genügend Information für die nächste Vorhersage.

### Autonom persistenter Prozess

Auch hier enthielt M2 den verborgenen Zustand teilweise (Decoder-\(R^2 = 0.565\)), ohne M0 zu übertreffen. Persistenz allein führte daher nicht zur ökonomischen Auswahl einer Entitätsrepräsentation.

### Identitätswechsel

Beim Wechsel B→B′ reagierten die latenten Modelle nicht spezifischer als auf die kurze Sensorstörung:

- M1, mittlere Spezifität: -0.105
- M2, mittlere Spezifität: -0.236

Negative Werte bedeuten, dass die vorübergehende Sensorstörung im Latentraum einen größeren bleibenden Abstand erzeugte als der tatsächliche Austausch. Ein belastbarer Identitätsbruch wurde nicht repräsentiert.

## Kausalfork

Bei Tick 4.950 wurde eine eigene Aktion verändert. Im Live-Zweig durfte die Umwelt darauf reagieren; im Playback-Zweig lief die ursprüngliche Beobachtungsfolge weiter.

Mittlere Differenz `Playbackfehler − Livefehler`:

| Modell | Differenz |
|---|---:|
| M0 | 0.025649 |
| M1 | 0.008938 |
| M2 | 0.009635 |

Die Differenz war für jedes Modell und jeden Holdout-Seed positiv. Die Modelle hatten also eine reale Erwartung darüber gelernt, wie die Umwelt auf die eigene Aktion reagiert.

Der stärkste Effekt trat jedoch bei M0 auf. Die erlernte Kausalität war damit kurzfristig und lokal erklärbar; sie erforderte keine persistente Repräsentation eines Gegenübers.

## Interpretation

Der Versuch trennt drei Dinge, die leicht verwechselt werden:

1. **Eine verborgene Ursache ist in den Daten vorhanden.**
2. **Ein neuronales Netz kann Informationen über sie intern kodieren.**
3. **Diese Ursache ist die einfachste, für Vorhersage tatsächlich benötigte Modellstruktur.**

In den Hauptwelten galten Punkt 1 und teilweise Punkt 2. Punkt 3 galt nicht.

Das ist ein substantieller negativer Befund für die konkrete Hypothese:

> Ein allgemeiner Bias zu sparsamer Vorhersage führt nicht bereits deshalb zu einer persistenten Gegenüber-Repräsentation, weil die Umwelt tatsächlich einen persistenten und reaktionsfähigen Prozess enthält.

Die „Baby-Analogie“ muss daher präzisiert werden. Ein Baby hat nicht nur einen allgemeinen Drang zur Erklärung. Seine sensorische Welt und seine Lernarchitektur machen langfristige Ursachen offenbar **notwendig oder stark bevorzugt**. In der simulierten Hauptwelt blieb die verborgene Ursache dagegen aus den unmittelbaren Beobachtungen hinreichend rekonstruierbar.

## Was der Nullbefund nicht zeigt

Er zeigt nicht, dass neuronale Agenten keine Entitäten bilden können. Die positive Kontrolle widerlegt das.

Er zeigt auch nicht, dass eine reaktionsfähige Ursache prinzipiell nie als Gegenüber modelliert wird. Er zeigt nur:

- nicht unter der gewählten Beobachtbarkeit,
- nicht bei dieser Dynamik,
- nicht mit passiver Exploration,
- und nicht mit dieser kleinen generativen Architektur.

## Methodische Grenzen

- Nur ein Train-/Validierungs-/Holdout-Split und eine Modellinitialisierung je Bedingung.
- Vier unabhängige Holdout-Seeds sind für eine definitive statistische Aussage zu wenig.
- M0 und M1/M2 sind kapazitätsangepasst, aber nicht exakt dieselbe generative Modellfamilie.
- Der Latentzustand ist ein variational regulierter GRU-Zustand, kein objektzentriertes hierarchisches Bayes-Modell.
- Die Sensorstörung war offenbar salienzstärker als der Identitätswechsel.
- Die Agenten erkundeten nicht aktiv, um konkurrierende Weltmodelle auseinanderzuhalten.

## Nächster sinnvoller Versuch

Nicht einfach mehr Seeds oder längere Trainingsläufe. Zunächst sollte eine **Notwendigkeitsgrenze** kartiert werden:

- Beobachtungsrauschen stufenweise erhöhen,
- direkte Sichtbarkeit des verborgenen Zustands reduzieren,
- Verzögerung der Reaktion erhöhen,
- Persistenzzeit variieren.

Gesucht wird der Punkt, an dem M1/M2 in der persistent-reaktiven Welt M0 zuverlässig übertreffen, aber nicht im Playback und nicht bei einer rein autonomen Ursache.

Erst wenn es einen solchen Bereich gibt, wäre die starke Anschlussfrage sinnvoll:

> Fügt Reaktionsfähigkeit über bloße Persistenz hinaus zusätzliche erklärende Kompression hinzu?

## Reproduzierbarkeit

Das Paket enthält:

- vollständiges ausführbares Python-Skript,
- eingefrorenes Protokoll,
- alle erzeugten Trajektorien,
- neuronale Checkpoints,
- Seed-Einzelergebnisse,
- latente Zeitreihen,
- Kausalfork-Daten,
- Aggregationen und Abbildungen.
