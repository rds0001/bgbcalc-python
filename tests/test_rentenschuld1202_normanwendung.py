import json
from pathlib import Path
import bgbcalc

def test_rentenschuld1202_normanwendung():
    for f in json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/rentenschuld1202_normanwendung.json').read_text()):
        grenze=bgbcalc.fristende(f['fristbeginn_am'],30,'jahre','ereignis')
        assert grenze['status']=='BERECHNET'
        assert grenze['wert']==f['erwartete_dreissigjahresgrenze']
        assert f['kuendigungszugang_am']>grenze['wert']
        ende=bgbcalc.fristende(f['kuendigungszugang_am'],6,'monate','ereignis')
        assert ende['status']=='BERECHNET'
        assert ende['wert']==f['erwartetes_kuendigungsfristende']
