"""Gesetzliche Sonderfristen zu Verein, Verbrauchsstiftung und Vollmachtsurkunde."""
from .betraege import _wahrheitswert
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _text


def _allgemeine_fristausgabe(wert, regel, eingaben, operation, hinweis):
    ergebnis = _ergebnis(wert, 'daten_und_wahrheitswerte', regel, eingaben,
        [dict(operation=operation)], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Rechtlich maßgebliche Ereignisse und Anwendungsbereich qualifiziert vorgegeben; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = [hinweis]
    return ergebnis


def verein_mitgliederschwund_antragsfrist(unterschreiten_am=None, einordnungsnachweis=None):
    """§73: Dreimonatsgrundfrist nach Unterschreiten von drei Mitgliedern."""
    _datum(unterschreiten_am, 'unterschreiten_am')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    ende = _frist(unterschreiten_am, 3, 'monate', 'ereignis')
    return _allgemeine_fristausgabe(dict(rechnerisches_antragsfristende=ende.isoformat()),
        'BGB_VEREIN_MITGLIEDERSCHWUND_ANTRAGSFRIST',
        dict(unterschreiten_am=unterschreiten_am, einordnungsnachweis=einordnungsnachweis),
        'Qualifiziertes Unterschreiten von drei Vereinsmitgliedern plus drei Kalendermonate',
        'Nur Grundfrist§73 ab rechtlich maßgeblichem Unterschreiten, nicht ab späterer Kenntnis des Vorstands. Schwelle unter drei mit vereins_mitgliederschwellen prüfen; genau drei genügt nicht. Rechtlich relevanten Verlauf einschließlich Wiederanstieg vorgeben. Keine automatische Entziehung der Rechtsfähigkeit: Antrag, Anhörung und gerichtliche Entscheidung gesondert. Gegebenenfalls einschlägige Kalender-/Verfahrenskorrekturen separat, keine pauschale Feiertagsverschiebung.')


def vollmachtsurkunde_kraftlosigkeitsfrist(letzte_einrueckung_am=None, vollmacht_widerruflich=None, einordnungsnachweis=None):
    """§176: Einmonatige Frist nach letzter Veröffentlichung der Kraftloserklärung."""
    _datum(letzte_einrueckung_am, 'letzte_einrueckung_am')
    _wahrheitswert(vollmacht_widerruflich, 'vollmacht_widerruflich')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    ende = _frist(letzte_einrueckung_am, 1, 'monate', 'ereignis')
    return _allgemeine_fristausgabe(dict(kraftlosigkeitsfristende=ende.isoformat()) if vollmacht_widerruflich else None,
        'BGB_VOLLMACHTSURKUNDE_KRAFTLOSIGKEITSFRIST',
        dict(letzte_einrueckung_am=letzte_einrueckung_am, vollmacht_widerruflich=vollmacht_widerruflich, einordnungsnachweis=einordnungsnachweis),
        'Letzte rechtlich maßgebliche Einrückung plus ein Kalendermonat; Wirkung mit Ablauf des Endtags',
        'Nur§176-Kraftloserklärung nach ordnungsgemäß bewilligter und veröffentlichter Bekanntmachung. Letzte Einrückung, nicht erste Veröffentlichung oder bloßer Vollmachtswiderruf. Bei nicht widerruflicher Vollmacht NICHT_ANWENDBAR wegen Absatz3; kein berechneter Wirksamkeitstag. Gerichtliche Zuständigkeit, ZPO-Veröffentlichungsvoraussetzungen und sonstige Wirksamkeit qualifiziert vorgeben. Wirkung mit Tagesablauf; keine automatische§193-Verschiebung dieser Wirkungsfrist.')


def verbrauchsstiftung_mindestdauer(errichtungsbeginn_am=None, errichtungsende_am=None, beginnart=None, einordnungsnachweis=None):
    """§82 Satz2: mindestens zehn Kalenderjahre Errichtungsdauer."""
    beginn = _datum(errichtungsbeginn_am, 'errichtungsbeginn_am')
    ende = _datum(errichtungsende_am, 'errichtungsende_am')
    _auswahl(beginnart, 'beginnart', ('ereignis', 'tagesbeginn'))
    _text(einordnungsnachweis, 'einordnungsnachweis')
    if ende < beginn:
        _fehler('errichtungsende_am', 'Errichtungsende darf nicht vor dem Beginn liegen.')
    mindestende = _frist(errichtungsbeginn_am, 10, 'jahre', beginnart)
    return _allgemeine_fristausgabe(dict(zehnjahres_mindestende=mindestende.isoformat(), mindestdauer_erreicht=ende >= mindestende),
        'BGB_VERBRAUCHSSTIFTUNG_MINDESTDAUER',
        dict(errichtungsbeginn_am=errichtungsbeginn_am, errichtungsende_am=errichtungsende_am, beginnart=beginnart, einordnungsnachweis=einordnungsnachweis),
        'Zehnjahresende mit qualifizierter Beginnart berechnen und einschließliches Satzungsende damit vergleichen',
        'Nur numerische Zehnjahresvoraussetzung§82 Satz2 einer Verbrauchsstiftung. Beginnart nach rechtlich bestimmtem Satzungszeitraum; errichtungsende_am ist dessen letzter eingeschlossener Tag mit Ende am Tagesablauf. Kein automatisch gleichmäßiger Vermögensverbrauch und keine3650-Tage-Näherung. Nachhaltige Zweckerfüllung, Satzungsanforderungen und Anerkennung insgesamt bleiben gesondert; FALSE ist keine automatische Ablehnung der Stiftung. Keine Feiertagsverlängerung einer Errichtungsdauer.')
