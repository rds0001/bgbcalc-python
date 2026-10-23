from .kalender import _datum, _ergebnis, _fehler, _frist, _text
from .reisezeitschwellen import _reise_utc_zeitpunkt

def mietpreisbremse_ruegezeitliche_beschraenkung(mietbeginn_am=None, ruegezugang_lokal_am=None, ruegezugang_utc=None, mietende_utc=None, zeitnachweis=None):
    """30Monatsende aus Tagesbeginn berechnen, lokalen Rügetag und unabhängig davon UTC-Beendigungszeitpunkt vergleichen; Beschränkungsgründe mit ODER verbinden."""
    a=_datum(mietbeginn_am,'mietbeginn_am');r=_datum(ruegezugang_lokal_am,'ruegezugang_lokal_am');u=_reise_utc_zeitpunkt(ruegezugang_utc,'ruegezugang_utc');_text(zeitnachweis,'zeitnachweis')
    if r<a: _fehler('ruegezugang_lokal_am','Rüge des betrachteten Mietverhältnisses nicht vor Mietbeginn.')
    e=_frist(mietbeginn_am,30,'monate','tagesbeginn');spaet=r>e
    beendet=False if mietende_utc is None else u>=_reise_utc_zeitpunkt(mietende_utc,'mietende_utc')
    wert=dict(dreissigmonatszeitraum_letzter_tag=e.isoformat(),ruege_nach_dreissig_monaten=spaet,mietverhaeltnis_bei_ruege_beendet=beendet,rueckforderung_auf_spaetere_faelligkeit_beschraenkt=spaet or beendet)
    eingaben = dict(mietbeginn_am=mietbeginn_am, ruegezugang_lokal_am=ruegezugang_lokal_am, ruegezugang_utc=ruegezugang_utc, mietende_utc=mietende_utc, zeitnachweis=zeitnachweis)
    ergebnis = _ergebnis(wert,'datum_und_wahrheitswerte','BGB_MIETPREISBREMSE_RUEGEZEITLICHE_BESCHRAENKUNG',eingaben,[dict(operation='30Monatsende aus Tagesbeginn berechnen, lokalen Rügetag und unabhängig davon UTC-Beendigungszeitpunkt vergleichen; Beschränkungsgründe mit ODER verbinden.')],eingaben.copy())
    ergebnis["hinweise"] = ['556gII3:30Kalendermonate ab Mietbeginn zu Tagesbeginn nach187II/188. Zugang nach dem so berechneten letzten Tag ist verspätet. Unabhängig davon Beschränkung, wenn Mietverhältnis beim UTC-Zugang bereits beendet ist; Zugang gleich exklusivem Beendigungszeitpunkt zählt als beendet. Bei üblichem Vertragsende31.12.um24Uhr ist dieser Zeitpunkt1.1.um00Uhr in zutreffender Zeitzone, anschließend inUTC normalisieren. Keine pauschalen900Tage, keine Zeitzone raten und keine193-Verlängerung dieses Rückwirkungsmerkmals. Kein materielles Urteil über Rügeform/Auskunft, Rückzahlungsbetrag oder Verjährung. Lokalzugangstag undUTC-Zeit müssen dasselbe rechtlich qualifizierte Ereignis bezeichnen. Für untertägigen Mietbeginn ist diese Tagesbeginnvariante nicht freigegeben.']
    return ergebnis

