"""Gleichanteile nach §§ 420 und 430 mit ausdrücklich benannter Leistungseinheit."""

from .betraege import _wahrheitswert
from .kalender import _auswahl, _ergebnis, _fehler, _ganzzahl, _text
from .zahlen import _bruch, _multiplizieren, _zahleneingabe
from .zinsen import _bruchteile


def _gleichanteils_ergebnis(
    gesamtleistung, anzahl, anzahl_parameter, leistungseinheit, anwendbar, regel_id, eingaben,
):
    menge = _zahleneingabe(gesamtleistung)
    if menge < 0:
        _fehler("gesamtleistung", "Nichtnegative Gesamtleistung erforderlich.")
    _ganzzahl(anzahl, anzahl_parameter, 2, 9007199254740991)
    _text(leistungseinheit, "leistungseinheit")
    wert = None
    if anwendbar:
        quote = _bruch(1, anzahl)
        wert = dict(
            anteilsquote=_bruchteile(quote),
            leistungsanteil=_bruchteile(_multiplizieren(menge, quote)),
        )
    ergebnis = _ergebnis(
        wert, leistungseinheit, regel_id, eingaben,
        [{"operation": "Gleiche Anteilsquote und Gesamtleistung geteilt durch Personenzahl",
          "anwendbar": anwendbar, "anzahl": anzahl, "ergebnis": wert}], eingaben.copy(),
    )
    ergebnis["status"] = "BERECHNET" if anwendbar else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = [
        "Feste lokale BGB-Fassung; Rechtsform, Gleichanteilsregel und gemeinsame Leistungseinheit ausdrücklich vorgegeben."
    ]
    ergebnis["hinweise"] = [
        "Keine automatische Bewertung, Einheitenumrechnung oder Rundung.",
        "Rechnerischer Anteil ohne Abrechnung bereits erbrachter oder vereinnahmter Leistungen."
    ]
    return ergebnis


def teilbare_leistung_gleichanteil(
    gesamtleistung=None,
    anzahl_beteiligte=None,
    leistungseinheit=None,
    rollenart=None,
    leistung_teilbar=None,
    gleichanteilsvermutung_anwendbar=None,
):
    """Gleiche Teilschuld oder Teilforderung nach der Zweifelsregel des § 420."""
    _auswahl(rollenart, "rollenart", ("teilschuld", "teilforderung"))
    _wahrheitswert(leistung_teilbar, "leistung_teilbar")
    _wahrheitswert(gleichanteilsvermutung_anwendbar, "gleichanteilsvermutung_anwendbar")
    eingaben = dict(
        gesamtleistung=gesamtleistung, anzahl_beteiligte=anzahl_beteiligte,
        leistungseinheit=leistungseinheit, rollenart=rollenart, leistung_teilbar=leistung_teilbar,
        gleichanteilsvermutung_anwendbar=gleichanteilsvermutung_anwendbar,
    )
    return _gleichanteils_ergebnis(
        gesamtleistung, anzahl_beteiligte, "anzahl_beteiligte", leistungseinheit,
        leistung_teilbar and gleichanteilsvermutung_anwendbar,
        "BGB_TEILBARE_LEISTUNG_GLEICHANTEIL", eingaben,
    )


def gesamtglaeubiger_innenanteil(
    gesamtleistung=None,
    anzahl_gesamtglaeubiger=None,
    leistungseinheit=None,
    gleichanteilige_innenberechtigung_anwendbar=None,
):
    """Gleicher Innenanteil nach § 430; keine Kürzung der Außenberechtigung."""
    _wahrheitswert(
        gleichanteilige_innenberechtigung_anwendbar, "gleichanteilige_innenberechtigung_anwendbar"
    )
    eingaben = dict(
        gesamtleistung=gesamtleistung, anzahl_gesamtglaeubiger=anzahl_gesamtglaeubiger,
        leistungseinheit=leistungseinheit,
        gleichanteilige_innenberechtigung_anwendbar=gleichanteilige_innenberechtigung_anwendbar,
    )
    ergebnis = _gleichanteils_ergebnis(
        gesamtleistung, anzahl_gesamtglaeubiger, "anzahl_gesamtglaeubiger", leistungseinheit,
        gleichanteilige_innenberechtigung_anwendbar, "BGB_GESAMTGLAEUBIGER_INNENANTEIL", eingaben,
    )
    ergebnis["hinweise"].append(
        "Nur Innenberechtigung der Gesamtgläubiger; Außenberechtigung gegenüber dem Schuldner nicht reduziert."
    )
    return ergebnis
