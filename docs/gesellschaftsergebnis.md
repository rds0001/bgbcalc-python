<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## gesellschaft_gewinn_verlust_betraege

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `gesellschaftsergebnis`: Rechtlich und rechnerisch festgestelltes Ergebnis der betrachteten Periode in EUR als exakter Dezimaltext oder Bruchobjekt. Positiv Gewinn, negativ Verlust, null ausgeglichen. Keine automatische Bilanzierung oder Feststellung eines Auszahlungsanspruchs.
- `gesellschafter`: Vollständige Liste2..1000 Objekte mit eindeutiger gesellschafter_id und gewicht. Bei Beteiligungsverhältnis/Beitragswert nichtnegative exakte Dezimalzeichenfolge/Bruch, Summe positiv; bei gleiche_anteile ausdrücklich null.
- `quotenbasis`: beteiligungsverhaeltnisse, beitragswerte oder gleiche_anteile; gesetzliche Vorrangfolge rechtlich qualifiziert auswählen.
- `einordnungsnachweis`: Nichtleerer Nachweis der vereinbarten Verhältnisse/Werte beziehungsweise deren Fehlens und desselben vollständigen Gesellschafterkreises.

Vorhandenen709-Quotenkern anwenden; vorzeichenbehaftetes festgestelltes Gesellschaftsergebnis mit jeder Quote exakt multiplizieren.

wert: Liste gesellschafter_id, quote und vorzeichenbehafteter ergebnisanteil; exakte Brüche. Summe der Ergebnisanteile entspricht exakt dem eingegebenen Gesellschaftsergebnis.

§§709III/718: festgestelltes Gesellschaftsergebnis mit rechtlich ausgewählter Gewinn-/Verlustquote verteilen. Beteiligungsverhältnisse haben Vorrang vor vereinbarten Beitragswerten, sonst gleiche Anteile. Individuelle abweichende Gewinn-/Verlustvereinbarungen und wechselnder Gesellschafterbestand gesondert. Rechnerische Ergebnisanteile sind nicht automatisch fällige Ausschüttungen oder sofortige Nachschusspflichten; keine Vermischung mit Liquidation oder Ausscheiden. Im Zweifel Rechnungsabschluss und Gewinnverteilung zum Kalenderjahresende718; abweichende Vereinbarung vorqualifizieren. Keine Rundung, kein Restcentverfahren.

Gesellschaftsergebnis vorzeichenbehaftet; Gewichte nichtnegativ und Quotensumme1. Gemeinsame exakte Zahlengrenzen nach NUMERIK.md, keine Rundung.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_709_T0003, BGB_709_T0004, BGB_709_T0005, BGB_718_T0001

```python
from bgbcalc import gesellschaft_gewinn_verlust_betraege
gesellschaft_gewinn_verlust_betraege(
    gesellschaftsergebnis='100',
    gesellschafter=[{'gesellschafter_id': 'Anna', 'gewicht': '1'}, {'gesellschafter_id': 'Bert', 'gewicht': '3'}],
    quotenbasis='beteiligungsverhaeltnisse',
    einordnungsnachweis='§§709III/718: festgestelltes Gesellschaftsergebnis mit rechtlich ausgewählter Gewinn-/Verlustquote verteilen. Beteiligungsverhältnisse haben Vorrang vor vereinbarten Beitragswerten, sonst gleiche Anteile. Individuelle abweichende Gewinn-/Verlustvereinbarungen und wechselnder Gesellschafterbestand gesondert. Rechnerische Ergebnisanteile sind nicht automatisch fällige Ausschüttungen oder sofortige Nachschusspflichten; keine Vermischung mit Liquidation oder Ausscheiden. Im Zweifel Rechnungsabschluss und Gewinnverteilung zum Kalenderjahresende718; abweichende Vereinbarung vorqualifizieren. Keine Rundung, kein Restcentverfahren.',
)
```
