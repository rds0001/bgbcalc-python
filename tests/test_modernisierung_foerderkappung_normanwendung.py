import json
from pathlib import Path
import bgbcalc

def test_modernisierung_foerderkappung_normanwendung():
    br=lambda x:dict(zaehler=x,nenner='1')
    for f in json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/modernisierung_foerderkappung_normanwendung.json').read_text()):
        zins=bgbcalc.modernisierung_zinsermaessigung('6000','3','5','Synthetischer Vergleichszins, kein aktueller Marktwert.',True,False)['wert']
        assert zins==br('120')
        basis=bgbcalc.modernisierung_regulaerer_zwischenbetrag('10000','2000','1000',zins,'0',True)['wert']
        assert basis['jahresbetrag_vor_laufenden_abzuegen']==br('560')
        kap=bgbcalc.modernisierung_kappungsgrenze(f['wohnflaeche'],f['altmiete_je_qm'],f['bisherige_erhoehung'],'0',f['erhoehungsart'],True)['wert']['massgebliche_restgrenze']
        assert kap==br(f['restkappung'])
        for modus,erwartet in [('abzug_vor_kappung',f['betrag_vor']),('abzug_nach_kappung',f['betrag_nach'])]:
            ergebnis=bgbcalc.modernisierung_kappung_mit_laufenden_abzuegen(basis['jahresbetrag_vor_laufenden_abzuegen'],zins,'0',kap,modus,'Synthetische explizite Methodenwahl; kein allgemeiner Rechtsauslegungsbeleg.')['wert']
            assert ergebnis['monatlicher_betrag_nach_vorgegebener_methode']==br(erwartet)
