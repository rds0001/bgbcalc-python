"""§493 Absatz4: unterschiedliche20%-Grenzen für Auslösung und Fortdauer."""
from .betraege import _geld, _wahrheitswert
from .kalender import _text, _fehler, _ergebnis
from .zahlen import _bruch, _subtrahieren, _multiplizieren, _dividieren
from .zinsen import _bruchteile


def immobiliardarlehen_wechselkurswarnschwelle(wert_zum_vertragskurs=None, wert_zum_vergleichskurs=None, warnfolge_bereits_ausgeloest=None, einordnungsnachweis=None):
    """Neue Warnschwelle strikt über20%, ausgelöste Folge bis zum Unterschreiten von20%."""
    basis,aktuell=_geld(wert_zum_vertragskurs),_geld(wert_zum_vergleichskurs)
    _wahrheitswert(warnfolge_bereits_ausgeloest,'warnfolge_bereits_ausgeloest'); _text(einordnungsnachweis,'einordnungsnachweis')
    if basis<=0:
        _fehler('wert_zum_vertragskurs','Positiver Vertragskurs-Vergleichswert erforderlich.')
    grenze=_multiplizieren(basis,_bruch(6,5)); veraenderung=_dividieren(_subtrahieren(aktuell,basis),basis)
    wert=dict(relative_wertaenderung=_bruchteile(veraenderung),zwanzigprozent_grenzwert=_bruchteile(grenze),neuausloesungsschwelle_ueberschritten=aktuell>grenze,fortdauerschwelle_erreicht=aktuell>=grenze,numerische_warnbedingung=aktuell>=grenze if warnfolge_bereits_ausgeloest else aktuell>grenze)
    eingaben=dict(wert_zum_vertragskurs=wert_zum_vertragskurs,wert_zum_vergleichskurs=wert_zum_vergleichskurs,warnfolge_bereits_ausgeloest=warnfolge_bereits_ausgeloest,einordnungsnachweis=einordnungsnachweis)
    ergebnis=_ergebnis(wert,'quote_und_landeswaehrung','BGB_IMMOBILIARDARLEHEN_WECHSELKURSWARNSCHWELLE',eingaben,[dict(operation='Relative Wertänderung bestimmen; erste Auslösung strikt über6/5 Basiswert, bereits ausgelöste Folge bis zum Unterschreiten dieser Grenze.')],eingaben.copy())
    ergebnis['hinweise']=['Nur numerischer Vergleich nach §493 Absatz4 Satz1/Satz2 Nummer4 im qualifizierten Fremdwährungs-/entsprechenden Einkommenswährungsfall. Beide Werte müssen denselben aktuellen Restbetrag oder dieselbe regelmäßige Rate in gleicher Landeswährung zu Vertrags- bzw. Vergleichskurs darstellen; Werte gegebenenfalls mit immobiliardarlehen_wechselkursrechnung vorbereiten. Bei bereits ausgelöster Folge hält genau20% die numerische Fortdauergrenze ein, löst aber erstmals keine Folge aus. Restbetrag und Raten gemeinsam fachlich berücksichtigen, sofern beide maßgeblich sind. Keine automatische Bestimmung regelmäßiger Informationsabstände, kein Versand und kein vollständiger Informationstatbestand. Nullvergleichsbasis außerhalb dieser relativen Rechnung.']
    return ergebnis
