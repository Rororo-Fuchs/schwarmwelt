# Externe Module

Neue Mechanismen können als einzelne Python-Dateien in diesem Ordner ergänzt werden. Sie registrieren sich über:

```python
from schwarmwelt_lab.core.registry import register
from schwarmwelt_lab.core.interfaces import SocialMemoryModule

@register("memory", "mein_gedaechtnis")
class MeinGedaechtnis(SocialMemoryModule):
    ...
```

Danach kann ein Szenario das Modul ausschließlich über JSON auswählen:

```json
"memory": {
  "name": "mein_gedaechtnis",
  "params": {"staerke": 0.4}
}
```

Die Oberfläche und der Simulationskern müssen dafür nicht geändert werden.

## Sicherheitsgrenze

Gedächtnismodule erhalten nur `ObservableContext`. Dieser enthält keine tatsächliche Valenz und keinen wahren Zustand anderer Agenten. Ein Plugin sollte diese Grenze nicht über globale Zugriffe oder Diagnoseobjekte umgehen.
