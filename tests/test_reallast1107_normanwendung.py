import json
from pathlib import Path
import bgbcalc as b

def test_reallast1107_normanwendung():
    faelle=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/reallast1107_normanwendung.json').read_text())
    for f in faelle:
        r=b.hypothek_folgequartalsgrenze(f['kenntnis'],f['faelligkeit'],'uebertragungskenntnis_1158',True,'1107 entsprechend anwendbare1158-Regel für einzelne Reallastleistung; Kenntnis und Fälligkeit qualifiziert.')
        assert r['status']=='BERECHNET'
        assert r['wert']==dict(folgequartalsende=f['grenze'],faelligkeit_nach_folgequartal=not f['erfuellt'],zeitmerkmal_erfuellt=f['erfuellt'])
