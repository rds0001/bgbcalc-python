# Kostenbasis im vereinfachten Verfahren

## modernisierung_vereinfachte_kostenbasis

Verbleibender Kostenhöchstbetrag = max(10000 Euro minus früher geltend gemachte Kosten, 0). Übersteigen die jetzt geltend gemachten Kosten diesen Betrag, ist die Teilrechnung nicht anwendbar; kein automatisches Abschneiden der Kosten. Andernfalls pauschaler Erhaltungsabzug von 30 Prozent und verbleibende Kostenbasis von 70 Prozent.

Nur Kostenprüfung und Pauschale nach § 559c Absätzen 1/2. Der tatsächliche Erhaltungsanteil wird in diesem Verfahren nicht zusätzlich abgezogen. Frühere Verfahren und ihr Fünfjahreszeitraum werden als geprüfte Nutzervorgabe zusammengefasst. Das Ergebnis ist weder die jährliche noch die monatliche Mieterhöhung; Kappung, laufende Aufwendungsförderung, Grundtatbestand, Heizungs-Härtefälle und Erklärung bleiben gesondert. Die Sperre für spätere Erhöhungen nach § 559c Absatz 4 wird nicht geprüft. Erhöhungsbeträge über der Kostengrenze werden nicht automatisch auf das reguläre Verfahren umgestellt.

Bei BERECHNET enthält wert kostenhoechstbetrag, erhaltungspauschale und kostenbasis als exakte EUR-Brüche. Bei nicht gewähltem Verfahren oder überschrittener Kostengrenze: NICHT_ANWENDBAR und wert null. Keine Cent-Rundung.

- `geltend_gemachte_kosten`: Nichtnegative EUR-Dezimalzeichenfolge oder exaktes Bruchobjekt mit zaehler/nenner nach NUMERIK.md. Für die Wohnung geltend gemachte, nach § 559a Absatz 1 bereits bereinigte Kosten vor der 30-Prozent-Pauschale. Keine Bruttokosten mit noch enthaltenen nicht anrechenbaren Kostenbeiträgen eingeben.
- `frueher_geltend_gemachte_kosten`: Nichtnegative EUR-Dezimalzeichenfolge oder exaktes Bruchobjekt mit zaehler/nenner nach NUMERIK.md. Summe der Kosten, die bei früheren Erhöhungen in den letzten fünf Jahren nach § 559c Absatz 1, § 559 oder § 559e geltend gemacht wurden (§ 559c Absatz 2). Der Aufrufer wählt Zeitraum und rechtlich einschlägige Verfahren; nicht die Summe früherer monatlicher Mieterhöhungen.
- `vereinfachtes_verfahren_gewaehlt`: Expliziter Wahrheitswert zur Wahl des vereinfachten Verfahrens. FALSE ergibt NICHT_ANWENDBAR; die Kostenprüfung allein ersetzt weder die Wahl noch die übrigen Voraussetzungen.
