<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## verbraucherdarlehen_fehlangaben_sollzinssatz

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `vertraglicher_sollzinssatz`: Vorzeichenbehaftete Jahresquote;0.05=5Prozent. Tatsächlich zugrunde gelegten Zinssatz rechtlich bestimmen.
- `fehlangabennachweis`: Geheilter Verbraucherdarlehensvertrag und fehlende Sollzins-, Effektivzins- oder Gesamtbetragsangabe494II qualifiziert; keine bloße Unterangabe nachIII.

Vertraglichen Jahreszinssatz auf höchstens den gesetzlichen Satz von vier Prozent vermindern.

Exakte vorzeichenbehaftete Jahresquote ohne Erhöhung niedrigerer Vertragssätze.

494II in Verbindung mit246: Jahresquote auf höchstens0.04 vermindern. Bereits niedrigerer oder negativer vertraglicher Satz wird nicht erhöht. Ergebnis ist nur die Zinsbasis; keine automatische Zahlungspflicht bei negativem Satz. Tatsächliche Zinsbeträge/Teilzahlungen anhand der rechtlich fortbestehenden Vertragsstruktur berechnen. Nicht mit der Differenzkorrektur bei zu niedrig angegebenem Effektivzins494III verwechseln.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_246_T0001, BGB_494_T0001, BGB_494_T0002, BGB_494_T0003, BGB_494_T0004, BGB_494_T0005, BGB_494_T0006, BGB_494_T0007, BGB_494_T0008, BGB_494_T0009, BGB_494_T0010, BGB_494_T0011

```python
from bgbcalc import verbraucherdarlehen_fehlangaben_sollzinssatz
verbraucherdarlehen_fehlangaben_sollzinssatz(
    vertraglicher_sollzinssatz='0.06',
    fehlangabennachweis='494II in Verbindung mit246: Jahresquote auf höchstens0.04 vermindern. Bereits niedrigerer oder negativer vertraglicher Satz wird nicht erhöht. Ergebnis ist nur die Zinsbasis; keine automatische Zahlungspflicht bei negativem Satz. Tatsächliche Zinsbeträge/Teilzahlungen anhand der rechtlich fortbestehenden Vertragsstruktur berechnen. Nicht mit der Differenzkorrektur bei zu niedrig angegebenem Effektivzins494III verwechseln.',
)
```
