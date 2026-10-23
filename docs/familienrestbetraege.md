<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## betreuer_staatskassen_anspruchsuebergang

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `bestehender_betreueranspruch`: Nichtnegativer bestehender Anspruch des Betreuers gegen Betreuten vor betrachteter Zahlung in EUR, frühere Übergänge bereits abgezogen.
- `staatskassenbefriedigung`: Nichtnegative tatsächliche Staatskassenzahlung für genau diesen Anspruch in EUR.
- `zuordnungsnachweis`: Nichtleerer Nachweis des bestehenden Anspruchs und Zuordnung der Befriedigung ohne Doppelanrechnung.

Übergang=min(bestehender Anspruch,zugeordnete Staatskassenbefriedigung); verbleibender Anspruch=Anspruch−Übergang.

wert enthält uebergegangener_anspruch und verbleibender_betreueranspruch als EUR-Brüche.

§1881Satz1, ein rechtlich abgegrenzter bestehender Anspruch des Betreuers gegen den Betreuten unmittelbar vor der betrachteten Befriedigung. Zugeordnete Zahlung der Staatskasse für denselben Anspruch; frühere Zahlungen/Übergänge nicht nochmals einrechnen. Überschießende Zahlung erzeugt keinen zusätzlichen Anspruch gegen den Betreuten und keinen automatisch festgestellten Rückzahlungsanspruch. Entstehung/Höhe des Betreueranspruchs und Mittellosigkeit nicht geprüft. Die Erbenhaftung nachSatz2 wird in dieser Funktion nicht berechnet. Der separate Baustein betreuer_erbenhaftungsbetrag berechnet den BGB-Nachlasswertdeckel; externe102III/IV-SGB-XII-Ausnahmen bleiben ausdrücklich rechtlich vorzuqualifizieren.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1881_T0001

```python
from bgbcalc import betreuer_staatskassen_anspruchsuebergang
betreuer_staatskassen_anspruchsuebergang(
    bestehender_betreueranspruch='1000',
    staatskassenbefriedigung='300',
    zuordnungsnachweis='Bestehender Anspruch und zugeordnete tatsächliche Staatskassenleistung belegt.',
)
```

## minderjaehrigen_unterhaltsfehlbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `unterhaltsbedarf`: Nichtnegativer qualifizierter Bedarf des minderjährigen Kindes für bestimmte Periode in EUR.
- `anrechenbare_vermoegenseinkuenfte`: Nichtnegative rechtlich anrechenbare Vermögenserträge derselben Periode in EUR; kein Vermögensstamm.
- `anrechenbarer_arbeitsertrag`: Nichtnegativer rechtlich anrechenbarer Arbeitsertrag derselben Periode in EUR.
- `bewertungsnachweis`: Nichtleerer Nachweis von Minderjährigkeit/Elternbeziehung, Bedarf und Anrechenbarkeit; keine ungeprüften Bruttowerte.

Fehlbetrag=max(Bedarf−Vermögenserträge−Arbeitserträge,0), ohne Vermögensstamm.

wert ist exakter EUR-Fehlbetrag.

§1602II im Verhältnis des minderjährigen Kindes zu seinen Eltern. Bedürftigkeitsrest, kein abschließender Zahlungsanspruch gegen einzelne Elternteile. Kindesalter, Bedarf, Anrechenbarkeit und identischer Zeitraum rechtlich qualifiziert; Einkünfte nicht ungeprüft brutto einsetzen. Vermögensstamm wird nicht verbraucht und ist keine Eingabe. Rang, Leistungsfähigkeit, Kindergeldbehandlung, weitere Deckungsmittel, Naturalunterhalt und Elternverteilung gesondert und ohne Doppelanrechnung. Nicht ungeprüft auf volljährige Kinder übertragen.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1602_T0002

```python
from bgbcalc import minderjaehrigen_unterhaltsfehlbetrag
minderjaehrigen_unterhaltsfehlbetrag(
    unterhaltsbedarf='1000',
    anrechenbare_vermoegenseinkuenfte='100',
    anrechenbarer_arbeitsertrag='200',
    bewertungsnachweis='Qualifizierter minderjähriger Bedarf und anrechenbare Erträge derselben Periode.',
)
```

## zugewinnausgleich_sachanrechnungsrest

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `ausgleichsforderung`: Nichtnegative qualifizierte Ausgleichsforderung in EUR.
- `gerichtlicher_anrechnungsbetrag`: Nichtnegativer gerichtlich festgesetzter und rechtlich wirksam anzurechnender Betrag für bestimmte Gegenstände in EUR, kein selbst gewählter Marktwert.
- `anrechnungsnachweis`: Nichtleerer Beleg der gerichtlichen Festsetzung und tatsächlichen Anrechnungsvoraussetzung.

Rest=max(Ausgleichsforderung−gerichtlicher Anrechnungsbetrag,0).

wert ist exakter EUR-Restbruch.

Nur§1383I-Anrechnungsrechnung: Ausgleichsforderung bereits bestimmt, Anrechnungsbetrag gerichtlich festgesetzt und seine tatsächliche Anrechnungsvoraussetzung qualifiziert. Keinen Marktwert anstelle des festgesetzten Betrags einsetzen. Ob Anordnung/Übertragung/Erfüllung wirksam ist und wann anzurechnen ist, nicht automatisch entschieden. Übersteigt Anrechnungsbetrag die betrachtete Forderung, Rest0; kein automatisch festgestellter Überschuss-/Rückzahlungsanspruch. Keine erneute Zugewinn-, Sachwert- oder Billigkeitsbewertung.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1383_T0001

```python
from bgbcalc import zugewinnausgleich_sachanrechnungsrest
zugewinnausgleich_sachanrechnungsrest(
    ausgleichsforderung='1000',
    gerichtlicher_anrechnungsbetrag='300',
    anrechnungsnachweis='Wirksam anzurechnender gerichtlich festgesetzter Betrag belegt.',
)
```
