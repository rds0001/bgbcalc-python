"""Kauf-, Wiederkauf- und Vorkauf-Sonderbeträge mit qualifizierten Werten."""
from .betraege import _geld, _geld_ergebnis
from .kalender import _text, _fehler
from .zahlen import _addieren, _subtrahieren, _multiplizieren, _dividieren, _bruch


def gesellschaft_ausscheidensfehlbetrag(gesellschaftsverbindlichkeiten=None, wert_gesellschaftsvermoegen=None, gewinn_verlust_anteil=None, einordnungsnachweis=None):
    """Positiven Fehlbetrag aus Gesellschaftsverbindlichkeiten minus Gesellschaftsvermögen mit Gewinn-/Verlustanteil des Ausgeschiedenen multiplizieren."""
    werte = [_geld(gesellschaftsverbindlichkeiten), _geld(wert_gesellschaftsvermoegen), _geld(gewinn_verlust_anteil)]
    _text(einordnungsnachweis, 'einordnungsnachweis')
    if werte[2] > 1:
        _fehler('gewinn_verlust_anteil', 'Anteil darf eins nicht übersteigen.')
    eingaben = dict(gesellschaftsverbindlichkeiten=gesellschaftsverbindlichkeiten, wert_gesellschaftsvermoegen=wert_gesellschaftsvermoegen, gewinn_verlust_anteil=gewinn_verlust_anteil, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(_multiplizieren(max(_subtrahieren(werte[0],werte[1]),_bruch(0)),werte[2]), 'BGB_GESELLSCHAFT_AUSSCHEIDENSFEHLBETRAG', eingaben, [dict(operation='Positiven Fehlbetrag aus Gesellschaftsverbindlichkeiten minus Gesellschaftsvermögen mit Gewinn-/Verlustanteil des Ausgeschiedenen multiplizieren')])
    ergebnis['hinweise'].append('Nur §728a im qualifizierten Ausscheidensfall. Vermögens- und Verbindlichkeitswerte auf rechtlich einheitlichen Stichtag und Bewertungsumfang beziehen; Gewinn-/Verlustanteil aus Vereinbarung bzw. §709 rechtlich bestimmen. Kein automatischer Abfindungswert nach §728, keine Liquidations-Beitragsrückerstattung nach §736d/737 und kein Ausfall anderer Gesellschafter. Gesellschaftsanteil zwischen null und eins; bereits geleistete Fehlbetragszahlungen gesondert anrechnen.')
    return ergebnis
