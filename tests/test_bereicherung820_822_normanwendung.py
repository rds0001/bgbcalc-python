import json
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import bgbcalc as b

def test_bereicherung820_822_normanwendung():
    f=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/bereicherung820_822_normanwendung.json').read_text())
    h='820I/II qualifiziert; Zinsbeginn lokale Mitternacht,6%undActual/365 ausdrücklich rechtlich qualifiziert.'
    zeiten=b.bereicherung_haftungszeitpunkte('2023-01-01T00:00:00Z',None,None,True,True,f['kenntnis_utc'],h)['wert']
    start=datetime.fromisoformat(zeiten['zins_und_nutzungskenntnis_820_utc'].replace('Z','+00:00')).astimezone(ZoneInfo('Europe/Berlin'))
    assert start.hour==0 and start.minute==0
    tage=b.zinskalendertage_nach_ausschluss(start.date().isoformat(),f['letzter_zinstag'],[],h)['wert']['verzinsliche_kalendertage']
    assert tage==f['zinstage']
    assert b.gesetzliche_zinsen('1000',tage,365,h,False,'6')['wert']==f['zinsbetrag']
    h='822-Tatbestand und kausal ausgeschlossene Ersthaftung; getrennte818III-Entreicherung des Dritten rechtlich qualifiziert.'
    assert b.bereicherung_entreicherungsrest(f['ursprungsbetrag'],f['weitergabe'],h)['wert']==dict(zaehler=f['rest_empfaenger'],nenner='1')
    assert b.bereicherung_entreicherungsrest(f['weitergabe'],f['drittentreicherung'],h)['wert']==dict(zaehler=f['rest_dritter'],nenner='1')
