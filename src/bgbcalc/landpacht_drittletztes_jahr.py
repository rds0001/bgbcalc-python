from .kalender import _datum, _ergebnis, _fehler, _frist, _tage_addieren, _text, _vorhanden

def landpacht_anfrage_im_drittletzten_pachtjahr(anfrage_am=None, pachtjahre=None, einordnungsnachweis=None):
    """Drittletztes qualifiziertes Pachtjahr auswählen und Anfragezeitpunkt vergleichen."""
    anfrage=_datum(anfrage_am,'anfrage_am');_text(einordnungsnachweis,'einordnungsnachweis');_vorhanden(pachtjahre,'pachtjahre')
    if not isinstance(pachtjahre,list) or not 3<=len(pachtjahre)<=1000: _fehler('pachtjahre','Liste3..1000 erforderlich.')
    namen=set();abschnitte=[]
    for p in pachtjahre:
        if not isinstance(p,dict) or set(p)!={'pachtjahr_id','erster_tag','letzter_tag'}: _fehler('pachtjahre','Genau Kennung und beide Tagesgrenzen erforderlich.')
        name=_text(p['pachtjahr_id'],'pachtjahr_id');a=_datum(p['erster_tag'],'erster_tag');b=_datum(p['letzter_tag'],'letzter_tag')
        if name in namen or a>b or (abschnitte and a!=_tage_addieren(abschnitte[-1][1],1)): _fehler('pachtjahre','Eindeutige lückenlose geordnete Pachtjahrsfolge erforderlich.')
        namen.add(name);abschnitte.append((a,b))
    if abschnitte[-1][1]<_frist(abschnitte[0][0].isoformat(),3,'jahre','tagesbeginn'): _fehler('pachtjahre','Mindestens dreijährige Vertragsdauer erforderlich.')
    a,b=abschnitte[-3]
    wert=dict(drittletztes_pachtjahr_erster_tag=a.isoformat(),drittletztes_pachtjahr_letzter_tag=b.isoformat(),anfrage_im_drittletzten_pachtjahr=a<=anfrage<=b)
    eingaben = dict(anfrage_am=anfrage_am, pachtjahre=pachtjahre, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'daten_und_wahrheitswert','BGB_LANDPACHT_ANFRAGE_IM_DRITTLETZTEN_PACHTJAHR',eingaben,[dict(operation='Drittletztes qualifiziertes Pachtjahr auswählen und Anfragezeitpunkt vergleichen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§594: dritten Pachtjahresabschnitt von hinten aus der vollständigen rechtlich qualifizierten Vertragsfolge auswählen und Anfragezugang mit seinen eingeschlossenen Kalendertagen vergleichen. Zusätzlich mindestens dreijährige Vertragsdauer ab erstem eingeschlossenem Kalendertag prüfen. Pachtjahre sind keine automatisch gleichgesetzten Kalenderjahre; rechtliche Pachtjahrsfolge ausdrücklich Eingabe. Kein automatischer Fortsetzungsentscheid oder Übergehen fehlender Vertragsjahre.']
    return ergebnis

