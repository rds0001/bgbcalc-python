"""Besondere Grundfristen nach §§196–201, ohne spätere Friständerungen."""
from .betraege import _wahrheitswert
from .kalender import _auswahl, _datum, _ergebnis, _frist, _text


def verjaehrung_besondere_grundfrist(
    anspruchsart=None, anspruchsbeginn_am=None, titelereignis_am=None,
    kuenftig_wiederkehrende_leistung=None, abweichende_sonderregel=None,
    einordnungsnachweis=None,
):
    """Zehn-/Dreißigjahresfrist mit späterem Anspruchs-/Titelbeginn bestimmen."""
    _auswahl(anspruchsart, "anspruchsart", ("grundstuecksanspruch", "vorsaetzliche_personenverletzung",
        "herausgabeanspruch", "rechtskraeftig_festgestellt", "vollstreckbarer_vergleich_urkunde",
        "insolvenzfeststellung", "zwangsvollstreckungskosten"))
    beginn = _datum(anspruchsbeginn_am, "anspruchsbeginn_am")
    titelarten = ("rechtskraeftig_festgestellt", "vollstreckbarer_vergleich_urkunde",
        "insolvenzfeststellung", "zwangsvollstreckungskosten")
    titel = None
    if titelereignis_am is not None or anspruchsart in titelarten:
        titel = _datum(titelereignis_am, "titelereignis_am")
    _wahrheitswert(kuenftig_wiederkehrende_leistung, "kuenftig_wiederkehrende_leistung")
    _wahrheitswert(abweichende_sonderregel, "abweichende_sonderregel")
    _text(einordnungsnachweis, "einordnungsnachweis")
    regelmaessig = anspruchsart in titelarten[:3] and kuenftig_wiederkehrende_leistung
    wert = None
    if not abweichende_sonderregel and not regelmaessig:
        if anspruchsart in titelarten:
            beginn = max(beginn, titel)
        jahre = 10 if anspruchsart == "grundstuecksanspruch" else 30
        wert = dict(fristdauer_jahre=jahre, fristbeginnereignis_am=beginn.isoformat(),
            rechnerischer_letzter_tag=_frist(beginn.isoformat(), jahre, "jahre", "ereignis").isoformat())
    eingaben = dict(anspruchsart=anspruchsart, anspruchsbeginn_am=anspruchsbeginn_am,
        titelereignis_am=titelereignis_am, kuenftig_wiederkehrende_leistung=kuenftig_wiederkehrende_leistung,
        abweichende_sonderregel=abweichende_sonderregel, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert, "fristdaten", "BGB_VERJAEHRUNG_BESONDERE_GRUNDFRIST", eingaben,
        [dict(operation="§196: zehn Jahre; §197: dreißig Jahre; §201: späterer Anspruchs-/Titelbeginn; Ausnahme §197 Absatz2")], eingaben.copy())
    ergebnis["status"] = "BERECHNET" if wert is not None else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = ["Anspruchsart und maßgebliche Entstehung beziehungsweise Zuwiderhandlung bei Unterlassung rechtlich eingeordnet; feste lokale BGB-Fassung."]
    ergebnis["hinweise"] = ["Nur Grundfrist; Hemmung, Ablaufhemmung, Neubeginn und gegebenenfalls §193 gesondert. Kein endgültiger Verjährungstag.", "Künftig fällige wiederkehrende Leistungen nach §197 Absatz1 Nummer3 bis5 unterliegen der regelmäßigen Frist; NICHT_ANWENDBAR bedeutet keine Verjährungsfreiheit. Bereits fällige Rückstände getrennt behandeln."]
    return ergebnis
