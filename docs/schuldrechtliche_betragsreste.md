<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## annahmeverzug_mehraufwendungsbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `mehraufwand_erfolgloses_angebot`: Erforderlicher zusätzlicher EUR-Aufwand für erfolgloses Angebot, rechtlich nach304 zugeordnet.
- `mehraufwand_aufbewahrung`: Erforderlicher zusätzlicher EUR-Aufwand für Aufbewahrung, überschneidungsfrei.
- `mehraufwand_erhaltung`: Erforderlicher zusätzlicher EUR-Aufwand für Erhaltung, überschneidungsfrei.
- `einordnungsnachweis`: Nichtleerer Nachweis des Gläubigerverzugs und der erforderlichen zusätzlichen Aufwendungen ohne Doppelzählung.

Erforderliche zusätzliche Aufwendungen für erfolgloses Angebot, Aufbewahrung und Erhaltung addieren.

wert ist der exakte EUR-Bruch.

§304: nur rechtlich zugeordnete erforderliche Mehraufwendungen infolge des Annahmeverzugs; keine pauschale Bewertung von Arbeitszeit oder ohnehin angefallenen Kosten. Kostenpositionen überschneidungsfrei den drei Gruppen zuordnen; dieselbe Rechnung nur einmal erfassen. Grundvoraussetzungen des Annahmeverzugs sowie weitergehende Schadensersatzansprüche werden nicht ermittelt.

Nichtnegative Eingangswerte, exakter nichtnegativer EUR-Bruch im sicheren gemeinsamen Zahlenbereich.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_304_T0001

```python
from bgbcalc import annahmeverzug_mehraufwendungsbetrag
annahmeverzug_mehraufwendungsbetrag(
    mehraufwand_erfolgloses_angebot='10',
    mehraufwand_aufbewahrung='20',
    mehraufwand_erhaltung='30',
    einordnungsnachweis='§304: nur rechtlich zugeordnete erforderliche Mehraufwendungen infolge des Annahmeverzugs; keine pauschale Bewertung von Arbeitszeit oder ohnehin angefallenen Kosten. Kostenpositionen überschneidungsfrei den drei Gruppen zuordnen; dieselbe Rechnung nur einmal erfassen. Grundvoraussetzungen des Annahmeverzugs sowie weitergehende Schadensersatzansprüche werden nicht ermittelt.',
)
```

## anweisung_schuldrest_nach_leistung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `schuld_vor_leistung`: Offene Schuld des Angewiesenen gegenüber dem Anweisenden vor tatsächlicher Leistung, in EUR.
- `tatsaechlich_geleisteter_betrag`: Tatsächlich bewirkte und dieser Anweisungsschuld zugeordnete Leistung in EUR; bloße Annahme der Anweisung zählt nicht.
- `einordnungsnachweis`: Nichtleerer Nachweis der Anweisung auf Schuld nach787I und tatsächlicher schuldbefreiender Leistung; eindeutige Zuordnung ohne Doppeltilgung.

Offene Anweisungsschuld um tatsächlich bewirkte zugeordnete Leistung mindern, mindestens null.

wert ist der exakte EUR-Bruch.

§787I: nur Betrag der Schuld des Angewiesenen gegenüber dem Anweisenden im qualifizierten Deckungsverhältnis. §788 trennt bloße Annahme von tatsächlicher Leistung im Valutaverhältnis; die Annahme allein wird nicht als Zahlung eingestellt. Andere Schuldverhältnisse nicht vermischen. Überschießende Zahlung begründet hier weder negative Schuld noch automatisch einen Rückforderungsanspruch.

Nichtnegative Eingangswerte, exakter nichtnegativer EUR-Bruch im sicheren gemeinsamen Zahlenbereich.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_787_T0001

```python
from bgbcalc import anweisung_schuldrest_nach_leistung
anweisung_schuldrest_nach_leistung(
    schuld_vor_leistung='100',
    tatsaechlich_geleisteter_betrag='40',
    einordnungsnachweis='§787I: nur Betrag der Schuld des Angewiesenen gegenüber dem Anweisenden im qualifizierten Deckungsverhältnis. §788 trennt bloße Annahme von tatsächlicher Leistung im Valutaverhältnis; die Annahme allein wird nicht als Zahlung eingestellt. Andere Schuldverhältnisse nicht vermischen. Überschießende Zahlung begründet hier weder negative Schuld noch automatisch einen Rückforderungsanspruch.',
)
```

