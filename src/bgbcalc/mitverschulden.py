"""Vermögensschaden anhand einer rechtlich vorgegebenen Mitverschuldensquote kürzen."""

from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _fehler, _text
from .zahlen import _bruch, _multiplizieren, _subtrahieren, _zahleneingabe
from .zinsen import _bruchteile


def vermoegensschaden_mitverschulden(
    vermoegensschaden=None,
    mitverschuldensquote=None,
    quotenbegruendung=None,
    kuerzung_nach_254_anwendbar=None,
):
    """Vorgegebene Kürzungsquote nach § 254 exakt auf eine Vermögensschadensposition anwenden."""
    schaden = _geld(vermoegensschaden)
    quote = _zahleneingabe(mitverschuldensquote)
    if not _bruch(0) <= quote <= _bruch(1):
        _fehler("mitverschuldensquote", "Anteil zwischen null und eins erforderlich, keine Prozentzahl.")
    _text(quotenbegruendung, "quotenbegruendung")
    _wahrheitswert(kuerzung_nach_254_anwendbar, "kuerzung_nach_254_anwendbar")
    eingaben = dict(
        vermoegensschaden=vermoegensschaden, mitverschuldensquote=mitverschuldensquote,
        quotenbegruendung=quotenbegruendung, kuerzung_nach_254_anwendbar=kuerzung_nach_254_anwendbar,
    )
    ergebnis = _geld_ergebnis(
        _bruch(0) if kuerzung_nach_254_anwendbar else None, "BGB_VERMOEGENSSCHADEN_MITVERSCHULDEN",
        eingaben,
        [{"operation": "Rechtlich vorgegebene Kürzungsquote dieser Vermögensschadensposition",
          "anwendbar": kuerzung_nach_254_anwendbar, "quote": _bruchteile(quote)}],
    )
    if kuerzung_nach_254_anwendbar:
        kuerzung = _multiplizieren(schaden, quote)
        rest = _subtrahieren(schaden, kuerzung)
        ergebnis["wert"] = dict(
            kuerzungsbetrag=_bruchteile(kuerzung), verbleibender_ersatzbetrag=_bruchteile(rest),
        )
        ergebnis["rechenschritte"].append({
            "operation": "Vermögensschaden mal Quote abziehen; keine Rundung",
            "kuerzungsbetrag": _bruchteile(kuerzung),
        })
    ergebnis["hinweise"].append(
        "Keine automatische Ermittlung der Mitverschuldensquote; nicht auf eine billige Entschädigung übertragen."
    )
    return ergebnis
