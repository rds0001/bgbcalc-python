"""Mängelbedingter Zahlungseinbehalt mit ausdrücklich bewertbarer Ausnahme."""

from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _fehler, _text
from .zahlen import _bruch, _multiplizieren
from .zinsen import _bruchteile


def werk_maengeleinbehalt(
    faellige_verguetung=None,
    mangelbeseitigungskosten=None,
    mangelbeseitigungsanspruch=None,
    abweichender_angemessener_betrag=None,
    abweichungsbegruendung=None,
):
    """§ 641 Abs. 3, entsprechend § 632a Abs. 1: angemessener Einbehalt."""
    verguetung, kosten = _geld(faellige_verguetung), _geld(mangelbeseitigungskosten)
    _wahrheitswert(mangelbeseitigungsanspruch, "mangelbeseitigungsanspruch")
    regelfall = abweichender_angemessener_betrag is None
    if regelfall:
        if abweichungsbegruendung is not None:
            _fehler("abweichungsbegruendung", "Begründung ohne abweichenden Betrag.")
        angemessen = _multiplizieren(kosten, _bruch(2))
    else:
        angemessen = _geld(abweichender_angemessener_betrag)
        _text(abweichungsbegruendung, "abweichungsbegruendung")
    wert = min(verguetung, angemessen) if mangelbeseitigungsanspruch else None
    return _geld_ergebnis(
        wert, "BGB_WERK_MAENGELEINBEHALT",
        dict(faellige_verguetung=faellige_verguetung,
             mangelbeseitigungskosten=mangelbeseitigungskosten,
             mangelbeseitigungsanspruch=mangelbeseitigungsanspruch,
             abweichender_angemessener_betrag=abweichender_angemessener_betrag,
             abweichungsbegruendung=abweichungsbegruendung),
        [{"operation": "Mangelbeseitigungsanspruch prüfen", "anwendbar": mangelbeseitigungsanspruch},
         {"operation": "Doppelte Kosten oder ausdrücklich begründete Einzelfallbewertung",
          "regelfall": regelfall, "angemessener_betrag": _bruchteile(angemessen)},
         {"operation": "Zahlungseinbehalt auf fällige Vergütung begrenzen"}],
    )
