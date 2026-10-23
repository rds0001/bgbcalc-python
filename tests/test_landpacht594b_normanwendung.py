import json
from pathlib import Path
import bgbcalc

def test_landpacht594b_normanwendung():
    for f in json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/landpacht594b_normanwendung.json').read_text()):
        grund=bgbcalc.fristende(**f['grund_eingaben'])
        assert grund['status']=='BERECHNET'
        assert grund['wert']==f['erwartetes_warteende']
        assert f['kuendigung_eingaben']['kuendigungszugang_am']>grund['wert']
        r=bgbcalc.pacht_kuendigungstermin(**f['kuendigung_eingaben'])
        assert r['status']=='BERECHNET'
        assert r['wert']['rechnerischer_pachtendtermin']==f['erwarteter_endtermin']
