# Kalenderkern der BGB-Libraries

Feste lokale PDF-Fassung: SHA256 `9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb`. Acht implementierte Kalenderfunktionen, keine Behauptung vollständiger BGB-Abdeckung.

Alle Datumsangaben sind skalare ISO-Zeichenfolgen mit vierstelligem Jahr 0001–9999. Der Kalender ist proleptisch gregorianisch. Eine Ausgabe zum Fristende bezeichnet den Ablauf des Tages; ein Lebensalterbeginn den Beginn des ausgegebenen Tages. Die Anwendbarkeit der festen Gesetzesfassung und speziellere Vorschriften müssen vorab geklärt sein.

Python: `None` oder ausgelassener Pflichtparameter → `Berechnungsfehler.status == "EINGABE_FEHLT"`; ungültige Typen/Werte → `EINGABE_UNGUELTIG`. Python verlangt echte `int`, keine `bool` oder `float`. R akzeptiert skalare endliche ganzzahlige Zahlen; `NULL`/`NA` fehlen, `NaN` und Vektoren sind ungültig. Es gibt keine stille Vektorisierung.

Ergebnisse enthalten `wert`, `einheit`, `regel_id`, `regelversion`, `quellenfassung`, `eingaben`, `nutzervorgaben`, `rechenschritte`, `annahmen`, `hinweise`, `status`. Fehler liefern keinen Zahlenwert. R verwendet die S3-Klasse `bgb_ergebnis` und die Condition `bgb_berechnungsfehler`.

## fristende

`fristende(anfangstag, anzahl, einheit, beginnart)`

Datum des letzten Fristtages, Ablauf am Tagesende. Tage/Wochen: Anfang + Dauer minus 1 nur bei Tagesbeginn. Monate/Jahre: Zielmonat nach Dauer, bei Ereignis Tag=Anfangstag, bei Tagesbeginn Tag=Anfangstag-1; Tag 0 bezeichnet letzten Tag des Vormonats. Fehlenden maßgeblichen Tag auf letztem Tag des Zielmonats begrenzen. Halbes Jahr 6, Vierteljahr 3 Monate, halber Monat 15 Tage.

- `anfangstag`: Anknüpfungsdatum als ISO-Zeichenfolge YYYY-MM-DD. Ereignistag und Tagesbeginn werden über beginnart unterschieden.
- `anzahl`: Ganze Anzahl der Einheiten, höchstens 3652059; positive Zahl bei Fristen, null bei zeitraum_tage zulässig. Technischer Wertebereich, keine gesetzliche Fristobergrenze.
- `einheit`: Fristen: tage, wochen, monate, jahre, halbjahre, vierteljahre oder halber_monat. Bei halber_monat ist anzahl genau eins. zeitraum_tage erlaubt nur monate oder jahre.
- `beginnart`: ereignis schließt den Anknüpfungstag aus; tagesbeginn zählt ihn mit.

Regel-ID: `BGB_FRIST_KALENDER`. Quellenanker: BGB_186_T0001, BGB_187_T0001, BGB_187_T0002, BGB_187_T0003, BGB_188_T0001, BGB_188_T0002, BGB_188_T0003, BGB_189_T0001, BGB_189_T0002.

## fristende_monate_halb

`fristende_monate_halb(anfangstag, ganze_monate, beginnart)`

Zuerst ganze Monate gemäß Kalenderfrist, danach exakt 15 Tage. Nicht zuerst 15 Tage und nicht 1,5*30 Tage.

- `anfangstag`: Anknüpfungsdatum als ISO-Zeichenfolge YYYY-MM-DD. Ereignistag und Tagesbeginn werden über beginnart unterschieden.
- `ganze_monate`: Positive ganze Zahl vollständiger Kalendermonate, höchstens 3652059; die 15 Tage werden danach gezählt.
- `beginnart`: ereignis schließt den Anknüpfungstag aus; tagesbeginn zählt ihn mit.

Regel-ID: `BGB_FRIST_MONATE_HALB`. Quellenanker: BGB_186_T0001, BGB_187_T0001, BGB_187_T0002, BGB_187_T0003, BGB_188_T0001, BGB_188_T0002, BGB_188_T0003, BGB_189_T0001, BGB_189_T0002.

## fristverlaengerung

`fristverlaengerung(bisheriges_fristende, anzahl, einheit)`

Voriger Ablauf als Ereignisdatum für Verlängerungsfrist. Keine erneute Anknüpfung an ursprünglichen Anfang. Nutzer liefert den rechtlich maßgeblichen vorigen Ablauf.

- `bisheriges_fristende`: Rechtlich maßgeblicher Ablauf der bisherigen Frist als ISO-Datum; keine automatische Bestimmung aus einem früheren Fristbeginn.
- `anzahl`: Ganze Anzahl der Einheiten, höchstens 3652059; positive Zahl bei Fristen, null bei zeitraum_tage zulässig. Technischer Wertebereich, keine gesetzliche Fristobergrenze.
- `einheit`: Fristen: tage, wochen, monate, jahre, halbjahre, vierteljahre oder halber_monat. Bei halber_monat ist anzahl genau eins. zeitraum_tage erlaubt nur monate oder jahre.

Regel-ID: `BGB_FRIST_VERLAENGERUNG`. Quellenanker: BGB_186_T0001, BGB_187_T0001, BGB_187_T0002, BGB_187_T0003, BGB_188_T0001, BGB_188_T0002, BGB_188_T0003, BGB_189_T0001, BGB_189_T0002, BGB_190_T0001.

