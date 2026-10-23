import json
from pathlib import Path
import bgbcalc

def test_alkohol_liefergrenze_normanwendung():
    faelle=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/alkohol_liefergrenze_normanwendung.json').read_text())
    for f in faelle:
        grenze=bgbcalc.fristende(f['vertragsschluss_am'],30,'tage','ereignis')['wert']
        assert grenze==f['erwartete_grenze']
        assert (f['fruehestmoegliche_lieferung_am']>=grenze)==f['erwartung']
