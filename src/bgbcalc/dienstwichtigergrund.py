"""Zweiwochenfrist und bewerteter wichtiger Grund der Dienstkündigung (§626)."""
from .betraege import _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler, _frist, _text


def dienst_ausserordentliche_kuendigungsfrist(kenntnis_massgeblicher_tatsachen_am=None,
    massgebliches_zweiwochenfristende=None, zugang_kuendigung=None,
    wichtiger_grund_nach_interessenabwaegung=None, kuendigungsregel_626_anwendbar=None,
    einordnungsnachweis=None):
    """§626: Zugang innerhalb zweier Wochen nach qualifizierter Kenntnis und wichtiger Grund."""
    kenntnis = _datum(kenntnis_massgeblicher_tatsachen_am, 'kenntnis_massgeblicher_tatsachen_am')
    ende = _datum(massgebliches_zweiwochenfristende, 'massgebliches_zweiwochenfristende')
    zugang = _datum(zugang_kuendigung, 'zugang_kuendigung')
    grundende = _frist(kenntnis_massgeblicher_tatsachen_am, 2, 'wochen', 'ereignis')
    if ende < grundende:
        _fehler('massgebliches_zweiwochenfristende', 'Maßgebliches Fristende darf die gesetzliche Zweiwochengrundfrist nicht verkürzen.')
    if zugang < kenntnis:
        _fehler('zugang_kuendigung', 'Kündigungszugang darf in diesem Kenntnisfall nicht vor der maßgeblichen Kenntnis liegen.')
    _wahrheitswert(wichtiger_grund_nach_interessenabwaegung, 'wichtiger_grund_nach_interessenabwaegung')
    _wahrheitswert(kuendigungsregel_626_anwendbar, 'kuendigungsregel_626_anwendbar')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    eingaben = dict(kenntnis_massgeblicher_tatsachen_am=kenntnis_massgeblicher_tatsachen_am,
        massgebliches_zweiwochenfristende=massgebliches_zweiwochenfristende, zugang_kuendigung=zugang_kuendigung,
        wichtiger_grund_nach_interessenabwaegung=wichtiger_grund_nach_interessenabwaegung,
        kuendigungsregel_626_anwendbar=kuendigungsregel_626_anwendbar, einordnungsnachweis=einordnungsnachweis)
    wert = dict(rechnerisches_zweiwochenfristende=grundende.isoformat(),
        zweiwochenfrist_eingehalten=zugang <= ende,
        grund_und_frist_626_erfuellt=wichtiger_grund_nach_interessenabwaegung and zugang <= ende) if kuendigungsregel_626_anwendbar else None
    ergebnis = _ergebnis(wert, 'datum_und_wahrheitswerte', 'BGB_DIENST_AUSSERORDENTLICHE_KUENDIGUNGSFRIST', eingaben,
        [dict(operation='Zwei Wochen ab Kenntnis der maßgebenden Tatsachen; rechtliches Fristende mit Zugang vergleichen und wichtigen Grund nach Interessenabwägung einbeziehen')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Kenntnis des Kündigungsberechtigten, maßgeblicher Zugang, zulässige Fristkorrekturen und wichtiger Grund rechtlich bestimmt; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['Kenntnis betrifft die für die Kündigung maßgebenden Tatsachen, nicht automatisch ersten Verdacht oder Eingang einer ungeprüften Meldung. Aufklärung/Zurechnung und etwaiger Dauer- oder Wiederholungssachverhalt vorab rechtlich bestimmen; kein automatischer Neubeginn durch spätere Kenntnis derselben Tatsachen. Wichtiger Grund erfordert Einzelfallumstände und Interessenabwägung einschließlich Unzumutbarkeit bis ordentlichem Fristende oder vereinbartem Vertragsende; kein pauschaler Punktwert. Maßgebliches Ende einschließlich rechtlich zulässiger Kalenderkorrekturen belegen, keine frei wählbare Verlängerung. TRUE bestätigt nur die beiden geprüften Anforderungen§626, nicht sämtliche Wirksamkeitsvoraussetzungen: Form, Vertretungsmacht, Anhörung und besondere Schutzregeln separat. Pflicht zur unverzüglichen schriftlichen Mitteilung des Grunds auf Verlangen nach Absatz2 Satz3 bleibt gesondert. Keine Kündigungserklärung wird durch diese Funktion abgegeben.']
    return ergebnis
