"""Mangelbedingter Fehlbetrag der Schenkungsauflage nach § 526 Satz 1."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _text
from .zahlen import _bruch, _subtrahieren


def schenkungsauflage_fehlbetrag(
    erforderliche_aufwendungen=None, wert_der_mangelhaften_zuwendung=None,
    unterdeckung_vollstaendig_mangelbedingt=None, bewertungsnachweis=None,
):
    """Positiver Abstand zwischen Auflagenaufwand und mangelbedingt reduziertem Wert."""
    eingaben = dict(erforderliche_aufwendungen=erforderliche_aufwendungen,
        wert_der_mangelhaften_zuwendung=wert_der_mangelhaften_zuwendung,
        unterdeckung_vollstaendig_mangelbedingt=unterdeckung_vollstaendig_mangelbedingt,
        bewertungsnachweis=bewertungsnachweis)
    aufwand = _geld(erforderliche_aufwendungen)
    wert = _geld(wert_der_mangelhaften_zuwendung)
    _wahrheitswert(unterdeckung_vollstaendig_mangelbedingt, "unterdeckung_vollstaendig_mangelbedingt")
    _text(bewertungsnachweis, "bewertungsnachweis")
    fehlbetrag = None
    if unterdeckung_vollstaendig_mangelbedingt:
        fehlbetrag = max(_subtrahieren(aufwand, wert), _bruch(0))
    ergebnis = _geld_ergebnis(fehlbetrag, "BGB_SCHENKUNGSAUFLAGE_FEHLBETRAG", eingaben,
        [dict(operation="Mangelbedingt unzureichenden Zuwendungswert von erforderlichem Auflagenaufwand abziehen, mindestens null")])
    ergebnis["hinweise"].append("Nur § 526 Satz 1 bei vollständig mangelbedingter Unterdeckung. Teilweise anders verursachte Unterdeckung gesondert bestimmen; FALSE ergibt NICHT_ANWENDBAR. Bereits geleisteter Ausgleich und Aufwendungsersatz nach Satz 2 werden hier nicht verrechnet.")
    return ergebnis
