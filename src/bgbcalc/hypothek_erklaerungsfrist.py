from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _text, _vorhanden, werktagsverschiebung
from .betraege import _wahrheitswert

def hypothek_widerspruchs_und_meldungsfrist(fristfall=None, ausloeser_am=None, erklaerung_am=None, werktagskorrektur_anwendbar=None, feiertagskalender=None, einordnungsnachweis=None):
    """Hypothekenbezogene Erklärungs-/Meldungsgrundfrist berechnen und tatsächlichen Eingang vergleichen."""
    _auswahl(fristfall,'fristfall',('versicherung_anzeige_1128','versicherung_untunlich_1128','hinterlegung_meldung_1171'))
    eingang=_datum(erklaerung_am,'erklaerung_am');_wahrheitswert(werktagskorrektur_anwendbar,'werktagskorrektur_anwendbar');_text(einordnungsnachweis,'einordnungsnachweis')
    grund=_frist(ausloeser_am,30 if fristfall=='hinterlegung_meldung_1171' else 1,'jahre' if fristfall=='hinterlegung_meldung_1171' else 'monate','ereignis');ende=grund
    if werktagskorrektur_anwendbar:
        _vorhanden(feiertagskalender,'feiertagskalender')
        if not isinstance(feiertagskalender,dict) or set(feiertagskalender)!={'feiertage','ort','kalenderquelle','kalender_von','kalender_bis'}: _fehler('feiertagskalender','Vollständiges Kalenderobjekt erforderlich.')
        ende=_datum(werktagsverschiebung(datum=grund.isoformat(),anwendungsfall='willenserklaerung',**feiertagskalender)['wert'],'fristende')
    elif feiertagskalender is not None: _fehler('feiertagskalender','Ohne Korrektur ausdrücklich None verwenden.')
    wert=dict(grundfrist_letzter_tag=grund.isoformat(),frist_letzter_tag=ende.isoformat(),erklaerung_bis_fristende=eingang<=ende,kalendertage_vom_eingang_bis_fristende=(ende-eingang).days)
    eingaben = dict(fristfall=fristfall, ausloeser_am=ausloeser_am, erklaerung_am=erklaerung_am, werktagskorrektur_anwendbar=werktagskorrektur_anwendbar, feiertagskalender=feiertagskalender, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'daten_anzahl_und_wahrheitswert','BGB_HYPOTHEK_WIDERSPRUCHS_UND_MELDUNGSFRIST',eingaben,[dict(operation='Hypothekenbezogene Erklärungs-/Meldungsgrundfrist berechnen und tatsächlichen Eingang vergleichen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§1128I ein Monat ab qualifiziertem Auslöser;§1171III dreißig Jahre ab Rechtskraft. Grundfrist und gegebenenfalls rechtlich qualifizierte193-Korrektur über vorhandene Kalenderkerne berechnen; tatsächlichen Erklärungseingang bis einschließlich letztem Tag und verbleibenden Tagesabstand vergleichen. Keine automatische Auszahlung, Zustimmungsfiktion oder Erlöschensentscheidung; keine pauschale Gleichbehandlung von1128I und1128II.193-Anwendbarkeit ist rechtliche Voraussetzung, keine zusätzliche Zahlenschätzung. Keine untertägige Reihenfolge aus identischen Kalendertagen erfinden.']
    return ergebnis

