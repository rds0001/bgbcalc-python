from .kalender import _datum, _ergebnis, _fehler, _frist, _ganzzahl, _text, _vorhanden

def landpacht_verzug_zeit_und_terminvergleich(verzugsbeginn_am=None, beginnart=None, prueftag=None, rueckstaendige_terminnummern=None, einordnungsnachweis=None):
    """Dreimonats-Verzugslaufzeit streng vergleichen und aufeinanderfolgende qualifiziert rückständige Pachtzahlungstermine zählen."""
    beginn=_datum(verzugsbeginn_am,'verzugsbeginn_am');tag=_datum(prueftag,'prueftag');_text(einordnungsnachweis,'einordnungsnachweis')
    if tag<beginn: _fehler('prueftag','Prüftag darf nicht vor dem qualifizierten Verzugsbeginn liegen.')
    ende=_frist(verzugsbeginn_am,3,'monate',beginnart)
    _vorhanden(rueckstaendige_terminnummern,'rueckstaendige_terminnummern')
    if not isinstance(rueckstaendige_terminnummern,list) or len(rueckstaendige_terminnummern)>1000: _fehler('rueckstaendige_terminnummern','Liste0..1000 erforderlich.')
    nummern=[_ganzzahl(n,'terminnummer',1,9007199254740991) for n in rueckstaendige_terminnummern]
    if len(set(nummern))!=len(nummern): _fehler('rueckstaendige_terminnummern','Termine dürfen nicht doppelt vorkommen.')
    laengste=0;aktuell=0;vorher=None
    for nummer in sorted(nummern):
        aktuell=aktuell+1 if vorher is not None and nummer-vorher==1 else 1
        laengste=max(laengste,aktuell);vorher=nummer
    wert=dict(dreimonatszeitraum_letzter_tag=ende.isoformat(),laenger_als_drei_monate=tag>ende,laengste_rueckstandsfolge=laengste,mindestens_zwei_aufeinanderfolgende_termine=laengste>=2)
    eingaben = dict(verzugsbeginn_am=verzugsbeginn_am, beginnart=beginnart, prueftag=prueftag, rueckstaendige_terminnummern=rueckstaendige_terminnummern, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'datum_anzahl_und_wahrheitswerte','BGB_LANDPACHT_VERZUG_ZEIT_UND_TERMINVERGLEICH',eingaben,[dict(operation='Dreimonats-Verzugslaufzeit streng vergleichen und aufeinanderfolgende qualifiziert rückständige Pachtzahlungstermine zählen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§594eII: Ende einer qualifizierten Dreimonats-Verzugslaufzeit und strenges Überschreiten am Prüftag berechnen; daneben längste lückenlos aufeinanderfolgende Folge qualifiziert rückständiger Zahlungstermine zählen und mit2vergleichen. Keine erfundene Euro-/Prozentgrenze für nicht unerheblichen Teil. Beide numerischen Teilprüfungen getrennt ausgegeben; rechtliche Fallzuordnung nach Zahlungsabschnitt sowie deren Zusammenspiel und Kündigung nicht automatisch entschieden. Terminnummern müssen dem vollständigen Kalender entsprechen, keine nachträgliche Neunummerierung nur rückständiger Raten. Kein künstlicher Neustart/Stillstand des Verzugs bei unbekannten Zahlungsvorgängen; Fristbeginn und kontinuierlicher Verlauf vorqualifiziert.']
    return ergebnis

