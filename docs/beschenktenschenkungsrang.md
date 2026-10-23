<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## pflichtteilsergaenzung_schenkungsvorgaenge

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `fehlbetrag`: Nichtnegative ergänzungsrechtliche EUR-Lücke.
- `schenkungen`: Liste1..1000: schenkung_id eindeutig,beschenkter_id mehrfach zulässig,schenkungsrang eindeutig höher=später,haftungsgrenze nichtnegative überschneidungsfreie rechtlich qualifizierte Vorgangsgrenze.
- `vorgangsgrenzen_qualifiziert`: Pflichtwahrheitswert: alle Vorgangsgrenzen bereits rechtlich qualifiziert; gemeinsame Personengrenzen dürfen nicht mehrfach angesetzt werden.
- `einordnungsnachweis`: Nichtleerer Nachweis von Rangfolge und Haftungsgrenzen.

Spätere Schenkungsvorgänge zuerst bis zu ihrer jeweiligen Grenze; verbleibende Lücke an vorherigen Vorgang. Danach Vorgangshaftung je tatsächlichem Empfänger summieren.

Haftung je Schenkung, aggregierte Haftung je Beschenktem und ungedeckte Lücke als exakte EUR-Brüche.

Keine simultanen Ränge, keine automatische Aufteilung einer gemeinsamen personenbezogenen Haftungsgrenze; rechtlich nicht verpflichtet ist nicht bloß zahlungsunfähig.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2329_T0003

```python
from bgbcalc import pflichtteilsergaenzung_schenkungsvorgaenge
pflichtteilsergaenzung_schenkungsvorgaenge(
    fehlbetrag='70',
    schenkungen=[{'schenkung_id': 'A1', 'beschenkter_id': 'A', 'schenkungsrang': 1, 'haftungsgrenze': '40'}, {'schenkung_id': 'B', 'beschenkter_id': 'B', 'schenkungsrang': 2, 'haftungsgrenze': '30'}, {'schenkung_id': 'A2', 'beschenkter_id': 'A', 'schenkungsrang': 3, 'haftungsgrenze': '20'}],
    vorgangsgrenzen_qualifiziert=True,
    einordnungsnachweis='Synthetische überschneidungsfreie Vorgangsgrenzen.',
)
```
