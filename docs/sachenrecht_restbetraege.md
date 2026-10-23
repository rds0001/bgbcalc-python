<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## abtrennung_abwendungsfehlbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `bestandteilswert_nach_abtrennung`: Nichtnegativer rechtlich bewerteter Betrag in EUR, qualifizierte Bedeutung gemäß Abgrenzung.
- `bereits_ersetzter_bestandteilswert`: Nichtnegativer rechtlich bewerteter Vergleichs-/Abzugs-/Zusatzbetrag in EUR für denselben Gegenstand und konsistente Bewertungsbasis.
- `anwendungsfall_qualifiziert`: Explizite Bestätigung des im Fachvertrag abgegrenzten Normfalls. FALSE ergibt NICHT_ANWENDBAR.
- `bewertungsnachweis`: Nichtleere Herkunft und rechtliche Begründung beider Beträge, Bewertungszeitpunkte und Anwendbarkeit.

Wert des Bestandteils nach Abtrennung um bereits ersetzten Wert mindern, mindestens null.

wert ist exakter EUR-Bruch, keine automatische Rundung.

Nur numerischer Fehlbetrag der Wertabwendung nach997Absatz2. Wert ist der rechtlich bewertete Nutzen des abgetrennten Bestandteils gerade für den Besitzer; tatsächlicher Ersatz, kein bloß angebotenes Geld. Weitere Ausschlüsse wegen gewöhnlicher Erhaltung oder fehlendem Nutzen sowie258 bleiben separat; Ergebnis allein entscheidet kein Abtrennungsrecht.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_997_T0003

```python
from bgbcalc import abtrennung_abwendungsfehlbetrag
abtrennung_abwendungsfehlbetrag(
    bestandteilswert_nach_abtrennung='100',
    bereits_ersetzter_bestandteilswert='30',
    anwendungsfall_qualifiziert=True,
    bewertungsnachweis='Synthetische qualifizierte Beträge für denselben Normfall.',
)
```

## fund_herausgabebetrag_nach_kosten

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `herausgabefaehiger_bruttobetrag`: Nichtnegativer rechtlich bewerteter Betrag in EUR, qualifizierte Bedeutung gemäß Abgrenzung.
- `abzugsfaehige_kosten`: Nichtnegativer rechtlich bewerteter Vergleichs-/Abzugs-/Zusatzbetrag in EUR für denselben Gegenstand und konsistente Bewertungsbasis.
- `anwendungsfall_qualifiziert`: Explizite Bestätigung des im Fachvertrag abgegrenzten Normfalls. FALSE ergibt NICHT_ANWENDBAR.
- `bewertungsnachweis`: Nichtleere Herkunft und rechtliche Begründung beider Beträge, Bewertungszeitpunkte und Anwendbarkeit.

Qualifizierten herauszugebenden Fundbetrag um abzugsfähige Kosten mindern, mindestens null.

wert ist exakter EUR-Bruch, keine automatische Rundung.

Nur rechtlich qualifizierter Herausgabebetrag und zugehörige abzugsfähige Kosten nach981Absatz3. Anspruchsperson, Erlöszuordnung und Fristablauf getrennt; übersteigende Kosten ergeben hier keinen negativen Auszahlungsbetrag und keinen neu festgestellten Zahlungsanspruch. Entsprechende981III-Anwendung bei qualifiziertem983-Behördenverwahrfall; keine eigenständige Berechtigungsentscheidung. Siehe fachkonzept/behoerdenfund_normanwendung.json.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_981_T0004, BGB_983_T0001

```python
from bgbcalc import fund_herausgabebetrag_nach_kosten
fund_herausgabebetrag_nach_kosten(
    herausgabefaehiger_bruttobetrag='100',
    abzugsfaehige_kosten='30',
    anwendungsfall_qualifiziert=True,
    bewertungsnachweis='Synthetische qualifizierte Beträge für denselben Normfall.',
)
```
