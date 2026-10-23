"""Stichtagsbezogene Hemmungstatbestände der §§207/208."""
from .betraege import _wahrheitswert
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _text, lebensalter_beginn


def _schutz_ergebnis(wert, kennung, eingaben):
    ergebnis = _ergebnis(wert, "wahrheitswerte", kennung, eingaben,
        [dict(operation="Gesetzliche Personenbeziehung und Alters- beziehungsweise Gemeinschaftsvoraussetzungen am Stichtag verknüpfen")], eingaben.copy())
    ergebnis["annahmen"] = ["Anspruchsrichtung, Rechtsbeziehung und Tatsachen am Stichtag rechtlich bestimmt; feste lokale BGB-Fassung."]
    ergebnis["hinweise"] = ["Nur Hemmungstatbestand am angegebenen Stichtag, keine Summe von Hemmungstagen und kein endgültiger Verjährungstag. Andere Hemmungsgründe bleiben selbst bei negativem Ergebnis möglich.", "Eine bereits vor Eintritt eines Hemmungsgrundes abgelaufene Verjährung wird nicht wiederbelebt. Rechtliche Fristlage und Änderungen während des gesamten Zeitraums gesondert prüfen."]
    return ergebnis


def verjaehrung_familienhemmung(
    beziehungsart=None, rechtsbeziehung_besteht=None, stichtag=None,
    geburtsdatum_kind=None, einordnungsnachweis=None,
):
    """§207: Beziehung und gegebenenfalls Vollendung des21.Lebensjahres prüfen."""
    _auswahl(beziehungsart, "beziehungsart", ("ehegatten", "lebenspartner", "kind_eltern",
        "kind_partner_elternteil", "vormund_muendel", "betreuer_betreuter",
        "pfleger_pflegling", "kind_gegen_beistand"))
    _wahrheitswert(rechtsbeziehung_besteht, "rechtsbeziehung_besteht")
    tag = _datum(stichtag, "stichtag")
    altersfall = beziehungsart in ("kind_eltern", "kind_partner_elternteil")
    geburt = None
    if geburtsdatum_kind is not None or altersfall:
        geburt = _datum(geburtsdatum_kind, "geburtsdatum_kind")
        if geburt > tag:
            _fehler("geburtsdatum_kind", "Geburt darf nicht nach dem Stichtag liegen.")
    _text(einordnungsnachweis, "einordnungsnachweis")
    altersvoraussetzung = True
    if altersfall:
        altersvoraussetzung = tag < _datum(lebensalter_beginn(geburtsdatum_kind, 21)["wert"], "altersgrenze")
    eingaben = dict(beziehungsart=beziehungsart, rechtsbeziehung_besteht=rechtsbeziehung_besteht,
        stichtag=stichtag, geburtsdatum_kind=geburtsdatum_kind, einordnungsnachweis=einordnungsnachweis)
    wert = dict(altersbegrenzung_anwendbar=altersfall,
        altersvoraussetzung_erfuellt=altersvoraussetzung,
        hemmungstatbestand_am_stichtag=rechtsbeziehung_besteht and altersvoraussetzung)
    return _schutz_ergebnis(wert, "BGB_VERJAEHRUNG_FAMILIENHEMMUNG", eingaben)


def verjaehrung_sexuelle_selbstbestimmung_hemmung(
    geburtsdatum=None, stichtag=None, anspruch_wegen_sexueller_selbstbestimmung=None,
    gemeinschaft_bei_verjaehrungsbeginn=None, gemeinschaft_ununterbrochen_bis_stichtag=None,
    einordnungsnachweis=None,
):
    """§208: Altershemmung oder fortdauernde anfängliche häusliche Gemeinschaft."""
    geburt = _datum(geburtsdatum, "geburtsdatum")
    tag = _datum(stichtag, "stichtag")
    if geburt > tag:
        _fehler("geburtsdatum", "Geburt darf nicht nach dem Stichtag liegen.")
    for name, wert in (("anspruch_wegen_sexueller_selbstbestimmung", anspruch_wegen_sexueller_selbstbestimmung),
        ("gemeinschaft_bei_verjaehrungsbeginn", gemeinschaft_bei_verjaehrungsbeginn),
        ("gemeinschaft_ununterbrochen_bis_stichtag", gemeinschaft_ununterbrochen_bis_stichtag)):
        _wahrheitswert(wert, name)
    _text(einordnungsnachweis, "einordnungsnachweis")
    jung = tag < _datum(lebensalter_beginn(geburtsdatum, 21)["wert"], "altersgrenze")
    gemeinschaft = gemeinschaft_bei_verjaehrungsbeginn and gemeinschaft_ununterbrochen_bis_stichtag
    eingaben = dict(geburtsdatum=geburtsdatum, stichtag=stichtag,
        anspruch_wegen_sexueller_selbstbestimmung=anspruch_wegen_sexueller_selbstbestimmung,
        gemeinschaft_bei_verjaehrungsbeginn=gemeinschaft_bei_verjaehrungsbeginn,
        gemeinschaft_ununterbrochen_bis_stichtag=gemeinschaft_ununterbrochen_bis_stichtag,
        einordnungsnachweis=einordnungsnachweis)
    wert = dict(altershemmung=anspruch_wegen_sexueller_selbstbestimmung and jung,
        gemeinschaftshemmung=anspruch_wegen_sexueller_selbstbestimmung and gemeinschaft,
        hemmungstatbestand_am_stichtag=anspruch_wegen_sexueller_selbstbestimmung and (jung or gemeinschaft))
    return _schutz_ergebnis(wert, "BGB_VERJAEHRUNG_SEXUELLE_SELBSTBESTIMMUNG_HEMMUNG", eingaben)
