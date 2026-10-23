"""Zusätzliche lokale Buch5-Normanwendungsbelege; keine neuen Produktions-APIs."""
import json
from pathlib import Path
import bgbcalc

def pruefe_faelle(pfad):
    faelle = json.loads(Path(pfad).read_text())
    ergebnisse = {}
    for fall in faelle:
        ergebnis = getattr(bgbcalc, fall['funktion'])(**fall['eingaben'])
        ergebnisse[fall['fall_id']] = ergebnis['wert']
        assert ergebnis['status'] == 'BERECHNET', fall['fall_id']
        wert = ergebnis['wert']
        for teil in fall['wertpfad']:
            wert = wert[teil]
        assert wert == fall['erwartet'], (fall['fall_id'], wert, fall['erwartet'])
    assert ergebnisse['2327_nur_eigengeschenk']['ordentlicher_pflichtteil'] == {'zaehler':'25','nenner':'1'}
    assert ergebnisse['2327_nur_eigengeschenk']['pflichtteilsergaenzung'] == {'zaehler':'35','nenner':'1'}
    return len(faelle)

def test_eigengeschenk_mehrhinterlassung():
    pruefe_faelle(Path(__file__).resolve().parents[1] / 'tests/fixtures/kompositionsfaelle/eigengeschenk_mehrhinterlassung.json')

if __name__ == '__main__':
    import sys
    print(pruefe_faelle(sys.argv[1]), 'Python Normanwendungen PASS')