## bereicherung_entreicherungsrest

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `qualifizierter_geldherausgabebetrag`: Nichtnegativer exakter EUR-Ausgangsbetrag rechtlich geschuldeter Geldherausgabe/Wertersatzes einschließlich zugeordneter Nutzungen/Surrogate, ohne Doppelzählung. Beispielsweise Summe aus schuldrecht_geldpositionssumme für bereicherung_geldkomponenten.
- `anrechenbare_entreicherung`: Nichtnegativer exakter EUR-Betrag des rechtlich anrechenbaren Wegfalls der Bereicherung, höchstens Ausgangsbetrag. Keine beliebigen Ausgaben oder Vermögensverluste; soweit verschärfte Haftung die Einwendung ausschließt, keine solchen Beträge einrechnen.
- `einordnungsnachweis`: Nichtleerer Nachweis von Ausgangsbereicherung, noch bestehender Bereicherung und rechtlich anrechenbarem Wegfall. Zeitpunkte und verschärfte Haftung818IV/819/820 gesondert bestimmen.

Qualifizierten Geldherausgabebetrag um rechtlich anrechenbare Entreicherung vermindern.

wert ist der exakte EUR-Bruch.

§818III: ausschließlich numerische Begrenzung auf Grundlage bereits rechtlich bestimmter Beträge. Entreicherung nicht automatisch aus vermindertem Kontostand, Konsumausgaben oder Verlusten ablesen. Anrechenbaren Wegfall auf die tatsächlich erfassten Komponenten und den maßgeblichen Haftungszeitraum beziehen. Verschärfte Haftung818IV/819/820, Nutzungsgrenze820II, Drittweitergabe822 und Einreden821 gesondert; ausgeschlossene Entreicherung darf nicht durch positives Eingabefeld wieder eingeführt werden. Keine automatische Saldotheorie oder Verrechnung beider Leistungsrichtungen, keine körperliche Sachherausgabe als Geldrest behandeln. Zahlungen separat.

Nichtnegative Eingangswerte, exakter nichtnegativer EUR-Bruch im sicheren gemeinsamen Zahlenbereich.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_818_T0003

```python
from bgbcalc import bereicherung_entreicherungsrest
bereicherung_entreicherungsrest(
    qualifizierter_geldherausgabebetrag='100',
    anrechenbare_entreicherung='40',
    einordnungsnachweis='§818III: ausschließlich numerische Begrenzung auf Grundlage bereits rechtlich bestimmter Beträge. Entreicherung nicht automatisch aus vermindertem Kontostand, Konsumausgaben oder Verlusten ablesen. Anrechenbaren Wegfall auf die tatsächlich erfassten Komponenten und den maßgeblichen Haftungszeitraum beziehen. Verschärfte Haftung818IV/819/820, Nutzungsgrenze820II, Drittweitergabe822 und Einreden821 gesondert; ausgeschlossene Entreicherung darf nicht durch positives Eingabefeld wieder eingeführt werden. Keine automatische Saldotheorie oder Verrechnung beider Leistungsrichtungen, keine körperliche Sachherausgabe als Geldrest behandeln. Zahlungen separat.',
)
```

## billigkeitshaftung_mittelbegrenzter_betrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `billig_erforderlicher_ersatzbetrag`: Vorqualifizierter nach Billigkeit erforderlicher Schadloshaltungsbetrag in EUR; nicht automatisch voller Schaden.
- `verfuegbare_mittel`: Rechtlich festgestellte für den betrachteten Ausgleich verfügbare Mittel in EUR, zeitlich und wirtschaftlich konsistent bewertet.
- `geschuetzter_unterhaltsbedarf`: Davon benötigte Mittel für angemessenen eigenen Unterhalt und gesetzliche Unterhaltspflichten in EUR; ohne Doppelzählung.
- `einordnungsnachweis`: Nachweis des Anwendungsbereichs829 und der Billigkeitsbewertung sowie konsistenter Mittel-/Unterhaltsbewertung; kein Ersatz durch aufsichtspflichtigen Dritten erlangbar.

Vom verfügbaren Mittelbestand geschützten Unterhaltsbedarf abziehen, mindestens null; Billigkeitsersatz auf diesen verbleibenden Betrag begrenzen.

wert ist der exakte EUR-Bruch.

§829: nur numerische Mittelgrenze eines bereits nach Billigkeit qualifizierten Ersatzbetrags. Keine automatische Billigkeitsentscheidung aus Vermögenszahlen und keine Tabelle für angemessenen Unterhalt. Haftungsvoraussetzungen827/828, fehlende Erlangbarkeit von Ersatz durch einen aufsichtspflichtigen Dritten und Verhältnisse der Beteiligten extern feststellen. Keine Entscheidung über zeitliche Streckung, künftige Einkünfte oder Vollstreckbarkeit.

Nichtnegative Eingangswerte, exakter nichtnegativer EUR-Bruch im sicheren gemeinsamen Zahlenbereich.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_829_T0001

