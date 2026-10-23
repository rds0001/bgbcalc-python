<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## gesellschaft_ausscheidensfehlbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `gesellschaftsverbindlichkeiten`: Nichtnegativer exakter qualifizierter EUR-Wert als Dezimalzeichenfolge/Bruchobjekt; gleiche Stichtags-/Bewertungsbasis.
- `wert_gesellschaftsvermoegen`: Nichtnegativer exakter qualifizierter EUR-Wert als Dezimalzeichenfolge/Bruchobjekt; gleiche Stichtags-/Bewertungsbasis.
- `gewinn_verlust_anteil`: Qualifizierter exakter Gewinn-/Verlustanteil des Ausgeschiedenen zwischen0und1 als Dezimalzeichenfolge/Bruchobjekt.
- `einordnungsnachweis`: Nichtleerer Nachweis des §728a-Ausscheidensfalls, maßgeblicher Werte und Gewinn-/Verlustquote.

Positiven Fehlbetrag aus Gesellschaftsverbindlichkeiten minus Gesellschaftsvermögen mit Gewinn-/Verlustanteil des Ausgeschiedenen multiplizieren

wert ist der anteilige Fehlbetrag in EUR als exaktes Bruchobjekt.

Nur §728a im qualifizierten Ausscheidensfall. Vermögens- und Verbindlichkeitswerte auf rechtlich einheitlichen Stichtag und Bewertungsumfang beziehen; Gewinn-/Verlustanteil aus Vereinbarung bzw. §709 rechtlich bestimmen. Kein automatischer Abfindungswert nach §728, keine Liquidations-Beitragsrückerstattung nach §736d/737 und kein Ausfall anderer Gesellschafter. Gesellschaftsanteil zwischen null und eins; bereits geleistete Fehlbetragszahlungen gesondert anrechnen.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_728a_T0001

```python
from bgbcalc import gesellschaft_ausscheidensfehlbetrag
gesellschaft_ausscheidensfehlbetrag(
    gesellschaftsverbindlichkeiten='1000',
    wert_gesellschaftsvermoegen='400',
    gewinn_verlust_anteil='0.25',
    einordnungsnachweis='Qualifiziertes Ausscheiden, gleiche Stichtagswerte und Gewinn-/Verlustquote.',
)
```
