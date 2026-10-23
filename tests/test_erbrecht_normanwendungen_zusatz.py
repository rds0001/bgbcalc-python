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
    # Native Kernarithmetik: getrennte qualifizierte Anteilstitel bewahren.
    from bgbcalc.zahlen import _bruch, _addieren, _subtrahieren
    teile = {'ehegatte': _bruch(1, 2), 'verwandter': _bruch(1, 8)}
    assert _addieren(*teile.values()) == _bruch(5, 8)
    assert teile == {'ehegatte': _bruch(1, 2), 'verwandter': _bruch(1, 8)}
    assert _subtrahieren(_bruch(1, 3), _bruch(1, 4)) == _bruch(1, 12)
    # Absolute Ausschlussgrenze nach relativer Hemmung erneut anwenden.
    assert min(ergebnisse['1954_grund']['dreissigjahresgrenze'], ergebnisse['1954_ablaufhemmung']['rechnerischer_letzter_tag']) == '2024-04-01'
    ende = ergebnisse['2252_hemmung']['rechnerischer_letzter_tag']
    assert '2024-04-10' <= ende and '2024-04-11' <= ende and not '2024-04-12' <= ende
    assert ergebnisse['2189_stufe1']['nachrangiger_zuteilungsbetrag'] == {'zaehler': '60', 'nenner': '1'}
    assert ergebnisse['2189_stufe2']['nachrangiger_zuteilungsbetrag'] == {'zaehler': '10', 'nenner': '1'}
    return len(faelle)

def test_erbrecht_normanwendungen_zusatz():
    pruefe_faelle(Path(__file__).resolve().parents[1] / 'tests/fixtures/kompositionsfaelle/erbrecht_normanwendungen_zusatz.json')

if __name__ == '__main__':
    import sys
    print(pruefe_faelle(sys.argv[1]), 'Python Normanwendungen PASS')
