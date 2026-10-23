"""Zeitanteil der Pflichtteilsergänzung nach§2325 Absatz3."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _datum, _fehler, _frist, _text
from .zahlen import _bruch, _multiplizieren
from .zinsen import _bruchteile


def pflichtteil_schenkungsabschmelzung(
    schenkungswert=None, leistung_am=None, erbfall_am=None,
    fristanlauf_durch_leistung=None, ehegattenschenkung=None,
    eheaufloesung_am=None, einordnungsnachweis=None,
):
    """Zehntelstaffel nach voll abgelaufenen Ereignisjahren, mit Ehegattenaufschub."""
    betrag = _geld(schenkungswert)
    leistung = _datum(leistung_am, "leistung_am")
    erbfall = _datum(erbfall_am, "erbfall_am")
    if leistung > erbfall:
        _fehler("leistung_am", "Leistung darf nicht nach dem Erbfall liegen.")
    _wahrheitswert(fristanlauf_durch_leistung, "fristanlauf_durch_leistung")
    _wahrheitswert(ehegattenschenkung, "ehegattenschenkung")
    aufloesung = None
    if eheaufloesung_am is not None:
        aufloesung = _datum(eheaufloesung_am, "eheaufloesung_am")
        if aufloesung > erbfall:
            _fehler("eheaufloesung_am", "Eheauflösung darf nicht nach dem Erbfall liegen.")
    _text(einordnungsnachweis, "einordnungsnachweis")
    beginn = None
    jahre = 0
    if fristanlauf_durch_leistung and (not ehegattenschenkung or aufloesung is not None):
        beginn = max(leistung, aufloesung) if ehegattenschenkung else leistung
        jahre = min(10, erbfall.year - beginn.year)
        if jahre > 0 and erbfall <= _frist(beginn.isoformat(), jahre, "jahre", "ereignis"):
            jahre -= 1
    faktor = _bruch(10 - jahre, 10)
    ansatz = _multiplizieren(betrag, faktor)
    eingaben = dict(schenkungswert=schenkungswert, leistung_am=leistung_am, erbfall_am=erbfall_am,
        fristanlauf_durch_leistung=fristanlauf_durch_leistung, ehegattenschenkung=ehegattenschenkung,
        eheaufloesung_am=eheaufloesung_am, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(ansatz, "BGB_PFLICHTTEIL_SCHENKUNGSABSCHMELZUNG", eingaben,
        [dict(operation="Wirksamen Fristanlauf und gegebenenfalls Eheauflösung bestimmen; voll abgelaufene Ereignisjahre bis zehn zählen und je Jahr ein Zehntel abziehen")])
    ergebnis["wert"] = dict(fristbeginnereignis_am=None if beginn is None else beginn.isoformat(),
        voll_abgelaufene_jahre_bis_zehn=jahre, beruecksichtigungsfaktor=_bruchteile(faktor),
        beruecksichtigter_schenkungswert=_bruchteile(ansatz))
    ergebnis["hinweise"].append("Fristauslösende Leistung rechtlich bestimmen; bloßer Schenkungsvertrag oder vorbehaltene Nutzung können hierfür unzureichend sein. Ehegattenschenkung: Frist frühestens ab Eheauflösung; kein Beginn bei noch nicht aufgelöster Ehe. Ereignisjahre gemäß§§187/188: jeweiliger Jahrestag wird noch bis Tagesschluss mitgerechnet, Abschlag ab Folgetag; keine Werktagsverschiebung. Vorherige Bewertung§2325 Absatz2 und Ausnahme§2330 separat, danach Pflichtteilsquote und weitere Anrechnungen; kein fertiger Ergänzungsanspruch.")
    return ergebnis
