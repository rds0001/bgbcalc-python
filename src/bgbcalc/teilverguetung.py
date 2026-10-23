"""Teilvergütung nach Dienstkündigung beziehungsweise besonderen Werkvertragsfällen."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _fehler, _ganzzahl, _text
from .zahlen import GRENZE, _addieren, _bruch, _multiplizieren, _subtrahieren


def _teilbetrag(gesamtverguetung, leistungsanteil_zaehler, leistungsanteil_nenner):
    betrag = _geld(gesamtverguetung)
    zaehler = _ganzzahl(leistungsanteil_zaehler, "leistungsanteil_zaehler", 0, GRENZE)
    nenner = _ganzzahl(leistungsanteil_nenner, "leistungsanteil_nenner", 1, GRENZE)
    if zaehler > nenner:
        _fehler("leistungsanteil_zaehler", "Leistungsanteil darf eins nicht übersteigen.")
    return _multiplizieren(betrag, _bruch(zaehler, nenner))


def dienstkuendigung_teilverguetung(
    gesamtverguetung=None, leistungsanteil_zaehler=None, leistungsanteil_nenner=None,
    interesseloser_verguetungsanteil=None, selbst_gekuendigt=None,
    durch_vertragsbruch_des_anderen_veranlasst=None, fremdkuendigung_durch_eigenen_vertragsbruch=None,
    kuendigung_nach_626_627_nach_dienstbeginn=None, bewertungsnachweis=None,
):
    """§628 Absatz1: anteilige Vergütung, gegebenenfalls Abzug interesselos gewordener Leistungen."""
    anteilig = _teilbetrag(gesamtverguetung, leistungsanteil_zaehler, leistungsanteil_nenner)
    interesselos = _geld(interesseloser_verguetungsanteil)
    if interesselos > anteilig:
        _fehler("interesseloser_verguetungsanteil", "Interesseloser Vergütungsanteil darf bisherige Teilvergütung nicht übersteigen.")
    eingaben = dict(gesamtverguetung=gesamtverguetung, leistungsanteil_zaehler=leistungsanteil_zaehler,
        leistungsanteil_nenner=leistungsanteil_nenner, interesseloser_verguetungsanteil=interesseloser_verguetungsanteil,
        selbst_gekuendigt=selbst_gekuendigt, durch_vertragsbruch_des_anderen_veranlasst=durch_vertragsbruch_des_anderen_veranlasst,
        fremdkuendigung_durch_eigenen_vertragsbruch=fremdkuendigung_durch_eigenen_vertragsbruch,
        kuendigung_nach_626_627_nach_dienstbeginn=kuendigung_nach_626_627_nach_dienstbeginn,
        bewertungsnachweis=bewertungsnachweis)
    for name in tuple(eingaben)[4:-1]:
        _wahrheitswert(eingaben[name], name)
    _text(bewertungsnachweis, "bewertungsnachweis")
    verlust = (selbst_gekuendigt and not durch_vertragsbruch_des_anderen_veranlasst) or fremdkuendigung_durch_eigenen_vertragsbruch
    wert = None
    if kuendigung_nach_626_627_nach_dienstbeginn:
        wert = _subtrahieren(anteilig, interesselos) if verlust else anteilig
    ergebnis = _geld_ergebnis(wert, "BGB_DIENSTKUENDIGUNG_TEILVERGUETUNG", eingaben,
        [dict(operation="Vergütung entsprechend bisheriger Leistung; bei gesetzlicher Verlustkonstellation den interesselos gewordenen Anteil abziehen")])
    ergebnis["hinweise"].append("Leistungsanteil und Interessenverlust rechtlich bewerten; keine automatische Zeitquote. Interessenverlust muss gerade infolge der Kündigung bestehen. Bloße Eigenkündigung führt nicht automatisch zum Verlust sämtlicher Vergütung. Vorausvergütungsrückzahlung§628 Absatz1 Satz3 und KündigungsschadenAbsatz2 separat; keine automatische Aufrechnung oder Aussage über andere Vergütungsregime.")
    return ergebnis


def werk_teilverguetung_und_auslagen(
    gesamtverguetung=None, leistungsanteil_zaehler=None, leistungsanteil_nenner=None,
    nicht_inbegriffene_auslagen=None, werkbeeintraechtigung_vor_abnahme=None,
    bestellerstoffmangel_oder_anweisung_ursaechlich=None, unternehmer_zu_vertretender_umstand=None,
    aufhebung_nach_643=None, kuendigung_nach_649=None, bewertungsnachweis=None,
):
    """§645 Absatz1 und§649 Absatz1: geleisteter Vergütungsanteil plus nicht inbegriffene Auslagen."""
    anteilig = _teilbetrag(gesamtverguetung, leistungsanteil_zaehler, leistungsanteil_nenner)
    auslagen = _geld(nicht_inbegriffene_auslagen)
    eingaben = dict(gesamtverguetung=gesamtverguetung, leistungsanteil_zaehler=leistungsanteil_zaehler,
        leistungsanteil_nenner=leistungsanteil_nenner, nicht_inbegriffene_auslagen=nicht_inbegriffene_auslagen,
        werkbeeintraechtigung_vor_abnahme=werkbeeintraechtigung_vor_abnahme,
        bestellerstoffmangel_oder_anweisung_ursaechlich=bestellerstoffmangel_oder_anweisung_ursaechlich,
        unternehmer_zu_vertretender_umstand=unternehmer_zu_vertretender_umstand,
        aufhebung_nach_643=aufhebung_nach_643, kuendigung_nach_649=kuendigung_nach_649,
        bewertungsnachweis=bewertungsnachweis)
    for name in tuple(eingaben)[4:-1]:
        _wahrheitswert(eingaben[name], name)
    _text(bewertungsnachweis, "bewertungsnachweis")
    werkfall = (werkbeeintraechtigung_vor_abnahme and bestellerstoffmangel_oder_anweisung_ursaechlich and
        not unternehmer_zu_vertretender_umstand)
    gilt = werkfall or aufhebung_nach_643 or kuendigung_nach_649
    ergebnis = _geld_ergebnis(_addieren(anteilig, auslagen) if gilt else None,
        "BGB_WERK_TEILVERGUETUNG_UND_AUSLAGEN", eingaben,
        [dict(operation="Werkbeeinträchtigung ohne mitwirkendes Unternehmervertretenmüssen oder qualifizierte Aufhebung/Kündigung; geleisteten Vergütungsanteil und nicht inbegriffene Auslagen addieren")])
    ergebnis["hinweise"].append("Nur gesetzliche Fälle§645 Absatz1/§649 Absatz1, nicht freie Bestellerkündigung§648. Leistungsanteil rechtlich bestimmen, keine automatische Zeitquote; in Vergütung enthaltene Auslagen nicht erneut addieren. Weitergehende Bestellerhaftung§645 Absatz2, Anzeige wesentlicher Anschlagsüberschreitung§649 Absatz2 und andere Schadenersatzansprüche separat.")
    return ergebnis


def werkkuendigung_wichtiger_grund_verguetung(
    verguetung_gekuendigter_umfang=None, leistungsanteil_zaehler=None,
    leistungsanteil_nenner=None, wichtiger_grund_wirksam_gekuendigt=None, bautraegervertrag=None, leistungsstandsnachweis=None,
):
    """§648a Absatz5: ausschließlich Vergütung für bis Kündigung erbrachten Teil."""
    anteilig = _teilbetrag(verguetung_gekuendigter_umfang, leistungsanteil_zaehler, leistungsanteil_nenner)
    _wahrheitswert(wichtiger_grund_wirksam_gekuendigt, "wichtiger_grund_wirksam_gekuendigt")
    _wahrheitswert(bautraegervertrag, "bautraegervertrag")
    _text(leistungsstandsnachweis, "leistungsstandsnachweis")
    eingaben = dict(verguetung_gekuendigter_umfang=verguetung_gekuendigter_umfang,
        leistungsanteil_zaehler=leistungsanteil_zaehler, leistungsanteil_nenner=leistungsanteil_nenner,
        wichtiger_grund_wirksam_gekuendigt=wichtiger_grund_wirksam_gekuendigt,
        bautraegervertrag=bautraegervertrag, leistungsstandsnachweis=leistungsstandsnachweis)
    ergebnis = _geld_ergebnis(anteilig if wichtiger_grund_wirksam_gekuendigt and not bautraegervertrag else None,
        "BGB_WERKKUENDIGUNG_WICHTIGER_GRUND_VERGUETUNG", eingaben,
        [dict(operation="Vergütung des gekündigten Umfangs mit Anteil der bis zur Kündigung erbrachten Leistung multiplizieren")])
    ergebnis["hinweise"].append("Nur wirksame Kündigung aus wichtigem Grund§648a, kein Bauträgervertrag gemäß§650u Absatz2; keine Fünfprozentvermutung oder Vergütung für nicht erbrachten Teil aus§648 übertragen. Bei Teilkündigung ausschließlich abgegrenzten gekündigten Umfang bewerten. Leistungsstand und Beweislast§648a Absatz4 rechtlich bestimmen; SchadenersatzAbsatz6 und Vergütung fortgesetzter Teile separat.")
    return ergebnis
