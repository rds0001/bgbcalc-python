import json
from pathlib import Path
import bgbcalc

def test_reiseverjaehrung_normanwendung():
    faelle=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/reiseverjaehrung_normanwendung.json').read_text())
    for f in faelle:
        ergebnis=bgbcalc.fristende(f['vertragliches_reiseende_am'],2,'jahre','tagesbeginn')
        assert ergebnis['wert']==f['erwartetes_grundfristende'],f['fall_id']
