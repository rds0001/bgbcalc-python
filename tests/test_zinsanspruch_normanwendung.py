import json
from pathlib import Path
import bgbcalc

def test_zinsanspruch_normanwendung():
    for f in json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/zinsanspruch_normanwendung.json').read_text()):
        erster=f['erster_zinstag']
        if f['beginn_eingaben'] is not None:
            beginn=bgbcalc.prozesszins_erster_zinstag(**f['beginn_eingaben'])
            assert beginn['status']=='BERECHNET',f['fall_id']
            erster=beginn['wert']['erster_prozesszinstag']
            assert erster==f['erster_zinstag'],f['fall_id']
        zeiten=bgbcalc.zinskalendertage_nach_ausschluss(erster_betrachteter_tag=erster,letzter_betrachteter_tag=f['letzter_zinstag'],ausschlusszeitraeume=[],einordnungsnachweis=f['einordnungsnachweis'])
        assert zeiten['status']=='BERECHNET',f['fall_id']
        tage=zeiten['wert']['verzinsliche_kalendertage']
        assert tage==f['tage'],f['fall_id']
        eingaben=dict(kapital='3650',zeitanteil_zaehler=tage,zeitanteil_nenner=365,zeitanteil_nachweis=f['einordnungsnachweis'],glaeubigerverzug=False)
        if f['funktion']=='verzugszinsen':
            eingaben.update(basiszinssatz_prozent='3',basiszinsnachweis='Synthetischer konstanter Basiszins für dieses Beispiel',entgeltforderung=True,verbraucher_beteiligt=f['verbraucher_beteiligt'],zinsschuld=f['zinsschuld'],verzugsart='allgemein',hoeherer_zinssatz_prozent=None)
        else:
            eingaben['abweichender_zinssatz_prozent']=None
        ergebnis=getattr(bgbcalc,f['funktion'])(**eingaben)
        assert {k:ergebnis[k] for k in ('status','wert')}==f['erwartung'],f['fall_id']
