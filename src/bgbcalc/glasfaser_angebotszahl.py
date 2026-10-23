from .kalender import _ergebnis, _ganzzahl, _text

def glasfaserbereitstellung_angebotszahl(anzahl_qualifizierter_angebote=None, einordnungsnachweis=None):
    """Qualifizierte Angebotsanzahl mit gesetzlicher Zahl drei vergleichen."""
    anzahl=_ganzzahl(anzahl_qualifizierter_angebote,'anzahl_qualifizierter_angebote',0,9007199254740991)
    _text(einordnungsnachweis,'einordnungsnachweis')
    wert=dict(mindestens_drei_angebote=anzahl>=3,fehlende_angebote_bis_drei=max(3-anzahl,0))
    eingaben = dict(anzahl_qualifizierter_angebote=anzahl_qualifizierter_angebote, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'anzahl_und_wahrheitswert','BGB_GLASFASERBEREITSTELLUNG_ANGEBOTSZAHL',eingaben,[dict(operation='Qualifizierte Angebotsanzahl mit gesetzlicher Zahl drei vergleichen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§556IIIa: Anzahl qualifizierter rechtzeitig eingeholter Angebote mit drei vergleichen und fehlende Zahl bis drei berechnen. Der Gesetzesvorbehalt soweit möglich und die Auswahl des wirtschaftlichsten Angebots werden nicht automatisch entschieden. Weniger als drei bedeutet daher kein automatisch unwirksames Bereitstellungsentgelt; drei oder mehr beweist keine Wirtschaftlichkeit. Keine TKG-Entgelthöhen oder erfundenen Kostenkennzahlen.']
    return ergebnis

