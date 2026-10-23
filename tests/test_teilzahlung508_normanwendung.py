import json
from pathlib import Path
import bgbcalc

def test_teilzahlung508_normanwendung():
    for f in json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/teilzahlung508_normanwendung.json').read_text()):
        r=bgbcalc.verbraucherdarlehen_verzugsschwelle(**f['rueckstand_eingaben'],nennbetrag=f['gesamtbetrag'],immobiliar_verbraucherdarlehen=False,teilzahlungsdarlehen=True)
        assert r['status']=='BERECHNET'
        assert r['wert']['rueckstandsquote']==f['erwartete_quote']
        assert r['wert']['mindestrueckstand']==f['erwarteter_mindestrueckstand']
        assert r['wert']['voraussetzungen_nummer_1_erfuellt'] is f['erwartete_nummer1']
        n=bgbcalc.verbraucherdarlehen_kuendigungsnachfrist(**f['nachfrist_eingaben'])
        assert n['status']=='BERECHNET'
        assert n['wert']['rechnerisches_mindestende']==f['erwartetes_mindestende']
        assert n['wert']['nachfrist_am_prueftag_abgelaufen'] is True
