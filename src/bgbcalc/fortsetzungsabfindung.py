"""Rechnerische Abfindungseinrechnung bei fortgesetzter Gütergemeinschaft."""
from .betraege import _geld
from .kalender import _ergebnis, _text
from .zahlen import _addieren, _bruch, _dividieren, _subtrahieren
from .zinsen import _bruchteile


def fortgesetzte_guetergemeinschaft_abfindungsbilanz(bereinigte_restmasse_ohne_abfindungen=None, qualifizierte_abfindungen=None, bilanznachweis=None):
    """§1501I: gewährte Abfindungen einrechnen und auf die Abkömmlingshälfte anrechnen."""
    masse = _geld(bereinigte_restmasse_ohne_abfindungen)
    abfindung = _geld(qualifizierte_abfindungen)
    _text(bilanznachweis,'bilanznachweis')
    rechenmasse = _addieren(masse,abfindung)
    haelfte = _dividieren(rechenmasse,_bruch(2))
    saldo = _subtrahieren(haelfte,abfindung)
    eingaben = dict(bereinigte_restmasse_ohne_abfindungen=bereinigte_restmasse_ohne_abfindungen,qualifizierte_abfindungen=qualifizierte_abfindungen,bilanznachweis=bilanznachweis)
    wert = dict(rechenmasse_mit_abfindung=_bruchteile(rechenmasse),rechnerischer_ehegattenhalbteil=_bruchteile(haelfte),abkoemmlingshalbteil_vor_anrechnung=_bruchteile(haelfte),abkoemmlingssaldo_nach_anrechnung=_bruchteile(saldo))
    ergebnis = _ergebnis(wert,'EUR','BGB_FORTGESETZTE_GUETERGEMEINSCHAFT_ABFINDUNGSBILANZ',eingaben,[dict(operation='Gewährte qualifizierte Abfindungen zur bereinigten Restmasse addieren, halbieren und vollständig auf die Abkömmlingshälfte anrechnen; rechnerischen Saldo gesondert ausweisen.')],eingaben.copy())
    ergebnis['hinweise'] = ['§1501I-Bilanz ohne abweichende Vereinbarung nachAbsatz2; entsprechend§1511III für tatsächlich aus Gesamtgut gezahlte Ausschlussbeträge. Ein bloß berechneter, noch nicht gezahlter Anspruch ist keine gewährte Abfindung und darf nicht als bereits abgeflossen hinzugerechnet werden. Nur tatsächlich aus Gesamtgut gewährte, rechtlich einrechenbare Abfindungen für Anteilsverzicht oder entsprechende gezahlte Ausschlussbeträge1511III; qualifizierte Summe und maßgebliche Werte vorgeben. Restmasse enthält diese bereits abgeflossenen Beträge gerade nicht und ist nach vorrangigen Verbindlichkeiten/Rückbehalten bereinigt. Andere Ersatzforderungen/Lasten nach§§1498bis1500 sowie Vorempfänge nach§1503II sind getrennt abzugrenzen; dies ist keine vollständige Schlussauseinandersetzung. §1503III belastet im Innenverhältnis nur begünstigte Abkömmlinge, keine automatische Gleichverteilung der Abfindung. Negativer Abkömmlingssaldo bleibt ausdrücklich bloße Rechengröße und begründet keinen ausgegebenen Nachschuss-/Rückzahlungsanspruch;§1498 beschränkt die überschießende§1476II2-Ersatzpflicht auf den überlebenden Ehegatten. Rechnerischer Ehegattenhalbteil ist kein Nachweis sofort verfügbarer Barauszahlung.']
    return ergebnis
