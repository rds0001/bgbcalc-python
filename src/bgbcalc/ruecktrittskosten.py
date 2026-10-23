"""Aufwendungsersatz im Rücktrittsverhältnis nach§347 Absatz2."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _text
from .zahlen import _addieren
from .zinsen import _bruchteile


def ruecktritt_aufwendungsersatz(
    notwendige_verwendungen=None, andere_aufwendungen=None, bereicherung_durch_andere_aufwendungen=None,
    gegenstand_zurueckgegeben=None, wertersatz_geleistet=None,
    wertersatzpflicht_nach_346_3_nummer_1_2_ausgeschlossen=None, bewertungsnachweis=None,
):
    """Notwendige Verwendungen plus auf Bereicherung begrenzte andere Aufwendungen."""
    notwendig = _geld(notwendige_verwendungen)
    andere = _geld(andere_aufwendungen)
    bereicherung = _geld(bereicherung_durch_andere_aufwendungen)
    eingaben = dict(notwendige_verwendungen=notwendige_verwendungen, andere_aufwendungen=andere_aufwendungen,
        bereicherung_durch_andere_aufwendungen=bereicherung_durch_andere_aufwendungen,
        gegenstand_zurueckgegeben=gegenstand_zurueckgegeben, wertersatz_geleistet=wertersatz_geleistet,
        wertersatzpflicht_nach_346_3_nummer_1_2_ausgeschlossen=wertersatzpflicht_nach_346_3_nummer_1_2_ausgeschlossen,
        bewertungsnachweis=bewertungsnachweis)
    for name in tuple(eingaben)[3:-1]:
        _wahrheitswert(eingaben[name], name)
    _text(bewertungsnachweis, "bewertungsnachweis")
    anwendbar = (gegenstand_zurueckgegeben or wertersatz_geleistet or
        wertersatzpflicht_nach_346_3_nummer_1_2_ausgeschlossen)
    gedeckt = min(andere, bereicherung)
    gesamt = _addieren(notwendig, gedeckt) if anwendbar else None
    ergebnis = _geld_ergebnis(gesamt, "BGB_RUECKTRITT_AUFWENDUNGSERSATZ", eingaben,
        [dict(operation="Rückgewähr-/Wertersatzlage prüfen; notwendige Verwendungen plus andere Aufwendungen bis zur Bereicherung")])
    if anwendbar:
        ergebnis["wert"] = dict(notwendige_verwendungen_ersatz=_bruchteile(notwendig),
            andere_aufwendungen_ersatz=_bruchteile(gedeckt), gesamtbetrag=_bruchteile(gesamt))
    ergebnis["hinweise"].append("Qualifizierte notwendige Verwendungen und andere Aufwendungen überschneidungsfrei abgrenzen. Bloßer Wertersatzausschluss nach§346 Absatz3 Nummer3 erfüllt die hier geprüfte Ausnahme nicht. Kein Rücktrittsgrund, keine Bewertung der Notwendigkeit/Bereicherung und keine automatische Aufrechnung mit Rückgewähransprüchen.")
    return ergebnis
