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
    from bgbcalc.zahlen import _subtrahieren, _zahleneingabe, _bruch
    begrenzt = _subtrahieren(_bruch(80), _zahleneingabe(ergebnisse['2187_GRENZE']))
    assert begrenzt == _bruch(50)
    assert _subtrahieren(begrenzt, _zahleneingabe(ergebnisse['2322_LAST_20']['kuerzungsbetrag'])) == _bruch(30)
    return len(faelle)

def test_untervermaechtnis_deckung():
    pruefe_faelle(Path(__file__).resolve().parents[1] / 'tests/fixtures/kompositionsfaelle/untervermaechtnis_deckung.json')

if __name__ == '__main__':
    import sys
    print(pruefe_faelle(sys.argv[1]), 'Python Normanwendungen PASS')
