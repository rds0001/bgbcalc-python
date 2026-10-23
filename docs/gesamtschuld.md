# Gesamtschuld und Ausfalltragung

## gesamtschuld_gleichanteile_mit_ausfall

Ursprüngliche Quote1/n; Grundbeitrag=Gesamtbetrag/n. Vollständiger Ausfallbetrag=Grundbeitrag mal Anzahl der ausgefallenen Beiträge. Zusatzbeitrag je Übrigem=Ausfallbetrag geteilt durch n minus Ausfallanzahl. Gesamtbelastung je Übrigem=Grundbeitrag plus Zusatzbeitrag. Auch ohne Ausfall werden Grundanteile ausgewiesen.

- `gesamtbetrag`: Nichtnegativer Gesamtbetrag der betrachteten Gesamtschuld in EUR als Dezimalzeichenfolge oder exaktes Bruchobjekt mit Zeichenfolgenfeldern zaehler und nenner nach NUMERIK.md. Keine Summe bereits individuell verteilter Rückgriffsforderungen; Zahlungsstände werden hier nicht verrechnet.
- `anzahl_gesamtschuldner`: Ganze Zahl zwischen 2 und9007199254740991 der intern zu gleichen Grundanteilen verpflichteten Gesamtschuldner. Gläubiger nicht mitzählen. Keine abweichenden internen Quoten oder persönlich ausgeschlossenen Ausgleichspflichten in diese Gleichanteilsgruppe aufnehmen.
- `anzahl_vollstaendig_ausfallender_beitraege`: Ganze Zahl von0 bis anzahl_gesamtschuldner minus1. Gezählt werden ausschließlich Beiträge, die vollständig nicht erlangt werden können. Die tatsächliche und rechtliche Nichterlangbarkeit ist eine Nutzervorgabe; bloßer Zahlungsverzug genügt nicht automatisch. Mindestens ein übriger ausgleichungspflichtiger Schuldner muss verbleiben. Teilweise Ausfälle werden von dieser Funktion nicht modelliert.
- `gleichanteiliger_ausgleich_anwendbar`: Expliziter Wahrheitswert zur Anwendbarkeit des gleichen internen Grundanteils nach §426 Abs.1 Satz1 und der Ausfalltragung unter diesen übrigen Schuldnern. Keine andere Bestimmung im Innenverhältnis. FALSE ergibt NICHT_ANWENDBAR; andere Quoten werden nicht als Gleichanteile behandelt.

wert enthält urspruenglicher_innenanteil (dimensionslos), urspruenglicher_beitrag, gesamter_ausfallbetrag, zusaetzlicher_beitrag_je_uebrigem und gesamtbelastung_je_uebrigem (jeweils exakter EUR-Bruch) sowie anzahl_uebrige als ganze Personenzahl. Bei NICHT_ANWENDBAR ist wert null. Keine automatische Cent-Rundung.

Beschränkter Teilfall des §426 Abs.1: gleiche interne Grundanteile, ausschließlich vollständig ausfallende Beiträge und mindestens ein übriger Ausgleichungspflichtiger. Keine automatische Bewertung der Nichterlangbarkeit, keine Teilinsolvenz, keine abweichenden Quoten, keine Ermittlung bereits geleisteter Beiträge. Ausfalltragung ist keine Befreiung des ausfallenden Schuldners und keine Begrenzung der Außenhaftung. Zahlungsanspruch, Fälligkeit, Forderungsübergang und Schutz des Gläubigers nach §426 Abs.2 sind gesondert zu bestimmen.