```python
from bgbcalc import billigkeitshaftung_mittelbegrenzter_betrag
billigkeitshaftung_mittelbegrenzter_betrag(
    billig_erforderlicher_ersatzbetrag='1000',
    verfuegbare_mittel='1200',
    geschuetzter_unterhaltsbedarf='500',
    einordnungsnachweis='§829: nur numerische Mittelgrenze eines bereits nach Billigkeit qualifizierten Ersatzbetrags. Keine automatische Billigkeitsentscheidung aus Vermögenszahlen und keine Tabelle für angemessenen Unterhalt. Haftungsvoraussetzungen827/828, fehlende Erlangbarkeit von Ersatz durch einen aufsichtspflichtigen Dritten und Verhältnisse der Beteiligten extern feststellen. Keine Entscheidung über zeitliche Streckung, künftige Einkünfte oder Vollstreckbarkeit.',
)
```

## buergschaft_forderungsuebergang_betrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `offene_hauptforderung`: Noch bestehende, von der Bürgschaft erfasste Gläubigerforderung gegen den Hauptschuldner in EUR unmittelbar vor der betrachteten Befriedigung. Bei entsprechender Anwendung1143I: Eigentümer ist nicht persönlicher Schuldner, konkrete gesicherte Forderung und darauf bewirkte Eigentümerbefriedigung qualifizieren; keine zusätzliche Bürgschaft erforderlich.
- `befriedigung_durch_buergen`: Durch die konkrete Bürgenleistung auf diese Hauptforderung tatsächlich bewirkter Befriedigungsbetrag in EUR; keine bloße Zahlung ohne Tilgungszuordnung. Bei entsprechender Anwendung1143I: Eigentümer ist nicht persönlicher Schuldner, konkrete gesicherte Forderung und darauf bewirkte Eigentümerbefriedigung qualifizieren; keine zusätzliche Bürgschaft erforderlich.
- `einordnungsnachweis`: Nachweis der wirksamen Bürgschaft, zugeordneten Hauptforderung und tatsächlich eingetretenen Befriedigung nach774I. Bei entsprechender Anwendung1143I: Eigentümer ist nicht persönlicher Schuldner, konkrete gesicherte Forderung und darauf bewirkte Eigentümerbefriedigung qualifizieren; keine zusätzliche Bürgschaft erforderlich.

Numerischer Forderungsübergang: Minimum aus noch bestehender erfasster Hauptforderung und darauf bewirkter Befriedigung durch den Bürgen.

wert ist der exakte EUR-Bruch.

§774I: ausschließlich Höhe des gesetzlichen Übergangs der konkret erfassten Hauptforderung. Entsprechend§1143I bei Befriedigung durch den Grundstückseigentümer, der nicht persönlicher Schuldner ist; befriedigung_durch_buergen bezeichnet in dieser Normanwendung dessen qualifizierten Befriedigungsbetrag. Der Funktionsname bezeichnet den wiederverwendeten774-Kern, keine zusätzlich vorausgesetzte Bürgschaft. Gesamthypothekenfolgen1143II/1173 und Sicherheitenverteilung werden hier nicht berechnet. Keine Vermehrung der Forderung bei Überzahlung und keine Berechnung eines daraus möglichen Rückforderungsanspruchs. Durchsetzung darf dem verbleibenden Gläubiger nicht schaden; Hauptschuldnereinwendungen bleiben bestehen. Innenausgleich unter Mitbürgen nach774II/426, Sicherheiten, Zinsen und Kosten separat zuordnen; keine doppelte Erfassung bereits übergegangener Forderungen.

Nichtnegative Eingangswerte, exakter nichtnegativer EUR-Bruch im sicheren gemeinsamen Zahlenbereich.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1143_T0001, BGB_1143_T0002, BGB_774_T0001, BGB_774_T0002, BGB_774_T0003

```python
from bgbcalc import buergschaft_forderungsuebergang_betrag
buergschaft_forderungsuebergang_betrag(
    offene_hauptforderung='100',
    befriedigung_durch_buergen='80',
    einordnungsnachweis='§774I: ausschließlich Höhe des gesetzlichen Übergangs der konkret erfassten Hauptforderung. Keine Vermehrung der Forderung bei Überzahlung und keine Berechnung eines daraus möglichen Rückforderungsanspruchs. Durchsetzung darf dem verbleibenden Gläubiger nicht schaden; Hauptschuldnereinwendungen bleiben bestehen. Innenausgleich unter Mitbürgen nach774II/426, Sicherheiten, Zinsen und Kosten separat zuordnen; keine doppelte Erfassung bereits übergegangener Forderungen.',
)
```

## buergschaft_regressverlust_restbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `buergschaftsverbindlichkeit`: Rechtlich bestimmter offener Bürgschaftsbetrag in EUR vor776-Freistellung.
- `verlorener_erlangbarer_regress`: Aus dem vom Gläubiger aufgegebenen Recht tatsächlich hypothetisch erlangbarer Ersatzbetrag nach774 in EUR; bereits rechtlich und wirtschaftlich bewertet.
- `einordnungsnachweis`: Nichtleerer Nachweis des776-Falls, Rechtsaufgabe durch den Gläubiger und erlangbarer Ersatz, ohne doppelte Erfassung derselben Regressmöglichkeit.

