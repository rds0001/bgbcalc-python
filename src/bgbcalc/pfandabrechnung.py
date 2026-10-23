"""Numerische Forderungsabrechnung bei Pfandverwertung (§§1247,1259)."""
from .betraege import _geld, _wahrheitswert
from .kalender import _auswahl, _ergebnis, _text
from .zahlen import _subtrahieren
from .zinsen import _bruchteile


def pfand_verwertungsabrechnung(gesicherte_forderung=None, befriedigungsbasis=None,
        verwertungsart=None, anwendungsfall_qualifiziert=None, bewertungsnachweis=None):
    """Verfügbaren Befriedigungswert bis Forderungshöhe tilgen und beide Restbeträge ausweisen."""
    forderung = _geld(gesicherte_forderung)
    basis = _geld(befriedigungsbasis)
    _auswahl(verwertungsart, 'verwertungsart', ('erloes_1247', 'marktpreis_eigentumszufall_1259'))
    _wahrheitswert(anwendungsfall_qualifiziert, 'anwendungsfall_qualifiziert')
    _text(bewertungsnachweis, 'bewertungsnachweis')
    tilgung = min(forderung, basis)
    eingaben = dict(gesicherte_forderung=gesicherte_forderung, befriedigungsbasis=befriedigungsbasis,
        verwertungsart=verwertungsart, anwendungsfall_qualifiziert=anwendungsfall_qualifiziert,
        bewertungsnachweis=bewertungsnachweis)
    wert = dict(getilgte_forderung=_bruchteile(tilgung), restforderung=_bruchteile(_subtrahieren(forderung, tilgung)),
        ueberschiessender_wert=_bruchteile(_subtrahieren(basis, tilgung))) if anwendungsfall_qualifiziert else None
    ergebnis = _ergebnis(wert, 'EUR', 'BGB_PFAND_VERWERTUNGSABRECHNUNG', eingaben,
        [dict(operation='Minimum aus gesicherter Forderung und qualifizierter Befriedigungsbasis als Tilgung; Differenzen als Restforderung und überschießenden Wert ausweisen')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if anwendungsfall_qualifiziert else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Eine gesicherte Forderungsposition nach qualifizierter Kosten-/Rangbereinigung; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['Bei1247 ist befriedigungsbasis der nach rechtlich vorrangigen Kosten und Ansprüchen für diesen Pfandgläubiger verfügbare Verwertungserlös. Tilgung zählt als Berichtigung durch den Eigentümer; überschießender Erlös tritt an Stelle des Pfandes, keine automatische Auszahlung an den Eigentümer oder Gläubiger. Bei1259 bezeichnet die Basis den gesamten Börsen-/Marktwert des Pfandes am Fälligkeitstag, nicht am späteren Übertragungstag. Nur qualifiziert vereinbarter Eigentumszufall innerhalb des besonderen persönlichen Anwendungsbereichs; kein pauschales Verfallrecht für Verbrauchersicherheiten. Überschießender Wert ist dort nur eine Rechendifferenz, keine aus1259 erfundene Erstattungspflicht. Andere Forderungen, Rangverteilungen und mehrere Pfandrechte vorgelagert abgrenzen; keine Doppelbefriedigung.']
    return ergebnis
