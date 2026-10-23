from .kalender import _ergebnis, _fehler, _text, _vorhanden
from .reisezeitschwellen import _reise_utc_zeitpunkt

def pfandrechte_bestellungsrang(pfandrechte=None, einordnungsnachweis=None):
    """Pfandrechte nach qualifizierter wirksamer Bestellungszeit in zeitlich aufsteigende Ranggruppen einordnen; Gleichzeitigkeit gleichrangig behandeln."""
    _vorhanden(pfandrechte,'pfandrechte');_text(einordnungsnachweis,'einordnungsnachweis')
    if not isinstance(pfandrechte,list) or not 1<=len(pfandrechte)<=1000: _fehler('pfandrechte','Liste1..1000 erforderlich.')
    kennungen=set();zeiten=[]
    for p in pfandrechte:
        if not isinstance(p,dict) or set(p)!={'pfandrecht_id','bestellung_am_utc'}: _fehler('pfandrechte','Genau pfandrecht_id und bestellung_am_utc erforderlich.')
        kennung=_text(p['pfandrecht_id'],'pfandrecht_id')
        if kennung in kennungen: _fehler('pfandrecht_id','Doppelte Kennung unzulässig.')
        kennungen.add(kennung);_reise_utc_zeitpunkt(p['bestellung_am_utc'],'bestellung_am_utc');zeiten.append(p['bestellung_am_utc'])
    raenge={zeit:i+1 for i,zeit in enumerate(sorted(set(zeiten)))}
    wert=[dict(pfandrecht_id=p['pfandrecht_id'],ranggruppe=raenge[p['bestellung_am_utc']]) for p in pfandrechte]
    eingaben = dict(pfandrechte=pfandrechte, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'ranggruppen','BGB_PFANDRECHTE_BESTELLUNGSRANG',eingaben,[dict(operation='Pfandrechte nach qualifizierter wirksamer Bestellungszeit in zeitlich aufsteigende Ranggruppen einordnen; Gleichzeitigkeit gleichrangig behandeln.')],eingaben.copy())
    ergebnis["hinweise"] = ['§1209: frühere rechtlich wirksame Bestellung hat niedrigere Ranggruppe, gleichzeitige Bestellung gleiche Ranggruppe. Künftige oder bedingte Forderungen verwenden ebenfalls die Bestellungszeit des Pfandrechts. Kein automatischer Rangwechsel, keine Entscheidung über Entstehung/Gutgläubigkeit oder Befriedigungsbeträge. Zeitpunkte müssen rechtlich ausreichend exakt auf UTC-Sekunden normalisiert sein; unterschiedliche Subsekunden dürfen nicht durch Abschneiden zu Gleichrang werden. Bei nicht sekundengenau abbildbarem Sachverhalt diese Funktion nicht verwenden. Ausgabe in Eingabereihenfolge; Ranggruppen sind lückenlos numeriert, kein Grundbuchrang nach879.']
    return ergebnis

