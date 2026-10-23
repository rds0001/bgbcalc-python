import json
from pathlib import Path
import bgbcalc

def test_baunachtrag650c_normanwendung():
    d=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/baunachtrag650c_normanwendung.json').read_text())
    h=d['nachweis']
    assert bgbcalc.bau_nachtragsverguetung_differenz('0','0','100','50',h)['wert']=={'zaehler':'-150','nenner':'1'}
    for f in d['ketten']:
        endgueltig=bgbcalc.bau_nachtragsverguetung_differenz('1000','200','300','50',h)['wert']
        assert endgueltig=={'zaehler':'850','nenner':'1'}
        abschlag=bgbcalc.bau_nachtrag_vorlaeufiger_abschlagsansatz('2000',h)['wert']
        assert abschlag=={'zaehler':'1600','nenner':'1'}
        rueck=bgbcalc.bau_nachtrag_ueberzahlungsbetrag(abschlag,endgueltig,h)['wert']
        assert rueck=={'zaehler':'750','nenner':'1'}
        z=bgbcalc.verzugszinsen(kapital=rueck,basiszinssatz_prozent='3',zeitanteil_zaehler=1,zeitanteil_nenner=2,zeitanteil_nachweis=h,entgeltforderung=True,verbraucher_beteiligt=f['verbraucher'],zinsschuld=False,glaeubigerverzug=False,verzugsart='allgemein',hoeherer_zinssatz_prozent=None,basiszinsnachweis='Expliziter Testzinssatz, keine Behauptung eines aktuellen Basiszinssatzes.')
        assert z['wert']==f['zinsen']
