from .kalender import _ergebnis, _frist, _text

def landpacht_erbenkuendigung_quartalstermin(kuendigungszugang_am=None, einordnungsnachweis=None):
    """Sechsmonatige Kündigungsfrist auf nächstes zulässiges Kalenderquartalsende ausrichten."""
    _text(einordnungsnachweis,'einordnungsnachweis')
    grund=_frist(kuendigungszugang_am,6,'monate','ereignis')
    quartalsbeginn=3*((grund.month-1)//3)+1
    ende=_frist(f'{grund.year:04}-{quartalsbeginn:02}-01',3,'monate','tagesbeginn')
    wert=dict(sechsmonatige_kuendigungsfrist_letzter_tag=grund.isoformat(),rechnerischer_pachtendtermin=ende.isoformat())
    eingaben = dict(kuendigungszugang_am=kuendigungszugang_am, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'daten','BGB_LANDPACHT_ERBENKUENDIGUNG_QUARTALSTERMIN',eingaben,[dict(operation='Sechsmonatige Kündigungsfrist auf nächstes zulässiges Kalenderquartalsende ausrichten.')],eingaben.copy())
    ergebnis["hinweise"] = ['§594dI: sechs Kalendermonate ab tatsächlichem Kündigungszugang berechnen, anschließend erstes Kalenderquartalsende auswählen, das nicht vor dieser Fristgrenze liegt. Einmonatige Ausübungsfrist ab Kenntnis ist eigenständig; sechs Monate beginnen nicht schon mit Tod oder Kenntnis. Erbenwiderspruch594dII und Fortsetzungsentscheidung gesondert. Keine automatische Feiertagsverschiebung des Pachtendtermins.']
    return ergebnis

