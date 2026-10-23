import json
from pathlib import Path
import bgbcalc as b

def test_miete563_ablaufhemmung():
    d=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/miete563_ablaufhemmung_normanwendung.json').read_text())
    for f in d['faelle']:
        grund=b.schuldrechtliche_sondergrundfrist('miete_eintrittsablehnung_563',f['kenntnis'],d['nachweis'])['wert']['rechnerisches_fristende']
        ende=b.verjaehrung_ablaufhemmung_mindestablauf('vertretungsmangel',f['ereignisse'],1,'monate',grund,False,True)['wert']
        assert ende['nachlauf_kuerzer_als_sechs_monate'] is True
        assert ende['rechnerischer_letzter_tag']==f['ende']