Offene Bürgschaftsverbindlichkeit um erlangbaren verlorenen Regress mindern, mindestens null.

wert ist der exakte EUR-Bruch.

§776: Maßgeblich ist der erlangbare Ersatz aus dem aufgegebenen Recht, nicht automatisch dessen Nominalwert. Verwertbarkeit, Rang, Mitbürgenquote und weitere Bedingungen vorqualifizieren. Keine automatische Auslegung einer wirksamen Rechtsaufgabe oder kumulative Anrechnung gleicher Sicherheiten. Ergebnis ist verbleibende betragsmäßige Bürgschaftsbindung vor weiteren Einreden; überschießender Regresswert begründet hier keine Forderung des Bürgen.

Nichtnegative Eingangswerte, exakter nichtnegativer EUR-Bruch im sicheren gemeinsamen Zahlenbereich.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_776_T0001, BGB_776_T0002

```python
from bgbcalc import buergschaft_regressverlust_restbetrag
buergschaft_regressverlust_restbetrag(
    buergschaftsverbindlichkeit='100',
    verlorener_erlangbarer_regress='40',
    einordnungsnachweis='§776: Maßgeblich ist der erlangbare Ersatz aus dem aufgegebenen Recht, nicht automatisch dessen Nominalwert. Verwertbarkeit, Rang, Mitbürgenquote und weitere Bedingungen vorqualifizieren. Keine automatische Auslegung einer wirksamen Rechtsaufgabe oder kumulative Anrechnung gleicher Sicherheiten. Ergebnis ist verbleibende betragsmäßige Bürgschaftsbindung vor weiteren Einreden; überschießender Regresswert begründet hier keine Forderung des Bürgen.',
)
```

## entgangener_gewinn_nettobetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `erwartbare_erloese`: Rechtlich begründete, ohne das Schadensereignis erwartbare Erlöse in EUR.
- `zugehoerige_aufwendungen`: Diesen Erlösen wirtschaftlich zugeordnete erwartbare Aufwendungen in EUR, ohne Doppelzählung.
- `einordnungsnachweis`: Nichtleerer Nachweis der qualifizierten kontrafaktischen Einnahmen-/Kostenbasis und des betrachteten Geschäfts/Zeitraums.

Erwartbare Erlöse um zugehörige Aufwendungen vermindern; positiver Nettogewinn mindestens null.

wert ist der exakte EUR-Bruch.

§252: rein rechnerische Nettogewinnermittlung aus qualifizierter kontrafaktischer Basis. Wahrscheinlichkeit, Kausalität und Bewertungsansatz werden nicht ermittelt. Kein zusätzlicher Anspruch auf Erlös und Nettogewinn zugleich; weitere Vorteile, tatsächlich verbleibende Erträge, Mitverschulden und Schadensminderung getrennt berücksichtigen. Negative Marge begründet hier keinen entgangenen Gewinn; kein vollständiger Schadensersatzbetrag.

Nichtnegative Eingangswerte, exakter nichtnegativer EUR-Bruch im sicheren gemeinsamen Zahlenbereich.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_252_T0001, BGB_252_T0002

```python
from bgbcalc import entgangener_gewinn_nettobetrag
entgangener_gewinn_nettobetrag(
    erwartbare_erloese='1000',
    zugehoerige_aufwendungen='400',
    einordnungsnachweis='§252: rein rechnerische Nettogewinnermittlung aus qualifizierter kontrafaktischer Basis. Wahrscheinlichkeit, Kausalität und Bewertungsansatz werden nicht ermittelt. Kein zusätzlicher Anspruch auf Erlös und Nettogewinn zugleich; weitere Vorteile, tatsächlich verbleibende Erträge, Mitverschulden und Schadensminderung getrennt berücksichtigen. Negative Marge begründet hier keinen entgangenen Gewinn; kein vollständiger Schadensersatzbetrag.',
)
```

## landpacht_beschreibung_kostenhaelfte

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `sachverstaendigenkosten`: Nichtnegative exakte EUR-Gesamtkosten der rechtlich qualifizierten Sachverständigenbeschreibung585bII; keine beliebigen Beratungskosten.
- `einordnungsnachweis`: Nichtleerer Nachweis des Sachverständigenverfahrens585bII und der diesem zugeordneten Kosten. Frist und gerichtliche Ernennung separat.

Qualifizierte Sachverständigenkosten zur Hälfte je Vertragsseite aufteilen.

wert ist der exakte EUR-Bruch.

