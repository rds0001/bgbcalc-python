# bgbcalc

Native Berechnungen zu Rechenregeln des Bürgerlichen Gesetzbuchs (BGB).
Version 0.1.0; 552 Funktionen mit deutschen Parametern.

## Installation

Veröffentlicht auf [PyPI](https://pypi.org/project/bgbcalc/0.1.0/):

```sh
python -m pip install bgbcalc==0.1.0
```

## Umfang und Stand

Diese Bibliothek enthält kalenderbezogene und numerische Rechenregeln.
Der systematische Rechenumfang wurde anhand des lokalen Norminventars und
der festen Liste von 86 Restprüfpunkten abgearbeitet. Eine universelle juristische
oder atomare Vollständigkeit wird nicht behauptet. Funktions- und Testzahlen
beweisen keine vollständige BGB-Abdeckung. Ausdrücklich bedingte Modelle
enthalten noch rechtlich zu qualifizierende Methoden; siehe MODELLE.md.
Rechtliche Voraussetzungen müssen anhand der jeweiligen Funktionsdokumentation
qualifiziert vorgegeben werden. Ergebnisse enthalten Rechenschritte, Annahmen und
Quellenfassung. Die feste Quellenfassung ist BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb.
Es findet keine automatische Aktualisierung von Gesetzen oder Zinssätzen statt.

Geldbeträge werden als Dezimalzeichenfolge eingegeben; Ergebnisse verwenden
exakte Brüche mit `zaehler` und `nenner`. Datumswerte verwenden `YYYY-MM-DD`.
Die Bibliothek arbeitet offline ohne Netzwerkzugriff oder Telemetrie.

Die komprimierte Ressource `daten/kompositionen.json.gz` enthält native
Anwendungstests, deren Eingabedaten und Fachbeschreibungen als Zuordnung
von relativen Dateipfaden zu UTF-8-Inhalten. Sie ergänzt die Einzelreferenzen;
ihr Vorhandensein allein ist kein Prüfbeleg. Enthaltene Tests lassen sich
in eine lokale Verzeichnisstruktur entpacken. Python-Tests verwenden pytest;
R-Skripte setzen die Paketfunktionen und interne Rechenhelfer voraus.
Die abschließenden Prüfberichte dokumentieren die tatsächlich ausgeführten Tests.

## Beispiel

Python:

```python
from bgbcalc import fristende
ergebnis = fristende("2024-01-31", 1, "monate", "ereignis")
assert ergebnis["wert"] == "2024-02-29"
```

R:

```r
ergebnis <- bgbcalc::fristende("2024-01-31", 1, "monate", "ereignis")
stopifnot(ergebnis$wert == "2024-02-29")
```

Vollständige Parameterverträge und Referenzfälle liegen komprimiert unter
`daten/regelvertraege.json.gz` und `daten/referenzen.json.gz`. Im Python-Repository
enthält `docs/` die Funktionsdokumentation; in R ist sie über `help()` erreichbar.

## Lizenz und Kontakt

Copyright RiskDataScience GmbH. GPL Version 3 oder neuer (GPL-3.0-or-later).
Maintainer: Dr. Dimitrios Geromichalos <riskdatascience@web.de>.
Siehe LICENSE und NOTICE.

## Repository und Entwicklung

Quellrepository: https://github.com/rds0001/bgbcalc-python

CI: https://github.com/rds0001/bgbcalc-python/actions

```sh
python -m pip install ".[test]"
python -m pytest
python -m pip install build twine
python -m build
python -m twine check dist/*
```

`src/bgbcalc/` enthält den Rechenkern, `tests/` alle Python-Tests und
`tests/fixtures/` die unkomprimierten Referenz- und Kompositionsdaten.
`contracts/` enthält die Fachverträge, `docs/` die Funktionsdokumentation.
Die vollständigen installierten Tests sind zusätzlich über `tools/` ausführbar.
