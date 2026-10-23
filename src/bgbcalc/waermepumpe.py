"""Kostenansatz der Wärmepumpe nach § 559f; kein fertiger Mieterhöhungsbetrag."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _ganzzahl, _text
from .zahlen import _bruch, _multiplizieren, _zahleneingabe
from .zinsen import _bruchteile


def waermepumpe_kostenansatz(
    kosten_wohnung=None, errichtungsjahr=None, jahresarbeitszahl=None,
    fachunternehmernachweis_ordnungsgemaess=None, waermeschutz_ausnahme_erfuellt=None,
    sanierungsstandard_erfuellt=None, vorlauftemperatur=None,
    beheizbarkeit_bei_normaussentemperatur=None, bewertungsnachweis=None,
    waermepumpenregel_anwendbar=None,
):
    """§ 559f: Nachweis oder Gebäudeausnahme, sonst halber Kostenansatz."""
    eingaben = dict(kosten_wohnung=kosten_wohnung, errichtungsjahr=errichtungsjahr,
        jahresarbeitszahl=jahresarbeitszahl,
        fachunternehmernachweis_ordnungsgemaess=fachunternehmernachweis_ordnungsgemaess,
        waermeschutz_ausnahme_erfuellt=waermeschutz_ausnahme_erfuellt,
        sanierungsstandard_erfuellt=sanierungsstandard_erfuellt,
        vorlauftemperatur=vorlauftemperatur,
        beheizbarkeit_bei_normaussentemperatur=beheizbarkeit_bei_normaussentemperatur,
        bewertungsnachweis=bewertungsnachweis,
        waermepumpenregel_anwendbar=waermepumpenregel_anwendbar)
    kosten = _geld(kosten_wohnung)
    jahr = _ganzzahl(errichtungsjahr, "errichtungsjahr", 1, 9999)
    _text(bewertungsnachweis, "bewertungsnachweis")
    for name in ("fachunternehmernachweis_ordnungsgemaess", "waermeschutz_ausnahme_erfuellt",
                 "sanierungsstandard_erfuellt", "beheizbarkeit_bei_normaussentemperatur",
                 "waermepumpenregel_anwendbar"):
        _wahrheitswert(eingaben[name], name)
    arbeitszahl = None
    if jahresarbeitszahl is not None or fachunternehmernachweis_ordnungsgemaess:
        arbeitszahl = _geld(jahresarbeitszahl)
    temperatur = None
    if vorlauftemperatur is not None or beheizbarkeit_bei_normaussentemperatur:
        temperatur = _zahleneingabe(vorlauftemperatur)
    nachweis = fachunternehmernachweis_ordnungsgemaess and arbeitszahl >= _bruch(5, 2)
    ausnahme = (jahr > 1996 or waermeschutz_ausnahme_erfuellt or sanierungsstandard_erfuellt
                or (beheizbarkeit_bei_normaussentemperatur and temperatur <= _bruch(55)))
    faktor = _bruch(1) if nachweis or ausnahme else _bruch(1, 2)
    ergebnis = _geld_ergebnis(None, "BGB_WAERMEPUMPE_KOSTENANSATZ", eingaben,
        [dict(operation="Jahresarbeitszahlnachweis und vier Gebäudeausnahmen prüfen; vollen oder halben Kostenansatz bilden")])
    if waermepumpenregel_anwendbar:
        ergebnis["wert"] = dict(jahresarbeitszahlnachweis_ausreichend=nachweis,
            gebaeudeausnahme_erfuellt=ausnahme, kostenfaktor=_bruchteile(faktor),
            kostenansatz=_bruchteile(_multiplizieren(kosten, faktor)))
        ergebnis["status"] = "BERECHNET"
    ergebnis["hinweise"].append("Nur § 559f: Kostenansatz vor weiteren gesetzlichen Abzügen und Kappungen; kein endgültiger Erhöhungsbetrag. Keine Berechnung der Jahresarbeitszahl nach VDI.")
    return ergebnis
