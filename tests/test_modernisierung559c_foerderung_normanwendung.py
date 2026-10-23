import json
from pathlib import Path
import bgbcalc as b
from bgbcalc.zahlen import _zahleneingabe,_multiplizieren,_bruch
from bgbcalc.zinsen import _bruchteile

def test_modernisierung559c_foerderung_normanwendung():
    faelle=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/modernisierung559c_foerderung_normanwendung.json').read_text())
    h='559c/559a-Methoden rechtlich begründet, einmalige und laufende Förderung getrennt. Zinsermäßigung nach559cI3nicht abzugsfähig.'
    for f in faelle:
        basis=b.modernisierung_vereinfachte_foerderkostenbasis('10000','0','2000',f['kostenmethode'],h)['wert']['ausgewaehlte_kostenbasis']
        jahr=_bruchteile(_multiplizieren(_zahleneingabe(basis),_bruch(2,25)))
        kap=b.modernisierung_kappungsgrenze('50','8',f['bisher'],'0','allgemein',True)['wert']['massgebliche_restgrenze']
        wert=b.modernisierung_kappung_mit_laufenden_abzuegen(jahr,'0','120',kap,f['abzugsreihenfolge'],h)['wert']
        assert wert['monatlicher_betrag_nach_vorgegebener_methode']==f['erwartet']
