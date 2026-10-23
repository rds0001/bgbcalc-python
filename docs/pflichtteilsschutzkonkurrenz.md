<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## vermaechtniskuerzung_bei_qualifiziertem_erbenvorrang

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `erwerbswert_vor_vermaechtnis`: Nichtnegativer Erwerbswert nach sonstigen Verbindlichkeiten vor Vermächtnis/Pflichtteilslast.
- `vermaechtniswert`: Nichtnegativer Wert höchstens Erwerb.
- `gesamte_pflichtteilslast`: Nichtnegative Last höchstens Erwerb.
- `anderweitig_getragene_last_2323`: Rechtlich anderweitig getragene Last0..gesamteLast.
- `pflichtteilswert_erbe`: Nichtnegativer rechtlich bestimmter eigener Pflichtteil; Schutz bleibt auf vorbestehenden Erwerbsrest begrenzt.
- `pflichtteilswert_vermaechtnisnehmer`: Nichtnegativer rechtlich bestimmter Schutzwert des Bedachten.
- `erbenvorrang_und_einzelfall_qualifiziert`: Pflichtwahrheitswert: konkrete Anwendung der Erbenvorrangvariante in2318II/III-Konkurrenz fachlich begründet, einErbe/einVermächtnis; FALSE NICHT_ANWENDBAR.
- `rechts_und_bewertungsnachweis`: Nichtleere dokumentierte rechtliche Zuordnung gerade zur Erbenvorrangvariante einschließlich Begründung/Quelle und vergleichbarer Bewertungen. Keine beliebige Methodenwahl.

L=Gesamtlast−2323Last;K_B=min(L×V/N,max(V−P_B,0)); geschützterEigenwert=min(P_E,N−V);Bedarf=min(V,max(geschützterEigenwert−(N−V−L),0));K=max(K_B,Bedarf).

Grundkürzung,vorbestehenderErbenschutz,Bedachtenschutzkürzung,Erbenbedarf,Kürzung und verbleibende Werte als EUR-Brüche.

Explizite extern rechtlich begründete Erbenvorrangvariante, keine universell gelöste2318Konkurrenz. Vorbeeinträchtigung durchVermächtnis nicht reparieren. KeinMehrvermächtnisfall oder freie Methodenwahl.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2318_T0001, BGB_2318_T0003, BGB_2318_T0004, BGB_2323_T0001

```python
from bgbcalc import vermaechtniskuerzung_bei_qualifiziertem_erbenvorrang
vermaechtniskuerzung_bei_qualifiziertem_erbenvorrang(
    erwerbswert_vor_vermaechtnis='100',
    vermaechtniswert='60',
    gesamte_pflichtteilslast='30',
    anderweitig_getragene_last_2323='0',
    pflichtteilswert_erbe='25',
    pflichtteilswert_vermaechtnisnehmer='30',
    erbenvorrang_und_einzelfall_qualifiziert=True,
    rechts_und_bewertungsnachweis='Synthetisch fachlich begründete Erbenvorrangvariante2318; rechtliche Zuordnung und Werte qualifiziert.',
)
```
