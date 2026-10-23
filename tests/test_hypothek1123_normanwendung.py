import json
from pathlib import Path
import bgbcalc as b

def test_hypothek1123_normanwendung():
    faelle=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/hypothek1123_normanwendung.json').read_text())
    for f in faelle:
        jahr=b.sachenrechtliche_grundfrist('hypothekenmiete_faelligkeitsjahr_1123',f['faellig'],'1123II1-Jahresablauf ab qualifizierter Fälligkeit.')['wert']['grundfristende']
        frei=jahr<f['beobachtung'] and (f['beschlagnahme'] is None or f['beschlagnahme']>jahr)
        if f['vorauszahlung'] and f['beschlagnahme'] is not None:
            grenze=b.hypothek_beschlagnahme_monatsgrenze(f['beschlagnahme'],'1123II2-vorqualifizierte Vorausmiete; eigener zeitlich getrennter Mietabschnitt.')['wert']['letzter_erfasster_monat_endet_am']
            frei=frei and f['mietende']<=grenze
        assert frei==f['befreit'],f
