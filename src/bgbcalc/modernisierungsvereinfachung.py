"""Kostenprüfung und Erhaltungspauschale nach § 559c Absätzen 1/2."""

from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .zahlen import _bruch, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile


def modernisierung_vereinfachte_kostenbasis(
    geltend_gemachte_kosten=None,
    frueher_geltend_gemachte_kosten=None,
    vereinfachtes_verfahren_gewaehlt=None,
):
    """Verbleibende Kostengrenze vor der Dreißigprozentpauschale prüfen."""
    eingaben = dict(
        geltend_gemachte_kosten=geltend_gemachte_kosten,
        frueher_geltend_gemachte_kosten=frueher_geltend_gemachte_kosten,
        vereinfachtes_verfahren_gewaehlt=vereinfachtes_verfahren_gewaehlt,
    )
    kosten = _geld(geltend_gemachte_kosten)
    frueher = _geld(frueher_geltend_gemachte_kosten)
    _wahrheitswert(vereinfachtes_verfahren_gewaehlt, "vereinfachtes_verfahren_gewaehlt")
    grenze = max(_subtrahieren(_bruch(10000), frueher), _bruch(0))
    anwendbar = vereinfachtes_verfahren_gewaehlt and kosten <= grenze
    ergebnis = _geld_ergebnis(
        _bruch(0) if anwendbar else None, "BGB_MODERNISIERUNG_VEREINFACHTE_KOSTENBASIS",
        eingaben,
        [{"operation": "Verbleibender Kostenhöchstbetrag vor Erhaltungspauschale",
          "kostenhoechstbetrag": _bruchteile(grenze)},
         {"operation": "Gewähltes Verfahren und Einhaltung der Kostengrenze",
          "anwendbar": anwendbar}],
    )
    if anwendbar:
        pauschale = _multiplizieren(kosten, _bruch(3, 10))
        basis = _subtrahieren(kosten, pauschale)
        ergebnis["wert"] = dict(
            kostenhoechstbetrag=_bruchteile(grenze),
            erhaltungspauschale=_bruchteile(pauschale),
            kostenbasis=_bruchteile(basis),
        )
        ergebnis["rechenschritte"].append({
            "operation": "Dreißig Prozent Erhaltungspauschale abziehen",
            "erhaltungspauschale": _bruchteile(pauschale),
        })
    ergebnis["hinweise"].append(
        "Nur Kostenbasis des vereinfachten Verfahrens; kein endgültiger Mieterhöhungsbetrag."
    )
    return ergebnis
