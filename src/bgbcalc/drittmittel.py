"""Kostenbezogene Auffangverteilung von Modernisierungs-Drittmitteln."""

from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _fehler, _text, _vorhanden
from .zahlen import _addieren, _bruch, _dividieren, _multiplizieren
from .zinsen import _bruchteile


def modernisierung_drittmittel_aufteilen(
    gesamtmittel=None, wohnungskosten=None, zuordnung_feststellbar=None,
):
    """§ 559a Abs. 4: unbekannte Einzelzuordnung nach aufgewendeten Kosten."""
    mittel = _geld(gesamtmittel)
    _vorhanden(wohnungskosten, "wohnungskosten")
    if not isinstance(wohnungskosten, list) or not 1 <= len(wohnungskosten) <= 1000:
        _fehler("wohnungskosten", "Liste mit 1 bis 1000 Wohnungen erforderlich.")
    _wahrheitswert(zuordnung_feststellbar, "zuordnung_feststellbar")
    namen, kosten = [], []
    gesamtkosten = _bruch(0)
    for wohnung in wohnungskosten:
        if not isinstance(wohnung, dict) or set(wohnung) != {"wohnung_id", "aufgewendete_kosten"}:
            _fehler("wohnungskosten", "Genau wohnung_id und aufgewendete_kosten erforderlich.")
        kennung = _text(wohnung["wohnung_id"], "wohnung_id")
        if kennung in namen:
            _fehler("wohnung_id", "Wohnungen dürfen nicht doppelt vorkommen.")
        wert = _geld(wohnung["aufgewendete_kosten"])
        namen.append(kennung)
        kosten.append(wert)
        gesamtkosten = _addieren(gesamtkosten, wert)
    if gesamtkosten == 0:
        _fehler("wohnungskosten", "Positive Gesamtkosten für den Verteilungsschlüssel erforderlich.")
    anwendbar = not zuordnung_feststellbar
    ergebnis = _geld_ergebnis(
        _bruch(0) if anwendbar else None, "BGB_MODERNISIERUNG_DRITTMITTEL_AUFTEILEN",
        dict(gesamtmittel=gesamtmittel, wohnungskosten=wohnungskosten,
             zuordnung_feststellbar=zuordnung_feststellbar),
        [{"operation": "Auffangschlüssel nur bei nicht feststellbarer Einzelzuordnung", "anwendbar": anwendbar},
         {"operation": "Nach Verhältnis aufgewendeter Wohnungskosten aufteilen",
          "gesamtkosten": _bruchteile(gesamtkosten)}],
    )
    if anwendbar:
        ergebnis["wert"] = []
        for kennung, einzelkosten in zip(namen, kosten):
            anteil = _dividieren(einzelkosten, gesamtkosten)
            ergebnis["wert"].append(dict(
                wohnung_id=kennung, kostenanteil=_bruchteile(anteil),
                drittmittel=_bruchteile(_multiplizieren(mittel, anteil)),
            ))
    return ergebnis
