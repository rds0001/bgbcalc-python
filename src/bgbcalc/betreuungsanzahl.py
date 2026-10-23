from .kalender import _datum, _ergebnis, _fehler, _text, _vorhanden

def betreuungen_im_qualifizierten_zweijahresfenster(prueftag=None, rueckblick_erster_tag=None, betreuungszeitraeume=None, einordnungsnachweis=None):
    """Eindeutige Betreuungen im qualifizierten Zweijahresfenster zählen und strikt mit eins vergleichen."""
    tag=_datum(prueftag,'prueftag');anfang=_datum(rueckblick_erster_tag,'rueckblick_erster_tag');_text(einordnungsnachweis,'einordnungsnachweis')
    if anfang>tag: _fehler('rueckblick_erster_tag','Fensterbeginn darf nicht nach Prüftag liegen.')
    _vorhanden(betreuungszeitraeume,'betreuungszeitraeume')
    if not isinstance(betreuungszeitraeume,list) or len(betreuungszeitraeume)>1000: _fehler('betreuungszeitraeume','Liste0..1000 erforderlich.')
    gesehen=set();ids=[]
    for z in betreuungszeitraeume:
        if not isinstance(z,dict) or set(z)!={'betreuungs_id','erster_tag','letzter_tag'}: _fehler('betreuungszeitraeume','Genau betreuungs_id,erster_tag,letzter_tag erforderlich.')
        kennung=_text(z['betreuungs_id'],'betreuungs_id');a=_datum(z['erster_tag'],'erster_tag');b=_datum(z['letzter_tag'],'letzter_tag')
        schluessel=(kennung,a,b)
        if schluessel in gesehen or a>b: _fehler('betreuungszeitraeume','Keine identischen doppelten Zeiträume; Beginn darf nicht nach Ende liegen.')
        gesehen.add(schluessel)
        if a<=tag and b>=anfang and kennung not in ids: ids.append(kennung)
    wert=dict(beruecksichtigte_betreuungs_ids=ids,anzahl_betreuungen=len(ids),mehr_als_eine_betreuung=len(ids)>1)
    eingaben = dict(prueftag=prueftag, rueckblick_erster_tag=rueckblick_erster_tag, betreuungszeitraeume=betreuungszeitraeume, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'anzahl_und_wahrheitswert','BGB_BETREUUNGEN_IM_QUALIFIZIERTEN_ZWEIJAHRESFENSTER',eingaben,[dict(operation='Eindeutige Betreuungen im qualifizierten Zweijahresfenster zählen und strikt mit eins vergleichen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§1861II: Zahl unterschiedlicher Betreuungen zählen, die am Prüftag geführt werden oder das vorqualifizierte eingeschlossene Zweijahresfenster schneiden. Mehr als eine bedeutet strikt mindestens zwei; nicht Anzahl einzelner Tätigkeitstage oder unterschiedlicher Betreuer. Keine automatische Pflichtbefreiung oder Festlegung eines ungeklärten rückwärts zu berechnenden Grenztags. Nicht zusammenhängende Zeiträume derselben Betreuung werden getrennt auf Schnittmenge geprüft; gezählt wird die eindeutige Betreuung, nicht ihre Zeiträume.']
    return ergebnis

