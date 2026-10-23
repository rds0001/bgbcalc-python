"""Jahresanteilige Erstattung üblicher Kosten einer Bauhandwerkersicherheit."""

from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _auswahl
from .zahlen import _bruch, _multiplizieren
from .zinsen import _bruchteile, _zeitanteil


def bau_sicherungskosten_erstattung(
    sicherheitsbetrag=None,
    tatsaechliche_kosten=None,
    uebliche_kosten=None,
    zeitanteil_zaehler=None,
    zeitanteil_nenner=None,
    zeitanteil_nachweis=None,
    sicherheit_nach_650f=None,
    aufrechterhaltung_wegen_unbegruendeter_einwendungen=None,
    bestellerart=None,
    baubetreuer_bevollmaechtigt=None,
):
    """§ 650f Abs. 3/6: entstandene übliche Kosten bis zwei Prozent pro Jahr."""
    eingaben = dict(
        sicherheitsbetrag=sicherheitsbetrag,
        tatsaechliche_kosten=tatsaechliche_kosten,
        uebliche_kosten=uebliche_kosten,
        zeitanteil_zaehler=zeitanteil_zaehler,
        zeitanteil_nenner=zeitanteil_nenner,
        zeitanteil_nachweis=zeitanteil_nachweis,
        sicherheit_nach_650f=sicherheit_nach_650f,
        aufrechterhaltung_wegen_unbegruendeter_einwendungen=aufrechterhaltung_wegen_unbegruendeter_einwendungen,
        bestellerart=bestellerart,
        baubetreuer_bevollmaechtigt=baubetreuer_bevollmaechtigt,
    )
    betrag = _geld(sicherheitsbetrag)
    kosten, ueblich = _geld(tatsaechliche_kosten), _geld(uebliche_kosten)
    zeit = _zeitanteil(zeitanteil_zaehler, zeitanteil_nenner, zeitanteil_nachweis)
    for parameter in ("sicherheit_nach_650f", "aufrechterhaltung_wegen_unbegruendeter_einwendungen",
                      "baubetreuer_bevollmaechtigt"):
        _wahrheitswert(eingaben[parameter], parameter)
    _auswahl(bestellerart, "bestellerart",
             ("sonstiger", "oeffentlich_insolvenzunfaehig", "verbraucherbau", "bautraeger_verbraucher"))
    anwendbar = (
        sicherheit_nach_650f and not aufrechterhaltung_wegen_unbegruendeter_einwendungen
        and bestellerart != "oeffentlich_insolvenzunfaehig"
        and (bestellerart == "sonstiger" or baubetreuer_bevollmaechtigt)
    )
    wert = None
    schritte = [{"operation": "Sicherheit, unbegründete Einwendungen und Bestellerausnahmen",
                 "anwendbar": anwendbar}]
    if anwendbar:
        hoechstbetrag = _multiplizieren(_multiplizieren(betrag, _bruch(1, 50)), zeit)
        wert = min(kosten, ueblich, hoechstbetrag)
        schritte.append({"operation": "Minimum aus tatsächlichen Kosten, üblichen Kosten und jahresanteiliger Zweiprozentgrenze",
                         "hoechstbetrag": _bruchteile(hoechstbetrag)})
    return _geld_ergebnis(wert, "BGB_BAU_SICHERUNGSKOSTEN_ERSTATTUNG", eingaben, schritte)
