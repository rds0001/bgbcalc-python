import json
from pathlib import Path
import bgbcalc as b

def test_mietruege556g_normanwendung():
    fälle=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/mietruege556g_normanwendung.json').read_text())
    h='Qualifizierter556gII3-Fall, beide Fälligkeiten dem betrachteten Mietverhältnis zugehörig; nach Vertragsende qualifizierte Abrechnung.'
    for f in fälle:
        zeit=b.mietpreisbremse_ruegezeitliche_beschraenkung('2024-01-01',f['ruegetag'],f['zugang'],f['mietende'],h)['wert']
        abschnitte=[dict(abschnitt_id=k,faelligkeit_utc=t,tatsaechlich_gezahlte_miete='1000',zulaessige_miete='940') for k,t in [('vorher','2026-06-01T00:00:00Z'),('nachher','2026-08-01T00:00:00Z')]]
        r=b.mietpreisbremse_rueckzahlungsbetraege(f['zugang'],zeit['rueckforderung_auf_spaetere_faelligkeit_beschraenkt'],abschnitte,'0',h)
        assert r['wert']['verbleibender_rueckzahlungsbetrag']==dict(zaehler=f['erwartet'],nenner='1')
