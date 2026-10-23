import json
from pathlib import Path
import bgbcalc as b

def test_mietform550_normanwendung():
    d=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/mietform550_normanwendung.json').read_text())
    for f in d['faelle']:
        normal=b.wohnraummiete_kuendigungstermin(f['zugang'],'mieter_standard',f['grenze'],None,False,d['nachweis'])['wert']['fruehester_beendigungstag']
        assert normal==f['regulaer']
        ende=b.miete_formmangel_beendigungsgrenze('2024-02-15',normal,d['nachweis'])['wert']
        assert ende==dict(jahresmindestgrenze='2025-02-15',fruehester_monatsendtermin='2025-02-28')
