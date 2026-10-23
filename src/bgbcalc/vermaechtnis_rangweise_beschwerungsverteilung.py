from .kalender import _ergebnis, _text, _vorhanden, _fehler, _ganzzahl
from .betraege import _geld
from .zahlen import _bruch, _subtrahieren
from .zinsen import _bruchteile
from .quotenverteilung import _begrenzte_quotenverteilung

def vermaechtnis_rangweise_beschwerungsverteilung(verfuegbarer_beschwerungsbetrag=None, beschwerungen=None, verteilungsnachweis=None):
    """Gemeinsames Kürzungsbudget rangweise, innerhalb eines Rangs proportional und anspruchsbegrenzt verteilen."""
    rest=_geld(verfuegbarer_beschwerungsbetrag);_text(verteilungsnachweis,'verteilungsnachweis');_vorhanden(beschwerungen,'beschwerungen')
    if not isinstance(beschwerungen,list) or not 1<=len(beschwerungen)<=1000:_fehler('beschwerungen','Liste1..1000erforderlich.')
    namen=[];raenge=[];werte=[];gewichte=[]
    for p in beschwerungen:
        if not isinstance(p,dict) or set(p)!={'beschwerung_id','rang','beschwerungswert','verteilungsgewicht'}:_fehler('beschwerungen','Genau Kennung,Rang,Wert und Gewicht erforderlich.')
        name=_text(p['beschwerung_id'],'beschwerung_id');rang=_ganzzahl(p['rang'],'rang',1,1000);wert=_geld(p['beschwerungswert']);gewicht=_geld(p['verteilungsgewicht'])
        if name in namen or gewicht<=0:_fehler('beschwerungen','Eindeutige Kennungen und positive Gewichte erforderlich.')
        namen.append(name);raenge.append(rang);werte.append(wert);gewichte.append(gewicht)
    zuordnung=[_bruch(0) for _ in namen]
    for rang in sorted(set(raenge)):
        indices=[i for i,r in enumerate(raenge) if r==rang];anteile,rest=_begrenzte_quotenverteilung(rest,[gewichte[i] for i in indices],[werte[i] for i in indices])
        for i,z in zip(indices,anteile):zuordnung[i]=z
    wert=dict(verteilung=[dict(beschwerung_id=k,zugeteilter_betrag=_bruchteile(z),kuerzungsbetrag=_bruchteile(_subtrahieren(v,z))) for k,v,z in zip(namen,werte,zuordnung)],verbleibendes_budget=_bruchteile(rest))
    eingaben = dict(verfuegbarer_beschwerungsbetrag=verfuegbarer_beschwerungsbetrag, beschwerungen=beschwerungen, verteilungsnachweis=verteilungsnachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_VERMAECHTNIS_RANGWEISE_BESCHWERUNGSVERTEILUNG',eingaben,[dict(operation='Gemeinsames Kürzungsbudget rangweise, innerhalb eines Rangs proportional und anspruchsbegrenzt verteilen.')],eingaben.copy())
    ergebnis["hinweise"] = ['Mehrere rechtlich feststehende Beschwerungsränge mit bestehendem begrenztem Quotenkern bedienen. Innerhalb eines Rangs proportional zu qualifizierten Gewichten, höchstens jeweiliger Beschwerungswert, über Obergrenzen hinausgehende Anteile innerhalb desselben Rangs neu verteilen. Restbudget erst danach an nachrangige Ränge. Keine automatische Testamentsauslegung, automatische Gleichrangigkeit oder Erfindung von Quoten. Individuelle2318II/III-Schutzkonkurrenz muss bereits rechtlich in Budget/zulässiger Rangverteilung berücksichtigt sein; dieser Kern entscheidet sie nicht. Kürzungsrecht muss ausgeübt werden, keine automatische Schuldtilgung. Keine mehrfache Verwendung desselben Budgets oder Umdeutung von Sachvermächtnissen in Zahlungsansprüche.']
    return ergebnis