§585bII: Verpächter und Pächter tragen jeweils eine Hälfte der qualifizierten Kosten. Nicht erneut durch die Anzahl einzelner Personen innerhalb einer Vertragsseite teilen. Keine Kostenentscheidung über andere Verfahren; bereits gezahlte Beiträge separat. Exakte Hälfte ohne Cent-Rundung; beide Seitenanteile ergeben zusammen den Gesamtbetrag.

Nichtnegative Eingangswerte, exakter nichtnegativer EUR-Bruch im sicheren gemeinsamen Zahlenbereich.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_585b_T0004, BGB_585b_T0005

```python
from bgbcalc import landpacht_beschreibung_kostenhaelfte
landpacht_beschreibung_kostenhaelfte(
    sachverstaendigenkosten='100',
    einordnungsnachweis='§585bII: Verpächter und Pächter tragen jeweils eine Hälfte der qualifizierten Kosten. Nicht erneut durch die Anzahl einzelner Personen innerhalb einer Vertragsseite teilen. Keine Kostenentscheidung über andere Verfahren; bereits gezahlte Beiträge separat. Exakte Hälfte ohne Cent-Rundung; beide Seitenanteile ergeben zusammen den Gesamtbetrag.',
)
```

## landpacht_erzeugnisse_mehrwert

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `wert_erforderlicher_endbestand`: Nichtnegativer exakter EUR-Wert der nach596bI tatsächlich zurückzulassenden erforderlichen Erzeugnisse, zum rechtlich maßgeblichen einheitlichen Bewertungsstichtag.
- `vergleichswert_uebernommener_anfangsbestand`: Nichtnegativer exakter EUR-Vergleichswert der bei Beginn übernommenen Menge und Beschaffenheit derselben Erzeugnisse, auf gleicher Bewertungsbasis wie Endbestand; nicht historischer Kaufpreis mit späteren Preisänderungen vermischt.
- `einordnungsnachweis`: Nichtleerer Nachweis des qualifizierten Betriebspachtfalls, Erforderlichkeit bis zur nächsten Ernte, ursprünglicher Menge/Beschaffenheit und konsistenter Werte. Getrennte Erzeugnisgruppen ohne ungeprüfte Verlustverrechnung behandeln.

Wert erforderlicher zurückzulassender Erzeugnisse abzüglich gleichartig bewerteten übernommenen Anfangsbestands, mindestens null.

wert ist der exakte EUR-Bruch.

§596bII: Ersatz nur für den rechtlich qualifizierten Mehrbestand beziehungsweise bessere Beschaffenheit der nachAbsatz1 zurückzulassenden Erzeugnisse. Werte müssen den Unterschied in Menge/Beschaffenheit abbilden, nicht bloße allgemeine Preissteigerung. Über die erforderlichen Erzeugnisse hinaus freiwillig zurückgelassene Mengen nicht einrechnen; Pflicht nachAbsatz1 kann auch ohne Anfangsübernahme bestehen, dann Vergleichswert0. Bei verschiedenen Produktgruppen gesondert qualifizieren; keine pauschale Verrechnung fremder Minderbestände. Kein automatischer Anspruch wegen Bestandsangaben allein; Zahlungen separat.

Nichtnegative Eingangswerte, exakter nichtnegativer EUR-Bruch im sicheren gemeinsamen Zahlenbereich.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_596b_T0002

```python
from bgbcalc import landpacht_erzeugnisse_mehrwert
landpacht_erzeugnisse_mehrwert(
    wert_erforderlicher_endbestand='150',
    vergleichswert_uebernommener_anfangsbestand='100',
    einordnungsnachweis='§596bII: Ersatz nur für den rechtlich qualifizierten Mehrbestand beziehungsweise bessere Beschaffenheit der nachAbsatz1 zurückzulassenden Erzeugnisse. Werte müssen den Unterschied in Menge/Beschaffenheit abbilden, nicht bloße allgemeine Preissteigerung. Über die erforderlichen Erzeugnisse hinaus freiwillig zurückgelassene Mengen nicht einrechnen; Pflicht nachAbsatz1 kann auch ohne Anfangsübernahme bestehen, dann Vergleichswert0. Bei verschiedenen Produktgruppen gesondert qualifizieren; keine pauschale Verrechnung fremder Minderbestände. Kein automatischer Anspruch wegen Bestandsangaben allein; Zahlungen separat.',
)
```

## landpacht_verbesserungsmassnahme_ersatzbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `ersatzfaehige_aufwendungen`: Qualifizierte, der Verbesserungsmaßnahme zugeordnete angemessene Aufwendungen in EUR.
- `ersatzfaehige_entgangene_ertraege`: Qualifizierte, angemessene entgangene Erträge in EUR, bereits ohne Überschneidung mit den eingegebenen Aufwendungen bewertet.
- `einordnungsnachweis`: Nachweis der Maßnahme588II und des angemessenen Ersatzumfangs; Überschneidungen zwischen Aufwand und Ertragsausfall ausdrücklich ausgeschlossen.

