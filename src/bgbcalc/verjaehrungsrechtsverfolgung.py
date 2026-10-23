"""Sechsmonatiger Nachlauf nach § 204 Absatz 2 Sätze 1/2."""

from .betraege import _wahrheitswert
from .kalender import _auswahl, _datum, _ergebnis, _monatsende


def verjaehrung_rechtsverfolgung_nachlauffrist(
    anknuepfungsereignis=None,
    anknuepfungsereignis_am=None,
    hemmung_durch_rechtsverfolgung_anwendbar=None,
):
    """Rechnerisches Ende des ausgewählten Nachlaufs, kein Verjährungsablauf."""
    _auswahl(anknuepfungsereignis, "anknuepfungsereignis", (
        "rechtskraeftige_entscheidung", "anderweitige_beendigung", "stillstand_durch_nichtbetreiben",
    ))
    ereignis = _datum(anknuepfungsereignis_am, "anknuepfungsereignis_am")
    _wahrheitswert(hemmung_durch_rechtsverfolgung_anwendbar, "hemmung_durch_rechtsverfolgung_anwendbar")
    eingaben = dict(
        anknuepfungsereignis=anknuepfungsereignis,
        anknuepfungsereignis_am=anknuepfungsereignis_am,
        hemmung_durch_rechtsverfolgung_anwendbar=hemmung_durch_rechtsverfolgung_anwendbar,
    )
    wert = None
    if hemmung_durch_rechtsverfolgung_anwendbar:
        wert = _monatsende(ereignis, 6, False).isoformat()
    ergebnis = _ergebnis(
        wert, "datum", "BGB_VERJAEHRUNG_RECHTSVERFOLGUNG_NACHLAUFFRIST", eingaben,
        [{"operation": "Sechsmonatiger Nachlauf ab rechtlich ausgewähltem Ereignis",
          "anknuepfungsereignis": anknuepfungsereignis, "ergebnis": wert}], eingaben.copy(),
    )
    ergebnis["status"] = "BERECHNET" if hemmung_durch_rechtsverfolgung_anwendbar else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = [
        "Feste lokale BGB-Fassung; Hemmungstatbestand und Anknüpfungsereignis rechtlich vorgegeben."
    ]
    ergebnis["hinweise"] = [
        "Rechnerisches Ende des ausgewählten Nachlaufs zum Tagesschluss, kein Verjährungsablauf.",
        "Erneutes Weiterbetreiben und spätere Verfahrensereignisse sowie gegebenenfalls Werktagsverschiebung sind gesondert zu berücksichtigen."
    ]
    return ergebnis
