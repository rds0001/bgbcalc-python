"""Wertbegrenzte interne Hypothekenlast eines Grundstücksvermächtnisses§2166."""
from .betraege import _geld, _wahrheitswert
from .kalender import _ergebnis, _fehler, _text
from .zahlen import _bruch, _subtrahieren
from .zinsen import _bruchteile


def hypothekenvermaechtnis_befriedigungsbetrag(schuldbetrag=None, grundstueckswert=None,
    vorrangige_belastungen=None, vom_dritten_erlangbarer_betrag=None,
    schuld_nach_2166_qualifiziert=None, zweifelsregel_anwendbar=None,
    hoechstbetragshypothek=None, weitere_grundstuecke_mithaftend=None, bewertungsnachweis=None):
    """Schuld nach Drittleistung auf um vorrangige Belastungen bereinigten Wert begrenzen."""
    schuld = _geld(schuldbetrag)
    wert = _geld(grundstueckswert)
    lasten = _geld(vorrangige_belastungen)
    dritter = _geld(vom_dritten_erlangbarer_betrag)
    if dritter > schuld:
        _fehler('vom_dritten_erlangbarer_betrag', 'Erlangbarer Drittbetrag darf die betrachtete Schuld nicht übersteigen.')
    eingaben = dict(schuldbetrag=schuldbetrag, grundstueckswert=grundstueckswert,
        vorrangige_belastungen=vorrangige_belastungen, vom_dritten_erlangbarer_betrag=vom_dritten_erlangbarer_betrag,
        schuld_nach_2166_qualifiziert=schuld_nach_2166_qualifiziert, zweifelsregel_anwendbar=zweifelsregel_anwendbar,
        hoechstbetragshypothek=hoechstbetragshypothek, weitere_grundstuecke_mithaftend=weitere_grundstuecke_mithaftend,
        bewertungsnachweis=bewertungsnachweis)
    for name in tuple(eingaben)[4:8]:
        _wahrheitswert(eingaben[name], name)
    _text(bewertungsnachweis, 'bewertungsnachweis')
    gilt = schuld_nach_2166_qualifiziert and zweifelsregel_anwendbar and not hoechstbetragshypothek and not weitere_grundstuecke_mithaftend
    ergebniswert = None
    if gilt:
        deckung = max(_subtrahieren(wert, lasten), _bruch(0))
        rest = _subtrahieren(schuld, dritter)
        ergebniswert = dict(bereinigter_grundstueckswert=_bruchteile(deckung),
            schuld_nach_drittberichtigung=_bruchteile(rest), befriedigungsbetrag=_bruchteile(min(rest, deckung)))
    ergebnis = _ergebnis(ergebniswert, 'EUR', 'BGB_HYPOTHEKENVERMAECHTNIS_BEFRIEDIGUNGSBETRAG', eingaben,
        [dict(operation='Wert bei Eigentumsübergang um rangvorrangige Belastungen mindern; verbleibende Schuld nach erlangbarer Drittberichtigung auf nichtnegative Deckung begrenzen')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if gilt else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Feste lokale BGB-Fassung; einzelnes vermachtes Nachlassgrundstück ohne weitere mithaftende Grundstücke, Wert und Schuld rechtlich vergleichbar qualifiziert.']
    ergebnis['hinweise'] = ['Nur interne Verpflichtung des Vermächtnisnehmers gegenüber dem Erben zur Befriedigung des Gläubigers nach§2166, keine Begrenzung dinglicher Gläubigerrechte. Schuld muss Schuld des Erblassers sein oder eine Schuld, zu deren Berichtigung er dem Schuldner gegenüber verpflichtet war. Grundstückswert im Zeitpunkt des Eigentumsübergangs; nur der betrachteten Hypothek im Rang vorgehende Belastungen abziehen, nicht die betrachtete Hypothek selbst doppelt. Drittbetrag ist die vom Erben rechtlich und tatsächlich erlangbare Berichtigung durch einen gegenüber dem Erblasser verpflichteten Dritten, nicht beliebige Zahlung eines Dritten; ohne entsprechenden Dritten null. Keine erfundene Bewertung oder Vollstreckungsprognose. Höchstbetragshypothek§1190 ausgeschlossen; mithaftende Grundstücke und Verteilung§2167 sowie Gesamtgrund-/Rentenschulden§2168 gesondert. Abweichender Erblasserwille verhindert Anwendung der Zweifelsregel. Keine Fälligkeitsberechnung.']
    return ergebnis
