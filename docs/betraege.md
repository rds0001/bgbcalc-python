# Sicherheitswerte und Sachschaden

Alle Beträge werden als Dezimalzeichenfolgen in EUR eingegeben. Ausgaben sind exakte Brüche als `wert = {"zaehler": "…", "nenner": "…"}`; es erfolgt keine automatische Cent-Rundung. Die gemeinsame Zahlenbasis und ihre Überlaufgrenzen stehen in `fachkonzept/NUMERIK.md`.

`NICHT_ANWENDBAR` hat `wert = null` beziehungsweise `NULL` und bedeutet keinen errechneten Nullbetrag. Fehlende Eingaben erzeugen `EINGABE_FEHLT`, ungültige Werte `EINGABE_UNGUELTIG`, jeweils als strukturierter Fehler. Die Funktionen entscheiden nur die dokumentierten Voraussetzungen und Betragsoperationen.

## sachschaden_ersatzbetrag

`sachschaden_ersatzbetrag(erforderlicher_nettobetrag, ersatzfaehige_angefallene_umsatzsteuer, mitverschuldensquote)`

(erforderlicher_nettobetrag + ersatzfaehige_angefallene_umsatzsteuer) * (1-mitverschuldensquote). Nettobetrag und Umsatzsteuer müssen überschneidungsfrei sein; Steuer nur soweit tatsächlich angefallen und vom erforderlichen Herstellungsaufwand umfasst. Quote als rechtlich bewertete Eingabe, keine eigene Abwägungsformel.

- `erforderlicher_nettobetrag`: Nichtnegative Dezimalzeichenfolge in EUR des als erforderlich bewerteten Herstellungsaufwands ohne Umsatzsteuer, keine doppelte Erfassung derselben Position.
- `ersatzfaehige_angefallene_umsatzsteuer`: Nichtnegative Dezimalzeichenfolge in EUR ausschließlich der tatsächlich angefallenen und vom erforderlichen Herstellungsaufwand umfassten Umsatzsteuer; bei fiktiver Abrechnung null. Keine automatische Steuerermittlung.
- `mitverschuldensquote`: Rechtlich bewertete Dezimalzeichenfolge von 0 bis 1. 0.25 bedeutet 25 Prozent; die Library führt keine eigene Abwägung nach § 254 durch.

Regel-ID: `BGB_SACHSCHADEN_BETRAG`. Quellenanker: BGB_249_T0001, BGB_249_T0002, BGB_249_T0003, BGB_254_T0001, BGB_254_T0002, BGB_254_T0003.

## buchforderung_sicherheitswert

`buchforderung_sicherheitswert(kurswert, schuldnerart)`

Kurswert der gegen Löschung auszuhändigenden Papiere * 3/4. Nur Schuldbuchforderung gegen Bund oder Land; sonst NICHT_ANWENDBAR.

- `kurswert`: Nichtnegative Dezimalzeichenfolge in EUR. Bei Buchforderung Kurswert der gegen Löschung auszuhändigenden Wertpapiere, nicht Forderungsnominalwert.
- `schuldnerart`: bund, land oder sonstiges. Die Funktion setzt eine Schuldbuchforderung der bezeichneten Art voraus.

Regel-ID: `BGB_SICHERHEIT_BUCHFORDERUNG`. Quellenanker: BGB_236_T0001.

## sicherheit_ergaenzungsbetrag

`sicherheit_ergaenzungsbetrag(erforderliche_sicherheit, vorhandener_sicherheitswert, verschulden_berechtigter)`

Bei fehlendem Verschulden des Berechtigten max(erforderliche_sicherheit-vorhandener_sicherheitswert,0). Bei Verschulden NICHT_ANWENDBAR für diese Norm, keine Aussage zu anderen Anspruchsgrundlagen.

- `erforderliche_sicherheit`: Nichtnegative Dezimalzeichenfolge in EUR des erforderlichen Sicherungsbetrags.
- `vorhandener_sicherheitswert`: Nichtnegative Dezimalzeichenfolge in EUR des bereits nach einschlägigen Regeln bewerteten Sicherungswerts; nicht ungeprüfter Nominalwert.
- `verschulden_berechtigter`: Expliziter Wahrheitswert, ob der Berechtigte die unzureichende Sicherheit verschuldet hat. Bei wahr ist § 240 in diesem Vertrag nicht anwendbar.

