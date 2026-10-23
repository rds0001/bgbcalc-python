<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## ersitzung_bewegliche_sache

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `eigenbesitzbeginn_am`: ISO-Datum des rechtlich maßgeblichen Beginns dieser eigenen Ersitzungsperiode, nach wirksamer Unterbrechung zutreffender Neubeginn. Ereignisfrist; keine Anrechnung von Rechtsvorgängerzeiten in diesem Modell.
- `qualifiziertes_fristende`: Erforderliches belegtes ISO-Ende unter Berücksichtigung einschlägiger Hemmung/Ablaufhemmung. Mindestens selbst berechnetes Zehnjahresgrundende; bei unveränderter Frist dieses Ende ausdrücklich angeben. Keine pauschale Wochenendverschiebung.
- `prueftag`: ISO-Prüftag, mindestens Eigenbesitzbeginn; geprüft zum Tagesende.
- `kenntnis_fremdeigentum_am`: Optionales Datum tatsächlicher Kenntnis fehlenden Eigentums zwischen Beginn und Prüftag. NULL bedeutet bis Prüftag keine spätere Kenntnis, nicht unbekannte Aktenlage. Kenntnis am Fristendtag noch vor Vollendung am Tagesende; spätere Kenntnis nach bereits vollendetem Erwerb unschädlich für diesen Erwerb.
- `guter_glaube_bei_eigenbesitzbeginn`: Expliziter Wahrheitswert zum guten Glauben bei Beginn; grob fahrlässige Unkenntnis fachlich berücksichtigen. Keine automatische Beweiswürdigung.
- `bewegliche_sache`: Expliziter Wahrheitswert des Anwendungsbereichs bewegliche Sache; FALSE ergibt NICHT_ANWENDBAR.
- `besitzverlauf_qualifiziert`: Expliziter Wahrheitswert, dass Beginn, anrechenbarer Eigenbesitzverlauf bis zum früheren von Prüftag/Ende sowie Fristkorrekturen nach§§939–942 rechtlich geprüft sind. Verlust und Rückerlangung nach§940 Absatz2 nicht pauschal als Unterbrechung behandeln. Ohne diese Qualifikation NICHT_ANWENDBAR. Anrechnung fremder Besitzzeiten nach§§943/944 außerhalb dieses Modells.
- `sonstige_erwerbsvoraussetzungen_erfuellt`: Expliziter Wahrheitswert aller sonstigen für den betrachteten Erwerb erforderlichen Voraussetzungen; FALSE verhindert Erwerb auch bei vollendeter Frist und ohne Kenntnisausschluss.
- `einordnungsnachweis`: Nichtleere Begründung des Besitzverlaufs, Anfangsglaubens, Kenntnisereignisses, korrigierten Endes und weiterer Voraussetzungen; Hemmungswirkung gegebenenfalls relativ zum betroffenen Berechtigten qualifizieren.

Zehnjahresgrundfrist aus Eigenbesitzbeginn berechnen; qualifiziertes Ende darf nicht früher liegen. Am Prüftagesende Frist vollendet genau ab Endtag. Fehlender Anfangsglaube oder spätere Kenntnis spätestens am Endtag schließen Erwerb aus; sonstige Voraussetzungen gesondert erforderlich.

wert enthält zehnjahresgrundfristende, ersitzungsfristende, frist_am_prueftag_vollendet, ausschluss_nach_937_absatz_2 und eigentum_durch_ersitzung_erworben. Unbewegliche Sache oder ungeklärter Besitzverlauf ergibt NICHT_ANWENDBAR.

Kein automatisches Hemmungs-/Unterbrechungsmodell§§939–942 und keine Fremdzeitenanrechnung§§943/944. Kenntnis nach bereits vollendetem Erwerb wirkt nicht rückwirkend. §938-Vermutung und§945-Drittrechte nicht implementiert. Keine Aussage über spätere Eigentumsverluste.

ISO-Daten und berechnete Grenzen0001..9999, explizite Wahrheitswerte, nichtleerer Nachweis.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_937_T0001, BGB_937_T0002

```python
from bgbcalc import ersitzung_bewegliche_sache
ersitzung_bewegliche_sache(
    eigenbesitzbeginn_am='2020-02-29',
    qualifiziertes_fristende='2030-02-28',
    prueftag='2030-02-27',
    kenntnis_fremdeigentum_am=None,
    guter_glaube_bei_eigenbesitzbeginn=False,
    bewegliche_sache=True,
    besitzverlauf_qualifiziert=True,
    sonstige_erwerbsvoraussetzungen_erfuellt=False,
    einordnungsnachweis='Synthetisch geprüfter anrechenbarer Besitzverlauf ohne Fremdzeiten; keine Fristverlängerung, Anfangsglaube und sonstige Voraussetzungen qualifiziert.',
)
```
