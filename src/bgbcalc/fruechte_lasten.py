"""Betragszuordnung von Früchten/Lasten sowie Gewinnungskostenersatz."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _auswahl, _fehler, _text
from .zahlen import _bruch, _multiplizieren
from .zinsen import _zeitanteil


def fruechte_lasten_betragszuordnung(
    zuordnungsart=None, gesamtbetrag=None, massgebliches_ereignis_im_zeitraum=None,
    zeitanteil_zaehler=None, zeitanteil_nenner=None, abweichende_bestimmung=None,
    zuordnungsnachweis=None,
):
    """§§101/103: Ereigniszuordnung oder zeitproportionale Zuordnung wiederkehrender Beträge."""
    _auswahl(zuordnungsart, "zuordnungsart", ("natuerliche_fruechte", "sonstige_fruechte",
        "regelmaessige_fruechte", "sonstige_lasten", "regelmaessige_lasten"))
    betrag = _geld(gesamtbetrag)
    _wahrheitswert(massgebliches_ereignis_im_zeitraum, "massgebliches_ereignis_im_zeitraum")
    _wahrheitswert(abweichende_bestimmung, "abweichende_bestimmung")
    _text(zuordnungsnachweis, "zuordnungsnachweis")
    regelmaessig = zuordnungsart in ("regelmaessige_fruechte", "regelmaessige_lasten")
    anteil = None
    if regelmaessig or zeitanteil_zaehler is not None or zeitanteil_nenner is not None:
        anteil = _zeitanteil(zeitanteil_zaehler, zeitanteil_nenner, zuordnungsnachweis)
        if anteil > 1:
            _fehler("zeitanteil", "Zeitanteil darf eins nicht übersteigen.")
    eingaben = dict(zuordnungsart=zuordnungsart, gesamtbetrag=gesamtbetrag,
        massgebliches_ereignis_im_zeitraum=massgebliches_ereignis_im_zeitraum,
        zeitanteil_zaehler=zeitanteil_zaehler, zeitanteil_nenner=zeitanteil_nenner,
        abweichende_bestimmung=abweichende_bestimmung, zuordnungsnachweis=zuordnungsnachweis)
    wert = None
    if not abweichende_bestimmung:
        wert = _multiplizieren(betrag, anteil) if regelmaessig else (betrag if massgebliches_ereignis_im_zeitraum else _bruch(0))
    ergebnis = _geld_ergebnis(wert, "BGB_FRUECHTE_LASTEN_BETRAGSZUORDNUNG", eingaben,
        [dict(operation="Wiederkehrende Beträge nach Zeitanteil, sonst nach rechtlich maßgeblichem Trennungs-/Fälligkeits-/Entrichtungsereignis zuordnen")])
    ergebnis["hinweise"].append("Natürliche Früchte: Trennung; sonstige Früchte: Fälligkeit; sonstige Lasten: rechtlicher Entrichtungszeitpunkt. Regelmäßige Beträge nach Daueranteil unabhängig vom einzelnen Fälligkeitstag. Abweichende Bestimmung gesondert; keine automatische Eigentumsübertragung bestimmter Naturstücke.")
    return ergebnis


def fruechte_gewinnungskostenersatz(
    ordnungsgemaesse_gewinnungskosten=None, wert_der_fruechte=None,
    herausgabepflicht_fruechte=None, kostennachweis=None,
):
    """§102: rechtlich qualifizierte Gewinnungskosten höchstens bis zum Fruchtwert."""
    kosten, wert = _geld(ordnungsgemaesse_gewinnungskosten), _geld(wert_der_fruechte)
    _wahrheitswert(herausgabepflicht_fruechte, "herausgabepflicht_fruechte")
    _text(kostennachweis, "kostennachweis")
    eingaben = dict(ordnungsgemaesse_gewinnungskosten=ordnungsgemaesse_gewinnungskosten,
        wert_der_fruechte=wert_der_fruechte, herausgabepflicht_fruechte=herausgabepflicht_fruechte,
        kostennachweis=kostennachweis)
    return _geld_ergebnis(min(kosten, wert) if herausgabepflicht_fruechte else None,
        "BGB_FRUECHTE_GEWINNUNGSKOSTENERSATZ", eingaben,
        [dict(operation="Bei Früchteherausgabepflicht ordnungsgemäße Gewinnungskosten auf Fruchtwert begrenzen")])