Angemessene ersatzfähige Aufwendungen und überschneidungsfrei bewertete entgangene Erträge addieren.

wert ist der exakte EUR-Bruch.

§588II: numerischer Ersatzumfang aus qualifizierten Betragskomponenten. Keine automatische Billigkeitsbewertung oder Brutto-/Nettobewertung entgangener Erträge; diese ist widerspruchsfrei mit den Aufwendungen vorzugeben. Vorschüsse/Zahlungen gesondert anrechnen. Eine Pachterhöhung wegen höherer Erträge588III ist ein anderer Rechengegenstand und wird nicht erfunden.

Nichtnegative Eingangswerte, exakter nichtnegativer EUR-Bruch im sicheren gemeinsamen Zahlenbereich.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_588_T0002, BGB_588_T0003, BGB_588_T0004

```python
from bgbcalc import landpacht_verbesserungsmassnahme_ersatzbetrag
landpacht_verbesserungsmassnahme_ersatzbetrag(
    ersatzfaehige_aufwendungen='200',
    ersatzfaehige_entgangene_ertraege='300',
    einordnungsnachweis='§588II: numerischer Ersatzumfang aus qualifizierten Betragskomponenten. Keine automatische Billigkeitsbewertung oder Brutto-/Nettobewertung entgangener Erträge; diese ist widerspruchsfrei mit den Aufwendungen vorzugeben. Vorschüsse/Zahlungen gesondert anrechnen. Eine Pachterhöhung wegen höherer Erträge588III ist ein anderer Rechengegenstand und wird nicht erfunden.',
)
```

## landpacht_verwendungsersatz_mehrwertgrenze

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `ersatzfaehige_verwendungen`: Nichtnegative Kosten qualifizierter anderer als notwendiger Verwendungen in EUR, mit wirksamer Zustimmung.
- `fortbestehender_mehrwert`: Nichtnegative rechtlich bewertete Erhöhung des Wertes der Pachtsache über das Pachtende hinaus in EUR.
- `einordnungsnachweis`: Nachweis der Voraussetzungen591I und des bei Pachtende fortbestehenden Mehrwerts; besondere gerichtliche Anordnungen separat.

Ersatzfähige Verwendungen auf den über die Pachtzeit hinaus fortbestehenden Mehrwert begrenzen.

wert ist der exakte EUR-Bruch.

§591I: Grundbetrag als Minimum aus ersatzfähigen Verwendungen und fortbestehendem Mehrwert. Notwendige Verwendungen590b und Wegnahmerechte591a, Zustimmung/gerichtliche Ersetzung, Bewertungsmethode und gerichtliche Teilzahlungen oder Vertragsfortsetzung591III separat. Kein automatischer Zahlungsplan und keine automatische Fälligkeit bei gerichtlich abweichender Regelung.

Nichtnegative Eingangswerte, exakter nichtnegativer EUR-Bruch im sicheren gemeinsamen Zahlenbereich.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_591_T0001

```python
from bgbcalc import landpacht_verwendungsersatz_mehrwertgrenze
landpacht_verwendungsersatz_mehrwertgrenze(
    ersatzfaehige_verwendungen='1000',
    fortbestehender_mehrwert='800',
    einordnungsnachweis='§591I: Grundbetrag als Minimum aus ersatzfähigen Verwendungen und fortbestehendem Mehrwert. Notwendige Verwendungen590b und Wegnahmerechte591a, Zustimmung/gerichtliche Ersetzung, Bewertungsmethode und gerichtliche Teilzahlungen oder Vertragsfortsetzung591III separat. Kein automatischer Zahlungsplan und keine automatische Fälligkeit bei gerichtlich abweichender Regelung.',
)
```

## mietsicherheit_mit_anlageertraegen

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `sicherheit_vor_ertragszuwachs`: Nichtnegativer vorhandener Sicherheitsbetrag in EUR unmittelbar vor den betrachteten Erträgen.
- `hinzukommende_anlageertraege`: Tatsächliche nichtnegative, dem Mieter zustehende und noch nicht im Sicherheitsbetrag enthaltene Anlageerträge in EUR.
- `einordnungsnachweis`: Nachweis des Sicherheitsbestands und der zusätzlich zugeordneten tatsächlichen Erträge nach551III.

Bestehende Sicherheit und noch nicht enthaltene zugeordnete Anlageerträge addieren.

wert ist der exakte EUR-Bruch.

§551III: tatsächlicher Ertragszuwachs erhöht die Sicherheit; keine erneute Begrenzung des Ertragszuwachses auf drei Monatsmieten. Ausgangssicherheit gesondert nach551I prüfen. Keine Hochrechnung eines hypothetischen Sparzinses, kein Ersatz einer unterlassenen Anlage und keine automatische Kautionsfreigabe. Anlageverluste, Entnahmen und bereits eingerechnete Erträge getrennt berücksichtigen; keine Doppelzählung.

