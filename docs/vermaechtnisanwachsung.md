<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## vermaechtnis_anwachsungsanteile

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `bedachte`: Liste2..1000 Bedachter desselben Gegenstands. Genau bedachter_id,vermaechtnisanteil (positive exakte Quote≤1),gemeinschaft_id (nichtleere Gruppenkennung oder NULL). Originalanteile summieren sich auf1 am vermachten Gegenstand; Kennungen eindeutig.
- `weggefallener_bedachter_id`: Nichtleere ID eines rechtlich weggefallenen Bedachten aus der Originalliste.
- `anwachsung_testamentarisch_ausgeschlossen`: Pflichtwahrheitswert zum Ausschluss der gesamten untersuchten Anwachsung2158II.
- `vorrangiges_ersatzvermaechtnis`: Pflichtwahrheitswert zu rechtlich vorrangigem Ersatzvermächtnis2190/2099.
- `einordnungsnachweis`: Nichtleerer Nachweis desselben Gegenstands, Wegfalls, Originalquoten und einfacher Gruppenzuordnung. Keine Voraussetzung ausgeschlossener gesetzlicher Erbfolge.

Wegfallquote proportional unter verbleibenden Gruppenmitgliedern, sonst allen übrigen Bedachten verteilen; Ausschluss/Ersatzvorrang beachten; Sonderanteil getrennt.

wert enthält anwachsung_erfolgt, vermaechtnisanteile mit ursprünglichem/angewachsenem/gesamtem Anteil und nicht_angewachsener_wegfallender_anteil.

Ein Wegfall, einfache Gruppe. Kein gesetzlicher Erbfolgeausschluss nötig; vollständige Anteile nur am vermachten Gegenstand. Keine Kaskaden oder Gleichsetzung Tod nach Erwerb mit Wegfall.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2158_T0001, BGB_2158_T0002, BGB_2158_T0003, BGB_2158_T0004, BGB_2159_T0001, BGB_2190_T0001

```python
from bgbcalc import vermaechtnis_anwachsungsanteile
vermaechtnis_anwachsungsanteile(
    bedachte=[{'bedachter_id': 'A', 'vermaechtnisanteil': '0.25', 'gemeinschaft_id': None}, {'bedachter_id': 'B', 'vermaechtnisanteil': '0.25', 'gemeinschaft_id': None}, {'bedachter_id': 'C', 'vermaechtnisanteil': '0.5', 'gemeinschaft_id': None}],
    weggefallener_bedachter_id='A',
    anwachsung_testamentarisch_ausgeschlossen=False,
    vorrangiges_ersatzvermaechtnis=False,
    einordnungsnachweis='Synthetischer Einzelwegfall am selben Gegenstand.',
)
```
