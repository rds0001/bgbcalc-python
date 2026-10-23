from .kalender import _datum, _ergebnis, _fehler, _frist, _text

def darlehen_verzugshemmungszeitraum(anspruch_entstanden_am=None, erster_verzugshemmungstag=None, feststellung_letzter_hemmungstag=None, betrachtung_bis=None, einordnungsnachweis=None):
    """Zehnjahresgrenze ab Anspruchsentstehung berechnen und beobachtetes Verzugshemmungsintervall an Feststellung beziehungsweise Hoechstgrenze abschneiden."""
    a=_datum(anspruch_entstanden_am,'anspruch_entstanden_am');v=_datum(erster_verzugshemmungstag,'erster_verzugshemmungstag');b=_datum(betrachtung_bis,'betrachtung_bis');_text(einordnungsnachweis,'einordnungsnachweis')
    f=None if feststellung_letzter_hemmungstag is None else _datum(feststellung_letzter_hemmungstag,'feststellung_letzter_hemmungstag')
    if v<a or b<a or (f is not None and not a<=f<=b): _fehler('zeitfolge','Verzug/Betrachtung nicht vor Entstehung; Feststellung innerhalb beobachteter Zeit erforderlich.')
    g=_frist(anspruch_entstanden_am,10,'jahre','ereignis');ende=min(g,b) if f is None else min(g,b,f)
    wert=dict(zehnjahresgrenze=g.isoformat(),hemmungszeitraeume=[] if v>ende else [dict(erster_gehemmter_tag=v.isoformat(),letzter_gehemmter_tag=ende.isoformat())])
    eingaben = dict(anspruch_entstanden_am=anspruch_entstanden_am, erster_verzugshemmungstag=erster_verzugshemmungstag, feststellung_letzter_hemmungstag=feststellung_letzter_hemmungstag, betrachtung_bis=betrachtung_bis, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'daten_und_intervalle','BGB_DARLEHEN_VERZUGSHEMMUNGSZEITRAUM',eingaben,[dict(operation='Zehnjahresgrenze ab Anspruchsentstehung berechnen und beobachtetes Verzugshemmungsintervall an Feststellung beziehungsweise Hoechstgrenze abschneiden.')],eingaben.copy())
    ergebnis["hinweise"] = ['§497III3: vom rechtlich normalisierten Verzugsbeginn bis qualifizierter Feststellung197I3bis5, hoechstens zehn Jahre ab Entstehung des einzelnen Anspruchs. Vorhandener Kalenderkern berechnet Zehnjahresgrenze, Intervall wird am fruehesten von Feststellung, Hoechstgrenze und Betrachtungsende abgeschnitten. Ohne Feststellung nur beobachtetes Intervall, kein behauptetes endgueltiges Verjaehrungsende. Unterschiedlich entstandene Einzelansprueche getrennt behandeln; Hemmung nach209 danach mit vorhandenem Kern kombinieren. Tagesnormalisierung einschliesslich Randtage rechtlich belegen; kein pauschales Aufrunden untertaegiger Ereignisse. Auch497IV nimmt III3nicht aus, wohingegen III5Titel-Hauptforderung-Zinsen-Ausnahme zu beachten ist. Keine persoenliche oder sachliche Anwendbarkeit automatisch feststellen, keine Hemmung einer schon abgelaufenen Frist.']
    return ergebnis