Nichtnegative Eingangswerte, exakter nichtnegativer EUR-Bruch im sicheren gemeinsamen Zahlenbereich.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_551_T0005, BGB_551_T0006, BGB_551_T0007, BGB_551_T0008, BGB_551_T0009

```python
from bgbcalc import mietsicherheit_mit_anlageertraegen
mietsicherheit_mit_anlageertraegen(
    sicherheit_vor_ertragszuwachs='900',
    hinzukommende_anlageertraege='20',
    einordnungsnachweis='§551III: tatsächlicher Ertragszuwachs erhöht die Sicherheit; keine erneute Begrenzung des Ertragszuwachses auf drei Monatsmieten. Ausgangssicherheit gesondert nach551I prüfen. Keine Hochrechnung eines hypothetischen Sparzinses, kein Ersatz einer unterlassenen Anlage und keine automatische Kautionsfreigabe. Anlageverluste, Entnahmen und bereits eingerechnete Erträge getrennt berücksichtigen; keine Doppelzählung.',
)
```

## werk_annahmeverzug_entschaedigungsbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `verzugsbezogene_verguetungsbasis`: Nichtnegativer exakter EUR-Vergütungsanteil, der rechtlich aus der maßgeblichen Verzugsdauer und vereinbarten Vergütung für vorgehaltene Produktionsmittel bestimmt wurde. Keine ungeprüfte gesamte Vertragssumme oder pauschaler Gesamtschaden.
- `ersparte_aufwendungen`: Nichtnegative exakte EUR-Aufwendungen, die infolge desselben Annahmeverzugs im betrachteten Zeitraum erspart werden.
- `anderweitiger_arbeitskraft_erwerb`: Nichtnegativer exakter EUR-Betrag des rechtlich anzurechnenden Erwerbs durch mögliche anderweitige Verwendung der Arbeitskraft im selben Verzugszeitraum;642II setzt hierfür nicht zusätzlich böswilliges Unterlassen voraus.
- `einordnungsnachweis`: Nichtleerer Nachweis erforderlicher Bestellerhandlung, Annahmeverzug, konkreter Dauer/Vergütungsbasis, Vorhaltung und zugehöriger überschneidungsfreier Abzüge. Keine automatische Bewertung angemessener Entschädigung.

Qualifizierte verzugsbezogene Vergütungsbasis abzüglich ersparter Aufwendungen und anderweitigen Arbeitskrafterwerbs, mindestens null.

wert ist der exakte EUR-Bruch.

§642I/II: numerischer Abrechnungsschritt aus rechtlich bestimmter Verzugsdauer-/Vergütungsbasis und zugehörigen Abzügen. Basis nicht blind als gesamte Vergütung geteilt durch gesamte Vertragszeit bilden; tatsächlich betroffene Vorhaltung und rechtlich maßgebliche Bewertungsanteile qualifizieren. Keine automatische Entschädigung sämtlicher Mehrkosten nach Verzugsende und keine Schadensersatzprognose. Ersparnis und anderweitiger Erwerb nur einmal, nicht bereits netto in der Basis und erneut als Abzug. Kein zusätzliches Böswilligkeitserfordernis aus615/648 übertragen. Negative Differenz ergibt0, keinen automatisch begründeten Zahlungsanspruch des Bestellers. Zahlungen separat.

Nichtnegative Eingangswerte, exakter nichtnegativer EUR-Bruch im sicheren gemeinsamen Zahlenbereich.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_642_T0001, BGB_642_T0002

```python
from bgbcalc import werk_annahmeverzug_entschaedigungsbetrag
werk_annahmeverzug_entschaedigungsbetrag(
    verzugsbezogene_verguetungsbasis='1000',
    ersparte_aufwendungen='200',
    anderweitiger_arbeitskraft_erwerb='100',
    einordnungsnachweis='§642I/II: numerischer Abrechnungsschritt aus rechtlich bestimmter Verzugsdauer-/Vergütungsbasis und zugehörigen Abzügen. Basis nicht blind als gesamte Vergütung geteilt durch gesamte Vertragszeit bilden; tatsächlich betroffene Vorhaltung und rechtlich maßgebliche Bewertungsanteile qualifizieren. Keine automatische Entschädigung sämtlicher Mehrkosten nach Verzugsende und keine Schadensersatzprognose. Ersparnis und anderweitiger Erwerb nur einmal, nicht bereits netto in der Basis und erneut als Abzug. Kein zusätzliches Böswilligkeitserfordernis aus615/648 übertragen. Negative Differenz ergibt0, keinen automatisch begründeten Zahlungsanspruch des Bestellers. Zahlungen separat.',
)
```

