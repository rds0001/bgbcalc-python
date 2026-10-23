"""Zugewinn und Ausgleichsgrundbetrag aus rechtlich bewerteten Vermögenswerten."""
from .betraege import _geld, _geld_ergebnis
from .kalender import _text
from .zahlen import _addieren, _bruch, _zahleneingabe, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile


def zugewinn_betrag(anfangsvermoegen=None, endvermoegen=None, bewertungsnachweis=None):
    """§ 1373: positive Vermögensdifferenz einschließlich möglichem Schuldenabbau."""
    anfang = _zahleneingabe(anfangsvermoegen)
    ende = _zahleneingabe(endvermoegen)
    _text(bewertungsnachweis, "bewertungsnachweis")
    differenz = _subtrahieren(ende, anfang)
    return _geld_ergebnis(max(differenz, _bruch(0)), "BGB_ZUGEWINN_BETRAG",
                          dict(anfangsvermoegen=anfangsvermoegen, endvermoegen=endvermoegen,
                               bewertungsnachweis=bewertungsnachweis),
                          [{"operation": "Endvermögen minus Anfangsvermögen, mindestens null",
                            "vermoegensdifferenz": _bruchteile(differenz)}])


def zugewinnausgleich_grundbetrag(
    zugewinn_ehegatte_a=None, zugewinn_ehegatte_b=None,
    nettovermoegen_ehegatte_a=None, nettovermoegen_ehegatte_b=None,
    hinzurechnung_ehegatte_a=None, hinzurechnung_ehegatte_b=None,
    bewertungsnachweis=None,
):
    """§ 1378 Abs. 1/2: halber Zugewinnüberschuss mit Haftungsgrenze, vor § 1380."""
    eingaben = dict(
        zugewinn_ehegatte_a=zugewinn_ehegatte_a, zugewinn_ehegatte_b=zugewinn_ehegatte_b,
        nettovermoegen_ehegatte_a=nettovermoegen_ehegatte_a,
        nettovermoegen_ehegatte_b=nettovermoegen_ehegatte_b,
        hinzurechnung_ehegatte_a=hinzurechnung_ehegatte_a,
        hinzurechnung_ehegatte_b=hinzurechnung_ehegatte_b, bewertungsnachweis=bewertungsnachweis,
    )
    zugewinn_a, zugewinn_b = _geld(zugewinn_ehegatte_a), _geld(zugewinn_ehegatte_b)
    netto_a, netto_b = _zahleneingabe(nettovermoegen_ehegatte_a), _zahleneingabe(nettovermoegen_ehegatte_b)
    hinzu_a, hinzu_b = _geld(hinzurechnung_ehegatte_a), _geld(hinzurechnung_ehegatte_b)
    _text(bewertungsnachweis, "bewertungsnachweis")
    if zugewinn_a == zugewinn_b:
        richtung, halb, grenze = "kein_ueberschuss", _bruch(0), _bruch(0)
    else:
        richtung = "a_an_b" if zugewinn_a > zugewinn_b else "b_an_a"
        differenz = _subtrahieren(max(zugewinn_a, zugewinn_b), min(zugewinn_a, zugewinn_b))
        halb = _multiplizieren(differenz, _bruch(1, 2))
        grenze = max(_addieren(netto_a, hinzu_a) if richtung == "a_an_b"
                     else _addieren(netto_b, hinzu_b), _bruch(0))
    grundbetrag = min(halb, grenze)
    ergebnis = _geld_ergebnis(grundbetrag, "BGB_ZUGEWINNAUSGLEICH_GRUNDBETRAG", eingaben, [
        {"operation": "Richtung und Hälfte des Zugewinnüberschusses bestimmen", "richtung": richtung},
        {"operation": "Vorhandenes Nettovermögen plus Hinzurechnung des Verpflichteten als Grenze anwenden"},
    ])
    ergebnis["wert"] = dict(richtung=richtung, halber_ueberschuss=_bruchteile(halb),
                            haftungsgrenze=_bruchteile(grenze), grundbetrag=_bruchteile(grundbetrag))
    ergebnis["hinweise"].append(
        "Grundbetrag vor § 1380 und weiteren Anspruchsmodifikationen; kein abschließender durchsetzbarer Zahlbetrag.")
    return ergebnis
