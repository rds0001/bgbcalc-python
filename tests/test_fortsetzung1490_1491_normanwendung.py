import json
from pathlib import Path
import bgbcalc

def test_fortsetzung1490_1491_normanwendung():
    for f in json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/fortsetzung1490_1491_normanwendung.json').read_text()):
        wert=bgbcalc.fortgesetzte_guetergemeinschaft_grundanteile('1200',f['abkoemmlinge'],f['nachweis'])['wert']
        assert wert['ehegattenhaelfte']=={'zaehler':'600','nenner':'1'}
        assert wert['abkoemmlingshaelfte']=={'zaehler':'600','nenner':'1'}
        assert wert['abkoemmlingsanteile']==f['erwartete_anteile']
