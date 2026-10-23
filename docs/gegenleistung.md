<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## gegenleistung_behaltensbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `vereinbarte_gegenleistung`: Nichtnegative vereinbarte Gegenleistung in EUR für den vollständig von der Leistung befreiten Bezugsfall. Teilweise Befreiung oder bloß ausgeschlossene Nacherfüllung nicht ungeprüft als diesen Fall eingeben.
- `ersparte_aufwendungen`: Nichtnegative infolge der Leistungsbefreiung ersparte Aufwendungen in EUR. Ursächliche und rechtlich anrechenbare Positionen vorab bestimmen.
- `anderweitiger_erwerb`: Nichtnegativer Erwerb durch anderweitige Verwendung der Arbeitskraft in EUR, rechtlich dem Befreiungsfall zugeordnet. Keine doppelte Anrechnung derselben Position als Ersparnis.
- `boeswillig_unterlassener_erwerb`: Nichtnegativer bewerteter Betrag böswillig unterlassenen anderweitigen Erwerbs in EUR. Böswilligkeit und Erwerbsmöglichkeit sind eigenständige rechtliche Bewertungen, keine frei eingesetzte Strafquote.
- `leistungsbefreiung_nach_275`: Wahrheitswert, ob der Schuldner nach§275 Absätze1–3 für den hier berechneten Bezugsfall nicht zu leisten braucht. Sachlichen Anwendungsbereich des§326 Absatz2 und Vorrang besonderer Gefahrtragungsregeln vorab bestimmen.
- `glaeubiger_allein_oder_weit_ueberwiegend_verantwortlich`: Wahrheitswert zur alleinigen oder weit überwiegenden Verantwortlichkeit des Gläubigers für den Befreiungsumstand. Nicht bloß irgendein Mitverschulden; keine erfundene prozentuale Schwelle.
- `schuldner_hat_umstand_zu_vertreten`: Wahrheitswert, ob der Schuldner den zur Leistungsbefreiung führenden Umstand zu vertreten hat. Für die Annahmeverzugsalternative muss dieser Wert FALSE sein.
- `annahmeverzug_bei_eintritt`: Wahrheitswert, ob gerade beim Eintritt des Befreiungsumstands der Gläubiger in Annahmeverzug war. Bloß irgendwann früherer Verzug reicht nicht.
- `bewertungsnachweis`: Nichtleere Beschreibung von Leistungsbefreiung, Gefahrtragung, Verantwortlichkeit, Zeitpunkt des Annahmeverzugs und den drei getrennten Anrechnungspositionen.

Behaltensgrund=Leistungsbefreiung UND(Gläubiger allein/weit überwiegend verantwortlich ODER(Schuldner nicht verantwortlich UND Annahmeverzug beim Eintritt)). Dann Gegenleistung minus Ersparnis minus Erwerb minus böswillig unterlassenen Erwerb, mindestens0. Ohne diesen Behaltensgrund NICHT_ANWENDBAR.

wert enthält den exakten verbleibenden EUR-Betrag. Nichtanwendbarkeit ergibt null, nicht einen festgestellten Gegenleistungswegfall.

Nur Absatz2, keine umfassende Gefahrtragungsberechnung. Bei Nichtanwendbarkeit kann Gegenleistung nach anderen Regeln bestehen oder entfallen; nicht automatisch0. Teilbefreiung, bloße Nacherfüllungsbefreiung, Ersatzverlangen nach Absatz3, Sonderregeln und Rückabwicklung separat.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_326_T0002, BGB_326_T0003, BGB_326_T0004, BGB_326_T0005

```python
from bgbcalc import gegenleistung_behaltensbetrag
gegenleistung_behaltensbetrag(
    vereinbarte_gegenleistung='1000',
    ersparte_aufwendungen='100',
    anderweitiger_erwerb='200',
    boeswillig_unterlassener_erwerb='50',
    leistungsbefreiung_nach_275=True,
    glaeubiger_allein_oder_weit_ueberwiegend_verantwortlich=False,
    schuldner_hat_umstand_zu_vertreten=False,
    annahmeverzug_bei_eintritt=True,
    bewertungsnachweis='Synthetischer vollständiger Befreiungsfall ohne vorrangige Sonderregel.',
)
```

## gegenleistung_bei_ersatzverlangen

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `vereinbarte_gegenleistung`: Nichtnegative vereinbarte Gegenleistung in EUR für den Bezugsfall des verlangten Ersatzes. Nicht durch den tatsächlichen Sachwert ersetzen.
- `wert_geschuldeter_leistung`: Positiver rechtlich maßgeblicher Wert der geschuldeten Leistung in EUR, konsistent zum Ersatzwert und dem Verweis auf§441 Absatz3 bewertet. Verhältnisrechnung benötigt einen positiven Vergleichswert.
- `wert_ersatz_oder_ersatzanspruch`: Nichtnegativer rechtlich maßgeblicher Wert des konkret nach§285 herauszugebenden Ersatzes oder abzutretenden Ersatzanspruchs in EUR. Der Nominalbetrag eines uneinbringlichen Anspruchs ist nicht automatisch dessen Wert.
- `ersatz_nach_285_verlangt`: Wahrheitswert eines rechtlich einschlägigen Ersatz-/Abtretungsverlangens nach§285 im Anwendungsbereich§326 Absatz3. FALSE ergibt NICHT_ANWENDBAR. Das Programm stellt keinen Ersatzanspruch aus beliebigen Drittzahlungen her.
- `bewertungsnachweis`: Nichtleere Beschreibung des Ersatzanspruchs, Verlangens und konsistenten Bewertungsmaßstabs/-zeitpunkts für geschuldete Leistung und Ersatz. Verhältnis zur sonstigen Gefahrtragung gesondert bestimmen.

Bei einschlägigem Ersatzverlangen: Gegenleistung×min(Ersatzwert,Wert geschuldeter Leistung)/Wert geschuldeter Leistung. Niedriger Ersatzwert vermindert relativ; gleicher oder höherer Wert belässt vereinbarte Gegenleistung.

wert ist die exakte noch geschuldete Gegenleistung als EUR-Bruch für diesen gesetzlichen Weg. NICHT_ANWENDBAR bei fehlendem Ersatzverlangen.

Nur§326 Absatz3; keine Feststellung des§285-Anspruchs und keine Addition zu einem Ergebnis nach Absatz2. Werte sind rechtlich bewertete Nutzervorgaben; Rückforderung bereits geleisteter Gegenleistung und Nutzungen separat.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_326_T0006, BGB_326_T0007, BGB_441_T0004, BGB_441_T0005

```python
from bgbcalc import gegenleistung_bei_ersatzverlangen
gegenleistung_bei_ersatzverlangen(
    vereinbarte_gegenleistung='800',
    wert_geschuldeter_leistung='1000',
    wert_ersatz_oder_ersatzanspruch='0',
    ersatz_nach_285_verlangt=True,
    bewertungsnachweis='Synthetisches rechtlich einschlägiges Ersatzverlangen und konsistente Vergleichswerte.',
)
```
