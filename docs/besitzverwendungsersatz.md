<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## besitz_notwendiger_verwendungsersatz

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `notwendige_eigene_verwendungen`: Nichtnegative eigene notwendige BruttoverwendungenEUR einschließlich Lasten nach995, ohne Vorgängerbetrag.
- `ausgeschlossene_erhaltungskosten`: In eigener Bruttosumme enthaltene gewöhnliche Erhaltungskosten für Zeit verbleibender Nutzungen.
- `ausgeschlossene_lasten`: Nicht ersatzfähige Lasten für Zeit verbleibender Nutzungen, nicht außergewöhnliche auf Stammwert gelegte Lasten. Keine Überschneidung mit Erhaltungskosten.
- `ersatzfaehige_vorgaengerverwendungen`: Separater rechtlich bereinigter ersatzfähiger Vorgängerbetrag nach999; nicht nochmals in eigenen Kosten enthalten.
- `zuordnungsnachweis`: Nichtleerer Nachweis994I-Fall, notwendige Verwendung, Zeitzuordnung/Lastenart und etwaige Rechtsnachfolge.

EigeneVerwendungen−ausgeschlosseneErhaltung−ausgeschlosseneLasten+bereinigteVorgängeransprüche.

wert ist bereinigter Ersatzbetrag als exakterEUR-Bruch.

Ausgeschlossene Posten müssen überschneidungsfreie Teile eigener Verwendungen sein.994II-GoA separat, keine automatische Prüfung997–1003 oder Fälligkeit.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_994_T0001, BGB_994_T0002, BGB_994_T0003, BGB_995_T0001, BGB_995_T0002, BGB_999_T0001, BGB_999_T0002

```python
from bgbcalc import besitz_notwendiger_verwendungsersatz
besitz_notwendiger_verwendungsersatz(
    notwendige_eigene_verwendungen='100',
    ausgeschlossene_erhaltungskosten='20',
    ausgeschlossene_lasten='10',
    ersatzfaehige_vorgaengerverwendungen='40',
    zuordnungsnachweis='Qualifizierte994I-Verwendungen und separat bereinigter999-Vorgängeranspruch.',
)
```
