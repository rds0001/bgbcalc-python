from .kalender import _ergebnis, _text, _auswahl, _vorhanden, _fehler
from .betraege import _geld
from .zahlen import _bruch, _addieren, _subtrahieren
from .zinsen import _bruchteile
from .gesamthypothekanteile import gesamthypothek_wertanteile

def gesamthypothek_nichtnegative_nettowertanteile(zu_verteilender_hypothekenbetrag=None, grundstuecke=None, gewichtsmethode=None, verteilungsnachweis=None):
    """Rohnettowerte und nichtnegative qualifizierte Gewichte bestimmen; vorhandenen Quotenkern nur bei positiver Gewichtssumme anwenden."""
    _geld(zu_verteilender_hypothekenbetrag);_text(verteilungsnachweis,'verteilungsnachweis');_auswahl(gewichtsmethode,'gewichtsmethode',('positive_nettowerte',));_vorhanden(grundstuecke,'grundstuecke')
    if not isinstance(grundstuecke,list) or not 1<=len(grundstuecke)<=1000:_fehler('grundstuecke','Liste1..1000erforderlich.')
    namen=set();netto=[];vorbereitet=[];summe=_bruch(0)
    for p in grundstuecke:
        if not isinstance(p,dict) or set(p)!={'grundstueck_id','grundstueckswert','vorrangige_belastungen'}:_fehler('grundstuecke','Genau Kennung,Wert und Vorranglasten erforderlich.')
        name=_text(p['grundstueck_id'],'grundstueck_id');roh=_subtrahieren(_geld(p['grundstueckswert']),_geld(p['vorrangige_belastungen']));g=max(roh,_bruch(0))
        if name in namen:_fehler('grundstueck_id','JedesGrundstücknurEinmal.')
        namen.add(name);summe=_addieren(summe,g);netto.append(dict(grundstueck_id=name,roher_nettowert=_bruchteile(roh),verteilungsgewicht=_bruchteile(g)));vorbereitet.append(dict(grundstueck_id=name,grundstueckswert=_bruchteile(g),vorrangige_belastungen='0'))
    anteile=gesamthypothek_wertanteile(zu_verteilender_hypothekenbetrag,vorbereitet,verteilungsnachweis)['wert'] if summe>0 else None
    wert=dict(nettowerte=netto,quoten_bestimmbar=summe>0,anteile=anteile)
    eingaben = dict(zu_verteilender_hypothekenbetrag=zu_verteilender_hypothekenbetrag, grundstuecke=grundstuecke, gewichtsmethode=gewichtsmethode, verteilungsnachweis=verteilungsnachweis)
    ergebnis = _ergebnis(wert,'EUR_und_Quoten','BGB_GESAMTHYPOTHEK_NICHTNEGATIVE_NETTOWERTANTEILE',eingaben,[dict(operation='Rohnettowerte und nichtnegative qualifizierte Gewichte bestimmen; vorhandenen Quotenkern nur bei positiver Gewichtssumme anwenden.')],eingaben.copy())
    ergebnis["hinweise"] = ['Bedingte Nettowertrechnung: ursprünglichen Wert minus qualifizierte vorrangige Belastungen ausweisen; unter ausdrücklich vorgegebener Methode positive_nettowerte Verteilungsgewicht=max(Rohsaldo,0). Bestehenden1172-Quotenkern mit diesen abgeleiteten Gewichten verwenden, Vorrang nicht doppelt abziehen. Bei Gewichtssumme0keine Division/keine künstliche Kopfquote: quoten_bestimmbar=false, anteile=None/NULL; die Rohsalden bleiben ausgewiesen. Gesetzliche Vorschrift liefert für0/0keine feste Ersatzquote. Keine automatische Bewertung der Vorranglast, Verwertung oder rechtliche Freigabe des Nullgewichtsmodells in jedem Streitfall.1174-Regress und1176/1182-Rangschutz gesondert.']
    return ergebnis

