<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## vorerbe_fruchtwertgrenze

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `fruchtwert`: Nichtnegativer exakter EUR-Wert der gerade untersuchten ordnungswidrig/übermäßig gezogenen Früchte.
- `beeintraechtigte_eigene_nutzungen`: Nichtnegativer rechtlich bewerteter EUR-Wert gerade durch diesen Bezug beeinträchtigter dem Vorerben gebührender Nutzungen. Nicht beliebiger Gesamtschaden und nicht bereits um denselben Wiederherstellungsbetrag gekürzt.
- `wiederherstellungsgebundener_fruchtwert`: Nichtnegativer nach ordnungsmäßiger Wirtschaft zur Wiederherstellung einzusetzender Anteil dieses Fruchtwerts, höchstens fruchtwert. Keine ungeprüfte volle Reparaturkostensumme.
- `fruchtziehung_nach_2133_qualifiziert`: Pflichtwahrheitswert: ordnungswidrige Fruchtziehung oder durch besonderes Ereignis notwendig gewordener Übermaßbezug2133; FALSE NICHT_ANWENDBAR.
- `bewertungsnachweis`: Nichtleerer Nachweis des Bezugs, der eigenen Nutzungsbeeinträchtigung und des gebundenen Fruchtwertanteils.

Freier Fruchtwert=Gesamtfruchtwert−wiederherstellungsgebundener Anteil; dem Vorerben gebührender Wert=min(freierFruchtwert,beeinträchtigteEigeneNutzungen). Nicht gebührenden Rest getrennt.

wert enthält nicht_wiederherstellungsgebundener_fruchtwert, dem_vorerben_gebuehrender_fruchtwert, dem_vorerben_nicht_gebuehrender_fruchtwert als exakte EUR-Brüche.

Keine Bewertung ordnungsmäßiger Wirtschaft, keine erfundene Reparaturkostenformel, kein sofortiger Zahlungsanspruch des Nacherben.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2133_T0001

```python
from bgbcalc import vorerbe_fruchtwertgrenze
vorerbe_fruchtwertgrenze(
    fruchtwert='100',
    beeintraechtigte_eigene_nutzungen='50',
    wiederherstellungsgebundener_fruchtwert='20',
    fruchtziehung_nach_2133_qualifiziert=True,
    bewertungsnachweis='Synthetisch qualifizierter Fruchtbezug und getrennte Wertgrenzen.',
)
```
