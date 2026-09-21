# PL-R2 — Rohkandidaten v1.0

**Datum:** 2026-07-11  
**Grundlage:** `PL_R2_Suchprozess_Freeze_v1.0.md`  
**Status:** Phase 1; noch keine Entdoppelung oder Prüfung

## PL-R2-K01 — Verzweigte gemeinsame Fortsetzung

**Prozessklasse:** Fortsetzung einer gemeinsam erzeugten Folge

Zwei Agenten ergänzen abwechselnd eine flüchtige Begegnungsfolge durch jeweils eine von drei sichtbaren, nichtsprachlichen Handlungen. Nach jeder Handlung kann der Partner einen von zwei anschlussfähigen Zweigen fortsetzen, auf einen dritten Zweig umlenken oder die Begegnung beenden. Es gibt kein äußeres Ziel und keine gespeicherte Sequenz; nach vier bis sechs Schritten wird die Begegnung vollständig zurückgesetzt. Wiederkehrende Dyaden können unterschiedliche Schleifen hervorbringen, deren Fortsetzungen untereinander nicht austauschbar sind.

**Mögliche Verlaufsformen:**
- `A0 → A1 → A2 → A0`
- `A0 → A2 → A1 → A0`
- Umlenkung mit anschließendem Abbruch

**Stärkster einfacher Gegner:** Endlicher Zustandsautomat aus den letzten ein bis zwei sichtbaren Handlungen.

## PL-R2-K02 — Reziproke Öffnung von Handlungsmöglichkeiten

**Prozessklasse:** wechselseitige Ermöglichung und Einschränkung

Jede Handlung eines Agenten öffnet für genau den nächsten Schritt eine von zwei Handlungsklassen des Partners und schließt die andere. Die Antwort des Partners formt anschließend auf dieselbe Weise die nächste Optionslage des ersten Agenten. Keine Öffnung bleibt über einen Schritt hinaus bestehen, und nach Begegnungsende wird der Zustand gelöscht. Mehrere geschlossene Zyklen gegenseitiger Ermöglichung sind möglich; unvereinbare Öffnungen führen zu Stillstand oder Abbruch.

**Mögliche Verlaufsformen:**
- `X öffnen → Y nutzen/öffnen → X' nutzen/öffnen`
- spiegelbildlicher Gegenzyklus
- inkompatible Öffnung mit Stillstand

**Stärkster einfacher Gegner:** Markov-Policy über den aktuell sichtbaren Optionszustand.

## PL-R2-K03 — Gemeinsam erzeugter Begegnungsabschluss

**Prozessklasse:** Grenzbildung und Abschluss

Eine Begegnung besitzt keine vorgegebene Dauer. In jedem Schritt können Agenten die laufende Aktivität fortsetzen, abschwächen oder sich lösen. Eine einseitige Lösung beendet die Begegnung abrupt; ein mehrschrittiger beiderseitiger Verlauf kann sie ohne abrupten Übergang schließen. Es existiert weder eine öffentliche Abschlussphase noch ein externer Turn- oder Zeitzähler.

**Mögliche Verlaufsformen:**
- paralleles Abschwächen mit gemeinsamer Lösung
- versetztes Abschwächen mit später Bestätigung
- Fortsetzung nach begonnenem Abschluss

**Stärkster einfacher Gegner:** Privater Timer oder feste endliche Abschlussroutine.

## PL-R2-K04 — Dyadische Bildung funktionaler Äquivalenzen

**Prozessklasse:** relationale Gleichsetzung und Unterscheidung

Vier sichtbar verschiedene Handlungen besitzen dieselbe unmittelbare Umweltwirkung. Ein Agent führt eine Handlung aus; der Partner antwortet, und der erste Agent setzt fort, substituiert oder beendet die Folge. Über wiederholte Begegnungen können verschiedene Dyaden dieselben vier Handlungen in unterschiedlichen Paaren ähnlich behandeln, erkennbar an gleichen oder verschiedenen Anschlussfolgen. Die Umwelt enthält keine Kategorie und speichert keine Zuordnung.

**Mögliche Verlaufsformen:**
- `{A0,A1}` und `{A2,A3}` werden jeweils gleich fortgesetzt
- `{A0,A2}` und `{A1,A3}` werden jeweils gleich fortgesetzt
- wechselnde Zuordnungen ohne stabile Fortsetzung

**Stärkster einfacher Gegner:** Partnerbezogene Reaktionstabelle oder formale Clusterung sichtbarer Aktionsindizes.

