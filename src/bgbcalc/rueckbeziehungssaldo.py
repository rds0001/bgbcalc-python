"""Bewertete Soll-/Ist-Differenz bei Bestätigung oder vereinbarter Rückbeziehung."""
from .betraege import _geld
from .kalender import _auswahl, _ergebnis, _text
from .zahlen import _bruch, _subtrahieren
from .zinsen import _bruchteile


def rueckbeziehung_leistungssaldo(sollwert_bei_rueckbeziehung=None, bereits_erlangter_istwert=None, regelfall=None, bewertungsnachweis=None):
    """§§141II/159: rechtlich qualifizierten kontrafaktischen Sollwert mit Istwert saldieren."""
    soll = _geld(sollwert_bei_rueckbeziehung)
    ist = _geld(bereits_erlangter_istwert)
    _auswahl(regelfall,'regelfall',('vertragsbestaetigung_141','bedingungsrueckbeziehung_159'))
    _text(bewertungsnachweis,'bewertungsnachweis')
    saldo = _subtrahieren(soll,ist)
    eingaben = dict(sollwert_bei_rueckbeziehung=sollwert_bei_rueckbeziehung,bereits_erlangter_istwert=bereits_erlangter_istwert,regelfall=regelfall,bewertungsnachweis=bewertungsnachweis)
    wert = dict(rechnerischer_leistungssaldo=_bruchteile(saldo),fehlender_leistungswert=_bruchteile(max(saldo,_bruch(0))),uebersteigender_istwert=_bruchteile(max(_subtrahieren(ist,soll),_bruch(0))))
    ergebnis = _ergebnis(wert,'EUR','BGB_RUECKBEZIEHUNG_LEISTUNGSSALDO',eingaben,[dict(operation='Bewerteten kontrafaktischen Sollwert minus schon erlangten Istwert je Beteiligtem und identischem Leistungskreis berechnen.')],eingaben.copy())
    ergebnis['hinweise'] = ['Nur qualifizierte Zweifelsregel bei Vertragsbestätigung141Absatz2 oder wirksam vereinbarte Rückbeziehung nach eingetretener Bedingung159. Beide Werte betreffen denselben Beteiligten, Leistungskreis, Zeitraum und Bewertungsmaßstab. Tatsächlich erfolgte Leistungen und Rückabwicklungen nur einmal erfassen. Keine automatische Bewertung hypothetischer Vorteile, Wirksamkeitsentscheidung, Aufrechnung verschiedener Beteiligter oder Rückgewährpflicht aus einem bloßen rechnerischen Mehrerhalt. Negative Differenz zeigt allein, dass Ist den vorgegebenen Sollwert übersteigt.']
    return ergebnis
