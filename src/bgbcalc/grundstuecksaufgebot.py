"""Zeit- und Statusvoraussetzungen des Grundstücksaufgebots (§927 Absatz1)."""
from .betraege import _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler, _frist, _text


def grundstuecksaufgebot_voraussetzungen(
    eigenbesitzbeginn_am=None, prueftag=None, einfacher_eigenbesitzzeitraum=None,
    eigentuemer_im_grundbuch_eingetragen=None, eigentuemer_gestorben_oder_verschollen=None,
    letzte_zustimmungsbeduerftige_eintragung_am=None, einordnungsnachweis=None,
):
    """Zwei gegebenenfalls kumulative Dreißigjahresgrenzen und Eigentümerstatus prüfen."""
    beginn = _datum(eigenbesitzbeginn_am, 'eigenbesitzbeginn_am')
    tag = _datum(prueftag, 'prueftag')
    if beginn > tag:
        _fehler('eigenbesitzbeginn_am', 'Eigenbesitzbeginn darf nicht nach dem Prüftag liegen.')
    eintragung = (_datum(letzte_zustimmungsbeduerftige_eintragung_am, 'letzte_zustimmungsbeduerftige_eintragung_am')
        if letzte_zustimmungsbeduerftige_eintragung_am is not None else None)
    if eintragung is not None and eintragung > tag:
        _fehler('letzte_zustimmungsbeduerftige_eintragung_am', 'Letzte Eintragung darf nicht nach dem Prüftag liegen.')
    eingaben = dict(eigenbesitzbeginn_am=eigenbesitzbeginn_am, prueftag=prueftag,
        einfacher_eigenbesitzzeitraum=einfacher_eigenbesitzzeitraum,
        eigentuemer_im_grundbuch_eingetragen=eigentuemer_im_grundbuch_eingetragen,
        eigentuemer_gestorben_oder_verschollen=eigentuemer_gestorben_oder_verschollen,
        letzte_zustimmungsbeduerftige_eintragung_am=letzte_zustimmungsbeduerftige_eintragung_am,
        einordnungsnachweis=einordnungsnachweis)
    for name in tuple(eingaben)[2:5]:
        _wahrheitswert(eingaben[name], name)
    _text(einordnungsnachweis, 'einordnungsnachweis')
    besitzende = _frist(eigenbesitzbeginn_am, 30, 'jahre', 'ereignis')
    grundbuchende = (_frist(letzte_zustimmungsbeduerftige_eintragung_am, 30, 'jahre', 'ereignis')
        if eigentuemer_im_grundbuch_eingetragen and eintragung is not None else None)
    besitzzeit = tag >= besitzende
    grundbuchruhe = grundbuchende is None or tag >= grundbuchende
    zusatz = not eigentuemer_im_grundbuch_eingetragen or (eigentuemer_gestorben_oder_verschollen and grundbuchruhe)
    wert = None if not einfacher_eigenbesitzzeitraum else dict(
        eigenbesitz_dreissigjahresende=besitzende.isoformat(),
        grundbuchruhe_dreissigjahresende=grundbuchende.isoformat() if grundbuchende is not None else None,
        eigenbesitzzeit_erfuellt=besitzzeit,
        zusatzvoraussetzungen_eingetragener_eigentuemer_erfuellt=zusatz,
        zeit_und_statusvoraussetzungen_erfuellt=besitzzeit and zusatz)
    ergebnis = _ergebnis(wert, 'daten_und_wahrheitswerte', 'BGB_GRUNDSTUECKSAUFGEBOT_VORAUSSETZUNGEN', eingaben,
        [dict(operation='30 Jahre Eigenbesitz; bei eingetragenem Eigentümer zusätzlich Tod oder Verschollenheit und 30 Jahre ohne zustimmungsbedürftige Eintragung')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if einfacher_eigenbesitzzeitraum else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Prüfung zum Ende des Prüftags; Eigenbesitz eines anderen als des Eigentümers und vollständige relevante Grundbuchhistorie rechtlich qualifiziert; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['Einfacher Eigenbesitzzeitraum bedeutet fortdauernder ungehemmter, ununterbrochener Eigenbesitz ohne anzurechnende Vorgängerzeit; andernfalls NICHT_ANWENDBAR und gesonderte Berechnung gemäß§927 Absatz1 Satz2. NULL bei letzter zustimmungsbedürftiger Eintragung bedeutet nach vollständig geprüfter Historie niemals eine solche Eintragung, nicht unbekannte Historie. Nur Eintragungen, die der Eigentümerzustimmung bedurften; nicht jede Grundbuchänderung. Ohne eingetragenen Eigentümer greifen die zusätzlichen Status-/Grundbuchruhevoraussetzungen nicht. Kein pauschales Erfordernis eines unbekannten Eigentümers aus dem Gesetzeswortlaut abgeleitet. Keine gerichtliche Zulässigkeitsentscheidung oder Eigentumsübertragung: Absatz2 verlangt Ausschließungsbeschluss und anschließende eigene Eigentümereintragung; Absatz3 schützt bestimmte vor Beschlusserlass eingetragene Drittrechte/Widersprüche. Andere Verfahrenserfordernisse und Ersitzungsregeln separat. Keine automatische Feiertagsverschiebung.']
    return ergebnis
