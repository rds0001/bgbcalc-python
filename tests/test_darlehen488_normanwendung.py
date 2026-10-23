import json
from pathlib import Path
import bgbcalc

def test_darlehen488_normanwendung():
    d=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/darlehen488_normanwendung.json').read_text())
    for f in d['kalender']:
        jahr=bgbcalc.fristende(f['beginn'],1,'jahre','ereignis')['wert']
        assert jahr==f['jahresende']
        nach_jahr=bgbcalc.fristverlaengerung(jahr,1,'tage')['wert']
        assert min(f['rueckzahlung'],nach_jahr)==f['zahlungstag']
    for f in d['zinsen']:
        assert bgbcalc.gesetzliche_zinsen(f['kapital'],f['zaehler'],f['nenner'],d['nachweis'],False,f['zinssatz'])['wert']==f['erwartung']
