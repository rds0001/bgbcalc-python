import json
from pathlib import Path
import bgbcalc

def test_darlehen493_waehrung_normanwendung():
    faelle=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/darlehen493_waehrung_normanwendung.json').read_text())
    for f in faelle:
        bedingungen=[]
        for i,betrag in enumerate(['1000','100']):
            werte=bgbcalc.immobiliardarlehen_wechselkursrechnung(betrag,'1',f['kurs'],f['kurs'],f['nachweis'])['wert']
            assert werte['wert_zum_vergleichskurs']==f['vergleichswerte'][i]
            warnung=bgbcalc.immobiliardarlehen_wechselkurswarnschwelle(werte['wert_zum_vertragskurs'],werte['wert_zum_vergleichskurs'],f['vorher'],f['nachweis'])['wert']
            bedingungen.append(warnung['numerische_warnbedingung'])
        assert any(bedingungen)==f['erwartung']
