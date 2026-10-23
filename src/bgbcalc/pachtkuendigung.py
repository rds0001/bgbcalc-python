from .bankgeschaeftstage import _bankkalender, _banktermin
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _text, _vorhanden

def pacht_kuendigungstermin(fristfall=None, kuendigungszugang_am=None, fristabschnitte=None, werktagskalender=None, einordnungsnachweis=None):
    """Dritten qualifizierten Werktag je normativ zugeordnetem Pachtabschnitt zählen und ersten beim Zugang noch erreichbaren Pachtendtermin auswählen."""
    _auswahl(fristfall,'fristfall',('pacht_584','landpacht_ordentlich_594a','landpacht_ausserordentlich_594a'))
    zugang = _datum(kuendigungszugang_am,'kuendigungszugang_am');_text(einordnungsnachweis,'einordnungsnachweis')
    _vorhanden(werktagskalender,'werktagskalender')
    if not isinstance(werktagskalender,dict) or set(werktagskalender)!={'erster_kalendertag','letzter_kalendertag','werktage'}:
        _fehler('werktagskalender','Genau erster_kalendertag, letzter_kalendertag und werktage erforderlich.')
    kalender = _bankkalender(dict(erster_kalendertag=werktagskalender['erster_kalendertag'],letzter_kalendertag=werktagskalender['letzter_kalendertag'],geschaeftstage=werktagskalender['werktage']))
    _vorhanden(fristabschnitte,'fristabschnitte')
    if not isinstance(fristabschnitte,list) or not 1<=len(fristabschnitte)<=1000:
        _fehler('fristabschnitte','Geordnete Liste1..1000 vollständig qualifizierter Fristabschnitte erforderlich.')
    vorher = None;wert = None
    for abschnitt in fristabschnitte:
        if not isinstance(abschnitt,dict) or set(abschnitt)!={'fristabschnitt_beginn_am','pachtende_am'}:
            _fehler('fristabschnitte','Genau fristabschnitt_beginn_am und pachtende_am erforderlich.')
        beginn = _datum(abschnitt['fristabschnitt_beginn_am'],'fristabschnitt_beginn_am')
        ende = _datum(abschnitt['pachtende_am'],'pachtende_am')
        if ende < beginn or (vorher is not None and (beginn<=vorher[0] or ende<=vorher[1])):
            _fehler('fristabschnitte','Beginn und Ende streng aufsteigend, Ende nicht vor Beginn.')
        vorher = (beginn,ende)
        dritter = _banktermin(_banktermin(beginn,kalender,'ab'),kalender,'nach',2)
        if dritter > ende:
            _fehler('fristabschnitte','Dritter Werktag darf nicht nach dem zugeordneten Pachtende liegen.')
        if wert is None and zugang<=dritter:
            wert = dict(letzter_zugangstag=dritter.isoformat(),rechnerischer_pachtendtermin=ende.isoformat())
    if wert is None:
        _fehler('fristabschnitte','Kein nach Zugang noch erreichbarer Termin in der vollständigen Liste.')
    eingaben = dict(fristfall=fristfall, kuendigungszugang_am=kuendigungszugang_am, fristabschnitte=fristabschnitte, werktagskalender=werktagskalender, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'daten','BGB_PACHT_KUENDIGUNGSTERMIN',eingaben,[dict(operation='Dritten qualifizierten Werktag je normativ zugeordnetem Pachtabschnitt zählen und ersten beim Zugang noch erreichbaren Pachtendtermin auswählen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§584I/II beziehungsweise594aI/II: dritten einschlägigen Werktag ab dem qualifizierten Fristabschnittsbeginn einschließlich bestimmen und erstes Pachtende auswählen, dessen Stichtag beim Zugang noch nicht überschritten ist.594aI koppelt Pachtjahresbeginn an Ende des nächsten Pachtjahres;584/594aII koppelt letzten Halbjahresbeginn an Ende desselben Pachtjahres. Diese Periodenzuordnung ist ausdrücklich Eingabe, keine freie Kürzungsvereinbarung. Liste muss sämtliche möglichen Termine ab Zugang vollständig enthalten; kein automatisches Überspringen ausgelassener Jahre. Samstag-/Feiertagsqualifikation extern, keine Gleichsetzung mit Bankgeschäftstagen trotz Wiederverwendung derselben Kalendersuche. Keine automatische Kündigungsberechtigung oder Textform-/Zugangsbewertung. Ein zu kurzer Kalender oder fehlender erreichbarer Termin ist Eingabefehler, kein unbefristeter Vertrag.']
    return ergebnis

