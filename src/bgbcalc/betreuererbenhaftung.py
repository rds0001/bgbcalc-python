from .betraege import _geld
from .kalender import _ergebnis, _text
from .zahlen import _bruch, _subtrahieren
from .zinsen import _bruchteile

def betreuer_erbenhaftungsbetrag(verbleibender_uebergegangener_anspruch=None, nachlasswert_im_erbfall=None, bereits_ausgeschoepfter_haftungsrahmen=None, haftungsnachweis=None):
    """Verbleibenden Nachlasswert-Haftungsrahmen als nichtnegativen Rest nach rechtlich qualifizierter Ausschöpfung berechnen; verbleibenden Staatskassenanspruch auf diesen Rahmen begrenzen."""
    anspruch = _geld(verbleibender_uebergegangener_anspruch)
    nachlass = _geld(nachlasswert_im_erbfall);ausgeschoepft = _geld(bereits_ausgeschoepfter_haftungsrahmen)
    _text(haftungsnachweis,'haftungsnachweis')
    rahmen = max(_subtrahieren(nachlass,ausgeschoepft),_bruch(0));betrag = min(anspruch,rahmen)
    wert = dict(verbleibender_haftungsrahmen=_bruchteile(rahmen),rechnerischer_haftungsbetrag=_bruchteile(betrag),durch_rahmen_nicht_gedeckter_anspruch=_bruchteile(_subtrahieren(anspruch,betrag)))
    eingaben = dict(verbleibender_uebergegangener_anspruch=verbleibender_uebergegangener_anspruch, nachlasswert_im_erbfall=nachlasswert_im_erbfall, bereits_ausgeschoepfter_haftungsrahmen=bereits_ausgeschoepfter_haftungsrahmen, haftungsnachweis=haftungsnachweis)
    ergebnis = _ergebnis(wert,"EUR",'BGB_BETREUER_ERBENHAFTUNGSBETRAG',eingaben,[dict(operation='Verbleibenden Nachlasswert-Haftungsrahmen als nichtnegativen Rest nach rechtlich qualifizierter Ausschöpfung berechnen; verbleibenden Staatskassenanspruch auf diesen Rahmen begrenzen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§1881Satz2: nur BGB-Nachlasswertdeckel bei bereits rechtlich bestimmten Eingaben, keine vollständige Sozialhilfe-Erbenhaftungsberechnung. Entsprechend102III/IVSGBXII geltende Ausnahmen und Erlöschen sind vorab in den verbleibenden Anspruch einzubeziehen; externe Freibeträge nicht erfinden.1880II wird nach1881Satz2 auf Erben nicht angewandt. Die Wertgrenze desselben Nachlasses bei mehreren Ansprüchen nicht mehrfach ungekürzt ausschöpfen; anrechenbare Vorbefriedigungen rechtlich belegen. Keine automatische Erbquotenaufteilung, gesamtschuldnerische Innenverteilung oder Sachbewertung. Betrag außerhalb des Rahmens ist rechnerisch ungedeckt, kein automatisches Erlöschen gegenüber anderen Verpflichteten. Überhöhte frühere Zahlung erzeugt hier keine Rückerstattung.']
    return ergebnis
