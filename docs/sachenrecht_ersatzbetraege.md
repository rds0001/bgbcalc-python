<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## besitzhaftung_verantwortungsgrenze

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `schaden_nach_989`: Nichtnegativer rechtlich bewerteter Betrag in EUR, qualifizierte Bedeutung gemäß Abgrenzung.
- `verantwortungsbetrag_gegenueber_mittelbarem_besitzer`: Nichtnegativer rechtlich bewerteter Vergleichs-/Abzugs-/Zusatzbetrag in EUR für denselben Gegenstand und konsistente Bewertungsbasis.
- `anwendungsfall_qualifiziert`: Explizite Bestätigung des im Fachvertrag abgegrenzten Normfalls. FALSE ergibt NICHT_ANWENDBAR.
- `bewertungsnachweis`: Nichtleere Herkunft und rechtliche Begründung beider Beträge, Bewertungszeitpunkte und Anwendbarkeit.

Schadensbetrag nach§989 auf Verantwortungsbetrag gegenüber dem mittelbaren Besitzer begrenzen.

wert ist exakter EUR-Bruch, keine automatische Rundung.

Nur qualifizierter Fall§991 Absatz2 mit bei Besitzerwerb gutgläubigem Besitzer. Beide Beträge betreffen denselben Schaden; keine eigenständige Haftungs-/Verschuldensprüfung.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_991_T0002

```python
from bgbcalc import besitzhaftung_verantwortungsgrenze
besitzhaftung_verantwortungsgrenze(
    schaden_nach_989='100',
    verantwortungsbetrag_gegenueber_mittelbarem_besitzer='30',
    anwendungsfall_qualifiziert=True,
    bewertungsnachweis='Synthetische qualifizierte Beträge für denselben Normfall.',
)
```

## hypothek_ausfall_nach_benachrichtigungsschaden

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `ausfallforderung`: Nichtnegativer rechtlich bewerteter Betrag in EUR, qualifizierte Bedeutung gemäß Abgrenzung.
- `kausaler_benachrichtigungsschaden`: Nichtnegativer rechtlich bewerteter Vergleichs-/Abzugs-/Zusatzbetrag in EUR für denselben Gegenstand und konsistente Bewertungsbasis.
- `anwendungsfall_qualifiziert`: Explizite Bestätigung des im Fachvertrag abgegrenzten Normfalls. FALSE ergibt NICHT_ANWENDBAR.
- `bewertungsnachweis`: Nichtleere Herkunft und rechtliche Begründung beider Beträge, Bewertungszeitpunkte und Anwendbarkeit.

Ausfallforderung um kausalen Schaden aus unterbliebener Benachrichtigung mindern, mindestens null.

wert ist exakter EUR-Bruch, keine automatische Rundung.

Nur nach1166 qualifiziertes Verweigerungsrecht, insbesondere Ersatzberechtigung, vom Gläubiger betriebene Versteigerung und nicht untunliche Benachrichtigung. Ergebnis ist verbleibender nicht durch diesen Schaden abgedeckter Ausfall, kein Erlöschen oder automatische Rechtsausübung.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1166_T0001, BGB_1166_T0002

```python
from bgbcalc import hypothek_ausfall_nach_benachrichtigungsschaden
hypothek_ausfall_nach_benachrichtigungsschaden(
    ausfallforderung='100',
    kausaler_benachrichtigungsschaden='30',
    anwendungsfall_qualifiziert=True,
    bewertungsnachweis='Synthetische qualifizierte Beträge für denselben Normfall.',
)
```

## hypothek_schuldbefreiung_nach_regressverlust

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `persoenliche_restschuld`: Nichtnegativer rechtlich bewerteter Betrag in EUR, qualifizierte Bedeutung gemäß Abgrenzung.
- `verlorener_hypothekarischer_regress`: Nichtnegativer rechtlich bewerteter Vergleichs-/Abzugs-/Zusatzbetrag in EUR für denselben Gegenstand und konsistente Bewertungsbasis.
- `anwendungsfall_qualifiziert`: Explizite Bestätigung des im Fachvertrag abgegrenzten Normfalls. FALSE ergibt NICHT_ANWENDBAR.
- `bewertungsnachweis`: Nichtleere Herkunft und rechtliche Begründung beider Beträge, Bewertungszeitpunkte und Anwendbarkeit.

