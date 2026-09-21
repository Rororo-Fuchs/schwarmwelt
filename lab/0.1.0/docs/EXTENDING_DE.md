# Neue Forschungsansätze ergänzen

## 1. Neue Parameterkombination

Eine vorhandene Szenariodatei kopieren, Titel und Parameter ändern. Beim nächsten Start erscheint sie automatisch in der Szenarioauswahl.

## 2. Neues Sozialgedächtnis

Eine Datei `plugins/mein_gedaechtnis.py` anlegen:

```python
from schwarmwelt_lab.core.interfaces import SocialMemoryModule
from schwarmwelt_lab.core.registry import register

@register("memory", "mein_gedaechtnis")
class MeinGedaechtnis(SocialMemoryModule):
    def __init__(self, staerke=0.3):
        self.staerke = staerke

    def initialize(self, zone_count, symbols, states):
        self.symbols = symbols

    def tick(self, tick):
        pass

    def action_bias(self, zone, estimated_state, previous_partner_symbol):
        return [0.0] * self.symbols

    def observe(self, context, chosen_symbol):
        # context enthält keine Ground Truth.
        pass

    def summary(self):
        return {"type": "mein_gedaechtnis", "entries": 0}
```

Dann im Szenario:

```json
"memory": {
  "name": "mein_gedaechtnis",
  "params": {"staerke": 0.3}
}
```

## 3. Neue Inferenz oder Praxis

Dasselbe Prinzip gilt für `inference` und `practice`. Die abstrakten Schnittstellen liegen in:

`src/schwarmwelt_lab/core/interfaces.py`

## 4. Neue Diagnosemetriken

Die erste Version zeigt bewusst nur robuste Prozessdaten und sichtbare Folgen. Neue Offline-Metriken sollten nicht als Lernsignal in die Module gelangen. Empfehlenswert ist ein separater Auswertungsprozess, der gespeicherte Replays liest.

## 5. Wann der Kern erweitert werden muss

Eine Kernänderung ist nötig, wenn sich die elementare Ereignisform ändert, etwa:

- echte Triaden oder größere Gruppen in einem einzigen Ereignis,
- persistente Umweltobjekte,
- Rollenvergabe vor einer Begegnung,
- mehrphasige öffentliche Ereignisse mit Beobachtern.

Auch dann bleiben Valenz-, Inferenz-, Gedächtnis-, Recording- und UI-Schichten verwendbar. Es muss nur ein neuer Begegnungsorchestrator ergänzt werden.

## Szenariovalidierung

`scenario.schema.json` beschreibt die Konfigurationsstruktur. Der Kern prüft unabhängig davon grundlegende Werte und Modulspezifikationen beim Laden.
