# PL-R2 — Abschlussvermerk Phase 6 und 7 v1.0

**Datum:** 11. Juli 2026  
**Status:** Runde 2 geschlossen  
**Grundlagen:**
- `PL_R2_Suchprozess_Freeze_v1.0.md`
- `PL_R2_Rohkandidaten_v1.0.md`
- `PL_R2_Phase2_Entdoppelung_v1.0.md`
- `PL_R2_Phase3_Blinder_Sofortfilter_v1.0.md`
- `PL_R2_Phase4_Neun_Fragen_v1.0.md`
- `PL_R2_Phase5_PL_Gate_K06_v1.0.md`
- verbindliches PL-Handoff
- verbindliches PL-Prüfraster

---

## 0. Zweck

Dieser Vermerk schließt die zweite Kandidatenrunde formal ab.

Er dient ausdrücklich **nicht** dazu,

- einen relativ besten Kandidaten nachträglich auszuwählen,
- einen verworfenen Kandidaten als „fast tragfähig“ zu reservieren,
- Phase 6 oder 7 zur stillen Reparatur einzelner Ansätze zu verwenden,
- oder unmittelbar eine dritte Generierungsrunde zu eröffnen.

Die alte E-Reihe bleibt abgeschlossen. Kein Kandidat dieser Runde wird in eine Reparaturlinie überführt.

---

# 1. Phase 6 — Adversariale Prüfung

## Kandidatenmenge

Nach Phase 5 gilt:

```text
Menge der Phase-6-Kandidaten = ∅
```

Es existiert daher kein Kandidat, auf den die adversariale Leitfrage noch anzuwenden wäre:

> Welches kleinstmögliche nichtsoziale Modell könnte denselben Befund erzeugen?

Diese Frage wurde für die jeweils verbliebenen Kandidaten bereits in den vorangegangenen Phasen beantwortet:

- K04 fiel auf eine partnerbezogene Reaktionstabelle beziehungsweise private Klassifikation zurück.
- K06 fiel auf eine Partner-ID-Zuordnung plus gedächtnislose Anschlussregel zurück.

## Phase-6-Ergebnis

**Formale Leerprüfung.**

Keine zusätzliche Einzelprüfung, keine Nachbesserung, keine Rangbildung.

---

# 2. Phase 7 — Vergleichendes Abschluss-Gate

## Entscheidungsregel

Ein Kandidat darf nur ausgewählt werden, wenn er die harten Gates absolut erfüllt. Relative Überlegenheit innerhalb einer schwachen Menge genügt nicht.

Unzulässige Auswahlgründe bleiben:

- anschaulichste Situation,
- größter bereits investierter Entwicklungsaufwand,
- letzter nicht sofort ausgeschiedener Kandidat,
- geringste Zahl offener Probleme,
- subjektiv sozial wirkende Oberfläche.

## Gesamtergebnis

> **Keiner der acht Rohkandidaten trägt als PL-Kandidat.**

Es wird kein Kandidat ausgewählt.

Es wird keine Shortlist gebildet.

Es wird kein Kandidat für Freeze, Agentenarchitektur, Simulation oder Implementierung freigegeben.

---

# 3. Vollständiges Kandidatenregister

| ID | Prozessklasse | Letzte Phase | Endstatus | Ausschlaggebender Grund |
|---|---|---:|---|---|
| **PL-R2-K01** | verzweigte gemeinsame Fortsetzung | 3 | verworfen | kurze Markov-Historie beziehungsweise endlicher Zustandsautomat genügt; Ghost-Replay prinzipiell möglich |
| **PL-R2-K02** | reziproke Öffnung von Handlungsmöglichkeiten | 2 | entfernt/absorbiert | mechanistisch engere, öffentlich zustandskodierte Variante von K01 |
| **PL-R2-K03** | gemeinsam erzeugter Begegnungsabschluss | 3 | verworfen | privater Timer oder feste Abschlussroutine genügt; Begegnungsgrenze unilateral festlegbar |
| **PL-R2-K04** | dyadische Bildung funktionaler Äquivalenzen | 4 | verworfen | kein definierter Koordinationsvorteil; keine nicht willkürliche Valenzgrundlage; Reaktionstabelle beobachtungsäquivalent |
| **PL-R2-K05** | Übergabe gemeinsamer Orientierung | 3 | verworfen | aktuelle Salienz und unmittelbares Folgen genügen; kein notwendiger Geschichtsbeitrag |
| **PL-R2-K06** | komplementäre Vervollständigung einer offenen Handlung | 5 | verworfen | keine geschlossene Wechselseitigkeit; unilaterale Variantenwahl; Partner-ID-Tabelle plus Markov-Anschlussregel genügt |
| **PL-R2-K07** | nichtkommutative gemeinsame Transformation | 2 | entfernt | sichtbarer Objektzustand trägt die Folge; Wiederholung der gemeinsamen-Körper-/Markov-Klasse |
| **PL-R2-K08** | selektive Aufnahme in dichter Handlungsfolge | 3 | verworfen | privater Positionszähler, Salienzgewichte oder kurze Markov-Historie genügen |

---

# 4. Dokumentierte Verwerfungsstruktur

Die Runde scheiterte nicht an einem einzigen gemeinsamen technischen Detail. Die Kandidaten fielen in mehrere wiederkehrende Erklärungstypen zurück.

## 4.1 Kurze Zustands- oder Markov-Regeln

