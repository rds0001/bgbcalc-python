"""Hälftige Gesamtgut-Teilungsbilanz mit beiderseitiger Ersatzanrechnung."""
from .betraege import _geld
from .kalender import _ergebnis, _text
from .zahlen import _addieren, _bruch, _dividieren, _subtrahieren
from .zinsen import _bruchteile


def gesamtgut_teilungsbilanz(bereinigte_masse_ohne_ersatzforderungen=None, ersatzschuld_ehegatte=None, ersatzschuld_anderer=None, bilanznachweis=None):
    """§1476: Ersatzforderungen vor Halbteilung einrechnen, dann auf jeweilige Hälfte anrechnen."""
    masse = _geld(bereinigte_masse_ohne_ersatzforderungen)
    erster = _geld(ersatzschuld_ehegatte)
    zweiter = _geld(ersatzschuld_anderer)
    _text(bilanznachweis,'bilanznachweis')
    teilungsmasse = _addieren(_addieren(masse,erster),zweiter)
    haelfte = _dividieren(teilungsmasse,_bruch(2))
    def einzel(ersatz):
        saldo = _subtrahieren(haelfte,ersatz)
        return dict(halbanteil=_bruchteile(haelfte),ersatzanrechnung=_bruchteile(min(haelfte,ersatz)),auseinandersetzungssaldo=_bruchteile(saldo),auseinandersetzungsanspruch=_bruchteile(max(saldo,_bruch(0))),restersatzpflicht=_bruchteile(max(_subtrahieren(ersatz,haelfte),_bruch(0))))
    eingaben = dict(bereinigte_masse_ohne_ersatzforderungen=bereinigte_masse_ohne_ersatzforderungen,ersatzschuld_ehegatte=ersatzschuld_ehegatte,ersatzschuld_anderer=ersatzschuld_anderer,bilanznachweis=bilanznachweis)
    ergebnis = _ergebnis(dict(teilungsmasse_einschliesslich_ersatzforderungen=_bruchteile(teilungsmasse),ehegatte=einzel(erster),anderer_ehegatte=einzel(zweiter)),'EUR','BGB_GESAMTGUT_TEILUNGSBILANZ',eingaben,[dict(operation='Voll bewertete Ersatzforderungen beider Ehegatten zur bereits bereinigten sonstigen Restmasse addieren, halbieren und jede eigene Ersatzschuld auf den eigenen Halbteil anrechnen; überschießende Ersatzschuld als Restpflicht ausweisen.')],eingaben.copy())
    ergebnis['hinweise'] = ['§1476I/II im Standardfall nach erledigter vorrangiger Verbindlichkeitenberichtigung und erforderlichen Rückbehalten nach§1475. Eingabemasse umfasst sonstiges verbleibendes Gesamtgut, aber gerade keine der gesondert eingegebenen Ersatzforderungen und keine nochmals abzuziehenden schon berücksichtigten Schulden. Beide Ersatzforderungen sind rechtlich festgestellt und in voller angesetzter Höhe realisierbar beziehungsweise anrechenbar; Abschläge wegen Uneinbringlichkeit, Insolvenz und Bewertungsstreit gesondert. Vor Halbteilung gehören die Ersatzforderungen zur Masse, danach wird die jeweilige Ersatzschuld auf den eigenen Halbanteil angerechnet; bloßes Halbieren der ersatzforderungsfreien Masse wäre falsch. Positiver Anspruch kann vorhandene Restmasse plus noch zu leistenden Ersatz des anderen umfassen und ist kein Nachweis sofort verfügbarer Barauszahlung. Negativer Saldo bedeutet überschießende Restersatzpflicht nachAbsatz2, nicht negativer Auszahlungsbetrag. Sonderrückerstattung§1478, Abfindungen§1501 und abweichende Vereinbarungen nicht in diese Standardbilanz hineinmischen.']
    return ergebnis
