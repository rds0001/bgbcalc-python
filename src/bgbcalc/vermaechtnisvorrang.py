"""Zweistufige numerische Vorrangverteilung (§2189)."""
from .betraege import _geld, _wahrheitswert
from .kalender import _ergebnis, _text
from .zahlen import _addieren, _bruch, _subtrahieren
from .zinsen import _bruchteile


def vermaechtnis_vorrangverteilung(verfuegbarer_beschwerungsbetrag=None, vorrangige_beschwerung=None,
    nachrangige_beschwerungen=None, vorrang_nach_2189_qualifiziert=None, bewertungsnachweis=None):
    """Qualifiziertes Beschwerungsbudget zuerst auf vorrangige, dann nachrangige Belastungen verteilen."""
    budget = _geld(verfuegbarer_beschwerungsbetrag)
    vorrang = _geld(vorrangige_beschwerung)
    nachrang = _geld(nachrangige_beschwerungen)
    _wahrheitswert(vorrang_nach_2189_qualifiziert, 'vorrang_nach_2189_qualifiziert')
    _text(bewertungsnachweis, 'bewertungsnachweis')
    eingaben = dict(verfuegbarer_beschwerungsbetrag=verfuegbarer_beschwerungsbetrag, vorrangige_beschwerung=vorrangige_beschwerung,
        nachrangige_beschwerungen=nachrangige_beschwerungen, vorrang_nach_2189_qualifiziert=vorrang_nach_2189_qualifiziert,
        bewertungsnachweis=bewertungsnachweis)
    wert = None
    if vorrang_nach_2189_qualifiziert:
        vor = min(budget, vorrang)
        nach = min(_subtrahieren(budget, vor), nachrang)
        wert = dict(vorrangiger_zuteilungsbetrag=_bruchteile(vor), nachrangiger_zuteilungsbetrag=_bruchteile(nach),
            vorrangiger_kuerzungsbetrag=_bruchteile(_subtrahieren(vorrang, vor)),
            nachrangiger_kuerzungsbetrag=_bruchteile(_subtrahieren(nachrang, nach)),
            nicht_verbrauchtes_budget=_bruchteile(_subtrahieren(budget, _addieren(vor, nach))))
    ergebnis = _ergebnis(wert, 'EUR', 'BGB_VERMAECHTNIS_VORRANGVERTEILUNG', eingaben,
        [dict(operation='Vorrang bis Budget und vollem Beschwerungswert bedienen; verbleibendes Budget bis vollem Nachrangwert; Kürzungen als Wertdifferenzen')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Wirksame Vorranganordnung2189 und zulässiger Kürzungsfall rechtlich vorgeprüft; ein vorrangiger Beschwerungsblock vor sämtlichen übrigen Beschwerungen.']
    ergebnis['hinweise'] = ['Beschwerungen sind Vermächtnisse/Auflagen auf gleicher rechtlich qualifizierter Wertgrundlage. Verfügbares Budget muss für diese Beschwerungen bereits aus einschlägiger Haftungsbeschränkung, Pflichtteil oder2187/2188 ermittelt sein, nicht unbesehen gesamter Nachlass oder Vermächtniswert. Nachrang wird nur insgesamt ausgewiesen; keine unbelegte Quotierung innerhalb desselben Rangs oder Automatik mehrerer Vorrangstufen. Keine Berechnung der vorgelagerten Kürzungsgrundlage und keine Feststellung sofortiger Geldzahlungspflichten bei Sachvermächtnissen. Budgetüberschuss erweitert keinen Beschwerungsanspruch.']
    return ergebnis
