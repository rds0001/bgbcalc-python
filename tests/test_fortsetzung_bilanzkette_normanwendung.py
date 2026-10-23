import json
from pathlib import Path
import bgbcalc as b

def test_fortsetzung_bilanzkette():
    d=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/fortsetzung_bilanzkette_normanwendung.json').read_text());h=d['nachweis']
    def br(n):return dict(zaehler=str(n),nenner='1')
    alt=b.fortgesetzte_guetergemeinschaft_altlasten('200','100','0','0',h)['wert']['anrechnungspostensumme']
    assert alt==br(100)
    bilanz=b.fortsetzung_rechnerische_schlussbilanz('900','100',alt,'100',h)['wert']
    assert bilanz['ehegattensaldo']==br(500)
    assert bilanz['abkoemmlingssaldo_vor_abfindungsanrechnung']==br(500)
    assert bilanz['abkoemmlingssaldo']==br(400)
    aus=b.fortgesetzte_guetergemeinschaft_vorempfangsausgleich(bilanz['abkoemmlingssaldo_vor_abfindungsanrechnung'],d['abkoemmlinge'],h)['wert']
    assert [p['betrag'] for p in aus['verteilung']]==[br(225),br(275)]
    personen=[dict(abkoemmling_id=p['person_id'],grundanteilswert=p['betrag']) for p in aus['verteilung']]
    ende=b.fortsetzung_beguenstigtenbezogene_lasten(personen,d['lasten'],h)['wert']
    assert [p['rechnerischer_saldo'] for p in ende['abkoemmlingssalden']]==[br(125),br(275)]
    assert ende['rechnerische_saldosumme']==bilanz['abkoemmlingssaldo']
