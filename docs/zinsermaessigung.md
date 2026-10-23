# Zinsvorteil bei Modernisierungsfinanzierung

## modernisierung_zinsermaessigung

Jahresbetrag der Zinsermäßigung = ursprünglicher Darlehensbetrag * (marktüblicher Jahreszinssatz minus ermäßigter Jahreszinssatz) / 100.

Teilstufe zur Anrechnung des Zinsvorteils nach § 559a Abs. 2/3, kein vollständiger Mieterhöhungsrechner und keine Tilgungsrechnung. Maßgeblich ist der ursprüngliche Darlehensbetrag, nicht eine sinkende Restschuld. Die Funktion berechnet weder öffentliche Kostenzuschüsse nach Absatz 1 noch Jahresbeträge von Zuschüssen oder Darlehen zur Deckung laufender Aufwendungen nach Absatz 2 Satz 4. Kostenverteilung auf Wohnungen, Kürzung des Erhöhungsbetrags, Kappungsgrenzen, Härte und Wirksamkeit sind gesonderte Schritte. Keine automatische Übertragung dieser Anrechnungsstufe in das abweichende Verfahren des § 559e. Negative eingegebene Zinssätze werden rechnerisch verarbeitet, sofern die ausdrückliche rechtliche Einordnung trägt und der Zinsabstand nicht negativ ist; keine Behauptung über tatsächliche Förderkonditionen.

wert ist der exakte EUR-Bruch des jährlichen Zinsvorteils, nicht eines Monatsbetrags. Ergebnisobjekt mit Quellenfassung, Eingaben, Nutzervorgaben und Rechenschritten. Bei NICHT_ANWENDBAR ist wert null. Keine Cent-Rundung.

- `darlehensursprungsbetrag`: Nichtnegative EUR-Dezimalzeichenfolge des der Wohnung zugeordneten ursprünglichen Darlehensbetrags. Nicht durch die laufende Restschuld ersetzen. Die Zuordnung nach § 559a Abs. 4 gegebenenfalls vorher berechnen.
- `ermaessigter_zinssatz_prozent`: Dezimalzeichenfolge des ermäßigten jährlichen Darlehenszinssatzes in Prozent. Bei zinslosem Darlehen "0". Darf den maßgeblichen Marktzinssatz nicht übersteigen.
- `marktueblicher_zinssatz_prozent`: Dezimalzeichenfolge des marktüblichen jährlichen Zinssatzes für erstrangige Hypotheken zum Zeitpunkt der Beendigung der Modernisierungsmaßnahmen, in Prozent. Keine automatische aktuelle Zinsreihe.
- `marktzinssatz_nachweis`: Nichtleere Herkunfts- und Stichtagsangabe des verwendeten Marktzinssatzes sowie erforderlichenfalls der Darlehenszuordnung.
- `beruecksichtigungsfaehiges_darlehen`: Expliziter Wahrheitswert zur rechtlichen Einordnung nach § 559a Abs. 2/3: entsprechendes öffentliches Darlehen oder gleichgestellte Finanzierung. Keine automatische Bewertung von Mieterdarlehen, Mietvorauszahlungen oder Drittleistungen.
- `vereinfachtes_verfahren`: Expliziter Wahrheitswert, ob § 559c anwendbar ist. Dort sind § 559a Abs. 2 Sätze 1 bis 3 nicht anzuwenden; die Funktion liefert deshalb NICHT_ANWENDBAR.

## Exakte Zahleneingaben

Für die als Dezimaltexte beschriebenen Eingaben sind auch exakte Bruchobjekte wie `{"zaehler": "1", "nenner": "3"}` zulässig, einschließlich solcher Felder in Listen. Zähler und Nenner sind kanonische Ganzzahlzeichenfolgen; der Nenner ist positiv. Fachliche Wertebereiche bleiben unverändert. Siehe [gemeinsamer Zahlenvertrag](../../fachkonzept/NUMERIK.md). Dadurch können passende Betragsfelder von Ergebnissen ohne Dezimalrundung weiterverwendet werden. Getrennte ganzzahlige Quotenzähler/-nenner, Anzahlen, Altersstufen und Datumsangaben behalten ihre bisherigen Typen.
