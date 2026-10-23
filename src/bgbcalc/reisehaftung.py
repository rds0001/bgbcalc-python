"""Rücktrittsentschädigung, Ausschlussgründe und vereinbarte Haftungsgrenze der Pauschalreise."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _ergebnis, _text
from .zahlen import _bruch, _multiplizieren, _subtrahieren


def pauschalreise_ruecktrittsentschaedigung(
    reisepreis=None, ersparte_aufwendungen=None, anderweitiger_erwerb=None,
    entschaedigungspauschale_vereinbart=None, ausschluss_aussergewoehnliche_umstaende=None,
    bewertungsnachweis=None,
):
    """§651h Absätze2/3: konkrete Differenzrechnung, ohne Erfindung einer Stornopauschale."""
    preis, erspart, erwerb = _geld(reisepreis), _geld(ersparte_aufwendungen), _geld(anderweitiger_erwerb)
    _wahrheitswert(entschaedigungspauschale_vereinbart, "entschaedigungspauschale_vereinbart")
    _wahrheitswert(ausschluss_aussergewoehnliche_umstaende, "ausschluss_aussergewoehnliche_umstaende")
    _text(bewertungsnachweis, "bewertungsnachweis")
    eingaben = dict(reisepreis=reisepreis, ersparte_aufwendungen=ersparte_aufwendungen,
        anderweitiger_erwerb=anderweitiger_erwerb, entschaedigungspauschale_vereinbart=entschaedigungspauschale_vereinbart,
        ausschluss_aussergewoehnliche_umstaende=ausschluss_aussergewoehnliche_umstaende, bewertungsnachweis=bewertungsnachweis)
    wert = None
    if ausschluss_aussergewoehnliche_umstaende:
        wert = _bruch(0)
    elif not entschaedigungspauschale_vereinbart:
        wert = max(_subtrahieren(_subtrahieren(preis, erspart), erwerb), _bruch(0))
    ergebnis = _geld_ergebnis(wert, "BGB_PAUSCHALREISE_RUECKTRITTSENTSCHAEDIGUNG", eingaben,
        [dict(operation="Vorrangigen Entschädigungsausschluss prüfen; sonst ohne Pauschalvereinbarung Reisepreis um Ersparnis und anderweitigen Erwerb vermindern")])
    ergebnis["hinweise"].append("Rücktritt des Reisenden vor Reisebeginn vorausgesetzt. Pauschalvereinbarung ohne Ausschluss ergibt NICHT_ANWENDBAR; Höhe und Angemessenheit einer Stornopauschale werden nicht erfunden. Rückerstattung und Fälligkeit gesondert.")
    return ergebnis


def pauschalreise_haftungsbegrenzung(
    reisepreis=None, ersatzfaehiger_schaden=None, haftungsbeschraenkung_vereinbart=None,
    koerperschaden=None, schuldhaft_herbeigefuehrt=None, bewertungsnachweis=None,
):
    """§651p Absatz1: vereinbarte Dreifachgrenze nur ohne Körper- und Verschuldensschaden."""
    preis, schaden = _geld(reisepreis), _geld(ersatzfaehiger_schaden)
    eingaben = dict(reisepreis=reisepreis, ersatzfaehiger_schaden=ersatzfaehiger_schaden,
        haftungsbeschraenkung_vereinbart=haftungsbeschraenkung_vereinbart, koerperschaden=koerperschaden,
        schuldhaft_herbeigefuehrt=schuldhaft_herbeigefuehrt, bewertungsnachweis=bewertungsnachweis)
    for name in ("haftungsbeschraenkung_vereinbart", "koerperschaden", "schuldhaft_herbeigefuehrt"):
        _wahrheitswert(eingaben[name], name)
    _text(bewertungsnachweis, "bewertungsnachweis")
    wert = schaden
    if haftungsbeschraenkung_vereinbart and not koerperschaden and not schuldhaft_herbeigefuehrt:
        wert = min(schaden, _multiplizieren(preis, _bruch(3)))
    ergebnis = _geld_ergebnis(wert, "BGB_PAUSCHALREISE_HAFTUNGSBEGRENZUNG", eingaben,
        [dict(operation="Vereinbarte Begrenzung auf dreifachen Reisepreis nur für nicht schuldhaft herbeigeführte Schäden ohne Körperschäden anwenden")])
    ergebnis["hinweise"].append("Nur Begrenzung nach§651p Absatz1 auf bereits ersatzfähigen Schaden. Internationale Beschränkungen nach Absatz2 und Anrechnung nach Absatz3 sowie andere Haftungsvoraussetzungen getrennt; keine Aufteilung gemischter Schadenspositionen.")
    return ergebnis


