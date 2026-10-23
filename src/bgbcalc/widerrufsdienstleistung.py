"""Dienstleistungswertersatz nach§357a Absatz2."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _fehler, _ganzzahl, _text
from .zahlen import GRENZE, _bruch, _multiplizieren


def widerruf_dienstleistungswertersatz(
    gesamtpreis=None, leistungsanteil_zaehler=None, leistungsanteil_nenner=None,
    gesamtpreis_unverhaeltnismaessig_hoch=None, marktwert_erbrachte_leistung=None,
    vorzeitiger_leistungsbeginn_verlangt=None, ausserhalb_geschaeftsraeumen=None,
    verlangen_auf_dauerhaftem_datentraeger=None, ordnungsgemaess_informiert=None,
    anwendungsfall_357a_absatz_2=None, bewertungsnachweis=None,
):
    """Preisanteil oder bereits leistungsbezogenen Marktwert mit gesetzlichen Voraussetzungen verknüpfen."""
    preis = _geld(gesamtpreis)
    zaehler = _ganzzahl(leistungsanteil_zaehler, "leistungsanteil_zaehler", 0, GRENZE)
    nenner = _ganzzahl(leistungsanteil_nenner, "leistungsanteil_nenner", 1, GRENZE)
    if zaehler > nenner:
        _fehler("leistungsanteil_zaehler", "Leistungsanteil darf eins nicht übersteigen.")
    eingaben = dict(gesamtpreis=gesamtpreis, leistungsanteil_zaehler=leistungsanteil_zaehler,
        leistungsanteil_nenner=leistungsanteil_nenner,
        gesamtpreis_unverhaeltnismaessig_hoch=gesamtpreis_unverhaeltnismaessig_hoch,
        marktwert_erbrachte_leistung=marktwert_erbrachte_leistung,
        vorzeitiger_leistungsbeginn_verlangt=vorzeitiger_leistungsbeginn_verlangt,
        ausserhalb_geschaeftsraeumen=ausserhalb_geschaeftsraeumen,
        verlangen_auf_dauerhaftem_datentraeger=verlangen_auf_dauerhaftem_datentraeger,
        ordnungsgemaess_informiert=ordnungsgemaess_informiert,
        anwendungsfall_357a_absatz_2=anwendungsfall_357a_absatz_2, bewertungsnachweis=bewertungsnachweis)
    for name in ("gesamtpreis_unverhaeltnismaessig_hoch", *tuple(eingaben)[5:-1]):
        _wahrheitswert(eingaben[name], name)
    marktwert = None
    if marktwert_erbrachte_leistung is not None or gesamtpreis_unverhaeltnismaessig_hoch:
        marktwert = _geld(marktwert_erbrachte_leistung)
    _text(bewertungsnachweis, "bewertungsnachweis")
    voraussetzungen = (vorzeitiger_leistungsbeginn_verlangt and ordnungsgemaess_informiert and
        (not ausserhalb_geschaeftsraeumen or verlangen_auf_dauerhaftem_datentraeger))
    wert = None
    if anwendungsfall_357a_absatz_2:
        wert = _bruch(0)
        if voraussetzungen:
            wert = marktwert if gesamtpreis_unverhaeltnismaessig_hoch else _multiplizieren(preis, _bruch(zaehler, nenner))
    ergebnis = _geld_ergebnis(wert, "BGB_WIDERRUF_DIENSTLEISTUNGSWERTERSATZ", eingaben,
        [dict(operation="Verlangen, Datenträgeranforderung und Unterrichtung prüfen; Vertragspreisanteil oder Marktwert der erbrachten Leistung")])
    ergebnis["hinweise"].append("Nur§357a Absatz2 bei wirksamem Widerruf und zutreffender Leistungsart. Leistungsanteil rechtlich und wirtschaftlich bestimmt, nicht ungeprüft Zeitanteil. Marktwert bezeichnet bereits die erbrachte Leistung und wird nicht nochmals anteilig gekürzt. Finanzdienstleistungen/Finanzierungshilfen§357b gesondert. Keine automatische Feststellung der Unverhältnismäßigkeit oder der Informationspflichten.")
    return ergebnis
