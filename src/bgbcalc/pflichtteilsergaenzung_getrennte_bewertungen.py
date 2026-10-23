from .kalender import _ergebnis, _text, _vorhanden, _fehler
from .betraege import _geld
from .zahlen import _bruch, _addieren, _subtrahieren, _multiplizieren
from .zinsen import _bruchteile
from .erbteilung_gemischter_ausgleich_mit_ueberempfang import erbteilung_gemischter_ausgleich_mit_ueberempfang
from .pflichtteilsergaenzung import pflichtteilsergaenzung_mehrhinterlassung

def pflichtteilsergaenzung_getrennte_bewertungen(gruppennachlass=None, gruppenquote_am_gesamtnachlass=None, berechtigter_id=None, ordentliche_bewertung=None, fiktive_bewertung=None, ergaenzungsposten=None, hinterlassener_erbteilwert=None, ausgleichungsmodell=None, methodennachweis=None):
    """Zwei vollständig berechnete Ausgleichungs-/Anrechnungsbewertungen mit differenzierten Schenkungswerten, Massenüberschneidungen und zusätzlicher Anrechnung verbinden; Mehrhinterlassung zuletzt abziehen."""
    masse=_geld(gruppennachlass);q=_geld(gruppenquote_am_gesamtnachlass);hinter=_geld(hinterlassener_erbteilwert);name=_text(berechtigter_id,'berechtigter_id');_text(methodennachweis,'methodennachweis')
    if not 0<q<=1:_fehler('gruppenquote_am_gesamtnachlass','Positive Quote höchstens1erforderlich.')
    def bewertung(d,n):
        _vorhanden(d,'bewertung')
        if not isinstance(d,dict) or set(d)!={'miterben','reiner_anrechnungswert_2315','doppelanrechnungswert_2316'}:_fehler('bewertung','Miterben und beide Anrechnungswerte erforderlich.')
        rein=_geld(d['reiner_anrechnungswert_2315']);dopp=_geld(d['doppelanrechnungswert_2316']);basis=_addieren(n,_multiplizieren(q,rein));teilung=erbteilung_gemischter_ausgleich_mit_ueberempfang(_bruchteile(basis),d['miterben'],ausgleichungsmodell,methodennachweis)['wert'];personen={p['person_id']:_geld(p['relative_erbquote']) for p in d['miterben']}
        if name not in personen:_fehler('berechtigter_id','Berechtigter muss Gruppenmitglied sein.')
        erb=_geld(next(p['erbteil_nach_gemischtem_ausgleich'] for p in teilung['zuteilungen'] if p['person_id']==name));pflicht=max(_subtrahieren(_subtrahieren(_multiplizieren(erb,_bruch(1,2)),_multiplizieren(dopp,_bruch(1,2))),rein),_bruch(0))
        return pflicht,personen
    ordentlich,personen=bewertung(ordentliche_bewertung,masse);_vorhanden(ergaenzungsposten,'ergaenzungsposten')
    if not isinstance(ergaenzungsposten,list) or len(ergaenzungsposten)>1000:_fehler('ergaenzungsposten','Liste0..1000erforderlich.')
    neu=masse;extra=_bruch(0);kennungen=set()
    for p in ergaenzungsposten:
        if not isinstance(p,dict) or set(p)!={'posten_id','hinzurechnungswert','bereits_erfasster_wert','bereits_erfasste_quote','ergaenzungsanrechnungswert','voranrechnungswert','voranrechnungsquote'}:_fehler('ergaenzungsposten','Vollständige sieben Postenfelder erforderlich.')
        kennung=_text(p['posten_id'],'posten_id')
        if kennung in kennungen:_fehler('posten_id','Jeden Posten nur einmal.')
        kennungen.add(kennung);v={k:_geld(x) for k,x in p.items() if k!='posten_id'}
        if v['bereits_erfasste_quote']>1 or v['voranrechnungsquote']>1:_fehler('quote','Quoten höchstens1.')
        vorhanden=_multiplizieren(v['bereits_erfasster_wert'],v['bereits_erfasste_quote']);voran=_multiplizieren(v['voranrechnungswert'],v['voranrechnungsquote'])
        if voran>v['ergaenzungsanrechnungswert']:_fehler('voranrechnung','Voranrechnung darf die hier betrachtete Ergänzungsanrechnung nicht übersteigen.')
        neu=_addieren(neu,_subtrahieren(_multiplizieren(q,v['hinzurechnungswert']),vorhanden));extra=_addieren(extra,_subtrahieren(v['ergaenzungsanrechnungswert'],voran))
    if neu<0:_fehler('ergaenzungsposten','Resultierende Gruppenmasse muss nichtnegativ bleiben.')
    fiktiv,personen_fiktiv=bewertung(fiktive_bewertung,neu)
    if personen!=personen_fiktiv:_fehler('bewertung','Beide Rechnungen benötigen identische Personen und relative Erbquoten.')
    vor=max(_subtrahieren(_subtrahieren(fiktiv,extra),ordentlich),_bruch(0));nach=pflichtteilsergaenzung_mehrhinterlassung(_bruchteile(vor),_bruchteile(hinter),_bruchteile(ordentlich),methodennachweis)['wert'];erg=_geld(nach['verbleibende_ergaenzung']);mehr=max(_subtrahieren(ordentlich,hinter),_bruch(0))
    wert=dict(ergaenzte_gruppenmasse=_bruchteile(neu),ordentlicher_pflichtteil=_bruchteile(ordentlich),fiktiver_pflichtteil_vor_zusaetzlicher_anrechnung=_bruchteile(fiktiv),zusaetzliche_ergaenzungsanrechnung=_bruchteile(extra),ergaenzung_vor_mehrhinterlassung=_bruchteile(vor),mehrhinterlassung=nach['mehrhinterlassung'],verbleibende_ergaenzung=_bruchteile(erg),ordentlicher_mehrbetrag=_bruchteile(mehr),zusaetzlicher_gesamtbetrag=_bruchteile(_addieren(erg,mehr)))
    eingaben = dict(gruppennachlass=gruppennachlass, gruppenquote_am_gesamtnachlass=gruppenquote_am_gesamtnachlass, berechtigter_id=berechtigter_id, ordentliche_bewertung=ordentliche_bewertung, fiktive_bewertung=fiktive_bewertung, ergaenzungsposten=ergaenzungsposten, hinterlassener_erbteilwert=hinterlassener_erbteilwert, ausgleichungsmodell=ausgleichungsmodell, methodennachweis=methodennachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_PFLICHTTEILSERGAENZUNG_GETRENNTE_BEWERTUNGEN',eingaben,[dict(operation='Zwei vollständig berechnete Ausgleichungs-/Anrechnungsbewertungen mit differenzierten Schenkungswerten, Massenüberschneidungen und zusätzlicher Anrechnung verbinden; Mehrhinterlassung zuletzt abziehen.')],eingaben.copy())
    ergebnis["hinweise"] = ['Bedingte Zweirechnungs-Komposition: ordentliche und fiktive gesetzliche Gruppenverteilung mit bestehendem2055/2056/2057a-Kern vollständig berechnen, jeweils reine2315-Zuwendung gruppenanteilig zur Masse hinzufügen; eigenen hypothetischen Erbteil halbieren, halbe2316-Doppelanrechnung und reine2315-Anrechnung abziehen, mindestens0. Ergänzte Gruppenmasse=ursprünglicheGruppenmasse+Summe(Gruppenquote*Hinzurechnungswert-bereitsErfassterWert*Erfassungsquote). Unterschiedliche Bewertungen derselben Zuwendung erlaubt; kein pauschaler Vergleich verschiedener2315/2055-Werte als Obergrenze. Zusätzliche2327-Anrechnung=Summe(Ergänzungsanrechnungswert-Voranrechnungswert*Voranrechnungsquote), danach Ergänzung=max(fiktiverPflichtteil-zusätzlicheAnrechnung-ordentlicherPflichtteil,0).2326-Mehrhinterlassung mit vorhandenem Kern abziehen; ordentlicher Mehrbetrag=max(ordentlicherPflichtteil-Hinterlassung,0). Kein doppeltes Hinzurechnen/Anrechnen automatisch unterstellen: korrespondierende Werte und Quoten ausdrücklich rechtlich bestimmen. Dieses Rechenmodell und die Zuordnung der Überschneidungen sind keine allgemein bestätigte Rechtsauslegung; keine Standardwahl der Bewertungs-/Ausgleichsmethode. Gleiche Personengruppe und Erbquoten in beiden Rechnungen; kein automatischer Rechtsverzicht oder Bewertungsentscheid. Nur nichtnegative resultierende Gruppenmassen im vorhandenen Ausgleichskern.']
    return ergebnis

