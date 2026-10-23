# Vorfälligkeitsentschädigung

## vorfaelligkeitsentschaedigung_betrag

Bei Allgemein-Verbraucherdarlehen min(unmittelbarer angemessener Schaden, 1 Prozent des vorzeitig gezahlten Betrags, verbleibende Sollzinsen); statt 1 Prozent nur 0,5 Prozent, wenn Zeitraum bis vereinbarter Rückzahlung höchstens ein Jahr beträgt. Bei Immobiliar-Verbraucherdarlehen keine Obergrenzen aus Abs. 3, sondern vorgegebene Schadensbewertung.

Gebundener Sollzinssatz zum Rückzahlungstag erforderlich; bei Allgemein-Verbraucherdarlehen bereits bei Vertragsschluss vereinbart. Ausschluss bei Rückzahlung aus vertraglich verpflichtend zur Rückzahlungssicherung abgeschlossener Versicherung oder unzureichenden Angaben über Laufzeit, Kündigungsrecht oder Berechnung der Vorfälligkeitsentschädigung. Eingeräumte Überziehung § 504 Abs. 1 und geduldete Überziehung § 505 Abs. 4 ausgeschlossen. Zulässige vorzeitige Erfüllung nach § 500 und Anwendbarkeit des Verbraucherdarlehensrechts sind vorab festgestellt; kein Kündigungsschadensrechner nach § 490. Unmittelbarer angemessener Schaden ist bewertete Nutzervorgabe, keine implementierte Aktiv-Aktiv-/Aktiv-Passiv-Schadensbewertung. Vereinbarte Rückzahlung bezeichnet den maßgeblichen Termin des vorzeitig zurückgezahlten Betrags. Keine automatische Berechnung verbleibender Sollzinsen oder Kostenminderung nach § 501.

- `vorzeitig_zurueckgezahlter_betrag`: Nichtnegative Dezimalzeichenfolge des vorzeitig zurückgezahlten Betrags in EUR.
- `unmittelbarer_schaden`: Nichtnegative Dezimalzeichenfolge des angemessenen, unmittelbar mit der vorzeitigen Rückzahlung zusammenhängenden Schadens. Bewertete Nutzervorgabe, keine automatisch berechnete Schadensgröße.
- `verbleibende_sollzinsen`: Nichtnegative Dezimalzeichenfolge der Sollzinsen, die zwischen vorzeitiger und vereinbarter Rückzahlung angefallen wären. Bei Immobiliardarlehen wird diese Obergrenze nicht angewendet.
- `rueckzahlungstag`: ISO-Datum der tatsächlichen vorzeitigen Rückzahlung.
- `vereinbarter_rueckzahlungstag`: ISO-Datum des maßgeblichen vereinbarten Rückzahlungstermins für den vorzeitig gezahlten Betrag; muss nach dem tatsächlichen Rückzahlungstag liegen.
- `darlehensart`: allgemein, immobiliar, eingeraeumte_ueberziehung oder geduldete_ueberziehung im Anwendungsbereich des Verbraucherdarlehensrechts.
- `gebundener_sollzins`: Expliziter Wahrheitswert: Werden zum Rückzahlungstag Zinsen zu einem gebundenen Sollzinssatz geschuldet?
- `bei_abschluss_gebunden`: Expliziter Wahrheitswert: Wurde der gebundene Sollzinssatz bereits bei Vertragsabschluss vereinbart? Nur bei Allgemein-Verbraucherdarlehen zusätzliche Voraussetzung.
- `versicherung_rueckzahlung`: Expliziter Wahrheitswert: Rückzahlung aus Mitteln einer Versicherung, die aufgrund entsprechender Verpflichtung im Darlehensvertrag zur Sicherung der Rückzahlung abgeschlossen wurde. Nicht jede Versicherungsleistung erfüllt den Ausschluss.
- `vertragsangaben_ausreichend`: Expliziter Wahrheitswert: Angaben zu Laufzeit, Kündigungsrecht und Berechnung der Vorfälligkeitsentschädigung sind ausreichend. Schon unzureichende Angaben in einem dieser Bereiche begründen den Ausschluss.

Die Jahresgrenze wird kalendarisch nach §§ 187/188 berechnet. Genau ein Jahr fällt unter 0,5 Prozent; am Schalttag beginnende Jahresfristen berücksichtigen § 188 Abs. 3. Keine automatische Cent-Rundung.

## Exakte Zahleneingaben

Für die als Dezimaltexte beschriebenen Eingaben sind auch exakte Bruchobjekte wie `{"zaehler": "1", "nenner": "3"}` zulässig, einschließlich solcher Felder in Listen. Zähler und Nenner sind kanonische Ganzzahlzeichenfolgen; der Nenner ist positiv. Fachliche Wertebereiche bleiben unverändert. Siehe [gemeinsamer Zahlenvertrag](../../fachkonzept/NUMERIK.md). Dadurch können passende Betragsfelder von Ergebnissen ohne Dezimalrundung weiterverwendet werden. Getrennte ganzzahlige Quotenzähler/-nenner, Anzahlen, Altersstufen und Datumsangaben behalten ihre bisherigen Typen.
