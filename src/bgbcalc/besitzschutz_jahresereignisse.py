from .kalender import _datum, _ergebnis, _fehler, _text, _vorhanden
from .reisezeitschwellen import _reise_utc_zeitpunkt
from .rueckwaertsfrist_kalendergrenze import rueckwaertsfrist_kalendergrenze

def besitzschutz_jahresereignisse(stoerung_lokal_am=None, stoerung_utc=None, ereignisse=None, monatsendregel=None, einordnungsnachweis=None):
    """Jahresrückblick berechnen, rechtlich qualifizierte Ereignisse nach lokalem Grenztag und tatsächlicher UTC-Reihenfolge auswählen und zählen."""
    s=_datum(stoerung_lokal_am,'stoerung_lokal_am');u=_reise_utc_zeitpunkt(stoerung_utc,'stoerung_utc');_text(einordnungsnachweis,'einordnungsnachweis');_vorhanden(ereignisse,'ereignisse')
    if not isinstance(ereignisse,list) or len(ereignisse)>1000:_fehler('ereignisse','Liste mit höchstens1000Ereignissen erforderlich.')
    g=rueckwaertsfrist_kalendergrenze(stoerung_lokal_am,1,'jahre','ereignistag',monatsendregel,einordnungsnachweis)['wert']['grenztag_beginn'];von=_datum(g,'fensterbeginn');ids=set();auswahl=[]
    for e in ereignisse:
        if not isinstance(e,dict) or set(e)!={'ereignis_id','lokal_am','zeitpunkt_utc'}:_fehler('ereignisse','Genau Kennung,lokal_am,zeitpunkt_utc erforderlich.')
        k=_text(e['ereignis_id'],'ereignis_id');tag=_datum(e['lokal_am'],'lokal_am');zeit=_reise_utc_zeitpunkt(e['zeitpunkt_utc'],'zeitpunkt_utc')
        if k in ids:_fehler('ereignis_id','Kennung doppelt.')
        ids.add(k)
        if von<=tag<=s and zeit<u:auswahl.append(k)
    wert=dict(jahresfenster_erster_tag=g,beruecksichtigte_ereignis_ids=auswahl,ereignisanzahl=len(auswahl),mindestens_ein_ereignis=bool(auswahl))
    eingaben = dict(stoerung_lokal_am=stoerung_lokal_am, stoerung_utc=stoerung_utc, ereignisse=ereignisse, monatsendregel=monatsendregel, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'datum_anzahl_und_wahrheitswert','BGB_BESITZSCHUTZ_JAHRESEREIGNISSE',eingaben,[dict(operation='Jahresrückblick berechnen, rechtlich qualifizierte Ereignisse nach lokalem Grenztag und tatsächlicher UTC-Reihenfolge auswählen und zählen.')],eingaben.copy())
    ergebnis["hinweise"] = ['861II/862II: zeitliches Merkmal der konkreten Besitzerlangung im letzten Jahr vor Entziehung/Störung; rechtliche Fehlerhaftigkeit und Gegenüberbeziehung separat.1029: mindestens eine qualifizierte Dienstbarkeitsausübung im Jahresfenster, keine Mindesthäufigkeit über einmal hinaus. Gemeinsamer Rückwärtskern bestimmt Grenztagesbeginn mit ausdrücklich vorgegebener Monatsendmethode. Ereignisse am Grenztag zählen, Ereignisse am Störungstag nur soweit ihrUTC-Zeitpunkt tatsächlich vor der Störung liegt. Spätere/gleichzeitige Ereignisse zählen nicht. Für861/862die konkret betrachtete Besitzerlangung eingeben; nicht jede beliebige Ausübung als Neuerwerb behandeln. Vollständige und konsistente Zeitpunkte rechtlich vorqualifiziert, keine stille UTC-zu-Lokaldatum-Umrechnung. Ausgabe nur Zeitmerkmale, keine Besitzschutzentscheidung.864-Erlöschen/Anspruchswahrung getrennt.']
    return ergebnis

