"""Volle Grundfrist nach einem rechtlich wirksamen Neubeginn (§ 212)."""

from .betraege import _wahrheitswert
from .kalender import _auswahl, _datum, _ergebnis, _frist, _ganzzahl


def verjaehrung_neubeginn_grundfrist(
    neubeginnereignis_am=None,
    fristdauer=None,
    fristeinheit=None,
    wirksamer_neubeginn=None,
):
    """Volle Ereignisfrist erneut berechnen, ohne automatischen Jahresschlussbeginn."""
    _datum(neubeginnereignis_am, "neubeginnereignis_am")
    _ganzzahl(fristdauer, "fristdauer", 1)
    _auswahl(fristeinheit, "fristeinheit", ("tage", "wochen", "monate", "jahre"))
    _wahrheitswert(wirksamer_neubeginn, "wirksamer_neubeginn")
    eingaben = dict(
        neubeginnereignis_am=neubeginnereignis_am, fristdauer=fristdauer,
        fristeinheit=fristeinheit, wirksamer_neubeginn=wirksamer_neubeginn,
    )
    wert = None
    if wirksamer_neubeginn:
        wert = _frist(neubeginnereignis_am, fristdauer, fristeinheit, "ereignis").isoformat()
    ergebnis = _ergebnis(
        wert, "datum", "BGB_VERJAEHRUNG_NEUBEGINN_GRUNDFRIST", eingaben,
        [{"operation": "Volle maßgebliche Ereignisfrist ab wirksamem Neubeginn",
          "ergebnis": wert}], eingaben.copy(),
    )
    ergebnis["status"] = "BERECHNET" if wirksamer_neubeginn else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = [
        "Feste lokale BGB-Fassung; Wirksamkeit des Neubeginns, Ereignis und volle Fristdauer rechtlich vorgegeben."
    ]
    ergebnis["hinweise"] = [
        "Rechnerischer letzter Tag zum Tagesschluss; kein automatischer Jahresschlussbeginn oder Abzug zuvor verstrichener Zeit.",
        "Spätere Friständerungen, konkurrierende Fristläufe und gegebenenfalls Werktagsverschiebung bleiben gesondert; kein abschließender Verjährungstag."
    ]
    return ergebnis
