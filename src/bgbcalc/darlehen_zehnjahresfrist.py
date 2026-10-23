from .kalender import _datum, _ergebnis, _fehler, _frist, _text, _vorhanden

def darlehen_zehnjahresfrist_nach_vereinbarungen(vollstaendiger_empfang_am=None, neue_vereinbarungen_am=None, einordnungsnachweis=None):
    """Jüngsten qualifizierten Bezugsakt auswählen und zehn Kalenderjahre berechnen."""
    empfang=_datum(vollstaendiger_empfang_am,'vollstaendiger_empfang_am');_text(einordnungsnachweis,'einordnungsnachweis')
    _vorhanden(neue_vereinbarungen_am,'neue_vereinbarungen_am')
    if not isinstance(neue_vereinbarungen_am,list) or len(neue_vereinbarungen_am)>1000: _fehler('neue_vereinbarungen_am','Liste0..1000 erforderlich.')
    bezug=empfang
    for datum in neue_vereinbarungen_am:
        tag=_datum(datum,'vereinbarung_am')
        if tag<empfang: _fehler('neue_vereinbarungen_am','Neue Vereinbarung darf nicht vor vollständigem Empfang liegen.')
        bezug=max(bezug,tag)
    ende=_frist(bezug.isoformat(),10,'jahre','ereignis')
    wert=dict(massgeblicher_bezugstag=bezug.isoformat(),zehnjahresfrist_letzter_tag=ende.isoformat())
    eingaben = dict(vollstaendiger_empfang_am=vollstaendiger_empfang_am, neue_vereinbarungen_am=neue_vereinbarungen_am, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'daten','BGB_DARLEHEN_ZEHNJAHRESFRIST_NACH_VEREINBARUNGEN',eingaben,[dict(operation='Jüngsten qualifizierten Bezugsakt auswählen und zehn Kalenderjahre berechnen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§489I2: Vollständiger Empfang als Ausgangspunkt, bei späteren qualifizierten Vereinbarungen jüngstes Vereinbarungsdatum; ab diesem Ereignistag zehn Kalenderjahre berechnen. Gleichdatierte Vereinbarungen verändern den Ausgangspunkt nicht mehrfach. Sechsmonatige Kündigungsfrist und Zweiwochenrückzahlung489III separat ab ihren jeweils tatsächlichen Auslösern. Keine automatische Fälligkeit, Kündigungserklärung oder Einstufung beliebiger Vertragsänderungen als Fristneustart.']
    return ergebnis

