"""Normgebundene familienrechtliche Grundfristen mit gemeinsamem Kalenderkern."""
from .kalender import _datum, _ergebnis, _fehler, _frist, _text

_FAMILIENFRISTEN = {'verloebnis_verjaehrung': (3, 'jahre'), 'rueckkehrabsicht_ehewohnung': (6, 'monate'), 'ehegatten_genehmigung': (2, 'wochen'), 'vormundverein_mitteilung': (2, 'wochen'), 'vormund_bestellung': (3, 'monate'), 'vormund_bereitschaft': (4, 'wochen'), 'vormund_nachholantrag': (6, 'monate'), 'betreuungsverein_mitteilung': (2, 'wochen'), 'betreuer_genehmigungsmitteilung': (2, 'kalenderfolgemonsende'), 'betreuer_aufwendungsersatz': (15, 'monate'), 'ehefaehigkeitsbefreiung': (6, 'monate'), 'eheaufhebung_irrtum_taeuschung': (1, 'jahre'), 'eheaufhebung_drohung': (3, 'jahre'), 'eheaufhebung_eigenantrag': (6, 'monate'), 'eheaufhebung_todeserklaerung': (1, 'jahre'), 'scheidung_ehewohnung_mietanspruch': (1, 'jahre'), 'scheidung_betreuungsunterhalt': (3, 'jahre'), 'unterhaltsauskunft_wiederholung': (2, 'jahre'), 'unterhalt_sonderbedarf': (1, 'jahre'), 'geburtsname_bestimmung': (1, 'monate'), 'adoption_elterneinwilligung': (3, 'jahre'), 'betreuung_anfangsbericht': (3, 'monate')}

def familienrecht_grundfrist(ereignis_am=None, fristfall=None, ereignisnachweis=None):
    """Fest bestimmte gesetzliche familienrechtliche Grundfrist berechnen."""
    ereignis = _datum(ereignis_am, 'ereignis_am')
    _text(fristfall, 'fristfall')
    _text(ereignisnachweis, 'ereignisnachweis')
    if fristfall not in _FAMILIENFRISTEN:
        _fehler('fristfall', 'Unbekannte gesetzliche familienrechtliche Grundfrist.')
    dauer, einheit = _FAMILIENFRISTEN[fristfall]
    if einheit == 'kalenderfolgemonsende':
        ende = _frist(f'{ereignis.year:04d}-{ereignis.month:02d}-01', 3, 'monate', 'tagesbeginn')
    else:
        ende = _frist(ereignis_am, dauer, einheit, 'ereignis')
    eingaben = dict(ereignis_am=ereignis_am, fristfall=fristfall, ereignisnachweis=ereignisnachweis)
    ergebnis = _ergebnis(ende.isoformat(), 'datum', 'BGB_FAMILIENRECHT_GRUNDFRIST', eingaben, [dict(operation='Feste normgebundene Dauer ab qualifiziertem Ereignis mit Kalenderkern;§1856II bis Ende des zweiten Folgemonats.')], eingaben.copy())
    ergebnis['hinweise'] = ['Nur gesetzliche Grundfrist, kein Wirksamkeits-, Anspruchs- oder Erlöschensurteil. Ereignisse rechtlich qualifizieren und Regeln nicht frei wählen. Hemmung, Ablaufhemmung, Neubeginn, gerichtliche Fristabweichungen/-verlängerungen und eine einschlägige§193-Verschiebung gesondert anwenden. Alsbald-Pflichten bleiben trotz Höchstfrist bestehen. Bei§1856II endet die Frist am letzten Tag des zweiten Folgemonats, auch bei Aufforderung am ersten Monatstag; keine bloße Addition zweier Monate zum Empfangstag. Verjährung§1302 benötigt außerhalb des ungestörten Grundfalls weitere Berechnung.']
    return ergebnis

def ehefaehigkeitszeugnis_geltungsende(ausstellung_am=None, urkundenende_am=None):
    """Sechsmonatige Zeugnisgeltung gegebenenfalls auf frühere Urkundengeltung begrenzen."""
    ausstellung = _datum(ausstellung_am, 'ausstellung_am')
    hoechstende = _frist(ausstellung_am, 6, 'monate', 'ereignis')
    urkundenende = None
    if urkundenende_am is not None:
        urkundenende = _datum(urkundenende_am, 'urkundenende_am')
        if urkundenende < ausstellung:
            _fehler('urkundenende_am', 'Urkundenende darf nicht vor Ausstellung liegen.')
    ende = hoechstende if urkundenende is None else min(hoechstende, urkundenende)
    eingaben = dict(ausstellung_am=ausstellung_am, urkundenende_am=urkundenende_am)
    ergebnis = _ergebnis(ende.isoformat(), 'datum', 'BGB_EHEFAEHIGKEITSZEUGNIS_GELTUNGSENDE', eingaben, [dict(operation='Ausstellung plus sechs Monate; frühere qualifizierte Urkundengeltung als Obergrenze berücksichtigen.')], eingaben.copy())
    ergebnis['hinweise'] = ['§1309I3, nur Zeugnisgeltung. In der Urkunde angegebene kürzere Dauer vorab in rechtlich maßgeblichen letzten Geltungstag umsetzen; fehlende Begrenzung als NULL. Späteres Urkundenende verlängert die gesetzliche Sechsmonatsgrenze nicht. Keine automatische Prüfung von Ehefähigkeit, Herkunft, Befreiung oder Eheschließung. Keine Verlängerung einer materiellen Geltungsdauer durch Wochenende/Feiertag.']
    return ergebnis
