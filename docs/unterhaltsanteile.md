<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## unterhalt_anteilsbetraege

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `verteilbarer_barunterhalt`: Nichtnegativer qualifizierter Barunterhaltsbetrag in EUR für identischen Zeitraum; Anspruch/Bereinigung bereits bestimmt.
- `unterhaltspflichtige`: Vollständige Liste1..1000 qualifizierter gleich naher Barunterhaltspflichtiger, je genau person_id und verteilungsgewicht. ID nichtleer/eindeutig, Gewicht positive exakte Zahl auf einheitlicher rechtlich qualifizierter Erwerbs-/Vermögensbasis; nicht ungeprüft Bruttoeinkommen. Persönliche Leistungsfähigkeitsgrenzen dürfen bei Grundverteilung nicht eingreifen.
- `verteilungsnachweis`: Nichtleerer Nachweis zu Rang, Personenkreis, Zeitraum, bewerteten Gewichten und nicht eingreifenden individuellen Grenzen. Keine freie Methodenwahl.

Quote=Gewicht/Summe aller Gewichte, Unterhaltsbetrag=verteilbarer Barunterhalt×Quote.

wert ist Liste in Eingabereihenfolge mit person_id, anteilsquote als dimensionslosem Bruch und unterhaltsbetrag als EUR-Bruch.

Grundverteilung nach§1606III1 für denselben Zeitraum und denselben qualifizierten Barunterhaltsbedarf. Kreis der tatsächlich gleich nahen barunterhaltspflichtigen Verwandten sowie Rang, Erwerbs-/Vermögensbewertung und Verteilungsgewichte rechtlich vorqualifiziert. Gewichte sind keine ungeprüften Bruttoeinkommen und nicht notwendig normierte Quoten. Keine Ermittlung von Selbstbehalt, gesteigerter Haftung, Bedarfsrang, Wechselmodell oder Naturalunterhalt nachSatz2. Nur wenn individuelle Leistungsfähigkeitsgrenzen bei den errechneten Anteilen nicht eingreifen; Mangelfall-/Deckelungsumverteilung gesondert. Nichtpflichtige oder mit Gewicht null ausgeschiedene Personen außerhalb dieses qualifizierten Kreises behandeln.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1606_T0003

```python
from bgbcalc import unterhalt_anteilsbetraege
unterhalt_anteilsbetraege(
    verteilbarer_barunterhalt='900',
    unterhaltspflichtige=[{'person_id': 'A', 'verteilungsgewicht': {'zaehler': '2', 'nenner': '1'}}, {'person_id': 'B', 'verteilungsgewicht': {'zaehler': '1', 'nenner': '1'}}],
    verteilungsnachweis='Gleich nahe und barpflichtig; bewertete Gewichte2:1, keine eingreifenden Individualgrenzen.',
)
```
