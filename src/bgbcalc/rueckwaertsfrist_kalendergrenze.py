from .kalender import _datum, _ergebnis, _fehler, _ganzzahl, _auswahl, _text, _tage_addieren, _monatsende

def rueckwaertsfrist_kalendergrenze(bezugstag=None, anzahl=None, einheit=None, bezugsart=None, monatsendregel=None, methodennachweis=None):
    """Qualifizierten Kalenderabstand rückwärts mit bestehenden Datumshelfern berechnen; Grenztagesbeginn und vorausgehenden vollen Tag ausweisen."""
    a=_datum(bezugstag,'bezugstag');z=_ganzzahl(anzahl,'anzahl',1,3652059);_auswahl(einheit,'einheit',('tage','wochen','monate','jahre'));_auswahl(bezugsart,'bezugsart',('ereignistag','tagesende'));_auswahl(monatsendregel,'monatsendregel',('nur_taggleiche_monate','letzter_monatstag'));_text(methodennachweis,'methodennachweis')
    if einheit in ('tage','wochen'):vergleich=_tage_addieren(a,-z*(7 if einheit=='wochen' else 1))
    else:
        vergleich=_monatsende(a,-z*(12 if einheit=='jahre' else 1),False)
        if vergleich.day!=a.day and monatsendregel=='nur_taggleiche_monate':_fehler('monatsendregel','Fehlende Tageszahl ohne freigegebene Monatsendregel.')
    grenze=_tage_addieren(vergleich,1) if bezugsart=='tagesende' else vergleich
    letzter=_tage_addieren(grenze,-1)
    wert=dict(grenztag_beginn=grenze.isoformat(),letzter_voller_tag_vor_grenze=letzter.isoformat())
    eingaben = dict(bezugstag=bezugstag, anzahl=anzahl, einheit=einheit, bezugsart=bezugsart, monatsendregel=monatsendregel, methodennachweis=methodennachweis)
    ergebnis = _ergebnis(wert,'daten','BGB_RUECKWAERTSFRIST_KALENDERGRENZE',eingaben,[dict(operation='Qualifizierten Kalenderabstand rückwärts mit bestehenden Datumshelfern berechnen; Grenztagesbeginn und vorausgehenden vollen Tag ausweisen.')],eingaben.copy())
    ergebnis["hinweise"] = ['Bedingter Kalenderkern zur ausdrücklich qualifizierten Rückwärtsanalogie187/188. Ereignistag: zurückliegender gleichbenannter/gleichzahliger Tag beginnt die Grenze; letzter voller vorausgehender Handlungstag ist dessen Vortag. Tagesende: rückwärts mitgezählter Bezugstag, Grenze am Folgetagesbeginn des zurückliegenden Vergleichstags; letzter voller Handlungstag ist Vergleichstag. Für reine Zeitfenster ist die Grenztagesbeginn-Ausgabe zu verwenden, nicht ungeprüft der letzte Handlungstag. Untertägige Zeitpunkte und rechtliche Einschließung einer einzelnen Grenzhandlung gesondert bestimmen. Monatsende nur auf ausdrückliche Methodenvorgabe; nur_taggleiche_monate verhindert eine ungesicherte Ersatzregel. Kein193-Automatismus: Verfahrenszwecke können unterschiedliche Werktagskorrekturen verlangen. Keine Inversion durch Suche nach einem beliebigen vorwärts passenden Datum. Standardkalender und bestehende Datumshelfer, unveränderte Vorwärtsfunktionen.']
    return ergebnis

