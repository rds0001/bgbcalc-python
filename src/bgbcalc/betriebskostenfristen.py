from .kalender import _auswahl, _datum, _ergebnis, _frist, _text

def betriebskosten_grundfristende(fristfall=None, bezugsdatum=None, fristberechnung=None, einordnungsnachweis=None):
    """Zwölfmonatige Ereignisfrist nach187/188 berechnen; nur bei ausdrücklich ausgewählter Monatsendevariante auf den letzten Kalendertag dieses Zielmonats setzen."""
    _auswahl(fristfall,'fristfall',('abrechnung','einwendungen'))
    tag = _datum(bezugsdatum,'bezugsdatum')
    _auswahl(fristberechnung,'fristberechnung',('taggenau_zwoelf_monate','ende_zwoelfter_kalendermonat'))
    _text(einordnungsnachweis,'einordnungsnachweis')
    ende = _frist(tag.isoformat(),12,'monate','ereignis')
    if fristberechnung=='ende_zwoelfter_kalendermonat':
        ende = _frist(ende.replace(day=1).isoformat(),1,'monate','tagesbeginn')
    wert = dict(rechnerisches_fristende=ende.isoformat())
    eingaben = dict(fristfall=fristfall, bezugsdatum=bezugsdatum, fristberechnung=fristberechnung, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,"datum",'BGB_BETRIEBSKOSTEN_GRUNDFRISTENDE',eingaben,[dict(operation='Zwölfmonatige Ereignisfrist nach187/188 berechnen; nur bei ausdrücklich ausgewählter Monatsendevariante auf den letzten Kalendertag dieses Zielmonats setzen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§556III: zwei explizite Berechnungsweisen ohne automatische Auslegungsentscheidung. LGFrankfurt(Oder)20.11.2012,16S47/12 befürwortet Monatsende192 und dokumentiert die gegenteilige taggenaue Berechnung der Vorinstanz. Hieraus folgt keine Behauptung einer heute universell verbindlichen Auslegung; Auswahl rechtlich belegen. Grundfrist ohne193-Wochenend-/Feiertagskorrektur; diese bei feststehender Anwendbarkeit mit vorhandenem Kalenderkern nachführen. Kein automatischer Ausschluss von Nachforderung oder Einwendung: ordnungsgemäße Abrechnung, Zugang, Vertretenmüssen und Sonderfälle gesondert. Jährliche Abrechnungspflicht ist nicht identisch mit dem anschließenden Mitteilungszeitraum.']
    return ergebnis
