<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## pfand_verwertungsabrechnung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `gesicherte_forderung`: Nichtnegative noch offene gesicherte Forderung in EUR, rechtlich zugehörige Nebenleistungen nur einmal einbeziehen.
- `befriedigungsbasis`: Nichtnegative qualifizierte Basis in EUR:1247 nach Kosten/Rang verbleibender Verwertungserlös oder1259 gesamter Börsen-/Marktwert des Pfandes exakt am Fälligkeitstag.
- `verwertungsart`: erloes_1247 oder marktpreis_eigentumszufall_1259; keine Gleichsetzung der Bewertungszeitpunkte.
- `anwendungsfall_qualifiziert`: Explizite Bestätigung des Normfalls, bei1259 insbesondere persönlicher Anwendungsbereich und wirksame Eigentumszufall-Vereinbarung. FALSE ergibt NICHT_ANWENDBAR.
- `bewertungsnachweis`: Nichtleerer Nachweis zu Forderung, Kosten-/Rangbereinigung bzw.Fälligkeitstag und Marktwert, Doppelbefriedigung ausgeschlossen.

Tilgung=min(Forderung,Basis), Restforderung=Forderung−Tilgung, Überschuss=Basis−Tilgung.

wert enthält getilgte_forderung, restforderung und ueberschiessender_wert als EUR-Brüche.

Nur eine abgegrenzte Forderungsposition, keine Rangverteilung.1247-Überschuss ist Ersatzpfanderlös;1259-Überschuss nur Rechendifferenz ohne hier begründete Erstattungspflicht. Keine spätere Marktpreiswahl.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1247_T0001, BGB_1247_T0002, BGB_1259_T0001, BGB_1259_T0002

```python
from bgbcalc import pfand_verwertungsabrechnung
pfand_verwertungsabrechnung(
    gesicherte_forderung='100',
    befriedigungsbasis='30',
    verwertungsart='erloes_1247',
    anwendungsfall_qualifiziert=True,
    bewertungsnachweis='Synthetische rangbereinigte Basis; bei1259 Gesamtmarktwert am Fälligkeitstag.',
)
```