Persönliche Restschuld bis zur Höhe des kausal verlorenen hypothekarischen Ersatzes freistellen.

wert ist exakter EUR-Bruch, keine automatische Rundung.

Qualifizierter Verzicht, Aufhebung oder Vorrangeinräumung durch Gläubiger. Verlorener Regress ist rechtlich bewerteter ohne Verfügung erzielbarer1164-Ersatz, nicht pauschaler Grundstücks- oder Hypothekennennwert.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1165_T0001

```python
from bgbcalc import hypothek_schuldbefreiung_nach_regressverlust
hypothek_schuldbefreiung_nach_regressverlust(
    persoenliche_restschuld='100',
    verlorener_hypothekarischer_regress='30',
    anwendungsfall_qualifiziert=True,
    bewertungsnachweis='Synthetische qualifizierte Beträge für denselben Normfall.',
)
```

## hypothek_schuldneruebergangsbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `hypothekarisch_gesicherte_befriedigung`: Nichtnegativer rechtlich bewerteter Betrag in EUR, qualifizierte Bedeutung gemäß Abgrenzung.
- `ersatzanspruch_gegen_eigentuemer`: Nichtnegativer rechtlich bewerteter Vergleichs-/Abzugs-/Zusatzbetrag in EUR für denselben Gegenstand und konsistente Bewertungsbasis.
- `anwendungsfall_qualifiziert`: Explizite Bestätigung des im Fachvertrag abgegrenzten Normfalls. FALSE ergibt NICHT_ANWENDBAR.
- `bewertungsnachweis`: Nichtleere Herkunft und rechtliche Begründung beider Beträge, Bewertungszeitpunkte und Anwendbarkeit.

Gesicherten Befriedigungsbetrag auf rechtlich bestehenden Ersatzanspruch begrenzen.

wert ist exakter EUR-Bruch, keine automatische Rundung.

Nur Umfang des Übergangs nach1164, nicht dingliche Rangverteilung. Befriedigung bezeichnet tatsächlich getilgten hypothekarisch gesicherten Betrag, keine ungesicherten Nebenforderungen. Vereinigung von Forderung und Schuld ist als entsprechender qualifizierter Betrag verwendbar. Konkurrierende Eigentümerhypothek darf nicht zum Nachteil des Schuldners geltend gemacht werden; kein Verteilungsplan.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1164_T0001, BGB_1164_T0002, BGB_1164_T0003

```python
from bgbcalc import hypothek_schuldneruebergangsbetrag
hypothek_schuldneruebergangsbetrag(
    hypothekarisch_gesicherte_befriedigung='100',
    ersatzanspruch_gegen_eigentuemer='30',
    anwendungsfall_qualifiziert=True,
    bewertungsnachweis='Synthetische qualifizierte Beträge für denselben Normfall.',
)
```

## niessbrauch_einloesungskapital

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `tilgungskapital`: Nichtnegativer rechtlich bewerteter Betrag in EUR, qualifizierte Bedeutung gemäß Abgrenzung.
- `einloesungspraemie`: Nichtnegativer rechtlich bewerteter Vergleichs-/Abzugs-/Zusatzbetrag in EUR für denselben Gegenstand und konsistente Bewertungsbasis.
- `anwendungsfall_qualifiziert`: Explizite Bestätigung des im Fachvertrag abgegrenzten Normfalls. FALSE ergibt NICHT_ANWENDBAR.
- `bewertungsnachweis`: Nichtleere Herkunft und rechtliche Begründung beider Beträge, Bewertungszeitpunkte und Anwendbarkeit.

Tilgungskapital und Einlösungsprämie zu Kapitalbetrag addieren.

wert ist exakter EUR-Bruch, keine automatische Rundung.

