<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## untervermaechtnis_verweigerungsbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `erhaltener_vermaechtniswert`: Nichtnegativer EUR-Wert dessen, was beschwerter Vermächtnisnehmer aus seinem Vermächtnis erhält; konsistente Bewertung, nicht ungeprüft ungekürzten nominalen Anspruch einsetzen.
- `erforderlicher_erfuellungswert`: Nichtnegativer EUR-Wert der Erfüllung der betrachteten Beschwerung durch Untervermächtnis oder Auflage. Bei mehreren Beschwerungen doppelte Verwendung desselben Deckungswerts vermeiden; keine automatische Rang-/Verteilungsentscheidung.
- `beschwerter_vermaechtnisnehmer`: Wahrheitswert des geprüften Tatbestands§2187 Absatz1: Vermächtnisnehmer mit Vermächtnis oder Auflage beschwert. Auch Annahme des eigenen Vermächtnisses schließt dieses Recht nicht aus.
- `bewertungsnachweis`: Nichtleere Begründung des Anspruchsregimes, des tatsächlich Erhaltenen und konsistent bewerteten Erfüllungsaufwands.

Maximum aus null und erforderlichem Erfüllungswert abzüglich erhaltenem Vermächtniswert.

wert ist exakter EUR-Bruch des ungedeckten, verweigerbaren Betrags. Ohne geprüften Tatbestand NICHT_ANWENDBAR/null.

Nur Umfang des Verweigerungsrechts§2187 Absatz1. Keine automatische Ausübung/Tilgung; Fälligkeit§2186, Nachrücken Absatz2 und Verweis auf§1992 Absatz3 gesondert.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2187_T0001, BGB_2187_T0002, BGB_2187_T0003

```python
from bgbcalc import untervermaechtnis_verweigerungsbetrag
untervermaechtnis_verweigerungsbetrag(
    erhaltener_vermaechtniswert='80',
    erforderlicher_erfuellungswert='100',
    beschwerter_vermaechtnisnehmer=True,
    bewertungsnachweis='Synthetisch konsistente EUR-Bewertung desselben Vermächtnisses und seiner Beschwerung.',
)
```

## vermaechtnis_beschwerungskuerzung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `ungekuerzter_vermaechtniswert`: Positiver ursprünglicher EUR-Wert der dem Vermächtnisnehmer gebührenden Leistung vor rechtlich qualifizierter Kürzung; unveränderte Bezugsbasis für Quote.
- `verbleibender_vermaechtniswert`: Nichtnegativer EUR-Wert derselben Leistung nach Kürzung aus gesetzlichem Grund, höchstens ursprünglicher Wert. Keine beliebige Wertschwankung.
- `urspruengliche_beschwerung`: Nichtnegativer ursprünglicher EUR-Wert der dem Vermächtnisnehmer auferlegten Beschwerung vor Anwendung dieser Kürzung. Bereits gekürzten Wert nicht nochmals mit kumulierter Quote kürzen.
- `kuerzungsgrund`: Genau erbenhaftungsbeschraenkung, pflichtteilsanspruch oder untervermaechtnis_2187. Rechtlich wirksame Kürzung aufgrund dieses Grundes belegen; kein frei gewählter Grund.
- `abweichender_erblasserwille`: Wahrheitswert: ein anderer Wille des Erblassers ist anzunehmen; dann NICHT_ANWENDBAR für dieses proportionale Modell.
- `beschwerungsregel_anwendbar`: Wahrheitswert des geprüften Anwendungsbereichs§2188 für Vermächtnisleistung und dem Vermächtnisnehmer auferlegte Beschwerung.
- `bewertungsnachweis`: Nichtleere Begründung von ursprünglicher/verbleibender Leistung, gesetzlichem Kürzungsgrund, Beschwerung und Erblasserwillen auf konsistenter Bewertungsbasis.

Verbleibensquote als verbleibender geteilt durch ungekürzten Vermächtniswert; ursprüngliche Beschwerung damit multiplizieren; Differenz als Kürzungsbetrag.

wert enthält dimensionslose verbleibensquote und EUR-Beträge gekuerzte_beschwerung/kuerzungsbetrag als exakte Brüche. NICHT_ANWENDBAR/null außerhalb Anwendungsbereich.

Abweichender Erblasserwille oder fehlender Anwendungsbereich schließen Modell aus. Keine automatische Ausübung des Kürzungsrechts; kein erneutes Kürzen bereits proportional gekürzter Beschwerung mit Gesamtquote.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2188_T0001

```python
from bgbcalc import vermaechtnis_beschwerungskuerzung
vermaechtnis_beschwerungskuerzung(
    ungekuerzter_vermaechtniswert='100',
    verbleibender_vermaechtniswert='60',
    urspruengliche_beschwerung='50',
    kuerzungsgrund='erbenhaftungsbeschraenkung',
    abweichender_erblasserwille=False,
    beschwerungsregel_anwendbar=True,
    bewertungsnachweis='Synthetisch gesetzlich begründete Kürzung und unveränderte ursprüngliche Bezugsgrößen.',
)
```
