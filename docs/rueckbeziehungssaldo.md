<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## rueckbeziehung_leistungssaldo

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `sollwert_bei_rueckbeziehung`: Nichtnegativer rechtlich bewerteter kontrafaktischer LeistungswertEUR eines Beteiligten bei anfänglicher Gültigkeit/wirksamer Rückbeziehung.
- `bereits_erlangter_istwert`: Nichtnegativer bereits erlangter WertEUR desselben Leistungskreises, Zeitraum und Bewertungsbasis; tatsächliche Rückabwicklungen konsistent berücksichtigt.
- `regelfall`: vertragsbestaetigung_141 oder bedingungsrueckbeziehung_159.
- `bewertungsnachweis`: Nichtleere rechtliche Qualifikation und Bewertung beider Werte, Beteiligter und Stichtag; keine freie Wahl einer hypothetischen Rechtsfolge.

SignedSaldo=Soll−Ist; positiver Fehlbetrag und rechnerischer Mehrerhalt getrennt.

wert enthält rechnerischer_leistungssaldo, fehlender_leistungswert und uebersteigender_istwert alsEUR-Brüche.

Kein automatischer Rückgewähranspruch bei Mehrerhalt, keine Aufrechnung zwischen Beteiligten, keine Hypothesenbewertung.141II-Abweichungen und159-Bedingungseintritt/Rückbeziehungsvereinbarung vorqualifiziert.

Nichtnegative EUR-Eingaben; rechnerischer Leistungssaldo darf negativ sein. Exakte Brüche innerhalb gemeinsamem sicheren Zahlenbereich.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_141_T0002, BGB_159_T0001

```python
from bgbcalc import rueckbeziehung_leistungssaldo
rueckbeziehung_leistungssaldo(
    sollwert_bei_rueckbeziehung='100',
    bereits_erlangter_istwert='30',
    regelfall='vertragsbestaetigung_141',
    bewertungsnachweis='Gleicher Beteiligter/Leistungskreis, qualifizierte gesetzliche Rückbeziehung.',
)
```
