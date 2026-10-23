"""Getrennte Geldfluss- und Vermögensbewegungssalden der Betreuungsrechnung."""
from .betraege import _geld
from .kalender import _ergebnis, _fehler, _text, _vorhanden
from .zahlen import _addieren, _bruch, _subtrahieren
from .zinsen import _bruchteile


def _rechnungssumme(positionen,name):
    _vorhanden(positionen,name)
    if not isinstance(positionen,list) or not 1 <= len(positionen) <= 10000:
        _fehler(name,'Liste mit 1 bis 10000 nichtnegativen Betragspositionen erforderlich; keine Bewegung ausdrücklich als einzelne Nullposition.')
    summe = _bruch(0)
    for betrag in positionen:
        summe = _addieren(summe,_geld(betrag))
    return summe


def betreuungsrechnung_summen(einnahmen=None, ausgaben=None, vermoegenszugaenge=None, vermoegensabgaenge=None, rechnungsnachweis=None):
    """§1865III/1872III: vier Positionssummen und zwei voneinander getrennte Salden berechnen."""
    ein = _rechnungssumme(einnahmen,'einnahmen')
    aus = _rechnungssumme(ausgaben,'ausgaben')
    zu = _rechnungssumme(vermoegenszugaenge,'vermoegenszugaenge')
    ab = _rechnungssumme(vermoegensabgaenge,'vermoegensabgaenge')
    _text(rechnungsnachweis,'rechnungsnachweis')
    eingaben = dict(einnahmen=einnahmen,ausgaben=ausgaben,vermoegenszugaenge=vermoegenszugaenge,vermoegensabgaenge=vermoegensabgaenge,rechnungsnachweis=rechnungsnachweis)
    wert = {k:_bruchteile(v) for k,v in dict(einnahmensumme=ein,ausgabensumme=aus,einnahmen_ausgaben_saldo=_subtrahieren(ein,aus),vermoegenszugangssumme=zu,vermoegensabgangssumme=ab,vermoegensbewegungssaldo=_subtrahieren(zu,ab)).items()}
    ergebnis = _ergebnis(wert,'EUR','BGB_BETREUUNGSRECHNUNG_SUMMEN',eingaben,[dict(operation='Einnahmen, Ausgaben, Vermögenszugänge und Vermögensabgänge getrennt summieren; Geldfluss- und Vermögensbewegungssaldo separat bilden, nicht addieren.')],eingaben.copy())
    ergebnis['hinweise'] = ['Rechnerischer Summenbaustein für§1865III1 und Schlussrechnung§1872III2, kein vollständiges Rechnungslegungsformular. Alle Positionen derselben rechtlich abgegrenzten Rechnungsperiode zuordnen; Rechnungsjahr gerichtlich bestimmt, Schlussrechnung grundsätzlich seit letzter eingereichter Rechnungslegung. Einnahmen/Ausgaben einerseits und Vermögenszugänge/-abgänge andererseits sind getrennte Sichten und können denselben wirtschaftlichen Vorgang abbilden. Ihre Salden daher nicht nochmals zu einem Vermögenszuwachs addieren. Vermögensumschichtungen und Sachwerte fachlich konsistent qualifizieren, keine automatische Buchungs-/Bewertungsmethode. Keine Bewegung explizit als eine Nullposition angeben; fehlende Kategorie ist keine stillschweigende Null. Reihenfolge, Einzelbelege, Anfangs-/Endbestand, Vollständigkeitserklärung, vom Betreuten selbst verwaltete Teile und Befreiungen gesondert. Negative Salden sind Rechenergebnisse, keine Feststellung einer Verbindlichkeit oder Pflichtverletzung.']
    return ergebnis
