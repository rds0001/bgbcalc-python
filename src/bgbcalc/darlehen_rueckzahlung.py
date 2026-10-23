from .kalender import _datum, _ergebnis, _fehler, _frist, _text, _vorhanden, werktagsverschiebung
from .betraege import _geld
from .zahlen import _addieren, _subtrahieren
from .zinsen import _bruchteile

def darlehen_rueckzahlung_im_zweiwochenfenster(kuendigung_wirksam_am=None, geschuldeter_betrag=None, rueckzahlungen=None, feiertagskalender=None, einordnungsnachweis=None):
    """Zweiwochenrückzahlungsfrist mit193 korrigieren und rechtzeitige Rückzahlungen mit geschuldetem Betrag vergleichen."""
    start=_datum(kuendigung_wirksam_am,'kuendigung_wirksam_am');schuld=_geld(geschuldeter_betrag);_text(einordnungsnachweis,'einordnungsnachweis')
    grund=_frist(kuendigung_wirksam_am,2,'wochen','ereignis')
    _vorhanden(feiertagskalender,'feiertagskalender')
    if not isinstance(feiertagskalender,dict) or set(feiertagskalender)!={'feiertage','ort','kalenderquelle','kalender_von','kalender_bis'}: _fehler('feiertagskalender','Vollständiges Kalenderobjekt erforderlich.')
    ende=_datum(werktagsverschiebung(datum=grund.isoformat(),anwendungsfall='leistung',**feiertagskalender)['wert'],'fristende')
    _vorhanden(rueckzahlungen,'rueckzahlungen')
    if not isinstance(rueckzahlungen,list) or len(rueckzahlungen)>1000: _fehler('rueckzahlungen','Liste0..1000 erforderlich.')
    namen=set();recht=_geld('0');spaet=_geld('0')
    for z in rueckzahlungen:
        if not isinstance(z,dict) or set(z)!={'zahlung_id','rueckzahlung_am','betrag'}: _fehler('rueckzahlungen','Genau zahlung_id,rueckzahlung_am,betrag erforderlich.')
        name=_text(z['zahlung_id'],'zahlung_id');tag=_datum(z['rueckzahlung_am'],'rueckzahlung_am');betrag=_geld(z['betrag'])
        if name in namen or tag<start: _fehler('rueckzahlungen','Eindeutige Zahlungen ab Wirksamwerden erforderlich.')
        namen.add(name)
        if tag<=ende: recht=_addieren(recht,betrag)
        else: spaet=_addieren(spaet,betrag)
    fehl=max(_subtrahieren(schuld,recht),0)
    wert=dict(rueckzahlungsgrundfrist_letzter_tag=grund.isoformat(),rueckzahlungsfrist_letzter_tag=ende.isoformat(),rechtzeitig_zurueckgezahlt=_bruchteile(recht),spaeter_zurueckgezahlt=_bruchteile(spaet),rechtzeitiger_fehlbetrag=_bruchteile(fehl),geschuldeter_betrag_rechtzeitig_gedeckt=fehl==0)
    eingaben = dict(kuendigung_wirksam_am=kuendigung_wirksam_am, geschuldeter_betrag=geschuldeter_betrag, rueckzahlungen=rueckzahlungen, feiertagskalender=feiertagskalender, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'daten_EUR_und_wahrheitswert','BGB_DARLEHEN_RUECKZAHLUNG_IM_ZWEIWOCHENFENSTER',eingaben,[dict(operation='Zweiwochenrückzahlungsfrist mit193 korrigieren und rechtzeitige Rückzahlungen mit geschuldetem Betrag vergleichen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§489III: Zweiwochengrundfrist ab Wirksamwerden der Kündigung, anschließend193-Leistungsfristkorrektur mit vorhandenem Kalenderkern. Nur bis einschließlich korrigiertem Ende erfüllungswirksame Rückzahlungen summieren; Deckung und positiven Fehlbetrag vergleichen. Spätere Zahlungen getrennt summieren, sie heilen die Frist nicht automatisch. Keine automatische Kündigungswirksamkeitsentscheidung; geschuldete Summe und Erfüllung rechtlich vorqualifiziert. Kalenderdatum einer Zahlung reicht nur bei rechtlich eindeutig normalisiertem Erfüllungszeitpunkt.']
    return ergebnis

