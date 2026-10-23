# Pflichtteilsbeträge

Diese Funktionen bilden abgegrenzte Berechnungsstufen ab. Sie ersetzen weder die Feststellung der Berechtigung noch eine vollständige Pflichtteilsergänzungs- oder Ausgleichungsrechnung. Geldwerte sind Dezimalzeichenfolgen; Ergebnisse bleiben exakte Brüche.

## pflichtteil_betrag

Pflichtteilsquote = gesetzliche Erbquote/2. Ohne Anrechnung max(Nettopflichtteilsnachlass,0)*Pflichtteilsquote. Bei wirksamer Bestimmung nach § 2315 erst Anrechnungswert zum Nachlass addieren, dann Pflichtteilsquote anwenden, danach gesamten Anrechnungswert abziehen; Ergebnis mindestens null.

Gesetzliche Erbquote für Pflichtteilszwecke gesondert nach § 2310 bestimmen: Ausgeschlossene, Ausschlagende und Erbunwürdige mitzählen, Erbverzichtende nicht. Tatsächliche Erbquote ist nicht ohne Weiteres maßgebend. Berechtigung umfasst Stellung nach § 2303 und Ausschluss nach § 2309 sowie weitere rechtliche Ausschlüsse. Nachlasswerte zum Erbfall; für Abkömmlinge/Eltern gebührenden Voraus außer Ansatz lassen. Anrechnungswerte zum Zuwendungszeitpunkt einschließlich erforderlicher Bewertungsbereinigung vorgeben; Bestimmung muss rechtlich wirksam sein. Mehrere Zuwendungen und § 2315 Abs. 3/§ 2051-Zurechnung vorab rechtlich abgrenzen. Kombination mit Ausgleichung § 2316 und Pflichtteilsergänzung §§ 2325 ff. sind gesonderte Rechenregeln; insbesondere § 2316 Abs. 4 nicht mit vollem §-2315-Abzug behandeln.

Ergebnisobjekt mit wert als zaehler/nenner-Ganzzahlzeichenfolgen, einheit EUR, Regel- und Quellenfassung, Eingaben, Nutzervorgaben und Rechenschritten. Bei NICHT_ANWENDBAR ist wert null. Fehlende oder ungültige Eingaben erzeugen einen strukturierten Berechnungsfehler.

- `pflichtteilsnachlass`: Signierte EUR-Dezimalzeichenfolge des bewerteten Nettopflichtteilsnachlasses zum Erbfall; keine automatische Bewertung oder Ermittlung abzugsfähiger Verbindlichkeiten.
- `gesetzliche_erbquote_zaehler`: Nichtnegative ganze Zahl, Zähler der für Pflichtteilszwecke nach § 2310 gesondert bestimmten gesetzlichen Erbquote.
- `gesetzliche_erbquote_nenner`: Positive ganze Zahl, Nenner der gesetzlichen Erbquote. Quote zwischen 0 und 1; technische Grenzen gemäß NUMERIK.md.
- `anrechnungswert`: Nichtnegative EUR-Dezimalzeichenfolge der nach § 2315 bewerteten Zuwendung; ohne Zuwendung ausdrücklich "0" eingeben.
- `anrechnungsbestimmung`: Expliziter Wahrheitswert, ob eine rechtlich wirksame Anrechnungsbestimmung vorliegt. Bei False wird der eingegebene Anrechnungswert nicht berücksichtigt.
- `pflichtteilsberechtigt`: Expliziter Wahrheitswert für die rechtlich vorab geprüfte Berechtigung im gewählten Fall. False ergibt NICHT_ANWENDBAR.
- `bewertungsnachweis`: Nichtleere Zeichenfolge mit Nachweis der verwendeten Nachlass- und Zuwendungsbewertungen sowie der maßgeblichen Quote.

## zusatzpflichtteil_betrag

Zusatzpflichtteil = max(Pflichtteilsbetrag - Wert des hinterlassenen Erbteils, 0).