## lebensalter_beginn

`lebensalter_beginn(geburtsdatum, lebensjahre)`

Geburtstag mitzählen. Beginn nach Vollendung der angeforderten Lebensjahre ist der Tag nach dem nach Tagesbeginnprinzip errechneten Jahresfristende. Bei Geburt am 29. Februar und nichtschaltigem Zieljahr: 1. März; kein Feiertagsaufschub. Alter 0 entspricht Geburtstagsbeginn, nicht dem tatsächlichen Geburtszeitpunkt.

- `geburtsdatum`: Geburtstag als ISO-Datum. Uhrzeit wird für das Lebensalter nach § 187 Abs. 2 nicht verwendet.
- `lebensjahre`: Nichtnegative ganze Zahl zu vollendender Jahre, höchstens 3652059. Null liefert den Geburtstagsbeginn; kein Ersatz für den tatsächlichen Beginn der Rechtsfähigkeit.

Regel-ID: `BGB_LEBENSALTER_BEGINN`. Quellenanker: BGB_187_T0001, BGB_187_T0002, BGB_187_T0003, BGB_188_T0001, BGB_188_T0002, BGB_188_T0003.

## monatstermin

`monatstermin(jahr, monat, lage)`

Anfang=1, Mitte=15, Ende=letzter Tag des konkret angegebenen Monats.

- `jahr`: Ganzes Kalenderjahr von 1 bis 9999.
- `monat`: Ganze Monatszahl von 1 bis 12.
- `lage`: anfang, mitte oder ende. Mitte bedeutet den 15. und nicht die Hälfte der Monatslänge.

Regel-ID: `BGB_MONATSTERMIN`. Quellenanker: BGB_192_T0001.

## volljaehrigkeitsbeginn

`volljaehrigkeitsbeginn(geburtsdatum)`

Lebensalterbeginn mit 18 Jahren, ohne Feiertagsverschiebung.

- `geburtsdatum`: Geburtstag als ISO-Datum. Uhrzeit wird für das Lebensalter nach § 187 Abs. 2 nicht verwendet.

Regel-ID: `BGB_VOLLJAEHRIGKEIT`. Quellenanker: BGB_2_T0001, BGB_187_T0001, BGB_187_T0002, BGB_187_T0003, BGB_188_T0001, BGB_188_T0002, BGB_188_T0003.

## werktagsverschiebung

`werktagsverschiebung(datum, anwendungsfall, feiertage, ort, kalenderquelle, kalender_von, kalender_bis)`

Für Leistung/Willenserklärung Samstag, Sonntag und ausdrücklich übergebene örtliche gesetzliche Feiertage überspringen bis nächster zulässiger Tag. Keine Anwendung auf Lebensalter oder beliebige sonstige Fristen.

- `datum`: Ausgangsdatum der Leistung oder Willenserklärung als ISO-Zeichenfolge.
- `anwendungsfall`: Ausschließlich leistung oder willenserklaerung; keine automatische Übertragung auf Lebensalter, Kündigungsfristen oder andere Tatbestände.
- `feiertage`: Explizite Liste oder Zeichenfolge der am angegebenen Ort gesetzlich anerkannten allgemeinen Feiertage; [] bedeutet ausdrücklich keine Feiertage im bestätigten Bereich. None bedeutet fehlend. Keine Netzanfrage.
- `ort`: Nichtleere Bezeichnung des Erklärungs- oder Leistungsorts; die Library ermittelt die Zuständigkeit nicht.
- `kalenderquelle`: Nichtleere Herkunfts- und Versionsangabe des Nutzerkalenders. Seine Vollständigkeit für den angegebenen Zeitraum wird vorausgesetzt und ausgewiesen.
- `kalender_von`: Erster eingeschlossener Tag des bestätigten Feiertagskalenders als ISO-Datum.
- `kalender_bis`: Letzter eingeschlossener Tag des bestätigten Feiertagskalenders. Reicht dieser nicht bis zum nächsten zulässigen Tag, wird die Berechnung abgebrochen.

Regel-ID: `BGB_WERKTAG_ERSATZ`. Quellenanker: BGB_193_T0001.

## zeitraum_tage

`zeitraum_tage(anzahl, einheit, nicht_zusammenhaengend)`

Nur für ausdrücklich nicht zusammenhängend zu verlaufende Zeiträume: Monate*30 oder Jahre*365. Kein Kalenderfrist- oder universeller Zinstageszähler.

- `anzahl`: Ganze Anzahl der Einheiten, höchstens 3652059; positive Zahl bei Fristen, null bei zeitraum_tage zulässig. Technischer Wertebereich, keine gesetzliche Fristobergrenze.
- `einheit`: Fristen: tage, wochen, monate, jahre, halbjahre, vierteljahre oder halber_monat. Bei halber_monat ist anzahl genau eins. zeitraum_tage erlaubt nur monate oder jahre.
- `nicht_zusammenhaengend`: Muss ausdrücklich True sein. Die 30/365-Regel ist keine Konvention für gewöhnliche Kalenderfristen oder Zinsberechnungen.

Regel-ID: `BGB_ZEITRAUM_UNZUSAMMENHAENGEND`. Quellenanker: BGB_191_T0001.

Die Unterscheidung zwischen geordneten Listen und Objekten sowie die zulässigen nativen R-Formen sind im [Strukturvertrag](../../fachkonzept/EINGABESTRUKTUREN.md) festgelegt.
