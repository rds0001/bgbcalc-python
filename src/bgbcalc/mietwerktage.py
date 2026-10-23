from .bankgeschaeftstage import _bankkalender, _banktermin
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _tage_addieren, _text, _vorhanden

def miete_werktagstermin(fristfall=None, bezugsdatum=None, werktagskalender=None, kalendernachweis=None):
    """Vorhandene Kalenderauswahl wiederverwenden:556b dritter einschlägiger Werktag ab Zeitabschnittsbeginn einschließlich;579 erster einschlägiger Werktag nach Kalenderquartalsende."""
    _auswahl(fristfall,'fristfall',('zahlung_556b','grundstueck_quartal_579','landpacht_abschnitt_587'))
    tag = _datum(bezugsdatum,'bezugsdatum');_text(kalendernachweis,'kalendernachweis')
    _vorhanden(werktagskalender,'werktagskalender')
    if not isinstance(werktagskalender,dict) or set(werktagskalender)!={'erster_kalendertag','letzter_kalendertag','werktage'}:
        _fehler('werktagskalender','Genau erster_kalendertag, letzter_kalendertag und werktage erforderlich.')
    kalender = _bankkalender(dict(erster_kalendertag=werktagskalender['erster_kalendertag'],letzter_kalendertag=werktagskalender['letzter_kalendertag'],geschaeftstage=werktagskalender['werktage']))
    if fristfall=='zahlung_556b':
        erster = _banktermin(tag,kalender,'ab')
        ende = _banktermin(erster,kalender,'nach',2)
    else:
        if fristfall=='grundstueck_quartal_579' and (tag.month not in (3,6,9,12) or tag!=_frist(tag.replace(day=1).isoformat(),1,'monate','tagesbeginn')):
            _fehler('bezugsdatum','Letzter Tag eines Kalenderquartals erforderlich.')
        ende = _banktermin(_tage_addieren(tag,1),kalender,'ab')
    wert = dict(rechnerischer_zahlungstermin=ende.isoformat())
    eingaben = dict(fristfall=fristfall, bezugsdatum=bezugsdatum, werktagskalender=werktagskalender, kalendernachweis=kalendernachweis)
    ergebnis = _ergebnis(wert,"datum",'BGB_MIETE_WERKTAGSTERMIN',eingaben,[dict(operation='Vorhandene Kalenderauswahl wiederverwenden:556b dritter einschlägiger Werktag ab Zeitabschnittsbeginn einschließlich;579 erster einschlägiger Werktag nach Kalenderquartalsende. 587: erster einschlaegiger Werktag nach dem rechtlich bestimmten Bemessungsabschnitt.')],eingaben.copy())
    ergebnis["hinweise"] = ['§556bI und579II: Miete zu Beginn, spätestens am dritten Werktag des Bemessungszeitabschnitts; Ergebnis ist äußerer Zahlungstermin, nicht automatisch Verzugseintritt oder notwendiger Geldeingang. §579I3 nur Grundstücksmiete ohne kürzere Bemessungsabschnitte: erster Werktag nach Kalenderquartal. Räume folgen579II/556b. Andere bewegliche Sachen oder kürzere Grundstücksabschnitte nach579I1/2 nicht dieser Quartalsregel unterwerfen. Werk-/Bankgeschäftstagsbegriffe nicht gleichsetzen: intern wird nur dieselbe geordnete Kalendersuche wiederverwendet. Überweisungs-/Barzahlungsregeln und Feiertage ausdrücklich im Werktagskalender begründen; keine pauschale Montag-bis-Freitag- oder Samstagannahme. Unzureichend belegte Kalender werden zurückgewiesen.']
    ergebnis["hinweise"].append('§587I2: bei Bemessung nach Zeitabschnitten erster rechtlich einschlaegiger Werktag nach deren Ablauf; bezugsdatum ist letzter Abschnittstag, kein zwingendes Kalenderquartal. Werktagskalender vollstaendig rechtlich belegen. Ohne Abschnittsbemessung gilt587I1: Ende der Pachtzeit; gegebenenfalls193 gesondert.587II verweist fuer Ersparnis und anderweitige Verwertung auf537; vorhandene Betragsrechnung verwenden.')
    return ergebnis
