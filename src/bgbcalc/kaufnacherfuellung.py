"""Fehlgeschlagene Nachbesserung und Fristsetzungsausnahmen beim Verbrauchsgüterkauf."""
from .betraege import _wahrheitswert
from .kalender import _auswahl, _ergebnis, _ganzzahl, _text
from .zahlen import GRENZE


def nachbesserung_fehlgeschlagen(
    erfolglose_versuche=None, abweichende_umstaende=None,
    fehlgeschlagen_nach_einzelfall=None, regel_440_anwendbar=None, einordnungsnachweis=None,
):
    """§440 Satz2: Zweitversuchsregel mit ausdrücklich bewerteter Einzelfallabweichung."""
    anzahl = _ganzzahl(erfolglose_versuche, "erfolglose_versuche", 0, GRENZE)
    eingaben = dict(erfolglose_versuche=erfolglose_versuche, abweichende_umstaende=abweichende_umstaende,
        fehlgeschlagen_nach_einzelfall=fehlgeschlagen_nach_einzelfall,
        regel_440_anwendbar=regel_440_anwendbar, einordnungsnachweis=einordnungsnachweis)
    for name in tuple(eingaben)[1:-1]:
        _wahrheitswert(eingaben[name], name)
    _text(einordnungsnachweis, "einordnungsnachweis")
    wert = None
    if regel_440_anwendbar:
        wert = fehlgeschlagen_nach_einzelfall if abweichende_umstaende else anzahl >= 2
    ergebnis = _ergebnis(wert, "wahrheitswert", "BGB_NACHBESSERUNG_FEHLGESCHLAGEN", eingaben,
        [dict(operation="Mindestens zwei erfolglose Nachbesserungsversuche; bei abweichenden Umständen belegte Einzelfallbewertung einsetzen")], eingaben.copy())
    ergebnis["status"] = "BERECHNET" if regel_440_anwendbar else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = ["Dieselbe rechtlich zusammengehörige Nachbesserung; erfolglose Versuche und etwaige abweichende Umstände geprüft."]
    ergebnis["hinweise"] = ["Keine starre Zweiversuchsregel bei abweichender Art der Sache, des Mangels oder sonstigen Umständen. Nur Nachbesserung, nicht automatisch Ersatzlieferung. §475d weicht für erfasste Verbrauchsgüterfälle von§440 ab; regel_440_anwendbar dort FALSE. FALSE beim Ergebnis bestätigt nicht, dass Fristsetzung aus anderen Gründen erforderlich ist; Rücktritts- und Schadensersatzvoraussetzungen separat."]
    return ergebnis


