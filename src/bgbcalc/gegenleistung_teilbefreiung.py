from .betraege import _geld
from .kalender import _ergebnis, _fehler, _text
from .zahlen import _bruch, _dividieren, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile

def gegenleistung_teilbefreiung_betraege(vereinbarte_gegenleistung=None, wert_vollstaendiger_leistung=None, wert_verbleibender_teilleistung=None, darauf_gezahlter_betrag=None, einordnungsnachweis=None):
    """Gegenleistung mit Verhältnis verbleibender Teilleistung zur Gesamtleistung multiplizieren; entfallenen Preisanteil, gezahlten Mehrbetrag und offenen Rest getrennt bestimmen."""
    preis = _geld(vereinbarte_gegenleistung);voll = _geld(wert_vollstaendiger_leistung)
    teil = _geld(wert_verbleibender_teilleistung);bezahlt = _geld(darauf_gezahlter_betrag)
    if voll<=0:
        _fehler('wert_vollstaendiger_leistung','Positiver Vergleichswert erforderlich.')
    if teil>voll:
        _fehler('wert_verbleibender_teilleistung','Teilwert darf Gesamtwert nicht übersteigen.')
    if bezahlt>preis:
        _fehler('darauf_gezahlter_betrag','Sonstige über den Vertragspreis hinausgehende Zahlung separat behandeln.')
    _text(einordnungsnachweis,'einordnungsnachweis')
    verbleibend = _multiplizieren(preis,_dividieren(teil,voll))
    wert = dict(verbleibende_gegenleistung=_bruchteile(verbleibend),entfallener_gegenleistungsanteil=_bruchteile(_subtrahieren(preis,verbleibend)),rueckforderungsbetrag=_bruchteile(max(_subtrahieren(bezahlt,verbleibend),_bruch(0))),rechnerisch_offener_rest=_bruchteile(max(_subtrahieren(verbleibend,bezahlt),_bruch(0))))
    eingaben = dict(vereinbarte_gegenleistung=vereinbarte_gegenleistung, wert_vollstaendiger_leistung=wert_vollstaendiger_leistung, wert_verbleibender_teilleistung=wert_verbleibender_teilleistung, darauf_gezahlter_betrag=darauf_gezahlter_betrag, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,"EUR",'BGB_GEGENLEISTUNG_TEILBEFREIUNG_BETRAEGE',eingaben,[dict(operation='Gegenleistung mit Verhältnis verbleibender Teilleistung zur Gesamtleistung multiplizieren; entfallenen Preisanteil, gezahlten Mehrbetrag und offenen Rest getrennt bestimmen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§326I in Verbindung mit441III und326IV: qualifizierte Teilbefreiung, konsistente Vergleichswerte entsprechend441III; keine beliebige Mengen- oder Zeitquote und keine zusätzliche Minderungserklärung erforderlich.326I2 bei bloß nicht zu erbringender Nacherfüllung, Behaltensanspruch326II und Ersatzverlangen326III gesondert. Rückforderungsbetrag ist ausschließlich bereits auf den hier entfallenen Gegenleistungsanteil Gezahltes; weitere Rückgewährvoraussetzungen346–348 und gegenseitige Ansprüche gesondert. Keine automatische Aufrechnung oder zusätzliche Schadensberechnung. Bezugswert muss positiv sein; anderer Fall mit nicht bestimmbarem Wert nicht durch fiktive1 ersetzen.']
    return ergebnis
