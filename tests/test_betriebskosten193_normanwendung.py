import json
from pathlib import Path
import bgbcalc

def test_betriebskosten193_normanwendung():
    for f in json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/betriebskosten193_normanwendung.json').read_text()):
        ende=bgbcalc.betriebskosten_grundfristende(f['fristfall'],f['bezugsdatum'],f['fristberechnung'],f['nachweis'])['wert']['rechnerisches_fristende']
        assert ende==f['grundfrist']
        korrigiert=bgbcalc.werktagsverschiebung(ende,'willenserklaerung',f['feiertage'],'Testort','Expliziter Kalender fuer die betroffenen Folgetage; keine weiteren einschlaegigen Feiertage.','2023-01-01','2024-01-02')['wert']
        assert korrigiert==f['korrigiert']
