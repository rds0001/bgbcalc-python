<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## ersatzerben_quoten

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `weggefallener_erbteil`: Positive exakte Quote bis1 eines einzelnen weggefallenen persönlichen Erbteils am Gesamtnachlass. Keine gesamte gemeinschaftliche Quote bei Wegfall nur eines Mitberechtigten.
- `ersatzerben`: Liste1..1000 eindeutiger tatsächlich berufener Ersatzerben vor Auswahl nach§2098 Absatz2. Je Objekt genau erbe_id (nichtleer), urspruenglicher_erbteil (positive exakte persönliche Quote am Gesamtnachlass), gleicher_gemeinschaftlicher_erbteil (Wahrheitswert der Zugehörigkeit zu derselben Gruppe wie weggefallene Person). Ursprüngliche Quoten plus weggefallener Anteil höchstens1; nicht berechtigte oder weggefallene Kandidaten vorab ausschließen.
- `gegenseitige_ersatzerbeneinsetzung`: Expliziter Wahrheitswert: Erben gegenseitig als Ersatzerben eingesetzt. Nur dann Gruppenrang§2098 Absatz2. FALSE setzt für Absatz1 qualifiziert voraus, dass übrige Erben als Ersatzerben für den weggefallenen eingesetzt sind.
- `auslegungsregel_anwendbar`: Expliziter Wahrheitswert, ob§2098 als Zweifelsregel einschlägig und keine abweichende testamentarische Anordnung maßgeblich ist; FALSE ergibt NICHT_ANWENDBAR.
- `einordnungsnachweis`: Nichtleere Begründung des einzelnen Wegfalls, tatsächlich berufenen Ersatzerbenkreises, ursprünglicher persönlicher Quoten, Gruppenbeziehungen und fehlender abweichender Anordnung. §§2096/2097 rechtlich vorqualifizieren.

Bei gegenseitiger Einsetzung und vorhandenen berufenen Mitberechtigten derselben gemeinschaftlichen Gruppe nur diese auswählen; sonst alle berufenen Ersatzerben. Ursprüngliche Quoten durch Summe ausgewählter Quoten teilen; mit weggefallenem Erbteil multiplizieren. Ersatzerbrecht hat Vorrang vor Anwachsung.

wert enthält gruppenvorrang_angewandt, ersatzerbquoten (erbe_id, anteil_am_weggefallenen_erbteil, zusaetzlicher_erbteil) und verbleibender_anteil_fuer_anwachsung (null als Bruch). Nicht vorrangige Kandidaten behalten Reihenfolge mit Zusatzquote0.

Ein einzelner Wegfall, keine Testamentsauslegung oder Kaskaden. Tatsächliche Berufung und Quoten vorqualifiziert. Ausgabe nur zusätzliche Quoten, ursprüngliche Erbteile werden nicht neu verteilt. Keine unbelegte Annahme gleicher Quoten.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2098_T0001, BGB_2098_T0002, BGB_2099_T0001

```python
from bgbcalc import ersatzerben_quoten
ersatzerben_quoten(
    weggefallener_erbteil='0.25',
    ersatzerben=[{'erbe_id': 'A', 'urspruenglicher_erbteil': '0.25', 'gleicher_gemeinschaftlicher_erbteil': False}, {'erbe_id': 'B', 'urspruenglicher_erbteil': '0.5', 'gleicher_gemeinschaftlicher_erbteil': False}],
    gegenseitige_ersatzerbeneinsetzung=False,
    auslegungsregel_anwendbar=True,
    einordnungsnachweis='Synthetisch qualifizierte Ersatzerbeneinsetzung und einzelne Wegfallquote; ursprüngliche persönliche Quoten bestimmt.',
)
```
