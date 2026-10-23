<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## inventarfrist_ehegatten

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `fristende_erbe`: ISO-Datum des rechtlich qualifizierten Inventarfristendes gegenüber dem Erben vor zusätzlicher Verlängerung nach§2008. Sonstige Friständerungen bereits berücksichtigen.
- `fristende_anderer_ehegatte`: Optionales qualifiziertes ISO-Fristende gegenüber dem anderen Ehegatten. Erforderlich bei Gesamtgut, dessen alleiniger/gemeinsamer Verwaltung und erfolgter Fristbestimmung. NULL bedeutet kein vorgegebenes Ende, nicht automatisch abgelaufen. Auch unbenötigte Eingaben werden validiert.
- `erbschaft_gehoert_zum_gesamtgut`: Expliziter Wahrheitswert zum Anwendungsbereich: Erbe ist Ehegatte und Erbschaft gehört zum Gesamtgut; auch nach Ende der Gütergemeinschaft gemäß Absatz2 entsprechend bestimmen. FALSE ergibt NICHT_ANWENDBAR.
- `anderer_ehegatte_verwaltet_gesamtgut`: Expliziter Wahrheitswert: anderer Ehegatte verwaltet Gesamtgut allein oder gemeinsam. Auch nach Ende der Gütergemeinschaft rechtlich entsprechend qualifizieren.
- `frist_auch_gegenueber_anderem_bestimmt`: Expliziter Wahrheitswert, ob wirksame Fristbestimmung auch gegenüber anderem Ehegatten erfolgt ist. Bei erforderlicher Mitbestimmung und FALSE kein wirksames Fristende des Erben.
- `inventar_durch_anderen_errichtet`: Expliziter Wahrheitswert der rechtlich wirksamen Inventarerrichtung durch anderen Ehegatten; keine bloße Entwurfserstellung und keine Aussage über rückwirkende Heilung versäumter Fristen.
- `einordnungsnachweis`: Nichtleerer Nachweis von Gesamtgutzugehörigkeit, Verwaltung, Fristbestimmungen, qualifizierten Fristenden und Inventarerrichtung; gegebenenfalls Fortgeltung nach Ende der Gütergemeinschaft begründen.

Bei Verwaltung durch anderen Ehegatten Fristbestimmung auch ihm gegenüber erforderlich. Bei wirksamer Bestimmung Ende gegenüber Erben auf späteres beider qualifizierten Fristenden anheben. Inventarerrichtung durch anderen kommt Erben zustatten. Fortgeltung nach Ende der Gütergemeinschaft.

wert enthält fristbestimmung_nach_2008_wirksam, inventarfristende_erbe (NULL bei unwirksamer Bestimmung) und inventar_kommt_erben_zustatten. Außerhalb Gesamtgut NICHT_ANWENDBAR.

Keine Gesamthaftungsprüfung oder automatische Heilung früherer Fristversäumnisse. Nur Zusatzbedingung§2008; sonstige Wirksamkeits- und Fristfragen vorqualifiziert. Nicht verwaltender anderer Ehegatte verlängert Frist nicht; Inventarzurechnung nach Satz3 bleibt hiervon getrennt.

ISO-Daten0001..9999, explizite Wahrheitswerte und nichtleerer Nachweis.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2008_T0001, BGB_2008_T0002, BGB_2008_T0003, BGB_2008_T0004

```python
from bgbcalc import inventarfrist_ehegatten
inventarfrist_ehegatten(
    fristende_erbe='2030-06-15',
    fristende_anderer_ehegatte='2030-06-30',
    erbschaft_gehoert_zum_gesamtgut=True,
    anderer_ehegatte_verwaltet_gesamtgut=False,
    frist_auch_gegenueber_anderem_bestimmt=False,
    inventar_durch_anderen_errichtet=False,
    einordnungsnachweis='Synthetisch qualifizierte Gesamtgutzugehörigkeit, Verwaltung und Inventarfristbestimmungen.',
)
```
