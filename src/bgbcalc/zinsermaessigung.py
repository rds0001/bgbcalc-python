"""Jährlicher Zinsvorteil als Teilstufe einer Modernisierungsmieterhöhung."""

from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _fehler, _text
from .zahlen import _bruch, _zahleneingabe, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile


def modernisierung_zinsermaessigung(
    darlehensursprungsbetrag=None, ermaessigter_zinssatz_prozent=None,
    marktueblicher_zinssatz_prozent=None, marktzinssatz_nachweis=None,
    beruecksichtigungsfaehiges_darlehen=None, vereinfachtes_verfahren=None,
):
    """§ 559a Abs. 2/3: Zinsdifferenz für den ursprünglichen Darlehensbetrag."""
    ursprung = _geld(darlehensursprungsbetrag)
    ermaessigt = _zahleneingabe(ermaessigter_zinssatz_prozent)
    markt = _zahleneingabe(marktueblicher_zinssatz_prozent)
    _text(marktzinssatz_nachweis, "marktzinssatz_nachweis")
    if ermaessigt > markt:
        _fehler("ermaessigter_zinssatz_prozent", "Ermäßigungssatz darf den maßgeblichen Marktzinssatz nicht übersteigen.")
    _wahrheitswert(beruecksichtigungsfaehiges_darlehen, "beruecksichtigungsfaehiges_darlehen")
    _wahrheitswert(vereinfachtes_verfahren, "vereinfachtes_verfahren")
    anwendbar = beruecksichtigungsfaehiges_darlehen and not vereinfachtes_verfahren
    unterschied = _subtrahieren(markt, ermaessigt)
    wert = _multiplizieren(_multiplizieren(ursprung, unterschied), _bruch(1, 100)) if anwendbar else None
    return _geld_ergebnis(
        wert, "BGB_MODERNISIERUNG_ZINSERMAESSIGUNG",
        dict(darlehensursprungsbetrag=darlehensursprungsbetrag,
             ermaessigter_zinssatz_prozent=ermaessigter_zinssatz_prozent,
             marktueblicher_zinssatz_prozent=marktueblicher_zinssatz_prozent,
             marktzinssatz_nachweis=marktzinssatz_nachweis,
             beruecksichtigungsfaehiges_darlehen=beruecksichtigungsfaehiges_darlehen,
             vereinfachtes_verfahren=vereinfachtes_verfahren),
        [{"operation": "Berücksichtigungsfähiges Darlehen und Ausnahme des vereinfachten Verfahrens",
          "anwendbar": anwendbar},
         {"operation": "Ursprünglichen Darlehensbetrag mit jährlicher Zinsdifferenz multiplizieren",
          "zinsdifferenz_prozentpunkte": _bruchteile(unterschied)}],
    )
