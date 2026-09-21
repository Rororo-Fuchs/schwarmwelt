# PL-R2 — Suchprozess-Freeze v1.0

**Datum:** 2026-07-11  
**Geltungsbereich:** zweite Kandidatenrunde für minimale Begegnungssituationen  
**Verbindliche Grundlagen:** PL-Handoff Neustart v1; PL-Prüfraster Protosoziale Praxis  
**Status:** vor Generierung der Rohkandidaten eingefroren

## 1. Eingaben

- verbindliches PL-Handoff
- verbindliches PL-Prüfraster
- Befunde der ersten Kandidatenrunde
- ausgeschlossene beziehungsweise besonders anzugreifende Erklärungstypen:
  - privater Taktgeber
  - private Bilanz
  - allgemeiner Zustandsregler
  - Partnerkalibrierung / Systemidentifikation
  - einseitige Führung
  - versteckter sozialer Zustand

## 2. Umfang und Format der Rohkandidaten

- Anzahl: genau 8 Rohkandidaten
- IDs: `PL-R2-K01` bis `PL-R2-K08`
- pro Kandidat:
  - Prozessklasse
  - minimale Situation in höchstens 6 Sätzen und höchstens 130 Wörtern
  - mindestens 2 mögliche Verlaufsformen
  - stärkster vermuteter einfacher Gegner in 1 Satz
- nicht zulässig in Phase 1:
  - Agentenarchitektur
  - Lernmethode
  - Valenzmechanismus
  - Verteidigung gegen das Raster
  - Verbesserung während der Beschreibung

## 3. Diversitätsachsen

Die Kandidatenmenge muss verschiedene Ausprägungen entlang dieser Achsen abdecken:

1. **Prozessfunktion**
   - Fortsetzung
   - Ermöglichung / Einschränkung
   - Abschluss / Grenzbildung
   - Abweichungsbehandlung
   - Aufmerksamkeitsübergabe
   - komplementäre Vervollständigung
   - endogener Wechsel
   - selektive Aufnahme

2. **Zeitform**
   - simultan
   - alternierend
   - mehrschrittig
   - offen beendet
   - störungs- oder wechselinduziert

3. **Relationale Abhängigkeit**
   - Partnerhandlung verändert aktuelle Optionen
   - Partnerantwort verändert Bedeutung oder Anschlussfähigkeit der eigenen Handlung
   - Praxis kann nicht durch bloße Parallelreaktion auf dieselbe Umwelt entstehen

4. **Geschichtsfunktion**
   - Geschichte soll, soweit der Kandidat trägt, nicht nur Reaktionsparameter schätzen,
     sondern zwischen mehreren aktuell möglichen Fortsetzungen unterscheiden.

5. **Träger der Ordnung**
   - keine persistente Umweltspur
   - kein dyadischer oder kollektiver Speicher
   - keine vorgegebenen Rollen, Normen, Bedeutungen oder Konventionen

## 4. Strukturelle Entdoppelung — Phase 2

Alle Kandidaten werden paarweise verglichen. Fusion oder Entfernung erfolgt, wenn mindestens einer der folgenden Punkte gilt:

- derselbe kausale Mechanismus trägt beide Kandidaten;
- derselbe einfache Gegner erklärt beide vollständig;
- die Kandidaten unterscheiden sich nur durch Oberfläche oder Metapher;
- eine Kandidatenklasse ist eine engere Variante einer anderen ohne zusätzlichen Prüfnutzen.

Wenn danach weniger als 6 eigenständige Kandidaten verbleiben, werden nur für die fehlenden Prozessklassen Ersatzkandidaten erzeugt. Ersatzkandidaten erhalten neue IDs und durchlaufen dieselben Phasen.

## 5. Blinder Sofortfilter — Phase 3

Ohne Verbesserungsvorschläge wird sofort verworfen, wenn mindestens eines gilt:

1. eine universelle externe Optimierungsgröße erklärt den gesamten Verlauf;
2. aktuelle Beobachtung plus kurze Markov-Historie genügt;
3. ein Agent kann die Ordnung unilateral festlegen oder aufrechterhalten;
4. privater Zähler, Kontostand, Sollwert oder feste Rollenregel genügt;
5. die Umwelt speichert eine soziale Regel oder Begegnungsgeschichte;
6. nur eine funktional optimale Praxis existiert;
7. Geschichte leistet nur Partnerkalibrierung oder Systemidentifikation;
8. eine aufgezeichnete plausible Partnersequenz kann die reale Interaktion prinzipiell ersetzen;
9. die behauptete Ordnung benötigt semantische Begriffe, die nicht formal im Verhalten abbildbar sind;
10. der Kandidat ist nur durch Hinzufügen einer Sozial-, Fairness-, Reputations- oder Konventionsvariable tragfähig.

Verdikte: `bestehen`, `verwerfen`, `unentscheidbar`.

## 6. Reihenfolge der weiteren Prüfungen

1. Phase 2 — strukturelle Entdoppelung
2. Phase 3 — blinder Sofortfilter
3. Phase 4 — neun Fragen, nur für verbliebene Kandidaten
4. Phase 5 — G1 bis G6, M0 bis M3 und Mindestkontrollen
5. Phase 6 — adversarialer Angriff durch kleinstes nichtsoziales Vollmodell
6. Phase 7 — vergleichendes Ansatz-Gate der geschlossenen Menge

Die Reihenfolge wird nach Beginn der Generierung nicht geändert.

## 7. Regel für Nachbesserungen

- In den Phasen 1 bis 7 wird kein Kandidat repariert.
- Einwände führen zu Verdikt oder dokumentierter Unsicherheit, nicht zu stiller Mutation.
- Nach Abschluss von Phase 7 ist höchstens eine versionierte Reparatur (`Kxx-b`) zulässig, wenn:
  - der ursprüngliche Kandidat höchstens an einem lokal behebbaren Punkt scheitert;
  - alle übrigen harten Gates prinzipiell erfüllt sind;
  - die Reparatur keinen neuen sozialen Zustand, keine Semantik und keine zusätzliche Optimierungsgröße einführt.
- Die reparierte Version gilt als neuer Kandidat und muss die Phasen 2 bis 7 vollständig erneut durchlaufen.

## 8. Abbruchregeln

Die Runde endet ohne Auswahl, wenn:

- kein Kandidat nach Phase 6 alle G1 bis G6 prinzipiell schließen kann;
- jeder verbleibende Kandidat durch ein plausibles einfaches nichtsoziales Vollmodell erklärt wird;
- Tragfähigkeit nur durch nachträgliche Komplexität oder semantische Umdeutung entsteht;
- nur ein relativ bester Kandidat übrig bleibt, aber kein absolut tragfähiger PL-Kandidat.

Ein Kandidat wird niemals ausgewählt, weil er anschaulich ist, bereits viel Text erzeugt hat oder als letzter nicht verworfen wurde.

## 9. Zielausgabe

- vollständiges Kandidatenregister
- dokumentierte Fusionen und Verwerfungen
- Shortlist von höchstens 3 Kandidaten
- Empfehlung für höchstens einen nächsten Prüfschritt
- zulässiges Gesamtergebnis: `Keiner trägt.`
