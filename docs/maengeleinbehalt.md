# Mängelbedingter Zahlungseinbehalt

## werk_maengeleinbehalt

Im Regelfall das Doppelte der erforderlichen Mangelbeseitigungskosten. Ein ausdrücklich begründeter abweichender angemessener Betrag ersetzt den Regeldoppelbetrag. Tatsächlich verweigerbare Zahlung = Minimum aus diesem Betrag und der noch zu zahlenden fälligen Vergütung.

§ 641 Abs. 3 setzt einen Anspruch auf Mangelbeseitigung voraus; § 632a Abs. 1 verweist für Abschläge entsprechend hierauf. Die Funktion bestimmt den betragsmäßigen Rahmen des Einbehalts, erklärt aber kein Zurückbehaltungsrecht für den Nutzer. Die doppelte Kostenhöhe gilt nur in der Regel und ist keine starre Obergrenze. Abweichungen müssen rechtlich begründet vorgegeben werden; die Funktion bewertet ihre Angemessenheit nicht selbst. Kein Schadensersatz- oder Kostenvorschussrechner; keine Entscheidung über andere Leistungsverweigerungsrechte. Bei mehreren Einbehalten keine doppelte Anrechnung derselben Vergütung oder Mängelkosten.

Ergebnisobjekt mit wert als zaehler/nenner-Ganzzahlzeichenfolgen, einheit EUR, Regel- und Quellenfassung, Eingaben, Nutzervorgaben und Rechenschritten. Bei NICHT_ANWENDBAR ist wert null. Fehlende oder ungültige Eingaben erzeugen einen strukturierten Berechnungsfehler.

- `faellige_verguetung`: Nichtnegative EUR-Dezimalzeichenfolge der noch zu zahlenden fälligen Vergütung beziehungsweise des nach § 632a berechtigten Abschlags. Fälligkeit, Leistungswert und Nachweis werden außerhalb dieser Funktion festgestellt.
- `mangelbeseitigungskosten`: Nichtnegative EUR-Dezimalzeichenfolge der erforderlichen Mangelbeseitigungskosten. Bewertung ausdrücklich vorgeben.
- `mangelbeseitigungsanspruch`: Expliziter Wahrheitswert zum Anspruch des Bestellers auf Mangelbeseitigung im geprüften Fall.
- `abweichender_angemessener_betrag`: Optional: nichtnegative EUR-Dezimalzeichenfolge eines im Einzelfall rechtlich begründeten angemessenen Einbehalts anstelle des Regeldoppelbetrags. Ohne Abweichung NULL in R beziehungsweise None in Python.
- `abweichungsbegruendung`: Bei abweichendem Betrag erforderliche nichtleere Beschreibung der Einzelfallbewertung. Ohne abweichenden Betrag NULL in R beziehungsweise None in Python.

## Exakte Zahleneingaben

Für die als Dezimaltexte beschriebenen Eingaben sind auch exakte Bruchobjekte wie `{"zaehler": "1", "nenner": "3"}` zulässig, einschließlich solcher Felder in Listen. Zähler und Nenner sind kanonische Ganzzahlzeichenfolgen; der Nenner ist positiv. Fachliche Wertebereiche bleiben unverändert. Siehe [gemeinsamer Zahlenvertrag](../../fachkonzept/NUMERIK.md). Dadurch können passende Betragsfelder von Ergebnissen ohne Dezimalrundung weiterverwendet werden. Getrennte ganzzahlige Quotenzähler/-nenner, Anzahlen, Altersstufen und Datumsangaben behalten ihre bisherigen Typen.
