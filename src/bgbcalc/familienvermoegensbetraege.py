"""Anlagebetrag verwalteten Vermögens und Regeljahresbetrag der Unterhaltssicherheit."""
from .betraege import _geld
from .kalender import _ergebnis, _text
from .zahlen import _bruch, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile


def verwaltungsanlagebetrag(geldbestand=None, ausgabenreserve=None, bewertungsnachweis=None):
    """§§1642/1841I: verwaltetes Geld abzüglich qualifizierten Ausgabenbedarfs, mindestens null."""
    geld = _geld(geldbestand)
    reserve = _geld(ausgabenreserve)
    _text(bewertungsnachweis, 'bewertungsnachweis')
    eingaben = dict(geldbestand=geldbestand, ausgabenreserve=ausgabenreserve, bewertungsnachweis=bewertungsnachweis)
    ergebnis = _ergebnis(_bruchteile(max(_subtrahieren(geld,reserve),_bruch(0))),'EUR','BGB_VERWALTUNGSANLAGEBETRAG',eingaben,[dict(operation='Qualifizierte Ausgabenreserve vom verwalteten Geldbestand abziehen; verbleibenden Anlagebetrag bei null begrenzen.')],eingaben.copy())
    ergebnis['hinweise'] = ['Anlagebetrag nach§1642 für der elterlichen Verwaltung unterliegendes Kindesgeld oder§1841I für Geld des Betreuten nach Ausgabenbedarf§1839. Verwaltungsunterworfenheit, erforderliche Ausgabenreserve und Bewertungszeitpunkt rechtlich qualifiziert. Reserve ist kein frei gewählter Sicherheitsabschlag. Übersteigt Reserve den Bestand, Anlagebetrag0; kein automatisch festgestellter Zahlungsanspruch oder Fehlbetragsausgleich. Anlageform, wirtschaftliche Vermögensverwaltung, Kontoinhaberschaft, Genehmigung und Rendite nicht berechnet.']
    return ergebnis


def unterhalt_sicherheitsregelbetrag(monatsrente=None, bewertungsnachweis=None):
    """§1585aI3: einfachen Jahresbetrag einer konstanten Unterhaltsrente berechnen."""
    rente = _geld(monatsrente)
    _text(bewertungsnachweis, 'bewertungsnachweis')
    eingaben = dict(monatsrente=monatsrente,bewertungsnachweis=bewertungsnachweis)
    ergebnis = _ergebnis(_bruchteile(_multiplizieren(rente,_bruch(12))),'EUR','BGB_UNTERHALT_SICHERHEITSREGELBETRAG',eingaben,[dict(operation='Qualifizierte konstante Monatsrente mit zwölf zum einfachen Jahresbetrag multiplizieren.')],eingaben.copy())
    ergebnis['hinweise'] = ['Rechnerische Regelsicherheitsgrenze nach§1585aI3 bei konstanter rechtlich qualifizierter Monatsrente. Keine automatische Sicherheitsleistungspflicht: Verlangen, Gefährdung, unbillige Belastung und Art der Sicherheit gesondert. Besondere Umstände können höhere Sicherheit rechtfertigen; dieser Regelbetrag ist keine ausnahmslose Höchstgrenze und keine freie gerichtliche Ermessensentscheidung. Wechselnde Rentenhöhen und zeitlich begrenzte Ansprüche außerhalb des konstanten Jahresansatzes separat bestimmen.']
    return ergebnis
