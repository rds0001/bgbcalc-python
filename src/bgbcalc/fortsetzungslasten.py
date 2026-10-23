"""Ungedeckte Anrechnungsposten der fortgesetzten Gütergemeinschaft."""
from .betraege import _geld
from .kalender import _ergebnis, _fehler, _text
from .zahlen import _addieren, _subtrahieren
from .zinsen import _bruchteile


def fortgesetzte_guetergemeinschaft_altlasten(persoenliche_altverbindlichkeiten=None, altverbindlichkeiten_erbendeckung=None, ersatzpflicht_zum_gesamtgut=None, ersatzpflicht_erbendeckung=None, zuordnungsnachweis=None):
    """§1500: qualifizierte persönliche Altlasten um jeweilige Erbendeckung vermindern."""
    schuld = _geld(persoenliche_altverbindlichkeiten)
    schulddeckung = _geld(altverbindlichkeiten_erbendeckung)
    ersatz = _geld(ersatzpflicht_zum_gesamtgut)
    ersatzdeckung = _geld(ersatzpflicht_erbendeckung)
    _text(zuordnungsnachweis,'zuordnungsnachweis')
    if schulddeckung > schuld or ersatzdeckung > ersatz:
        _fehler('EINGABE_UNGUELTIG','Erbendeckung darf den jeweils zugeordneten Ausgangsposten nicht übersteigen.')
    schuldrest = _subtrahieren(schuld,schulddeckung)
    ersatzrest = _subtrahieren(ersatz,ersatzdeckung)
    eingaben = dict(persoenliche_altverbindlichkeiten=persoenliche_altverbindlichkeiten,altverbindlichkeiten_erbendeckung=altverbindlichkeiten_erbendeckung,ersatzpflicht_zum_gesamtgut=ersatzpflicht_zum_gesamtgut,ersatzpflicht_erbendeckung=ersatzpflicht_erbendeckung,zuordnungsnachweis=zuordnungsnachweis)
    ergebnis = _ergebnis(dict(ungedeckte_altverbindlichkeiten=_bruchteile(schuldrest),ungedeckte_ersatzpflicht=_bruchteile(ersatzrest),anrechnungspostensumme=_bruchteile(_addieren(schuldrest,ersatzrest))),'EUR','BGB_FORTGESETZTE_GUETERGEMEINSCHAFT_ALTLASTEN',eingaben,[dict(operation='Jeweils zugeordnete Erbendeckung abziehen und ungedeckte Altverbindlichkeiten sowie Ersatzpflicht addieren.')],eingaben.copy())
    ergebnis['hinweise'] = ['§1500I/II: reine Ermittlung der ungedeckten Anrechnungsposten vor der Auseinandersetzungsbilanz. Ausgangsposten rechtlich getrennt und ohne Überschneidung: persönliche Verbindlichkeiten des Verstorbenen im Innenverhältnis sowie dessen Ersatzpflicht zum Gesamtgut. Erbendeckung umfasst die rechtlich erlangbare Deckung, nicht lediglich bisher tatsächlich eingegangene Zahlung; deren Uneinbringlichkeit/Erreichbarkeit ist qualifiziert. Keine doppelte Deckungszuordnung. Nicht bereits bereinigte Restposten nochmals vermindern. Kein zusätzlicher Geldanspruch gegen Abkömmlinge und keine individuelle Verteilung; nach§1498 besteht die überschießende persönliche Ersatzpflicht des§1476II2 nur für den überlebenden Ehegatten. Gesamtgutsbereinigung, Einrechnung vor Halbteilung, Anrechnung auf die Abkömmlingshälfte sowie§1501/1503 sind nachgelagerte Bilanzschritte, hier nicht als vollständige Teilung ausgegeben.']
    return ergebnis
