"""Betragsgrenzen für Abschläge und Sicherungsvereinbarungen beim Verbraucherbau."""

from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .zahlen import _bruch, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile


def verbraucherbau_abschlagsgrenze(
    gesamtverguetung=None,
    bisherige_abschlaege=None,
    verbraucherbauvertrag=None,
    bautraegervertrag=None,
    abschlag_nach_632a=None,
):
    """§ 650m Abs. 1: Gesamtgrenze und rechnerisch verbleibender Rahmen."""
    eingaben = dict(
        gesamtverguetung=gesamtverguetung,
        bisherige_abschlaege=bisherige_abschlaege,
        verbraucherbauvertrag=verbraucherbauvertrag,
        bautraegervertrag=bautraegervertrag,
        abschlag_nach_632a=abschlag_nach_632a,
    )
    verguetung, bisher = _geld(gesamtverguetung), _geld(bisherige_abschlaege)
    for parameter in ("verbraucherbauvertrag", "bautraegervertrag", "abschlag_nach_632a"):
        _wahrheitswert(eingaben[parameter], parameter)
    anwendbar = verbraucherbauvertrag and not bautraegervertrag and abschlag_nach_632a
    ergebnis = _geld_ergebnis(
        _bruch(0) if anwendbar else None,
        "BGB_VERBRAUCHERBAU_ABSCHLAGSGRENZE",
        eingaben,
        [{"operation": "Verbraucherbau, Abschlag nach § 632a und Bauträgerausschluss",
          "anwendbar": anwendbar}],
    )
    if anwendbar:
        grenze = _multiplizieren(verguetung, _bruch(9, 10))
        rest = max(_subtrahieren(grenze, bisher), _bruch(0))
        ergebnis["wert"] = dict(
            gesamtgrenze=_bruchteile(grenze), verbleibender_rahmen=_bruchteile(rest)
        )
        ergebnis["rechenschritte"].append(
            {"operation": "90 Prozent der Gesamtvergütung; bisherige Abschläge abziehen, mindestens null"}
        )
    return ergebnis


def verbraucherbau_sicherungsgrenze(
    vereinbarte_verguetung=None,
    naechste_abschlagszahlung=None,
    vereinbarte_sicherheit=None,
    verbraucherbauvertrag=None,
    abschlaege_verlangt=None,
    abschlaege_vereinbart=None,
):
    """§ 650m Abs. 4: Betragsschwelle für eine Sicherheit des Verbrauchers."""
    eingaben = dict(
        vereinbarte_verguetung=vereinbarte_verguetung,
        naechste_abschlagszahlung=naechste_abschlagszahlung,
        vereinbarte_sicherheit=vereinbarte_sicherheit,
        verbraucherbauvertrag=verbraucherbauvertrag,
        abschlaege_verlangt=abschlaege_verlangt,
        abschlaege_vereinbart=abschlaege_vereinbart,
    )
    verguetung = _geld(vereinbarte_verguetung)
    abschlag, sicherheit = _geld(naechste_abschlagszahlung), _geld(vereinbarte_sicherheit)
    for parameter in ("verbraucherbauvertrag", "abschlaege_verlangt", "abschlaege_vereinbart"):
        _wahrheitswert(eingaben[parameter], parameter)
    anwendbar = verbraucherbauvertrag and (abschlaege_verlangt or abschlaege_vereinbart)
    ergebnis = _geld_ergebnis(
        _bruch(0) if anwendbar else None,
        "BGB_VERBRAUCHERBAU_SICHERUNGSGRENZE",
        eingaben,
        [{"operation": "Verbraucherbau und verlangte oder vereinbarte Abschläge",
          "anwendbar": anwendbar}],
    )
    if anwendbar:
        grenze = min(abschlag, _multiplizieren(verguetung, _bruch(1, 5)))
        ergebnis["wert"] = dict(
            betragsgrenze=_bruchteile(grenze),
            betragsgrenze_ueberschritten=sicherheit > grenze,
        )
        ergebnis["rechenschritte"].append(
            {"operation": "Minimum aus nächstem Abschlag und 20 Prozent der Vergütung; strenger Vergleich"}
        )
    return ergebnis
