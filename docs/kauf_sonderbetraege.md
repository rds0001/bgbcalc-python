<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## neuverkauf_kosten_und_mindererloes

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `urspruenglicher_verkaufspreis`: Nichtnegativer rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge oder Bruchobjekt zaehler/nenner; gleiche Bewertungsbasis, keine Doppelzählung.
- `neuer_verkaufspreis`: Nichtnegativer rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge oder Bruchobjekt zaehler/nenner; gleiche Bewertungsbasis, keine Doppelzählung.
- `kosten_neuverkauf`: Nichtnegativer rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge oder Bruchobjekt zaehler/nenner; gleiche Bewertungsbasis, keine Doppelzählung.
- `einordnungsnachweis`: Nichtleerer Nachweis des gesetzlichen Anwendungsfalls und der rechtlich qualifizierten Beträge; kein automatischer Anspruchstatbestand.

Kosten des neuen Verkaufs plus positiver Mindererlös gegenüber ursprünglichem Verkauf

wert ist der exakt berechnete EUR-Betrag als Bruchobjekt.

Nur§451 Absatz2 nach qualifizierter Genehmigungsverweigerung und dadurch veranlasstem Neuverkauf. Mehrerlös wird nicht gegen Neuverkaufskosten aufgerechnet; kein automatischer Gesamtschadensersatz.

Nichtnegative exakte EUR-Beträge und sichere Zwischenwerte nachNUMERIK; positiveGesamtwertbasis und validierteTeilgrenzen.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_451_T0003

```python
from bgbcalc import neuverkauf_kosten_und_mindererloes
neuverkauf_kosten_und_mindererloes(
    urspruenglicher_verkaufspreis='1000',
    neuer_verkaufspreis='800',
    kosten_neuverkauf='50',
    einordnungsnachweis='Qualifizierte Genehmigungsverweigerung und Neuverkaufswerte.',
)
```

## vorkauf_gesamtpreisanteil

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `gesamtpreis`: Nichtnegativer rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge oder Bruchobjekt zaehler/nenner; gleiche Bewertungsbasis, keine Doppelzählung.
- `wert_vorkaufsgegenstand`: Nichtnegativer rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge oder Bruchobjekt zaehler/nenner; gleiche Bewertungsbasis, keine Doppelzählung.
- `wert_gesamtkauf`: Nichtnegativer rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge oder Bruchobjekt zaehler/nenner; gleiche Bewertungsbasis, keine Doppelzählung. Striktpositiv und mindestens Gegenstandswert.
- `einordnungsnachweis`: Nichtleerer Nachweis des gesetzlichen Anwendungsfalls und der rechtlich qualifizierten Beträge; kein automatischer Anspruchstatbestand.

Gesamtpreis mit Wert des Vorkaufsgegenstands geteilt durch positiven Wert des Gesamtkaufs multiplizieren

wert ist der exakt berechnete EUR-Betrag als Bruchobjekt.

Nur§467 Satz1, rechtlich qualifiziertes Wertverhältnis als Eingabe. Bei Verlangen der Gesamterstreckung nach Satz2 anderen Umfang bewerten; keine automatische Alleinbewertung oder Kopfteilung. Gegenstandswert darf Gesamtwert nicht übersteigen.

Nichtnegative exakte EUR-Beträge und sichere Zwischenwerte nachNUMERIK; positiveGesamtwertbasis und validierteTeilgrenzen.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_467_T0001

```python
from bgbcalc import vorkauf_gesamtpreisanteil
vorkauf_gesamtpreisanteil(
    gesamtpreis='1000',
    wert_vorkaufsgegenstand='1',
    wert_gesamtkauf='3',
    einordnungsnachweis='Qualifiziertes Wertverhältnis des Vorkaufsgegenstands im Gesamtkauf.',
)
```

## vorkauf_preis_mit_nebenleistungswert

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `kaufpreis`: Nichtnegativer rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge oder Bruchobjekt zaehler/nenner; gleiche Bewertungsbasis, keine Doppelzählung.
- `zu_ersetzender_nebenleistungswert`: Nichtnegativer rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge oder Bruchobjekt zaehler/nenner; gleiche Bewertungsbasis, keine Doppelzählung.
- `einordnungsnachweis`: Nichtleerer Nachweis des gesetzlichen Anwendungsfalls und der rechtlich qualifizierten Beträge; kein automatischer Anspruchstatbestand.

