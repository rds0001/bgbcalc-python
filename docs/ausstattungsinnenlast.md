<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## ausstattung_persoenliche_innenlast

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `ausstattungsbetrag`: Nichtnegativer rechtlich qualifizierter versprochener/gewährter Ausstattungsbetrag aus Gesamtgut in EUR.
- `gesamtgutangemessener_betrag`: Nichtnegatives rechtlich bewertetes dem Gesamtgut entsprechendes Ausstattungsmaß in EUR; kein ungeprüfter Elternvermögenswert.
- `zugestimmter_mehrbetrag`: Nichtnegativer konkret zugestimmter Teil des Betrags über dem Gesamtgutmaß, höchstens tatsächlicher Mehrbetrag. Nur im Nichtverwalter-Elternfall, sonst0. Keine Doppelzählung mit bereits angemessenem Grundbetrag.
- `berechnungsfall`: Rechtlich qualifizierter Fall: gemeinschaftliches_kind_alleinverwalter; nichtgemeinschaftliches_kind_elternteil_alleinverwalter; nichtgemeinschaftliches_kind_elternteil_nichtverwalter; nichtgemeinschaftliches_kind_gemeinschaftliche_verwaltung.
- `zuordnungsnachweis`: Nichtleerer Nachweis von Kindeseinordnung, Elternteil/Verwalter, Gesamtgutmaß und gegebenenfalls konkreter Zustimmung zum Mehrbetrag.

Grundbetrag=min(Ausstattung,Gesamtgutmaß), Mehrbetrag=Ausstattung−Grundbetrag. Gemeinschaftliches Kind/Alleinverwalter: persönliche Last=Mehrbetrag. Nichtgemeinschaftliches Kind/Elternteil nicht verwaltend: Grundbetrag+zugestimmter Mehrbetrag. Sonstige modellierte Elternfälle: voller Ausstattungsbetrag.

wert enthält persoenliche_innenlast und nicht_als_persoenliche_innenlast_erfasst als EUR-Brüche. Letzterer weist keine andere persönliche Last zu.

Gesetzliche Innenlast ohne abweichende Vereinbarung. Bei gemeinschaftlichem Kind nach§1444I ist die persönliche Last des allein verwaltenden Ehegatten gemeint. Bei nichtgemeinschaftlichem Kind ist die persönliche Last des Elternteils gemeint:§1444II bei Alleinverwaltung,§1466 bei gemeinschaftlicher Verwaltung. Umfang der Ausstattung und Gesamtgutmaß rechtlich bewertet; keine automatische Bestimmung von Elternschaft, Kindeseigenschaft, Verwaltungsform oder Angemessenheit. Im Nichtverwalter-Elternfall Zustimmung ausschließlich als tatsächlich zugestimmter Teil des über dem Maß liegenden Mehrbetrags vorgeben; nicht pauschal irgendeinen zugestimmten Gesamtbetrag verwenden, da sonst Überlappungen doppelt zählen. Übriger Betrag wird nur als nicht dieser persönlichen Last zugeordnet ausgewiesen, nicht automatisch dem anderen Ehegatten oder einer Masse auferlegt. Keine Außenhaftung, Erfüllung, Schenkungsbewertung oder Ausgleichsfälligkeit berechnet.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1444_T0001, BGB_1444_T0002, BGB_1466_T0001

```python
from bgbcalc import ausstattung_persoenliche_innenlast
ausstattung_persoenliche_innenlast(
    ausstattungsbetrag='100',
    gesamtgutangemessener_betrag='60',
    zugestimmter_mehrbetrag='0',
    berechnungsfall='gemeinschaftliches_kind_alleinverwalter',
    zuordnungsnachweis='Gesetzlicher Fall ohne abweichende Vereinbarung; Gesamtgutmaß und konkrete Zustimmung belegt.',
)
```
