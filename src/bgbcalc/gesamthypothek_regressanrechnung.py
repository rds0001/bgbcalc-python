from .kalender import _ergebnis, _text, _fehler
from .betraege import _geld
from .zahlen import _bruch, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile

def gesamthypothek_regressanrechnung(verbleibender_gesamthypothekenbetrag=None, eigentuemerquote=None, uebergegangener_regressbetrag=None, anwendungsnachweis=None):
    """Restbetrag mit Eigentümerquote multiplizieren und übergegangenen Regressbetrag anrechnen; positiven Anteil und Überhang getrennt ausweisen."""
    r=_geld(verbleibender_gesamthypothekenbetrag);q=_geld(eigentuemerquote);e=_geld(uebergegangener_regressbetrag);_text(anwendungsnachweis,'anwendungsnachweis')
    if q>1:_fehler('eigentuemerquote','Quote muss zwischen0und1liegen.')
    a=_multiplizieren(r,q);s=_subtrahieren(a,e)
    wert=dict(anteil_vor_anrechnung=_bruchteile(a),rechnerischer_saldo=_bruchteile(s),verbleibender_anteil=_bruchteile(max(s,_bruch(0))),nicht_am_anteil_verrechenbarer_regress=_bruchteile(max(-s,_bruch(0))))
    eingaben = dict(verbleibender_gesamthypothekenbetrag=verbleibender_gesamthypothekenbetrag, eigentuemerquote=eigentuemerquote, uebergegangener_regressbetrag=uebergegangener_regressbetrag, anwendungsnachweis=anwendungsnachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_GESAMTHYPOTHEK_REGRESSANRECHNUNG',eingaben,[dict(operation='Restbetrag mit Eigentümerquote multiplizieren und übergegangenen Regressbetrag anrechnen; positiven Anteil und Überhang getrennt ausweisen.')],eingaben.copy())
    ergebnis["hinweise"] = ['Unmittelbare Anrechnung gemäß1174II: Anteil am übrig bleibenden Betrag=Restbetrag*1172Quote. Davon den übergegangenen Regressbetrag abziehen. Negativen rechnerischen Saldo gesondert ausweisen; positiver verbleibender Anteil=max(Saldo,0), nicht am Anteil verrechenbarer Regress=max(-Saldo,0). Der übergegangene dingliche Regress wird durch diese Anrechnung nicht getilgt. Keine zusätzliche persönliche Zahlungspflicht aus negativem Saldo, keine erfundene Umverteilung an andere Eigentümer. Die Funktion berechnet ausschließlich die individuelle Anrechnung, nicht eine vollständige Neuverteilung oder Rangvollstreckung.']
    return ergebnis

