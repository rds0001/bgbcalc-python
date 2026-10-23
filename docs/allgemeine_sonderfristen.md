<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## verbrauchsstiftung_mindestdauer

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `errichtungsbeginn_am`: ISO-Datum des rechtlich bestimmten Beginns des Satzungszeitraums einer Verbrauchsstiftung.
- `errichtungsende_am`: ISO-Datum des letzten eingeschlossenen Tages der Errichtungszeit mit Ende am Tagesablauf; nicht vor Beginn.
- `beginnart`: ereignis oder tagesbeginn gemäß rechtlich qualifiziertem Satzungsbeginn. Zehn Kalenderjahre statt3650Tage.
- `einordnungsnachweis`: Nichtleere Begründung der Verbrauchsstiftung und Zeitbestimmung einschließlich Beginnart und einschließliches Ende.

Zehnjahresende nach qualifizierter Beginnart; festgelegtes einschließliches Ende mindestens so spät.

wert enthält zehnjahres_mindestende und mindestdauer_erreicht.

Nur numerische Voraussetzung§82 Satz2; keine Anerkennungsentscheidung, Prognose nachhaltiger Erfüllung oder automatische lineare Vermögensverbrauchsrate.

ISO-Daten und berechnete Grenzen0001..9999, explizite Beginnart/Wahrheitswerte soweit gefordert und nichtleerer Nachweis.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_82_T0001, BGB_82_T0002

```python
from bgbcalc import verbrauchsstiftung_mindestdauer
verbrauchsstiftung_mindestdauer(
    errichtungsbeginn_am='2028-02-29',
    errichtungsende_am='2038-02-28',
    beginnart='ereignis',
    einordnungsnachweis='Qualifizierte Satzungsdauer einer Verbrauchsstiftung.',
)
```

## verein_mitgliederschwund_antragsfrist

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `unterschreiten_am`: ISO-Datum des rechtlich maßgeblichen Unterschreitens von drei Vereinsmitgliedern, nicht späterer Kenntnis. Tatsächlichen Verlauf einschließlich Wiederanstieg qualifizieren; Schwelle separat mit vereins_mitgliederschwellen prüfbar.
- `einordnungsnachweis`: Nichtleere Begründung des Ereignisses und rechtlichen Anwendungsbereichs§73.

Ereignisdatum plus3 Kalendermonate.

wert enthält rechnerisches_antragsfristende.

Nur rechnerische Grundfrist; rechtliche Kalender-/Verfahrenskorrekturen separat. Keine Entziehung ohne gerichtliche Entscheidung.

ISO-Daten und berechnete Grenzen0001..9999, explizite Beginnart/Wahrheitswerte soweit gefordert und nichtleerer Nachweis.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_73_T0001

```python
from bgbcalc import verein_mitgliederschwund_antragsfrist
verein_mitgliederschwund_antragsfrist(
    unterschreiten_am='2030-01-31',
    einordnungsnachweis='Qualifiziertes Unterschreiten der Dreimitgliederschwelle.',
)
```

## vollmachtsurkunde_kraftlosigkeitsfrist

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `letzte_einrueckung_am`: ISO-Datum der letzten rechtlich maßgeblichen Einrückung einer ordnungsgemäß bewilligten/veröffentlichten Kraftloserklärung; nicht erste Veröffentlichung oder bloßer Widerruf.
- `vollmacht_widerruflich`: Expliziter Wahrheitswert zur rechtlichen Widerruflichkeit; FALSE ergibt NICHT_ANWENDBAR entsprechend§176 Absatz3.
- `einordnungsnachweis`: Nichtleere Begründung der letzten Einrückung, ordnungsgemäßen Veröffentlichung und Widerruflichkeit.

Letzte Einrückung plus1 Kalendermonat als Ereignisfrist; Wirkung mit Tagesablauf.

wert enthält kraftlosigkeitsfristende, bei fehlender Widerruflichkeit null.

ZPO-Veröffentlichungsvoraussetzungen und Zuständigkeit nicht automatisch geprüft; keine pauschale§193-Verschiebung.

ISO-Daten und berechnete Grenzen0001..9999, explizite Beginnart/Wahrheitswerte soweit gefordert und nichtleerer Nachweis.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_176_T0001, BGB_176_T0002, BGB_176_T0004

```python
from bgbcalc import vollmachtsurkunde_kraftlosigkeitsfrist
vollmachtsurkunde_kraftlosigkeitsfrist(
    letzte_einrueckung_am='2030-01-31',
    vollmacht_widerruflich=True,
    einordnungsnachweis='Letzte ordnungsgemäße Einrückung, Vollmacht widerruflich.',
)
```
