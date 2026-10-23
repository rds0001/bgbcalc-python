from .kalender import _datum, _ergebnis, _fehler, _text, _vorhanden, _auswahl
from .betraege import _wahrheitswert

def gesellschaft_nachhaftung_fristsicherung(nachhaftungsfrist_letzter_tag=None, faelligkeit_am=None, sicherungsereignisse=None, einordnungsnachweis=None):
    """Fälligkeit und qualifizierte Sicherungszeitpunkte gegen unveränderte korrigierte Nachhaftungsfrist vergleichen;212II/III-rückwirkend unwirksame Vollstreckungsakte ausschließen."""
    ende=_datum(nachhaftungsfrist_letzter_tag,'nachhaftungsfrist_letzter_tag');faellig=_datum(faelligkeit_am,'faelligkeit_am');_text(einordnungsnachweis,'einordnungsnachweis');_vorhanden(sicherungsereignisse,'sicherungsereignisse')
    if not isinstance(sicherungsereignisse,list) or len(sicherungsereignisse)>1000:_fehler('sicherungsereignisse','Liste mit höchstens1000Ereignissen erforderlich.')
    arten=('feststellung_197','gerichtliche_vollstreckung','behoerdliche_vollstreckung','vollstreckungsantrag','verwaltungsakt_oeffentlich_rechtlich','schriftliches_anerkenntnis');vollstreckung=set(arten[1:4]);ids=set();wirksam=[]
    for e in sicherungsereignisse:
        if not isinstance(e,dict) or set(e)!={'ereignis_id','art','datum','rueckwirkend_unwirksam_212'}:_fehler('sicherungsereignisse','Genau Kennung,Art,Datum und212-Rückwirkungsmerkmal erforderlich.')
        k=_text(e['ereignis_id'],'ereignis_id');_auswahl(e['art'],'art',arten);tag=_datum(e['datum'],'datum');rueck=_wahrheitswert(e['rueckwirkend_unwirksam_212'],'rueckwirkend_unwirksam_212')
        if k in ids:_fehler('ereignis_id','Kennung doppelt.')
        ids.add(k)
        if rueck and e['art'] not in vollstreckung:_fehler('rueckwirkend_unwirksam_212','212II/III-Rückwirkung hier nur für Vollstreckung/Antrag.')
        if not rueck and tag<=ende:wirksam.append(k)
    f=faellig<=ende
    wert=dict(nachhaftungsfrist_letzter_tag=nachhaftungsfrist_letzter_tag,faelligkeit_innerhalb_frist=f,rechtzeitige_sicherungsereignis_ids=wirksam,zeitliche_kopplung_erfuellt=f and bool(wirksam))
    eingaben = dict(nachhaftungsfrist_letzter_tag=nachhaftungsfrist_letzter_tag, faelligkeit_am=faelligkeit_am, sicherungsereignisse=sicherungsereignisse, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'datum_und_wahrheitswerte','BGB_GESELLSCHAFT_NACHHAFTUNG_FRISTSICHERUNG',eingaben,[dict(operation='Fälligkeit und qualifizierte Sicherungszeitpunkte gegen unveränderte korrigierte Nachhaftungsfrist vergleichen;212II/III-rückwirkend unwirksame Vollstreckungsakte ausschließen.')],eingaben.copy())
    ergebnis["hinweise"] = ['728bI/II: Fälligkeit bis einschließlich letztem Fristtag und mindestens ein rechtlich geeigneter rechtzeitiger Sicherungsakt; schriftliches Anerkenntnis ersetzt in qualifiziertem Umfang Feststellung. Vollstreckungsakte/Anträge mit rechtlich feststehender212II/III-Rückwirkung zählen nicht. Kein pauschaler212I-Neubeginn: der übergebene korrigierte Nachhaftungsfristtag bleibt unverändert.212-Rückwirkung ist Rechtsbewertung, keine neue Fristdauer. Bei teilweise wirksamem Anerkenntnis oder nur teilweise gesicherter Forderung vorher sachlich in Forderungsteile trennen; kein volles Anerkenntnis vortäuschen. Gerichtliche/behördliche Vollstreckung, Titel nach197Absatz1Nummer3–5und öffentlich-rechtlicher Verwaltungsakt müssen zum konkreten Anspruch passen. Funktion berechnet Zeitkopplung, keinen vollständigen Haftungstatbestand. Untertägige Grenzprobleme vorab qualifizieren.']
    return ergebnis

