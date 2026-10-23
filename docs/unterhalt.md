# Unterhaltsrechenregeln

Keine aktuellen Tabellenbeträge sind fest eingebaut. Alle fachlichen Beträge sind explizite Eingaben. Die Mindestunterhaltsverordnung, der Zeitraum, die Anspruchsvoraussetzungen und der dynamische Prozentsatz müssen zutreffend bestimmt sein.

## unterhaltsaltersstufe

Bis zum Monat der Vollendung von sechs Jahren Stufe 1, ab dessen Beginn Stufe 2; ab Monatsbeginn der Vollendung von zwölf Jahren Stufe 3. Am Stichtag volljährige Personen NICHT_ANWENDBAR.

Altersstufe des Minderjährigenunterhalts, keine automatische Anspruchsprüfung. Volljährigkeit taggenau, nicht auf Monatsbeginn vorziehen. Geburt am Schalttag wird über die gesetzliche Lebensaltersberechnung behandelt. Keine Feiertagsverschiebung.

Rundung: KEINE.

wert ist die ganze Altersstufe 1, 2 oder 3; einheit altersstufe. Bei Volljährigkeit wert null und status NICHT_ANWENDBAR.

- `geburtsdatum`: ISO-Geburtsdatum; darf nicht nach dem Stichtag liegen.
- `stichtag`: ISO-Datum zur Ermittlung der am Stichtag maßgeblichen Minderjährigen-Altersstufe. Volljährigkeit wird taggenau geprüft.

## mindestunterhalt_aus_existenzminimum

Jahresbetrag durch 12 teilen, mit 87/100/117 Prozent je Altersstufe multiplizieren und auf volle EUR aufrunden.

Rechenrelation aus § 1612a Abs. 1/2; liefert keine amtliche Festsetzung nach Abs. 4. Für konkrete dynamische Titel gilt der einschlägige Mindestunterhalt der Rechtsverordnung, als externe Eingabe mit Fassung/Zeitraum. Jahresbetrag weder Grundfreibetrag noch beliebige Einkommensgröße.

Rundung: AUF_VOLLE_EURO_AM_ENDE.

wert enthält den auf volle EUR aufgerundeten Betrag als Bruch mit zaehler und nenner als Ganzzahlzeichenfolgen; nenner ist 1.

- `jaehrliches_existenzminimum`: Positive Dezimalzeichenfolge des maßgeblichen jährlichen sächlichen Existenzminimums in EUR; externe fachliche Eingabe, kein Grundfreibetrag.
- `altersstufe`: Ganze Zahl 1, 2 oder 3; Zuordnung nach § 1612a Abs. 1 und 3.
- `quellenangabe`: Nichtleerer Herkunfts- und Gültigkeitsnachweis der Jahresgrundlage.

## dynamischer_kindesunterhalt

Prozentsatz nach einer Dezimalstelle abschneiden, Mindestunterhalt mit diesem Satz/100 multiplizieren, Ergebnis auf volle EUR aufrunden.

Gesetzliche Voraussetzungen und maßgeblicher Prozentsatz bereits rechtlich bestimmt. Null als Prozentsatz rechnerisch erlaubt, bestätigt keinen Verzicht oder rechtliche Wirksamkeit. Keine automatische Düsseldorfer Tabelle, Leistungsfähigkeitsprüfung oder Kindergeldanrechnung. Mindestunterhaltsquelle ausdrücklich vorgeben.

Rundung: PROZENTSATZ_NACH_1_DEZIMALSTELLE_ABSCHNEIDEN_DANN_BETRAG_AUF_VOLLE_EURO.

wert enthält den auf volle EUR aufgerundeten Betrag als Bruch mit zaehler und nenner als Ganzzahlzeichenfolgen; nenner ist 1.

