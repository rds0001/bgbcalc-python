<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## gesamtgrundpfandvermaechtnis_nachlassgruppe_mit_fremdhaftung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `gesamtbelastungsbetrag`: Nichtnegativer einheitlich qualifizierter EUR-Befriedigungsbetrag.
- `grundpfandart`: gesamtgrundschuld oder gesamtrentenschuld.
- `grundstuecke`: Vollständige Liste2..1000 ausschließlich mithaftender NACHLASSgrundstücke mit grundstueck_id,grundstueckswert,vorrangige_belastungen; keine Fremdgrundstücke aufnehmen.
- `vermachtes_grundstueck_id`: Eindeutige ID des vermachten Nachlassgrundstücks aus Liste.
- `fremdhaftung_und_erblasserpflicht_qualifiziert`: Pflichtwahrheitswert:2168II-Fremdhaftung mit Erblasserpflicht imErbfall gegenüberFremdeigentümer/Rechtsvorgänger für betrachtetenGesamtbetrag und vollständiger Nachlassvergleichsgruppe rechtlich qualifiziert;FALSE NICHT_ANWENDBAR.
- `zweifelsregel_anwendbar`: Pflichtwahrheitswert ohne abweichendenErblasserwillen.
- `rechts_und_bewertungsnachweis`: Nichtleerer Nachweis der2168II-Pflicht, vollständigenNachlassgruppe und vergleichbarerWerte beiEigentumsübergang.

Je Nachlassgrundstück max(Wert−Rangvorrang,0). Q=Eigenwert/SummeNachlasswerte; Befriedigung=min(Gesamtbetrag×Q,Eigenwert). KeineFremdwerte imNenner. Gesamtdeckung0:Quote/AnteilNULL,Befriedigung0.

Eigenwert,Nachlassgesamtwert,Quote,AnteilvorDeckel,Befriedigungsbetrag exakt.

2168II-Erblasserpflicht ausdrücklichqualifizieren. Keine unterschiedlichenTeilpflichten oder2166II-Drittberichtigung, keineRentenkapitalisierung. Grundstücksliste ausschließlichNachlassgruppe.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2168_T0003, BGB_2166_T0001, BGB_2166_T0002, BGB_2167_T0001, BGB_2167_T0002

```python
from bgbcalc import gesamtgrundpfandvermaechtnis_nachlassgruppe_mit_fremdhaftung
gesamtgrundpfandvermaechtnis_nachlassgruppe_mit_fremdhaftung(
    gesamtbelastungsbetrag='300',
    grundpfandart='gesamtgrundschuld',
    grundstuecke=[{'grundstueck_id': 'A', 'grundstueckswert': '100', 'vorrangige_belastungen': '20'}, {'grundstueck_id': 'B', 'grundstueckswert': '150', 'vorrangige_belastungen': '30'}],
    vermachtes_grundstueck_id='A',
    fremdhaftung_und_erblasserpflicht_qualifiziert=True,
    zweifelsregel_anwendbar=True,
    rechts_und_bewertungsnachweis='A/B vollständigeNachlassgruppe; FremdgrundstückC gehört nichtinWertliste, ErblasserpflichtgegenüberFremdeigentümer fürdenselbenGesamtbetragqualifiziert.',
)
```
