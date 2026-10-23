<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## verjaehrung_selbstbestimmungszeitraum

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `fristlauf_erster_tag`: Erster rechtlich qualifizierter Verjährungslauftag alsISO-Datum.
- `grundfrist_letzter_tag`: Letzter Tag ohne diese Hemmung, nicht vor erstem Fristtag.
- `geburtsdatum`: ISO-Geburtstag des Anspruchsgläubigers, nicht nach Fristbeginn.
- `gemeinschaft_bei_fristbeginn`: Expliziter Wahrheitswert, ob bei Verjährungsbeginn häusliche Gemeinschaft mit Schuldner bestand.
- `letzter_gemeinschaftstag`: BeiTRUE Pflichtdatum des letzten eingeschlossenen Hemmungstags der ununterbrochenen anfänglichen Gemeinschaft; beiFALSE NULL. Kein Auswertungsstichtag einer laufenden Gemeinschaft.
- `einordnungsnachweis`: Nichtleerer Nachweis des208-Anspruchs und der rechtlich normalisierten zeitlichen Voraussetzungen.

Altersintervall bis Tag vor21 und gegebenenfalls anfängliches Gemeinschaftsintervall bilden; vorhandener209-Kern zählt Vereinigungsdauer und verschiebt Fristablauf.

wert enthält rechnerischer_letzter_tag und beruecksichtigte_hemmungstage.

Nur208-Ansprüche, keine neu begonnene spätere Gemeinschaft. Andere Hemmungen/Ablaufhemmung/Neubeginn und193 separat.

ISO-Daten und Ergebnisse0001..9999 mit darstellbarer21-Jahresgrenze.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_208_T0001, BGB_208_T0002

```python
from bgbcalc import verjaehrung_selbstbestimmungszeitraum
verjaehrung_selbstbestimmungszeitraum(
    fristlauf_erster_tag='2030-01-01',
    grundfrist_letzter_tag='2030-01-10',
    geburtsdatum='2009-01-10',
    gemeinschaft_bei_fristbeginn=True,
    letzter_gemeinschaftstag='2030-01-20',
    einordnungsnachweis='Qualifizierter208-Anspruch, anfängliche Gemeinschaft mit tatsächlichem Ende.',
)
```