## zahlungsinstrument_ersatzentgelt_grenze

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `vereinbartes_ersatzentgelt`: Vereinbartes nichtnegatives Ersatzentgelt in EUR, ohne Aussage über die Wirksamkeit eines überschießenden Vertragsbestandteils.
- `unmittelbare_ersatzkosten`: Ausschließlich und unmittelbar mit dem qualifizierten Ersatz verbundene Kosten in EUR; keine allgemeinen Betriebskosten oder Gewinnmarge.
- `einordnungsnachweis`: Nachweis des Ersatzfalls675lI, der Entgeltvereinbarung und der unmittelbar zugeordneten Kosten.

Numerisch auf die ausschließlich unmittelbaren Ersatzkosten begrenztes Entgelt: Minimum aus vereinbartem Entgelt und Kosten.

wert ist der exakte EUR-Bruch.

§675lI: ausschließlich numerische Entgeltobergrenze für Ersatz nach Verlust, Diebstahl, Missbrauch oder sonst nicht autorisierter Nutzung. Das Minimum heilt keine unwirksame Entgeltvereinbarung und entscheidet keinen Zahlungsanspruch; Wirksamkeit und Rechtsfolgen einer überschießenden Klausel gesondert. Kosten müssen dem konkreten Ersatz unmittelbar und ausschließlich zurechenbar sein; kein allgemeines Entgelt für Sperrung oder Anzeige.

Nichtnegative Eingangswerte, exakter nichtnegativer EUR-Bruch im sicheren gemeinsamen Zahlenbereich.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_675l_T0001, BGB_675l_T0002, BGB_675l_T0003

```python
from bgbcalc import zahlungsinstrument_ersatzentgelt_grenze
zahlungsinstrument_ersatzentgelt_grenze(
    vereinbartes_ersatzentgelt='100',
    unmittelbare_ersatzkosten='80',
    einordnungsnachweis='§675lI: ausschließlich numerische Entgeltobergrenze für Ersatz nach Verlust, Diebstahl, Missbrauch oder sonst nicht autorisierter Nutzung. Das Minimum heilt keine unwirksame Entgeltvereinbarung und entscheidet keinen Zahlungsanspruch; Wirksamkeit und Rechtsfolgen einer überschießenden Klausel gesondert. Kosten müssen dem konkreten Ersatz unmittelbar und ausschließlich zurechenbar sein; kein allgemeines Entgelt für Sperrung oder Anzeige.',
)
```

## zahlung_empfaengerentgelt_restbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `vollstaendiger_zahlungsbetrag`: Vollständiger übermittelter Zahlungsbetrag in EUR; vor einem zulässigen Empfängerentgeltabzug.
- `vereinbartes_empfaengerentgelt`: Rechtlich zustehendes vereinbartes Empfängerentgelt in EUR, höchstens der übermittelte Betrag.
- `einordnungsnachweis`: Nichtleerer Nachweis der wirksamen Abzugsvereinbarung nach675qII und des Anwendungsbereichs ohne abweichenden675qIV-Fall.

Vollständigen Zahlungsbetrag um das zulässige vereinbarte Empfängerentgelt vermindern.

wert ist der exakte EUR-Bruch.

§675qII-Grundfall, vor Erteilung der Gutschrift vereinbarter Abzug eines zustehenden Entgelts. Vollständiger Zahlungsbetrag und Entgelt bleiben in eingaben und nutzervorgaben getrennt dokumentiert; gesetzliche Zahlungsinformationen müssen sie separat ausweisen. Keine Kürzung durch zwischengeschaltete Stellen nachAbsatz1, keine Entgeltberechnung und keine Abweichung nachAbsatz4. Entgelt über Zahlungsbetrag und gesonderte Kontobelastungen außerhalb dieses Modells.

Nichtnegative Eingangswerte, exakter nichtnegativer EUR-Bruch im sicheren gemeinsamen Zahlenbereich.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_675q_T0002, BGB_675q_T0003

```python
from bgbcalc import zahlung_empfaengerentgelt_restbetrag
zahlung_empfaengerentgelt_restbetrag(
    vollstaendiger_zahlungsbetrag='100',
    vereinbartes_empfaengerentgelt='3',
    einordnungsnachweis='§675qII-Grundfall, vor Erteilung der Gutschrift vereinbarter Abzug eines zustehenden Entgelts. Vollständiger Zahlungsbetrag und Entgelt bleiben in eingaben und nutzervorgaben getrennt dokumentiert; gesetzliche Zahlungsinformationen müssen sie separat ausweisen. Keine Kürzung durch zwischengeschaltete Stellen nachAbsatz1, keine Entgeltberechnung und keine Abweichung nachAbsatz4. Entgelt über Zahlungsbetrag und gesonderte Kontobelastungen außerhalb dieses Modells.',
)
```
