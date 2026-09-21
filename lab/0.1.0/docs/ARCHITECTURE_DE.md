# Architektur

## Ziel

Forschungsentscheidungen wie ein soziales Gedächtnis, andere Inferenzmechanismen oder neue Praxisformen sollen nicht zu einem Neuaufbau der Anwendung führen.

Die Software trennt deshalb sechs Ebenen:

1. **Agentenzustand** – Position, intrinsische Valenz, Decoy-Zustand, Alter
2. **Simulationsorchestrierung** – Tick, Begegnungen, Turnover
3. **Forschungsmodule** – Valenz, Geografie, Ausdruck, Inferenz, Praxis, Gedächtnis
4. **Beobachterebene** – öffentliche und diagnostische Snapshots
5. **Aufzeichnung/Replay** – gespeicherte Snapshots ohne Rückwirkung
6. **Oberfläche** – reine Darstellung und Steuerung

## Module

Jede Forschungsentscheidung gehört möglichst in genau eine Schnittstelle:

- `ValenceModule`
- `GeographyModule`
- `EmissionModule`
- `InferenceModule`
- `PracticeModule`
- `SocialMemoryModule`

Ein Szenario wählt die konkrete Implementierung über JSON aus.

Beispiel:

```json
"memory": {
  "name": "distributed_trace",
  "params": {
    "decay": 0.998,
    "read_strength": 0.65
  }
}
```

## Schutz vor Ground-Truth-Kontamination

Der Simulationskern kennt den tatsächlichen Fremdzustand, weil er Ausdruck und Diagnose berechnen muss. Lern- und Gedächtnismodule erhalten ihn jedoch nicht.

Das Sozialgedächtnis sieht ausschließlich `ObservableContext`:

- beobachtete Symbole,
- private Zustandsschätzung,
- sichtbare Vorgeschichte,
- Zone,
- eigene intrinsische Valenzreaktion.

Es enthält weder tatsächliche Fremdvalenz noch ein Korrektheitslabel.

## Oberflächen- und Diagnosekanal

Der normale Snapshot enthält keine Valenz und keinen tatsächlichen Zustand. Die Diagnoseansicht wird separat angefordert. Dadurch kann die künstlerische Außenansicht die Innen-/Außen-Trennung bewahren.

## Plugin-Lader

Alle `.py`-Dateien in `plugins/` werden beim Start dynamisch geladen. Ein neues Modul registriert sich selbst. Szenarien können es anschließend über seinen Namen verwenden.

Damit sind drei Änderungstiefen möglich:

1. **Parameterentscheidung**: nur JSON ändern
2. **Neue Kombination vorhandener Mechanismen**: neues JSON-Szenario
3. **Neuer Mechanismus**: eine Plugin-Datei plus Szenario

Nur Änderungen an der grundsätzlichen Ereignisstruktur – etwa Begegnungen mit beliebig vielen gleichzeitigen Rollen – würden eine Erweiterung des Simulationskerns erfordern. Auch dafür sind Ereignis- und Beobachterschicht bereits getrennt.
