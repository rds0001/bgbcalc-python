import json
from pathlib import Path
import bgbcalc as b

def test_schenkung528_529_normanwendung():
    faelle=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/schenkung528_529_normanwendung.json').read_text())
    for f in faelle:
        a=b.schenkung_verarmungsrueckforderung_ausschluss(f['geschenk_am'],'2024-01-31',False,False,'Qualifizierte Leistung und Bedürftigkeit.')['wert']['rueckforderung_nach_529_absatz_eins_oder_534_ausgeschlossen']
        assert a is f['ausgeschlossen']
        p=[dict(beschenkten_id='alt',schenkungsrang=1,bereicherungsgrenze='0' if a else '200',leistungsfaehigkeitsgrenze='200'),dict(beschenkten_id='jung',schenkungsrang=2,bereicherungsgrenze='100',leistungsfaehigkeitsgrenze='40')]
        r=b.schenkung_unterhaltsrueckforderung('200','50',p,'Geldrückforderung, gleicher Zeitraum, qualifizierte Rangfolge und529II-Grenzen.')['wert']
        assert [x['rueckforderungsbetrag'] for x in r['verteilung']]==[dict(zaehler='40',nenner='1'),dict(zaehler=f['altbetrag'],nenner='1')]
        assert r['ungedeckter_fehlbetrag']==dict(zaehler=f['rest'],nenner='1')
