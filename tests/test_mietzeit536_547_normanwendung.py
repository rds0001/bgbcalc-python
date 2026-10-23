import json
from pathlib import Path
from datetime import date
from fractions import Fraction
import bgbcalc

def test_mietzeit536_547_normanwendung():
    d=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/mietzeit536_547_normanwendung.json').read_text());h=d['nachweis']
    summe=Fraction(0);letzter=None
    for f in d['minderung']:
        von=date.fromisoformat(f['von']);bis=date.fromisoformat(f['bis'])
        assert letzter is None or von>letzter
        letzter=bis;tage=(bis-von).days+1
        assert tage==f['tage']
        wert=bgbcalc.miete_zeitanteiliger_minderungsbetrag(f['monatsmiete'],f['quote'],{'zaehler':str(tage),'nenner':'31'},h)['wert']
        assert wert==f['betrag'];summe+=Fraction(int(wert['zaehler']),int(wert['nenner']))
    assert summe==200
    ausschluss=bgbcalc.fristende('2024-08-17',3,'monate','tagesbeginn')['wert']
    assert ausschluss=='2024-11-16'
    assert bgbcalc.fristverlaengerung(ausschluss,1,'tage')['wert']=='2024-11-17'
    tage=(date(2024,2,29)-date(2024,2,10)).days
    rueck=bgbcalc.mietvorauszahlung_zeitanteilige_rueckerstattung('290',{'zaehler':str(tage),'nenner':'29'},h)['wert']
    assert rueck=={'zaehler':'190','nenner':'1'}
    zinstage=(date(2024,7,1)-date(2024,1,1)).days
    assert bgbcalc.gesetzliche_zinsen(rueck,zinstage,366,h+' Empfang zu Tagesbeginn1.1.;Actual/Actual fuer diesen Abschnitt.',False,None)['wert']=={'zaehler':'3458','nenner':'915'}
    assert bgbcalc.bereicherung_entreicherungsrest(rueck,'40',h+' Nicht zu vertretende Beendigung und Entreicherung40 rechtlich festgestellt.')['wert']=={'zaehler':'150','nenner':'1'}
