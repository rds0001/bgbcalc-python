# Kappungsgrenzen bei Modernisierung

## modernisierung_kappungsgrenze

Allgemeine Restgrenze pro Monat = max(Wohnfläche * 2 Euro bei vorheriger Quadratmetermiete unter 7 Euro, sonst Wohnfläche * 3 Euro, minus bereits berücksichtigte monatliche Gesamterhöhungen, 0). Bei qualifiziertem Heizungsfall zusätzlich Heizungsrestgrenze = max(Wohnfläche * 0,50 Euro minus bisherige monatliche Heizungssteigerungen, 0); maßgeblich ist das Minimum beider Restgrenzen.

Nur rechnerische Restgrenzen nach § 559 Abs. 3a beziehungsweise § 559e Abs. 3. Sechsjahreszeitraum, Einbeziehung früherer Erhöhungen und der rechtlich maßgebliche Miet-/Flächenbegriff sind vorab festzustellen; keine automatische Datums- oder Änderungshistorie. Vorherige Heizungssteigerungen gehören auch in die allgemeine Gesamterhöhung. Für andere Maßnahmen sperrt eine erschöpfte Heizungsgrenze nicht automatisch den allgemeinen Rest. Die Restgrenze ist kein bereits zulässiger Mieterhöhungsbetrag: Kostenbasis, Erhaltungsanteile, Drittmittel, Acht-/Zehnprozentrechnung, Härteeinwand, Erklärung und Wirksamkeitszeitpunkt sind gesonderte Schritte. Keine negativen Erhöhungen oder Rückzahlungsansprüche bei früherer Grenzüberschreitung. Keine automatische Übertragung auf nicht erfasste Fälle.

wert enthält allgemeine_restgrenze, heizungs_restgrenze und massgebliche_restgrenze als exakte EUR-Brüche für den monatlichen Erhöhungsbetrag der gesamten Wohnung. heizungs_restgrenze ist im allgemeinen Fall null. Bei NICHT_ANWENDBAR ist der gesamte wert null. Keine Cent-Rundung.

- `wohnflaeche`: Positive Dezimalzeichenfolge der rechtlich maßgeblichen Wohnfläche in Quadratmetern. Keine automatische Flächenberechnung oder Rundung.
- `monatliche_miete_je_quadratmeter`: Nichtnegative EUR-Dezimalzeichenfolge der maßgeblichen monatlichen Miete je Quadratmeter unmittelbar vor der geprüften Erhöhung. Strikt unter 7 Euro gilt die Zwei-Euro-Grenze; bei genau 7 Euro gilt die Drei-Euro-Grenze. Mietbestandteile rechtlich vorab abgrenzen.
- `bisherige_monatliche_erhoehung_gesamt`: Nichtnegative EUR-Dezimalzeichenfolge der im einschlägigen Sechsjahreszeitraum bereits zu berücksichtigenden monatlichen Mieterhöhungsbeträge für die gesamte Wohnung. Erhöhungen nach §§ 558 und 560 nicht einbeziehen. Heizungsbeträge sind enthalten. Kein Jahresbetrag und kein kumulierter Zahlungsbetrag.
- `bisherige_monatliche_heizungserhoehung`: Nichtnegative EUR-Dezimalzeichenfolge des innerhalb desselben Zeitraums auf die zusätzliche Heizungsgrenze anzurechnenden monatlichen Erhöhungsbetrags der gesamten Wohnung. Dieser Teilbetrag darf die berücksichtigte Gesamterhöhung nicht übersteigen.
- `erhoehungsart`: allgemein für die allgemeine Grenze; heizung_559 für eine nach § 559 Abs. 1 berechtigte Heizungsmaßnahme mittels Einbau/Aufstellung zur Inbetriebnahme, die zugleich § 555b Nr. 1 oder 1a erfüllt; heizung_559e für den Fall des § 559e Abs. 3. Nicht jede Heizungsmaßnahme automatisch der Sondergrenze zuordnen.
- `kappungsregel_anwendbar`: Expliziter Wahrheitswert zur rechtlich ausgewählten Anwendung der Kappungsregel in der festen Quellenfassung, einschließlich gegebenenfalls einschlägiger Verweis- und Übergangsregeln.

## Exakte Zahleneingaben

Für die als Dezimaltexte beschriebenen Eingaben sind auch exakte Bruchobjekte wie `{"zaehler": "1", "nenner": "3"}` zulässig, einschließlich solcher Felder in Listen. Zähler und Nenner sind kanonische Ganzzahlzeichenfolgen; der Nenner ist positiv. Fachliche Wertebereiche bleiben unverändert. Siehe [gemeinsamer Zahlenvertrag](../../fachkonzept/NUMERIK.md). Dadurch können passende Betragsfelder von Ergebnissen ohne Dezimalrundung weiterverwendet werden. Getrennte ganzzahlige Quotenzähler/-nenner, Anzahlen, Altersstufen und Datumsangaben behalten ihre bisherigen Typen.
