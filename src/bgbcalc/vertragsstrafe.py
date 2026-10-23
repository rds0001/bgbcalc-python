"""Verwirkung und Schadensmindestbetrag der Vertragsstrafe (§§339–341)."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _auswahl, _ergebnis, _text
from .zahlen import _bruch, _subtrahieren
from .zinsen import _bruchteile




def vertragsstrafe_schadensmindestbetrag(
    strafbetrag=None, ersatzfaehiger_schaden=None, strafart=None, strafe_verwirkt=None,
    erfuellung_angenommen=None, vorbehalt_bei_annahme=None,
    schadensersatzanspruch_besteht=None, bewertungsnachweis=None,
):
    """Vertragsstrafe als Mindestschaden, mit Annahmevorbehalt bei nicht gehöriger Erfüllung."""
    strafe = _geld(strafbetrag)
    schaden = _geld(ersatzfaehiger_schaden)
    _auswahl(strafart, "strafart", ("nichterfuellung", "nicht_gehoerige_erfuellung"))
    eingaben = dict(strafbetrag=strafbetrag, ersatzfaehiger_schaden=ersatzfaehiger_schaden,
        strafart=strafart, strafe_verwirkt=strafe_verwirkt, erfuellung_angenommen=erfuellung_angenommen,
        vorbehalt_bei_annahme=vorbehalt_bei_annahme, schadensersatzanspruch_besteht=schadensersatzanspruch_besteht,
        bewertungsnachweis=bewertungsnachweis)
    for name in tuple(eingaben)[3:-1]:
        _wahrheitswert(eingaben[name], name)
    _text(bewertungsnachweis, "bewertungsnachweis")
    vorbehalt_noetig = strafart == "nicht_gehoerige_erfuellung" and erfuellung_angenommen
    strafe_verlangbar = strafe_verwirkt and (not vorbehalt_noetig or vorbehalt_bei_annahme)
    mindest = strafe if strafe_verlangbar else _bruch(0)
    ersatz = schaden if schadensersatzanspruch_besteht else _bruch(0)
    gesamt = max(mindest, ersatz)
    ergebnis = _geld_ergebnis(gesamt, "BGB_VERTRAGSSTRAFE_SCHADENSMINDESTBETRAG", eingaben,
        [dict(operation="Verlangbare Strafe als Mindestbetrag; zusätzlichen Schaden nur oberhalb der Strafe berücksichtigen")])
    ergebnis["wert"] = dict(strafe_nach_diesen_voraussetzungen_verlangbar=strafe_verlangbar,
        strafmindestbetrag=_bruchteile(mindest), weiterer_schadensbetrag=_bruchteile(_subtrahieren(gesamt, mindest)),
        gesamtbetrag=_bruchteile(gesamt))
    ergebnis["hinweise"].append("Nur derselbe von der Strafe erfasste Nichterfüllungs-/Schlechterfüllungsschaden; keine Addition voller Strafe und voller Schadenhöhe. Wirksamer gegebenenfalls herabgesetzter Strafbetrag vorgegeben. Erfüllungsanspruch, dessen Ausschluss durch Erklärung§340 Absatz1 und sonstige Einwendungen separat. Fehlender Vorbehalt beseitigt hier die Strafe, nicht automatisch einen unabhängig bestehenden Schadensersatzanspruch.")
    return ergebnis
