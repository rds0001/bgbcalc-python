<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## hypothek_widerspruchs_und_meldungsfrist

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `fristfall`: versicherung_anzeige_1128, versicherung_untunlich_1128 oder hinterlegung_meldung_1171.
- `ausloeser_am`: 1128: tatsächlicher Empfang der Schadensanzeige; nur bei rechtlich untunlicher Anzeige stattdessen Fälligkeit der Versicherungssumme.1171: Rechtskraft des Ausschließungsbeschlusses. ISO-Datum.
- `erklaerung_am`: Qualifizierter tatsächlicher Eingang des Widerspruchs beim Versicherer beziehungsweise der Meldung bei der HinterlegungsstelleYYYY-MM-DD; kein bloßes Absendedatum.
- `werktagskorrektur_anwendbar`: Ausdrücklich rechtlich qualifizierter Wahrheitswert zur193-Anwendbarkeit auf diese Erklärungs-/Meldungsfrist; keine freie Fristverlängerungswahl.
- `feiertagskalender`: Bei anwendbarer193-Korrektur Objekt mit genau feiertage,ort,kalenderquelle,kalender_von,kalender_bis entsprechend werktagsverschiebung; andernfalls ausdrücklichNULL/None.
- `einordnungsnachweis`: Nichtleerer Nachweis des Normfalls, maßgeblichen Auslösers, richtigen Empfängers, kalendertäglicher Erfüllung und begründeter193-Einordnung.1128IIangemeldeteHypothek/Schriftzustimmung gesondert.

Hypothekenbezogene Erklärungs-/Meldungsgrundfrist berechnen und tatsächlichen Eingang vergleichen.

wert.grundfrist_letzter_tag/frist_letzter_tag alsISO-Datum, erklaerung_bis_fristende alsWahrheitswert, kalendertage_vom_eingang_bis_fristende als vorzeichenbehaftete ganzeZahl.

§1128I ein Monat ab qualifiziertem Auslöser;§1171III dreißig Jahre ab Rechtskraft. Grundfrist und gegebenenfalls rechtlich qualifizierte193-Korrektur über vorhandene Kalenderkerne berechnen; tatsächlichen Erklärungseingang bis einschließlich letztem Tag und verbleibenden Tagesabstand vergleichen. Keine automatische Auszahlung, Zustimmungsfiktion oder Erlöschensentscheidung; keine pauschale Gleichbehandlung von1128I und1128II.193-Anwendbarkeit ist rechtliche Voraussetzung, keine zusätzliche Zahlenschätzung. Keine untertägige Reihenfolge aus identischen Kalendertagen erfinden.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1128_T0001, BGB_1128_T0002, BGB_1128_T0003, BGB_1171_T0005

```python
from bgbcalc import hypothek_widerspruchs_und_meldungsfrist
hypothek_widerspruchs_und_meldungsfrist(
    fristfall='versicherung_anzeige_1128',
    ausloeser_am='2024-01-31',
    erklaerung_am='2024-02-29',
    werktagskorrektur_anwendbar=False,
    feiertagskalender=None,
    einordnungsnachweis='§1128I ein Monat ab qualifiziertem Auslöser;§1171III dreißig Jahre ab Rechtskraft. Grundfrist und gegebenenfalls rechtlich qualifizierte193-Korrektur über vorhandene Kalenderkerne berechnen; tatsächlichen Erklärungseingang bis einschließlich letztem Tag und verbleibenden Tagesabstand vergleichen. Keine automatische Auszahlung, Zustimmungsfiktion oder Erlöschensentscheidung; keine pauschale Gleichbehandlung von1128I und1128II.193-Anwendbarkeit ist rechtliche Voraussetzung, keine zusätzliche Zahlenschätzung. Keine untertägige Reihenfolge aus identischen Kalendertagen erfinden.',
)
```
