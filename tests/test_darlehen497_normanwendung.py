import json
from pathlib import Path
import bgbcalc as b

def test_darlehen497_normanwendung():
    d=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/darlehen497_normanwendung.json').read_text())
    for f in d['faelle']:
        intervall=b.darlehen_verzugshemmungszeitraum('2020-01-01','2021-01-01',f['feststellung'],f['betrachtung'],d['nachweis'])['wert']
        assert intervall['zehnjahresgrenze']=='2030-01-01'
        ende=b.verjaehrung_gehemmte_kalendertage('2021-01-01','2023-12-31',intervall['hemmungszeitraeume'],True)['wert']
        assert ende==dict(rechnerischer_letzter_tag='2024-01-10',beruecksichtigte_hemmungstage=10)
