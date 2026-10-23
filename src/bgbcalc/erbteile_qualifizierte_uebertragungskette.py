from .kalender import _ergebnis, _text, _vorhanden, _fehler
from .betraege import _geld
from .zahlen import _bruch, _addieren, _subtrahieren, _multiplizieren, _dividieren
from .zinsen import _bruchteile

def erbteile_qualifizierte_uebertragungskette(erben_ids=None, ursprungsanteile=None, uebertragungsschritte=None, einordnungsnachweis=None):
    """Qualifizierte Anteilstransfers chronologisch exakt verteilen, Restanteile fortschreiben und Sonderteile nach Urspruengen erhalten."""
    _text(einordnungsnachweis,'einordnungsnachweis')
    for x,name,minimum in [(erben_ids,'erben_ids',1),(ursprungsanteile,'ursprungsanteile',1),(uebertragungsschritte,'uebertragungsschritte',0)]:
        _vorhanden(x,name)
        if not isinstance(x,list) or not minimum<=len(x)<=1000: _fehler(name,'Begrenzte Liste erforderlich.')
    personen=[_text(x,'erbe_id') for x in erben_ids]
    if len(set(personen))!=len(personen): _fehler('erben_ids','Doppelte Kennung.')
    urspruenge=[];bestand={};gesamt=_bruch(0)
    for a in ursprungsanteile:
        if not isinstance(a,dict) or set(a)!={'ursprung_id','erbe_id','erbquote'}: _fehler('ursprungsanteile','Genau Ursprung, Erbe und Quote erforderlich.')
        u=_text(a['ursprung_id'],'ursprung_id');e=_text(a['erbe_id'],'erbe_id');q=_geld(a['erbquote'])
        if e not in personen or (u,e) in bestand or not 0<q<=1: _fehler('ursprungsanteile','Bekannter Erbe, eindeutiges Ursprung-Erbe-Paar, positive Quote bis1erforderlich.')
        if u not in urspruenge: urspruenge.append(u)
        bestand[u,e]=q;gesamt=_addieren(gesamt,q)
    if gesamt>1: _fehler('ursprungsanteile','Gesamtquote darf1nicht uebersteigen.')
    for s in uebertragungsschritte:
        if not isinstance(s,dict) or set(s)!={'abgebender_erbe_id','ursprung_ids','uebertragungsquote','empfaenger'}: _fehler('uebertragungsschritte','Genau Abgebender, Urspruenge, Uebertragungsquote und Empfaenger erforderlich.')
        v=_text(s['abgebender_erbe_id'],'abgebender_erbe_id');us=s['ursprung_ids'];emp=s['empfaenger'];q=_geld(s['uebertragungsquote'])
        if v not in personen or not 0<q<=1 or not isinstance(us,list) or not 1<=len(us)<=1000 or not isinstance(emp,list) or not 1<=len(emp)<=1000: _fehler('uebertragungsschritte','Gueltige Person, positive Quote bis1und begrenzte nichtleere Listen erforderlich.')
        us=[_text(u,'ursprung_id') for u in us]
        if len(set(us))!=len(us) or any(u not in urspruenge or bestand.get((u,v),_bruch(0))<=0 for u in us): _fehler('ursprung_ids','Eindeutige beim Abgebenden vorhandene Urspruenge erforderlich.')
        gewichte={};summe=_bruch(0)
        for a in emp:
            if not isinstance(a,dict) or set(a)!={'erbe_id','verteilungsgewicht'}: _fehler('empfaenger','Genau Erbe und Gewicht erforderlich.')
            e=_text(a['erbe_id'],'erbe_id');g=_geld(a['verteilungsgewicht'])
            if e not in personen or e==v or e in gewichte or g<=0: _fehler('empfaenger','Eindeutiger anderer bekannter Erbe mit positivem Gewicht erforderlich.')
            gewichte[e]=g;summe=_addieren(summe,g)
        for u in us:
            transfer=_multiplizieren(bestand[u,v],q);bestand[u,v]=_subtrahieren(bestand[u,v],transfer)
            for e,g in gewichte.items(): bestand[u,e]=_addieren(bestand.get((u,e),_bruch(0)),_multiplizieren(transfer,_dividieren(g,summe)))
    summen={e:_bruch(0) for e in personen};zeilen=[]
    for u in urspruenge:
        for e in personen:
            q=bestand.get((u,e),_bruch(0));summen[e]=_addieren(summen[e],q)
            if q>0: zeilen.append(dict(ursprung_id=u,erbe_id=e,erbquote=_bruchteile(q)))
    wert=dict(sonderteile_nach_ursprung=zeilen,gesamtquoten=[dict(erbe_id=e,erbquote=_bruchteile(summen[e])) for e in personen],erfasste_gesamtquote=_bruchteile(gesamt))
    eingaben = dict(erben_ids=erben_ids, ursprungsanteile=ursprungsanteile, uebertragungsschritte=uebertragungsschritte, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'erbquoten','BGB_ERBTEILE_QUALIFIZIERTE_UEBERTRAGUNGSKETTE',eingaben,[dict(operation='Qualifizierte Anteilstransfers chronologisch exakt verteilen, Restanteile fortschreiben und Sonderteile nach Urspruengen erhalten.')],eingaben.copy())
    ergebnis["hinweise"] = ['§§2094/2095/2098/2099: rein rechnerische Fortfuehrung rechtlich bestimmter einzelner Uebertragungsschritte. Je ausgewahltem Ursprungsanteil aktuelle Quote des Abgebenden mit Uebertragungsquote multiplizieren, danach nach qualifizierten relativen Gewichten auf Empfaenger verteilen; Rest beim Abgebenden belassen. Jede spaetere Stufe verwendet den fortgeschriebenen Bestand, jeder angewachsene Sonderteil behaelt seinen Ursprung2095. Verschachtelte Gruppenvorraenge, individuelle Sperren und Ersatzerben bestimmen den rechtlich vorgegebenen Empfaengerkreis je Stufe; sie sind keine automatisch aus Namen erschlossene Familientopologie. Relative Gewichte muessen zum jeweiligen Normfall passen, insbesondere nicht blind aktuelle durch vorherige Anwachsung vergroesserte Gesamtquoten als urspruengliche Einsetzungsgewichte verwenden. Vorhandene2094/2098Grundfunktionen koennen passende Empfaenger-/Quotenbelege liefern. Nicht zu uebertragende oder rechtlich ungeklärte Teile bleiben getrennt; keine automatische Zuteilung an gesetzliche Erben. Gesamtquoten nur Summen, keine Aufhebung von Vermächtnis-/Auflagen-/Ausgleichungslasten am Ursprung. Keine Aussage, dass ein konkreter Wegfallgrund oder eine konkrete Testamentseinsetzung wirksam ist.']
    return ergebnis

