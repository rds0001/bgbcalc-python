"""Anteilige Lasten und Kosten einer Bruchteilsgemeinschaft."""

from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _fehler, _ganzzahl, _text, _vorhanden
from .zahlen import GRENZE, _addieren, _bruch, _multiplizieren
from .zinsen import _bruchteile


def gemeinschaft_lastenanteile(
    gesamtbetrag=None, teilhaber=None, gleiche_anteile_im_zweifel=None, gemeinschaft_nach_bruchteilen=None,
):
    """§§ 742/748: Lasten und Kosten nach ausdrücklichen oder gleichen Anteilen."""
    betrag = _geld(gesamtbetrag)
    _vorhanden(teilhaber, "teilhaber")
    if not isinstance(teilhaber, list) or not 2 <= len(teilhaber) <= 1000:
        _fehler("teilhaber", "Liste mit 2 bis 1000 Teilhabern erforderlich.")
    _wahrheitswert(gleiche_anteile_im_zweifel, "gleiche_anteile_im_zweifel")
    _wahrheitswert(gemeinschaft_nach_bruchteilen, "gemeinschaft_nach_bruchteilen")
    namen, quoten = [], []
    summe = _bruch(0)
    for person in teilhaber:
        if not isinstance(person, dict) or set(person) != {"person_id", "anteil_zaehler", "anteil_nenner"}:
            _fehler("teilhaber", "Genau person_id, anteil_zaehler und anteil_nenner erforderlich.")
        kennung = _text(person["person_id"], "person_id")
        if kennung in namen:
            _fehler("person_id", "Teilhaber dürfen nicht doppelt vorkommen.")
        zaehler, nenner = person["anteil_zaehler"], person["anteil_nenner"]
        if gleiche_anteile_im_zweifel:
            if zaehler is not None or nenner is not None:
                _fehler("gleiche_anteile_im_zweifel", "Zweifelsregel nicht mit ausdrücklich vorgegebenen Anteilen vermischen.")
            quote = _bruch(1, len(teilhaber))
        else:
            _ganzzahl(zaehler, "anteil_zaehler", 1, GRENZE)
            _ganzzahl(nenner, "anteil_nenner", 1, GRENZE)
            quote = _bruch(zaehler, nenner)
        summe = _addieren(summe, quote)
        namen.append(kennung)
        quoten.append(quote)
    if summe != 1:
        _fehler("teilhaber", "Positive Teilhaberanteile müssen zusammen 1 ergeben.")
    ergebnis = _geld_ergebnis(
        _bruch(0) if gemeinschaft_nach_bruchteilen else None, "BGB_GEMEINSCHAFT_LASTENANTEILE",
        dict(gesamtbetrag=gesamtbetrag, teilhaber=teilhaber,
             gleiche_anteile_im_zweifel=gleiche_anteile_im_zweifel,
             gemeinschaft_nach_bruchteilen=gemeinschaft_nach_bruchteilen),
        [{"operation": "Anwendbarkeit der Bruchteilsgemeinschaft", "anwendbar": gemeinschaft_nach_bruchteilen},
         {"operation": "Gesamtbetrag nach Teilhaberanteilen verteilen",
          "zweifelsregel_gleiche_anteile": gleiche_anteile_im_zweifel}],
    )
    if gemeinschaft_nach_bruchteilen:
        ergebnis["wert"] = [
            dict(person_id=n, anteil=_bruchteile(q), betrag=_bruchteile(_multiplizieren(betrag, q)))
            for n, q in zip(namen, quoten)
        ]
    return ergebnis
