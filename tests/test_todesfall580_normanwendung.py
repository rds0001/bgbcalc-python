import json
from datetime import date
from pathlib import Path
import bgbcalc

def test_todesfall580_normanwendung():
    for f in json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/todesfall580_normanwendung.json').read_text()):
        warte=bgbcalc.schuldrechtliche_sondergrundfrist(**f['warte_eingaben'])
        assert warte['status']=='BERECHNET'
        assert warte['wert']['rechnerisches_fristende']==f['erwartetes_warteende'],f['fall_id']
        assert '2024-01-31' <= f['zugang_am'] <= warte['wert']['rechnerisches_fristende']
        ende=getattr(bgbcalc,f['funktion'])(**f['kuendigungs_eingaben'])
        assert ende['status']=='BERECHNET'
        assert ende['wert'][f['ergebnisfeld']]==f['erwartetes_ende'],f['fall_id']
        if f['funktion']=='wohnraummiete_kuendigungstermin':
            assert ende['wert']['verlaengerungsmonate']==0
