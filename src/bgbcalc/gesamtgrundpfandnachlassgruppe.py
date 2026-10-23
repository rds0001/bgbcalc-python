"""Interne Lastenteilung bei Gesamtgrund-/Gesamtrentenschuld (§2168)."""
from .betraege import _geld, _wahrheitswert
from .kalender import _auswahl, _ergebnis, _fehler, _text, _vorhanden
from .zahlen import _addieren, _bruch, _dividieren, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile


from .gesamtgrundpfandvermaechtnis import _gesamtgrundpfand_ergebnis

def gesamtgrundpfandvermaechtnis_nachlassgruppe_mit_fremdhaftung(gesamtbelastungsbetrag=None, grundpfandart=None,
    grundstuecke=None, vermachtes_grundstueck_id=None, fremdhaftung_und_erblasserpflicht_qualifiziert=None,
    zweifelsregel_anwendbar=None, rechts_und_bewertungsnachweis=None):
    """§2168 Absatz2: ausschließlich Nachlasswerte vergleichen, Eigenwertdeckel anwenden."""
    betrag = _geld(gesamtbelastungsbetrag)
    _auswahl(grundpfandart, 'grundpfandart', ('gesamtgrundschuld', 'gesamtrentenschuld'))
    _vorhanden(grundstuecke, 'grundstuecke')
    if not isinstance(grundstuecke, list) or not 2 <= len(grundstuecke) <= 1000:
        _fehler('grundstuecke', 'Liste mit 2 bis 1000 mithaftenden Grundstücken erforderlich.')
    namen, werte = [], []
    summe = _bruch(0)
    for g in grundstuecke:
        if not isinstance(g, dict) or set(g) != {'grundstueck_id', 'grundstueckswert', 'vorrangige_belastungen'}:
            _fehler('grundstuecke', 'Genau grundstueck_id, grundstueckswert und vorrangige_belastungen erforderlich.')
        name = _text(g['grundstueck_id'], 'grundstueck_id')
        if name in namen:
            _fehler('grundstueck_id', 'Grundstücke dürfen nicht doppelt vorkommen.')
        bereinigt = max(_subtrahieren(_geld(g['grundstueckswert']), _geld(g['vorrangige_belastungen'])), _bruch(0))
        namen.append(name)
        werte.append(bereinigt)
        summe = _addieren(summe, bereinigt)
    vermacht = _text(vermachtes_grundstueck_id, 'vermachtes_grundstueck_id')
    if vermacht not in namen:
        _fehler('vermachtes_grundstueck_id', 'Vermachtes Grundstück muss in vollständiger Grundstücksliste enthalten sein.')
    _wahrheitswert(fremdhaftung_und_erblasserpflicht_qualifiziert, 'fremdhaftung_und_erblasserpflicht_qualifiziert')
    _wahrheitswert(zweifelsregel_anwendbar, 'zweifelsregel_anwendbar')
    _text(rechts_und_bewertungsnachweis, 'rechts_und_bewertungsnachweis')
    eingaben = dict(gesamtbelastungsbetrag=gesamtbelastungsbetrag, grundpfandart=grundpfandart,
        grundstuecke=grundstuecke, vermachtes_grundstueck_id=vermachtes_grundstueck_id,
        fremdhaftung_und_erblasserpflicht_qualifiziert=fremdhaftung_und_erblasserpflicht_qualifiziert,
        zweifelsregel_anwendbar=zweifelsregel_anwendbar, rechts_und_bewertungsnachweis=rechts_und_bewertungsnachweis)
    wert = None
    if fremdhaftung_und_erblasserpflicht_qualifiziert and zweifelsregel_anwendbar:
        eigenwert = werte[namen.index(vermacht)]
        quote = _dividieren(eigenwert, summe) if summe else None
        anteil = _multiplizieren(betrag, quote) if quote is not None else None
        wert = dict(bereinigter_wert_vermachtes_grundstueck=_bruchteile(eigenwert),
            bereinigter_gesamtwert=_bruchteile(summe), wertquote=_bruchteile(quote) if quote is not None else None,
            anteil_vor_wertbegrenzung=_bruchteile(anteil) if anteil is not None else None,
            befriedigungsbetrag=_bruchteile(min(anteil,eigenwert) if anteil is not None else _bruch(0)))
    return _gesamtgrundpfand_ergebnis(wert, 'BGB_GESAMTGRUNDPFANDVERMAECHTNIS_NACHLASSGRUPPE_MIT_FREMDHAFTUNG', eingaben,
        '2168II-Nachlassvergleichsgruppe rangbereinigen; Fremdwerte ausgeschlossen; Gesamtbelastung mal Eigenwertquote,aufEigenwertbegrenzen',
        'Nur2168II mit weiterenNachlassgrundstücken und mindestens einemFremdgrundstück sowie qualifizierterErblasserpflicht imErbfall gegenüberFremdeigentümer/Rechtsvorgänger für betrachtetenGesamtbetrag. grundstuecke enthält vollständig ausschließlichmithaftendeNachlassgrundstücke,keinFremdgrundstück.2167-Quote nurinnerhalbNachlassgruppe; anschließend2166I-Eigenwertdeckel. Fremdwerte sindkeinInput undverdünnenQuoten nicht. Keine2166II-Drittberichtigung/ungleicheTeilpflichten/abweichendenInnenlasten. WertebeiEigentumsübergangvergleichbar; RentenschuldnurqualifiziertereinheitlicherEUR-Betrag,keineKapitalisierung. NurinterneLast,keineAußenhaftungs-/Fälligkeitsentscheidung.')

