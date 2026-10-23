<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## ausstattung_schenkungsmehrbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `ausstattungswert`: Rechtlich bewertete Ausstattung in EUR. Nichtnegative exakte EUR-Zahl.
- `angemessenes_mass`: Nach Umständen insbesondere Elternvermögen qualifiziertes entsprechendes Maß in EUR. Nichtnegative exakte EUR-Zahl.
- `bewertungsnachweis`: Nichtleerer Nachweis der rechtlichen Qualifikation, Bewertung und gegebenenfalls identischen Bezugsperiode.

max(erster Betrag−zweiter Betrag,0)

wert ist exakter nichtnegativer EUR-Bruch.

§1624I: Ausstattung über dem qualifizierten entsprechenden Maß, mindestens null. Ausstattungseigenschaft und Bewertung vorqualifiziert; keine selbst erfundene Vermögensquote.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1624_T0001

```python
from bgbcalc import ausstattung_schenkungsmehrbetrag
ausstattung_schenkungsmehrbetrag(
    ausstattungswert='1000',
    angemessenes_mass='400',
    bewertungsnachweis='Qualifizierte synthetische Beträge derselben Bezugsperiode.',
)
```

## unterhalt_beerdigungskostenrest

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `beerdigungskosten`: Rechtlich zu tragende Beerdigungskosten in EUR. Nichtnegative exakte EUR-Zahl.
- `vom_erben_erlangbar`: Von dem Erben für genau diese Kosten rechtlich und tatsächlich erlangbarer Betrag, nicht bloß bereits gezahlter Betrag. Nichtnegative exakte EUR-Zahl.
- `bewertungsnachweis`: Nichtleerer Nachweis der rechtlichen Qualifikation, Bewertung und gegebenenfalls identischen Bezugsperiode.

max(erster Betrag−zweiter Betrag,0)

wert ist exakter nichtnegativer EUR-Bruch.

§1615II: Kosten abzüglich vom Erben erlangbarem Betrag, mindestens null. Unterhaltspflicht und Umfang der Beerdigungskosten vorqualifiziert; keine automatische Erbenhaftungsprüfung.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1615_T0002

```python
from bgbcalc import unterhalt_beerdigungskostenrest
unterhalt_beerdigungskostenrest(
    beerdigungskosten='1000',
    vom_erben_erlangbar='400',
    bewertungsnachweis='Qualifizierte synthetische Beträge derselben Bezugsperiode.',
)
```

## unterhalt_monatsgesamtbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `monatsbetrag`: Konstanter rechtlich qualifizierter voller Monatsunterhalt als nichtnegative exakte EUR-Zahl; keine automatische Bedarfsbemessung.
- `erster_voller_monat`: ISO-Datum des ersten vollständig geschuldeten Monats, zwingend erster Tag. Teilweiser Erstmonat bleibt außerhalb.
- `beendigung_am`: ISO-Datum des gesetzlich einschlägigen Todes-/Wiederheiratsereignisses. Anspruch und Erhaltung des vollen Endmonats rechtlich vorqualifiziert, nicht vor Anfang.
- `zeitraumnachweis`: Nichtleerer Nachweis der einschlägigen Norm, des zulässigen Beendigungsgrundes, Vollmonatsanspruchs und konstanten Monatsbetrags.

Monatszahl=(Endjahr−Anfangsjahr)×12+Endmonat−Anfangsmonat+1; Gesamtbetrag=Monatszahl×konstanter Monatsbetrag.

wert enthält monatsanzahl als Ganzzahl und gesamtbetrag als EUR-Bruch.

Konstanter qualifizierter voller Monatsbetrag und erster vollständig geschuldeter Monat. Letzter Monat ist rechtlich als voll geschuldeter Monat bestimmt: Tod nach§1361IV/1585I/1612III oder Wiederheirat nach§1585I, gegebenenfalls§1586II. Auch bei Beendigung am ersten oder letzten Tag zählt er voll. Keine tägliche Kürzung dieses Endmonats; kein automatischer voller Anfangsmonat bei erstmaliger Entstehung im Monatslauf. Abweichende Vereinbarungen/Bestimmungen nach§1612II und andere Endgründe nicht abgedeckt. Keine Ermittlung der Unterhaltshöhe, Zahlungsrückstände oder Fälligkeit an Bankarbeitstagen.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1361_T0006, BGB_1361_T0007, BGB_1585_T0002, BGB_1585_T0003, BGB_1612_T0005, BGB_1612_T0006, BGB_1586_T0003

```python
from bgbcalc import unterhalt_monatsgesamtbetrag
unterhalt_monatsgesamtbetrag(
    monatsbetrag='300',
    erster_voller_monat='2030-01-01',
    beendigung_am='2030-03-15',
    zeitraumnachweis='Konstanter qualifizierter Vollmonatsanspruch; Tod im Endmonat, keine abweichende Bestimmung.',
)
```

## unterhalt_unterschiedsbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `voller_unterhalt`: Voller Unterhalt für denselben Zeitraum, nach§1578 rechtlich bewertet. Nichtnegative exakte EUR-Zahl.
- `erwerbsdeckung`: Qualifizierte Erwerbseinkünfte nach§1573II oder nachhaltig gesicherter Teil nachIV2 für denselben Zeitraum. Nichtnegative exakte EUR-Zahl.
- `bewertungsnachweis`: Nichtleerer Nachweis der rechtlichen Qualifikation, Bewertung und gegebenenfalls identischen Bezugsperiode.

max(erster Betrag−zweiter Betrag,0)

wert ist exakter nichtnegativer EUR-Bruch.

Gesetzlicher Unterschiedsbetrag nach§1573II/IV2, mindestens null. Angemessenheit, Nachhaltigkeit, Anschlussunterhalt und Ausschluss konkurrierender Ansprüche vorqualifiziert; keine Bedarfsbemessung, Quotenmethode oder vollständige Unterhaltsprüfung. Numerische Wiederverwendung für1577/1578 mit rechtlich qualifiziertem Bedarf und anrechenbaren Deckungsbeträgen: fachkonzept/unterhalt1577_normanwendung.json. Keine automatische1577II-Freistellung aus tatsächlich ausgebliebenen Zahlungen.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1573_T0002, BGB_1573_T0003, BGB_1573_T0005, BGB_1577_T0001, BGB_1578_T0001, BGB_1578_T0002, BGB_1578_T0003, BGB_1578_T0004

```python
from bgbcalc import unterhalt_unterschiedsbetrag
unterhalt_unterschiedsbetrag(
    voller_unterhalt='1000',
    erwerbsdeckung='400',
    bewertungsnachweis='Qualifizierte synthetische Beträge derselben Bezugsperiode.',
)
```
