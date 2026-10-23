"""Gegenleistungsbeträge nach §326 Absätze2 und3, getrennte gesetzliche Wege."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _fehler, _text
from .zahlen import _bruch, _dividieren, _multiplizieren, _subtrahieren


def gegenleistung_behaltensbetrag(
    vereinbarte_gegenleistung=None, ersparte_aufwendungen=None, anderweitiger_erwerb=None,
    boeswillig_unterlassener_erwerb=None, leistungsbefreiung_nach_275=None,
    glaeubiger_allein_oder_weit_ueberwiegend_verantwortlich=None,
    schuldner_hat_umstand_zu_vertreten=None, annahmeverzug_bei_eintritt=None,
    bewertungsnachweis=None,
):
    """§326 Absatz2: Behaltensgrund und drei gesetzliche Anrechnungen."""
    preis = _geld(vereinbarte_gegenleistung)
    erspart, erwerb = _geld(ersparte_aufwendungen), _geld(anderweitiger_erwerb)
    unterlassen = _geld(boeswillig_unterlassener_erwerb)
    eingaben = dict(vereinbarte_gegenleistung=vereinbarte_gegenleistung,
        ersparte_aufwendungen=ersparte_aufwendungen, anderweitiger_erwerb=anderweitiger_erwerb,
        boeswillig_unterlassener_erwerb=boeswillig_unterlassener_erwerb,
        leistungsbefreiung_nach_275=leistungsbefreiung_nach_275,
        glaeubiger_allein_oder_weit_ueberwiegend_verantwortlich=glaeubiger_allein_oder_weit_ueberwiegend_verantwortlich,
        schuldner_hat_umstand_zu_vertreten=schuldner_hat_umstand_zu_vertreten,
        annahmeverzug_bei_eintritt=annahmeverzug_bei_eintritt, bewertungsnachweis=bewertungsnachweis)
    for name in tuple(eingaben)[4:-1]:
        _wahrheitswert(eingaben[name], name)
    _text(bewertungsnachweis, "bewertungsnachweis")
    behalten = leistungsbefreiung_nach_275 and (
        glaeubiger_allein_oder_weit_ueberwiegend_verantwortlich
        or (not schuldner_hat_umstand_zu_vertreten and annahmeverzug_bei_eintritt))
    wert = None
    if behalten:
        wert = max(_subtrahieren(_subtrahieren(_subtrahieren(preis, erspart), erwerb), unterlassen), _bruch(0))
    ergebnis = _geld_ergebnis(wert, "BGB_GEGENLEISTUNG_BEHALTENSBETRAG", eingaben,
        [dict(operation="Behaltensgrund aus Verantwortlichkeit oder Annahmeverzug prüfen; Ersparnis, Erwerb und böswillig unterlassenen Erwerb abziehen")])
    ergebnis["hinweise"].append("Nur§326 Absatz2. NICHT_ANWENDBAR bedeutet fehlenden Behaltensgrund in diesem Modell, nicht automatisch endgültige Gegenleistung0. Teilbefreiung, bloß ausgeschlossene Nacherfüllung, Ersatzverlangen nach Absatz3 und Sonderregeln gesondert.")
    return ergebnis


def gegenleistung_bei_ersatzverlangen(
    vereinbarte_gegenleistung=None, wert_geschuldeter_leistung=None,
    wert_ersatz_oder_ersatzanspruch=None, ersatz_nach_285_verlangt=None,
    bewertungsnachweis=None,
):
    """§326 Absatz3: Gegenleistung nach relativem Wert des verlangten Ersatzes."""
    preis, leistungswert = _geld(vereinbarte_gegenleistung), _geld(wert_geschuldeter_leistung)
    ersatz = _geld(wert_ersatz_oder_ersatzanspruch)
    if leistungswert <= 0:
        _fehler("wert_geschuldeter_leistung", "Positiver Vergleichswert erforderlich.")
    _wahrheitswert(ersatz_nach_285_verlangt, "ersatz_nach_285_verlangt")
    _text(bewertungsnachweis, "bewertungsnachweis")
    eingaben = dict(vereinbarte_gegenleistung=vereinbarte_gegenleistung,
        wert_geschuldeter_leistung=wert_geschuldeter_leistung,
        wert_ersatz_oder_ersatzanspruch=wert_ersatz_oder_ersatzanspruch,
        ersatz_nach_285_verlangt=ersatz_nach_285_verlangt, bewertungsnachweis=bewertungsnachweis)
    wert = None
    if ersatz_nach_285_verlangt:
        wert = _multiplizieren(preis, _dividieren(min(ersatz, leistungswert), leistungswert))
    ergebnis = _geld_ergebnis(wert, "BGB_GEGENLEISTUNG_BEI_ERSATZVERLANGEN", eingaben,
        [dict(operation="Bei Ersatzverlangen Gegenleistung im Verhältnis des niedrigeren Ersatzwerts zum Wert der geschuldeten Leistung herabsetzen")])
    ergebnis["hinweise"].append("Nur§326 Absatz3 in Verbindung mit§441 Absatz3. Höherer Ersatzwert erhöht die Gegenleistung nicht. Ersatzanspruch und konsistente Vergleichswerte rechtlich bestimmen; kein automatischer Anspruch auf Versicherungserlös oder sonstige Zahlungen.")
    return ergebnis
