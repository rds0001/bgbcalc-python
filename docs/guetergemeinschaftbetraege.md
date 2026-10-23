<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## guetergemeinschaft_einbringungsrueckerstattung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `verfuegbares_gesamtgut`: Nichtnegativer für Einbringungsrückerstattung verfügbarer Gesamtgutswert in EUR nach qualifizierter vorrangiger Berichtigung/Rückbehalten.
- `einbringungswert_ehegatte`: Nichtnegativer qualifizierter Einbringungswert des ersten Ehegatten, zum Zeitpunkt der Einbringung bewertet, EUR.
- `einbringungswert_anderer`: Entsprechender qualifizierter Einbringungswert des anderen Ehegatten, EUR.
- `bewertungsnachweis`: Nichtleerer Nachweis zu Anwendbarkeit§1478, Verlangen, verfügbarem Wert und qualifizierten Einbringungswerten.

Erstattungsmasse=min(verfügbares Gesamtgut,Summe Einbringungswerte); Erstattung proportional Einbringungswerten, Fehlbeträge als Differenz; überschüssiges Gesamtgut gesondert. Bei Summe0 Erstattung0.

wert enthält rueckerstattung_ehegatte, rueckerstattung_anderer, fehlbetrag_ehegatte, fehlbetrag_anderer und verbleibendes_gesamtgut als EUR-Brüche.

Scheidung vor Abschluss der Auseinandersetzung und erforderliches Verlangen nach§1478I sind vorausgesetzt. Einbringungswerte nachAbsatz2 qualifiziert und nachAbsatz3 zum Zeitpunkt der jeweiligen Einbringung bewertet. Verfügbares Gesamtgut bereits nach vorrangiger Verbindlichkeitenberichtigung und erforderlichen Rückbehalten bestimmt. Ersatzforderungen/Anrechnung nach§1476II und anschließende Überschussverteilung sind gesonderte Berechnungen. Keine Bewertung von Gegenständen oder automatische Güterstandsprüfung. Bei beiden Einbringungswerten null keine Rückerstattung und keine Division durch null.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1478_T0001, BGB_1478_T0006

```python
from bgbcalc import guetergemeinschaft_einbringungsrueckerstattung
guetergemeinschaft_einbringungsrueckerstattung(
    verfuegbares_gesamtgut='120',
    einbringungswert_ehegatte='100',
    einbringungswert_anderer='200',
    bewertungsnachweis='Scheidung und Verlangen gegeben; prioritäre Berichtigung abgeschlossen, Einbringungszeitwerte belegt.',
)
```

## guetergemeinschaft_freistellungsbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `verbindlichkeit`: Nichtnegativer Betrag eines konsistent abgegrenzten noch unberichtigten Schuldpostens einschließlich zugeordneter Nebenforderungen in EUR.
- `inanspruchnahme`: Nichtnegative vom Gläubiger geltend gemachte Belastung des geschützten Ehegatten für denselben Posten, höchstens Verbindlichkeit, EUR.
- `verwaltungsfall`: Rechtlich qualifizierte Zuordnung: alleinverwaltung_anderer fürAbsatz1, gemeinschaftlich fürAbsatz2, alleinlast_anderer fürAbsatz3. Keine freie Rechtswahl.
- `aus_gesamtgut_erlangt`: Nichtnegativer aus Gesamtgut erlangter Betrag des geschützten Ehegatten in EUR. Zusätzliche Grenze nur beiAbsatz1; auch in anderen Fällen numerisch validiert.
- `zuordnungsnachweis`: Nichtleerer Nachweis zu Gesamtgutsteilung vor Berichtigung, interner Lastzuordnung und Verwaltungssituation.

Grenze=Schuld/2 bei gemeinschaftlicher Verwaltung; bei Alleinverwaltung des anderen min(Schuld/2,Erlangtes); bei Alleinlast des anderen0. Freistellung=max(Inanspruchnahme−Grenze,0).

wert enthält interne_belastungsgrenze und freistellungsbetrag als EUR-Brüche.

Ein einzelner noch unberichtigter, vor Berichtigung geteiltem Gesamtgut zugeordneter Schuldposten. Beträge einschließlich rechtlich zugeordneter Nebenforderungen konsistent abgrenzen. alleinverwaltung_anderer bezeichnet den Schutz des nicht allein verwaltenden Ehegatten nachAbsatz1; gemeinschaftlich Absatz2. alleinlast_anderer bezeichnet ausschließlich interne Alleinlast des anderen Ehegatten nachAbsatz3 und geht Verwaltungssituation vor. Qualifizierte Zuordnung ist keine freie Wahl. Erlangtes wird nur inAbsatz1 als zusätzliche Grenze verwendet; inAbsätzen2/3 nicht automatisch anrechnen. Keine Änderung der Außenhaftung gegenüber Gläubigern und keine Mehrschuld-/Gesamthaftungsverrechnung.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1481_T0001, BGB_1481_T0002, BGB_1481_T0003

```python
from bgbcalc import guetergemeinschaft_freistellungsbetrag
guetergemeinschaft_freistellungsbetrag(
    verbindlichkeit='100',
    inanspruchnahme='80',
    verwaltungsfall='gemeinschaftlich',
    aus_gesamtgut_erlangt='20',
    zuordnungsnachweis='Einzelposten und geschützter Ehegatte qualifiziert, Teilung vor Berichtigung.',
)
```