Betroffen:

- K01
- K02
- K05
- K07
- K08
- teilweise K06

Die aktuelle öffentliche Lage oder wenige letzte Handlungen reichten aus, um die nächste Aktion zu bestimmen. Konkrete gemeinsame Episodengeschichte leistete keinen notwendigen Zusatzbeitrag.

## 4.2 Private Routinen und Zähler

Betroffen:

- K03
- K08
- teilweise K01

Timer, Positionszähler oder feste Abschluss- und Fortsetzungsroutinen konnten die beobachteten Folgen erzeugen, ohne dass eine gemeinsam hervorgebrachte Praxis erforderlich war.

## 4.3 Partnerkalibrierung oder Systemidentifikation

Betroffen:

- K04
- K06

Geschichte diente höchstens dazu, eine partnerbezogene Reaktionstabelle, Präferenz oder Zuordnung zu lernen. Nach erfolgter Kalibrierung konnte eine offene Partner-ID-Policy den Verlauf tragen.

## 4.4 Unilaterale Festlegung

Betroffen:

- K03
- K06

Ein Agent konnte die relevante Grenze oder Variantenwahl bestimmen. Der andere musste lediglich reagieren. Physische Beteiligung mehrerer Agenten war vorhanden, aber keine verteilte Stabilisierung der Praxis.

## 4.5 Fehlender unabhängiger Koordinationsvorteil

Besonders deutlich bei:

- K04

Mehrere symmetrische Verhaltensordnungen waren beschreibbar, aber es war nicht definiert, warum ihre gemeinsame Stabilisierung gegenüber Drift, Wechsel oder privater Klassifikation funktional vorteilhaft wäre.

---

# 5. Gemeinsames strukturelles Defizit der Runde

Die acht Kandidaten wurden zwar aus verschiedenen Prozessklassen erzeugt, aber die meisten folgten implizit demselben Grundschema:

```text
öffentliche Handlung oder Lage
→ passende Partnerreaktion
→ kompatible Fortsetzung
```

Dieses Schema erzeugt leicht Interaktion, Koordination und dyadenspezifische Anpassung. Es erzwingt jedoch nicht, dass:

1. die konkrete gemeinsame Geschichte die aktuell passende Fortsetzung bestimmt;
2. diese Fortsetzung nicht aus aktuellem Zustand, kurzer Historie oder Partner-ID ableitbar ist;
3. mehrere Agenten die Ordnung fortlaufend und verteilt stabilisieren;
4. ein nichtreaktiver, aber plausibler Partnerersatz scheitert;
5. mehrere gleichwertige Praktiken bei Kreuzung spezifisch inkompatibel werden.

Die Runde hat damit vor allem gezeigt:

> **Mehrschrittigkeit, Komplementarität und dyadische Spezifität reichen nicht aus.**

Auch gemeinsam vollzogene und partnerabhängige Verläufe können vollständig durch M0 bis M3 erklärt werden.

---

# 6. Abschlussentscheidung

## Kein Build

Nicht freigegeben sind:

- Agentenarchitektur,
- episodisches Gedächtnis,
- Valenzmodell,
- prozedurale Konsolidierung,
- Simulation,
- Terrarium-Pilot,
- Versuchsfreeze.

## Keine Reserveshortlist

K04 und K06 werden nicht als Reserven geführt.

Kandidat 4 aus Runde 1 bleibt ausschließlich ein Koordinations- und Gegenmodellpilot; er wird nicht durch das Scheitern von Runde 2 aufgewertet.

## Keine unmittelbare dritte Kandidatenrunde

Eine erneute Generierung nach demselben Suchschema würde voraussichtlich weitere Oberflächenvarianten derselben Erklärungstypen produzieren.

---

# 7. Einziger empfohlener nächster Prüfschritt

## Meta-Gate der Suchannahmen

Vor einer dritten Kandidatenrunde ist ein eigener, enger Analysechunk erforderlich:

> **Welche formalen Eigenschaften müsste eine Begegnung besitzen, damit konkrete gemeinsame Geschichte nicht nur Parameter, Präferenzen, Takt, Bilanz oder Partnerverhalten schätzt, sondern die Menge der aktuell anschlussfähigen Fortsetzungen konstitutiv mitbestimmt?**

Dieser Schritt soll noch keine neue Begegnungssituation erzeugen.

Er soll ausschließlich:

1. den Unterschied zwischen **Geschichte als Information** und **Geschichte als konstitutiver Bedingung** präzisieren;
2. prüfen, ob diese Unterscheidung ohne versteckten sozialen Zustand überhaupt operationalisierbar ist;
3. daraus notwendige, aber noch keine hinreichenden Konstruktionsbedingungen ableiten;
4. ein Abbruchkriterium formulieren, falls das Ziel unter den aktuellen PL-Leitplanken nicht sauber prüfbar ist.

Erst nach einem positiven Meta-Gate wäre eine dritte Kandidatenrunde zulässig.

---

# 8. Schlussstatus

```text
PL-R2: GESCHLOSSEN
Rohkandidaten: 8
Nach Entdoppelung: 6
Nach Sofortfilter: 2
Nach Neun-Fragen-Prüfung: 1
Nach PL-Gate: 0
Shortlist: 0
Ausgewählt: 0
Freeze-Freigabe: NEIN
Nächster Schritt: Meta-Gate der Suchannahmen
```
