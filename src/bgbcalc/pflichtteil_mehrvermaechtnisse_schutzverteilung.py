from .kalender import _ergebnis, _text, _vorhanden, _fehler, _auswahl, _ganzzahl
from .betraege import _geld, _wahrheitswert
from .zahlen import _bruch, _addieren, _subtrahieren, _multiplizieren, _dividieren
from .zinsen import _bruchteile
from .quotenverteilung import _begrenzte_quotenverteilung

def pflichtteil_mehrvermaechtnisse_schutzverteilung(erwerbswert_vor_vermaechtnissen=None, gesamte_pflichtteilslast=None, anderweitig_getragene_last_2323=None, vermaechtnisse=None, erbenschutz_anwendbar=None, eigener_pflichtteilswert=None, konkurrenzmodell=None, methodennachweis=None):
    """Gemeinsame Pflichtteilskürzung und zusätzlichen Erbenschutz in getrennten Rangstufen unter individuellen Schutzgrenzen verteilen."""
    n=_geld(erwerbswert_vor_vermaechtnissen);gesamt=_geld(gesamte_pflichtteilslast);fremd=_geld(anderweitig_getragene_last_2323);eigen=_geld(eigener_pflichtteilswert);schutz_erbe=_wahrheitswert(erbenschutz_anwendbar,'erbenschutz_anwendbar');_text(methodennachweis,'methodennachweis');_auswahl(konkurrenzmodell,'konkurrenzmodell',('erbe_vorrangig','bedachte_vorrangig'));_vorhanden(vermaechtnisse,'vermaechtnisse')
    if gesamt>n or fremd>gesamt or (not schutz_erbe and eigen!=0):_fehler('last_und_schutz','Last höchstens Erwerb,anderweitigeLast höchstens Gesamtlast; ohneErbenschutz Wert0.')
    if not isinstance(vermaechtnisse,list) or not 1<=len(vermaechtnisse)<=1000:_fehler('vermaechtnisse','Liste1..1000erforderlich.')
    namen=[];werte=[];schutz=[];raenge=[];summe=_bruch(0)
    for p in vermaechtnisse:
        if not isinstance(p,dict) or set(p)!={'beschwerung_id','vermaechtniswert','pflichtteilsschutzwert','rang'}:_fehler('vermaechtnisse','Genau Kennung,Wert,Schutzwert und Rang erforderlich.')
        name=_text(p['beschwerung_id'],'beschwerung_id');v=_geld(p['vermaechtniswert']);s=_geld(p['pflichtteilsschutzwert']);r=_ganzzahl(p['rang'],'rang',1,1000)
        if name in namen:_fehler('beschwerung_id','JedeBeschwerungnurEinmal.')
        namen.append(name);werte.append(v);schutz.append(min(v,s));raenge.append(r);summe=_addieren(summe,v)
    if summe>n:_fehler('vermaechtnisse','Beschwerungssumme höchstens Erwerb; vorgelagerte Haftungsbegrenzung gesondert.')
    last=_subtrahieren(gesamt,fremd);kuerzungen=[_bruch(0) for _ in werte];grund=_bruch(0)
    for v,s in zip(werte,schutz):grund=_addieren(grund,min(_multiplizieren(last,_dividieren(v,n)) if n else _bruch(0),_subtrahieren(v,s)))
    def verteilen(betrag,grenzen):
        rest=betrag
        for rang in sorted(set(raenge),reverse=True):
            indices=[i for i,r in enumerate(raenge) if r==rang];anteile,rest=_begrenzte_quotenverteilung(rest,[werte[i] for i in indices],[grenzen[i] for i in indices])
            for i,a in zip(indices,anteile):kuerzungen[i]=_addieren(kuerzungen[i],a)
        return rest
    verteilen(grund,[_subtrahieren(v,s) for v,s in zip(werte,schutz)])
    def erbenrest():
        s=_subtrahieren(_subtrahieren(n,summe),last)
        for k in kuerzungen:s=_addieren(s,k)
        return s
    ziel=min(eigen,_subtrahieren(n,summe)) if schutz_erbe else _bruch(0)
    if schutz_erbe:
        bedarf=max(_subtrahieren(ziel,erbenrest()),_bruch(0));rest=verteilen(bedarf,[max(_subtrahieren(_subtrahieren(v,k),s),_bruch(0)) for v,k,s in zip(werte,kuerzungen,schutz)])
        if konkurrenzmodell=='erbe_vorrangig' and rest>0:verteilen(rest,[_subtrahieren(v,k) for v,k in zip(werte,kuerzungen)])
    erbe=erbenrest();fehl=max(_subtrahieren(ziel,erbe),_bruch(0)) if schutz_erbe else _bruch(0)
    wert=dict(verteilung=[dict(beschwerung_id=name,kuerzungsbetrag=_bruchteile(k),verbleibender_vermaechtniswert=_bruchteile(_subtrahieren(v,k))) for name,v,k in zip(namen,werte,kuerzungen)],verbleibender_erbenwert=_bruchteile(erbe),ungedeckter_erbenschutz=_bruchteile(fehl))
    eingaben = dict(erwerbswert_vor_vermaechtnissen=erwerbswert_vor_vermaechtnissen, gesamte_pflichtteilslast=gesamte_pflichtteilslast, anderweitig_getragene_last_2323=anderweitig_getragene_last_2323, vermaechtnisse=vermaechtnisse, erbenschutz_anwendbar=erbenschutz_anwendbar, eigener_pflichtteilswert=eigener_pflichtteilswert, konkurrenzmodell=konkurrenzmodell, methodennachweis=methodennachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_PFLICHTTEIL_MEHRVERMAECHTNISSE_SCHUTZVERTEILUNG',eingaben,[dict(operation='Gemeinsame Pflichtteilskürzung und zusätzlichen Erbenschutz in getrennten Rangstufen unter individuellen Schutzgrenzen verteilen.')],eingaben.copy())
    ergebnis["hinweise"] = ['Bedingtes Mehrbeschwerungsmodell2318/2189/2323: anderweitigeLast zuerst abziehen. Grundkürzung je Beschwerung anteiligLast*V_i/Erwerb, höchstens positiver Überschuss über individuellen Schutzwert; gemeinsame Grundkürzung rangweise auf nachrangige Beschwerungen zuerst verteilen, innerhalb eines Rangs wertproportional mit Obergrenzen. Zusätzlichen Erbenschutzbedarf zunächst vollständig aus noch ungeschützten Beschwerungsanteilen decken. Nur bei ausdrücklich qualifiziertem Erbenvorrang darf danach verbleibender Bedarf in geschützte Anteile eingreifen; Bedachtenvorrang lässt diesen Fehlbetrag offen. Keine vorbestehende Unterdeckung auf eigenen Pflichtteil auffüllen: SchutzErbe höchstens Erwerb-SummeV, SchutzBedachter höchstensV_i. Rang-/Schutzhierarchie ist eine zwingende rechtliche Modellvoraussetzung, keine allgemeine Lösung aller Auslegungsstreitigkeiten. Negative rechnerische Erbenreste sind offen ausgewiesene Belastung, kein automatisch neuer Anspruch. Keine automatischeGeldforderung beiSachvermächtnissen, keine doppelte Gesamtlastausübung pro Vermächtnis.']
    return ergebnis

