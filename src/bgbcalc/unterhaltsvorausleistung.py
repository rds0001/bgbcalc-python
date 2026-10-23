from .kalender import _auswahl, _ergebnis, _fehler, _frist, _ganzzahl, _text

def unterhalt_vorausleistung_zeitgrenze(zeitabschnittsfall=None, bezugstag_am=None, beginnart=None, qualifizierte_dauer=None, qualifizierte_einheit=None, einordnungsnachweis=None):
    """Gesetzliche Dreimonatsdauer oder ausdrücklich rechtlich qualifizierte Sonderdauer auswählen und Zeitraum mit vorhandener Kalenderbibliothek berechnen."""
    _auswahl(zeitabschnittsfall,'zeitabschnittsfall',('geldrente_760','andere_rente_760','angemessener_selbstbestimmter_zeitabschnitt'))
    _text(einordnungsnachweis,'einordnungsnachweis')
    if zeitabschnittsfall=='geldrente_760':
        if qualifizierte_dauer is not None or qualifizierte_einheit is not None:
            _fehler('qualifizierte_dauer','Im gesetzlichen Geldrentenfall Sonderdauer und Einheit ausdrücklich null.')
        anzahl,einheit = 3,'monate'
    else:
        anzahl = _ganzzahl(qualifizierte_dauer,'qualifizierte_dauer',1,3652059)
        _auswahl(qualifizierte_einheit,'qualifizierte_einheit',('tage','wochen','monate','jahre'))
        einheit = qualifizierte_einheit
    wert = dict(rechnerische_befreiungsgrenze=_frist(bezugstag_am,anzahl,einheit,beginnart).isoformat())
    eingaben = dict(zeitabschnittsfall=zeitabschnittsfall, bezugstag_am=bezugstag_am, beginnart=beginnart, qualifizierte_dauer=qualifizierte_dauer, qualifizierte_einheit=qualifizierte_einheit, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'datum','BGB_UNTERHALT_VORAUSLEISTUNG_ZEITGRENZE',eingaben,[dict(operation='Gesetzliche Dreimonatsdauer oder ausdrücklich rechtlich qualifizierte Sonderdauer auswählen und Zeitraum mit vorhandener Kalenderbibliothek berechnen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§1614II in Verbindung mit760II: nur zeitliche Grenze der befreienden Wirkung einer Vorausleistung bei erneuter Bedürftigkeit, kein wirksamer Verzicht auf künftigen Unterhalt. Im gesetzlichen Geldrentenfall drei Kalendermonate. Bei anderer Rente den nach Beschaffenheit/Zweck bestimmten Zeitabschnitt vorqualifizieren. Die angemessene Sonderdauer gilt nur, wenn der Verpflichtete den Zeitabschnitt rechtlich selbst zu bestimmen hatte, nicht schon bei jeder tatsächlich von ihm gewählten Vorauszahlung. Maßgeblichen Beginn und Beginnart rechtlich bestimmen; keine automatische neue Dreimonatsfrist ab erneuter Bedürftigkeit, keine Gleichsetzung von Zahlungstag und Periodenbeginn. Betrag, Bedarfsentwicklung, ausreichende Vorausleistung und weitere Unterhaltsvoraussetzungen separat. Keine eigenständige Angemessenheitsbewertung oder pauschale90Tage-Annahme.']
    return ergebnis

