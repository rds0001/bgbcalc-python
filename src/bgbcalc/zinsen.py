"""Zinsoperationen mit belegtem Jahresanteil und ausdrücklich gelieferten Sätzen."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _auswahl, _datum, _fehler, _ganzzahl, _text
from .zahlen import (
    GRENZE, _addieren, _bruch, _zahleneingabe, _multiplizieren, _subtrahieren,
)


def _zeitanteil(zaehler, nenner, nachweis):
    _ganzzahl(zaehler, "zeitanteil_zaehler", 0, GRENZE)
    _ganzzahl(nenner, "zeitanteil_nenner", 1, GRENZE)
    _text(nachweis, "zeitanteil_nachweis")
    return _bruch(zaehler, nenner)


def _bruchteile(wert):
    return {"zaehler": str(wert.numerator), "nenner": str(wert.denominator)}


def basiszinssatz_fortschreibung(bisheriger_basiszinssatz_prozent=None,
                                bisheriger_bezugszinssatz_prozent=None,
                                neuer_bezugszinssatz_prozent=None,
                                anpassungsdatum=None, quellenangabe=None):
    """§ 247: Änderung der Bezugsgröße auf den bisherigen Basiszins anwenden."""
    basis = _zahleneingabe(bisheriger_basiszinssatz_prozent)
    alt = _zahleneingabe(bisheriger_bezugszinssatz_prozent)
    neu = _zahleneingabe(neuer_bezugszinssatz_prozent)
    tag = _datum(anpassungsdatum, "anpassungsdatum")
    _text(quellenangabe, "quellenangabe")
    if tag.day != 1 or tag.month not in (1, 7):
        _fehler("anpassungsdatum", "Anpassung nur zum 1. Januar oder 1. Juli.")
    aenderung = _subtrahieren(neu, alt)
    wert = _addieren(basis, aenderung)
    ergebnis = _geld_ergebnis(wert, "BGB_BASISZINS_FORTSCHREIBUNG", dict(
        bisheriger_basiszinssatz_prozent=bisheriger_basiszinssatz_prozent,
        bisheriger_bezugszinssatz_prozent=bisheriger_bezugszinssatz_prozent,
        neuer_bezugszinssatz_prozent=neuer_bezugszinssatz_prozent,
        anpassungsdatum=anpassungsdatum, quellenangabe=quellenangabe
    ), [{"operation": "Änderung der Bezugsgröße", "prozentpunkte": _bruchteile(aenderung)},
        {"operation": "Änderung zum bisherigen Basiszins addieren"}], {"quellenangabe": quellenangabe})
    ergebnis["einheit"] = "prozent_pro_jahr"
    ergebnis["hinweise"] = ["Fortschreibung vorgegebener Werte; keine amtliche Feststellung oder aktuelle Zeitreihe."]
    return ergebnis


def gesetzliche_zinsen(kapital=None, zeitanteil_zaehler=None, zeitanteil_nenner=None,
                      zeitanteil_nachweis=None, glaeubigerverzug=None,
                      abweichender_zinssatz_prozent=None):
    """§§ 246/301: einfache Zinsen für einen belegten, einheitlichen Jahresanteil."""
    hauptbetrag = _geld(kapital)
    anteil = _zeitanteil(zeitanteil_zaehler, zeitanteil_nenner, zeitanteil_nachweis)
    _wahrheitswert(glaeubigerverzug, "glaeubigerverzug")
    zinssatz = _bruch(4) if abweichender_zinssatz_prozent is None else _zahleneingabe(abweichender_zinssatz_prozent)
    wert = None if glaeubigerverzug else _multiplizieren(
        _multiplizieren(hauptbetrag, _multiplizieren(zinssatz, _bruch(1, 100))), anteil)
    return _geld_ergebnis(wert, "BGB_GESETZLICHE_ZINSEN", dict(
        kapital=kapital, zeitanteil_zaehler=zeitanteil_zaehler, zeitanteil_nenner=zeitanteil_nenner,
        zeitanteil_nachweis=zeitanteil_nachweis, glaeubigerverzug=glaeubigerverzug,
        abweichender_zinssatz_prozent=abweichender_zinssatz_prozent
    ), [{"operation": "Jahreszinssatz bestimmen", "zinssatz_prozent": _bruchteile(zinssatz)},
        {"operation": "Ohne Gläubigerverzug Kapital mal Zinssatz/100 mal Jahresanteil"}],
        {"zeitanteil_nachweis": zeitanteil_nachweis,
         "abweichender_zinssatz_prozent": abweichender_zinssatz_prozent})


def verzugszinsen(kapital=None, basiszinssatz_prozent=None, zeitanteil_zaehler=None,
                 zeitanteil_nenner=None, zeitanteil_nachweis=None, entgeltforderung=None,
                 verbraucher_beteiligt=None, zinsschuld=None, glaeubigerverzug=None,
                 verzugsart=None, hoeherer_zinssatz_prozent=None, basiszinsnachweis=None):
    """§§ 288/289/497: gesetzlicher Verzugszins für einen einheitlichen Zeitanteil."""
    eingaben = dict(
        kapital=kapital, basiszinssatz_prozent=basiszinssatz_prozent,
        zeitanteil_zaehler=zeitanteil_zaehler, zeitanteil_nenner=zeitanteil_nenner,
        zeitanteil_nachweis=zeitanteil_nachweis, entgeltforderung=entgeltforderung,
        verbraucher_beteiligt=verbraucher_beteiligt, zinsschuld=zinsschuld,
        glaeubigerverzug=glaeubigerverzug, verzugsart=verzugsart,
        hoeherer_zinssatz_prozent=hoeherer_zinssatz_prozent, basiszinsnachweis=basiszinsnachweis
    )
    hauptbetrag, basis = _geld(kapital), _zahleneingabe(basiszinssatz_prozent)
    anteil = _zeitanteil(zeitanteil_zaehler, zeitanteil_nenner, zeitanteil_nachweis)
    _text(basiszinsnachweis, "basiszinsnachweis")
    for parameter in ("entgeltforderung", "verbraucher_beteiligt", "zinsschuld", "glaeubigerverzug"):
        _wahrheitswert(eingaben[parameter], parameter)
    _auswahl(verzugsart, "verzugsart", ("allgemein", "verbraucherdarlehen", "immobiliar_verbraucherdarlehen"))
    if verzugsart == "immobiliar_verbraucherdarlehen":
        aufschlag = _bruch(5, 2)
    elif verzugsart == "verbraucherdarlehen":
        aufschlag = _bruch(5)
    else:
        aufschlag = _bruch(9 if entgeltforderung and not verbraucher_beteiligt else 5)
    zinssatz = _addieren(basis, aufschlag)
    if hoeherer_zinssatz_prozent is not None:
        if verzugsart != "allgemein":
            _fehler("hoeherer_zinssatz_prozent", "Abweichender Schaden nach § 497 gesondert zu prüfen.")
        zinssatz = max(zinssatz, _zahleneingabe(hoeherer_zinssatz_prozent))
    wert = None if zinsschuld or glaeubigerverzug else _multiplizieren(
        _multiplizieren(hauptbetrag, _multiplizieren(zinssatz, _bruch(1, 100))), anteil)
    return _geld_ergebnis(wert, "BGB_VERZUGSZINSEN", eingaben,
        [{"operation": "Gesetzlichen Aufschlag auswählen", "prozentpunkte": _bruchteile(aufschlag)},
         {"operation": "Basiszins und gegebenenfalls höheren anderen Satz berücksichtigen",
          "zinssatz_prozent": _bruchteile(zinssatz)},
         {"operation": "Zinsschuld/Gläubigerverzug ausschließen; Kapital mal Zinssatz/100 mal Jahresanteil"}],
        {"basiszinsnachweis": basiszinsnachweis, "zeitanteil_nachweis": zeitanteil_nachweis})


def verzug_nebenkosten(rechtsverfolgungsschaden=None, entgeltforderung=None,
                      schuldner_verbraucher=None, schuldnerverzug=None):
    """§ 288 Abs. 5: 40-Euro-Pauschale mit Anrechnung auf Rechtsverfolgungsschaden."""
    kosten = _geld(rechtsverfolgungsschaden)
    _wahrheitswert(entgeltforderung, "entgeltforderung")
    _wahrheitswert(schuldner_verbraucher, "schuldner_verbraucher")
    _wahrheitswert(schuldnerverzug, "schuldnerverzug")
    anwendbar = entgeltforderung and not schuldner_verbraucher and schuldnerverzug
    wert = max(kosten, _bruch(40)) if anwendbar else None
    schritte = [{"operation": "Pauschalenvoraussetzungen", "anwendbar": anwendbar}]
    if anwendbar:
        schritte.append({"operation": "40 EUR Pauschale auf Rechtsverfolgungsschaden anrechnen",
                         "anrechnung": _bruchteile(min(kosten, _bruch(40)))})
    return _geld_ergebnis(wert, "BGB_VERZUG_NEBENKOSTEN", dict(
        rechtsverfolgungsschaden=rechtsverfolgungsschaden, entgeltforderung=entgeltforderung,
        schuldner_verbraucher=schuldner_verbraucher, schuldnerverzug=schuldnerverzug
    ), schritte)
