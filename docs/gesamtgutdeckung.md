<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## familienunterhalt_mittelvorrang

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `bedarf_dieser_mittelstufe`: Nichtnegativer bereits qualifizierter Bedarf, der aus der gewählten Mittelstufe zu decken ist, EUR.
- `gesamtgutsmittel`: Nichtnegative verfügbare Gesamtguteinkünfte oder Gesamtgutstamm je nach mittelart, EUR.
- `nachrangige_mittel`: Bei einkuenfte verfügbare Vorbehaltseinkünfte; bei vermoegensstamm verfügbare zusammengefasste Vorbehalts-/Sondergutstämme, nichtnegative EUR.
- `mittelart`: einkuenfte oder vermoegensstamm; rechtlich qualifizierte getrennte Mittelstufe, keine freie Umschichtung.
- `zuordnungsnachweis`: Nichtleerer Nachweis zu Mittelart, Bedarfszuordnung, Verfügbarkeit und identischem Bezugszeitraum.

Gesamtguteinsatz=min(Bedarf,Gesamtgutsmittel); nachrangiger Einsatz=min(Restbedarf,nachrangige Mittel); verbleibenden Bedarf und beide Restmittel ausweisen.

wert enthält einsatz_gesamtgut, einsatz_nachrangige_mittel, ungedeckter_bedarf, verbleibende_gesamtgutsmittel und verbleibende_nachrangige_mittel als EUR-Brüche.

§1420 enthält zwei getrennte Vorränge. mittelart=einkuenfte: Gesamtguteinkünfte vor Vorbehaltseinkünften. mittelart=vermoegensstamm: Gesamtgutstamm vor zusammengefasstem Vorbehalts-/Sondergutstamm. Bedarf und verfügbare Mittel für dieselbe qualifizierte Mittelstufe/Periode vorgeben. Keine zusätzliche allgemeine Reihenfolge zwischen Vorbehaltseinkünften und Gesamtgutstamm oder zwischen Vorbehalts-/Sondergutstamm erfunden; diese Funktion allein ist kein vollständiger Familienunterhaltsfinanzierungsplan. Keine Bedarfsermittlung, Verfügbarkeitsermittlung oder freie Vermögensmassenzuordnung.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1420_T0001

```python
from bgbcalc import familienunterhalt_mittelvorrang
familienunterhalt_mittelvorrang(
    bedarf_dieser_mittelstufe='100',
    gesamtgutsmittel='70',
    nachrangige_mittel='20',
    mittelart='einkuenfte',
    zuordnungsnachweis='Getrennte Einkünfteebene rechtlich bestimmt; keine globale Einkünfte-/Stamm-Rangfolge.',
)
```

## gesamtgut_vorzeitiger_berichtigungsbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `schuld`: Nichtnegative qualifizierte Innenlast in EUR gemäß§1446II oder§1468.
- `verfuegbares_vorbehaltsgut`: Nichtnegativer rechtlich verfügbarer Wert des Vorbehaltsguts des Schuldners in EUR.
- `verfuegbares_sondergut`: Nichtnegativer rechtlich verfügbarer Wert des Sonderguts des Schuldners in EUR.
- `zuordnungsnachweis`: Nichtleerer Nachweis des einschlägigen Verwaltungsfalls, der Innenlast und verfügbaren bereinigten Vermögenswerte.

Vorzeitige Berichtigung=min(Schuld,verfügbares Vorbehaltsgut+Sondergut); Rest=Schuld−Berichtigung.

wert enthält vorzeitiger_berichtigungsbetrag und restschuld als exakte EUR-Brüche.

Qualifizierte Innenlast gegenüber Gesamtgut oder Vorbehalts-/Sondergut des anderen Ehegatten. §1446II nur für den nicht allein verwaltenden Ehegatten; bei gemeinschaftlicher Verwaltung§1468. Verfügbarkeit der Vermögenswerte und konkurrierende Verpflichtungen rechtlich bereinigt. Keine Pflicht zur vorzeitigen Leistung aus Gesamtgut und keine Rangfolge zwischen Vorbehaltsgut und Sondergut erfunden. Restschuld wird nicht erlassen; gesetzlicher Aufschub bis Beendigung und weitere Fälligkeit rechtlich gesondert. Keine Außenhaftungsentscheidung.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1446_T0002, BGB_1468_T0001

```python
from bgbcalc import gesamtgut_vorzeitiger_berichtigungsbetrag
gesamtgut_vorzeitiger_berichtigungsbetrag(
    schuld='100',
    verfuegbares_vorbehaltsgut='20',
    verfuegbares_sondergut='30',
    zuordnungsnachweis='Innenlast und Verfügbarkeit qualifiziert, zutreffender Verwaltungsfall.',
)
```
