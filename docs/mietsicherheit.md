# Wohnraummietsicherheit

## mietsicherheit_hoechstbetrag

Dreifache Monatsmiete nach Abzug der als Pauschale oder Vorauszahlung ausgewiesenen Betriebskosten.

Grundhöchstbetrag nach § 551 Abs. 1. Tatsächliche Erträge erhöhen die Sicherheit nach Absatz 3 Satz 4 zusätzlich und werden hier weder berechnet noch auf diesen Grundhöchstbetrag gekappt. Kein pauschaler Abzug geschätzter Betriebskosten aus einer undifferenzierten Inklusivmiete. Keine Aussage über zusätzliche freiwillige Dritt-Sicherheiten, keine automatische Erhöhung einer bestehenden Sicherheit bei Mietänderung. Vereinbarungen und weitere rechtliche Besonderheiten gesondert prüfen.

wert ist der exakte EUR-Bruch des Grundhöchstbetrags. Bei NICHT_ANWENDBAR ist wert null. Ergebnisobjekt mit Quellenfassung, Eingaben, Nutzervorgaben und Rechenschritten.

- `monatsmiete`: Nichtnegative EUR-Dezimalzeichenfolge der für die Sicherheitsvereinbarung rechtlich maßgeblichen Monatsmiete einschließlich der darin enthaltenen ausgewiesenen Betriebskosten. Nicht automatisch die heutige erhöhte Miete verwenden.
- `ausgewiesene_betriebskosten`: Nichtnegative EUR-Dezimalzeichenfolge der in der Monatsmiete enthaltenen, als Pauschale oder Vorauszahlung ausgewiesenen Betriebskosten. Höchstens die Monatsmiete; ohne ausgewiesene Kosten ausdrücklich "0".
- `wohnraummietverhaeltnis`: Expliziter Wahrheitswert zur rechtlichen Einordnung als hier nach § 551 zu behandelndes Wohnraummietverhältnis. Ausnahmen des § 549 Abs. 2/3 schließen § 551 nicht pauschal aus.

## mietsicherheit_raten

Die rechtlich geschuldete Geldsicherheit in drei exakt gleiche Teilbeträge teilen. Erster Ausgangstermin ist der Mietbeginn; die weiteren Termine sind die ausdrücklich vorgegebenen folgenden Mietfälligkeiten.

Die Funktion bildet das Teilzahlungsrecht ab, verpflichtet aber nicht zur Ausübung dieses Rechts. Sie prüft weder die Wirksamkeit der Sicherheitsvereinbarung noch die Höhe anhand der Monatsmiete; dafür den Grundhöchstbetrag gesondert bestimmen. Nachfolgende Mietfälligkeiten müssen rechtlich passend ausgewählt sein; die Funktion prüft Datumsformat und Reihenfolge, nicht den zugrunde liegenden Mietvertrag. Keine automatische Feiertags-/Wochenendverschiebung; eine gegebenenfalls erforderliche Anwendung des § 193 gesondert berechnen. Keine stillschweigende Cent-Rundung oder Verteilung von Rundungsresten; exakte Drittel können von technisch ausführbaren Zahlungsbeträgen abweichen. Keine Verzugs- oder Kündigungsentscheidung.

wert ist eine Liste von drei Einträgen mit nummer, faellig_am und betrag als exaktem EUR-Bruch. Bei NICHT_ANWENDBAR ist wert null. Ergebnisobjekt mit Quellenfassung, Eingaben, Nutzervorgaben und Rechenschritten.

- `geschuldete_geldsicherheit`: Nichtnegative EUR-Dezimalzeichenfolge der rechtlich geschuldeten Geldsicherheit. Wirksame Vereinbarung und Höchstbetrag gesondert prüfen; kein ungeprüfter überhöhter Vertragsbetrag.
- `mietbeginn`: Beginn des Mietverhältnisses als ISO-Zeichenfolge YYYY-MM-DD, zugleich gesetzlicher Ausgangstermin der ersten Teilzahlung.
- `zweite_mietfaelligkeit`: Rechtlich bestimmter Fälligkeitstermin der unmittelbar auf die erste Mietzahlung folgenden Mietzahlung als ISO-Zeichenfolge. Dies ist der Termin der zweiten Kautionsrate; keine automatische Ableitung aus einem Monatskalender.
- `dritte_mietfaelligkeit`: Rechtlich bestimmter Fälligkeitstermin der darauf folgenden Mietzahlung als ISO-Zeichenfolge; Termin der dritten Kautionsrate. Beide Folgetermine müssen nach Mietbeginn und in aufsteigender Reihenfolge liegen.
- `wohnraummietverhaeltnis`: Expliziter Wahrheitswert zur rechtlichen Einordnung als hier nach § 551 zu behandelndes Wohnraummietverhältnis. Ausnahmen des § 549 Abs. 2/3 schließen § 551 nicht pauschal aus.
- `geldsicherheit_geschuldet`: Expliziter Wahrheitswert, ob als Sicherheit eine Geldsumme bereitzustellen ist. Das Teilzahlungsrecht wird hier nicht auf andere Sicherungsarten übertragen.

## Exakte Zahleneingaben

Für die als Dezimaltexte beschriebenen Eingaben sind auch exakte Bruchobjekte wie `{"zaehler": "1", "nenner": "3"}` zulässig, einschließlich solcher Felder in Listen. Zähler und Nenner sind kanonische Ganzzahlzeichenfolgen; der Nenner ist positiv. Fachliche Wertebereiche bleiben unverändert. Siehe [gemeinsamer Zahlenvertrag](../../fachkonzept/NUMERIK.md). Dadurch können passende Betragsfelder von Ergebnissen ohne Dezimalrundung weiterverwendet werden. Getrennte ganzzahlige Quotenzähler/-nenner, Anzahlen, Altersstufen und Datumsangaben behalten ihre bisherigen Typen.
