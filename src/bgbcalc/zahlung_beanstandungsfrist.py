from .kalender import _datum, _ergebnis, _fehler, _frist, _text

def zahlung_beanstandungsfrist(belastung_am=None, ordnungsgemaesse_unterrichtung_am=None, beanstandung_am=None, einordnungsnachweis=None):
    """Spaeteren qualifizierten Belastungs-/Unterrichtungstag bestimmen,13Monatsgrundfrist berechnen und Beanstandung vergleichen; bei fehlender Unterrichtung kein Fristende erfinden."""
    b=_datum(belastung_am,'belastung_am');a=_datum(beanstandung_am,'beanstandung_am');_text(einordnungsnachweis,'einordnungsnachweis')
    if a<b: _fehler('beanstandung_am','Beanstandung der betrachteten Belastung nicht vor Belastungstag.')
    u=None if ordnungsgemaesse_unterrichtung_am is None else _datum(ordnungsgemaesse_unterrichtung_am,'ordnungsgemaesse_unterrichtung_am')
    beginn=None if u is None else max(b,u);ende=None if beginn is None else _frist(beginn.isoformat(),13,'monate','ereignis')
    wert=dict(massgeblicher_fristbeginn=None if beginn is None else beginn.isoformat(),rechnerisches_grundfristende=None if ende is None else ende.isoformat(),beanstandung_bis_grundfristende=None if ende is None else a<=ende)
    eingaben = dict(belastung_am=belastung_am, ordnungsgemaesse_unterrichtung_am=ordnungsgemaesse_unterrichtung_am, beanstandung_am=beanstandung_am, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'daten_und_wahrheitswert','BGB_ZAHLUNG_BEANSTANDUNGSFRIST',eingaben,[dict(operation='Spaeteren qualifizierten Belastungs-/Unterrichtungstag bestimmen,13Monatsgrundfrist berechnen und Beanstandung vergleichen; bei fehlender Unterrichtung kein Fristende erfinden.')],eingaben.copy())
    ergebnis["hinweise"] = ['§676bII/IV:13Monate ab Belastung, bei spaeterer ordnungsgemaesser Unterrichtung erst ab dieser; vollstaendig fehlende Unterrichtung startet keinen fiktiven Fristlauf. Fehlendes Fristende ist keine Behauptung unbegrenzter Anspruchsdauer: allgemeine Verjaehrung und unverzuegliche Meldung676bI bleiben getrennt. Fristende nach187I/188, kein pauschales390Tage-Fenster. Beanstandung vor spaeterer formeller Unterrichtung kann die Ausschlussfrist bereits wahren.676bIII/Vunverschuldete Verhinderung bei dort genannten anderen Anspruechen ist qualitative Ausnahme ohne feste weitere Tageszahl; keine automatische6Monatsverlaengerung oder erfundenes Nachfristende.676cHaftungsausschluesse sind qualitative Tatbestaende ohne zusaetzliche feste Rechenregel.193gegebenenfalls mit bestehendem Kern nach rechtlicher Qualifikation, keine automatische Verschiebung.']
    return ergebnis

