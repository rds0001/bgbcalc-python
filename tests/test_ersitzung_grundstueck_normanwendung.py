import json
from pathlib import Path
import bgbcalc

def test_ersitzung_grundstueck_normanwendung():
    for f in json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/ersitzung_grundstueck_normanwendung.json').read_text()):
        k=bgbcalc.ersitzung_anrechenbare_zeitkette(**f['ketten_eingaben'])
        assert k['status']=='BERECHNET'
        assert k['wert']['rechnerisches_fristende']==f['erwartetes_besitzende']
        if f['art']=='buchersitzung_900':
            r=bgbcalc.buchersitzung_dreissigjahresfrist(eintragung_am='1994-01-31',besitzbeginn_am='1994-01-31',beginnart='ereignis',rechtsart='eigentum',korrigiertes_fristende=k['wert']['rechnerisches_fristende'],prueftag='2024-02-29',zusammenhaengender_zeitraum_qualifiziert=True,einordnungsnachweis=f['ketten_eingaben']['einordnungsnachweis'])
            assert r['status']=='BERECHNET'
            ende=r['wert']['massgebliches_fristende']
        else:
            r=bgbcalc.grundstuecksaufgebot_kombinierte_zeitgrenze(berechnetes_eigenbesitzfristende=k['wert']['rechnerisches_fristende'],letzte_massgebliche_zustimmungseintragung_am='1995-02-28',einordnungsnachweis=f['ketten_eingaben']['einordnungsnachweis'])
            assert r['status']=='BERECHNET'
            ende=r['wert']['rechnerische_kombinierte_zeitgrenze']
        assert ende==f['erwartete_endgrenze']
