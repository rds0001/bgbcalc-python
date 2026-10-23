"""Regelmäßige Dreijahres-Grundfrist mit Jahresschlussbeginn."""

from datetime import date

from .betraege import _wahrheitswert
from .kalender import _datum, _ergebnis, _monatsende


def regelverjaehrung_grundfrist(
    entstehung_oder_zuwiderhandlung_am=None,
    kenntnis_oder_kennenmuessen_am=None,
    regelmaessiger_jahresschlussbeginn_anwendbar=None,
):
    """Grundfrist nach §§ 195, 199 Absatz 1/5, ohne Hemmung und weitere Änderungen."""
    eingaben = dict(
        entstehung_oder_zuwiderhandlung_am=entstehung_oder_zuwiderhandlung_am,
        kenntnis_oder_kennenmuessen_am=kenntnis_oder_kennenmuessen_am,
        regelmaessiger_jahresschlussbeginn_anwendbar=regelmaessiger_jahresschlussbeginn_anwendbar,
    )
    entstehung = _datum(entstehung_oder_zuwiderhandlung_am, "entstehung_oder_zuwiderhandlung_am")
    kenntnis = _datum(kenntnis_oder_kennenmuessen_am, "kenntnis_oder_kennenmuessen_am")
    _wahrheitswert(
        regelmaessiger_jahresschlussbeginn_anwendbar, "regelmaessiger_jahresschlussbeginn_anwendbar"
    )
    wert = None
    jahr = max(entstehung.year, kenntnis.year)
    if regelmaessiger_jahresschlussbeginn_anwendbar:
        beginn = date(jahr, 12, 31)
        ende = _monatsende(beginn, 36, False)
        wert = dict(
            beginn_mit_jahresschluss=beginn.isoformat(),
            rechnerischer_letzter_tag=ende.isoformat(),
        )
    ergebnis = _ergebnis(
        wert, "datum", "BGB_REGELVERJAEHRUNG_GRUNDFRIST", eingaben,
        [{"operation": "Späteres Jahr der beiden gesetzlichen Voraussetzungen",
          "jahr": jahr},
         {"operation": "Jahresschluss und unmodifizierte Dreijahresfrist",
          "ergebnis": wert}], eingaben.copy(),
    )
    ergebnis["status"] = (
        "BERECHNET" if regelmaessiger_jahresschlussbeginn_anwendbar else "NICHT_ANWENDBAR"
    )
    ergebnis["annahmen"] = [
        "Feste lokale BGB-Fassung; Anspruchsentstehung oder Zuwiderhandlung und Kenntnis oder Kennenmüssen rechtlich vorgegeben."
    ]
    ergebnis["hinweise"] = [
        "Beide Ergebnisdaten bezeichnen den Tagesschluss; kein abschließender Verjährungstag.",
        "Höchstfristen, Hemmung, Ablaufhemmung, Neubeginn, Sonderregeln und eine gegebenenfalls erforderliche Werktagsverschiebung sind nicht eingerechnet."
    ]
    return ergebnis
