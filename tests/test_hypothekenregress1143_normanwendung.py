import json
from pathlib import Path
import bgbcalc

def test_hypothekenregress1143_normanwendung():
    for f in json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/hypothekenregress1143_normanwendung.json').read_text()):
        r=getattr(bgbcalc,f['funktion'])(**f['eingaben'])
        assert r['status']=='BERECHNET'
        assert r['wert']==f['erwarteter_wert'],f['fall_id']
