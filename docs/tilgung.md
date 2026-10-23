# Zahlungsanrechnung

Die Funktionen setzen eine bereits ausgewählte Schuld voraus. Die Bestimmung unter mehreren Schulden nach § 366 ist davon zu unterscheiden. Die Beträge werden exakt ohne Cent-Rundung zugeordnet.

## zahlung_anrechnen

Zahlung nacheinander auf Kosten, Zinsen und Hauptforderung bis zur jeweiligen Höhe anrechnen; Überschuss gesondert ausweisen. Bei angenommener abweichender Bestimmung eingegebene Reihenfolge verwenden.

Einzelne Schuld bereits ausgewählt, § 366 gesondert. Abweichende Bestimmung bildet hier eine Reihenfolge, keine beliebige Betragsbestimmung. Ablehnung einer tatsächlich abweichenden Bestimmung führt zu NICHT_ANWENDBAR. Ablehnung ohne Abweichung ist für diesen Eingabevertrag ungültig. Keine Aussage zu anderen Ablehnungsgründen oder Spezialregeln.

wert: zuordnungen als geordnete Liste mit position, betrag, restforderung; nicht_zugeordnet als Überschuss. Alle Beträge exakte EUR-Brüche. Keine implizite Erstattung des Überschusses.

- `zahlung`: Nichtnegative Dezimalzeichenfolge der geleisteten Zahlung in EUR.
- `kosten`: Nichtnegative Dezimalzeichenfolge der geschuldeten Kosten in EUR.
- `zinsen`: Nichtnegative Dezimalzeichenfolge der geschuldeten Zinsen in EUR.
- `hauptforderung`: Nichtnegative Dezimalzeichenfolge der Hauptforderung in EUR.
- `abweichende_reihenfolge`: Optional eine geordnete Liste der Positionen kosten, zinsen, hauptforderung, jede genau einmal. In R auch Zeichenvektor. None bedeutet gesetzliche Reihenfolge. Die Bestimmung muss bei Leistung getroffen worden sein.
- `annahme_abgelehnt`: Expliziter Wahrheitswert, ob der Gläubiger die abweichend bestimmte Leistung abgelehnt hat. TRUE setzt tatsächliche Abweichung voraus.

## verbraucherdarlehen_zahlung_anrechnen

Zuerst Rechtsverfolgungskosten, dann übriger geschuldeter Betrag nach § 497 Abs. 1, zuletzt gesonderte Zinsen nach Abs. 2. Teilzahlungen werden rechnerisch vollständig in dieser Reihenfolge eingesetzt.

Verbraucherdarlehensrechtliche Zuordnung einschließlich § 513 vorausgesetzt. Übriger geschuldeter Betrag umfasst insbesondere die geschuldeten Vertragsleistungen, nicht nur ursprüngliches Kapital; keine Doppelzählung der gesonderten Verzugszinsen. Bei Immobiliar-Verbraucherdarlehen, Titel mit Zinsen als Hauptforderung oder fehlendem Verzug NICHT_ANWENDBAR. Teilzahlungen dürfen im Anwendungsbereich nicht zurückgewiesen werden. Verjährung und Schadensersatz wegen Zinsverzugs sind gesonderte Regeln.

wert: zuordnungen als geordnete Liste mit position, betrag, restforderung; nicht_zugeordnet als Überschuss. Alle Beträge exakte EUR-Brüche. Keine implizite Erstattung des Überschusses.

- `zahlung`: Nichtnegative Dezimalzeichenfolge der geleisteten Zahlung in EUR.
- `rechtsverfolgungskosten`: Nichtnegative Dezimalzeichenfolge der geschuldeten Rechtsverfolgungskosten in EUR.
- `uebriger_geschuldeter_betrag`: Nichtnegative Dezimalzeichenfolge des übrigen fälligen geschuldeten Betrags nach § 497 Abs. 1. Einschließlich einschlägiger Vertragsleistungen; gesonderte Verzugszinsen nicht doppelt erfassen.
- `verzugszinsen`: Nichtnegative Dezimalzeichenfolge der gesondert erfassten Zinsen nach § 497 Abs. 2.
- `immobiliar_verbraucherdarlehen`: Expliziter Wahrheitswert zur rechtlichen Einordnung als Immobiliar-Verbraucherdarlehen.
- `titel_hauptforderung_zinsen`: Expliziter Wahrheitswert, ob die Zahlung auf einen Vollstreckungstitel erfolgt, dessen Hauptforderung auf Zinsen lautet.
- `schuldnerverzug`: Expliziter Wahrheitswert zum Schuldnerverzug im Anwendungsbereich des § 497.

