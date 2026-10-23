<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## fund_anzeigewertgrenze

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `sachenwert`: Nichtnegativer rechtlich bewerteter Wert der gefundenen SacheEUR.

Strikter Vergleich Sachenwert>10EUR, Gleichheit genügt nicht.

wert enthält wertgrenze als EUR-Bruch und wertgrenze_ueberschritten.

Nur numerische965II-Anzeigegrenze; keine Befreiung von965I oder sonstigen Finderpflichten.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_965_T0003

```python
from bgbcalc import fund_anzeigewertgrenze
fund_anzeigewertgrenze(
    sachenwert='0',
)
```

## liquidatoren_einstimmigkeitsgrenze

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `anzahl_liquidatoren`: Ganze Zahl1..2^53−1 des qualifizierten Liquidatorenkreises.
- `zustimmende_liquidatoren`: Ganze Zahl0..AnzahlLiquidatoren der tatsächlich anrechenbaren Zustimmungen.

ErforderlicheStimmen=AnzahlLiquidatoren; Fehlbetrag=Anzahl−Zustimmungen; erreicht genau bei Gleichheit.

wert enthält erforderliche_zustimmungen, fehlende_zustimmungen und einstimmigkeit_erreicht.

Nur gesetzlicher Grundfall ohne abweichende Bestimmung. Keine Beschluss-/Vertretungswirksamkeitsentscheidung.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_48_T0004

```python
from bgbcalc import liquidatoren_einstimmigkeitsgrenze
liquidatoren_einstimmigkeitsgrenze(
    anzahl_liquidatoren=3,
    zustimmende_liquidatoren=2,
)
```
