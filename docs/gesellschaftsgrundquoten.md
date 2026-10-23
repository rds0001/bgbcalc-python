<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## gesellschaft_gewinn_verlust_stimmquoten

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `gesellschafter`: Vollständige Liste2..1000 Objekte mit eindeutiger gesellschafter_id und gewicht. Bei Beteiligungsverhältnis/Beitragswert nichtnegative exakte Dezimalzeichenfolge/Bruch, Summe positiv; bei gleiche_anteile ausdrücklich null.
- `quotenbasis`: beteiligungsverhaeltnisse, beitragswerte oder gleiche_anteile; gesetzliche Vorrangfolge rechtlich qualifiziert auswählen.
- `einordnungsnachweis`: Nichtleerer Nachweis der vereinbarten Verhältnisse/Werte beziehungsweise deren Fehlens und desselben vollständigen Gesellschafterkreises.

Vereinbarte Beteiligungsverhältnisse, sonst vereinbarte Beitragswerte durch ihre Summe normieren; sonst1/Anzahl.

wert ist Liste gesellschafter_id/quote, Quoten exakte Bruchobjekte mit Summe1.

§709 Absatz3: vereinbarte Beteiligungsverhältnisse gehen vor vereinbarten Beitragswerten; nur wenn beides fehlt Gleichanteile. quotenbasis ist rechtlich qualifiziert auszuwählen, kein freies Wahlrecht zur günstigeren Quote. Beteiligungsgewichte sind relative Verhältnisse, Beitragswerte vertraglich vereinbarte gleichartige Werte, keine von der Bibliothek geschätzten tatsächlichen Leistungen. Vollständiger identischer Gesellschafterkreis; individuelle Sondervereinbarungen über Gewinn/Verlust/Stimmkraft gesondert behandeln. Bei fehlender Wertevereinbarung ausdrücklich gewicht=null, nicht unbekannte Aktenlage. Beitragsleistungspflichten nach Absatz2 und Ausschüttungsbetrag nicht berechnet.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_709_T0003, BGB_709_T0004, BGB_709_T0005

```python
from bgbcalc import gesellschaft_gewinn_verlust_stimmquoten
gesellschaft_gewinn_verlust_stimmquoten(
    gesellschafter=[{'gesellschafter_id': 'A', 'gewicht': '2'}, {'gesellschafter_id': 'B', 'gewicht': '3'}],
    quotenbasis='beteiligungsverhaeltnisse',
    einordnungsnachweis='Qualifizierter709III-Vorrangfall und vollständiger Gesellschafterkreis.',
)
```
