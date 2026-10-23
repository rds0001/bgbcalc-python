from .betraege import _geld
from .kalender import _ergebnis, _fehler, _text, _vorhanden
from .zahlen import _addieren, _bruch, _dividieren, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile
from .quotenverteilung import _begrenzte_quotenverteilung

def unterhalt_anteile_mit_leistungsgrenzen(verteilbarer_barunterhalt=None, unterhaltspflichtige=None, verteilungsnachweis=None):
    """Qualifizierten Barunterhalt mit vorhandenem begrenztem Quotenkern nach Gewichten unter individuellen Leistungsgrenzen verteilen und ungedeckten Rest ausweisen."""
    bedarf=_geld(verteilbarer_barunterhalt);_text(verteilungsnachweis,'verteilungsnachweis');_vorhanden(unterhaltspflichtige,'unterhaltspflichtige')
    if not isinstance(unterhaltspflichtige,list) or not 1<=len(unterhaltspflichtige)<=1000:
        _fehler('unterhaltspflichtige','Liste1..1000 qualifizierter gleich naher Pflichtiger erforderlich.')
    namen=[];gewichte=[];grenzen=[];summe=_bruch(0)
    for person in unterhaltspflichtige:
        if not isinstance(person,dict) or set(person)!={'person_id','verteilungsgewicht','leistungsfaehiger_hoechstbetrag'}:
            _fehler('unterhaltspflichtige','Genau person_id, verteilungsgewicht und leistungsfaehiger_hoechstbetrag erforderlich.')
        name=_text(person['person_id'],'person_id');gewicht=_geld(person['verteilungsgewicht'])
        if name in namen or gewicht<=0:
            _fehler('unterhaltspflichtige','Eindeutige Kennungen und positive qualifizierte Gewichte erforderlich.')
        namen.append(name);gewichte.append(gewicht);grenzen.append(_geld(person['leistungsfaehiger_hoechstbetrag']));summe=_addieren(summe,gewicht)
    zugeordnet,rest=_begrenzte_quotenverteilung(bedarf,gewichte,grenzen)
    wert=dict(verteilung=[dict(person_id=name,ungekuerzter_anteil=_bruchteile(_multiplizieren(bedarf,_dividieren(g,summe))),beibringbarer_unterhaltsbetrag=_bruchteile(a)) for name,g,a in zip(namen,gewichte,zugeordnet)],gesamt_beibringbar=_bruchteile(_subtrahieren(bedarf,rest)),ungedeckter_barunterhalt=_bruchteile(rest))
    eingaben = dict(verteilbarer_barunterhalt=verteilbarer_barunterhalt, unterhaltspflichtige=unterhaltspflichtige, verteilungsnachweis=verteilungsnachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_UNTERHALT_ANTEILE_MIT_LEISTUNGSGRENZEN',eingaben,[dict(operation='Qualifizierten Barunterhalt mit vorhandenem begrenztem Quotenkern nach Gewichten unter individuellen Leistungsgrenzen verteilen und ungedeckten Rest ausweisen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§1606III1 mit rechtlich bestimmten1603-Leistungsgrenzen: proportionaler Barunterhaltsanteil für einen Berechtigten; bei Begrenzung verbleibenden Bedarf im ausdrücklich qualifizierten Modell nach relativen Gewichten der übrigen Pflichtigen nachverteilen. Keine automatisch vorausgesetzte einheitliche Methode für sämtliche Unterhalts-Mangelfälle. Eingaben enthalten bereits passende Selbstbehalte, Belastungen, Rang- und Bewertungsentscheidungen; keine Tabelle oder Einkommensbereinigung erfinden. Gewichte/Grenzen müssen für diesen Bedarf und sämtliche Nachverteilungsschritte rechtlich gelten. Ändert sich dadurch die rechtliche Berechnungsbasis, ist diese außerhalb neu zu bestimmen. Mehrere Berechtigte, konkurrierende1609-Ränge, gesteigerte1603II-Gesamtmittelaufteilung, Wechselmodell, Naturalunterhalt und subsidiäre1607-Haftung nicht automatisch kombiniert. Ergebnis ungedeckter Bedarf ist kein Erlass oder automatischer Anspruch gegen weitere Personen. Keine Cent-Rundung.']
    return ergebnis

