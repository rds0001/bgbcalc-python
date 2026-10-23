import json
from pathlib import Path
import bgbcalc as b

def test_hoehere_gewalt_verweis_normanwendung():
    faelle=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/hoehere_gewalt_verweis_normanwendung.json').read_text())
    for f in faelle:
        grund=getattr(b,f['funktion'])(**f['eingaben'])['wert'][f['ergebnisschluessel']]
        assert grund==f['grundende']
        r=b.verjaehrung_hoehere_gewalt_festes_ablauffenster(f['erster'],grund,[dict(erster_verhinderter_tag=f['hindernis_von'],letzter_verhinderter_tag=f['hindernis_bis'])],'fester_ablauf_ohne_206','letzter_monatstag','Festes Fenster und188III-Analogie für diesen Fall rechtlich begründet.')['wert']
        assert r['beruecksichtigte_hemmungstage']==f['tage']
        assert r['rechnerischer_letzter_tag']==f['ende']
        if f['fall']=='1762II':
            s=b.verjaehrung_ablaufhemmung_mindestablauf('vertretungsmangel',[dict(ereignis='vertretungsmangel_behoben',datum='2022-02-01')],1,'jahre',r['rechnerischer_letzter_tag'],False,True)
            assert s['wert']['rechnerischer_letzter_tag']=='2022-08-01'
    alterswarteende=b.fristende('2020-01-01',8,'wochen','tagesbeginn')['wert']
    assert alterswarteende=='2020-02-25'
    assert b.fristende('2020-02-26',1,'jahre','tagesbeginn')['wert']=='2021-02-25'
    a=b.adoption_aufhebungsgrundfrist('2020-02-01',alterswarteende,'1762IId:Frist ab Ablauf der1747II-Alterswartezeit,bei relativer Ereignisberechnung deren Ablauftag verwenden.')
    assert a['wert']['antragsgrundfristende']=='2021-02-25'


def test_adoption1762_getrennte_fristlaeufe():
    d=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/adoption1762_getrennte_fristlaeufe.json').read_text())
    enden=[]
    for f in d['fristen']:
        grund=b.fristende(f['ereignis'],f['jahre'],'jahre','ereignis')['wert']
        assert grund==f['grundende']
        r=b.verjaehrung_hoehere_gewalt_festes_ablauffenster(f['erster'],grund,[dict(erster_verhinderter_tag=d['hemmung_von'],letzter_verhinderter_tag=d['hemmung_bis'])],'fester_ablauf_ohne_206','letzter_monatstag','Getrennte1762-Fristläufe, festes206-Modell qualifiziert.')['wert']['rechnerischer_letzter_tag']
        assert r==f['nach206']
        s=b.verjaehrung_ablaufhemmung_mindestablauf('vertretungsmangel',[dict(ereignis='vertretungsmangel_behoben',datum=d['vertretungsmangel_behoben'])],f['jahre'],'jahre',r,False,True)['wert']['rechnerischer_letzter_tag']
        assert s==f['nach210']
        enden.append(s)
    assert min(enden)==d['kombiniertes_ende']
