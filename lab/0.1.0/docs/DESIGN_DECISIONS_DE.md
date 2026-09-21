# Designentscheidungen

## D1 – Schrittweiser Kern statt nachträglicher Animation

Die Simulation wird tatsächlich Tick für Tick ausgeführt. Die Oberfläche animiert keine erfundene Rekonstruktion eines bereits abgeschlossenen Batchlaufs.

## D2 – Deterministische Seeds

Alle Zufallsentscheidungen laufen über eine einzige lokale `Random`-Instanz. Gleicher Seed und gleiches Szenario ergeben denselben Zustandsdigest.

## D3 – Oberfläche ist Beobachterin

Die UI liest Snapshots und sendet nur Steuerbefehle wie Start, Pause und Reset. Sie schreibt keine Werte in Agenten oder Umwelt zurück.

## D4 – Diagnose getrennt von Außenansicht

Verborgene Zustände werden nur im Diagnosemodus ausgegeben. Aufzeichnungen speichern jeweils den aktuell gewählten Modus; für wissenschaftliche Auswertung sollte ein gesonderter Diagnoselauf protokolliert werden.

## D5 – Soziales Gedächtnis als Plugin

Die Prüfthese „Protokultur benötigt einen sozial persistenten Träger“ wird nicht in den Kern eingebaut. `distributed_trace` ist nur eine austauschbare, ausdrücklich unvalidierte Hypothese.

## D6 – Keine automatische Kulturpunktzahl

Die Anwendung zeigt keine laufende Kulturmetrik. Das würde zum visuellen Zielwert werden und Apophänie beziehungsweise Parameteroptimierung begünstigen.

## D7 – Null externe Laufzeitabhängigkeiten

Tkinter wurde für Version 0.1 gewählt, weil 48 Agenten problemlos darstellbar sind und die Anwendung ohne Paketinstallation startet. Die UI kann später gegen Qt Quick ausgetauscht werden, ohne den Kern zu ändern.

## D8 – Decoy-Zustand bleibt erhalten

Jeder Agent besitzt weiterhin einen unabhängig evolvierenden Decoy-Zustand. Er wird nicht in der Oberfläche standardmäßig gezeigt, steht aber im Diagnosemodus und für spätere Auswertungen zur Verfügung.
