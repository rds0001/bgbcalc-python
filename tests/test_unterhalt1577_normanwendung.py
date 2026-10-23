import json
from pathlib import Path
import bgbcalc

def test_unterhalt1577_normanwendung():
    for f in json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/unterhalt1577_normanwendung.json').read_text()):
        zwischen=bgbcalc.unterhalt_unterschiedsbetrag(f['voller_bedarf'],f['anrechenbare_vermoegensdeckung'],f['nachweis'])['wert']
        assert zwischen==f['zwischen']
        rest=bgbcalc.unterhalt_unterschiedsbetrag(zwischen,f['anrechenbare_einkuenfte'],f['nachweis'])['wert']
        assert rest==f['rest']