Nur Einlösung des vom Nießbrauch betroffenen Papiers. Einlösungsprämie wird als Kapital, nicht Zinsertrag behandelt; separat fällige Zinsen nicht als Prämie eingeben. Keine Bewertung oder automatische Auszahlung an den Nießbraucher.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1083_T0002, BGB_1083_T0003

```python
from bgbcalc import niessbrauch_einloesungskapital
niessbrauch_einloesungskapital(
    tilgungskapital='100',
    einloesungspraemie='30',
    anwendungsfall_qualifiziert=True,
    bewertungsnachweis='Synthetische qualifizierte Beträge für denselben Normfall.',
)
```

## niessbrauch_uebermassfruechte_ersatz

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `wert_der_uebermassfruechte`: Nichtnegativer rechtlich bewerteter Betrag in EUR, qualifizierte Bedeutung gemäß Abgrenzung.
- `wert_der_beeintraechtigten_eigenen_nutzungen`: Nichtnegativer rechtlich bewerteter Vergleichs-/Abzugs-/Zusatzbetrag in EUR für denselben Gegenstand und konsistente Bewertungsbasis.
- `anwendungsfall_qualifiziert`: Explizite Bestätigung des im Fachvertrag abgegrenzten Normfalls. FALSE ergibt NICHT_ANWENDBAR.
- `bewertungsnachweis`: Nichtleere Herkunft und rechtliche Begründung beider Beträge, Bewertungszeitpunkte und Anwendbarkeit.

Fruchtwert um Beeinträchtigung der dem Nießbraucher gebührenden Nutzungen mindern, mindestens null.

wert ist exakter EUR-Bruch, keine automatische Rundung.

Nur wenn Verwendung zur Wiederherstellung nicht verlangt wird. Eingaben rechtlich bewertete, kausal zusammengehörige Werte. Eigenständige Verschuldenshaftung, Sicherheitsleistung und Wiederherstellungsalternative nicht eingerechnet.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1039_T0002, BGB_1039_T0003, BGB_1039_T0004

```python
from bgbcalc import niessbrauch_uebermassfruechte_ersatz
niessbrauch_uebermassfruechte_ersatz(
    wert_der_uebermassfruechte='100',
    wert_der_beeintraechtigten_eigenen_nutzungen='30',
    anwendungsfall_qualifiziert=True,
    bewertungsnachweis='Synthetische qualifizierte Beträge für denselben Normfall.',
)
```

## pfandrecht_einziehungsgrenze

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `einziehbare_geldforderung`: Nichtnegativer rechtlich bewerteter Betrag in EUR, qualifizierte Bedeutung gemäß Abgrenzung.
- `erforderlicher_befriedigungsbetrag`: Nichtnegativer rechtlich bewerteter Vergleichs-/Abzugs-/Zusatzbetrag in EUR für denselben Gegenstand und konsistente Bewertungsbasis.
- `anwendungsfall_qualifiziert`: Explizite Bestätigung des im Fachvertrag abgegrenzten Normfalls. FALSE ergibt NICHT_ANWENDBAR.
- `bewertungsnachweis`: Nichtleere Herkunft und rechtliche Begründung beider Beträge, Bewertungszeitpunkte und Anwendbarkeit.

Einziehbare Geldforderung auf erforderlichen Befriedigungsbetrag begrenzen.

wert ist exakter EUR-Bruch, keine automatische Rundung.

Einziehungsberechtigung gemäß1228Absatz2/1282 und Umfang der gepfändeten Geldforderung vorqualifiziert. Erforderlicher Befriedigungsbetrag enthält ausschließlich gedeckte Ansprüche; keine eigenständige Feststellung der Fälligkeit oder Ermächtigung zu anderen Verfügungen.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1282_T0001, BGB_1282_T0002, BGB_1282_T0003

```python
from bgbcalc import pfandrecht_einziehungsgrenze
pfandrecht_einziehungsgrenze(
    einziehbare_geldforderung='100',
    erforderlicher_befriedigungsbetrag='30',
    anwendungsfall_qualifiziert=True,
    bewertungsnachweis='Synthetische qualifizierte Beträge für denselben Normfall.',
)
```
