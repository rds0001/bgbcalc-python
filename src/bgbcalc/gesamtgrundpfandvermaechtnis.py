"""Interne Lastenteilung bei Gesamtgrund-/Gesamtrentenschuld (§2168)."""
from .betraege import _geld, _wahrheitswert
from .kalender import _auswahl, _ergebnis, _fehler, _text, _vorhanden
from .zahlen import _addieren, _bruch, _dividieren, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile


def _gesamtgrundpfand_ergebnis(wert, kennung, eingaben, operation, hinweis):
    ergebnis = _ergebnis(wert, 'EUR_und_quote', kennung, eingaben,
        [dict(operation=operation)], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Feste lokale BGB-Fassung; rechtlich vergleichbare Grundstückswerte bei Eigentumsübergang und einheitlich qualifizierter Bezugsbetrag der Gesamtbelastung.']
    ergebnis['hinweise'] = [hinweis]
    return ergebnis


def gesamtgrundpfandvermaechtnis_nachlassanteil(gesamtbelastungsbetrag=None, grundpfandart=None,
    grundstuecke=None, vermachtes_grundstueck_id=None, ausschliesslich_nachlassgrundstuecke=None,
    zweifelsregel_anwendbar=None, bewertungsnachweis=None):
    """§2168 Absatz1: Gesamtbelastung proportional verteilen, ohne zusätzlichen Schuld-/Wertdeckel."""
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
    if summe == 0:
        _fehler('grundstuecke', 'Positive Summe bereinigter Grundstückswerte für Verhältnis erforderlich.')
    _wahrheitswert(ausschliesslich_nachlassgrundstuecke, 'ausschliesslich_nachlassgrundstuecke')
    _wahrheitswert(zweifelsregel_anwendbar, 'zweifelsregel_anwendbar')
    _text(bewertungsnachweis, 'bewertungsnachweis')
    eingaben = dict(gesamtbelastungsbetrag=gesamtbelastungsbetrag, grundpfandart=grundpfandart,
        grundstuecke=grundstuecke, vermachtes_grundstueck_id=vermachtes_grundstueck_id,
        ausschliesslich_nachlassgrundstuecke=ausschliesslich_nachlassgrundstuecke,
        zweifelsregel_anwendbar=zweifelsregel_anwendbar, bewertungsnachweis=bewertungsnachweis)
    wert = None
    if ausschliesslich_nachlassgrundstuecke and zweifelsregel_anwendbar:
        eigenwert = werte[namen.index(vermacht)]
        quote = _dividieren(eigenwert, summe)
        wert = dict(bereinigter_wert_vermachtes_grundstueck=_bruchteile(eigenwert),
            bereinigter_gesamtwert=_bruchteile(summe), wertquote=_bruchteile(quote),
            zugeordneter_belastungsteil=_bruchteile(_multiplizieren(betrag, quote)))
    return _gesamtgrundpfand_ergebnis(wert, 'BGB_GESAMTGRUNDPFANDVERMAECHTNIS_NACHLASSANTEIL', eingaben,
        'Rangvorrangige Lasten von Grundstückswerten abziehen; nichtnegative Werte summieren; Gesamtbelastungsbetrag mit Wertquote des vermachten Grundstücks multiplizieren',
        'Nur§2168 Absatz1: sämtliche mithaftenden Grundstücke gehören zum Nachlass. Werte bei Eigentumsübergang auf Vermächtnisnehmer; nur rangvorrangige Lasten abziehen, nicht die Gesamtbelastung selbst. Keine zusätzliche Begrenzung auf Grundstückswert oder persönliche Schuld und kein Drittleistungsabzug aus§2166 Absatz2: Absatz1 verweist nur auf dessen Wertbestimmung. Gesamtbelastungsbetrag ist ein rechtlich bestimmter einheitlicher EUR-Bezugsbetrag der betrachteten Grund-/Rentenschuld; bei wiederkehrender Rentenschuld selben qualifizierten Zeitraum verwenden. Keine Kapitalisierung oder Wahl zwischen laufender Rente und Ablösungssumme. Interne Lastenverteilung gegenüber Erben, keine Einschränkung dinglicher Gläubigerrechte oder Fälligkeitsberechnung. Fremdgrundstücksfälle nach Absatz2 gesondert; abweichender Erblasserwille sperrt Zweifelsregel.')


def gesamtgrundpfandvermaechtnis_fremdgrundstueck(gesamtbelastungsbetrag=None, grundpfandart=None,
    wert_vermachtes_grundstueck=None, vorrangige_lasten_vermachtes_grundstueck=None,
    wert_fremdgrundstueck=None, vorrangige_lasten_fremdgrundstueck=None,
    erblasserpflicht_gegenueber_fremdeigentuemer=None, zweifelsregel_anwendbar=None,
    genau_zwei_grundstuecke_qualifiziert=None, bewertungsnachweis=None):
    """§2168 Absatz2: qualifizierter Fremdgrundstücksfall, alleiniger Nachlasswert als Deckel."""
    betrag = _geld(gesamtbelastungsbetrag)
    _auswahl(grundpfandart, 'grundpfandart', ('gesamtgrundschuld', 'gesamtrentenschuld'))
    eigener = max(_subtrahieren(_geld(wert_vermachtes_grundstueck), _geld(vorrangige_lasten_vermachtes_grundstueck)), _bruch(0))
    _geld(wert_fremdgrundstueck)
    _geld(vorrangige_lasten_fremdgrundstueck)
    summe = eigener
    eingaben = dict(gesamtbelastungsbetrag=gesamtbelastungsbetrag, grundpfandart=grundpfandart,
        wert_vermachtes_grundstueck=wert_vermachtes_grundstueck,
        vorrangige_lasten_vermachtes_grundstueck=vorrangige_lasten_vermachtes_grundstueck,
        wert_fremdgrundstueck=wert_fremdgrundstueck,
        vorrangige_lasten_fremdgrundstueck=vorrangige_lasten_fremdgrundstueck,
        erblasserpflicht_gegenueber_fremdeigentuemer=erblasserpflicht_gegenueber_fremdeigentuemer,
        zweifelsregel_anwendbar=zweifelsregel_anwendbar,
        genau_zwei_grundstuecke_qualifiziert=genau_zwei_grundstuecke_qualifiziert, bewertungsnachweis=bewertungsnachweis)
    for name in tuple(eingaben)[6:9]:
        _wahrheitswert(eingaben[name], name)
    _text(bewertungsnachweis, 'bewertungsnachweis')
    wert = None
    if erblasserpflicht_gegenueber_fremdeigentuemer and zweifelsregel_anwendbar and genau_zwei_grundstuecke_qualifiziert:
        quote = _dividieren(eigener, summe) if summe != 0 else None
        anteil = _multiplizieren(betrag, quote) if quote is not None else None
        wert = dict(bereinigter_wert_vermachtes_grundstueck=_bruchteile(eigener),
            bereinigter_gesamtwert=_bruchteile(summe), wertquote=_bruchteile(quote) if quote is not None else None,
            anteil_vor_wertbegrenzung=_bruchteile(anteil) if anteil is not None else None,
            befriedigungsbetrag=_bruchteile(min(anteil, eigener) if anteil is not None else _bruch(0)))
    return _gesamtgrundpfand_ergebnis(wert, 'BGB_GESAMTGRUNDPFANDVERMAECHTNIS_FREMDGRUNDSTUECK', eingaben,
        'Eigenwert um rangvorrangige Lasten bereinigen; nur Nachlassgrundstücke bilden2167-Vergleichsgruppe; hier einzigesNachlassgrundstück, Gesamtbetrag aufEigenwert begrenzen',
        'Nur2168Absatz2 mit genau einem vermachtenNachlassgrundstück und einem fremdenGrundstück. Erblasserpflicht imErbfall gegenüberFremdeigentümer/Rechtsvorgänger qualifizieren.2167 bezieht nurNachlassgrundstücke in Vergleichsgruppe ein: Fremdwerte mindern diese interneLast nicht. Hier einzigesNachlassgrundstück, deshalb Befriedigung=min(Gesamtbetrag,bereinigterEigenwert). bereinigter_gesamtwert ist alleinWertsumme derNachlassgrundstücke; wertquote beiEigenwertpositiv1,bei0NULL. Fremdwert-/Ranglastenparameter werden ausKompatibilitätsgründen validiert,aber nichtquotenbildend verwendet. Kein2166II-Drittleistungsabzug, keineAußenhaftungsbegrenzung, Rentenkapitalisierung oderFälligkeitsentscheidung. WeitereNachlassgrundstücke benötigen gesonderte2167-Quote.')
