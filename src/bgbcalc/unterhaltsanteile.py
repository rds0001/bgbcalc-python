"""Proportionale Barunterhaltsgrundverteilung bei gleich nahen Verwandten."""
from .betraege import _geld
from .kalender import _ergebnis, _fehler, _text, _vorhanden
from .zahlen import _addieren, _bruch, _dividieren, _multiplizieren, _zahleneingabe
from .zinsen import _bruchteile


def unterhalt_anteilsbetraege(verteilbarer_barunterhalt=None, unterhaltspflichtige=None, verteilungsnachweis=None):
    """§1606III1: qualifizierten Barunterhaltsbetrag nach Erwerbs-/Vermögensgewichten verteilen."""
    bedarf = _geld(verteilbarer_barunterhalt)
    _vorhanden(unterhaltspflichtige, 'unterhaltspflichtige')
    if not isinstance(unterhaltspflichtige,list) or not 1 <= len(unterhaltspflichtige) <= 1000:
        _fehler('unterhaltspflichtige','Liste mit 1 bis 1000 qualifizierten gleich nahen Barunterhaltspflichtigen erforderlich.')
    namen,gewichte = [],[]
    summe = _bruch(0)
    for eintrag in unterhaltspflichtige:
        if not isinstance(eintrag,dict) or set(eintrag) != {'person_id','verteilungsgewicht'}:
            _fehler('unterhaltspflichtige','Genau person_id und verteilungsgewicht erforderlich.')
        name = _text(eintrag['person_id'],'person_id')
        if name in namen:
            _fehler('person_id','Unterhaltspflichtige Person nicht mehrfach aufführen.')
        _vorhanden(eintrag['verteilungsgewicht'],'verteilungsgewicht')
        gewicht = _zahleneingabe(eintrag['verteilungsgewicht'])
        if gewicht <= 0:
            _fehler('verteilungsgewicht','Positives rechtlich bewertetes Verteilungsgewicht erforderlich.')
        namen.append(name);gewichte.append(gewicht);summe = _addieren(summe,gewicht)
    _text(verteilungsnachweis,'verteilungsnachweis')
    anteile=[]
    for name,gewicht in zip(namen,gewichte):
        quote = _dividieren(gewicht,summe)
        anteile.append(dict(person_id=name,anteilsquote=_bruchteile(quote),unterhaltsbetrag=_bruchteile(_multiplizieren(bedarf,quote))))
    eingaben = dict(verteilbarer_barunterhalt=verteilbarer_barunterhalt,unterhaltspflichtige=unterhaltspflichtige,verteilungsnachweis=verteilungsnachweis)
    ergebnis = _ergebnis(anteile,'EUR','BGB_UNTERHALT_ANTEILSBETRAEGE',eingaben,[dict(operation='Qualifizierte Erwerbs-/Vermögensgewichte summieren, jedes Gewicht durch die Summe teilen und Barunterhalt damit multiplizieren.')],eingaben.copy())
    ergebnis['hinweise'] = ['Grundverteilung nach§1606III1 für denselben Zeitraum und denselben qualifizierten Barunterhaltsbedarf. Kreis der tatsächlich gleich nahen barunterhaltspflichtigen Verwandten sowie Rang, Erwerbs-/Vermögensbewertung und Verteilungsgewichte rechtlich vorqualifiziert. Gewichte sind keine ungeprüften Bruttoeinkommen und nicht notwendig normierte Quoten. Keine Ermittlung von Selbstbehalt, gesteigerter Haftung, Bedarfsrang, Wechselmodell oder Naturalunterhalt nachSatz2. Nur wenn individuelle Leistungsfähigkeitsgrenzen bei den errechneten Anteilen nicht eingreifen; Mangelfall-/Deckelungsumverteilung gesondert. Nichtpflichtige oder mit Gewicht null ausgeschiedene Personen außerhalb dieses qualifizierten Kreises behandeln.']
    return ergebnis
