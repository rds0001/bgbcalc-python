<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## zahlung_belastungszeitgrenzen

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `auftragszugang_utc`: Tatsaechlicher rechtlich massgeblicher Zugang als sekundengenauer UTC-Zeitpunkt.
- `kontobelastung_utc`: Tatsaechliche Kontobelastung als sekundengenauer UTC-Zeitpunkt.
- `wertstellung_utc`: Tatsaechliche Belastungswertstellung als sekundengenauer UTC-Zeitpunkt.
- `einordnungsnachweis`: 675tIIIAnwendbarkeit und tatsaechliche zeitliche Zuordnung belegen; UTCvorher normalisieren.

Tatsaechliche Kontobelastung nicht vor Auftragszugang und Wertstellung nicht vor Belastung vergleichen.

Zwei getrennte einschliessliche UTC-Zeitgrenzenvergleiche.

§675tI2/III: Gutschriftspaetestens am qualifizierten Eingangsgeschaeftstag wertstellen; Belastung nicht vor tatsaechlichem Auftragszugang, Belastungswertstellung nicht vor tatsaechlicher Kontobelastung. Keine automatische Bankkalender-/Zeitzonenannahme. Eingangsgeschaeftstag nach tatsaechlichem Vorgang und anwendbarem Kalender qualifizieren, kein frei erfundener spaeterer Valutatag. Unverzuegliche Verfuegbarkeit und Verbraucherbareinzahlung675tII1 haben keine feste weitere BGB-Sekundenzahl; nicht als Erlaubnis bis Tagesende ausgeben. Nichtverbraucher-Bareinzahlung verwendet bestehenden Geschaeftstagskern675tII2.675tIVSperrfreigabe unverzueglich, genaue Zustimmungssumme ist qualitative Befugnisgrenze; keine erfundene fixe Haltefrist.675dVI/675tVSonderausnahmen vorqualifizieren.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_675t_T0008, BGB_675t_T0009

```python
from bgbcalc import zahlung_belastungszeitgrenzen
zahlung_belastungszeitgrenzen(
    auftragszugang_utc='2024-02-29T08:00:00Z',
    kontobelastung_utc='2024-02-29T09:00:00Z',
    wertstellung_utc='2024-02-29T09:00:00Z',
    einordnungsnachweis='§675tI2/III: Gutschriftspaetestens am qualifizierten Eingangsgeschaeftstag wertstellen; Belastung nicht vor tatsaechlichem Auftragszugang, Belastungswertstellung nicht vor tatsaechlicher Kontobelastung. Keine automatische Bankkalender-/Zeitzonenannahme. Eingangsgeschaeftstag nach tatsaechlichem Vorgang und anwendbarem Kalender qualifizieren, kein frei erfundener spaeterer Valutatag. Unverzuegliche Verfuegbarkeit und Verbraucherbareinzahlung675tII1 haben keine feste weitere BGB-Sekundenzahl; nicht als Erlaubnis bis Tagesende ausgeben. Nichtverbraucher-Bareinzahlung verwendet bestehenden Geschaeftstagskern675tII2.675tIVSperrfreigabe unverzueglich, genaue Zustimmungssumme ist qualitative Befugnisgrenze; keine erfundene fixe Haltefrist.675dVI/675tVSonderausnahmen vorqualifizieren.',
)
```

## zahlung_gutschrift_wertstellung

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `eingangsgeschaeftstag`: Qualifizierter tatsaechlicher Eingangsgeschaeftstag beim Zahlungsdienstleister als ISO-Datum.
- `wertstellungsdatum`: Tatsaechlich gebuchtes Datum der Gutschrift-Wertstellung.
- `einordnungsnachweis`: 675tI2Anwendbarkeit, Eingangsgeschaeftstag und Bankkalender rechtlich belegen.

Tatsaechliches Gutschrift-Wertstellungsdatum mit Eingangsgeschaeftstag als spaetester Grenze vergleichen.

Spaetestes Datum und einschliesslicher Vergleich, keine automatische Verfuegbarkeitsentscheidung.

§675tI2/III: Gutschriftspaetestens am qualifizierten Eingangsgeschaeftstag wertstellen; Belastung nicht vor tatsaechlichem Auftragszugang, Belastungswertstellung nicht vor tatsaechlicher Kontobelastung. Keine automatische Bankkalender-/Zeitzonenannahme. Eingangsgeschaeftstag nach tatsaechlichem Vorgang und anwendbarem Kalender qualifizieren, kein frei erfundener spaeterer Valutatag. Unverzuegliche Verfuegbarkeit und Verbraucherbareinzahlung675tII1 haben keine feste weitere BGB-Sekundenzahl; nicht als Erlaubnis bis Tagesende ausgeben. Nichtverbraucher-Bareinzahlung verwendet bestehenden Geschaeftstagskern675tII2.675tIVSperrfreigabe unverzueglich, genaue Zustimmungssumme ist qualitative Befugnisgrenze; keine erfundene fixe Haltefrist.675dVI/675tVSonderausnahmen vorqualifizieren.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_675t_T0001, BGB_675t_T0002, BGB_675t_T0003, BGB_675t_T0004, BGB_675t_T0005

```python
from bgbcalc import zahlung_gutschrift_wertstellung
zahlung_gutschrift_wertstellung(
    eingangsgeschaeftstag='2024-02-29',
    wertstellungsdatum='2024-02-29',
    einordnungsnachweis='§675tI2/III: Gutschriftspaetestens am qualifizierten Eingangsgeschaeftstag wertstellen; Belastung nicht vor tatsaechlichem Auftragszugang, Belastungswertstellung nicht vor tatsaechlicher Kontobelastung. Keine automatische Bankkalender-/Zeitzonenannahme. Eingangsgeschaeftstag nach tatsaechlichem Vorgang und anwendbarem Kalender qualifizieren, kein frei erfundener spaeterer Valutatag. Unverzuegliche Verfuegbarkeit und Verbraucherbareinzahlung675tII1 haben keine feste weitere BGB-Sekundenzahl; nicht als Erlaubnis bis Tagesende ausgeben. Nichtverbraucher-Bareinzahlung verwendet bestehenden Geschaeftstagskern675tII2.675tIVSperrfreigabe unverzueglich, genaue Zustimmungssumme ist qualitative Befugnisgrenze; keine erfundene fixe Haltefrist.675dVI/675tVSonderausnahmen vorqualifizieren.',
)
```
