from .betraege import _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler, _frist, _text

def miete_schonfrist_wiederholungszeitraum(fruehere_geheilte_kuendigung_am=None, erneute_kuendigung_am=None, einordnungsnachweis=None):
    """Frühere geheilte Kündigung um zwei Jahre fortschreiben und erneute Kündigung einschließlich des Grenztags vergleichen."""
    frueher = _datum(fruehere_geheilte_kuendigung_am,'fruehere_geheilte_kuendigung_am')
    erneut = _datum(erneute_kuendigung_am,'erneute_kuendigung_am')
    if erneut <= frueher:
        _fehler('erneute_kuendigung_am','Erneute Kündigung muss nach früherer Kündigung liegen.')
    ende = _frist(fruehere_geheilte_kuendigung_am,2,'jahre','ereignis')
    wert = dict(zweijahresgrenze=ende.isoformat(),innerhalb_wiederholungszeitraum=erneut<=ende)
    _text(einordnungsnachweis,"einordnungsnachweis")
    eingaben = dict(fruehere_geheilte_kuendigung_am=fruehere_geheilte_kuendigung_am, erneute_kuendigung_am=erneute_kuendigung_am, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,"daten_und_wahrheitswerte",'BGB_MIETE_SCHONFRIST_WIEDERHOLUNGSZEITRAUM',eingaben,[dict(operation='Frühere geheilte Kündigung um zwei Jahre fortschreiben und erneute Kündigung einschließlich des Grenztags vergleichen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§569III2Satz2: erneute Kündigung innerhalb von einschließlich zwei Jahren nach früherer, durch Schonfrist unwirksam gewordener Kündigung. Eine bloß erfolgte Mietzahlung ohne diese frühere Heilung genügt nicht als Bezugsvorgang. Zeitraum keine Handlungsfrist; keine193Verschiebung. Ergebnis betrifft nur die Wiederholungsgrenze der Schonfrist, nicht jede Zahlung, Aufrechnung oder sonstige Unwirksamkeit der neuen Kündigung.']
    return ergebnis

def kauf_digitale_mindesthaftungsdauer(ablieferung_am=None, bereitstellung_bis=None, bereitstellung_unbefristet=None, einordnungsnachweis=None):
    """Zweijahresgrenze ab Ablieferung berechnen und mit qualifiziertem Bereitstellungsende das spätere Ende bestimmen."""
    lieferung = _datum(ablieferung_am,'ablieferung_am')
    _wahrheitswert(bereitstellung_unbefristet,'bereitstellung_unbefristet')
    if bereitstellung_unbefristet:
        if bereitstellung_bis is not None:
            _fehler('bereitstellung_bis','Bei unbefristeter Bereitstellung kein bestimmtes Ende einsetzen.')
        ende = None
    else:
        ende = _datum(bereitstellung_bis,'bereitstellung_bis')
        if ende < lieferung:
            _fehler('bereitstellung_bis','Bereitstellungsende darf nicht vor Ablieferung liegen.')
    mindestende = _frist(ablieferung_am,2,'jahre','ereignis')
    wert = dict(zweijahresgrenze=mindestende.isoformat(),massgebliches_zeitraumende=None if ende is None else max(ende,mindestende).isoformat())
    _text(einordnungsnachweis,"einordnungsnachweis")
    eingaben = dict(ablieferung_am=ablieferung_am, bereitstellung_bis=bereitstellung_bis, bereitstellung_unbefristet=bereitstellung_unbefristet, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,"daten_und_wahrheitswerte",'BGB_KAUF_DIGITALE_MINDESTHAFTUNGSDAUER',eingaben,[dict(operation='Zweijahresgrenze ab Ablieferung berechnen und mit qualifiziertem Bereitstellungsende das spätere Ende bestimmen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§475cII: zeitlicher Umfang der Anforderungen an dauerhaft bereitzustellende digitale Elemente, mindestens zwei Jahre ab Ablieferung. Bei längerem qualifizierten Bereitstellungszeitraum gilt dessen Ende; bei unbefristeter Bereitstellung kein bestimmtes Gesamtende. Keine Verjährungsfrist und keine Beweislastvermutung477II; Mangel, übrige Anspruchsvoraussetzungen und rechtliche Bestimmung des Bereitstellungszeitraums separat. Keine193Verschiebung. Nur hier festgelegte endliche oder tatsächlich unbefristete Dauer; unbekannte Dauer darf nicht als unbefristet eingesetzt werden.']
    return ergebnis

