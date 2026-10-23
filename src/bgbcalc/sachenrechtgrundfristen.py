"""Normgebundene gesetzliche Sachenrechtsfristen mit vorhandenem Kalenderkern."""
from .betraege import _wahrheitswert
from .kalender import _auswahl, _datum, _ergebnis, _frist, _text

_GRUNDFRISTEN = {'hypothekenmiete_faelligkeitsjahr_1123': (1, 'jahre'), 'hypothek_wiederkehrende_leistung_1126': (3, 'monate'), 'besitzschutz_864': (1, 'jahre'), 'fundanzeige_973': (6, 'monate'), 'geringwertiger_fund_973': (6, 'monate'), 'fundbereicherung_977': (3, 'jahre'), 'finderlohn_erloes_978': (3, 'jahre'), 'fundversteigerung_anmeldefrist_981': (3, 'jahre'), 'fundgeld_bekanntmachung_981': (3, 'jahre'), 'niessbrauch_eigentuemerersatz_1057': (6, 'monate'), 'niessbrauch_verwendungsersatz_1057': (6, 'monate'), 'hypothekenversicherung_anzeige_1128': (1, 'monate'), 'hypothekenversicherung_untunlich_1128': (1, 'monate'), 'buchhypothek_widerspruch_1139': (1, 'monate'), 'grundschuld_kuendigung_1193': (6, 'monate'), 'rentenschuld_kuendigung_1202': (6, 'monate'), 'pfand_verpfaenderersatz_1226': (6, 'monate'), 'pfand_verwendungsersatz_1226': (6, 'monate'), 'pfandverkauf_androhung_1234': (1, 'monate'), 'pfandverkauf_untunlich_1234': (1, 'monate')}

def sachenrechtliche_grundfrist(regelfall=None, fristbeginnereignis_am=None, einordnungsnachweis=None):
    """Gesetzliche Monats-/Jahresdauer ab normbezogen qualifiziertem Ereignis berechnen."""
    _auswahl(regelfall, 'regelfall', tuple(_GRUNDFRISTEN))
    _datum(fristbeginnereignis_am, 'fristbeginnereignis_am')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    anzahl, einheit = _GRUNDFRISTEN[regelfall]
    ende = _frist(fristbeginnereignis_am, anzahl, einheit, 'ereignis')
    eingaben = dict(regelfall=regelfall, fristbeginnereignis_am=fristbeginnereignis_am, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(dict(grundfristende=ende.isoformat(), anzahl=anzahl, einheit=einheit),
        'datum_und_fristlaenge', 'BGB_SACHENRECHTLICHE_GRUNDFRIST', eingaben,
        [dict(operation='Gesetzliche Dauer des ausgewählten Normfalls ab qualifiziertem Ereignis mit vorhandenem Kalenderkern berechnen')], eingaben.copy())
    ergebnis['annahmen'] = ['Unveränderte gesetzliche Grundfrist, Anfangsereignis und Anwendungsfall vorqualifiziert; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['Kein abschließender Eigentums-, Erlöschens-, Verjährungs-, Fälligkeits- oder Verkaufsberechtigungsentscheid. Anfangsereignis muss zur Fallbeschreibung im Fachvertrag passen; gesetzlich verschiedene Auslöser nicht austauschen. Gerichtliche Wahrung, Hemmung, Neubeginn, früherer Gleichlauf nach548, zulässige Kalenderkorrekturen und abweichende Bestimmungen gesondert. Wartefristen enden erst mit Ablauf des angegebenen Tages; keine Freigabe schon zu dessen Beginn.']
    return ergebnis


def hypothek_folgequartalsgrenze(bezugsereignis_am=None, faelligkeit_am=None, regelfall=None,
        anwendungsfall_qualifiziert=None, einordnungsnachweis=None):
    """Ende des auf Bezugsquartal folgenden Kalenderquartals und Fälligkeitslage berechnen."""
    bezug = _datum(bezugsereignis_am, 'bezugsereignis_am')
    faellig = _datum(faelligkeit_am, 'faelligkeit_am')
    _auswahl(regelfall, 'regelfall', ('teilbefriedigung_1145', 'uebertragungskenntnis_1158'))
    _wahrheitswert(anwendungsfall_qualifiziert, 'anwendungsfall_qualifiziert')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    quartalsbeginn_monat = 3*((bezug.month-1)//3)+1
    grenze = _frist(f'{bezug.year:04}-{quartalsbeginn_monat:02}-01', 6, 'monate', 'tagesbeginn')
    spaeter = faellig > grenze
    eingaben = dict(bezugsereignis_am=bezugsereignis_am, faelligkeit_am=faelligkeit_am, regelfall=regelfall,
        anwendungsfall_qualifiziert=anwendungsfall_qualifiziert, einordnungsnachweis=einordnungsnachweis)
    wert = dict(folgequartalsende=grenze.isoformat(), faelligkeit_nach_folgequartal=spaeter,
        zeitmerkmal_erfuellt=spaeter if regelfall == 'teilbefriedigung_1145' else not spaeter) if anwendungsfall_qualifiziert else None
    ergebnis = _ergebnis(wert, 'datum_und_wahrheitswerte', 'BGB_HYPOTHEK_FOLGEQUARTALSGRENZE', eingaben,
        [dict(operation='Beginn des Bezugsquartals plus6Monate nach Tagesbeginnregel ergibt Ende des Folgequartals;1145 verlangt spätere,1158 nicht spätere Fälligkeit')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if anwendungsfall_qualifiziert else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Qualifizierte Zinsen/andere Nebenleistungen und ihr Fälligkeitsdatum; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['1145: Bezugsereignis ist teilweise Befriedigung durch Eigentümer; Kosten nach1118 sind ausdrücklich nicht einbezogen.1158: Bezugsereignis ist maßgebliche Kenntnis des Eigentümers von Forderungsübertragung. Kein Einwendungs-/Gutglaubens-/Briefherausgabeentscheid und keine Zinsbetragsberechnung. Am Folgequartalsendtag ist1158-Zeitmerkmal erfüllt,1145-Zeitmerkmal nicht.']
    return ergebnis
