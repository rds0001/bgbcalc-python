"""Gesetzliche Vermögenssummierung ohne Immobilien und Verbindlichkeitsabzug."""
from .betraege import _geld, _wahrheitswert
from .kalender import _ergebnis, _fehler, _text, _vorhanden
from .zahlen import _addieren, _bruch
from .zinsen import _bruchteile


def betreuung_vermoegenswert_ohne_immobilien(vermoegenspositionen=None, verbindlichkeiten=None, bewertungsnachweis=None):
    """§1860I: qualifizierte Nichtimmobilienwerte summieren, Verbindlichkeiten nicht abziehen."""
    _vorhanden(vermoegenspositionen,'vermoegenspositionen')
    if not isinstance(vermoegenspositionen,list) or not 1 <= len(vermoegenspositionen) <= 10000:
        _fehler('vermoegenspositionen','Liste mit 1 bis 10000 qualifizierten Vermögenspositionen erforderlich; kein Vermögen als einzelne Nullposition.')
    ansatz = _bruch(0)
    immobilien = _bruch(0)
    for position in vermoegenspositionen:
        if not isinstance(position,dict) or set(position) != {'wert','immobilie'}:
            _fehler('vermoegenspositionen','Genau wert und immobilie je Position erforderlich.')
        wert = _geld(position['wert'])
        _wahrheitswert(position['immobilie'],'immobilie')
        if position['immobilie']:
            immobilien = _addieren(immobilien,wert)
        else:
            ansatz = _addieren(ansatz,wert)
    _geld(verbindlichkeiten)
    _text(bewertungsnachweis,'bewertungsnachweis')
    eingaben = dict(vermoegenspositionen=vermoegenspositionen,verbindlichkeiten=verbindlichkeiten,bewertungsnachweis=bewertungsnachweis)
    ergebnis = _ergebnis(dict(anzusetzender_vermoegenswert=_bruchteile(ansatz),nicht_beruecksichtigter_immobilienwert=_bruchteile(immobilien)),'EUR','BGB_BETREUUNG_VERMOEGENSWERT_OHNE_IMMOBILIEN',eingaben,[dict(operation='Qualifizierte Vermögenspositionen nach Immobilienzuordnung trennen; ausschließlich Nichtimmobilienwerte summieren, Verbindlichkeiten nicht abziehen.')],eingaben.copy())
    ergebnis['hinweise'] = ['§1860I schreibt Berechnung ohne Immobilien und Verbindlichkeiten vor. Positionen und Werte zum maßgeblichen Stichtag rechtlich qualifiziert, anteilige Berechtigungen bereits bewertet. Wert einer Nichtimmobilienposition nicht vorher um separat zu berücksichtigende Verbindlichkeiten vermindern; sonst würde der gesetzlich ausgeschlossene Schuldenabzug verdeckt nachgeholt. Verbindlichkeiten werden als nichtnegative dokumentierte Eingabe validiert und bewusst nicht abgezogen. Immobilienzuordnung ist Nutzervorgabe, keine automatische Objektklassifikation. Kein Vermögen als einzelne Nullposition angeben. Die6000EUR-Schwelle, Antrag, richterliches Ermessen, Gefährdung und sonstige Befreiungswege werden nicht als eigenständige Befreiungsentscheidung berechnet.']
    return ergebnis
