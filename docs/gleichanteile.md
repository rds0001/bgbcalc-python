# Gleichanteile bei teilbaren Leistungen und Gesamtgläubigern

## teilbare_leistung_gleichanteil

Bei teilbarer Leistung und anwendbarer Zweifelsregel: Anteilsquote=1geteilt durch Anzahl der beteiligten Schuldner beziehungsweise Gläubiger; Leistungsanteil=Gesamtleistung mal Anteilsquote.

Nur Zweifelsregel für Teilschuld beziehungsweise Teilforderung nach §420. Keine Gesamtschuld, Gesamtgläubigerschaft, gemeinschaftliche Gläubigerschaft oder automatische Vertragsauslegung. Jede Person erhält hier den gleichen rechnerischen Anteil; bereits erbrachte Zahlungen, Einwendungen und abweichende Quoten sind gesondert. Bezifferte Mengen sind keine automatische Anordnung, eine physisch unteilbare Sache zu zerteilen.

wert enthält anteilsquote als exakten dimensionslosen Bruch und leistungsanteil als exakten Bruch in leistungseinheit. Bei NICHT_ANWENDBAR ist wert null. Keine automatische Rundung; Nutzerangaben einschließlich Einheit bleiben im Ergebnis sichtbar.

- `gesamtleistung`: Nichtnegative Dezimalzeichenfolge oder exaktes Bruchobjekt mit zaehler/nenner nach NUMERIK.md. Bezifferte Gesamtleistung in der gesondert angegebenen Einheit; keine automatische Bewertung oder Umrechnung.
- `anzahl_beteiligte`: Ganzzahl zwischen 2 und 9007199254740991. Gezählt werden ausschließlich die Personen auf der aufzuteilenden Seite; die Gegenpartei nicht mitzählen. Keine Anzahl verschiedener Ansprüche oder Leistungsteile.
- `leistungseinheit`: Nichtleere Zeichenfolge der gemeinsamen Leistungseinheit, beispielsweise EUR oder kg. Wird als Ergebniseinheit übernommen; keine Umrechnung und keine automatische Cent- oder Stückrundung. Physische Teilbarkeit und rechtliche Einordnung bleiben gesonderte Tatsachen.
- `rollenart`: Auswahl teilschuld oder teilforderung. Im ersten Fall sind Schuldner zu zählen, im zweiten Gläubiger. Keine Auswahl einer Gesamtschuld oder Gesamtgläubigerschaft nach anderen Vorschriften.
- `leistung_teilbar`: Expliziter Wahrheitswert zur Teilbarkeit der Leistung. FALSE ergibt NICHT_ANWENDBAR.
- `gleichanteilsvermutung_anwendbar`: Expliziter Wahrheitswert zur Zweifelsregel des § 420: keine vorrangige abweichende Zuordnung oder andere Haftungs-/Berechtigungsform. FALSE ergibt NICHT_ANWENDBAR; keine automatische Vertragsauslegung.

## gesamtglaeubiger_innenanteil

Bei anwendbarer gleichanteiliger Innenberechtigung: Anteilsquote=1geteilt durch Anzahl der Gesamtgläubiger; rechnerischer Innenanteil=Gesamtleistung mal Anteilsquote.

Nur rechnerische gleiche Innenberechtigung der Gesamtgläubiger nach §430. Die gegenüber dem Schuldner bestehende Außenberechtigung wird nicht auf diesen Innenanteil reduziert. Keine Abrechnung bereits vereinnahmter Leistungen, kein selbständiger Ausgleichsanspruch in exakt dieser Höhe ohne Prüfung weiterer Voraussetzungen. Abweichende Bestimmungen und andere Gläubigerformen bleiben gesondert.

wert enthält anteilsquote als exakten dimensionslosen Bruch und leistungsanteil als exakten Bruch in leistungseinheit. Bei NICHT_ANWENDBAR ist wert null. Keine automatische Rundung; Nutzerangaben einschließlich Einheit bleiben im Ergebnis sichtbar.

- `gesamtleistung`: Nichtnegative Dezimalzeichenfolge oder exaktes Bruchobjekt mit zaehler/nenner nach NUMERIK.md. Bezifferte Gesamtleistung in der gesondert angegebenen Einheit; keine automatische Bewertung oder Umrechnung.
- `anzahl_gesamtglaeubiger`: Ganzzahl zwischen 2 und 9007199254740991. Gezählt werden ausschließlich die Personen auf der aufzuteilenden Seite; die Gegenpartei nicht mitzählen. Keine Anzahl verschiedener Ansprüche oder Leistungsteile.
- `leistungseinheit`: Nichtleere Zeichenfolge der gemeinsamen Leistungseinheit, beispielsweise EUR oder kg. Wird als Ergebniseinheit übernommen; keine Umrechnung und keine automatische Cent- oder Stückrundung. Physische Teilbarkeit und rechtliche Einordnung bleiben gesonderte Tatsachen.
- `gleichanteilige_innenberechtigung_anwendbar`: Expliziter Wahrheitswert: Gesamtgläubigerschaft liegt vor und im Innenverhältnis ist kein anderer Anteil bestimmt (§ 430). FALSE ergibt NICHT_ANWENDBAR. Eine abweichende Bestimmung wird nicht automatisch verworfen oder durch Gleichanteile ersetzt.
