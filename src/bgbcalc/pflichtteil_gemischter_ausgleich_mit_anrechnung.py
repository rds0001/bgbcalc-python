from .kalender import _ergebnis, _text, _fehler
from .betraege import _geld
from .zahlen import _bruch, _addieren, _subtrahieren, _multiplizieren, _zahleneingabe
from .zinsen import _bruchteile
from .erbteilung_gemischter_ausgleich_mit_ueberempfang import erbteilung_gemischter_ausgleich_mit_ueberempfang

def pflichtteil_gemischter_ausgleich_mit_anrechnung(gruppennachlass=None, miterben=None, berechtigter_id=None, gruppenquote_am_gesamtnachlass=None, zugleich_anrechenbarer_zuwendungswert=None, reiner_anrechnungswert_2315=None, hinterlassener_erbteilwert=None, ausgleichungsmodell=None, methodennachweis=None):
    """Reine2315-Zuwendung anteilig zur hypothetischen Gruppenmasse addieren, gemischtes Modell berechnen, Anteil halbieren und getrennte Anrechnungen abziehen."""
    n=_geld(gruppennachlass);q=_zahleneingabe(gruppenquote_am_gesamtnachlass);a=_geld(zugleich_anrechenbarer_zuwendungswert);rein=_geld(reiner_anrechnungswert_2315);hinter=_geld(hinterlassener_erbteilwert);name=_text(berechtigter_id,'berechtigter_id')
    if not 0<q<=1:_fehler('gruppenquote_am_gesamtnachlass','Positive Quote höchstens1erforderlich.')
    masse=_addieren(n,_multiplizieren(rein,q));teilung=erbteilung_gemischter_ausgleich_mit_ueberempfang(_bruchteile(masse),miterben,ausgleichungsmodell,methodennachweis)['wert']
    personen=[p for p in miterben if p['person_id']==name]
    if not personen:_fehler('berechtigter_id','Berechtigter muss Gruppenmitglied sein.')
    if a>_geld(personen[0]['ausgleichungswert_zuwendungen']):_fehler('zugleich_anrechenbarer_zuwendungswert','Doppelanrechnung höchstens eigener enthaltener Zuwendungswert.')
    erb=_geld(next(p['erbteil_nach_gemischtem_ausgleich'] for p in teilung['zuteilungen'] if p['person_id']==name));vor=_multiplizieren(erb,_bruch(1,2));halb=_multiplizieren(a,_bruch(1,2));pflicht=max(_subtrahieren(_subtrahieren(vor,halb),rein),_bruch(0))
    wert=dict(hypothetischer_gruppennachlass=_bruchteile(masse),hypothetischer_gesetzlicher_erbteil=_bruchteile(erb),pflichtteil_vor_anrechnungen=_bruchteile(vor),halber_doppelanrechnungswert=_bruchteile(halb),pflichtteilswert=_bruchteile(pflicht),mehrbetrag_gegenueber_hinterlassenem_erbteil=_bruchteile(max(_subtrahieren(pflicht,hinter),_bruch(0))))
    eingaben = dict(gruppennachlass=gruppennachlass, miterben=miterben, berechtigter_id=berechtigter_id, gruppenquote_am_gesamtnachlass=gruppenquote_am_gesamtnachlass, zugleich_anrechenbarer_zuwendungswert=zugleich_anrechenbarer_zuwendungswert, reiner_anrechnungswert_2315=reiner_anrechnungswert_2315, hinterlassener_erbteilwert=hinterlassener_erbteilwert, ausgleichungsmodell=ausgleichungsmodell, methodennachweis=methodennachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_PFLICHTTEIL_GEMISCHTER_AUSGLEICH_MIT_ANRECHNUNG',eingaben,[dict(operation='Reine2315-Zuwendung anteilig zur hypothetischen Gruppenmasse addieren, gemischtes Modell berechnen, Anteil halbieren und getrennte Anrechnungen abziehen.')],eingaben.copy())
    ergebnis["hinweise"] = ['Bedingte2316/2315-Komposition: reine eigene2315-Zuwendung mit gesetzlicher Gruppenquote zur Gruppenmasse hinzufügen; vorhandenen ausdrücklich ausgewählten2055/2056/2057a-Kern auf hypothetische Masse anwenden. Eigenen hypothetischen gesetzlichen Anteil halbieren; zugleich ausgleichungspflichtige2315-Zuwendung nach2316IVnur halb, zusätzliche reine2315-Zuwendung vollständig abziehen; positiver Rest und2316II-Mehrbetrag. Gruppenquote verhindert volle Hinzurechnung zur Teilgruppe bei weiteren gesetzlichen Erben. Kein doppelt erfasstes Geschenk, keine automatische Bewertung/Kaufkraftbereinigung. Kombination und Reihenfolge sind rechtliche Modellvoraussetzungen, insbesondere zugleich leistende Überempfänger bleiben keine automatisch gelöste Auslegungsfrage. Unterschiedliche Wertansätze derselben Doppelzuwendung und2325/2327-Ergänzung separat. Rechtlicher Gruppenausschluss durch Erbverzicht und Ausstattungsschutz2316IIIvorqualifiziert.']
    return ergebnis

