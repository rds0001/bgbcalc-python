import json
from datetime import date,timedelta
from pathlib import Path
import bgbcalc as b

def test_fund973_977_normanwendung():
    d=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/fund973_977_normanwendung.json').read_text());h=d['nachweis']
    for f in d['faelle']:
        gross=b.fund_anzeigewertgrenze(f['sachenwert'])['wert']['wertgrenze_ueberschritten']
        ende=b.sachenrechtliche_grundfrist('fundanzeige_973' if gross else 'geringwertiger_fund_973',f['anzeige'] if gross else f['fund'],h)['wert']['grundfristende']
        assert ende==f['sechsmonatsende']
        erwerb=(date.fromisoformat(ende)+timedelta(days=1)).isoformat()
        assert erwerb==f['erwerb']
        ende977=b.fristende(erwerb,3,'jahre','tagesbeginn')['wert']
        assert ende977==f['dreijahresende']
        for geltendmachung in f['geltendmachungen']:
            assert (geltendmachung['am']<=ende977)==geltendmachung['rechtzeitig']
    for f in d['gesetzte_fristen']:
        erwerb=(date.fromisoformat(f['ende'])+timedelta(days=1)).isoformat()
        assert erwerb==f['erwerb']
        assert b.fristende(erwerb,3,'jahre','tagesbeginn')['wert']==f['dreijahresende']
