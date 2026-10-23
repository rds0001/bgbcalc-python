import json
from pathlib import Path
import bgbcalc as b

def test_rueckblicke_normanwendung():
    d=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/rueckblicke_normanwendung.json').read_text())
    h='Rechtlich qualifizierte normbezogene Rückwärtsanalogie, Tagesgrenzen und taggleiche Zielmonate.'
    f=d['mietpfand']
    start=b.rueckwaertsfrist_kalendergrenze(f['pfaendung_am'],1,'jahre','ereignistag','nur_taggleiche_monate',h)['wert']['grenztag_beginn']
    assert start==f['erwarteter_fensterbeginn']
    for a in f['abschnitte']:
        assert (start<=a['von']<=a['bis']<f['pfaendung_am'])==a['innerhalb']
    f=d['privatglaeubiger']
    start=b.rueckwaertsfrist_kalendergrenze(f['pfaendung_am'],6,'monate','ereignistag','nur_taggleiche_monate',h)['wert']['grenztag_beginn']
    assert start==f['erwarteter_fensterbeginn']
    for a in f['vollstreckungen']:
        assert (start<=a['am']<f['pfaendung_am'])==a['innerhalb']
    assert b.gesellschaft_jahresendkuendigung(f['kuendigung'],'privatglaeubiger_726',h)['wert']['beendigungsgrundtermin']==f['beendigung']
    f=d['zeitmiete']
    start=b.rueckwaertsfrist_kalendergrenze(f['mietende_am'],4,'monate','tagesende','nur_taggleiche_monate',h)['wert']['grenztag_beginn']
    assert start==f['fruehester_auskunftstag']
    for a in f['anfragen']:
        assert (a['am']>=start)==a['zulaessiger_zeitpunkt']
