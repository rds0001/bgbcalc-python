<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## zugewinnausgleich_vorausempfang_standardfall

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `zugewinn_zuwendender`: Nichtnegativer Zugewinn des ausschließlich zuwendenden Ehegatten vor§1380. Standardfall verlangt tatsächliche nichtnegative Vermögensdifferenz, nicht auf null abgeschnittenen Verlust.
- `zugewinn_empfaenger`: Nichtnegativer Zugewinn des ausschließlich empfangenden Ehegatten vor§1380; Empfang darf verbraucht sein oder Zugewinn unterschreiten; nach Herausrechnung Mindestwert null.
- `vorausempfang`: Nichtnegative Summe einseitiger wirksam zur Anrechnung bestimmter Zuwendungen, rechtlich maßgeblicher Zuwendungszeitwert einschließlich gebotener Wertanpassung. Keine gegenläufigen Empfänge oder unterschiedlichen Empfängerbereinigungswerte.
- `haftungsgrenze_zuwendender`: Nichtnegative rechtlich bestimmte Haftungsgrenze§1378 Absatz2 des Zuwendenden. Muss selbst vor Anrechnung errechnete Empfängerforderung decken, sonst NICHT_ANWENDBAR; keine ungeprüfte Kappungsreihenfolge.
- `haftungsgrenze_empfaenger`: Nichtnegative rechtlich bestimmte Haftungsgrenze§1378 Absatz2 des Empfängers. Muss gegebenenfalls separat errechnete Gegenforderung decken, sonst NICHT_ANWENDBAR.
- `standardfall_bestaetigt`: Explizite fachliche Bestätigung ausschließlich einseitiger Empfänge mit wirksamer Anrechnung, nichtnegativen tatsächlichen Vermögensdifferenzen, qualifiziert gleichem Zuwendungs- und Herausrechnungswert und ohne negative tatsächliche Vermögensdifferenz oder unterschiedliche Zuwendungs-/Herausrechnungswerte. FALSE ergibt NICHT_ANWENDBAR; keine eigenständige qualitative API.
- `bewertungsnachweis`: Nichtleere Herkunft und Begründung von Zugewinnen vor§1380, Zuwendungswerten, Anrechnungsbestimmung, Standardfall und Haftungsgrenzen.

Geberzugewinn plus Vorausempfang, Empfängerzugewinn minus Vorausempfang, mindestens null. Hälfte positiven Überschusses als Empfängerforderung, darauf Empfang maximal bis null anrechnen. Gegenforderung separat aus ursprünglichen Zugewinnen ohne§1380. Nur wenn Haftungsgrenzen beide relevanten Forderungen ohne Kürzung decken.

wert enthält bereinigte Zugewinne, ausgleichsforderung_vor_anrechnung, angerechneter_vorausempfang, restforderung_empfaenger, gegenforderung_ohne_1380, richtung und zahlbetrag. Eingrenzungsfälle außerhalb Standardmodells NICHT_ANWENDBAR.

Ausdrücklich begrenzter Standardfall; keine Freigabe negativer tatsächlicher Vermögensdifferenzen, verschiedener Bereinigungswerte, gegenseitiger Vorausempfänge oder eingreifender Haftungsbegrenzung. Keine Schenkungsteuerberechnung; sonstige Anspruchsmodifikationen offen.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1380_T0001, BGB_1380_T0003, BGB_1380_T0004

```python
from bgbcalc import zugewinnausgleich_vorausempfang_standardfall
zugewinnausgleich_vorausempfang_standardfall(
    zugewinn_zuwendender='100',
    zugewinn_empfaenger='40',
    vorausempfang='20',
    haftungsgrenze_zuwendender='1000',
    haftungsgrenze_empfaenger='1000',
    standardfall_bestaetigt=True,
    bewertungsnachweis='Synthetischer einseitiger Standardfall; tatsächliche Vermögensdifferenzen nichtnegativ, Vorausempfang vollständig wertgleich enthalten, Haftungsgrenzen greifen nicht ein.',
)
```
