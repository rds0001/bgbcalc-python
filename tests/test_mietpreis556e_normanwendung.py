import json
from pathlib import Path
import bgbcalc as b

def test_mietpreis556e_normanwendung():
    faelle=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/mietpreis556e_normanwendung.json').read_text())
    h='Zeitlich und sachlich qualifizierter556e-Fall, ohne laufende Förderabzüge stimmen beide Reihenfolgen überein.'
    vormiete=b.mietpreisbegrenzung_vormiete_bereinigen('900','100',['50','25'],h)['wert']['bereinigte_vormiete']
    grund=b.mietpreisbegrenzung_grundbetrag('820',True,False,h)['wert']
    vormietweg=b.mietpreisbegrenzung_vormietgrenze(grund,vormiete,True,h)['wert']
    ohne=b.mietpreisbegrenzung_grundbetrag('800',True,False,h)['wert']
    jahr=b.modernisierung_regulaerer_zwischenbetrag('12000','2000','1000','0','0',True)['wert']['jahresbetrag_vor_laufenden_abzuegen']
    for f in faelle:
        kap=b.modernisierung_kappungsgrenze('50','16',f['vorherige_erhoehung'],'0','allgemein',True)['wert']['massgebliche_restgrenze']
        z=b.modernisierung_kappung_mit_laufenden_abzuegen(jahr,'0','0',kap,'abzug_vor_kappung',h)['wert']['monatlicher_betrag_nach_vorgegebener_methode']
        assert z==dict(zaehler=f['zuschlag'],nenner='1')
        r=b.mietpreisbegrenzung_modernisierungsalternative(vormietweg,ohne,z,f['privileg'],h)
        assert r['wert']['nutzbare_monatsgrenze']==dict(zaehler=f['grenze'],nenner='1')
