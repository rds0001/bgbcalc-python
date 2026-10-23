from .kalender import _datum, _ergebnis, _fehler, _frist, _text

def landpacht_dreijahres_restlaufzeit(beurteilungsbeginn_am=None, beginnart=None, pachtende_am=None, einordnungsnachweis=None):
    """Dreijährige Restlaufzeit streng unterschreiten."""
    beginn=_datum(beurteilungsbeginn_am,'beurteilungsbeginn_am');ende=_datum(pachtende_am,'pachtende_am');_text(einordnungsnachweis,'einordnungsnachweis')
    if ende<beginn: _fehler('pachtende_am','Vertragsende darf nicht vor dem Beurteilungsbeginn liegen.')
    grenze=_frist(beurteilungsbeginn_am,3,'jahre',beginnart)
    wert=dict(dreijahreszeitraum_letzter_tag=grenze.isoformat(),restlaufzeit_weniger_als_drei_jahre=ende<grenze)
    eingaben = dict(beurteilungsbeginn_am=beurteilungsbeginn_am, beginnart=beginnart, pachtende_am=pachtende_am, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'datum_und_wahrheitswert','BGB_LANDPACHT_DREIJAHRES_RESTLAUFZEIT',eingaben,[dict(operation='Dreijährige Restlaufzeit streng unterschreiten.')],eingaben.copy())
    ergebnis["hinweise"] = ['§§590II/591II: Ende eines Dreijahreszeitraums ab qualifiziertem Bezugstag mit dem letzten Vertragstag vergleichen. Strikt früheres Pachtende bedeutet weniger als drei Jahre; Gleichheit genügt nicht. Keine automatische gerichtliche Erlaubnis, keine Festlegung des juristischen Beurteilungszeitpunkts. Nur kalendertäglich eindeutig normalisierte Zeitpunkte, keine ungeklärten untertägigen Grenzfälle.']
    return ergebnis

