import json
from pathlib import Path
import bgbcalc as b

def test_gesellschaft206_212_normanwendung():
    d=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/gesellschaft206_212_normanwendung.json').read_text())
    h='Qualifizierte728b/739-Verweise, festes206-Modell und Monatsendregel.'
    grund=b.gesellschaft_fuenfjahresgrundfrist('nachhaftung_728b',d['wirksam'],d['kenntnis'],None,None,h)['wert']['rechnerisches_fuenfjahresende']
    assert grund==d['partnergrundende']
    f=d['nachhaftung']
    r=b.verjaehrung_hoehere_gewalt_festes_ablauffenster('2024-02-01',grund,[dict(erster_verhinderter_tag=f['hindernis_von'],letzter_verhinderter_tag=f['hindernis_bis'])],'fester_ablauf_ohne_206','letzter_monatstag',h)['wert']
    assert r['rechnerischer_letzter_tag']==f['ende']
    for unwirksam in [False,True]:
        s=b.gesellschaft_nachhaftung_fristsicherung(r['rechnerischer_letzter_tag'],f['sicherungstag'],[dict(ereignis_id='V',art='vollstreckungsantrag',datum=f['sicherungstag'],rueckwirkend_unwirksam_212=unwirksam)],h)['wert']
        assert s['zeitliche_kopplung_erfuellt'] is (not unwirksam)
        assert s['nachhaftungsfrist_letzter_tag']==f['ende']
    f=d['gesellschaft']
    grund=b.gesellschaft_fuenfjahresgrundfrist('erloeschen_verjaehrung_739',d['wirksam'],d['kenntnis'],None,None,h)['wert']['rechnerisches_fuenfjahresende']
    kurz=b.fristende(d['kenntnis'],3,'jahre','ereignis')['wert']
    assert kurz==f['kurzgrundende']
    k=b.verjaehrung_hoehere_gewalt_festes_ablauffenster('2024-02-01',kurz,[dict(erster_verhinderter_tag=f['hindernis_von'],letzter_verhinderter_tag=f['hindernis_bis'])],'fester_ablauf_ohne_206','letzter_monatstag',h)['wert']
    assert k['rechnerischer_letzter_tag']==f['kurzende']
    von=max(f['hindernis_von'],k['fenster_erster_tag']);bis=min(f['hindernis_bis'],k['fenster_letzter_tag'])
    p=b.verjaehrung_gehemmte_kalendertage('2024-02-01',grund,[dict(erster_gehemmter_tag=von,letzter_gehemmter_tag=bis)],True)['wert']['rechnerischer_letzter_tag']
    assert p==f['partnerende']
    assert min(p,k['rechnerischer_letzter_tag'])==f['kurzende']
    invalid=b.verjaehrung_neubeginn_grundfrist('2026-01-01',5,'jahre',False)
    assert invalid['status']=='NICHT_ANWENDBAR'
    assert invalid['wert'] is None
