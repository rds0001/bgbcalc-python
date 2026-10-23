<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## nachbesserung_fehlgeschlagen

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `erfolglose_versuche`: Ganze Zahl0..2^53-1 rechtlich zusammengehöriger erfolgloser Nachbesserungsversuche am konkreten Mangel. Nicht beliebige Werkstattkontakte oder Nachlieferungen mitzählen.
- `abweichende_umstaende`: Wahrheitswert, ob Art der Sache, Art des Mangels oder sonstige Umstände ein Abweichen von der Zweitversuchsregel rechtfertigen. Keine automatische Bewertung aus Preis, Lebensdauer oder einer erfundenen Skala.
- `fehlgeschlagen_nach_einzelfall`: Wahrheitswert der dokumentierten Einzelfallentscheidung bei abweichenden Umständen; kann früheres oder späteres Fehlschlagen bedeuten. Wird nur bei abweichende_umstaende=TRUE für das Ergebnis verwendet, ansonsten validiert und von der gesetzlichen Versuchszahlregel verdrängt.
- `regel_440_anwendbar`: Wahrheitswert der Anwendbarkeit der kaufrechtlichen Nachbesserungsregel. Insbesondere FALSE, wenn§475d im konkreten Verbrauchsgüterfall abweichend gilt; dann NICHT_ANWENDBAR.
- `einordnungsnachweis`: Nichtleere Begründung von Nachbesserung, zusammengehörigen erfolglosen Versuchen und etwaiger abweichender Einzelfallbewertung; Vorrang des Verbrauchsgüterrechts prüfen.

Ohne abweichende Umstände mindestens zwei erfolglose Nachbesserungsversuche; bei belegter Ausnahme rechtliche Einzelfallbewertung verwenden.

wert ist Wahrheitswert des Fehlschlagens in dieser Regel; NICHT_ANWENDBAR/null bei fehlendem Anwendungsbereich.

Einzelfallbewertung ist Nutzervorgabe, keine selbständige implementierte Bewertungsformel. Nicht auf Nachlieferung oder vorrangig abweichende Verbrauchsgüterfälle übertragen. Andere Fristsetzungsausnahmen separat.

Explizite Auswahl/Wahrheitswerte und nichtleerer Nachweis; Versuchszahl ganzzahlig0..2^53-1; Kalenderdaten und berechnete Grenzen0001..9999, sofern jeweiliger Parameter einschlägig.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_440_T0002

```python
from bgbcalc import nachbesserung_fehlgeschlagen
nachbesserung_fehlgeschlagen(
    erfolglose_versuche=0,
    abweichende_umstaende=False,
    fehlgeschlagen_nach_einzelfall=False,
    regel_440_anwendbar=True,
    einordnungsnachweis='Synthetische zusammengehörige erfolglose Nachbesserungsversuche; begründete Einzelfalleinordnung.',
)
```
