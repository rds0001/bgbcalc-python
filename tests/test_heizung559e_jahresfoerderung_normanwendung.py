import json
from pathlib import Path
import bgbcalc as b

def test_heizung559e_jahresfoerderung_normanwendung():
    f=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/heizung559e_jahresfoerderung_normanwendung.json').read_text())
    h='559e-Fördertatbestand sowie559aII-Jahresabzugsmethode im konkreten Fall ausdrücklich rechtlich qualifiziert; Reihenfolge gegenüber Kappung vorgegeben.'
    zins=b.modernisierung_zinsermaessigung(f['darlehen'],f['ermaessigt'],f['markt'],h,True,False)['wert']
    kap=b.modernisierung_kappungsgrenze(f['wohnflaeche'],'8','0','0','heizung_559e',True)['wert']['massgebliche_restgrenze']
    assert zins==dict(zaehler=f['zinsvorteil'],nenner='1')
    assert kap==dict(zaehler=f['kappung'],nenner='1')
    for s in f['faelle']:
        r=b.heizungsmodernisierung_mit_jahresfoerderung('10000','0','0',zins,'20',kap,s['methode'],h)['wert']['foerderkappung']
        assert r['monatlicher_betrag_nach_vorgegebener_methode']==dict(zaehler=s['monat'],nenner='1')
