"""Sicherheiten und Sachschaden aus expliziten deutschen Bewertungseingaben."""
from .kalender import _auswahl, _ergebnis, _fehler, _text, _vorhanden
from .zahlen import _addieren, _bruch, _zahleneingabe, _multiplizieren, _subtrahieren, _vergleichen


def _wahrheitswert(wert, parameter):
    _vorhanden(wert, parameter)
    if type(wert) is not bool:
        _fehler(parameter, "Expliziter Wahrheitswert erforderlich.")
    return wert


def _geld(wert):
    betrag = _zahleneingabe(wert)
    if betrag < 0:
        _fehler("betrag", "Nichtnegativer Geldbetrag erforderlich.")
    return betrag


def _geld_ergebnis(wert, regel_id, eingaben, schritte, nutzervorgaben=None):
    ausgabe = None if wert is None else {
        "zaehler": str(wert.numerator), "nenner": str(wert.denominator)
    }
    vorgaben = dict(eingaben)
    vorgaben.update(nutzervorgaben or {})
    ergebnis = _ergebnis(ausgabe, "EUR", regel_id, eingaben, schritte, vorgaben)
    ergebnis["status"] = "NICHT_ANWENDBAR" if wert is None else "BERECHNET"
    ergebnis["annahmen"] = ["Berechnung anhand der festen BGB-Fassung und der ausdrücklich eingegebenen Tatsachen und rechtlichen Bewertungen."]
    ergebnis["hinweise"] = ["Bewertungen stammen vom Nutzer; exaktes Bruchergebnis ohne automatische Cent-Rundung."]
    return ergebnis


def wertpapier_sicherheitswert(kurswert=None, papierart=None, gattung_zulaessig=None,
                              scheine_hinterlegt=None, gattungsnachweis=None):
    """§ 234: drei Viertel des Kurswerts bei erfüllten Geeignetheitsbedingungen."""
    betrag = _geld(kurswert)
    _auswahl(papierart, "papierart", ("inhaberpapier", "blanko_orderpapier", "sonstiges"))
    _wahrheitswert(gattung_zulaessig, "gattung_zulaessig")
    _wahrheitswert(scheine_hinterlegt, "scheine_hinterlegt")
    _text(gattungsnachweis, "gattungsnachweis")
    geeignet = papierart != "sonstiges" and gattung_zulaessig and scheine_hinterlegt
    wert = _multiplizieren(betrag, _bruch(3, 4)) if geeignet else None
    return _geld_ergebnis(wert, "BGB_SICHERHEIT_WERTPAPIER", dict(
        kurswert=kurswert, papierart=papierart, gattung_zulaessig=gattung_zulaessig,
        scheine_hinterlegt=scheine_hinterlegt, gattungsnachweis=gattungsnachweis
    ), [{"operation": "Geeignetheit prüfen; bei Geeignetheit Kurswert mal 3/4", "geeignet": geeignet}],
        {"gattungsnachweis": gattungsnachweis})


def buchforderung_sicherheitswert(kurswert=None, schuldnerart=None):
    """§ 236: Kurswert der auszuhändigenden Papiere, nicht Forderungsnominalwert."""
    betrag = _geld(kurswert)
    _auswahl(schuldnerart, "schuldnerart", ("bund", "land", "sonstiges"))
    wert = None if schuldnerart == "sonstiges" else _multiplizieren(betrag, _bruch(3, 4))
    return _geld_ergebnis(wert, "BGB_SICHERHEIT_BUCHFORDERUNG",
                         dict(kurswert=kurswert, schuldnerart=schuldnerart),
                         [{"operation": "Bund/Land prüfen; Kurswert mal 3/4"}])


def sach_sicherheitswert(schaetzungswert=None, verderb_zu_besorgen=None,
                        aufbewahrung_schwierig=None, zurueckweisung_erklaert=None):
    """§ 237: zwei Drittel; Zurückweisungsgrund allein bewirkt keine Zurückweisung."""
    betrag = _geld(schaetzungswert)
    _wahrheitswert(verderb_zu_besorgen, "verderb_zu_besorgen")
    _wahrheitswert(aufbewahrung_schwierig, "aufbewahrung_schwierig")
    _wahrheitswert(zurueckweisung_erklaert, "zurueckweisung_erklaert")
    if zurueckweisung_erklaert and not (verderb_zu_besorgen or aufbewahrung_schwierig):
        _fehler("zurueckweisung_erklaert", "Gesetzlicher Zurückweisungsgrund fehlt.")
    wert = None if zurueckweisung_erklaert else _multiplizieren(betrag, _bruch(2, 3))
    return _geld_ergebnis(wert, "BGB_SICHERHEIT_SACHE", dict(
        schaetzungswert=schaetzungswert, verderb_zu_besorgen=verderb_zu_besorgen,
        aufbewahrung_schwierig=aufbewahrung_schwierig,
        zurueckweisung_erklaert=zurueckweisung_erklaert
    ), [{"operation": "Erklärte Zurückweisung prüfen; sonst Schätzungswert mal 2/3"}])


def sicherheit_ergaenzungsbetrag(erforderliche_sicherheit=None, vorhandener_sicherheitswert=None,
                                verschulden_berechtigter=None):
    """§ 240: positive Deckungslücke bei fehlendem Berechtigtenverschulden."""
    erforderlich, vorhanden = _geld(erforderliche_sicherheit), _geld(vorhandener_sicherheitswert)
    _wahrheitswert(verschulden_berechtigter, "verschulden_berechtigter")
    wert = None if verschulden_berechtigter else max(_subtrahieren(erforderlich, vorhanden), _bruch(0))
    return _geld_ergebnis(wert, "BGB_SICHERHEIT_ERGAENZUNG", dict(
        erforderliche_sicherheit=erforderliche_sicherheit,
        vorhandener_sicherheitswert=vorhandener_sicherheitswert,
        verschulden_berechtigter=verschulden_berechtigter
    ), [{"operation": "Ohne Berechtigtenverschulden positive Deckungslücke"}])


def sachschaden_ersatzbetrag(erforderlicher_nettobetrag=None,
                            ersatzfaehige_angefallene_umsatzsteuer=None, mitverschuldensquote=None):
    """§§ 249, 254: ersatzfähiger Aufwand nach vorgegebener Mitverschuldensquote."""
    netto = _geld(erforderlicher_nettobetrag)
    steuer = _geld(ersatzfaehige_angefallene_umsatzsteuer)
    quote = _zahleneingabe(mitverschuldensquote)
    if _vergleichen(quote, _bruch(0)) < 0 or _vergleichen(quote, _bruch(1)) > 0:
        _fehler("mitverschuldensquote", "Quote muss zwischen null und eins liegen.")
    gesamt = _addieren(netto, steuer)
    restquote = _subtrahieren(_bruch(1), quote)
    wert = _multiplizieren(gesamt, restquote)
    return _geld_ergebnis(wert, "BGB_SACHSCHADEN_BETRAG", dict(
        erforderlicher_nettobetrag=erforderlicher_nettobetrag,
        ersatzfaehige_angefallene_umsatzsteuer=ersatzfaehige_angefallene_umsatzsteuer,
        mitverschuldensquote=mitverschuldensquote
    ), [{"operation": "Erforderlicher Nettoaufwand plus ersatzfähige angefallene Steuer"},
        {"operation": "Mit dem verbleibenden Haftungsanteil multiplizieren"}],
        {"mitverschuldensquote": mitverschuldensquote,
         "bewertung": "Vorgegeben; keine automatische rechtliche Abwägung."})
