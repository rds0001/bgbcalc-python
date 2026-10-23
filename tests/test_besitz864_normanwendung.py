import json
from pathlib import Path
import bgbcalc as b

def test_besitz864_normanwendung():
    faelle=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/besitz864_normanwendung.json').read_text())
    ende=b.sachenrechtliche_grundfrist('besitzschutz_864','2024-05-10','Qualifizierte verbotene Eigenmacht, gesetzliches Grundjahr.')['wert']['grundfristende']
    assert ende=='2025-05-10'
    for f in faelle:
        klage_wahrt=f['klage_am'] is not None and f['klage_am']<=ende
        jahresablauf=f['prueftag']>ende and not klage_wahrt
        urteil=f['rechtskraft_am'] is not None and f['rechtskraft_am']<f['prueftag']
        assert (jahresablauf or urteil)==f['erloschen']
