<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## erbteil_individuelle_schuldendeckung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `zugeteilter_erbteilwert`: Nichtnegativer rechtlich bestimmter EUR-Teilungsanteil nach gemeinsamer Lastbereinigung und ggf.Ausgleichung.
- `individuell_zugeordnete_nachlassschuld`: Nichtnegative EUR-Nachlassschuld, die nur diesem Erben zugeordnet ist. Nicht nochmals in gemeinsamen Schulden abziehen.
- `last_nach_2046_abs2_qualifiziert`: Pflichtwahrheitswert zu individuell qualifizierter Last2046II; bei mehreren belasteten Erben deren individuelle Last vorher bestimmen. FALSE NICHT_ANWENDBAR.
- `bewertungsnachweis`: Nichtleerer Nachweis des Teilungsanteils und der individuellen Last.

Berichtigung=min(Teilungsanteil,individuelleSchuld); verbleibender Anteil und ungedeckte Schuld als Differenzen.

wert enthält berichtigung_aus_eigenem_anteil, verbleibender_erbteilwert und nicht_aus_anteil_berichtigter_schuldteil als exakte EUR-Brüche.

Ungedeckte Schuld erlischt nicht; keine Umlage auf unbelastete Erben oder erfundene Gleichquote mehrerer belasteter Erben.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2046_T0003

```python
from bgbcalc import erbteil_individuelle_schuldendeckung
erbteil_individuelle_schuldendeckung(
    zugeteilter_erbteilwert='40',
    individuell_zugeordnete_nachlassschuld='60',
    last_nach_2046_abs2_qualifiziert=True,
    bewertungsnachweis='Synthetisch individuelle Nachlasslast.',
)
```

## nachlass_zulaenglichkeitsbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `nachlassaktiva`: Nichtnegative exakte EUR-Summe rechtlich bewerteter Nachlassaktiva.
- `gesamte_nachlassverbindlichkeiten`: Nichtnegative exakte Gesamtschuldensumme einschließlich separat genannter Vermächtnis-/Auflagenlasten.
- `enthaltene_vermaechtnisverbindlichkeiten`: Nichtnegative darin enthaltene Vermächtnisschulden, überschneidungsfrei zu Auflagen.
- `enthaltene_auflagenverbindlichkeiten`: Nichtnegative darin enthaltene Auflagenlasten; Summe beider Ausnahmen höchstens Gesamtschulden.
- `bewertungsnachweis`: Nichtleerer Nachweis der rechtlichen Bewertung und Abgrenzung. Keine automatische Insolvenzfeststellung.

Vermächtnis-/Auflagenschulden aus Gesamtschulden abziehen; Aktiva minus bereinigte Schulden.

wert enthält beruecksichtigte_verbindlichkeiten und vorzeichenbehaftete zulaenglichkeitsdifferenz als exakte EUR-Brüche.

Nur numerische Bereinigung, keine Feststellung von Zahlungsunfähigkeit/Überschuldung/Antragspflicht.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1980_T0003

```python
from bgbcalc import nachlass_zulaenglichkeitsbetrag
nachlass_zulaenglichkeitsbetrag(
    nachlassaktiva='100',
    gesamte_nachlassverbindlichkeiten='120',
    enthaltene_vermaechtnisverbindlichkeiten='30',
    enthaltene_auflagenverbindlichkeiten='10',
    bewertungsnachweis='Synthetisch qualifizierte Aktiva/Schulden.',
)
```

## vertragsvermaechtnis_subsidiaerer_fehlbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `geschuldeter_ersatzwert`: Nichtnegativer rechtlich bewerteter gesamter EUR-Ersatzwert2288II.
- `vom_erben_erlangbarer_ersatz`: Nichtnegativer rechtlich beim Erben erlangbarer Ersatzanteil, höchstens Gesamtwert; nicht bloß bislang gezahlte Summe.
- `subsidiaerfall_nach_2288_qualifiziert`: Pflichtwahrheitswert zu beeinträchtigender schenkweiser Veräußerung/Belastung eines vertragsmäßig vermachten Gegenstands2288II2; FALSE NICHT_ANWENDBAR.
- `bewertungsnachweis`: Nichtleerer Nachweis der Ersatzbewertung und rechtlichen Erlangbarkeit beim Erben.

Geschuldeten Ersatzwert minus vom Erben erlangbaren Ersatzanteil.

wert ist subsidiärer Fehlbetrag als exakter EUR-Bruch.

Nur subsidiäre Ausgangsgröße vor weiteren2287-Bereicherungsgrenzen, kein automatischer endgültiger Zahlungsanspruch; kein2329-Rangmodell.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2288_T0003

```python
from bgbcalc import vertragsvermaechtnis_subsidiaerer_fehlbetrag
vertragsvermaechtnis_subsidiaerer_fehlbetrag(
    geschuldeter_ersatzwert='100',
    vom_erben_erlangbarer_ersatz='30',
    subsidiaerfall_nach_2288_qualifiziert=True,
    bewertungsnachweis='Synthetisch qualifizierter subsidiärer Ersatzfall.',
)
```