Kaufpreis um qualifizierten Geldwert der nicht selbst erfüllbaren Nebenleistung erhöhen

wert ist der exakt berechnete EUR-Betrag als Bruchobjekt.

Nur§466 monetär schätzbare und rechtlich zu ersetzende Nebenleistung, die Vorkaufsberechtigter nicht selbst bewirken kann. Keine Wertbestimmung und kein Wert einer nach§466 unbeachtlichen Nebenleistungsvereinbarung. Kaufpreis darf diesen Wert noch nicht enthalten.

Nichtnegative exakte EUR-Beträge und sichere Zwischenwerte nachNUMERIK; positiveGesamtwertbasis und validierteTeilgrenzen.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_466_T0001

```python
from bgbcalc import vorkauf_preis_mit_nebenleistungswert
vorkauf_preis_mit_nebenleistungswert(
    kaufpreis='1000',
    zu_ersetzender_nebenleistungswert='200',
    einordnungsnachweis='Schätzbare, nicht selbst erfüllbare und zu ersetzende Nebenleistung.',
)
```

## vorkauf_stundungssicherheit

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `gestundeter_kaufpreis`: Nichtnegativer rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge oder Bruchobjekt zaehler/nenner; gleiche Bewertungsbasis, keine Doppelzählung.
- `bereits_qualifiziert_gesicherter_teil`: Nichtnegativer rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge oder Bruchobjekt zaehler/nenner; gleiche Bewertungsbasis, keine Doppelzählung. Nur§468II-befreiter Teil,0wennkeinFall, höchstens gestundeterKaufpreis.
- `einordnungsnachweis`: Nichtleerer Nachweis des gesetzlichen Anwendungsfalls und der rechtlich qualifizierten Beträge; kein automatischer Anspruchstatbestand.

Gestundeten Kaufpreis um den nach§468 Absatz2 von zusätzlicher Sicherheit befreiten Teil vermindern

wert ist der exakt berechnete EUR-Betrag als Bruchobjekt.

Befreiter Teil nur für qualifiziert vereinbarte Hypothek bzw.in Anrechnung auf Kaufpreis übernommene hypothekarische Schuld, entsprechend eingetragenes Schiff/Schiffsbauwerk; sonst0. Keine beliebige vorhandene Sicherheit anrechnen, Überlappungen vorab entfernen. Teil höchstens gestundeter Kaufpreis.

Nichtnegative exakte EUR-Beträge und sichere Zwischenwerte nachNUMERIK; positiveGesamtwertbasis und validierteTeilgrenzen.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_468_T0001, BGB_468_T0002, BGB_468_T0003

```python
from bgbcalc import vorkauf_stundungssicherheit
vorkauf_stundungssicherheit(
    gestundeter_kaufpreis='1000',
    bereits_qualifiziert_gesicherter_teil='300',
    einordnungsnachweis='Qualifiziert befreiter Hypothekenteil468II ohne Überlappung.',
)
```

## wiederkauf_verwendungsersatz

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `verwendungsaufwand`: Nichtnegativer rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge oder Bruchobjekt zaehler/nenner; gleiche Bewertungsbasis, keine Doppelzählung.
- `bewirkte_werterhoehung`: Nichtnegativer rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge oder Bruchobjekt zaehler/nenner; gleiche Bewertungsbasis, keine Doppelzählung.
- `einordnungsnachweis`: Nichtleerer Nachweis des gesetzlichen Anwendungsfalls und der rechtlich qualifizierten Beträge; kein automatischer Anspruchstatbestand.

Qualifizierten Verwendungsaufwand auf dadurch bewirkte Werterhöhung begrenzen

wert ist der exakt berechnete EUR-Betrag als Bruchobjekt.

Nur§459 Verwendungen vor Wiederkauf; keine Schätzungswertvereinbarung nach§460, die diesen Anspruch ausschließt. Kausale Werterhöhung extern bewerten; Wegnahmerecht und weitere Kosten gesondert.

Nichtnegative exakte EUR-Beträge und sichere Zwischenwerte nachNUMERIK; positiveGesamtwertbasis und validierteTeilgrenzen.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_459_T0001

```python
from bgbcalc import wiederkauf_verwendungsersatz
wiederkauf_verwendungsersatz(
    verwendungsaufwand='300',
    bewirkte_werterhoehung='200',
    einordnungsnachweis='Qualifizierte Verwendungen vor Wiederkauf ohne460-Sonderfall.',
)
```