- `mindestunterhalt`: Positive volle EUR als Dezimalzeichenfolge des einschlägigen Mindestunterhalts für Altersstufe und Zeitraum.
- `prozentsatz`: Nichtnegative Dezimalzeichenfolge in Prozent des Mindestunterhalts; wird nach einer Dezimalstelle abgeschnitten. Keine automatische Einkommensgruppenzuordnung.
- `mindestunterhaltsnachweis`: Nichtleere Beschreibung der maßgeblichen Mindestunterhaltsverordnung, Fassung, Altersstufe und Gültigkeit. Synthetische Beispiele entsprechend kennzeichnen.

## kindbezogene_leistung_anrechnen

Leistung um Erhöhung wegen nicht gemeinschaftlichen Kindes vermindern, bei Erfüllung durch Betreuung Hälfte, sonst volle Summe auf Barbedarf anrechnen. Bedarf mindestens null. Ersatzleistung nur bei regelmäßigem Wiederkehren und Ausschluss von Kindergeld.

betreuung_durch_elternteil bezeichnet rechtlich bewertete Erfüllung nach § 1606 Abs. 3 Satz 2, nicht jede tatsächliche Betreuungszeit. Wechselmodell nicht ohne Einordnung als Halbfall behandeln. Ersatzleistungen nur soweit sie Kindergeld ausschließen; anteilig betroffene Leistung vorab abgrenzen. Keine automatische Verteilung unter mehreren Unterhaltspflichtigen und keine Behandlung sonstiger Sozialleistungen.

Rundung: KEINE.

wert enthält bedarfsrelevante_leistung, bedarfsdeckung und verbleibender_barbedarf, jeweils als exakten EUR-Bruch. Bedarfsdeckung ist auf den Bedarf begrenzt; die bedarfsrelevante Leistung kann höher sein.

- `barbedarf`: Nichtnegative Dezimalzeichenfolge des bewerteten Barbedarfs vor dieser Anrechnung in EUR.
- `leistungsbetrag`: Nichtnegative Dezimalzeichenfolge des auf das Kind entfallenden Kindergelds oder der einschlägigen Ersatzleistung in EUR.
- `erhoehung_nichtgemeinschaftliches_kind`: Nichtnegative Dezimalzeichenfolge des Erhöhungsanteils wegen Berücksichtigung eines nicht gemeinschaftlichen Kindes; höchstens Leistungsbetrag.
- `betreuung_durch_elternteil`: Expliziter Wahrheitswert: Ein Elternteil erfüllt seine Unterhaltspflicht durch Betreuung nach § 1606 Abs. 3 Satz 2. Keine bloße Angabe, ob Betreuung tatsächlich stattfindet.
- `leistungsart`: kindergeld oder ersatzleistung. Andere Leistungsarten sind nicht erfasst.
- `regelmaessig_wiederkehrend`: Expliziter Wahrheitswert, ob die Ersatzleistung regelmäßig wiederkehrt. Im Kindergeldzweig keine zusätzliche Berechnungsbedingung.
- `kindergeld_ausgeschlossen`: Expliziter Wahrheitswert: Die angegebene Ersatzleistung schließt Kindergeld aus. Für Kindergeld selbst muss False angegeben werden.

## Exakte Zahleneingaben

Für die als Dezimaltexte beschriebenen Eingaben sind auch exakte Bruchobjekte wie `{"zaehler": "1", "nenner": "3"}` zulässig, einschließlich solcher Felder in Listen. Zähler und Nenner sind kanonische Ganzzahlzeichenfolgen; der Nenner ist positiv. Fachliche Wertebereiche bleiben unverändert. Siehe [gemeinsamer Zahlenvertrag](../../fachkonzept/NUMERIK.md). Dadurch können passende Betragsfelder von Ergebnissen ohne Dezimalrundung weiterverwendet werden. Getrennte ganzzahlige Quotenzähler/-nenner, Anzahlen, Altersstufen und Datumsangaben behalten ihre bisherigen Typen.
