<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## pflichtteilsergaenzung_gleichzeitige_schenkungen

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `fehlbetrag`: Nach vorrangiger Erben-/späterer Beschenktenhaftung verbleibender Ergänzungsfehlbetrag in Euro.
- `beschenkte`: Liste2..1000 gleichzeitig Beschenkter, je genau beschenkter_id und massgeblicher_schenkungswert (positiver Euro-Wert unter dem rechtlich maßgeblichen Bewertungsmaßstab). Je Person genau ein zusammengefasster Wert derselben Zeitgruppe.
- `einordnungsnachweis`: Nichtleerer Nachweis der2329-Gleichzeitigkeitsgruppe, vollständiger Empfängerliste, richtigen Schenkungswerte und anwendbarer proportionaler Haftung. Keine zusätzlichen individuellen Kürzungen, Entreicherung oder gemeinsamen Personenrahmen in diesem Grundfall.

Fehlbetrag innerhalb einer qualifizierten Gleichzeitigkeitsgruppe proportional nach Schenkungswerten bis zur Summe dieser Werte aufteilen.

wert.beschenktenanteile in Eingabereihenfolge mit beschenkter_id und rechnerischer_haftungsanteil; nicht_gedeckter_fehlbetrag. Beträge als exakte Eurobrüche.

§2329III mit ergänzender Primärquelle AG Bielefeld, Urteil17.05.2019,409C30/18,Rn35: gleichzeitige Schenkungen anteilig nach maßgeblichen Schenkungswerten. Nur Grundfall ohne zusätzliche individuelle Haftungsbegrenzungen/Ausfälle und ohne gruppenübergreifende Personenrahmen. Fehlbetrag höchstens bis zur Summe dieser Schenkungswerte proportional zuordnen; größerer Rest bleibt für eine gesonderte Prüfung früherer Schenkungen. Nicht nach Köpfen, keine Gesamtschuld. Werte, Gleichzeitigkeit und Bereicherungs-/Pflichtteilsvoraussetzungen rechtlich qualifizieren; kein automatischer Geldanspruch statt Sachherausgabe. Kein allgemeiner Streitentscheid über Sonderfälle aus einem amtsgerichtlichen Urteil ableiten.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2329_T0001, BGB_2329_T0002, BGB_2329_T0003, BGB_2329_T0004

```python
from bgbcalc import pflichtteilsergaenzung_gleichzeitige_schenkungen
pflichtteilsergaenzung_gleichzeitige_schenkungen(
    fehlbetrag='6000',
    beschenkte=[{'beschenkter_id': 'A', 'massgeblicher_schenkungswert': '5000'}, {'beschenkter_id': 'B', 'massgeblicher_schenkungswert': '10000'}],
    einordnungsnachweis='§2329III mit ergänzender Primärquelle AG Bielefeld, Urteil17.05.2019,409C30/18,Rn35: gleichzeitige Schenkungen anteilig nach maßgeblichen Schenkungswerten. Nur Grundfall ohne zusätzliche individuelle Haftungsbegrenzungen/Ausfälle und ohne gruppenübergreifende Personenrahmen. Fehlbetrag höchstens bis zur Summe dieser Schenkungswerte proportional zuordnen; größerer Rest bleibt für eine gesonderte Prüfung früherer Schenkungen. Nicht nach Köpfen, keine Gesamtschuld. Werte, Gleichzeitigkeit und Bereicherungs-/Pflichtteilsvoraussetzungen rechtlich qualifizieren; kein automatischer Geldanspruch statt Sachherausgabe. Kein allgemeiner Streitentscheid über Sonderfälle aus einem amtsgerichtlichen Urteil ableiten.',
)
```
