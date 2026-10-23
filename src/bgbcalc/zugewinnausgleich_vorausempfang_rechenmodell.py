from .kalender import _ergebnis, _text, _auswahl, _vorhanden, _fehler
from .betraege import _geld
from .zahlen import _bruch, _zahleneingabe, _addieren, _subtrahieren, _multiplizieren
from .zinsen import _bruchteile

def zugewinnausgleich_vorausempfang_rechenmodell(ehegatten=None, vorausempfaenge=None, nullbegrenzungsfolge=None, haftungsgrenzenfolge=None, methodennachweis=None):
    """Getrennte Richtungsrechnungen mit tatsächlichen Vermögensdifferenzen, bewerteten Vorausempfängen und ausdrücklich vorgegebener Null-/Haftungsgrenzenfolge ausführen."""
    _text(methodennachweis,'methodennachweis');_auswahl(nullbegrenzungsfolge,'nullbegrenzungsfolge',('zugewinn_vor_korrektur','vermoegenskorrektur_vor_nullgrenze'));_auswahl(haftungsgrenzenfolge,'haftungsgrenzenfolge',('haftungsgrenze_vor_anrechnung','haftungsgrenze_nach_anrechnung'));_vorhanden(ehegatten,'ehegatten');_vorhanden(vorausempfaenge,'vorausempfaenge')
    if not isinstance(ehegatten,dict) or set(ehegatten)!={'a','b'}:_fehler('ehegatten','Genau a und b erforderlich.')
    basen={};grenzen={}
    for k,p in ehegatten.items():
        if not isinstance(p,dict) or set(p)!={'vermoegensdifferenz','endnettovermoegen','illoyale_hinzurechnung'}:_fehler('ehegatten','Drei Vermögensfelder erforderlich.')
        basen[k]=_zahleneingabe(p['vermoegensdifferenz']);grenzen[k]=max(_addieren(_zahleneingabe(p['endnettovermoegen']),_geld(p['illoyale_hinzurechnung'])),_bruch(0))
    if not isinstance(vorausempfaenge,list) or len(vorausempfaenge)>1000:_fehler('vorausempfaenge','Liste0..1000erforderlich.')
    summen={k:[_bruch(0),_bruch(0),_bruch(0)] for k in ('a_an_b','b_an_a')}
    for p in vorausempfaenge:
        if not isinstance(p,dict) or set(p)!={'richtung','hinzurechnungswert','herausrechnungswert','anrechnungswert'}:_fehler('vorausempfaenge','Richtung und drei Werte erforderlich.')
        r=_auswahl(p['richtung'],'richtung',('a_an_b','b_an_a'))
        for i,k in enumerate(('hinzurechnungswert','herausrechnungswert','anrechnungswert')):summen[r][i]=_addieren(summen[r][i],_geld(p[k]))
    wege={};reste={}
    for r,geber,empfaenger in (('a_an_b','a','b'),('b_an_a','b','a')):
        gb=basen[geber];eb=basen[empfaenger];hinzu,heraus,anrechnung=summen[r]
        if nullbegrenzungsfolge=='zugewinn_vor_korrektur':gb=max(gb,_bruch(0));eb=max(eb,_bruch(0))
        gb=max(_addieren(gb,hinzu),_bruch(0));eb=max(_subtrahieren(eb,heraus),_bruch(0));halb=_multiplizieren(max(_subtrahieren(gb,eb),_bruch(0)),_bruch(1,2));grenze=grenzen[geber]
        rest=max(_subtrahieren(min(halb,grenze),anrechnung),_bruch(0)) if haftungsgrenzenfolge=='haftungsgrenze_vor_anrechnung' else min(max(_subtrahieren(halb,anrechnung),_bruch(0)),grenze)
        reste[r]=rest;wege[r]=dict(korrigierte_geberbasis=_bruchteile(gb),korrigierte_empfaengerbasis=_bruchteile(eb),halbe_positive_differenz=_bruchteile(halb),haftungsgrenze=_bruchteile(grenze),anrechnungswert=_bruchteile(anrechnung),bedingter_restbetrag=_bruchteile(rest))
    wert=dict(a_an_b=wege['a_an_b'],b_an_a=wege['b_an_a'],rechnerischer_saldo_a_an_b=_bruchteile(_subtrahieren(reste['a_an_b'],reste['b_an_a'])))
    eingaben = dict(ehegatten=ehegatten, vorausempfaenge=vorausempfaenge, nullbegrenzungsfolge=nullbegrenzungsfolge, haftungsgrenzenfolge=haftungsgrenzenfolge, methodennachweis=methodennachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_ZUGEWINNAUSGLEICH_VORAUSEMPFANG_RECHENMODELL',eingaben,[dict(operation='Getrennte Richtungsrechnungen mit tatsächlichen Vermögensdifferenzen, bewerteten Vorausempfängen und ausdrücklich vorgegebener Null-/Haftungsgrenzenfolge ausführen.')],eingaben.copy())
    ergebnis["hinweise"] = ['Bedingte Erweiterung des vorhandenen einseitigen1380-Grundmodells: je Anspruchsrichtung die zugehörigen Vorausempfänge summieren, Geberbasis um Hinzurechnung erhöhen und Empfängerbasis um Herausrechnung vermindern. Zwingend gewählte Nullbegrenzungsfolge bestimmt, ob ursprüngliche Vermögensdifferenzen schon vor dieser Korrektur bei0begrenzt werden oder erst die korrigierten Differenzen. Positive halbe Differenz berechnen;1378II-Haftungsgrenze=max(Endnettovermögen+illoyaleHinzurechnung,0) selbst berechnen. Haftungsgrenze gemäß gewählter Folge vor oder nach der auf0begrenzten Anrechnung anwenden. Beide Richtungsrechnungen separat ausweisen, einschließlich Gegenrichtung ohne einschlägigen Empfang. Gegenseitige Empfänge werden in diesem ausdrücklich qualifizierten Modell getrennt nach Richtung behandelt; kein unbelegtes automatisches Saldieren der Zuwendungswerte. Rechnerischer Saldo der beiden Ergebnisse ist nur Vergleichswert, keine automatische Aufrechnung oder rechtliche Feststellung zweier Ansprüche. Reihenfolge/reziproke Behandlung/verschiedene Wertansätze rechtlich nicht allgemein bestätigt; keine Standardwahl. Kein negativer Rückforderungsanspruch allein aus überhöhter Anrechnung.']
    return ergebnis

