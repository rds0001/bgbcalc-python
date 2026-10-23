<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## erbschaftskauf_zahlungsausgleich

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `abrechnungsposten`: Liste0..1000 eindeutiger Posten mit genau posten_id,postenart,zeitbezug,betrag,tatsaechliche_partei. Arten:nutzungen,gewoehnliche_lasten,schuldzinsen,erbschaftsabgaben,ausserordentliche_stammwertlasten,nachlassschuldtilgung. Zeitbezug:vor_kauf/ab_kauf, bereits rechtlich zeitanteilig abgegrenzt. Betrag nichtnegativ exakter EUR-Wert. Partei:kaeufer/verkaeufer, bei Nutzungen Empfänger, sonst tatsächlicher Zahler.
- `gesetzliche_lastenverteilung_qualifiziert`: Pflichtwahrheitswert für gesetzlichen Erbschaftskauffall ohne abweichende Vereinbarung; Tilgungen nur soweit Käuferpflicht2378 besteht, keine2376-Verkäuferhaftung. FALSE NICHT_ANWENDBAR.
- `abrechnungsnachweis`: Nichtleerer Nachweis tatsächlicher Zahlungen/Empfänge, zeitlicher Zuordnung und Lastenarten. Regelmäßige grenzüberschreitende Posten zuvor mit bestehendem Zeitanteilskern aufteilen.

Nutzungen/gewöhnliche Lasten/Zinsen vor Kauf Verkäufer, ab Kauf Käufer; Erbschaftsabgaben/Stammwertlasten/Tilgungen Käufer. Tatsächliche Partei mit Zuordnung vergleichen; gegenläufige Erstattungsbeträge summieren und signierten Saldo bilden.

wert enthält rechnerischer_ausgleich_kaeufer_an_verkaeufer,rechnerischer_ausgleich_verkaeufer_an_kaeufer und vorzeichenbehafteten saldo_zugunsten_verkaeufer als exakte EUR-Brüche.

Keine automatische Zeitbewertung oder Aufrechnung. Kaufpreis,2375/2381 und unberechtigte Zahlungen getrennt. Sonderlasten nur rechtlich qualifiziert.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2378_T0001, BGB_2378_T0002, BGB_2379_T0001, BGB_2379_T0002, BGB_2379_T0003, BGB_2380_T0002

```python
from bgbcalc import erbschaftskauf_zahlungsausgleich
erbschaftskauf_zahlungsausgleich(
    abrechnungsposten=[{'posten_id': 'N', 'postenart': 'nutzungen', 'zeitbezug': 'vor_kauf', 'betrag': '100', 'tatsaechliche_partei': 'kaeufer'}, {'posten_id': 'L', 'postenart': 'gewoehnliche_lasten', 'zeitbezug': 'vor_kauf', 'betrag': '20', 'tatsaechliche_partei': 'kaeufer'}, {'posten_id': 'T', 'postenart': 'nachlassschuldtilgung', 'zeitbezug': 'vor_kauf', 'betrag': '30', 'tatsaechliche_partei': 'verkaeufer'}],
    gesetzliche_lastenverteilung_qualifiziert=True,
    abrechnungsnachweis='Synthetisch rechtlich zugeordnete tatsächliche Zahlungen.',
)
```
