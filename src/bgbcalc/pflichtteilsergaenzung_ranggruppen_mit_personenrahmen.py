from .kalender import _ergebnis, _text, _vorhanden, _fehler, _auswahl, _ganzzahl
from .betraege import _geld
from .zahlen import _bruch, _subtrahieren
from .zinsen import _bruchteile
from .quotenverteilung import _begrenzte_quotenverteilung

def pflichtteilsergaenzung_ranggruppen_mit_personenrahmen(fehlbetrag=None, schenkungsgruppen=None, personenrahmen=None, kuerzungsmethode=None, methodennachweis=None):
    """Chronologische Gruppen mit gleichzeitig wertproportionaler Verteilung und ausdrücklich qualifizierter Kappungsmethode unter einmaligen Personenrahmen abarbeiten."""
    rest=_geld(fehlbetrag);_text(methodennachweis,'methodennachweis');_auswahl(kuerzungsmethode,'kuerzungsmethode',('anteilige_kuerzung_ohne_umverteilung','begrenzte_umverteilung'))
    for name,liste in (('schenkungsgruppen',schenkungsgruppen),('personenrahmen',personenrahmen)):
        _vorhanden(liste,name)
        if not isinstance(liste,list) or not 1<=len(liste)<=1000:_fehler(name,'Liste1..1000erforderlich.')
    rahmen={}
    for p in personenrahmen:
        if not isinstance(p,dict) or set(p)!={'beschenkter_id','gemeinsame_haftungsgrenze'}:_fehler('personenrahmen','Kennung und Grenze erforderlich.')
        name=_text(p['beschenkter_id'],'beschenkter_id')
        if name in rahmen:_fehler('personenrahmen','Personenrahmen nur einmal.')
        rahmen[name]=_geld(p['gemeinsame_haftungsgrenze'])
    gruppen=[];gesehen=set()
    for p in schenkungsgruppen:
        if not isinstance(p,dict) or set(p)!={'beschenkter_id','schenkungsrang','schenkungswert','einzelhaftungsgrenze'}:_fehler('schenkungsgruppen','Vier Gruppenfelder erforderlich.')
        name=_text(p['beschenkter_id'],'beschenkter_id');rang=_ganzzahl(p['schenkungsrang'],'schenkungsrang',1,1000);gewicht=_geld(p['schenkungswert']);grenze=_geld(p['einzelhaftungsgrenze'])
        if (name,rang) in gesehen:_fehler('schenkungsgruppen','Genau eine Gruppe je Person und Rang.')
        gesehen.add((name,rang));gruppen.append((name,rang,gewicht,grenze))
    if {g[0] for g in gruppen}!=set(rahmen):_fehler('personenrahmen','Genau alle Gruppenempfänger erforderlich.')
    zugeordnet=[_bruch(0) for _ in gruppen]
    for rang in sorted({g[1] for g in gruppen},reverse=True):
        ind=[i for i,g in enumerate(gruppen) if g[1]==rang];gewichte=[gruppen[i][2] for i in ind];grenzen=[min(gruppen[i][3],gruppen[i][2],rahmen[gruppen[i][0]]) for i in ind]
        if kuerzungsmethode=='begrenzte_umverteilung':anteile,_=_begrenzte_quotenverteilung(rest,gewichte,grenzen)
        else:
            basis,_=_begrenzte_quotenverteilung(rest,gewichte,gewichte);anteile=[min(x,g) for x,g in zip(basis,grenzen)]
        for i,x in zip(ind,anteile):zugeordnet[i]=x;rest=_subtrahieren(rest,x);rahmen[gruppen[i][0]]=_subtrahieren(rahmen[gruppen[i][0]],x)
    wert=dict(gruppenanteile=[dict(beschenkter_id=g[0],schenkungsrang=g[1],rechnerischer_haftungsanteil=_bruchteile(x)) for g,x in zip(gruppen,zugeordnet)],personenrahmen_rest=[dict(beschenkter_id=p['beschenkter_id'],verbleibender_rahmen=_bruchteile(rahmen[p['beschenkter_id']])) for p in personenrahmen],nicht_gedeckter_fehlbetrag=_bruchteile(rest))
    eingaben = dict(fehlbetrag=fehlbetrag, schenkungsgruppen=schenkungsgruppen, personenrahmen=personenrahmen, kuerzungsmethode=kuerzungsmethode, methodennachweis=methodennachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_PFLICHTTEILSERGAENZUNG_RANGGRUPPEN_MIT_PERSONENRAHMEN',eingaben,[dict(operation='Chronologische Gruppen mit gleichzeitig wertproportionaler Verteilung und ausdrücklich qualifizierter Kappungsmethode unter einmaligen Personenrahmen abarbeiten.')],eingaben.copy())
    ergebnis["hinweise"] = ['Bedingte arithmetische2329III-Komposition: spätere Gruppen zuerst; gleichzeitig nach Schenkungswerten. Individuelle Kapazität=min(Gruppengrenze,Schenkungswert,noch unverbrauchter Personenrahmen). Bei anteilige_kuerzung_ohne_umverteilung erst Wertquote am kleineren Betrag aus Restfehlbetrag/Gesamtgruppenwert und danach persönliche Kappung; bei begrenzte_umverteilung proportional mit Kappung und Neuverteilung auf übrige Gruppenmitglieder. Nur tatsächlich zugeordnete Beträge verbrauchen den gemeinsamen Personenrahmen; rechtlich nicht gedeckter Rest geht zum früheren Rang. Kein doppelter Personenrahmen über mehrere Ränge. Die beiden Methoden sind ausdrücklich bedingte Rechenmodelle, keine Behauptung, dass beide gesetzlich zulässig sind. Rechtsfrage zusätzlicher Kürzungen bei Gleichzeitigkeit bleibt vom Anwender anhand seines Falls zu entscheiden; bloße Insolvenz macht spätere Verpflichtung nicht automatisch unwirksam. Keine gewöhnliche Geldhaftung statt qualifizierter Sachherausgabe unterstellen.']
    return ergebnis

