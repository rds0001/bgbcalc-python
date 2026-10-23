import json
from pathlib import Path
import bgbcalc as b

def test_vergleichsmiete558_normanwendung():
    f=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/vergleichsmiete558_normanwendung.json').read_text())
    h='558IV/V: Bindungswegfall zu Tagesbeginn und Rückwärtsmethode qualifiziert; Auskunftszugang und alternativ wirkende Ausgleichszahlung rechtlich vorgegeben.'
    grenze=b.rueckwaertsfrist_kalendergrenze(f['wegfall'],4,'monate','ereignistag','nur_taggleiche_monate',h)['wert']['grenztag_beginn']
    assert grenze==f['frueheste_anfrage']
    assert '2024-08-31'<grenze<='2024-09-01'
    assert b.schuldrechtliche_sondergrundfrist('miete_ausgleichszahlung_auskunft_558',grenze,h)['wert']['rechnerisches_fristende']==f['antwortfrist']
    zins=b.modernisierung_zinsermaessigung('3000','1','3',h,True,False)['wert']
    assert zins==dict(zaehler=f['zinsvorteil'],nenner='1')
    r=b.vergleichsmiete_ausgleich_und_drittmittel('500','0','500','900',False,'1500',zins,'60','150','alternative_erhoehungsgrenze',h)['wert']
    assert r['monatsmiete_nach_vorgegebenem_modell']==dict(zaehler=f['neue_monatsmiete'],nenner='1')