## Exakte Zahleneingaben

Für die als Dezimaltexte beschriebenen Eingaben sind auch exakte Bruchobjekte wie `{"zaehler": "1", "nenner": "3"}` zulässig, einschließlich solcher Felder in Listen. Zähler und Nenner sind kanonische Ganzzahlzeichenfolgen; der Nenner ist positiv. Fachliche Wertebereiche bleiben unverändert. Siehe [gemeinsamer Zahlenvertrag](../../fachkonzept/NUMERIK.md). Dadurch können passende Betragsfelder von Ergebnissen ohne Dezimalrundung weiterverwendet werden. Getrennte ganzzahlige Quotenzähler/-nenner, Anzahlen, Altersstufen und Datumsangaben behalten ihre bisherigen Typen.

Die Unterscheidung zwischen geordneten Listen und Objekten sowie die zulässigen nativen R-Formen sind im [Strukturvertrag](../../fachkonzept/EINGABESTRUKTUREN.md) festgelegt.


Für die entsprechende Nutzungsanrechnung nach §1214II/III ist `zahlung` der rechtlich bestimmte Reinertrag. Gewinnungskosten nicht nochmals als Forderungskosten abziehen. Eine wirksam vereinbarte andere Reihenfolge kann ausdrücklich vorgegeben werden; `annahme_abgelehnt=False`, da der Ablehnungsmechanismus nach §367II hier nicht übertragen wird. Sieben zusätzliche Normanwendungsfälle dokumentiert in `fachkonzept/pfandnutzungsanrechnung.json`. Quellenanker: BGB_1214_T0002, BGB_1214_T0003.

## Numerische Tilgungsreste nach §§362,378,421,422,428

Numerische Normanwendung362/378/421/422/428: bereits qualifizierte wirksame Geldbefriedigung einer konkret ausgewählten Schuld; bei378 nur Geldhinterlegung mit ausgeschlossener Rücknahme. Bei Gesamtschuld/Gesamtgläubigern den gemeinsamen Außenrest einmal fortschreiben, nicht für jede Person eine neue Vollforderung anlegen. Beispielbelege ohne Kosten/Zinsen; annahme_abgelehnt stetsFALSE, keine Übertragung eines Zahlungsablehnungsrechts auf andere Erlöschensakte. Andere Befriedigungsarten und Innenausgleich separat; Aufrechnung389 mit aufrechnung_betragswirkung behandeln. Siehe fachkonzept/tilgungsreste_normanwendung.json.

## Numerischer Forderungsübergang nach §268III

§268III: numerischer Teilbeleg einer bereits qualifizierten Ablösung einer einzelnen Geldhauptforderung ohne Kosten/Zinsen. Der bei zahlung_anrechnen der hauptforderung zugeordnete Betrag wird hier als übergegangener Forderungsbetrag gelesen, NICHT als Erlöschen der Schuld gegenüber dem Schuldner. restforderung bezeichnet den beim bisherigen Gläubiger verbleibenden Betrag; beide Forderungsteile bestehen zusammen in ursprünglicher Höhe. Nicht zugeordneter Überschuss ist kein zusätzlicher Forderungsübergang und kein automatisch begründeter Erstattungsanspruch. Ablösungsberechtigung, wirksame Befriedigung gemäß268I/II und Schutz des bisherigen Gläubigers268III2 separat qualifiziert. annahme_abgelehnt=FALSE ist nur der verwendete numerische Rechenmodus, keine Aussage über ein Ablehnungsrecht. Keine automatische Verteilung mehrerer Sicherheiten oder Gläubiger.
