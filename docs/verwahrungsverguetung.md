<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## verwahrung_vorzeitige_teilverguetung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `gesamtverguetung`: Nichtnegative EUR-Vergütung für den vorzeitig beendeten Aufbewahrungsumfang.
- `leistungsanteil_zaehler`: Nichtnegative ganze Zahl des bis zur Beendigung erbrachten bewerteten Leistungsanteils, höchstens Nenner und2^53-1.
- `leistungsanteil_nenner`: Positive ganze Bezugsgröße der gesamten betrachteten Leistung, höchstens2^53-1. Keine automatische Zeitquote.
- `leistungsstandsnachweis`: Nichtleerer Nachweis vorzeitiger Beendigung699II und des bewerteten Leistungsstands; keine abweichende Vergütungsvereinbarung.

Gesamtvergütung der vorzeitig beendeten Aufbewahrung mit dem bewerteten Anteil der bis zur Beendigung erbrachten Leistungen multiplizieren.

wert: exakter EUR-Vergütungsbruch für die erbrachte Leistung.

§699II: vorzeitiges Aufbewahrungsende ohne abweichende Vergütungsvereinbarung. Teilbetrag entspricht rechtlich bewerteter bisheriger Leistung; keine ungeprüfte Tagesquote. Keine volle Vergütung nicht erbrachter Leistungen. Bereits geleistete Vergütung, Aufwendungsersatz und Zinsen bei Eigennutzung698 separat abrechnen; keine automatische Aufrechnung.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_699_T0003

```python
from bgbcalc import verwahrung_vorzeitige_teilverguetung
verwahrung_vorzeitige_teilverguetung(
    gesamtverguetung='1000',
    leistungsanteil_zaehler=1,
    leistungsanteil_nenner=4,
    leistungsstandsnachweis='§699II: vorzeitiges Aufbewahrungsende ohne abweichende Vergütungsvereinbarung. Teilbetrag entspricht rechtlich bewerteter bisheriger Leistung; keine ungeprüfte Tagesquote. Keine volle Vergütung nicht erbrachter Leistungen. Bereits geleistete Vergütung, Aufwendungsersatz und Zinsen bei Eigennutzung698 separat abrechnen; keine automatische Aufrechnung.',
)
```
