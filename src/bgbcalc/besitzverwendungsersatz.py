"""Bereinigung notwendiger Verwendungen im Grundfall§§994I/995/999."""
from .betraege import _geld, _geld_ergebnis
from .kalender import _fehler, _text
from .zahlen import _addieren, _subtrahieren


def besitz_notwendiger_verwendungsersatz(notwendige_eigene_verwendungen=None, ausgeschlossene_erhaltungskosten=None, ausgeschlossene_lasten=None, ersatzfaehige_vorgaengerverwendungen=None, zuordnungsnachweis=None):
    """Ausgeschlossene Erhaltung/Lasten abziehen und qualifizierte Vorgängeransprüche addieren."""
    eigene = _geld(notwendige_eigene_verwendungen)
    erhaltung = _geld(ausgeschlossene_erhaltungskosten)
    lasten = _geld(ausgeschlossene_lasten)
    vorgaenger = _geld(ersatzfaehige_vorgaengerverwendungen)
    ausschluss = _addieren(erhaltung,lasten)
    if ausschluss > eigene:
        _fehler('notwendige_eigene_verwendungen','Ausgeschlossene Erhaltungskosten und Lasten müssen überschneidungsfreie Teile der eigenen Verwendungen sein.')
    _text(zuordnungsnachweis,'zuordnungsnachweis')
    wert = _addieren(_subtrahieren(eigene,ausschluss),vorgaenger)
    eingaben = dict(notwendige_eigene_verwendungen=notwendige_eigene_verwendungen,ausgeschlossene_erhaltungskosten=ausgeschlossene_erhaltungskosten,ausgeschlossene_lasten=ausgeschlossene_lasten,ersatzfaehige_vorgaengerverwendungen=ersatzfaehige_vorgaengerverwendungen,zuordnungsnachweis=zuordnungsnachweis)
    ergebnis = _geld_ergebnis(wert,'BGB_BESITZ_NOTWENDIGER_VERWENDUNGSERSATZ',eingaben,[dict(operation='Eigene notwendige Verwendungen um nicht ersatzfähige Erhaltungskosten/Lasten kürzen und bereits bereinigte Vorgängeransprüche addieren.')])
    ergebnis['hinweise'].append('Nur994Absatz1-Grundfall vor Rechtshängigkeit/990-Haftungsbeginn. Eigene Bruttoverwendungen enthalten die nach995 einbezogenen Lasten. Ausgeschlossen sind gewöhnliche Erhaltungskosten für die Zeit verbleibender Nutzungen sowie nicht ersatzfähige Lasten dieser Zeit; außergewöhnliche auf den Stammwert gelegte Lasten nicht pauschal ausschließen. Vorgängerbetrag nach999 bereits rechtlich bereinigt, nicht erneut in eigenen Kosten enthalten. Rechtsnachfolge, zeitliche Zuordnung und notwendige Verwendung vorqualifiziert.994Absatz2-Geschäftsführung-ohne-Auftrag und weitere997–1003-Voraussetzungen gesondert; Ergebnis keine automatische Fälligkeit oder Verwendungsbewertung.')
    return ergebnis
