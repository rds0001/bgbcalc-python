import json
from pathlib import Path
import bgbcalc

def test_gesellschaft_fristketten():
    for f in json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/gesellschaft_fristketten.json').read_text()):
        if f['art']=='erbe':
            schutz=bgbcalc.verjaehrung_ablaufhemmung_mindestablauf(**f['schutz_eingaben'])
            assert schutz['status']=='BERECHNET'
            r=bgbcalc.gesellschaft_erbenrechtsfrist(erbschaftskenntnis_am='2024-01-31',ablaufhemmung_mindestende_am=schutz['wert']['rechnerischer_letzter_tag'],ausschlagungsrecht_bei_dreimonatsablauf_noch_offen=True,ausschlagungsfristende_am='2024-07-31',einordnungsnachweis=f['nachweis'])
            assert r['status']=='BERECHNET'
            ende=r['wert']['rechnerisches_ausuebungsfristende']
        elif f['art']=='hemmung':
            grund=bgbcalc.gesellschaft_fuenfjahresgrundfrist(fristfall='erloeschen_verjaehrung_739',ausscheiden_oder_erloeschen_am='2024-01-01',glaeubigerkenntnis_am='2024-01-31',registereintragung_am=None,einordnungsnachweis=f['nachweis'])
            assert grund['status']=='BERECHNET'
            r=bgbcalc.verjaehrung_gehemmte_kalendertage(fristlauf_erster_tag='2024-02-01',grundfrist_letzter_tag=grund['wert']['rechnerisches_fuenfjahresende'],hemmungszeitraeume=[dict(erster_gehemmter_tag='2024-03-01',letzter_gehemmter_tag='2024-03-31')],hemmung_nach_209_anwendbar=True)
            assert r['status']=='BERECHNET'
            assert r['wert']['beruecksichtigte_hemmungstage']==31
            ende=r['wert']['rechnerischer_letzter_tag']
        else:
            r=bgbcalc.verjaehrung_neubeginn_grundfrist(neubeginnereignis_am='2026-06-30',fristdauer=5,fristeinheit='jahre',wirksamer_neubeginn=True)
            assert r['status']=='BERECHNET'
            ende=r['wert']
            if f['art']=='neubeginn_kurz':
                kurz=bgbcalc.verjaehrung_neubeginn_grundfrist(neubeginnereignis_am='2026-06-30',fristdauer=3,fristeinheit='jahre',wirksamer_neubeginn=True)
                assert kurz['status']=='BERECHNET'
                ende=min(ende,kurz['wert'])
        assert ende==f['erwartetes_ende'],f['fall_id']
