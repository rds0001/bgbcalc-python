import json
from pathlib import Path
import bgbcalc

def test_inventar590_normanwendung():
    for f in json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/inventar590_normanwendung.json').read_text()):
        r=bgbcalc.pacht_inventar_ausgleichsdifferenz(**f['eingaben'])
        assert r['status']=='BERECHNET'
        assert r['wert']==f['erwarteter_wert'],f['fall_id']
