"""Nettowertquoten einer gemeinschaftlichen Gesamthypothek nach§1172."""
from .betraege import _geld
from .kalender import _ergebnis, _fehler, _text, _vorhanden
from .zahlen import _addieren, _bruch, _dividieren, _multiplizieren, _zahleneingabe, _subtrahieren
from .zinsen import _bruchteile


def gesamthypothek_wertanteile(zu_verteilender_hypothekenbetrag=None, grundstuecke=None, verteilungsnachweis=None):
    """§1172II: Gesamthypothekenbetrag nach qualifizierten Nettogrundstückswerten verteilen."""
    bedarf = _geld(zu_verteilender_hypothekenbetrag)
    _vorhanden(grundstuecke, 'grundstuecke')
    if not isinstance(grundstuecke,list) or not 1 <= len(grundstuecke) <= 1000:
        _fehler('grundstuecke','Liste mit 1 bis 1000 qualifizierten belasteten Grundstücken erforderlich.')
    namen,gewichte = [],[]
    summe = _bruch(0)
    for eintrag in grundstuecke:
        if not isinstance(eintrag,dict) or set(eintrag) != {'grundstueck_id','grundstueckswert','vorrangige_belastungen'}:
            _fehler('grundstuecke','Genau grundstueck_id, grundstueckswert und vorrangige_belastungen erforderlich.')
        name = _text(eintrag['grundstueck_id'],'grundstueck_id')
        if name in namen:
            _fehler('grundstueck_id','Grundstücksteil nicht mehrfach aufführen.')
        _vorhanden(eintrag['grundstueckswert'],'grundstueckswert')
        gewicht = _subtrahieren(_geld(eintrag['grundstueckswert']), _geld(eintrag['vorrangige_belastungen']))
        if gewicht < 0:
            _fehler('grundstueckswert','Dieser Grundfall setzt einen nichtnegativen Nettogrundstückswert voraus.')
        namen.append(name);gewichte.append(gewicht);summe = _addieren(summe,gewicht)
    if summe == 0:
        _fehler('grundstuecke','Positive Summe der Nettogrundstückswerte erforderlich.')
    _text(verteilungsnachweis,'verteilungsnachweis')
    anteile=[]
    for name,gewicht in zip(namen,gewichte):
        quote = _dividieren(gewicht,summe)
        anteile.append(dict(grundstueck_id=name,anteilsquote=_bruchteile(quote),hypothekenanteil=_bruchteile(_multiplizieren(bedarf,quote))))
    eingaben = dict(zu_verteilender_hypothekenbetrag=zu_verteilender_hypothekenbetrag,grundstuecke=grundstuecke,verteilungsnachweis=verteilungsnachweis)
    ergebnis = _ergebnis(anteile,'EUR','BGB_GESAMTHYPOTHEK_WERTANTEILE',eingaben,[dict(operation='Vorranglasten vom Grundstückswert abziehen, positive Nettowertsumme bilden und Hypothekenbetrag nach Nettowerten verteilen.')],eingaben.copy())
    ergebnis['hinweise'] = ['Grundfall§1172Absatz2, ebenso§1175: keine abweichende Vereinbarung; alle gemeinschaftlich berechtigten belasteten Grundstücke vollständig erfassen. Maßgebliche Werte und vorrangige Belastungen rechtlich bewertet, keine bloßen Nominalbeträge ohne Zuordnung. Diese Grundrechnung setzt nichtnegative Nettowerte und positive Nettowertsumme voraus; Überbelastung und ausschließlich wertlose Grundstücke benötigen gesonderte rechtliche Behandlung. Teilübergang mit Schuldnerregress§1174, Konkurrenz§1176 und bestehende Gläubigervorränge nicht durch diese Quotenrechnung entschieden.']
    return ergebnis
