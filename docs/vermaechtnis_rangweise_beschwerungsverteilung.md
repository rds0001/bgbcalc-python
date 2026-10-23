<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## vermaechtnis_rangweise_beschwerungsverteilung

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `verfuegbarer_beschwerungsbetrag`: Nach rechtlich einschlägiger2187/2188/2318/2322-Kürzung berechnetes gemeinsames Budget, nicht ungeprüft voller Nachlass.
- `beschwerungen`: Nichtleere Liste eindeutiger beschwerung_id, rang (positive Ganzzahl, kleiner=vorrangig), beschwerungswert und positivem verteilungsgewicht. Rang und Gewichte rechtlich qualifizieren.
- `verteilungsnachweis`: Wirksame2189/2324-Anordnung und innerhalb jedes Rangs geltende proportionale Verteilung mit individuellen Anspruchsobergrenzen belegen; Schutzbeträge und gemeinsame Budgetberechnung vorgelagert.

Gemeinsames Kürzungsbudget rangweise, innerhalb eines Rangs proportional und anspruchsbegrenzt verteilen.

Je Beschwerung Zuteilung und Kürzung; verbleibendes gemeinsames Budget.

Mehrere rechtlich feststehende Beschwerungsränge mit bestehendem begrenztem Quotenkern bedienen. Innerhalb eines Rangs proportional zu qualifizierten Gewichten, höchstens jeweiliger Beschwerungswert, über Obergrenzen hinausgehende Anteile innerhalb desselben Rangs neu verteilen. Restbudget erst danach an nachrangige Ränge. Keine automatische Testamentsauslegung, automatische Gleichrangigkeit oder Erfindung von Quoten. Individuelle2318II/III-Schutzkonkurrenz muss bereits rechtlich in Budget/zulässiger Rangverteilung berücksichtigt sein; dieser Kern entscheidet sie nicht. Kürzungsrecht muss ausgeübt werden, keine automatische Schuldtilgung. Keine mehrfache Verwendung desselben Budgets oder Umdeutung von Sachvermächtnissen in Zahlungsansprüche.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2189_T0001, BGB_2322_T0001, BGB_2324_T0001

```python
from bgbcalc import vermaechtnis_rangweise_beschwerungsverteilung
vermaechtnis_rangweise_beschwerungsverteilung(
    verfuegbarer_beschwerungsbetrag='90',
    beschwerungen=[{'beschwerung_id': 'A', 'rang': 1, 'beschwerungswert': '60', 'verteilungsgewicht': '1'}, {'beschwerung_id': 'B', 'rang': 2, 'beschwerungswert': '40', 'verteilungsgewicht': '1'}, {'beschwerung_id': 'C', 'rang': 2, 'beschwerungswert': '20', 'verteilungsgewicht': '1'}],
    verteilungsnachweis='Mehrere rechtlich feststehende Beschwerungsränge mit bestehendem begrenztem Quotenkern bedienen. Innerhalb eines Rangs proportional zu qualifizierten Gewichten, höchstens jeweiliger Beschwerungswert, über Obergrenzen hinausgehende Anteile innerhalb desselben Rangs neu verteilen. Restbudget erst danach an nachrangige Ränge. Keine automatische Testamentsauslegung, automatische Gleichrangigkeit oder Erfindung von Quoten. Individuelle2318II/III-Schutzkonkurrenz muss bereits rechtlich in Budget/zulässiger Rangverteilung berücksichtigt sein; dieser Kern entscheidet sie nicht. Kürzungsrecht muss ausgeübt werden, keine automatische Schuldtilgung. Keine mehrfache Verwendung desselben Budgets oder Umdeutung von Sachvermächtnissen in Zahlungsansprüche.',
)
```
