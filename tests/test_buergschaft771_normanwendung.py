import json
from pathlib import Path
import bgbcalc

def test_buergschaft771_normanwendung():
    for f in json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/buergschaft771_normanwendung.json').read_text()):
        r=bgbcalc.verjaehrung_gehemmte_kalendertage(**f['eingaben'])
        assert r['status']=='BERECHNET'
        assert r['wert']==f['erwarteter_wert'],f['fall_id']
