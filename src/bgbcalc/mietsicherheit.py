"""Höchstbetrag und Teilzahlungen der Wohnraummietsicherheit."""

from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _datum, _fehler
from .zahlen import _bruch, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile


def mietsicherheit_hoechstbetrag(
    monatsmiete=None, ausgewiesene_betriebskosten=None, wohnraummietverhaeltnis=None,
):
    """§ 551 Abs. 1: dreifache Monatsmiete ohne ausgewiesene Betriebskosten."""
    miete, kosten = _geld(monatsmiete), _geld(ausgewiesene_betriebskosten)
    _wahrheitswert(wohnraummietverhaeltnis, "wohnraummietverhaeltnis")
    if kosten > miete:
        _fehler("ausgewiesene_betriebskosten", "Ausgewiesene Betriebskosten dürfen die Monatsmiete nicht übersteigen.")
    basis = _subtrahieren(miete, kosten)
    wert = _multiplizieren(basis, _bruch(3)) if wohnraummietverhaeltnis else None
    return _geld_ergebnis(
        wert, "BGB_MIETSICHERHEIT_HOECHSTBETRAG",
        dict(monatsmiete=monatsmiete, ausgewiesene_betriebskosten=ausgewiesene_betriebskosten,
             wohnraummietverhaeltnis=wohnraummietverhaeltnis),
        [{"operation": "Wohnraummietverhältnis prüfen", "anwendbar": wohnraummietverhaeltnis},
         {"operation": "Ausgewiesene Betriebskosten abziehen; verbleibende Monatsmiete verdreifachen",
          "massgebliche_monatsmiete": _bruchteile(basis)}],
    )


def mietsicherheit_raten(
    geschuldete_geldsicherheit=None, mietbeginn=None, zweite_mietfaelligkeit=None,
    dritte_mietfaelligkeit=None, wohnraummietverhaeltnis=None, geldsicherheit_geschuldet=None,
):
    """§ 551 Abs. 2: drei gleiche Beträge mit ausdrücklich bestimmten Terminen."""
    sicherheit = _geld(geschuldete_geldsicherheit)
    termine = (mietbeginn, zweite_mietfaelligkeit, dritte_mietfaelligkeit)
    daten = [_datum(tag, name) for tag, name in zip(
        termine, ("mietbeginn", "zweite_mietfaelligkeit", "dritte_mietfaelligkeit")
    )]
    if not daten[0] < daten[1] < daten[2]:
        _fehler("mietfaelligkeiten", "Die drei Teilzahlungstermine müssen zeitlich aufeinander folgen.")
    _wahrheitswert(wohnraummietverhaeltnis, "wohnraummietverhaeltnis")
    _wahrheitswert(geldsicherheit_geschuldet, "geldsicherheit_geschuldet")
    anwendbar = wohnraummietverhaeltnis and geldsicherheit_geschuldet
    ergebnis = _geld_ergebnis(
        _bruch(0) if anwendbar else None, "BGB_MIETSICHERHEIT_RATEN",
        dict(geschuldete_geldsicherheit=geschuldete_geldsicherheit, mietbeginn=mietbeginn,
             zweite_mietfaelligkeit=zweite_mietfaelligkeit, dritte_mietfaelligkeit=dritte_mietfaelligkeit,
             wohnraummietverhaeltnis=wohnraummietverhaeltnis, geldsicherheit_geschuldet=geldsicherheit_geschuldet),
        [{"operation": "Geschuldete Geldsicherheit im Wohnraummietverhältnis", "anwendbar": anwendbar},
         {"operation": "Dritteln; Mietbeginn und ausdrücklich bestimmte Folgemietfälligkeiten verwenden"}],
    )
    if anwendbar:
        rate = _multiplizieren(sicherheit, _bruch(1, 3))
        ergebnis["wert"] = [dict(nummer=i+1, faellig_am=tag, betrag=_bruchteile(rate))
                            for i, tag in enumerate(termine)]
    return ergebnis
