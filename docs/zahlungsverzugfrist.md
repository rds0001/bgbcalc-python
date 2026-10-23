<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## entgeltforderung_dreissigtagefrist

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `faelligkeit_am`: ISO-Datum der rechtlich maßgeblichen Fälligkeit, nicht bloß Rechnungsdatum.
- `bezugsereignis_am`: ISO-Datum des tatsächlichen Zugangs der Rechnung/gleichwertigen Zahlungsaufstellung; bei rechtlich zulässigem Ersatzfall Datum des Gegenleistungsempfangs.
- `bezugsart`: rechnungszugang oder gegenleistungsempfang_bei_unsicherem_zugang. Ersatzfall ausschließlich Nichtverbraucher bei unsicherem Rechnungszugang.
- `dreissigtageregel_anwendbar`: Explizite Bestätigung des286III-Falls, bei Verbrauchern insbesondere besonderer Folgenhinweis; FALSE ergibt NICHT_ANWENDBAR.
- `einordnungsnachweis`: Nichtleerer Nachweis der Fälligkeit, Zugang/Empfang, Fallwahl und ggf.Verbraucherhinweis.

Maximum aus Fälligkeit und Bezugstag;30Tage Ereignisfrist und nachfolgender Kalendertag.

wert: massgeblicher_beginn, grundfristende und tag_nach_grundfrist alsISO-Daten.

Nur rechnerische Grundfrist. Kein endgültiger Verzugsbeginn: frühere Verzugsgründe, Leistung, Vertretenmüssen, wirksame Vereinbarungen und erforderliche Kalenderkorrekturen separat.

ISO-Daten im Bereich0001..9999 inklusive berechneter Folgetage; feste Fallwahl undWahrheitswert.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_286_T0009, BGB_286_T0010

```python
from bgbcalc import entgeltforderung_dreissigtagefrist
entgeltforderung_dreissigtagefrist(
    faelligkeit_am='2030-01-01',
    bezugsereignis_am='2030-01-10',
    bezugsart='rechnungszugang',
    dreissigtageregel_anwendbar=True,
    einordnungsnachweis='Synthetisch qualifizierter286III-Fall.',
)
```
