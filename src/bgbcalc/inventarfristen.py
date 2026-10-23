"""Grundrahmen und Wiederherstellungsantrag der Inventarfrist (§§1995–1997)."""
from .betraege import _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler, _frist, _text


def inventarfrist_grundrahmen(zustellung_fristbeschluss_am=None, annahme_erbschaft_am=None,
    bestimmtes_grundfristende=None, erstmalige_inventarfrist=None, einordnungsnachweis=None):
    """Beginn nicht vor Zustellung/Annahme; Sollrahmen ein bis drei Monate für Erstbestimmung."""
    zustellung = _datum(zustellung_fristbeschluss_am, 'zustellung_fristbeschluss_am')
    annahme = _datum(annahme_erbschaft_am, 'annahme_erbschaft_am')
    ende = _datum(bestimmtes_grundfristende, 'bestimmtes_grundfristende')
    beginn = max(zustellung, annahme)
    if ende < beginn:
        _fehler('bestimmtes_grundfristende', 'Bestimmtes Grundfristende darf nicht vor dem maßgeblichen Beginn liegen.')
    _wahrheitswert(erstmalige_inventarfrist, 'erstmalige_inventarfrist')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    eingaben = dict(zustellung_fristbeschluss_am=zustellung_fristbeschluss_am,
        annahme_erbschaft_am=annahme_erbschaft_am, bestimmtes_grundfristende=bestimmtes_grundfristende,
        erstmalige_inventarfrist=erstmalige_inventarfrist, einordnungsnachweis=einordnungsnachweis)
    wert = None
    if erstmalige_inventarfrist:
        minimum = _frist(beginn.isoformat(), 1, 'monate', 'ereignis')
        maximum = _frist(beginn.isoformat(), 3, 'monate', 'ereignis')
        wert = dict(fristbeginnereignis_am=beginn.isoformat(), einmonatsgrenze=minimum.isoformat(),
            dreimonatsgrenze=maximum.isoformat(), bestimmtes_ende_im_sollrahmen=minimum <= ende <= maximum)
    ergebnis = _ergebnis(wert, 'daten_und_wahrheitswert', 'BGB_INVENTARFRIST_GRUNDRAHMEN', eingaben,
        [dict(operation='Späteren Tag von Zustellung und Annahme als Beginn; Ein-/Dreimonatsgrenzen des gesetzlichen Sollrahmens berechnen')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Tatsächliche Zustellung, wirksame Annahme und erstmalige gerichtliche Grundfristbestimmung vorgegeben; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['§1995 Absatz1 enthält einen Sollrahmen, keine automatische Unwirksamkeit jedes außerhalb liegenden gerichtlichen Termins. Ergebnis beurteilt nur den rechnerischen Rahmen der Erstbestimmung. Annahme kann ausdrücklich oder rechtlich anderweitig erfolgt sein und ist nicht automatisch Erbfalltag. Vor Annahme bestimmte Frist beginnt nicht vor Annahme; spätere Zustellung bleibt ebenfalls Startgrenze. Gerichtliche Verlängerung nach Absatz3 nicht auf drei Monate kappen und nicht ohne gerichtliche Entscheidung annehmen. Ablaufhemmung§1997/210, Sonderfall Ehegatten§2008 und zulässige Kalenderkorrekturen separat; bestimmtes_grundfristende ist die zum unbereinigten Rahmen vergleichbare Grundgrenze. Keine automatische Ermittlung eines endgültigen Inventarablaufs oder unbeschränkter Erbenhaftung.']
    return ergebnis


def inventarfrist_neubestimmungsantrag(hindernis_beseitigt_am=None,
    ende_zuerst_bestimmter_inventarfrist=None, massgebliches_zweiwochenfristende=None,
    massgebliche_jahreshoechstgrenze=None, antrag_massgeblich_gestellt_am=None,
    unverschuldete_verhinderung=None, einordnungsnachweis=None):
    """Zwei Wochen ab Hindernisbeseitigung, begrenzt durch ein Jahr ab erster Inventarfrist."""
    beseitigt = _datum(hindernis_beseitigt_am, 'hindernis_beseitigt_am')
    _datum(ende_zuerst_bestimmter_inventarfrist, 'ende_zuerst_bestimmter_inventarfrist')
    korrigiert = _datum(massgebliches_zweiwochenfristende, 'massgebliches_zweiwochenfristende')
    jahresgrenze = _datum(massgebliche_jahreshoechstgrenze, 'massgebliche_jahreshoechstgrenze')
    antrag = _datum(antrag_massgeblich_gestellt_am, 'antrag_massgeblich_gestellt_am')
    grundende = _frist(hindernis_beseitigt_am, 2, 'wochen', 'ereignis')
    hoechstende = _frist(ende_zuerst_bestimmter_inventarfrist, 1, 'jahre', 'ereignis')
    if korrigiert < grundende:
        _fehler('massgebliches_zweiwochenfristende', 'Maßgebliches Zweiwochenende darf die Grundfrist nicht verkürzen.')
    if jahresgrenze < hoechstende:
        _fehler('massgebliche_jahreshoechstgrenze', 'Maßgebliche Jahresgrenze darf die gesetzliche Jahresgrundgrenze nicht verkürzen.')
    if antrag < beseitigt:
        _fehler('antrag_massgeblich_gestellt_am', 'Antrag vor Hindernisbeseitigung außerhalb dieses Fristmodells.')
    _wahrheitswert(unverschuldete_verhinderung, 'unverschuldete_verhinderung')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    eingaben = dict(hindernis_beseitigt_am=hindernis_beseitigt_am,
        ende_zuerst_bestimmter_inventarfrist=ende_zuerst_bestimmter_inventarfrist,
        massgebliches_zweiwochenfristende=massgebliches_zweiwochenfristende,
        massgebliche_jahreshoechstgrenze=massgebliche_jahreshoechstgrenze,
        antrag_massgeblich_gestellt_am=antrag_massgeblich_gestellt_am,
        unverschuldete_verhinderung=unverschuldete_verhinderung, einordnungsnachweis=einordnungsnachweis)
    ende = min(korrigiert, jahresgrenze)
    wert = dict(rechnerisches_zweiwochenfristende=grundende.isoformat(), jahreshoechstgrenze=hoechstende.isoformat(),
        massgeblicher_letzter_antragstag=ende.isoformat(), antragsfrist_eingehalten=antrag <= ende,
        verhinderung_und_frist_erfuellt=unverschuldete_verhinderung and antrag <= ende)
    ergebnis = _ergebnis(wert, 'daten_und_wahrheitswerte', 'BGB_INVENTARFRIST_NEUBESTIMMUNGSANTRAG', eingaben,
        [dict(operation='Zweiwochenfrist nach Hindernisbeseitigung mit absoluter Jahresgrenze ab zuerst bestimmtem Inventarfristende begrenzen; unverschuldete Verhinderung gesondert einbeziehen')], eingaben.copy())
    ergebnis['annahmen'] = ['Unverschuldete Verhinderung, Hindernisbeseitigung, erste Inventarfrist und rechtlicher Antragstag qualifiziert vorgegeben; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['§1996 Absatz1 erfasst unverschuldete Verhinderung an Inventarerrichtung, gerechtfertigtem Verlängerungsantrag oder Einhaltung der Zweiwochenfrist. Keine automatische Bewertung des Verschuldens. §1997 verweist für die Zweiwochenfrist auf§210; solche Korrektur im maßgeblichen Zweiwochenende belegen. Die Jahresgrenze ist gesondert einschließlich nur rechtlich zulässiger Kalenderkorrekturen vorzugeben; die Verweisung auf§210 in§1997 betrifft gerade nicht diese Jahresgrenze. Keine frei wählbare Verlängerung. Jahresgrenze bezieht sich auf Ende der zuerst bestimmten Frist und wird hier nicht durch erneute Anträge oder spätere Grundfristen neu gestartet. Späte Hindernisbeseitigung kann hinter der Jahresgrenze liegen und lässt diese nicht entfallen. Taggenau bis Ablauf des letzten Tages, rechtlichen Antragseingang statt Versand vorgeben. Gerichtliche Neubestimmung und Anhörung§1996 Absatz3 erfolgen nicht durch diese Berechnung; TRUE ist keine automatische gerichtliche Bewilligung.']
    return ergebnis
