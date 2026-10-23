<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## ruecktritt_aufwendungsersatz

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `notwendige_verwendungen`: Nichtnegative tatsächlich getätigte und rechtlich notwendige Verwendungen auf den zurückzugewährenden Gegenstand in EUR. Notwendigkeit vorab bestimmen; kein beliebiges Investitionsbudget.
- `andere_aufwendungen`: Nichtnegative andere tatsächliche Aufwendungen in EUR, die nicht schon als notwendige Verwendungen erfasst sind. Überschneidungsfrei; keine doppelte Erstattung.
- `bereicherung_durch_andere_aufwendungen`: Nichtnegative rechtlich bewertete Bereicherung des Gläubigers gerade durch die eingegebenen anderen Aufwendungen in EUR. Gleicher Gegenstand und Bewertungsbezug; kein gesamter Gegenstandswert ohne Kausalbezug.
- `gegenstand_zurueckgegeben`: Wahrheitswert einer im Rücktrittsverhältnis erfolgten Rückgabe des Gegenstands, nicht bloß Angebot oder Rückgabeabsicht.
- `wertersatz_geleistet`: Wahrheitswert eines im Rücktrittsverhältnis geleisteten Wertersatzes, nicht bloß Bestehen der Wertersatzpflicht.
- `wertersatzpflicht_nach_346_3_nummer_1_2_ausgeschlossen`: Wahrheitswert des Ausschlusses gerade nach§346 Absatz3 Nummer1 oder2. Allein Nummer3 (eigenübliche Sorgfalt bei gesetzlichem Rücktritt) genügt hier nicht. Voraussetzungen und gegebenenfalls Teilfälle rechtlich abgrenzen.
- `bewertungsnachweis`: Nichtleere Beschreibung des wirksamen Rücktrittsverhältnisses, Rückgabe-/Wertersatzlage, qualifizierten Verwendungen und kausalen Bereicherung. Keine sonstigen Ausschlüsse im abgegrenzten Fall.

Bei Rückgabe ODER geleistetem Wertersatz ODER Ausschluss nach§346 Absatz3 Nummer1/2: notwendige Verwendungen + min(andere Aufwendungen, dadurch verursachte Bereicherung). Sonst NICHT_ANWENDBAR.

wert enthält notwendige_verwendungen_ersatz, andere_aufwendungen_ersatz, gesamtbetrag als exakte EUR-Brüche. Fehlender Ausgangsfall ergibt NICHT_ANWENDBAR mit null.

Nicht mit Wertersatzausschluss nach§346 Absatz3 Nummer3 verwechseln. Kein automatischer Rücktritt, keine automatische Aufrechnung und keine erfundene Bewertungsformel für Notwendigkeit/Bereicherung. Teilgegenstände gesondert zutreffend abgrenzen.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_347_T0003, BGB_347_T0004

```python
from bgbcalc import ruecktritt_aufwendungsersatz
ruecktritt_aufwendungsersatz(
    notwendige_verwendungen='100',
    andere_aufwendungen='500',
    bereicherung_durch_andere_aufwendungen='0',
    gegenstand_zurueckgegeben=False,
    wertersatz_geleistet=False,
    wertersatzpflicht_nach_346_3_nummer_1_2_ausgeschlossen=True,
    bewertungsnachweis='Synthetischer wirksamer Rücktritt und getrennt bewertete Verwendungen/Aufwendungen.',
)
```