Regel-ID: `BGB_SICHERHEIT_ERGAENZUNG`. Quellenanker: BGB_240_T0001.

## sach_sicherheitswert

`sach_sicherheitswert(schaetzungswert, verderb_zu_besorgen, aufbewahrung_schwierig, zurueckweisung_erklaert)`

Schätzungswert * 2/3. Verderbsbesorgnis oder schwierige Aufbewahrung ermöglichen Zurückweisung, bewirken sie nicht automatisch. Bei darauf gestützter erklärter Zurückweisung NICHT_ANWENDBAR; Zurückweisung ohne angegebenen gesetzlichen Grund EINGABE_UNGUELTIG.

- `schaetzungswert`: Nichtnegative Dezimalzeichenfolge in EUR, vom Nutzer bereitgestellter Schätzungswert; keine automatische Schätzung.
- `verderb_zu_besorgen`: Expliziter Wahrheitswert einer rechtlich bewerteten Verderbsbesorgnis.
- `aufbewahrung_schwierig`: Expliziter Wahrheitswert besonderer Aufbewahrungsschwierigkeiten, nicht beliebiger Lagerkosten.
- `zurueckweisung_erklaert`: Expliziter Wahrheitswert der tatsächlichen Zurückweisung aus einem der beiden genannten gesetzlichen Gründe. Ein Grund allein bewirkt noch keine Zurückweisung.

Regel-ID: `BGB_SICHERHEIT_SACHE`. Quellenanker: BGB_237_T0001, BGB_237_T0002.

## wertpapier_sicherheitswert

`wertpapier_sicherheitswert(kurswert, papierart, gattung_zulaessig, scheine_hinterlegt, gattungsnachweis)`

Bei zulässigem Inhaberpapier oder blankoindossiertem Orderpapier, zugelassener Gattung und mit hinterlegten zugehörigen Scheinen: Kurswert * 3/4. Andernfalls NICHT_ANWENDBAR ohne Wert.

- `kurswert`: Nichtnegative Dezimalzeichenfolge in EUR. Bei Buchforderung Kurswert der gegen Löschung auszuhändigenden Wertpapiere, nicht Forderungsnominalwert.
- `papierart`: inhaberpapier, blanko_orderpapier oder sonstiges. Nur die ersten beiden Arten erfüllen die Papierartvoraussetzung.
- `gattung_zulaessig`: Expliziter Wahrheitswert zur Zulässigkeit der Gattung nach der Verordnung zu § 240a. Diese externe Einordnung wird nicht von der Library ermittelt.
- `scheine_hinterlegt`: Expliziter Wahrheitswert: zugehörige Zins-, Renten-, Gewinnanteil- und Erneuerungsscheine sind mit hinterlegt.
- `gattungsnachweis`: Nichtleere Herkunfts-/Versionsangabe der externen Gattungseinordnung.

Regel-ID: `BGB_SICHERHEIT_WERTPAPIER`. Quellenanker: BGB_234_T0001, BGB_234_T0002, BGB_234_T0003, BGB_240a_T0001, BGB_240a_T0002, BGB_240a_T0003, BGB_240a_T0004.

## Exakte Zahleneingaben

Für die als Dezimaltexte beschriebenen Eingaben sind auch exakte Bruchobjekte wie `{"zaehler": "1", "nenner": "3"}` zulässig, einschließlich solcher Felder in Listen. Zähler und Nenner sind kanonische Ganzzahlzeichenfolgen; der Nenner ist positiv. Fachliche Wertebereiche bleiben unverändert. Siehe [gemeinsamer Zahlenvertrag](../../fachkonzept/NUMERIK.md). Dadurch können passende Betragsfelder von Ergebnissen ohne Dezimalrundung weiterverwendet werden. Getrennte ganzzahlige Quotenzähler/-nenner, Anzahlen, Altersstufen und Datumsangaben behalten ihre bisherigen Typen.
