"""Pflichtteilsbeträge aus gesondert bestimmten Quoten und Bewertungsgrößen."""

from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _fehler, _ganzzahl, _text
from .zahlen import (
    GRENZE,
    _addieren,
    _bruch,
    _zahleneingabe,
    _multiplizieren,
    _subtrahieren,
)
from .zinsen import _bruchteile


def pflichtteil_betrag(
    pflichtteilsnachlass=None,
    gesetzliche_erbquote_zaehler=None,
    gesetzliche_erbquote_nenner=None,
    anrechnungswert=None,
    anrechnungsbestimmung=None,
    pflichtteilsberechtigt=None,
    bewertungsnachweis=None,
):
    """§§ 2303/2315: halber gesetzlicher Erbteil, gegebenenfalls Anrechnung."""
    nachlass = _zahleneingabe(pflichtteilsnachlass)
    zuwendung = _geld(anrechnungswert)
    _ganzzahl(gesetzliche_erbquote_zaehler, "gesetzliche_erbquote_zaehler", 0, GRENZE)
    _ganzzahl(gesetzliche_erbquote_nenner, "gesetzliche_erbquote_nenner", 1, GRENZE)
    if gesetzliche_erbquote_zaehler > gesetzliche_erbquote_nenner:
        _fehler(
            "gesetzliche_erbquote", "Gesetzliche Erbquote darf 1 nicht überschreiten."
        )
    _wahrheitswert(anrechnungsbestimmung, "anrechnungsbestimmung")
    _wahrheitswert(pflichtteilsberechtigt, "pflichtteilsberechtigt")
    _text(bewertungsnachweis, "bewertungsnachweis")
    quote = _multiplizieren(
        _bruch(gesetzliche_erbquote_zaehler, gesetzliche_erbquote_nenner), _bruch(1, 2)
    )
    eingaben = dict(
        pflichtteilsnachlass=pflichtteilsnachlass,
        gesetzliche_erbquote_zaehler=gesetzliche_erbquote_zaehler,
        gesetzliche_erbquote_nenner=gesetzliche_erbquote_nenner,
        anrechnungswert=anrechnungswert,
        anrechnungsbestimmung=anrechnungsbestimmung,
        pflichtteilsberechtigt=pflichtteilsberechtigt,
        bewertungsnachweis=bewertungsnachweis,
    )
    schritte = [
        {
            "operation": "Pflichtteilsberechtigung und halbe gesetzliche Erbquote",
            "anwendbar": pflichtteilsberechtigt,
            "pflichtteilsquote": _bruchteile(quote),
        }
    ]
    wert = None
    if pflichtteilsberechtigt:
        anrechnung = zuwendung if anrechnungsbestimmung else _bruch(0)
        grundlage = max(_addieren(nachlass, anrechnung), _bruch(0))
        vor_anrechnung = _multiplizieren(grundlage, quote)
        wert = max(_subtrahieren(vor_anrechnung, anrechnung), _bruch(0))
        schritte.append(
            dict(
                operation="Anrechnungswert hinzurechnen, Quote anwenden, Wert abziehen; mindestens null",
                berechnungsgrundlage=_bruchteile(grundlage),
                vor_anrechnung=_bruchteile(vor_anrechnung),
                anrechnung=_bruchteile(anrechnung),
            )
        )
    return _geld_ergebnis(wert, "BGB_PFLICHTTEIL_BETRAG", eingaben, schritte)


def zusatzpflichtteil_betrag(
    pflichtteilsbetrag=None,
    unbeschwerter_erbteilwert=None,
    pflichtteilsberechtigt=None,
):
    """§§ 2305/2316 Abs. 2: fehlender Wert zum bereits bestimmten Pflichtteil."""
    anspruch, erbteil = _geld(pflichtteilsbetrag), _geld(unbeschwerter_erbteilwert)
    _wahrheitswert(pflichtteilsberechtigt, "pflichtteilsberechtigt")
    wert = (
        max(_subtrahieren(anspruch, erbteil), _bruch(0))
        if pflichtteilsberechtigt
        else None
    )
    return _geld_ergebnis(
        wert,
        "BGB_ZUSATZPFLICHTTEIL_BETRAG",
        dict(
            pflichtteilsbetrag=pflichtteilsbetrag,
            unbeschwerter_erbteilwert=unbeschwerter_erbteilwert,
            pflichtteilsberechtigt=pflichtteilsberechtigt,
        ),
        [
            {
                "operation": "Pflichtteilsbetrag minus unbeschwerter Erbteilwert, mindestens null",
                "anwendbar": pflichtteilsberechtigt,
            }
        ],
    )


def pflichtteil_vermaechtnisrest(
    pflichtteilsbetrag=None,
    unbeschwerter_vermaechtniswert=None,
    vermaechtnis_ausgeschlagen=None,
    pflichtteilsberechtigt=None,
):
    """§ 2307: Vermächtnis nur ohne wirksame Ausschlagung bedarfsdeckend abziehen."""
    anspruch, vermaechtnis = (
        _geld(pflichtteilsbetrag),
        _geld(unbeschwerter_vermaechtniswert),
    )
    _wahrheitswert(vermaechtnis_ausgeschlagen, "vermaechtnis_ausgeschlagen")
    _wahrheitswert(pflichtteilsberechtigt, "pflichtteilsberechtigt")
    abzug = _bruch(0) if vermaechtnis_ausgeschlagen else vermaechtnis
    wert = (
        max(_subtrahieren(anspruch, abzug), _bruch(0))
        if pflichtteilsberechtigt
        else None
    )
    return _geld_ergebnis(
        wert,
        "BGB_PFLICHTTEIL_VERMAECHTNISREST",
        dict(
            pflichtteilsbetrag=pflichtteilsbetrag,
            unbeschwerter_vermaechtniswert=unbeschwerter_vermaechtniswert,
            vermaechtnis_ausgeschlagen=vermaechtnis_ausgeschlagen,
            pflichtteilsberechtigt=pflichtteilsberechtigt,
        ),
        [
            {
                "operation": "Nicht ausgeschlagenes Vermächtnis auf Pflichtteil anrechnen, mindestens null",
                "anwendbar": pflichtteilsberechtigt,
                "abzug": _bruchteile(abzug),
            }
        ],
    )
