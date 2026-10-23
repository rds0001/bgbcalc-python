from .betraege import _geld
from .kalender import _ergebnis, _fehler, _ganzzahl, _text
from .zahlen import _bruch, _multiplizieren
from .zinsen import _bruchteile


def gemeinschaft_fruchtanteil(gesamtfruchtmenge=None, teilhaberanteil_zaehler=None, teilhaberanteil_nenner=None, fruchteinheit=None, zuordnungsnachweis=None):
    """Qualifizierte gesamte Früchte mit dem Anteil des Teilhabers multiplizieren."""
    menge=_geld(gesamtfruchtmenge);z=_ganzzahl(teilhaberanteil_zaehler,'teilhaberanteil_zaehler',0,9007199254740991);n=_ganzzahl(teilhaberanteil_nenner,'teilhaberanteil_nenner',1,9007199254740991)
    if z>n:_fehler('teilhaberanteil_zaehler','Teilhaberanteil darf eins nicht übersteigen.')
    _text(fruchteinheit,'fruchteinheit');_text(zuordnungsnachweis,'zuordnungsnachweis')
    eingaben=dict(gesamtfruchtmenge=gesamtfruchtmenge,teilhaberanteil_zaehler=teilhaberanteil_zaehler,teilhaberanteil_nenner=teilhaberanteil_nenner,fruchteinheit=fruchteinheit,zuordnungsnachweis=zuordnungsnachweis)
    ergebnis=_ergebnis(_bruchteile(_multiplizieren(menge,_bruch(z,n))),fruchteinheit,'BGB_GEMEINSCHAFT_FRUCHTANTEIL',eingaben,[dict(operation='Qualifizierte gesamte Früchte mit rechtlich bestimmtem Teilhaberanteil multiplizieren; ursprüngliche Einheit beibehalten.')],eingaben.copy())
    ergebnis['hinweise']=['§743I: Früchte einer Bruchteilsgemeinschaft entsprechend qualifiziertem Teilhaberanteil. Gesamte Früchte und Betrachtungszeitraum vorab rechtlich bestimmen; notwendige Abgrenzungen101/102 sowie Kosten-/Lasten748 separat, keine automatische Netto-/Bruttoannahme. Einheit ausdrücklich vorgeben, etwa kg oder EUR; nicht unterschiedliche Einheiten addieren. Rechnerischer Bruchteil begründet keine automatische Zuweisung bestimmter unteilbarer Naturstücke. Bei mehreren Einzelaufrufen Teilhaberanteile ohne Doppelzählung verwenden; kein Ersatz für die Bestimmung der tatsächlichen Anteilsquoten.']
    return ergebnis
