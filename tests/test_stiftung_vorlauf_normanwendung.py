import json
from pathlib import Path
import bgbcalc

def test_stiftung_vorlauf_normanwendung():
    faelle=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/stiftung_vorlauf_normanwendung.json').read_text())
    for f in faelle:
        ablauf=bgbcalc.fristende(f['ausloesung_am'],1,'monate','ereignis')['wert']
        frueh=bgbcalc.fristverlaengerung(ablauf,1,'tage')['wert']
        assert ablauf==f['erwarteter_ablauf']
        assert frueh==f['erwarteter_fruehester_zieltag']
        assert (f['zieltag_am']>=frueh)==f['erwartung']
