<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## darlehen_zehnjahresfrist_nach_vereinbarungen

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `vollstaendiger_empfang_am`: ISO-Datum des vollständigen Darlehensempfangs, nicht bloß erster Teilauszahlung.
- `neue_vereinbarungen_am`: Liste0..1000 ISO-Daten tatsächlich nach vollständigem Empfang geschlossener, rechtlich nach489I2 berücksichtigungsfähiger neuer Vereinbarungen über Rückzahlungszeit oder Sollzinssatz. Leere Liste nur bei festgestellt keiner solchen Vereinbarung.
- `einordnungsnachweis`: Nichtleerer Nachweis489I2, gebundener Sollzins und tatsächliche rechtlich qualifizierte Bezugsereignisse. Eine bloße einseitige Mitteilung oder Teilzahlung ist keine neue Vereinbarung.

Jüngsten qualifizierten Bezugsakt auswählen und zehn Kalenderjahre berechnen.

wert.massgeblicher_bezugstag und zehnjahresfrist_letzter_tag als ISO-Daten.

§489I2: Vollständiger Empfang als Ausgangspunkt, bei späteren qualifizierten Vereinbarungen jüngstes Vereinbarungsdatum; ab diesem Ereignistag zehn Kalenderjahre berechnen. Gleichdatierte Vereinbarungen verändern den Ausgangspunkt nicht mehrfach. Sechsmonatige Kündigungsfrist und Zweiwochenrückzahlung489III separat ab ihren jeweils tatsächlichen Auslösern. Keine automatische Fälligkeit, Kündigungserklärung oder Einstufung beliebiger Vertragsänderungen als Fristneustart.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_489_T0001, BGB_489_T0002, BGB_489_T0003

```python
from bgbcalc import darlehen_zehnjahresfrist_nach_vereinbarungen
darlehen_zehnjahresfrist_nach_vereinbarungen(
    vollstaendiger_empfang_am='2014-01-31',
    neue_vereinbarungen_am=[],
    einordnungsnachweis='§489I2: Vollständiger Empfang als Ausgangspunkt, bei späteren qualifizierten Vereinbarungen jüngstes Vereinbarungsdatum; ab diesem Ereignistag zehn Kalenderjahre berechnen. Gleichdatierte Vereinbarungen verändern den Ausgangspunkt nicht mehrfach. Sechsmonatige Kündigungsfrist und Zweiwochenrückzahlung489III separat ab ihren jeweils tatsächlichen Auslösern. Keine automatische Fälligkeit, Kündigungserklärung oder Einstufung beliebiger Vertragsänderungen als Fristneustart.',
)
```
