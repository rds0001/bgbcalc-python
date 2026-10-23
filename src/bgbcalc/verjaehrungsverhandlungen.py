"""Dreimonatiger Mindestnachlauf nach Verhandlungshemmung (§ 203 Satz 2)."""

from .betraege import _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler, _monatsende


def verjaehrung_verhandlungen_mindestablauf(
    hemmungsende_am=None,
    rechnerischer_letzter_tag=None,
    hemmung_durch_verhandlungen_anwendbar=None,
):
    """Späteren Ablauf aus Hemmungswirkung und Dreimonatsnachlauf bestimmen."""
    eingaben = dict(
        hemmungsende_am=hemmungsende_am,
        rechnerischer_letzter_tag=rechnerischer_letzter_tag,
        hemmung_durch_verhandlungen_anwendbar=hemmung_durch_verhandlungen_anwendbar,
    )
    hemmungsende = _datum(hemmungsende_am, "hemmungsende_am")
    bisher = _datum(rechnerischer_letzter_tag, "rechnerischer_letzter_tag")
    _wahrheitswert(hemmung_durch_verhandlungen_anwendbar, "hemmung_durch_verhandlungen_anwendbar")
    wert = None
    if hemmung_durch_verhandlungen_anwendbar:
        if bisher < hemmungsende:
            _fehler("rechnerischer_letzter_tag", "Bereinigte Frist endet vor dem Hemmungsende.")
        mindestablauf = _monatsende(hemmungsende, 3, False)
        wert = dict(
            mindestablauf_nach_verhandlungen=mindestablauf.isoformat(),
            rechnerischer_letzter_tag=max(bisher, mindestablauf).isoformat(),
        )
    ergebnis = _ergebnis(
        wert, "datum", "BGB_VERJAEHRUNG_VERHANDLUNGEN_MINDESTABLAUF", eingaben,
        [{"operation": "Drei Monate nach Ende der Verhandlungshemmung; späteren Ablauf auswählen",
          "ergebnis": wert}], eingaben.copy(),
    )
    ergebnis["status"] = "BERECHNET" if hemmung_durch_verhandlungen_anwendbar else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = [
        "Feste lokale BGB-Fassung; Verhandlungshemmung rechtlich bestimmt und Hemmungswirkung bereits eingerechnet."
    ]
    ergebnis["hinweise"] = [
        "Enddaten bezeichnen den Tagesschluss; Mindestnachlauf statt pauschaler Addition weiterer drei Monate.",
        "Andere Friständerungen und gegebenenfalls Werktagsverschiebung bleiben gesondert; kein abschließender Verjährungstag."
    ]
    return ergebnis
