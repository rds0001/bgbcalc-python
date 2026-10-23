import json
from datetime import date,timedelta
from pathlib import Path
import bgbcalc as b

def test_zahlung675y_wertstellung():
    d=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/zahlung675y_wertstellung_normanwendung.json').read_text());h=d['nachweis'];kal=d['bankkalender']
    zugang=b.zahlungsauftrag_zugangstage('2024-06-03',False,None,kal,h)['wert']['zugangstag_fuer_ausfuehrungsfrist']
    for f in d['faelle']:
        soll=b.zahlung_ausfuehrungsfristende(zugang,f['fristfall'],None,kal,h)['wert']['spaetester_eingangstag']
        assert soll==f['soll']
        vergleich=b.zahlung_gutschrift_wertstellung(soll,'2024-06-10',h)['wert']
        assert vergleich['wertstellungsgrenze_eingehalten'] is False
        assert vergleich['spaetestes_wertstellungsdatum']==soll
        letzter=(date.fromisoformat('2024-06-10')-timedelta(days=1)).isoformat()
        tage=b.zinskalendertage_nach_ausschluss(soll,letzter,[],h)['wert']['verzinsliche_kalendertage']
        assert tage==f['tage']
        zins=b.gesetzliche_zinsen('1000',tage,366,h,False,'3.66')['wert']
        assert zins==f['zins']
