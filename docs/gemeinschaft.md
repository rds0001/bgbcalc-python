# Lasten und Kosten der Bruchteilsgemeinschaft

## gemeinschaft_lastenanteile

Der Lasten- oder Kostenbetrag wird mit dem jeweiligen Teilhaberanteil multipliziert. Bei ausdrücklich ausgewählter Zweifelsregel nach § 742 erhält jeder Teilhaber den Anteil 1/Anzahl der Teilhaber.

Abgegrenzte Kostenverteilung nach § 748 innerhalb einer Bruchteilsgemeinschaft. Rechtsgrund, Erstattungsfähigkeit, wirksame abweichende Regelungen und einschlägiges Sonderrecht sind vorab zu prüfen. Keine automatische Beschlussprüfung oder Berechnung von Ansprüchen aus einer eigenmächtigen Maßnahme. Die Funktion verteilt den vorgegebenen Gesamtbetrag, bestimmt aber keinen bereits durch Zahlung ausgelösten Ausgleichsanspruch und verrechnet keine Vorleistungen. Kein WEG-Abrechnungsautomat. Technische Gruppengrenze 1000, keine gesetzliche Obergrenze. Zwei Teilhaber mindestens, weil eine Gemeinschaft mehrerer vorausgesetzt ist.

wert ist eine Liste in Eingabereihenfolge mit person_id, anteil und betrag. Anteil und EUR-Betrag sind exakte Brüche als zaehler/nenner-Ganzzahlzeichenfolgen. Die Beträge ergeben zusammen den Gesamtbetrag; keine Cent-Rundung. Bei NICHT_ANWENDBAR ist wert null.

- `gesamtbetrag`: Nichtnegative EUR-Dezimalzeichenfolge der für § 748 rechtlich maßgeblichen Lasten oder Kosten. Nur gemeinschaftliche Lasten und Kosten der Erhaltung, Verwaltung oder gemeinschaftlichen Benutzung einbeziehen.
- `teilhaber`: Liste mit 2 bis 1000 Objekten mit genau person_id, anteil_zaehler und anteil_nenner. Kennungen nichtleer und eindeutig. Bei vorgegebenen Anteilen sind Zähler und Nenner positive ganze Zahlen innerhalb NUMERIK.md und die Anteile summieren sich zu 1. Bei ausdrücklich gewählter Zweifelsregel beide Anteilsfelder jedes Teilhabers NULL in R beziehungsweise None in Python. In R eine Liste benannter Listen verwenden.
- `gleiche_anteile_im_zweifel`: Expliziter Wahrheitswert, ob die Zweifelsregel gleicher Anteile nach § 742 für diesen Fall ausgewählt ist. Kein stillschweigender Ersatz für fehlende Angaben zu bekannten Anteilen.
- `gemeinschaft_nach_bruchteilen`: Expliziter Wahrheitswert zur rechtlichen Einordnung nach § 741 einschließlich der Prüfung vorrangiger gesetzlicher Sonderregeln.

## Exakte Zahleneingaben

Für die als Dezimaltexte beschriebenen Eingaben sind auch exakte Bruchobjekte wie `{"zaehler": "1", "nenner": "3"}` zulässig, einschließlich solcher Felder in Listen. Zähler und Nenner sind kanonische Ganzzahlzeichenfolgen; der Nenner ist positiv. Fachliche Wertebereiche bleiben unverändert. Siehe [gemeinsamer Zahlenvertrag](../../fachkonzept/NUMERIK.md). Dadurch können passende Betragsfelder von Ergebnissen ohne Dezimalrundung weiterverwendet werden. Getrennte ganzzahlige Quotenzähler/-nenner, Anzahlen, Altersstufen und Datumsangaben behalten ihre bisherigen Typen.

Die Unterscheidung zwischen geordneten Listen und Objekten sowie die zulässigen nativen R-Formen sind im [Strukturvertrag](../../fachkonzept/EINGABESTRUKTUREN.md) festgelegt.
