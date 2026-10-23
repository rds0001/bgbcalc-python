import json
from pathlib import Path
import bgbcalc as b

def test_widerruf356f_normanwendung():
    d=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/widerruf356f_normanwendung.json').read_text())
    h='Unterrichtung tatsächlich vollständig ausgeblieben, kein erfundenes Regelfristende.'
    ende=b.widerruf_hoechstfristende('unentgeltliches_darlehen_ohne_unterrichtung_356f',[d['vertrag']],h)['wert']['hoechstfristende_ohne_kalenderkorrektur']
    assert ende==d['hoechstende']
    r=b.widerruf_fristenden_zusammenfuehren(None,ende,h)['wert']
    assert r['rechnerisch_bestimmbares_ende']==d['hoechstende']
    assert r['regelfristende_vorhanden'] is False
    assert r['hoechstfristende_vorhanden'] is True
