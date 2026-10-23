"""Numerische Nachlass-Restdeckung und Nacherbhaftung (§§1973ff.,2144/2145)."""
from .betraege import _geld, _wahrheitswert
from .kalender import _auswahl, _ergebnis, _fehler, _text
from .zahlen import _addieren, _bruch, _subtrahieren
from .zinsen import _bruchteile


def _haftungsrest_ergebnis(wert, regel, eingaben, operation, hinweis):
    ergebnis = _ergebnis(wert, 'EUR', regel, eingaben, [dict(operation=operation)], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Rechtlich qualifizierte Haftungsmasse, individuelle Forderung und vorrangige Bindungen; keine automatische Insolvenz- oder Rangprüfung.']
    ergebnis['hinweise'] = [hinweis]
    return ergebnis


def nachlassglaeubiger_restdeckung(haftungsmasse_vor_bindungen=None, vorrangig_gebundener_betrag=None,
    forderungsbetrag=None, haftungsfall=None, rang_und_einrede_qualifiziert=None, bewertungsnachweis=None):
    """Vorqualifizierte vorrangige Bindungen abziehen; eine Forderung bis zur freien Masse decken."""
    masse = _geld(haftungsmasse_vor_bindungen)
    bindung = _geld(vorrangig_gebundener_betrag)
    forderung = _geld(forderungsbetrag)
    _auswahl(haftungsfall, 'haftungsfall', ('ausgeschlossener_glaeubiger_1973', 'spaetglaeubiger_1974', 'duerftigkeit_1990', 'vermaechtnisueberschuldung_1992'))
    _wahrheitswert(rang_und_einrede_qualifiziert, 'rang_und_einrede_qualifiziert')
    _text(bewertungsnachweis, 'bewertungsnachweis')
    eingaben = dict(haftungsmasse_vor_bindungen=haftungsmasse_vor_bindungen, vorrangig_gebundener_betrag=vorrangig_gebundener_betrag,
        forderungsbetrag=forderungsbetrag, haftungsfall=haftungsfall, rang_und_einrede_qualifiziert=rang_und_einrede_qualifiziert,
        bewertungsnachweis=bewertungsnachweis)
    wert = None
    if rang_und_einrede_qualifiziert:
        frei = max(_subtrahieren(masse, bindung), _bruch(0))
        gedeckt = min(frei, forderung)
        wert = dict(freie_haftungsmasse=_bruchteile(frei), gedeckter_forderungsteil=_bruchteile(gedeckt),
            nicht_gedeckter_forderungsteil=_bruchteile(_subtrahieren(forderung, gedeckt)))
    return _haftungsrest_ergebnis(wert, 'BGB_NACHLASSGLAEUBIGER_RESTDECKUNG', eingaben,
        'Positive Haftungsmasse nach vorrangigen Bindungen bestimmen; einzelne Forderung darauf begrenzen, ungedeckten Rest getrennt',
        '1973: Nichtausgeschlossene grundsätzlich vorab; Pflichtteils-/Vermächtnis-/Auflagenlasten grundsätzlich nachrangig, außer schon vor Geltendmachung berichtigt.1974II: unter diesen besonderen Lastarten nur Vorrang entsprechend Nachlassinsolvenz; Rang muss ausdrücklich vorqualifiziert sein.1990 erfordert besondere Dürftigkeitseinrede,1992 einschlägige Vermächtnis-/Auflagenüberschuldung;1991IV-Insolvenzrang berücksichtigen. Bereicherungsrechtlich maßgebliche Haftungsmasse1973II und Verantwortlichkeitskorrekturen1991 vorher bewerten. Bereits befriedigte oder gleichstehend rechtskräftig zuerkannte Beträge1973II3/1991III können Bindungen sein, nicht doppelt von bereits bereinigter Masse abziehen. Keine automatische Gleichrangquote; bei konkurrierenden gleichrangigen Forderungen verfügbare Masse/Bindungen rechtlich zuordnen. Ungedeckte Forderung erlischt nicht, Sachherausgabe nicht pauschal in Geldpflicht umwandeln.')


def nacherbe_haftungsmasse(erlangter_erbschaftswert_ohne_vorerbenansprueche=None, anspruchswert_gegen_vorerben=None,
    bewertungsnachweis=None):
    """§2144I: erlangten Erbschaftswert und darin noch nicht enthaltene Ansprüche gegen Vorerben addieren."""
    erlangt = _geld(erlangter_erbschaftswert_ohne_vorerbenansprueche)
    ansprueche = _geld(anspruchswert_gegen_vorerben)
    _text(bewertungsnachweis, 'bewertungsnachweis')
    eingaben = dict(erlangter_erbschaftswert_ohne_vorerbenansprueche=erlangter_erbschaftswert_ohne_vorerbenansprueche,
        anspruchswert_gegen_vorerben=anspruchswert_gegen_vorerben, bewertungsnachweis=bewertungsnachweis)
    return _haftungsrest_ergebnis(_bruchteile(_addieren(erlangt, ansprueche)), 'BGB_NACHERBE_HAFTUNGSMASSE', eingaben,
        'Erlangten Erbschaftswert und überschneidungsfrei bewertete Ansprüche gegen Vorerben summieren',
        'Nur numerische Masse2144I; Ansprüche gegen Vorerben als solchen rechtlich und wirtschaftlich bewerten. Keine doppelte Erfassung bereits erfüllter Ansprüche als erhaltene Gegenstände und offene Forderungen. Kein automatischer Haftungsdeckel für jede Schuld: Voraussetzungen der Haftungsbeschränkung sowie Rang-/Kostenbindungen separat. Inventarwirkung2144II und Sonderverhältnis2144III sind rechtliche Voraussetzungen, keine zusätzliche Rechnung.')


def vorerbe_verbleibende_haftung(nachlassschuld=None, rechtlich_vom_nacherben_getragener_schuldteil=None,
    schuld_im_innenverhaeltnis_vorerbe=None, vorerbe_unbeschraenkt_haftend=None,
    fuer_forderung_verfuegbare_vorerbenmasse=None, nacherbfall_qualifiziert=None, bewertungsnachweis=None):
    """§2145: rechtliche Resthaftung/Innenlast bestimmen und gegebenenfalls auf verfügbare Vorerbenmasse begrenzen."""
    schuld = _geld(nachlassschuld)
    nacherbe = _geld(rechtlich_vom_nacherben_getragener_schuldteil)
    masse = _geld(fuer_forderung_verfuegbare_vorerbenmasse)
    if nacherbe > schuld:
        _fehler('rechtlich_vom_nacherben_getragener_schuldteil', 'Rechtlicher Nacherbenhaftungsteil darf Gesamtforderung nicht übersteigen.')
    _wahrheitswert(schuld_im_innenverhaeltnis_vorerbe, 'schuld_im_innenverhaeltnis_vorerbe')
    _wahrheitswert(vorerbe_unbeschraenkt_haftend, 'vorerbe_unbeschraenkt_haftend')
    _wahrheitswert(nacherbfall_qualifiziert, 'nacherbfall_qualifiziert')
    _text(bewertungsnachweis, 'bewertungsnachweis')
    eingaben = dict(nachlassschuld=nachlassschuld, rechtlich_vom_nacherben_getragener_schuldteil=rechtlich_vom_nacherben_getragener_schuldteil,
        schuld_im_innenverhaeltnis_vorerbe=schuld_im_innenverhaeltnis_vorerbe, vorerbe_unbeschraenkt_haftend=vorerbe_unbeschraenkt_haftend,
        fuer_forderung_verfuegbare_vorerbenmasse=fuer_forderung_verfuegbare_vorerbenmasse, nacherbfall_qualifiziert=nacherbfall_qualifiziert,
        bewertungsnachweis=bewertungsnachweis)
    wert = None
    if nacherbfall_qualifiziert:
        resthaftung = schuld if schuld_im_innenverhaeltnis_vorerbe else _subtrahieren(schuld, nacherbe)
        deckung = resthaftung if vorerbe_unbeschraenkt_haftend else min(resthaftung, masse)
        wert = dict(verbleibende_haftung_vor_massenbegrenzung=_bruchteile(resthaftung), befriedigungsbetrag_nach_massenbegrenzung=_bruchteile(deckung),
            wegen_massenbegrenzung_nicht_gedeckter_teil=_bruchteile(_subtrahieren(resthaftung, deckung)))
    return _haftungsrest_ergebnis(wert, 'BGB_VORERBE_VERBLEIBENDE_HAFTUNG', eingaben,
        'Ohne eigene Innenlast rechtlich vom Nacherben getragenen Teil abziehen; bei eigener Innenlast volle Schuld; beschränkte Vorerbenhaftung auf zugeordnete Masse begrenzen',
        'Nach Eintritt Nacherbfolge2145. Maßgeblich ist rechtliche Haftung des Nacherben, nicht dessen Zahlungsfähigkeit oder bisherige Zahlung. Innenlast betrifft gesamte hier eingegebene Forderung; gemischte Innenlasten vorher überschneidungsfrei aufteilen. Rechtliche Resthaftung bei eigener Innenlast nicht doppelt addieren. Verfügbare Vorerbenmasse ist der ihm von Erbschaft gebührende, dieser Forderung nach Rang/Bindungen tatsächlich zugeordnete Wert;1990/1991 entsprechend berücksichtigen. Unbeschränkte Haftung wird nicht auf diese Masse gekappt. Keine beliebige eigene Vermögenssumme und kein automatisches Erlöschen ungedeckter Forderung.')