Berechnungsstufe bei hinterlassenem Erbteil nach § 2305 bzw. § 2316 Abs. 2. Pflichtteilsbetrag muss bereits nach den einschlägigen Regeln einschließlich gegebenenfalls Ausgleichungen bestimmt sein. Beschränkungen/Beschwerungen nach § 2306 beim Erbteilwert nicht abziehen. Kein automatisches Ausschlagungsrecht, keine Ausschlagungsfrist und keine Entscheidung über gleichzeitige Vermächtnisse.

Ergebnisobjekt mit wert als zaehler/nenner-Ganzzahlzeichenfolgen, einheit EUR, Regel- und Quellenfassung, Eingaben, Nutzervorgaben und Rechenschritten. Bei NICHT_ANWENDBAR ist wert null. Fehlende oder ungültige Eingaben erzeugen einen strukturierten Berechnungsfehler.

- `pflichtteilsbetrag`: Nichtnegative EUR-Dezimalzeichenfolge des nach den einschlägigen Vorschriften bereits bestimmten Pflichtteilsbetrags.
- `unbeschwerter_erbteilwert`: Nichtnegative EUR-Dezimalzeichenfolge des hinterlassenen Erbteilwerts ohne Abzug der Beschränkungen und Beschwerungen nach § 2306.
- `pflichtteilsberechtigt`: Expliziter Wahrheitswert für die rechtlich vorab geprüfte Berechtigung im gewählten Fall. False ergibt NICHT_ANWENDBAR.

## pflichtteil_vermaechtnisrest

Bei rechtlich wirksamer Ausschlagung des Vermächtnisses voller vorgegebener Pflichtteilsbetrag; sonst max(Pflichtteilsbetrag - Vermächtniswert, 0).

Ausschlagungsstatus einschließlich möglicher Fiktion nach § 2307 Abs. 2 vorab rechtlich feststellen; Funktion berechnet keine Fristen. Vermächtniswert ohne Beschränkungen/Beschwerungen der in § 2306 bezeichneten Art. Kein universeller Rechner für gleichzeitige Erbeinsetzung und Vermächtnisse, keine Ausschlagung der Erbschaft unterstellen.

Ergebnisobjekt mit wert als zaehler/nenner-Ganzzahlzeichenfolgen, einheit EUR, Regel- und Quellenfassung, Eingaben, Nutzervorgaben und Rechenschritten. Bei NICHT_ANWENDBAR ist wert null. Fehlende oder ungültige Eingaben erzeugen einen strukturierten Berechnungsfehler.

- `pflichtteilsbetrag`: Nichtnegative EUR-Dezimalzeichenfolge des nach den einschlägigen Vorschriften bereits bestimmten Pflichtteilsbetrags.
- `unbeschwerter_vermaechtniswert`: Nichtnegative EUR-Dezimalzeichenfolge des Vermächtniswerts ohne Abzug der Beschränkungen und Beschwerungen nach § 2306.
- `vermaechtnis_ausgeschlagen`: Expliziter Wahrheitswert zur rechtlich wirksamen Ausschlagung des Vermächtnisses einschließlich gegebenenfalls der Fiktion nach § 2307 Abs. 2.
- `pflichtteilsberechtigt`: Expliziter Wahrheitswert für die rechtlich vorab geprüfte Berechtigung im gewählten Fall. False ergibt NICHT_ANWENDBAR.

## Exakte Zahleneingaben

Für die als Dezimaltexte beschriebenen Eingaben sind auch exakte Bruchobjekte wie `{"zaehler": "1", "nenner": "3"}` zulässig, einschließlich solcher Felder in Listen. Zähler und Nenner sind kanonische Ganzzahlzeichenfolgen; der Nenner ist positiv. Fachliche Wertebereiche bleiben unverändert. Siehe [gemeinsamer Zahlenvertrag](../../fachkonzept/NUMERIK.md). Dadurch können passende Betragsfelder von Ergebnissen ohne Dezimalrundung weiterverwendet werden. Getrennte ganzzahlige Quotenzähler/-nenner, Anzahlen, Altersstufen und Datumsangaben behalten ihre bisherigen Typen.
