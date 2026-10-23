"""Taggenaue Hemmungswirkung für rechtlich normalisierte Intervalle (§ 209)."""

from .betraege import _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler, _tage_addieren, _vorhanden


def verjaehrung_gehemmte_kalendertage(
    fristlauf_erster_tag=None,
    grundfrist_letzter_tag=None,
    hemmungszeitraeume=None,
    hemmung_nach_209_anwendbar=None,
):
    """Vereinigte Hemmungstage aus dem laufenden Fristzeitraum herausrechnen."""
    eingaben = dict(
        fristlauf_erster_tag=fristlauf_erster_tag,
        grundfrist_letzter_tag=grundfrist_letzter_tag,
        hemmungszeitraeume=hemmungszeitraeume,
        hemmung_nach_209_anwendbar=hemmung_nach_209_anwendbar,
    )
    erster = _datum(fristlauf_erster_tag, "fristlauf_erster_tag")
    ende = _datum(grundfrist_letzter_tag, "grundfrist_letzter_tag")
    if erster > ende:
        _fehler("grundfrist_letzter_tag", "Grundfrist darf nicht vor ihrem ersten Lauftag enden.")
    _vorhanden(hemmungszeitraeume, "hemmungszeitraeume")
    if not isinstance(hemmungszeitraeume, list) or len(hemmungszeitraeume) > 10000:
        _fehler("hemmungszeitraeume", "Liste mit höchstens 10000 Intervallen erforderlich.")
    intervalle = []
    for zeitraum in hemmungszeitraeume:
        if not isinstance(zeitraum, dict) or set(zeitraum) != {
            "erster_gehemmter_tag", "letzter_gehemmter_tag"
        }:
            _fehler("hemmungszeitraeume", "Intervall mit genau den beiden Tagesgrenzen erforderlich.")
        anfang = _datum(zeitraum["erster_gehemmter_tag"], "erster_gehemmter_tag")
        schluss = _datum(zeitraum["letzter_gehemmter_tag"], "letzter_gehemmter_tag")
        if anfang > schluss:
            _fehler("hemmungszeitraeume", "Hemmungsende liegt vor Hemmungsbeginn.")
        if schluss >= erster:
            intervalle.append((max(anfang, erster), schluss))
    _wahrheitswert(hemmung_nach_209_anwendbar, "hemmung_nach_209_anwendbar")
    vereinigt = []
    for anfang, schluss in sorted(intervalle):
        if vereinigt and (anfang - vereinigt[-1][1]).days <= 1:
            vereinigt[-1] = (vereinigt[-1][0], max(vereinigt[-1][1], schluss))
        else:
            vereinigt.append((anfang, schluss))
    schritte = [{"operation": "Taggenaue Hemmungswirkung", "anwendbar": hemmung_nach_209_anwendbar}]
    wert = None
    if hemmung_nach_209_anwendbar:
        tage = 0
        for anfang, schluss in vereinigt:
            if anfang > ende:
                break
            dauer = (schluss - anfang).days + 1
            ende = _tage_addieren(ende, dauer)
            tage += dauer
            schritte.append({
                "operation": "Vereinigtes Hemmungsintervall nicht mitzählen",
                "erster_gehemmter_tag": anfang.isoformat(),
                "letzter_gehemmter_tag": schluss.isoformat(),
                "hemmungstage": dauer,
                "rechnerischer_letzter_tag": ende.isoformat(),
            })
        wert = dict(rechnerischer_letzter_tag=ende.isoformat(), beruecksichtigte_hemmungstage=tage)
    ergebnis = _ergebnis(
        wert, "datum", "BGB_VERJAEHRUNG_GEHEMMTE_KALENDERTAGE",
        eingaben, schritte, eingaben.copy(),
    )
    ergebnis["status"] = "BERECHNET" if hemmung_nach_209_anwendbar else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = [
        "Feste lokale BGB-Fassung; Hemmungsgründe und eingeschlossene Kalendertage rechtlich vorgegeben."
    ]
    ergebnis["hinweise"] = [
        "Abgeschlossene, auf ganze Kalendertage normalisierte Intervalle; keine automatische Bestimmung der Hemmungstatbestände.",
        "Ablaufhemmung, Neubeginn, konkurrierende Fristläufe und Werktagsverschiebung bleiben gesondert; kein abschließender Verjährungstag."
    ]
    return ergebnis
