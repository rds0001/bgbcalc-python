import json
from pathlib import Path
import bgbcalc as b

def test_vaterschaft1600b_korrekturen_normanwendung():
    f=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/vaterschaft1600b_korrekturen_normanwendung.json').read_text())
    h='1600b-Fall und Ereignisse rechtlich qualifiziert, abgeschlossene ganze Hemmungstage.'
    beginn=max(f['kenntnis_am'],f['geschaeftsunfaehigkeit_weggefallen_am'])
    r=b.fristende(max(beginn,f['kind_geboren_am']),2,'jahre','ereignis')
    assert r['wert']==f['wiederanfechtung_ende']
    r=b.fristende(f['unzumutbarkeit_bekannt_am'],2,'jahre','ereignis')
    assert r['wert']==f['neubeginn_ende']
    grund=b.vaterschaftsanfechtung_grundfrist(f['grundereignis'],f['kind_geboren_am'],'allgemein',None,None,h)['wert']['anfechtungsgrundfristende']
    assert grund==f['grundende']
    r=b.verjaehrung_verfahrenshemmungskette('2020-01-02',grund,[dict(hemmungsbeginn_am='2021-01-01',nachlaufereignis_am='2021-01-01',nachlaufgrund='anderweitige_beendigung')],h)
    assert r['wert']['beruecksichtigte_hemmungstage']==182
    assert r['wert']['rechnerischer_letzter_tag']==f['verfahrensende']
    r=b.verjaehrung_gehemmte_kalendertage('2020-01-02',grund,[dict(erster_gehemmter_tag='2021-01-01',letzter_gehemmter_tag='2021-01-10')],True)
    assert r['wert']['rechnerischer_letzter_tag']==f['drohungsende']
    r=b.verjaehrung_ablaufhemmung_mindestablauf('vertretungsmangel',[dict(ereignis='vertretungsmangel_behoben',datum='2022-02-01')],2,'jahre',grund,False,True)
    assert r['wert']['rechnerischer_letzter_tag']==f['schutzende']
