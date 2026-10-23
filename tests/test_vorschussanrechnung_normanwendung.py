import json
from pathlib import Path
import bgbcalc

def test_vorschussanrechnung_normanwendung():
    for f in json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/vorschussanrechnung_normanwendung.json').read_text()):
        r=getattr(bgbcalc,f['funktion'])(**f['eingaben'])
        assert r['status']=='BERECHNET'
        assert r['wert']==f['erwarteter_wert'],f['fall_id']
