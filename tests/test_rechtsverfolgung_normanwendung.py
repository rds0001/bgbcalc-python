import json
from pathlib import Path
import bgbcalc

def test_rechtsverfolgung_normanwendung():
    for f in json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/rechtsverfolgung_normanwendung.json').read_text()):
        grund=bgbcalc.rechtsverfolgung_sondergrundfrist(**f['grund_eingaben'])
        assert grund['status']=='BERECHNET'
        assert grund['wert']['rechnerisches_fristende']==f['erwartetes_grundende']
        schutz=bgbcalc.verjaehrung_ablaufhemmung_mindestablauf(**f['schutz_eingaben'],rechnerischer_letzter_tag=grund['wert']['rechnerisches_fristende'])
        assert schutz['status']=='BERECHNET'
        assert schutz['wert']['nachlauf_kuerzer_als_sechs_monate'] is True
        assert schutz['wert']['rechnerischer_letzter_tag']==f['erwartetes_ende'],f['fall_id']
