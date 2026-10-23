<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## pflichtteil_deckung_beschwerungskuerzung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `erwerbswert_vor_beschwerung`: Nichtnegativer EUR-Erwerbswert vor gerade dieser Beschwerung, aus rechtlich qualifiziert ausgeschlagener Erbschaft/Vermächtnis.
- `beschwerungswert`: Nichtnegative EUR-Beschwerung höchstens Erwerbswert; bei Überschreitung vorgelagerte Kürzungsregeln zuerst klären.
- `zu_deckende_pflichtteilslast`: Nichtnegative rechtlich zugeordnete EUR-Pflichtteilslast, keine ungekürzte Fremdlast.
- `kuerzung_nach_2322_qualifiziert`: Pflichtwahrheitswert zum durch Ausschlagung begünstigten beschwerten Erwerb2322; FALSE NICHT_ANWENDBAR.
- `bewertungsnachweis`: Nichtleerer Nachweis des Erwerbs, der Beschwerung und Lastzuordnung.

Freier Rest=Erwerb−Beschwerung; Kürzung=min(Beschwerung,max(Pflichtteilslast−freierRest,0)); Restbeschwerung und noch ungedeckte Last getrennt.

wert enthält kuerzungsbetrag, verbleibende_beschwerung und nicht_gedeckte_pflichtteilslast als exakte EUR-Brüche.

Keine vorgelagerte Überschuldungs-/Haftungskürzung, kein interner Gleichrangverteiler oder Missachtung2189.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2322_T0001

```python
from bgbcalc import pflichtteil_deckung_beschwerungskuerzung
pflichtteil_deckung_beschwerungskuerzung(
    erwerbswert_vor_beschwerung='100',
    beschwerungswert='80',
    zu_deckende_pflichtteilslast='50',
    kuerzung_nach_2322_qualifiziert=True,
    bewertungsnachweis='Synthetisch qualifizierter beschwerter Erwerb.',
)
```

## pflichtteil_miterbe_eigenbedarf

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `erbteilwert_nach_teilung`: Nichtnegativer exakter EUR-Erbteilwert nach Teilung, vor gerade dieser Pflichtteilslast. Keine bereits erfüllte Last doppelt abziehen.
- `eigener_pflichtteilswert`: Nichtnegativer rechtlich bestimmter eigener EUR-Pflichtteilswert.
- `verlangter_pflichtteilsbetrag`: Nichtnegative rechtlich bestimmte noch offene Forderung eines anderen Pflichtteilsberechtigten gegen diesen Miterben.
- `schutz_nach_2319_qualifiziert`: Pflichtwahrheitswert zum pflichtteilsberechtigten Miterben nach Teilung und einschlägigen2319-Schutz; FALSE NICHT_ANWENDBAR.
- `bewertungsnachweis`: Nichtleerer Nachweis der Werte und Schutzvoraussetzungen.

Forderungsdeckung=min(verlangt,max(Erbteil−eigenerPflichtteil,0)); Ausfall=verlangt−Deckung.

wert enthält befriedigungsbetrag und ausfall_fuer_uebrige_erben als exakte EUR-Brüche.

Kein automatischer interner Haftungsanteil der übrigen Erben und kein Schutz gegen andere Schulden.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2319_T0001, BGB_2319_T0002

```python
from bgbcalc import pflichtteil_miterbe_eigenbedarf
pflichtteil_miterbe_eigenbedarf(
    erbteilwert_nach_teilung='100',
    eigener_pflichtteilswert='60',
    verlangter_pflichtteilsbetrag='70',
    schutz_nach_2319_qualifiziert=True,
    bewertungsnachweis='Synthetisch qualifizierter Schutz nach Teilung.',
)
```

## pflichtteil_vorteilslast

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `fallart`: ersatzerwerb_2320 oder vermaechtnisausschlagung_2321, jeweils rechtlich qualifiziert.
- `pflichtteilslast`: Nichtnegative exakte EUR-Pflichtteilslast, bei angenommenem Vermächtnis Anrechnung2307 bereits berücksichtigt.
- `angenommenes_vermaechtnis`: Nichtnegativer EUR-Wert eines angenommenen Vermächtnisses2320; überschneidungsfrei zur Pflichtteilslast. Bei2321 null.
- `erlangter_vorteil`: Nichtnegativer rechtlich bewerteter EUR-Vorteil gerade aus Ersatzerwerb/Ausschlagung, nicht automatisch gesamter Erbteil.
- `lastzuordnung_qualifiziert`: Pflichtwahrheitswert der Sonderzuordnung2320/2321 einschließlich abweichender Verfügung2324; FALSE NICHT_ANWENDBAR.
- `bewertungsnachweis`: Nichtleerer Nachweis von Vorteil und überschneidungsfreien Lastkomponenten.

Pflichtteilslast plus angenommenes Vermächtnis addieren; zugeordnete Sonderlast=min(Gesamtlast,Vorteil); Rest getrennt.

wert enthält zugeordnete_sonderlast und nicht_durch_vorteil_zugeordnete_restlast als exakte EUR-Brüche.

Keine Doppelanrechnung2307 und keine automatische Quote für mehrere Begünstigte oder übrige Erben.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2320_T0001, BGB_2320_T0002, BGB_2321_T0001

```python
from bgbcalc import pflichtteil_vorteilslast
pflichtteil_vorteilslast(
    fallart='ersatzerwerb_2320',
    pflichtteilslast='60',
    angenommenes_vermaechtnis='20',
    erlangter_vorteil='50',
    lastzuordnung_qualifiziert=True,
    bewertungsnachweis='Synthetischer Vorteil und getrennte Lasten.',
)
```
