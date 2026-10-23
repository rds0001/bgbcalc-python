"""Addition gesetzlich gedeckter dinglicher Forderungskomponenten."""
from .betraege import _geld
from .kalender import _ergebnis, _fehler, _text, _vorhanden
from .zahlen import _addieren, _bruch
from .zinsen import _bruchteile

_FAELLE = {'hypothek_1118': ['forderung', 'gesetzliche_zinsen', 'kuendigungskosten', 'rechtsverfolgungskosten'], 'pfand_1210': ['forderung', 'zinsen', 'vertragsstrafen', 'verwendungsersatz', 'kuendigungskosten', 'rechtsverfolgungskosten', 'pfandverkaufskosten']}

def dinglicher_haftungsumfang(regelfall=None, forderungsbestandteile=None, zuordnungsnachweis=None):
    """§§1118/1210: nicht überlappende gedeckte Bestandteile addieren."""
    _text(regelfall,'regelfall')
    if regelfall not in _FAELLE:
        _fehler('regelfall','Unbekannter Sicherungsfall.')
    _vorhanden(forderungsbestandteile,'forderungsbestandteile')
    if not isinstance(forderungsbestandteile,dict) or set(forderungsbestandteile) != set(_FAELLE[regelfall]):
        _fehler('forderungsbestandteile','Genau die für den Sicherungsfall festgelegten Komponenten erforderlich; fehlende Ansprüche mit nullEUR angeben.')
    _text(zuordnungsnachweis,'zuordnungsnachweis')
    summe = _bruch(0)
    for name in _FAELLE[regelfall]:
        summe = _addieren(summe,_geld(forderungsbestandteile[name]))
    eingaben = dict(regelfall=regelfall,forderungsbestandteile=forderungsbestandteile,zuordnungsnachweis=zuordnungsnachweis)
    ergebnis = _ergebnis(_bruchteile(summe),'EUR','BGB_DINGLICHER_HAFTUNGSUMFANG',eingaben,[dict(operation='Rechtlich gedeckte, nicht überlappende Forderungsbestandteile summieren.')],eingaben.copy())
    ergebnis['hinweise'] = ['Nur Umfang bereits rechtlich zugeordneter, nicht überlappender gedeckter Forderungsbestandteile.1118 enthält gesetzliche Zinsen sowie Kündigung und Rechtsverfolgung zur Befriedigung aus dem Grundstück.1210: nachträgliche rechtsgeschäftliche Erweiterungen des persönlichen Schuldners bei abweichendem Pfandeigentümer ausgeschlossen. Forderung ohne nochmals getrennt erfasste Nebenbeträge angeben. Keine Ermittlung von Zinslauf, Rang, Verwertungserlös oder tatsächlicher Deckung; externe Sonderbegrenzungen gesondert.']
    return ergebnis
