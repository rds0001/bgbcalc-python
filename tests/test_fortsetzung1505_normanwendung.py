import json
from pathlib import Path
import bgbcalc as b

def test_fortsetzung1505():
    d=json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/kompositionsfaelle/fortsetzung1505_normanwendung.json').read_text());h=d['nachweis']
    anteil=b.fortgesetzte_guetergemeinschaft_grundanteile('1000',[dict(abkoemmling_id=x,hypothetischer_erbteil='0.5') for x in ['A','B']],h)['wert']['abkoemmlingsanteile'][0]
    assert anteil['pflichtteilswertbasis']==dict(zaehler='125',nenner='1')
    q=anteil['anteil_gesamtgut']
    for f in d['faelle']:
        wert=b.pflichtteil_schenkungswert(f['vergleich'],f['beendigungwert'],False,False,h)['wert']
        zeit=b.pflichtteil_schenkungsabschmelzung(wert,'2020-01-01','2023-01-02',True,False,None,h)['wert']
        assert zeit['beruecksichtigter_schenkungswert']==f['geschenk']
        grund=b.pflichtteilsergaenzung_grundbetrag('1000',zeit['beruecksichtigter_schenkungswert'],int(q['zaehler']),int(q['nenner']),True,h)['wert']
        assert grund['ordentlicher_pflichtteilswert']==anteil['pflichtteilswertbasis']
        assert grund['ergaenzungsgrundbetrag']==f['grund']
        ende=b.pflichtteilsergaenzung_mehrhinterlassung(grund['ergaenzungsgrundbetrag'],f['hinterlassen'],grund['ordentlicher_pflichtteilswert'],h)['wert']
        assert ende['verbleibende_ergaenzung']==f['rest']
