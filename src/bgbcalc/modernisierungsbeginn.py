"""Beginn der erhöhten Miete nach § 559b Absatz 2."""

from .betraege import _geld, _wahrheitswert
from .kalender import _datum, _ergebnis, _monatsende
from .zahlen import _bruch, _multiplizieren


def modernisierung_erhoehungsbeginn(
    zugang_erklaerung=None,
    ankuendigung_ordnungsgemaess=None,
    angekuendigter_erhoehungsbetrag=None,
    tatsaechlicher_erhoehungsbetrag=None,
    erklaerung_wirksam=None,
):
    """Dritter Folgemonat; bei mindestens einem Verzögerungsgrund plus sechs Monate."""
    eingaben = dict(
        zugang_erklaerung=zugang_erklaerung,
        ankuendigung_ordnungsgemaess=ankuendigung_ordnungsgemaess,
        angekuendigter_erhoehungsbetrag=angekuendigter_erhoehungsbetrag,
        tatsaechlicher_erhoehungsbetrag=tatsaechlicher_erhoehungsbetrag,
        erklaerung_wirksam=erklaerung_wirksam,
    )
    zugang = _datum(zugang_erklaerung, "zugang_erklaerung")
    _wahrheitswert(ankuendigung_ordnungsgemaess, "ankuendigung_ordnungsgemaess")
    angekuendigt = _geld(angekuendigter_erhoehungsbetrag)
    tatsaechlich = _geld(tatsaechlicher_erhoehungsbetrag)
    _wahrheitswert(erklaerung_wirksam, "erklaerung_wirksam")
    ueberschreitung = tatsaechlich > _multiplizieren(angekuendigt, _bruch(11, 10))
    verlaengerung = not ankuendigung_ordnungsgemaess or ueberschreitung
    wert = None
    if erklaerung_wirksam:
        wert = _monatsende(zugang.replace(day=1), 9 if verlaengerung else 3, False).isoformat()
    ergebnis = _ergebnis(
        wert, "datum", "BGB_MODERNISIERUNG_ERHOEHUNGSBEGINN", eingaben,
        [{"operation": "Tatsächlicher Betrag über 110 Prozent der Ankündigung",
          "erfuellt": ueberschreitung},
         {"operation": "Einmalige Verlängerung um sechs Monate",
          "erfuellt": verlaengerung},
         {"operation": "Beginn des dritten beziehungsweise neunten Folgemonats",
          "ergebnis": wert}],
        eingaben.copy(),
    )
    ergebnis["status"] = "BERECHNET" if erklaerung_wirksam else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = [
        "Feste lokale BGB-Fassung; Wirksamkeit der Erklärung und Ordnungsmäßigkeit der Ankündigung ausdrücklich eingegeben."
    ]
    ergebnis["hinweise"] = [
        "Beginn der erhöhten Miete, keine Zahlungsfälligkeitsberechnung oder Feiertagsverschiebung.",
        "§ 559b Absatz 2; entsprechende Anwendung nach § 559c Absatz 3 und § 559e Absatz 4 setzt deren Voraussetzungen voraus."
    ]
    return ergebnis
