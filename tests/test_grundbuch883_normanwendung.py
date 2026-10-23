import json
from pathlib import Path
import bgbcalc as b

def test_grundbuch883_normanwendung():
    f=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/grundbuch883_normanwendung.json').read_text())
    h='883III: maßgeblicher Eintragungsrang der rechtlich zugeordneten Vormerkung, keine automatische Auslegung des gesicherten Anspruchs.'
    assert b.grundbuch_rangpaarvergleich(f['vormerkung'],f['anderes_recht'],h)['wert']['rangvergleich']==f['rangvergleich']
    spaet=dict(f['vormerkung'],eintragungstag=f['spaetere_rechtseintragung'])
    assert b.grundbuch_rangpaarvergleich(spaet,f['anderes_recht'],h)['wert']['rangvergleich']==1
    r=b.grundbuch_betraglicher_rangumfang('120','100','vormerkungsumfang_883',h)['wert']
    assert r['erfasster_rechtsteil']==dict(zaehler=f['erfasster_teil'],nenner='1')
    assert r['nicht_erfasster_rechtsteil']==dict(zaehler=f['restteil'],nenner='1')
