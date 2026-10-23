<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## erbauflage_herausgabebegrenzung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `bereicherungsrechtlicher_zuwendungswert`: Nichtnegativer exakter EUR-Wert der rechtlich herauszugebenden Bereicherung aus der Zuwendung, einschließlich einschlägiger Einwendungen vorbewertet.
- `zur_auflagenvollziehung_erforderlicher_zuwendungsanteil`: Nichtnegativer exakter EUR-Wert gerade des Zuwendungsanteils, der zur Auflagenvollziehung hätte eingesetzt werden müssen; kein beliebiger Auflagen-/Schadenspauschalbetrag.
- `herausgabevoraussetzungen_2196_erfuellt`: Expliziter Wahrheitswert: Berechtigung und entweder schuldhafte Unmöglichkeit2196I oder erfolglose zulässige Zwangsmittel nach rechtskräftigem Urteil bei nicht durch Dritte vollziehbarer Auflage2196II. Bloße Nichtvollziehung genügt nicht.
- `bewertungsnachweis`: Nichtleerer Nachweis zu Bereicherung, zweckgebundenem Zuwendungsanteil und rechtlichem Herausgabegrund.

Minimum aus bereicherungsrechtlichem Zuwendungswert und zur Auflagenvollziehung erforderlichem Zuwendungsanteil.

wert ist exakter EUR-Herausgabebegrenzungswert, negative Anwendbarkeit NULL.

Wertmäßige Begrenzung, keine automatische Umwandlung von Sachherausgabe in Geldzahlung. Keine Bereicherungs-/Auflagenbewertung, Frist- oder Vollstreckungsprüfung erfinden.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2196_T0001, BGB_2196_T0002

```python
from bgbcalc import erbauflage_herausgabebegrenzung
erbauflage_herausgabebegrenzung(
    bereicherungsrechtlicher_zuwendungswert='100',
    zur_auflagenvollziehung_erforderlicher_zuwendungsanteil='30',
    herausgabevoraussetzungen_2196_erfuellt=True,
    bewertungsnachweis='Synthetisch qualifizierte2196-Herausgabe und bewerteter zweckgebundener Anteil.',
)
```

## erbschaftsbesitzer_verwendungsrest

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `ersatzfaehige_verwendungen`: Nichtnegative exakte EUR-Summe rechtlich unter2022I/II fallender Verwendungen einschließlich qualifizierter Lasten-/Schuldentilgungsaufwendungen. Noch vor Abzug des bereits bereicherungsrechtlich gedeckten Teils.
- `bereits_durch_bereicherungsanrechnung_gedeckt`: Nichtnegativer exakter EUR-Teil gerade dieser Verwendungen, der durch Anrechnung auf2021-Bereicherung bereits gedeckt wird, höchstens ersatzfaehige_verwendungen.
- `anspruch_nach_2022_qualifiziert`: Expliziter Wahrheitswert des rechtlich einschlägigen Verwendungsersatzes. Verschärfte Haftung2023–2025 und abweichende/weitergehende Ersatzgrundlagen separat qualifiziert; FALSE ergibt NICHT_ANWENDBAR.
- `bewertungsnachweis`: Nichtleerer Nachweis zu qualifizierten Aufwendungen, bereits gedecktem Anteil und Rechtsgrund.

Ersatzfähige Verwendungen minus gerade durch Anrechnung auf2021-Bereicherung bereits gedeckter Aufwand.

wert ist exakter noch nicht durch Bereicherungsanrechnung gedeckter EUR-Verwendungsrest; negative Anwendbarkeit NULL.

Keine eigenständige Bereicherungsbewertung, keine automatische Durchsetzbarkeit/Zurückbehaltung oder weitergehender Anspruch2022III. Bereits gedeckter Teil darf Aufwand nicht übersteigen.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2022_T0001, BGB_2022_T0003

```python
from bgbcalc import erbschaftsbesitzer_verwendungsrest
erbschaftsbesitzer_verwendungsrest(
    ersatzfaehige_verwendungen='100',
    bereits_durch_bereicherungsanrechnung_gedeckt='30',
    anspruch_nach_2022_qualifiziert=True,
    bewertungsnachweis='Synthetisch2022-qualifizierter Aufwand und nach2021 bereits gedeckter Teil.',
)
```
