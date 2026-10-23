<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## gemeinschaft_fruchtanteil

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `gesamtfruchtmenge`: Nichtnegative exakte gesamte Fruchtmenge oder Fruchtbetrag als Dezimaltext/Bruch in der angegebenen einheitlichen Einheit.
- `teilhaberanteil_zaehler`: Nichtnegative ganze Zahl des qualifizierten Teilhaberanteils, höchstens Nenner und2^53-1.
- `teilhaberanteil_nenner`: Positive ganze Bezugsgröße des Teilhaberanteils, höchstens2^53-1.
- `fruchteinheit`: Nichtleere qualifizierte Einheit, etwa kg oder EUR; keine automatische Einheitenumrechnung.
- `zuordnungsnachweis`: Nichtleerer Nachweis der Gemeinschaft, zugeordneten Früchte, Periode und Teilhaberquote; Kosten-/Lastenzuordnung separat.

Gesamte qualifizierte Früchte mit Teilhaberanteil multiplizieren; Einheit beibehalten.

wert: exakter Bruch des Fruchtanteils, einheit entspricht fruchteinheit.

§743I: Früchte einer Bruchteilsgemeinschaft entsprechend qualifiziertem Teilhaberanteil. Gesamte Früchte und Betrachtungszeitraum vorab rechtlich bestimmen; notwendige Abgrenzungen101/102 sowie Kosten-/Lasten748 separat, keine automatische Netto-/Bruttoannahme. Einheit ausdrücklich vorgeben, etwa kg oder EUR; nicht unterschiedliche Einheiten addieren. Rechnerischer Bruchteil begründet keine automatische Zuweisung bestimmter unteilbarer Naturstücke. Bei mehreren Einzelaufrufen Teilhaberanteile ohne Doppelzählung verwenden; kein Ersatz für die Bestimmung der tatsächlichen Anteilsquoten.

Nichtnegative exakte Gesamtmenge, Anteil0..1, sicherer gemeinsamer Zahlenbereich nach NUMERIK.md; keine Rundung.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_743_T0001

```python
from bgbcalc import gemeinschaft_fruchtanteil
gemeinschaft_fruchtanteil(
    gesamtfruchtmenge='100',
    teilhaberanteil_zaehler=1,
    teilhaberanteil_nenner=4,
    fruchteinheit='kg',
    zuordnungsnachweis='Qualifizierte gesamte Früchte derselben Periode und bekannte Teilhaberquote743I.',
)
```
