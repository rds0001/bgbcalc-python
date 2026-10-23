import json
from pathlib import Path
import bgbcalc as b

def test_schuldverschreibung802_801_normanwendung():
    faelle=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/schuldverschreibung802_801_normanwendung.json').read_text())
    h='Qualifizierte801III-Urkundenbestimmung und802/206-Verknüpfung; festes Fenster rechtlich bestimmt.'
    vorgrund=b.fristende('2024-01-01',1,'jahre','tagesbeginn')['wert']
    assert vorgrund=='2024-12-31'
    sechs=b.schuldrechtliche_sondergrundfrist('schuldverschreibung_zahlungssperre_802','2024-01-01',h)['wert']['rechnerisches_fristende']
    assert sechs=='2024-07-01'
    korr=b.verjaehrung_hoehere_gewalt_festes_ablauffenster('2024-01-02',sechs,[dict(erster_verhinderter_tag='2024-06-25',letzter_verhinderter_tag='2024-07-05')],'fester_ablauf_ohne_206','letzter_monatstag',h)['wert']['rechnerischer_letzter_tag']
    assert korr=='2024-07-08'
    for f in faelle:
        intervalle=b.schuldverschreibung_zahlungssperre_intervall('2024-01-01',True,korr,None,f['erledigung'],'2024-08-01',h)['wert']
        assert intervalle['hemmung_bis_beobachtung_abgeschlossen'] is True
        assert intervalle['feststehendes_hemmungsende']==f['hemmungsende']
        vor=b.verjaehrung_gehemmte_kalendertage('2024-01-01',vorgrund,intervalle['hemmungszeitraeume'],True)['wert']
        assert vor['beruecksichtigte_hemmungstage']==f['tage']
        assert vor['rechnerischer_letzter_tag']==f['vorlegungsende']
        assert b.fristende(vor['rechnerischer_letzter_tag'],2,'jahre','ereignis')['wert']==f['verjaehrungsende']
