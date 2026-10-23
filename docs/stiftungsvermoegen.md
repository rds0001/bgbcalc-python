<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## stiftung_vermoegenszusammensetzung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `gewidmetes_vermoegen`: Bewerteter noch vorhandener Gesamtbestand der WidmungEUR, einschließlich separat sonstig gewidmetem Teil.
- `davon_sonstig_gewidmet`: Nach83bIII dem sonstigen Vermögen zugeordneter Teil, höchstens Gesamtwidmung.
- `zustiftungen`: Zusätzlicher zugeordneter Grundstockbestand, nicht bereits in Widmung erfasst.
- `umgewidmeter_grundstock`: Von Stiftung zusätzlich zum Grundstock bestimmter Bestand, nicht bereits in Widmung/Zustiftungen/sonstigem Rest erfasst.
- `weiteres_sonstiges_vermoegen`: Sonstiger Restbestand nach Abzug umgewidmeter Werte, ohne separat genannten sonstig gewidmeten Teil.
- `zuordnungsnachweis`: Nichtleere Bewertung und überschneidungsfreie Zuordnung der Bestände desselben Stichtags. Nur auf unbestimmte Zeit errichtete Stiftung.

Grundstock=Widmung−sonstigerWidmungsteil+Zustiftungen+Umwidmungen; sonstiges=sonstigerWidmungsteil+sonstigerRest; Gesamt=summe.

wert enthält grundstockvermoegen, sonstiges_vermoegen und stiftungsvermoegen als EUR-Brüche.

Keine Verbrauchsstiftung, keine unbereinigten historischen Zuflüsse, keine Doppelzählung einer internen Umwidmung. Erhaltung, Vermögensbewertung und Verwendbarkeit separat.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_83b_T0001, BGB_83b_T0002, BGB_83b_T0003, BGB_83b_T0004, BGB_83b_T0005, BGB_83b_T0006, BGB_83b_T0007, BGB_83b_T0008, BGB_83b_T0009

```python
from bgbcalc import stiftung_vermoegenszusammensetzung
stiftung_vermoegenszusammensetzung(
    gewidmetes_vermoegen='100',
    davon_sonstig_gewidmet='20',
    zustiftungen='30',
    umgewidmeter_grundstock='10',
    weiteres_sonstiges_vermoegen='5',
    zuordnungsnachweis='Gleicher Stichtag, überschneidungsfreie vorhandene Vermögensbestandteile.',
)
```

## stiftung_wiederaufstockungsrest

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `verbrauchter_grundstock`: Betrag eines rechtlich qualifizierten Grundstockverbrauchs nach83cII inEUR.
- `bereits_wiederaufgestockt`: Demselben Verbrauch auf gleicher Bewertungsbasis zugeordnete bisherige AuffüllungEUR.
- `zuordnungsnachweis`: Nichtleerer Nachweis der Zuordnung, keine doppelt angerechnete Auffüllung.

max(Verbrauch−zugeordneteAuffüllung,0).

wert ist verbleibender Auffüllungsbetrag als exakter EUR-Bruch.

Keine Bewertung angemessener Zeit, keine Zulässigkeit des Verbrauchs, keine Entnahmefreigabe bei Überschuss.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_83c_T0001, BGB_83c_T0002, BGB_83c_T0003, BGB_83c_T0004, BGB_83c_T0005, BGB_83c_T0006

```python
from bgbcalc import stiftung_wiederaufstockungsrest
stiftung_wiederaufstockungsrest(
    verbrauchter_grundstock='100',
    bereits_wiederaufgestockt='40',
    zuordnungsnachweis='Derselbe qualifizierte Verbrauch, keine Doppelanrechnung.',
)
```
