"""§712: rechnerische Anteilsänderung bei einem Ein- oder Austritt."""
from .kalender import _text, _fehler, _auswahl, _ergebnis
from .zahlen import _zahleneingabe, _bruch, _addieren, _subtrahieren, _multiplizieren, _dividieren
from .zinsen import _bruchteile


def gesellschaft_anteil_nach_bestandswechsel(bisheriger_anteil=None, wechselanteil=None, wechselart=None, einordnungsnachweis=None):
    """Bestehenden Anteil bei Ausscheiden relativ erhöhen oder bei Eintritt relativ vermindern."""
    alt=_zahleneingabe(bisheriger_anteil); wechsel=_zahleneingabe(wechselanteil)
    _auswahl(wechselart,'wechselart',('ausscheiden','eintritt')); _text(einordnungsnachweis,'einordnungsnachweis')
    if not 0 <= alt <= 1 or not 0 <= wechsel <= 1:
        _fehler('anteile','Anteile müssen zwischen null und eins liegen.')
    rest=_subtrahieren(_bruch(1),wechsel)
    if wechselart=='ausscheiden':
        if rest==0 or _addieren(alt,wechsel)>1:
            _fehler('wechselanteil','Ausscheidender Anteil kleiner eins und Summe mit verbleibendem Einzelanteil höchstens eins erforderlich.')
        neu=_dividieren(alt,rest)
    else:
        neu=_multiplizieren(alt,rest)
    eingaben=dict(bisheriger_anteil=bisheriger_anteil,wechselanteil=wechselanteil,wechselart=wechselart,einordnungsnachweis=einordnungsnachweis)
    ergebnis=_ergebnis(_bruchteile(neu),'quote','BGB_GESELLSCHAFT_ANTEIL_NACH_BESTANDSWECHSEL',eingaben,[dict(operation='Ausscheiden: alter Anteil/(1-ausscheidender Anteil); Eintritt: alter Anteil*(1-neuer Anteil).')],eingaben.copy())
    ergebnis['hinweise']=['Nur qualifizierter Zweifelsfall des §712 ohne abweichende Vereinbarung. Ergebnis betrifft einen verbleibenden bisherigen Gesellschafter. wechselanteil bei Ausscheiden ist bisheriger Anteil des ausscheidenden Gesellschafters; bei Eintritt der rechtlich bestimmte neue Endanteil des Eintretenden. Alte Anteile zuvor vollständig auf eins normieren. Ein Wechsel je Rechnung; gleichzeitige Ein-/Austritte rechtlich ordnen, nicht blind nacheinander fortschreiben. Ausscheiden des alleinigen Inhabers und rechtlicher Übergang auf einen letzten Gesellschafter nach §712a gesondert prüfen; keine Aussage zum Fortbestand der Gesellschaft. Nicht Abfindung oder persönliche Haftung.']
    return ergebnis
