"""Zwölfmonatsgrenzen für verspäteten Beginn und Arbeitsruhe nach§559d."""
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _tage_addieren, _text


def _verzoegerungs_ergebnis(wert, kennung, eingaben, operation):
    ergebnis = _ergebnis(wert, "daten_und_wahrheitswerte", kennung, eingaben,
        [dict(operation=operation)], eingaben.copy())
    ergebnis["annahmen"] = ["Sachlicher und zeitlicher Anwendungsbereich§559d und rechtlich maßgebliche Zeitpunkte vorgegeben; feste lokale BGB-Fassung."]
    ergebnis["hinweise"] = ["Nur zeitlicher Vermutungstatbestand; nachvollziehbarer objektiver Grund und weitere Tatbestände separat mit modernisierung_pflichtverletzungsvermutung prüfen. Keine automatische Pflichtverletzungs- oder Schadensersatzentscheidung. Keine automatische Feiertagsverschiebung des tatsächlichen Beginns oder Ruhens; untertägige Grenzfälle gesondert rechtlich einordnen."]
    return ergebnis


def modernisierung_beginnverzoegerung(
    ankuendigungszugang_am=None, angekuendigter_beginn_am=None,
    tatsaechlicher_beginn_am=None, prueftag=None, zeitnachweis=None,
):
    """§559d Nummer1: Beginn binnen zwölf Monaten, ersatzweise ab Ankündigungszugang."""
    zugang = _datum(ankuendigungszugang_am, "ankuendigungszugang_am")
    angekuendigt = _datum(angekuendigter_beginn_am, "angekuendigter_beginn_am") if angekuendigter_beginn_am is not None else None
    tatsaechlich = _datum(tatsaechlicher_beginn_am, "tatsaechlicher_beginn_am") if tatsaechlicher_beginn_am is not None else None
    tag = _datum(prueftag, "prueftag")
    _text(zeitnachweis, "zeitnachweis")
    if tag < zugang:
        _fehler("prueftag", "Prüftag darf nicht vor Ankündigungszugang liegen.")
    if tatsaechlich is not None and tatsaechlich > tag:
        _fehler("tatsaechlicher_beginn_am", "Tatsächlicher Beginn darf nicht erst nach dem Prüftag liegen.")
    basis = angekuendigt if angekuendigt is not None else zugang
    ende = _frist(basis.isoformat(), 12, "monate", "ereignis")
    verzoegert = tatsaechlich > ende if tatsaechlich is not None else tag > ende
    eingaben = dict(ankuendigungszugang_am=ankuendigungszugang_am,
        angekuendigter_beginn_am=angekuendigter_beginn_am, tatsaechlicher_beginn_am=tatsaechlicher_beginn_am,
        prueftag=prueftag, zeitnachweis=zeitnachweis)
    wert = dict(anknuepfung_am=basis.isoformat(), zwoelfmonatsgrenze=ende.isoformat(),
        beginnverzoegerung_nummer_1=verzoegert)
    return _verzoegerungs_ergebnis(wert, "BGB_MODERNISIERUNG_BEGINNVERZOEGERUNG", eingaben,
        "Angekündigten Beginn vorrangig, nur bei fehlender Angabe Ankündigungszugang verwenden; tatsächlichen Beginn oder Prüftag mit Zwölfmonatsgrenze vergleichen")


def modernisierung_arbeitsruhe(
    ruhebeginn_am=None, beginnart=None, wiederaufnahme_am=None,
    prueftag=None, zeitnachweis=None,
):
    """§559d Nummer4: einzelne ununterbrochene Arbeitsruhe strikt länger als zwölf Monate."""
    ruhe = _datum(ruhebeginn_am, "ruhebeginn_am")
    _auswahl(beginnart, "beginnart", ("ereignis", "tagesbeginn"))
    wieder = _datum(wiederaufnahme_am, "wiederaufnahme_am") if wiederaufnahme_am is not None else None
    tag = _datum(prueftag, "prueftag")
    _text(zeitnachweis, "zeitnachweis")
    if tag < ruhe:
        _fehler("prueftag", "Prüftag darf nicht vor Beginn der Arbeitsruhe liegen.")
    if wieder is not None and (wieder < ruhe or wieder > tag):
        _fehler("wiederaufnahme_am", "Wiederaufnahme muss zwischen Ruhebeginn und Prüftag liegen.")
    grenze = _frist(ruhebeginn_am, 12, "monate", beginnart)
    letzter_ruhetag = _tage_addieren(wieder, -1) if wieder is not None else tag
    wert = dict(zwoelfmonatsgrenze=grenze.isoformat(), letzter_beruecksichtigter_ruhetag=letzter_ruhetag.isoformat(),
        arbeitsruhe_nummer_4=letzter_ruhetag > grenze)
    eingaben = dict(ruhebeginn_am=ruhebeginn_am, beginnart=beginnart,
        wiederaufnahme_am=wiederaufnahme_am, prueftag=prueftag, zeitnachweis=zeitnachweis)
    return _verzoegerungs_ergebnis(wert, "BGB_MODERNISIERUNG_ARBEITSRUHE", eingaben,
        "Ununterbrochene Arbeitsruhe bis Prüftagsschluss oder Vortag tagbeginnlicher Wiederaufnahme; strikt mehr als zwölf Monate verlangen")
