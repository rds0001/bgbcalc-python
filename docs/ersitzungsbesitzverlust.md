<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## ersitzung_besitzverlust_nichtunterbrechung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `eigenbesitzverlust_am`: ISO-Datum des qualifizierten Verlusts des Eigenbesitzes, nicht bloße Störung oder vorübergehendes tatsächliches Hindernis ohne Besitzverlust.
- `prueftag`: ISO-Datum ab Eigenbesitzverlust; tatsächliche Wiedererlangung und Klageerhebung dürfen nicht danach liegen.
- `massgebliches_jahresfristende`: ISO-Datum des rechtlich maßgeblichen Jahresfristendes, mindestens kalendarisches Ereignisfristende. Ohne gesondert begründete gesetzliche Korrektur genau dieses Ende eingeben. Keine automatische Feiertagsverlängerung.
- `wiedererlangung_am`: Optionales ISO-Datum tatsächlicher Wiedererlangung gerade des Eigenbesitzes zwischen Verlust und Prüftag. NULL bedeutet noch nicht eingetreten, nicht unbekannt.
- `klageerhebung_am`: Optionales rechtlich maßgebliches ISO-Datum wirksamer Klageerhebung zwischen Verlust und Prüftag. Nicht unbesehen Versand oder Eingang einsetzen; prozessuale Wirkungen gesondert beurteilen. NULL bedeutet noch nicht eingetreten.
- `eigenbesitz_ohne_willen_verloren`: Expliziter Wahrheitswert des unfreiwilligen Verlusts; freiwilliger Verlust erfüllt Absatz2 auch bei rascher Wiedererlangung nicht.
- `wiedererlangung_mittels_klage`: Expliziter Wahrheitswert, dass die tatsächliche Wiedererlangung mittels der eingegebenen Klage erfolgt ist. TRUE erfordert beide Ereignisse mit Klage spätestens bei Wiedererlangung; rechtzeitige Klage ohne Wiedererlangung genügt nicht.
- `einordnungsnachweis`: Nichtleere rechtliche Begründung von Eigenbesitz, Unfreiwilligkeit, Wiedererlangung, wirksamer Klage und maßgeblichem Jahresfristende; untertägige Ereignisreihenfolge bei gleichen Daten bestätigen.

Jahresfrist ab Eigenbesitzverlust als Ereignisfrist. Unfreiwilliger Verlust und entweder tatsächliche Wiedererlangung spätestens am maßgeblichen Fristende oder Wiedererlangung mittels spätestens dann erhobener Klage. Spätere Wiedererlangung auf rechtzeitige Klage möglich.

wert enthält kalendarisches_jahresfristende, massgebliches_jahresfristende, wiedererlangung_binnen_jahresfrist, wiedererlangung_durch_rechtzeitige_klage, unterbrechung_gilt_als_nicht_erfolgt. Letzter Wert ist auf§940 Absatz2 und den aktuellen Ereignisstand begrenzt.

Keine automatische Eigentumsbehauptung. Nur Ausnahme zur Besitzverlustunterbrechung§940; Hemmung§939, Vollstreckungsunterbrechung§941 und Folgen§942 sowie Voraussetzungen§937 separat. Fehlende bisherige Wiedererlangung kann künftig noch eintreten; FALSE ist keine abschließende Prognose.

ISO-Daten und berechnete Grenzen0001..9999, explizite Wahrheitswerte und nichtleerer Nachweis.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_940_T0001, BGB_940_T0002

```python
from bgbcalc import ersitzung_besitzverlust_nichtunterbrechung
ersitzung_besitzverlust_nichtunterbrechung(
    eigenbesitzverlust_am='2028-02-29',
    prueftag='2030-03-01',
    massgebliches_jahresfristende='2029-02-28',
    wiedererlangung_am='2029-02-28',
    klageerhebung_am='2028-03-01',
    eigenbesitz_ohne_willen_verloren=False,
    wiedererlangung_mittels_klage=False,
    einordnungsnachweis='Synthetisch qualifizierter unfreiwilliger Eigenbesitzverlust und tatsächliche Wiedererlangung.',
)
```