## PL-R2-K05 — Übergabe gemeinsamer Orientierung

**Prozessklasse:** Aufmerksamkeitsübergabe zwischen neutralen Ereignissen

Während einer Begegnung sind jeweils drei kurzlebige, gleichwertige Ereignisse öffentlich sichtbar. Jeder Agent kann sich einem Ereignis zuwenden, dort bleiben oder zu einem anderen wechseln; ein gemeinsam fokussiertes Ereignis bleibt einen zusätzlichen Schritt verfügbar. Kein Ereignis ist dauerhaft ausgezeichnet, und die Ereignismenge wird nach der Begegnung gelöscht. Dyaden können unterschiedliche Verlaufsformen aus Initiation, Folgen, Halten und Umlenken ausbilden.

**Mögliche Verlaufsformen:**
- Initiatorwechsel mit unmittelbarem Folgen
- verzögerte Übergabe nach einem Halteschritt
- alternierende Umlenkung zwischen Ereignissen

**Stärkster einfacher Gegner:** Blickfolgen beziehungsweise Reaktion auf aktuelle Ereignissalienz.

## PL-R2-K06 — Komplementäre Vervollständigung einer offenen Handlung

**Prozessklasse:** gemeinsame Vervollständigung

Eine Begegnung beginnt mit einer sichtbaren, unvollständigen Handlung eines Agenten, die zwei physisch mögliche Endpunkte offenlässt. Der Partner kann einen der Endpunkte durch eine komplementäre Handlung herstellen; der Initiator setzt von dort aus fort, kehrt um oder bricht ab. Dieselbe offene Anfangshandlung kann in getrennten Begegnungslinien unterschiedlich vervollständigt und weitergeführt werden. Es gibt kein öffentliches Label dafür, welcher Endpunkt gelten soll, und keinen gespeicherten Abschlusszustand über die Begegnung hinaus.

**Mögliche Verlaufsformen:**
- Endpunkt X → Fortsetzung X1 → Abschluss
- Endpunkt Y → Fortsetzung Y1 → Abschluss
- Vervollständigung und anschließende Umkehr

**Stärkster einfacher Gegner:** Partner-ID-basierte Zuordnung von Anfangshandlung zu Endpunkt und Fortsetzung.

## PL-R2-K07 — Nichtkommutative gemeinsame Transformation

**Prozessklasse:** order-sensitive Ko-Konstruktion

Ein flüchtiger neutraler Körper kann durch drei sichtbare, reversible Operationen verändert werden. Die Agenten führen abwechselnd je eine Operation aus; die Reihenfolge verändert den Zwischenzustand, weil die Operationen nicht kommutieren. Mehrere kurze Operationszyklen führen mit gleichem Aufwand in den neutralen Zustand zurück, während gekreuzte Teilfolgen andere Zwischenzustände erzeugen. Nach jeder Begegnung wird der Körper unabhängig vom Ergebnis vollständig zurückgesetzt.

**Mögliche Verlaufsformen:**
- `T0 → T1 → T2 → neutral`
- `T0 → T2 → T1 → neutral`
- gekreuzte Folge ohne Rückkehr

**Stärkster einfacher Gegner:** Zustandsbasierter Planer oder Markov-Controller über den sichtbaren Körperzustand.

## PL-R2-K08 — Selektive Aufnahme in einer dichten Handlungsfolge

**Prozessklasse:** selektive Aufnahme und Nichtaufnahme

Während einer Begegnung erzeugen beide Agenten mehrere sichtbare Mikrohandlungen; nicht auf jede Handlung folgt eine Antwort. Eine Antwort kann die vorausgehende Handlung fortsetzen, verändern oder überspringen, und auch Nichtantwort bleibt öffentlich beobachtbar. Dyaden können bei gleichen Aktionshäufigkeiten und gleicher Gesamtzahl von Antworten unterschiedliche wiederkehrende Muster dafür ausbilden, welche Stellen einer Folge aufgenommen werden. Keine Handlung und keine Position ist von der Umwelt als relevant markiert.

**Mögliche Verlaufsformen:**
- regelmäßige Aufnahme jeder zweiten Handlung
- Aufnahme erst nach einer Zweierfolge
- verzweigte Aufnahme mit selektivem Überspringen

**Stärkster einfacher Gegner:** Gelernte Salienzgewichte oder privater Positionszähler ohne gemeinsame Episodenfolge.
