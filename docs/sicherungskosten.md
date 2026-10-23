# Kosten der Bauhandwerkersicherung

## bau_sicherungskosten_erstattung

Höchstbetrag = Sicherheitsbetrag * 2/100 * ausdrücklich bestimmter Jahresanteil. Erstattungsbetrag = Minimum aus tatsächlichen Kosten, üblichen Kosten und Höchstbetrag.

Ausnahmen nach § 650f Abs. 6 und die Rückausnahme für den bevollmächtigten Baubetreuer werden ausgewertet. Keine Erstattung nach Absatz 3 für einen Teilzeitraum, in dem die Sicherheit wegen Einwendungen gegen den Vergütungsanspruch aufrechterhalten werden muss und diese sich als unbegründet erweisen. Bloßes Bestehen von Einwendungen genügt nicht. Bei wechselnder Sicherheitshöhe oder nur teilweisem Eingreifen dieser Ausnahme getrennte, überschneidungsfreie Zeit-/Kostenabschnitte bilden. Kosten jedem Abschnitt nur einmal zuordnen. Die Funktion bestimmt weder übliche Bankgebühren noch die rechtliche Berechtigung der Einwendungen selbst. Keine automatische Erstattung sonstiger Sicherheiten außerhalb § 650f.

Ergebnisobjekt mit wert als zaehler/nenner-Ganzzahlzeichenfolgen, einheit EUR, Regel- und Quellenfassung, Eingaben, Nutzervorgaben und Rechenschritten. Bei NICHT_ANWENDBAR ist wert null. Fehlende oder ungültige Eingaben erzeugen einen strukturierten Berechnungsfehler.

- `sicherheitsbetrag`: Nichtnegative EUR-Dezimalzeichenfolge des über den gesamten ausgewerteten Zeitraum gleichbleibenden Sicherheitsbetrags.
- `tatsaechliche_kosten`: Nichtnegative EUR-Dezimalzeichenfolge der für diesen Zeitraum tatsächlich entstandenen Sicherungskosten.
- `uebliche_kosten`: Nichtnegative EUR-Dezimalzeichenfolge der rechtlich bewerteten üblichen Sicherungskosten für genau denselben Zeitraum und Sicherheitsumfang.
- `zeitanteil_zaehler`: Nichtnegative ganze Zahl als Zähler des ausdrücklich bestimmten Jahresanteils.
- `zeitanteil_nenner`: Positive ganze Zahl als Nenner des Jahresanteils; gemeinsame technische Grenzen gemäß NUMERIK.md.
- `zeitanteil_nachweis`: Nichtleere Beschreibung des Zeitraums und der maßgeblichen Zeitkonvention. Keine stillschweigende 365-Tage- oder 30/360-Annahme.
- `sicherheit_nach_650f`: Expliziter Wahrheitswert zur Einordnung als Sicherheitsleistung nach § 650f.
- `aufrechterhaltung_wegen_unbegruendeter_einwendungen`: Expliziter Wahrheitswert: Die Sicherheit muss für den gesamten ausgewerteten Teilzeitraum wegen Einwendungen des Bestellers gegen den Vergütungsanspruch aufrechterhalten werden, die sich als unbegründet erweisen. Nur dann greift die Ausnahme des Absatzes 3 Satz 2.
- `bestellerart`: sonstiger, oeffentlich_insolvenzunfaehig, verbraucherbau oder bautraeger_verbraucher. Die öffentlich-rechtliche Kategorie setzt gesetzliche Insolvenzunfähigkeit voraus.
- `baubetreuer_bevollmaechtigt`: Expliziter Wahrheitswert zur Betreuung durch einen zur Verfügung über die Finanzierungsmittel des Bestellers ermächtigten Baubetreuer. Hebt nur die Verbraucherausnahme auf, nicht die öffentlich-rechtliche Ausnahme.

## Exakte Zahleneingaben

Für die als Dezimaltexte beschriebenen Eingaben sind auch exakte Bruchobjekte wie `{"zaehler": "1", "nenner": "3"}` zulässig, einschließlich solcher Felder in Listen. Zähler und Nenner sind kanonische Ganzzahlzeichenfolgen; der Nenner ist positiv. Fachliche Wertebereiche bleiben unverändert. Siehe [gemeinsamer Zahlenvertrag](../../fachkonzept/NUMERIK.md). Dadurch können passende Betragsfelder von Ergebnissen ohne Dezimalrundung weiterverwendet werden. Getrennte ganzzahlige Quotenzähler/-nenner, Anzahlen, Altersstufen und Datumsangaben behalten ihre bisherigen Typen.
