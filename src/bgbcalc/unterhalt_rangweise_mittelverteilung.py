from .kalender import _ergebnis, _text, _vorhanden, _fehler, _ganzzahl
from .betraege import _geld
from .zahlen import _bruch, _subtrahieren
from .zinsen import _bruchteile
from .quotenverteilung import _begrenzte_quotenverteilung

def unterhalt_rangweise_mittelverteilung(verfuegbare_mittel=None, berechtigte=None, verteilungsnachweis=None):
    """Verfuegbare Mittel nach1609Raengen, innerhalb jedes Rangs nach qualifizierten Gewichten unter Bedarfsgrenzen verteilen und ungedeckten Rest ausweisen."""
    mittel=_geld(verfuegbare_mittel);_text(verteilungsnachweis,'verteilungsnachweis');_vorhanden(berechtigte,'berechtigte')
    if not isinstance(berechtigte,list) or not 1<=len(berechtigte)<=1000: _fehler('berechtigte','Nichtleere begrenzte Liste erforderlich.')
    personen=[];raenge=[];grade=[];gewichte=[];bedarfe=[]
    for p in berechtigte:
        if not isinstance(p,dict) or set(p)!={'person_id','rang1609','verwandtschaftsgrad','ungedeckter_bedarf','verteilungsgewicht'}: _fehler('berechtigte','Genau Kennung, Rang, Bedarf und Gewicht erforderlich.')
        k=_text(p['person_id'],'person_id');r=_ganzzahl(p['rang1609'],'rang1609',1,7);g=_geld(p['verteilungsgewicht']);b=_geld(p['ungedeckter_bedarf'])
        if k in personen or g<=0: _fehler('berechtigte','Eindeutige Kennung und positives Gewicht erforderlich.')
        grad=_ganzzahl(p['verwandtschaftsgrad'],'verwandtschaftsgrad',2,1000) if r==7 else 0
        if r!=7 and p['verwandtschaftsgrad'] is not None: _fehler('verwandtschaftsgrad','Nur Rang7verwendet einen Naehegrad.')
        personen.append(k);raenge.append(r);grade.append(grad);gewichte.append(g);bedarfe.append(b)
    rest=mittel;zuordnung=[_bruch(0) for _ in personen]
    for rang,grad in sorted(set(zip(raenge,grade))):
        indices=[i for i,r in enumerate(raenge) if r==rang and grade[i]==grad]
        werte,rest=_begrenzte_quotenverteilung(rest,[gewichte[i] for i in indices],[bedarfe[i] for i in indices])
        for i,z in zip(indices,werte): zuordnung[i]=z
    wert=dict(verteilung=[dict(person_id=k,rang1609=r,verwandtschaftsgrad=g if r==7 else None,zugeordneter_unterhalt=_bruchteile(z),ungedeckter_restbedarf=_bruchteile(_subtrahieren(b,z))) for k,r,g,b,z in zip(personen,raenge,grade,bedarfe,zuordnung)],gesamt_zugeordnet=_bruchteile(_subtrahieren(mittel,rest)),verbleibende_mittel=_bruchteile(rest))
    eingaben = dict(verfuegbare_mittel=verfuegbare_mittel, berechtigte=berechtigte, verteilungsnachweis=verteilungsnachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_UNTERHALT_RANGWEISE_MITTELVERTEILUNG',eingaben,[dict(operation='Verfuegbare Mittel nach1609Raengen, innerhalb jedes Rangs nach qualifizierten Gewichten unter Bedarfsgrenzen verteilen und ungedeckten Rest ausweisen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§§1603/1609: qualifizierte verfuegbare Mittel rangweise verwenden. Rang1vor2usw.; innerhalb Rang7gehen naehere Verwandtschaftsgrade den ferneren vor. Innerhalb eines Rangs nach rechtlich begruendeten Gewichten proportional unter individuellen ungedeckten Bedarfsgrenzen mit vorhandenem begrenztem Quotenkern verteilen. Erst danach Restmittel an naechsten Rang. Keine Gleichverteilung nach Koepfen und keine erfundene Unterhaltstabelle/Selbstbehaltshoehe.1603IIgesteigerte Haftung bestimmt rechtlich verfuegbare Mittel und qualifizierte Mangelfallgewichte, kein vom BGB vorgegebener weiterer pauschaler Prozentsatz. Gewichte und Grenzen muessen fuer die gesamte jeweilige Rangverteilung gelten; rechtliche Neubewertung bei geaenderter Grundlage explizit erforderlich. Mehrere Pflichtige1606IIIund Ersatzhaftung1607/1608mit bestehenden Anteils-/Leistungsgrenzenkernen in rechtlich bestimmter Reihenfolge komponieren; keine automatische globale Familienmatrix oder Umdeutung eines ungedeckten Bedarfs in Anspruch gegen beliebige Dritte. Bereits anderweitig gedeckte Bedarfe/gebundene Mittel nicht doppelt verwenden. Keine automatische Bestimmung von Berechtigung, Rang, Leistungsfaehigkeit, Naturalleistung oder Tabellenbetrag.']
    return ergebnis

