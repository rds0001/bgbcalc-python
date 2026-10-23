import json
from pathlib import Path
import bgbcalc

def test_gesellschaft_jahresabschluss_normanwendung():
    for f in json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/gesellschaft_jahresabschluss_normanwendung.json').read_text()):
        datum=bgbcalc.fristende(**f['kalender_eingaben'])
        assert datum['status']=='BERECHNET'
        assert datum['wert']==f['erwarteter_abschluss'],f['fall_id']
        betraege=bgbcalc.gesellschaft_gewinn_verlust_betraege(**f['betrag_eingaben'])
        assert betraege['status']=='BERECHNET'
        assert [p['ergebnisanteil'] for p in betraege['wert']]==f['erwartete_betraege'],f['fall_id']
