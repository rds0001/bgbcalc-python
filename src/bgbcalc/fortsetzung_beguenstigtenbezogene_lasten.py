from .kalender import _ergebnis, _fehler, _text, _vorhanden
from .betraege import _geld
from .zahlen import _bruch, _addieren, _subtrahieren, _multiplizieren, _dividieren
from .zinsen import _bruchteile

def fortsetzung_beguenstigtenbezogene_lasten(abkoemmlinge=None, lasten=None, einordnungsnachweis=None):
    """Jede qualifizierte Last nach relativen Beguenstigtengewichten verteilen, personenbezogen addieren und vom ungekürzten Ausgangsanteilswert abziehen."""
    _text(einordnungsnachweis,'einordnungsnachweis');_vorhanden(abkoemmlinge,'abkoemmlinge');_vorhanden(lasten,'lasten')
    if not isinstance(abkoemmlinge,list) or not 1<=len(abkoemmlinge)<=1000 or not isinstance(lasten,list) or len(lasten)>1000: _fehler('listen','Gueltige begrenzte Personen- und Lastenlisten erforderlich.')
    basis={};abzug={};gesamt=_bruch(0)
    for p in abkoemmlinge:
        if not isinstance(p,dict) or set(p)!={'abkoemmling_id','grundanteilswert'}: _fehler('abkoemmlinge','Genau Kennung und grundanteilswert erforderlich.')
        k=_text(p['abkoemmling_id'],'abkoemmling_id')
        if k in basis: _fehler('abkoemmling_id','Person doppelt.')
        basis[k]=_geld(p['grundanteilswert']);abzug[k]=_bruch(0);gesamt=_addieren(gesamt,basis[k])
    lastkennungen=set();lastsumme=_bruch(0)
    for l in lasten:
        if not isinstance(l,dict) or set(l)!={'last_id','betrag','beguenstigte'}: _fehler('lasten','Genau last_id, betrag und beguenstigte erforderlich.')
        kennung=_text(l['last_id'],'last_id');betrag=_geld(l['betrag']);gruppe=l['beguenstigte']
        if kennung in lastkennungen: _fehler('last_id','Last doppelt.')
        lastkennungen.add(kennung)
        if not isinstance(gruppe,list) or not 1<=len(gruppe)<=1000: _fehler('beguenstigte','Nichtleere begrenzte Liste erforderlich.')
        gewichte={};summe=_bruch(0)
        for p in gruppe:
            if not isinstance(p,dict) or set(p)!={'abkoemmling_id','lastgewicht'}: _fehler('beguenstigte','Genau Kennung und Lastgewicht erforderlich.')
            k=_text(p['abkoemmling_id'],'abkoemmling_id');q=_geld(p['lastgewicht'])
            if k not in basis or k in gewichte or q<=0: _fehler('beguenstigte','Bekannte eindeutige Person mit positivem Gewicht erforderlich.')
            gewichte[k]=q;summe=_addieren(summe,q)
        for k,q in gewichte.items(): abzug[k]=_addieren(abzug[k],_multiplizieren(betrag,_dividieren(q,summe)))
        lastsumme=_addieren(lastsumme,betrag)
    wert=dict(abkoemmlingssalden=[dict(abkoemmling_id=k,grundanteilswert=_bruchteile(v),lastensumme=_bruchteile(abzug[k]),rechnerischer_saldo=_bruchteile(_subtrahieren(v,abzug[k]))) for k,v in basis.items()],grundanteilswertsumme=_bruchteile(gesamt),lastensumme=_bruchteile(lastsumme),rechnerische_saldosumme=_bruchteile(_subtrahieren(gesamt,lastsumme)))
    eingaben = dict(abkoemmlinge=abkoemmlinge, lasten=lasten, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_FORTSETZUNG_BEGUENSTIGTENBEZOGENE_LASTEN',eingaben,[dict(operation='Jede qualifizierte Last nach relativen Beguenstigtengewichten verteilen, personenbezogen addieren und vom ungekürzten Ausgangsanteilswert abziehen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§1503III/§1511III2: Abfindungs-/Ausschlusslast nur bei den durch Verzicht/Ausschliessung beguenstigten Abkoemmlingen verteilen. Relative Lastgewichte sind rechtlich bestimmte Vorteils-/Belastungsverhaeltnisse, nicht automatisch Erbquoten oder gleiche Kopfanteile. Jede Last wird exakt einmal verteilt; nicht beguenstigte Personen behalten ihren Ausgangswert. Grundanteilswerte muessen vor diesen Lasten und unter zutreffender Gesamtgutsbilanz1501/1498 bestimmt sein. Negative Salden sind ausschliesslich rechnerische Bilanzgroessen, kein ausgegebener Nachschuss-, Rueckzahlungs- oder persoenlicher Ersatzanspruch;1498/1476II2 beachten. Keine eigenstaendige Ermittlung von Berechtigung, Lastgewichten, Abfindungswirksamkeit oder faelliger Barauszahlung.']
    return ergebnis

