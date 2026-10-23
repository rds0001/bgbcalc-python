import json
from pathlib import Path
import bgbcalc as b

def test_unterhalt1607_1609_normanwendung():
    d=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/unterhalt1607_1609_normanwendung.json').read_text());h=d['nachweis']
    primaer=b.unterhalt_rangweise_mittelverteilung('100',d['berechtigte'],h)['wert']
    rest=primaer['verteilung'][0]['ungedeckter_restbedarf']
    assert rest==dict(zaehler='75',nenner='1')
    ersatz=b.unterhalt_anteile_mit_leistungsgrenzen(rest,d['ersatzpflichtige'],h)['wert']
    assert [p['beibringbarer_unterhaltsbetrag'] for p in ersatz['verteilung']]==[dict(zaehler='20',nenner='1'),dict(zaehler='55',nenner='1')]
    assert ersatz['ungedeckter_barunterhalt']==dict(zaehler='0',nenner='1')
