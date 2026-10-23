from .betraege import _geld, _wahrheitswert
from .teilverguetung import _teilbetrag
from .kalender import _ergebnis, _fehler, _text
from .zahlen import _bruch, _subtrahieren
from .zinsen import _bruchteile

def dienstkuendigung_vorausverguetungsrueckzahlung(vorausverguetung=None, zeitanteil_nach_kuendigung_zaehler=None, zeitanteil_nach_kuendigung_nenner=None, kuendigungsumstand_nicht_zu_vertreten=None, abziehbare_entreicherung=None, einordnungsnachweis=None):
    """Vorauszahlung mit qualifiziertem Nachkündigungsanteil multiplizieren; nur im Bereicherungsfall rechtlich abzugsfähige Entreicherung abziehen."""
    anteil = _teilbetrag(vorausverguetung,zeitanteil_nach_kuendigung_zaehler,zeitanteil_nach_kuendigung_nenner)
    _wahrheitswert(kuendigungsumstand_nicht_zu_vertreten,'kuendigungsumstand_nicht_zu_vertreten');_text(einordnungsnachweis,'einordnungsnachweis')
    verlust = _bruch(0)
    if kuendigungsumstand_nicht_zu_vertreten:
        verlust = _geld(abziehbare_entreicherung)
        if verlust>anteil:
            _fehler('abziehbare_entreicherung','Abzugsbetrag darf den Nachkündigungsanteil nicht übersteigen.')
    elif abziehbare_entreicherung is not None:
        _fehler('abziehbare_entreicherung','Im346-Fall ausdrücklich null, kein Bereicherungsabzug.')
    wert = dict(rechnerischer_vorausanteil=_bruchteile(anteil),rechnerischer_rueckzahlungsbetrag=_bruchteile(_subtrahieren(anteil,verlust)))
    eingaben = dict(vorausverguetung=vorausverguetung, zeitanteil_nach_kuendigung_zaehler=zeitanteil_nach_kuendigung_zaehler, zeitanteil_nach_kuendigung_nenner=zeitanteil_nach_kuendigung_nenner, kuendigungsumstand_nicht_zu_vertreten=kuendigungsumstand_nicht_zu_vertreten, abziehbare_entreicherung=abziehbare_entreicherung, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_DIENSTKUENDIGUNG_VORAUSVERGUETUNGSRUECKZAHLUNG',eingaben,[dict(operation='Vorauszahlung mit qualifiziertem Nachkündigungsanteil multiplizieren; nur im Bereicherungsfall rechtlich abzugsfähige Entreicherung abziehen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§628I3 nach qualifizierter Kündigung626/627 nach Dienstbeginn: nur im Voraus entrichtete Vergütung für Zeit nach Kündigung. Anteil auf den tatsächlich vorausbezahlten Zeitraum beziehen, nicht blind auf gesamte Vertragsvergütung oder bisherige Leistungsquote. Teilbetrag nach der rechtlich einschlägigen Vergütungs-/Zeitkonvention bestimmen; keine universelle Dreißigtage- oder Jahreskonvention. Hat der Dienstverpflichtete den Kündigungsumstand nicht zu vertreten, gelten Bereicherungsvorschriften; abzugsfähige Entreicherung insbesondere unter Berücksichtigung818/819/820 rechtlich bestimmen. Im346-Fall keine818III-Entreicherung abziehen. Weitere Nutzungen, Wertersatz, frühere Leistungen und Interessenverlust628I1/2 sowie Kündigungsschaden628II separat; keine automatische Aufrechnung.']
    return ergebnis

