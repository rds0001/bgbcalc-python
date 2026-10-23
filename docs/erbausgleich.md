# Erbrechtliche Zuwendungsausgleichung

## erb_zuwendungen_ausgleichen

Zuwendungswerte zum Gruppennachlass hinzufügen und die Rechenmasse nach Gruppenquoten aufteilen. Ist bei einem Miterben der Zuwendungswert strikt größer als sein rechnerischer Anteil, diesen Miterben samt Zuwendung und Quote nach § 2056 herausnehmen. Mit den verbleibenden Quoten und Zuwendungen erneut rechnen, bis kein Überempfänger verbleibt. Dann jeweilige Zuwendung vom rechnerischen Anteil abziehen. Ausgeschlossene erhalten aus dieser Verteilung null; keine Herauszahlung des Mehrbetrags.

Die Funktion berechnet nur die Verteilung nach §§ 2055/2056 für bereits rechtlich bestimmte und bewertete Zuwendungen. Ausstattung, übermäßige Zuschüsse/Ausbildungskosten, ausdrückliche Ausgleichungsanordnung sowie Ausnahmen nach §§ 2050 bis 2054 sind vorab zu prüfen. Bei eintretenden Abkömmlingen muss insbesondere die Zurechnung nach § 2051 richtig bestimmt sein; nicht einfach denselben vollen Zuwendungsbetrag mehrfach eingeben. Gruppenquoten sind innerhalb der Gruppe normiert und nicht ohne Umrechnung mit den Gesamt-Erbquoten gleichzusetzen. Nicht beteiligte Ehegatten oder andere Erben werden nicht in die Gruppe aufgenommen. Keine kombinierte Ausgleichung besonderer Leistungen nach § 2057a, keine Pflichtteilsberechnung nach § 2316, keine Pflichtteilsergänzung und keine Rückforderung von Schenkungen. Technische Gruppengrenze 1000, keine gesetzliche Erbenobergrenze. Keine Rundung.

wert enthält verteilung mit person_id, exaktem EUR-Bruch betrag und Wahrheitswert ausser_ansatz für jeden eingegebenen Miterben. Die zusätzliche Liste ausser_ansatz enthält die ausgeschlossenen Kennungen. Beide Listen folgen der Eingabereihenfolge; die Rechenschritte dokumentieren die tatsächlichen Ausschlussrunden. Die Summe der ausgezahlten Beträge entspricht exakt dem Gruppennachlass. NICHT_ANWENDBAR mit wert null bei fehlendem Ausgleichungstatbestand.

- `gruppennachlass`: Nichtnegative EUR-Dezimalzeichenfolge des nach Berichtigung der Verbindlichkeiten verbleibenden Nachlasswerts, soweit er der Ausgleichungsgruppe zukommt. Anteile nicht beteiligter Erben vorher abgrenzen.
- `miterben`: Liste mit 1 bis 1000 Objekten mit genau person_id, erbquote_zaehler, erbquote_nenner und ausgleichungswert. person_id ist eine nichtleere eindeutige Zeichenfolge. Zähler und Nenner sind positive ganze Zahlen innerhalb NUMERIK.md; die Quoten beziehen sich auf die Ausgleichungsgruppe und müssen zusammen 1 ergeben. ausgleichungswert ist eine nichtnegative EUR-Dezimalzeichenfolge der dieser Person rechtlich zuzurechnenden, bewerteten ausgleichungspflichtigen Zuwendungen. In R eine Liste benannter Listen verwenden.
- `ausgleichung_anwendbar`: Expliziter Wahrheitswert zur rechtlich bestimmten Ausgleichungspflicht der Gruppe nach §§ 2050 ff., einschließlich gegebenenfalls des testamentarischen Falls nach § 2052.
- `bewertungsnachweis`: Nichtleere Beschreibung der Gruppenabgrenzung, Quoten, Zurechnung und Zuwendungsbewertung nach § 2055 Abs. 2 einschließlich erforderlicher Wertbereinigung.

Die unabhängige Gegenprüfung in `pruefungen/erbausgleich_orakel.py` untersucht alle verbleibenden Teilmengen kleiner Gruppen, statt Überempfänger wie die Bibliothek iterativ herauszunehmen. Sie ergänzt 25 manuell hergeleitete Fälle um 48 deterministische Orakelfälle.

## Exakte Zahleneingaben

Für die als Dezimaltexte beschriebenen Eingaben sind auch exakte Bruchobjekte wie `{"zaehler": "1", "nenner": "3"}` zulässig, einschließlich solcher Felder in Listen. Zähler und Nenner sind kanonische Ganzzahlzeichenfolgen; der Nenner ist positiv. Fachliche Wertebereiche bleiben unverändert. Siehe [gemeinsamer Zahlenvertrag](../../fachkonzept/NUMERIK.md). Dadurch können passende Betragsfelder von Ergebnissen ohne Dezimalrundung weiterverwendet werden. Getrennte ganzzahlige Quotenzähler/-nenner, Anzahlen, Altersstufen und Datumsangaben behalten ihre bisherigen Typen.

Die Unterscheidung zwischen geordneten Listen und Objekten sowie die zulässigen nativen R-Formen sind im [Strukturvertrag](../../fachkonzept/EINGABESTRUKTUREN.md) festgelegt.
