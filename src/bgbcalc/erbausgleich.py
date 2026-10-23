"""Ausgleichung bewerteter Zuwendungen innerhalb einer bestimmten Erbengruppe."""

from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _fehler, _ganzzahl, _text, _vorhanden
from .zahlen import (
    GRENZE, _addieren, _bruch, _dividieren, _multiplizieren, _subtrahieren,
)
from .zinsen import _bruchteile


def erb_zuwendungen_ausgleichen(
    gruppennachlass=None, miterben=None, ausgleichung_anwendbar=None, bewertungsnachweis=None,
):
    """§§ 2055/2056: Hinzurechnung, Anrechnung und wiederholter Überempfangausschluss."""
    nachlass = _geld(gruppennachlass)
    _vorhanden(miterben, "miterben")
    if not isinstance(miterben, list) or not 1 <= len(miterben) <= 1000:
        _fehler("miterben", "Liste mit 1 bis 1000 Miterben erforderlich.")
    _wahrheitswert(ausgleichung_anwendbar, "ausgleichung_anwendbar")
    _text(bewertungsnachweis, "bewertungsnachweis")
    namen, quoten, zuwendungen = [], [], []
    gesamtquote = _bruch(0)
    for person in miterben:
        if not isinstance(person, dict) or set(person) != {
            "person_id", "erbquote_zaehler", "erbquote_nenner", "ausgleichungswert",
        }:
            _fehler("miterben", "Objekte mit genau person_id, erbquote_zaehler, erbquote_nenner und ausgleichungswert erforderlich.")
        kennung = _text(person["person_id"], "person_id")
        if kennung in namen:
            _fehler("person_id", "Jede Person darf nur einmal zur Ausgleichungsgruppe gehören.")
        zaehler = _ganzzahl(person["erbquote_zaehler"], "erbquote_zaehler", 1, GRENZE)
        nenner = _ganzzahl(person["erbquote_nenner"], "erbquote_nenner", 1, GRENZE)
        quote = _bruch(zaehler, nenner)
        gesamtquote = _addieren(gesamtquote, quote)
        namen.append(kennung)
        quoten.append(quote)
        zuwendungen.append(_geld(person["ausgleichungswert"]))
    if gesamtquote != 1:
        _fehler("miterben", "Positive Quoten innerhalb der Ausgleichungsgruppe müssen zusammen 1 ergeben.")
    ergebnis = _geld_ergebnis(
        _bruch(0) if ausgleichung_anwendbar else None, "BGB_ERB_ZUWENDUNGEN_AUSGLEICHEN",
        dict(gruppennachlass=gruppennachlass, miterben=miterben,
             ausgleichung_anwendbar=ausgleichung_anwendbar, bewertungsnachweis=bewertungsnachweis),
        [{"operation": "Vorgegebene Ausgleichungsgruppe prüfen", "anwendbar": ausgleichung_anwendbar}],
    )
    if not ausgleichung_anwendbar:
        return ergebnis
    aktiv = list(range(len(namen)))
    ausgeschlossen = []
    betraege = [_bruch(0) for _ in namen]
    while True:
        masse, quotensumme = nachlass, _bruch(0)
        for i in aktiv:
            masse = _addieren(masse, zuwendungen[i])
            quotensumme = _addieren(quotensumme, quoten[i])
        anteile = {i: _multiplizieren(masse, _dividieren(quoten[i], quotensumme)) for i in aktiv}
        ueberempfaenger = [i for i in aktiv if zuwendungen[i] > anteile[i]]
        ergebnis["rechenschritte"].append(dict(
            operation="Zuwendungen hinzurechnen; Überempfänger mit Zuwendung und Quote herausnehmen",
            rechenmasse=_bruchteile(masse), verbleibende_quotensumme=_bruchteile(quotensumme),
            ausgeschlossene_personen=[namen[i] for i in ueberempfaenger],
        ))
        if not ueberempfaenger:
            for i in aktiv:
                betraege[i] = _subtrahieren(anteile[i], zuwendungen[i])
            break
        ausgeschlossen.extend(ueberempfaenger)
        aktiv = [i for i in aktiv if i not in ueberempfaenger]
    ergebnis["wert"] = dict(
        verteilung=[dict(person_id=name, betrag=_bruchteile(betraege[i]), ausser_ansatz=i in ausgeschlossen)
                    for i, name in enumerate(namen)],
        ausser_ansatz=[name for i, name in enumerate(namen) if i in ausgeschlossen],
    )
    return ergebnis
