<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## unterhalt_sicherheitsregelbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `monatsrente`: Nichtnegative qualifizierte konstante Monatsunterhaltsrente in EUR.
- `bewertungsnachweis`: Nichtleerer Nachweis der rechtlichen Höhe und Konstanz der Monatsrente für einfachen Jahresbetrag.

Einfacher Jahresbetrag=12×konstante Monatsrente.

wert ist einfacher Jahresbetrag als exakter EUR-Bruch, keine zwingende endgültige Sicherheitsleistung.

Rechnerische Regelsicherheitsgrenze nach§1585aI3 bei konstanter rechtlich qualifizierter Monatsrente. Keine automatische Sicherheitsleistungspflicht: Verlangen, Gefährdung, unbillige Belastung und Art der Sicherheit gesondert. Besondere Umstände können höhere Sicherheit rechtfertigen; dieser Regelbetrag ist keine ausnahmslose Höchstgrenze und keine freie gerichtliche Ermessensentscheidung. Wechselnde Rentenhöhen und zeitlich begrenzte Ansprüche außerhalb des konstanten Jahresansatzes separat bestimmen.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1585a_T0003

```python
from bgbcalc import unterhalt_sicherheitsregelbetrag
unterhalt_sicherheitsregelbetrag(
    monatsrente='300',
    bewertungsnachweis='Konstante qualifizierte Monatsrente300EUR.',
)
```

## verwaltungsanlagebetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `geldbestand`: Nichtnegativer verwalteter Geldbestand in EUR; Verwaltungsunterworfenheit und Bezugszeitpunkt qualifiziert.
- `ausgabenreserve`: Nichtnegativer rechtlich erforderlicher bereitgehaltener Ausgabenbedarf desselben Bezugszeitpunkts in EUR; kein frei gewählter Abschlag.
- `bewertungsnachweis`: Nichtleerer Nachweis zu Anwendungsfall§1642 oder§1841I, Geldbestand und qualifizierter Reserve.

Anlagebetrag=max(Geldbestand−Ausgabenreserve,0).

wert ist exakter EUR-Bruch.

Anlagebetrag nach§1642 für der elterlichen Verwaltung unterliegendes Kindesgeld oder§1841I für Geld des Betreuten nach Ausgabenbedarf§1839. Verwaltungsunterworfenheit, erforderliche Ausgabenreserve und Bewertungszeitpunkt rechtlich qualifiziert. Reserve ist kein frei gewählter Sicherheitsabschlag. Übersteigt Reserve den Bestand, Anlagebetrag0; kein automatisch festgestellter Zahlungsanspruch oder Fehlbetragsausgleich. Anlageform, wirtschaftliche Vermögensverwaltung, Kontoinhaberschaft, Genehmigung und Rendite nicht berechnet.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1642_T0001, BGB_1841_T0001

```python
from bgbcalc import verwaltungsanlagebetrag
verwaltungsanlagebetrag(
    geldbestand='1000',
    ausgabenreserve='300',
    bewertungsnachweis='Verwaltetes Geld und notwendiger Ausgabenbedarf zum selben Zeitpunkt qualifiziert.',
)
```
