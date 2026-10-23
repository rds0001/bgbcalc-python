"""Numerische Kette: wirksame Ausschlusstage vereinigen, danach vorhandenen Zinskern nutzen."""
import json
from pathlib import Path
import bgbcalc

def test_zinsausschluss_normanwendung():
    faelle=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/zinsausschluss_normanwendung.json').read_text())
    for fall in faelle:
        zeiten=bgbcalc.zinskalendertage_nach_ausschluss(**fall['ausschluss_eingaben'])
        assert zeiten['status']=='BERECHNET'
        tage=zeiten['wert']['verzinsliche_kalendertage']
        assert tage==fall['erwartete_zinstage'],fall['fall_id']
        zins=bgbcalc.gesetzliche_zinsen(kapital='3650',zeitanteil_zaehler=tage,zeitanteil_nenner=365,zeitanteil_nachweis=fall['einordnungsnachweis'],glaeubigerverzug=False,abweichender_zinssatz_prozent=None)
        assert zins['status']=='BERECHNET'
        assert zins['wert']==fall['erwarteter_zins'],fall['fall_id']
