"""Betragswirkung einer rechtlich qualifizierten Aufrechnung."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler, _text
from .zahlen import _subtrahieren
from .zinsen import _bruchteile








def aufrechnung_betragswirkung(
    eigene_forderung=None, gegenforderung=None, aufrechnungslage_am=None,
    erklaerung_am=None, aufrechnung_zulaessig_und_erklaert=None, forderungsnachweis=None,
):
    """§389: Forderungen im deckungsgleichen Betrag rückwirkend erlöschen lassen."""
    eigene = _geld(eigene_forderung)
    gegen = _geld(gegenforderung)
    lage = _datum(aufrechnungslage_am, "aufrechnungslage_am")
    erklaerung = _datum(erklaerung_am, "erklaerung_am")
    if lage > erklaerung:
        _fehler("aufrechnungslage_am", "Aufrechnungslage darf nicht erst nach der Erklärung eintreten.")
    _wahrheitswert(aufrechnung_zulaessig_und_erklaert, "aufrechnung_zulaessig_und_erklaert")
    _text(forderungsnachweis, "forderungsnachweis")
    eingaben = dict(eigene_forderung=eigene_forderung, gegenforderung=gegenforderung,
        aufrechnungslage_am=aufrechnungslage_am, erklaerung_am=erklaerung_am,
        aufrechnung_zulaessig_und_erklaert=aufrechnung_zulaessig_und_erklaert,
        forderungsnachweis=forderungsnachweis)
    ergebnis = _geld_ergebnis(None, "BGB_AUFRECHNUNG_BETRAGSWIRKUNG", eingaben,
        [dict(operation="Deckung als Minimum beider Forderungen; beide Restbeträge und gesetzlichen rückwirkenden Erlöschenszeitpunkt ausweisen")])
    if aufrechnung_zulaessig_und_erklaert:
        deckung = min(eigene, gegen)
        ergebnis["wert"] = dict(erloschener_betrag_je_forderung=_bruchteile(deckung),
            rest_eigene_forderung=_bruchteile(_subtrahieren(eigene, deckung)),
            rest_gegenforderung=_bruchteile(_subtrahieren(gegen, deckung)), erloeschenszeitpunkt_am=lage.isoformat())
        ergebnis["status"] = "BERECHNET"
    ergebnis["hinweise"].append("Eine rechtlich bestimmte Paarung gleichartiger Geldforderungen in EUR; Beträge zur maßgeblichen Aufrechnungslage, nicht ungeprüft inklusive späterer Zinsen. Mehrere Forderungen und Zins-/Kostenreihenfolge§396 in Verbindung mit§§366/367 separat. Nur taggenau rechtlich normalisierte Ereignisdaten; untertägige Reihenfolge nicht aus gleichem Datum folgern. Voraussetzungen, Einreden und Verbote vorab prüfen.")
    return ergebnis
