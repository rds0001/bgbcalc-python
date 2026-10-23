import json
from pathlib import Path
import bgbcalc as b
from bgbcalc.zahlen import _zahleneingabe
from bgbcalc.zinsen import _bruchteile

def test_staffel556d_g_normanwendung():
    f=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/staffel556d_g_normanwendung.json').read_text())
    h='556d–g/557a-Folge mit zunächst fehlender Auskunft; spätere Nachholung, Modernisierung im maßgeblichen Dreijahresfenster, ersteFälligkeit jeweilsStaffelbeginn; Schutzmodell ausdrücklich qualifiziert.'
    warteende=b.fristende(f['nachholung'],2,'jahre','ereignis')['wert']
    assert warteende=='2025-12-31'
    vormiete=b.mietpreisbegrenzung_vormiete_bereinigen('850','100',['50'],h)['wert']['bereinigte_vormiete']
    modern=b.modernisierung_regulaerer_zwischenbetrag('12000','2000','1000','0','0',True)['wert']['monatlicher_zwischenbetrag']
    kap=b.modernisierung_kappungsgrenze('50','8','0','0','allgemein',True)['wert']['massgebliche_restgrenze']
    modern=_bruchteile(min(_zahleneingabe(modern),_zahleneingabe(kap)))
    staffeln=[]
    for s in f['staffeln']:
        nutzbar=s['beginn']>warteende
        grund=b.mietpreisbegrenzung_grundbetrag(s['vergleich'],True,False,h)['wert']
        vor=b.mietpreisbegrenzung_vormietgrenze(grund,vormiete,nutzbar,h)['wert']
        unmod=b.mietpreisbegrenzung_grundbetrag(s['unmodernisiert'],True,False,h)['wert']
        grenze=b.mietpreisbegrenzung_modernisierungsalternative(vor,unmod,modern,nutzbar,h)['wert']['nutzbare_monatsgrenze']
        staffeln.append(dict(staffelbeginn_am=s['beginn'],vereinbarte_monatsmiete=s['vereinbart'],zulaessige_monatsmiete_ohne_vorstaffelschutz=grenze))
    werte=b.staffelmiete_flexible_betragsfolge(staffeln,'hoechste_wirksame_vorstaffel',h)['wert']
    for s,r in zip(f['staffeln'],werte):assert r['rechnerische_monatsmiete']==dict(zaehler=s['erwartet'],nenner='1')
    beschraenkt=b.mietpreisbremse_ruegezeitliche_beschraenkung('2024-01-01',f['ruege_am'],f['ruege_utc'],None,h)['wert']['rueckforderung_auf_spaetere_faelligkeit_beschraenkt']
    abschnitte=[dict(abschnitt_id=str(i),faelligkeit_utc=s['beginn']+'T12:00:00Z',tatsaechlich_gezahlte_miete=s['vereinbart'],zulaessige_miete=r['rechnerische_monatsmiete']) for i,(s,r) in enumerate(zip(f['staffeln'],werte))]
    assert b.mietpreisbremse_rueckzahlungsbetraege(f['ruege_utc'],beschraenkt,abschnitte,'0',h)['wert']['verbleibender_rueckzahlungsbetrag']==dict(zaehler=f['rueckzahlung'],nenner='1')
