<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## gesamtgutszuwendung_anteile

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `zuwendungswert`: Rechtlich bewerteter nichtnegativer EUR-Wert einer einzelnen Gesamtgutszuwendung; exakte Dezimalzeichenfolge oder Bruch. Keine eigene Schenkungsbewertung.
- `abstammungszuordnung`: keine, ehegatte_1 oder ehegatte_2. Ausschließlich die Abstammungsausnahme des§2331 Absatz1 Satz2: Empfänger ist Abkömmling nur dieses Ehegatten oder Person, von der nur dieser Ehegatte abstammt. Gemeinsame Abstammung: keine.
- `ersatzpflichtzuordnung`: keine, ehegatte_1 oder ehegatte_2. Rechtlich festgestellte Ersatzpflicht dieses Ehegatten gegenüber dem Gesamtgut gerade wegen der Zuwendung. Widerspruch zur Abstammungszuordnung führt NICHT_ANWENDBAR; kein erfundener Vorrang.
- `gesamtgut_anwendbar`: Expliziter Wahrheitswert: Zuwendung stammt aus Gesamtgut der Gütergemeinschaft oder fortgesetzten Gütergemeinschaft§2331 Absatz2. FALSE ergibt NICHT_ANWENDBAR.
- `einordnungsnachweis`: Nichtleere rechtliche Begründung des Gesamtguts, der Bewertung und beider Sonderzuordnungen. Ehegatte_1/2 bezeichnet stets dieselben ursprünglichen Ehegatten.

Ohne Sonderzuordnung je Hälfte, bei eindeutiger Abstammungs-/Ersatzpflichtzuordnung alles diesem Ehegatten, dem anderen null. Exakte Multiplikation des Wertes mit den Quoten.

wert enthält quote_ehegatte_1, quote_ehegatte_2, betrag_ehegatte_1 und betrag_ehegatte_2 als exakte Brüche.

Keine eigene Wertbestimmung, Pflichtteilsquote, Abschmelzung oder Zahlungsforderung. Kollidierende Sonderzuordnungen außerhalb des Modells, NICHT_ANWENDBAR. Fortgesetzte Gütergemeinschaft entsprechend.

Nichtnegative exakte Beträge innerhalb gemeinsamer Numerikgrenzen, Auswahlwerte und Wahrheitswert.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2331_T0001, BGB_2331_T0002, BGB_2331_T0003

```python
from bgbcalc import gesamtgutszuwendung_anteile
gesamtgutszuwendung_anteile(
    zuwendungswert='101',
    abstammungszuordnung='keine',
    ersatzpflichtzuordnung='keine',
    gesamtgut_anwendbar=True,
    einordnungsnachweis='Synthetisch vollständig qualifiziertes Gesamtgut und Zuordnung nach§2331.',
)
```
