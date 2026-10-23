<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## gegenleistung_teilbefreiung_betraege

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `vereinbarte_gegenleistung`: Nichtnegativer exakter EUR-Vertragspreis für die gesamte betrachtete Leistung.
- `wert_vollstaendiger_leistung`: Positiver exakter EUR-Wert der vollständigen geschuldeten Leistung im rechtlich maßgeblichen Vergleichszeitpunkt entsprechend441III.
- `wert_verbleibender_teilleistung`: Nichtnegativer exakter EUR-Wert der trotz qualifizierter Teilbefreiung verbleibenden Leistung auf derselben Bewertungsbasis, höchstens Wert der vollständigen Leistung.
- `darauf_gezahlter_betrag`: Nichtnegativer exakter EUR-Betrag bereits auf diese Gegenleistung gezahlter Beträge, höchstens vereinbarte Gegenleistung. Sonstige irrtümliche Überzahlungen separat.
- `einordnungsnachweis`: Nichtleerer Nachweis von Teilbefreiung275/326I, Leistungsbewertung entsprechend441III und Zahlungszuordnung. Kein Behaltensfall326II, kein Ersatzverlangen326III, kein bloßer Nacherfüllungsausschluss326I2.

Gegenleistung mit Verhältnis verbleibender Teilleistung zur Gesamtleistung multiplizieren; entfallenen Preisanteil, gezahlten Mehrbetrag und offenen Rest getrennt bestimmen.

wert: verbleibende_gegenleistung, entfallener_gegenleistungsanteil, rueckforderungsbetrag und rechnerisch_offener_rest als exakte EUR-Brüche; kein automatischer Gesamtvergleich gegenseitiger Ansprüche.

§326I in Verbindung mit441III und326IV: qualifizierte Teilbefreiung, konsistente Vergleichswerte entsprechend441III; keine beliebige Mengen- oder Zeitquote und keine zusätzliche Minderungserklärung erforderlich.326I2 bei bloß nicht zu erbringender Nacherfüllung, Behaltensanspruch326II und Ersatzverlangen326III gesondert. Rückforderungsbetrag ist ausschließlich bereits auf den hier entfallenen Gegenleistungsanteil Gezahltes; weitere Rückgewährvoraussetzungen346–348 und gegenseitige Ansprüche gesondert. Keine automatische Aufrechnung oder zusätzliche Schadensberechnung. Bezugswert muss positiv sein; anderer Fall mit nicht bestimmbarem Wert nicht durch fiktive1 ersetzen.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_326_T0001, BGB_326_T0002, BGB_326_T0003, BGB_326_T0004, BGB_326_T0005, BGB_326_T0006, BGB_326_T0007, BGB_326_T0008, BGB_326_T0009, BGB_326_T0010, BGB_441_T0004, BGB_441_T0005

```python
from bgbcalc import gegenleistung_teilbefreiung_betraege
gegenleistung_teilbefreiung_betraege(
    vereinbarte_gegenleistung='1000',
    wert_vollstaendiger_leistung='2000',
    wert_verbleibender_teilleistung='1500',
    darauf_gezahlter_betrag='1000',
    einordnungsnachweis='§326I in Verbindung mit441III und326IV: qualifizierte Teilbefreiung, konsistente Vergleichswerte entsprechend441III; keine beliebige Mengen- oder Zeitquote und keine zusätzliche Minderungserklärung erforderlich.326I2 bei bloß nicht zu erbringender Nacherfüllung, Behaltensanspruch326II und Ersatzverlangen326III gesondert. Rückforderungsbetrag ist ausschließlich bereits auf den hier entfallenen Gegenleistungsanteil Gezahltes; weitere Rückgewährvoraussetzungen346–348 und gegenseitige Ansprüche gesondert. Keine automatische Aufrechnung oder zusätzliche Schadensberechnung. Bezugswert muss positiv sein; anderer Fall mit nicht bestimmbarem Wert nicht durch fiktive1 ersetzen.',
)
```
