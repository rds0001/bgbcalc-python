import json
from pathlib import Path
import bgbcalc as b
from bgbcalc.zahlen import _bruch,_zahleneingabe,_multiplizieren,_subtrahieren
from bgbcalc.zinsen import _bruchteile

def test_pflichtteil2322_raenge_normanwendung():
    f=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/pflichtteil2322_raenge_normanwendung.json').read_text())
    h='2320/21-Zuordnungsgewichte3:2 rechtlich qualifiziert; keine automatische Rang-/Testamentsauslegung.'
    for gewicht,vorteil,soll in zip(f['gewichte'],f['vorteile'],f['sonderlasten']):
        anteil=_bruchteile(_multiplizieren(_zahleneingabe(f['gesamtlast']),_bruch(gewicht,sum(f['gewichte']))))
        r=b.pflichtteil_vorteilslast('ersatzerwerb_2320',anteil,'0',vorteil,True,h)['wert']
        assert r['zugeordnete_sonderlast']==dict(zaehler=soll,nenner='1')
    h='2187II/2322-Begünstigter eines ausgeschlagenen beschwerten Vermächtnisses; gemeinsam begrenzter Unterlastblock; wirksamer2189-Vorrang und proportionale Restgewichte rechtlich qualifiziert.'
    gesamt=sum(int(p['beschwerungswert']) for p in f['beschwerungen'])
    verweigert=b.untervermaechtnis_verweigerungsbetrag(f['erwerb'],str(gesamt),True,h)['wert']
    begrenzt=_bruchteile(_subtrahieren(_bruch(gesamt),_zahleneingabe(verweigert)))
    budget=b.pflichtteil_deckung_beschwerungskuerzung(f['erwerb'],begrenzt,f['last'],True,h)['wert']['verbleibende_beschwerung']
    r=b.vermaechtnis_rangweise_beschwerungsverteilung(budget,f['beschwerungen'],h)['wert']
    assert [p['zugeteilter_betrag'] for p in r['verteilung']]==f['zuteilungen']
    assert r['verbleibendes_budget']==dict(zaehler='0',nenner='1')
