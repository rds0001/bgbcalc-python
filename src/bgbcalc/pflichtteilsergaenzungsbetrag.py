"""Grunddifferenz der Pflichtteilsergänzung nach§2325 Absatz1."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _fehler, _ganzzahl, _text
from .zahlen import GRENZE, _addieren, _bruch, _multiplizieren, _subtrahieren, _zahleneingabe
from .zinsen import _bruchteile


def pflichtteilsergaenzung_grundbetrag(
    pflichtteilsnachlass=None, hinzuzurechnende_schenkungen=None,
    gesetzliche_erbquote_zaehler=None, gesetzliche_erbquote_nenner=None,
    pflichtteilsberechtigt=None, bewertungsnachweis=None,
):
    """Pflichtteilsdifferenz mit/ohne qualifizierte Drittschenkungen, auch bei negativem Nachlass."""
    nachlass = _zahleneingabe(pflichtteilsnachlass)
    schenkungen = _geld(hinzuzurechnende_schenkungen)
    zaehler = _ganzzahl(gesetzliche_erbquote_zaehler, "gesetzliche_erbquote_zaehler", 0, GRENZE)
    nenner = _ganzzahl(gesetzliche_erbquote_nenner, "gesetzliche_erbquote_nenner", 1, GRENZE)
    if zaehler > nenner:
        _fehler("gesetzliche_erbquote", "Gesetzliche Erbquote darf eins nicht übersteigen.")
    _wahrheitswert(pflichtteilsberechtigt, "pflichtteilsberechtigt")
    _text(bewertungsnachweis, "bewertungsnachweis")
    eingaben = dict(pflichtteilsnachlass=pflichtteilsnachlass, hinzuzurechnende_schenkungen=hinzuzurechnende_schenkungen,
        gesetzliche_erbquote_zaehler=gesetzliche_erbquote_zaehler, gesetzliche_erbquote_nenner=gesetzliche_erbquote_nenner,
        pflichtteilsberechtigt=pflichtteilsberechtigt, bewertungsnachweis=bewertungsnachweis)
    ergebnis = _geld_ergebnis(None, "BGB_PFLICHTTEILSERGAENZUNG_GRUNDBETRAG", eingaben,
        [dict(operation="Tatsächlichen und um qualifizierte Drittschenkungen erhöhten Nachlass jeweils mindestens null ansetzen; halbe gesetzliche Erbquote anwenden und Pflichtteilsdifferenz bilden")])
    if pflichtteilsberechtigt:
        quote = _multiplizieren(_bruch(zaehler, nenner), _bruch(1, 2))
        ordentlich = _multiplizieren(max(nachlass, _bruch(0)), quote)
        erhoeht = _multiplizieren(max(_addieren(nachlass, schenkungen), _bruch(0)), quote)
        ergebnis["wert"] = dict(ordentlicher_pflichtteilswert=_bruchteile(ordentlich),
            erhoehter_pflichtteilswert=_bruchteile(erhoeht), ergaenzungsgrundbetrag=_bruchteile(_subtrahieren(erhoeht, ordentlich)))
        ergebnis["status"] = "BERECHNET"
    ergebnis["hinweise"].append("Grundmodell ohne Anrechnung eigener Geschenke§§2315/2327 oder Ausgleichung§2316. Summe der Drittschenkungen muss bereits Bewertung, Abschmelzung und Ausnahmen erfüllen. Bei negativem Nachlass nicht bloß Schenkungswert mal Quote rechnen. Mehrhinterlassung§2326, Erbenschutz§2328 und Beschenktenhaftung§2329 separat; kein abschließender Zahlungsanspruch.")
    return ergebnis
