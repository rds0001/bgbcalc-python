from .kalender import _ergebnis, _auswahl
from .betraege import _geld
from .zahlen import _bruch, _addieren, _subtrahieren, _multiplizieren, _dividieren, _zahleneingabe
from .zinsen import _bruchteile
from .gemischter_erbausgleich import erbteilung_gemischter_ausgleich
from .erbausgleich import erb_zuwendungen_ausgleichen

def erbteilung_gemischter_ausgleich_mit_ueberempfang(gruppennachlass=None, miterben=None, ausgleichungsmodell=None, methodennachweis=None):
    """Zwingend gewähltes kombiniertes Ausgleichungsmodell unter Wiederverwendung vorhandener Validierung/2056-Rechnung berechnen; keine automatische Auslegung."""
    _auswahl(ausgleichungsmodell,'ausgleichungsmodell',('leistungsvorwegabzug_mit_fortgeltung','gemeinsame_neuberechnung_ohne_ausgeschiedene'))
    erbteilung_gemischter_ausgleich(gruppennachlass,miterben,True,methodennachweis)
    n=_geld(gruppennachlass);quoten=[_zahleneingabe(p['relative_erbquote']) for p in miterben];z=[_geld(p['ausgleichungswert_zuwendungen']) for p in miterben];l=[_geld(p['leistungs_ausgleichsbetrag']) for p in miterben];aus=[]
    def summieren(werte):
        s=_bruch(0)
        for x in werte:s=_addieren(s,x)
        return s
    if ausgleichungsmodell=='leistungsvorwegabzug_mit_fortgeltung':
        liste=[dict(person_id=p['person_id'],erbquote_zaehler=q.numerator,erbquote_nenner=q.denominator,ausgleichungswert=p['ausgleichungswert_zuwendungen']) for p,q in zip(miterben,quoten)]
        kern=erb_zuwendungen_ausgleichen(_bruchteile(_subtrahieren(n,summieren(l))),liste,True,methodennachweis)['wert'];aus=kern['ausser_ansatz'];betraege=[_addieren(_geld(p['betrag']),leistung) for p,leistung in zip(kern['verteilung'],l)]
    else:
        aktiv=list(range(len(miterben)));aus_indices=[];betraege=[_bruch(0) for _ in miterben]
        while aktiv:
            masse=_addieren(_subtrahieren(n,summieren(l[i] for i in aktiv)),summieren(z[i] for i in aktiv));qsum=summieren(quoten[i] for i in aktiv)
            pruefung={i:_addieren(_subtrahieren(_multiplizieren(masse,_dividieren(quoten[i],qsum)),z[i]),l[i]) for i in aktiv};negativ=[i for i in aktiv if pruefung[i]<0]
            if not negativ:
                for i in aktiv:betraege[i]=pruefung[i]
                break
            aus_indices.extend(negativ);aktiv=[i for i in aktiv if i not in negativ]
        aus=[p['person_id'] for i,p in enumerate(miterben) if i in aus_indices]
    wert=dict(ausgleichungsmodell=ausgleichungsmodell,ausser_ansatz=aus,zuteilungen=[dict(person_id=p['person_id'],erbteil_nach_gemischtem_ausgleich=_bruchteile(b)) for p,b in zip(miterben,betraege)])
    eingaben = dict(gruppennachlass=gruppennachlass, miterben=miterben, ausgleichungsmodell=ausgleichungsmodell, methodennachweis=methodennachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_ERBTEILUNG_GEMISCHTER_AUSGLEICH_MIT_UEBEREMPFANG',eingaben,[dict(operation='Zwingend gewähltes kombiniertes Ausgleichungsmodell unter Wiederverwendung vorhandener Validierung/2056-Rechnung berechnen; keine automatische Auslegung.')],eingaben.copy())
    ergebnis["hinweise"] = ['2055/2056/2057a-Rechenkonkurrenz bei zugleich Leistenden und Überempfängern: keine allgemeine juristische Lösung aus ungeprüfter Iteration behaupten. Bedingtes Vorwegmodell zieht sämtliche qualifizierten Leistungen ab, verwendet vorhandene2056-Zuwendungsausscheidung und fügt individuelle Leistungen auch ausgeschiedenen Zuwendungsempfängern wieder hinzu. Bedingtes gemeinsames Modell berechnet je aktiver Gruppe q_i/Summeq*(N-SummeL+SummeZ)-Z_i+L_i; negative Endbeträge scheiden mit Quote,Zuwendung und Leistungsposition aus, Gruppe wird neu berechnet. Diese Behandlung muss im konkreten Fall rechtlich vorgegeben sein, nicht aus einem bloßen negativen Zwischenergebnis als Rechtsfolge erfunden werden. Beide Modelle erhalten die SummeN und erzeugen keine Rückzahlung aus negativem Erbteil. Leistungen sind billig bemessene Eingaben, keine erfundene Pflegevergütung. Keine2315-Anrechnung, Pflichtteilsergänzung oder automatische rechtliche Auswahl.']
    return ergebnis

