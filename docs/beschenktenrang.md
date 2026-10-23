<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## pflichtteilsergaenzung_beschenktenrang

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `fehlbetrag`: Nichtnegativer EUR-Ergänzungsfehlbetrag nach rechtlicher Abgrenzung zur Verpflichtung des Erben§2329 Absatz1, einschließlich Sonderfall pflichtteilsberechtigter Alleinerbe. Bloße Nichtzahlung des Erben genügt nicht.
- `beschenkte`: Unbenannte Liste mit1..1000 unterschiedlichen Personen, je genau beschenkter_id (nichtleere eindeutige Zeichenfolge), schenkungsrang (eindeutige ganze Zahl1..1000, höher bedeutet später) und haftungsgrenze (nichtnegative exakte EUR-Dezimalzeichenfolge/Bruchobjekt). Jede Person mit genau einer Schenkung; gleiche/ungeklärte Rangfolge und mehrere Schenkungen derselben Person außerhalb des Modells. Haftungsgrenzen nach Bereicherungsrecht und Einwendungen rechtlich vorgeben, nicht bloß historischen Geschenkewert.
- `beschenktenhaftung_2329_anwendbar`: Wahrheitswert der geprüften Anwendbarkeit der Beschenktenhaftung§2329 für Fehlbetrag und Schenkungen. FALSE ergibt NICHT_ANWENDBAR.
- `einordnungsnachweis`: Nichtleere Begründung des Fehlbetrags, Erben-/Alleinerbenfalls, rechtlich maßgeblicher Schenkungsreihenfolge und individuellen Haftungsgrenzen.

Nach Schenkungsrang absteigend jedem Beschenkten Minimum aus verbliebenem Fehlbetrag und rechtlicher Haftungsgrenze zuordnen; nur Rest früher Beschenkten zuordnen.

wert enthält zugeordnete_haftung als Liste in ursprünglicher Eingabereihenfolge mit beschenkter_id/haftungsbetrag und nicht_gedeckter_fehlbetrag; Beträge exakte EUR-Brüche. Außerhalb Anwendungsbereich NICHT_ANWENDBAR/null.

Früherer haftet soweit späterer nicht verpflichtet ist, nicht bloß bei Nichtzahlung. Ein Schenkungsvorgang je Person und eindeutige Reihenfolge. Bereicherungsrecht, gleichzeitige/mehrfache Schenkungen und tatsächliche Erfüllung separat; Geldwerte begründen keinen pauschalen Zahlungsanspruch.

1..1000 eindeutige Beschenkte und eindeutige Ränge1..1000, nichtnegative exakte EUR-Beträge. Alle exakten Ganzzahl-Zwischenwerte höchstens2^53-1.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2329_T0001, BGB_2329_T0002, BGB_2329_T0003, BGB_2329_T0004

```python
from bgbcalc import pflichtteilsergaenzung_beschenktenrang
pflichtteilsergaenzung_beschenktenrang(
    fehlbetrag='100',
    beschenkte=[{'beschenkter_id': '0', 'schenkungsrang': 1, 'haftungsgrenze': {'zaehler': '80', 'nenner': '1'}}, {'beschenkter_id': '1', 'schenkungsrang': 2, 'haftungsgrenze': {'zaehler': '30', 'nenner': '1'}}],
    beschenktenhaftung_2329_anwendbar=True,
    einordnungsnachweis='Synthetisch Erbe insoweit nicht verpflichtet; A früher und B später beschenkt, Grenzen bereicherungsrechtlich bestimmt.',
)
```
