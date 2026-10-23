from .betraege import _wahrheitswert
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _ganzzahl, _text, _vorhanden

def verein_austrittskalender(kuendigungszugang_am=None, fristdauer=None, fristeinheit=None, nur_zum_geschaeftsjahresende=None, geschaeftsjahresenden=None, satzungsnachweis=None):
    """Ereignisfrist und Zweijahresgrenze kalendergenau berechnen; gegebenenfalls erstes einschlägiges Geschäftsjahresende ab Fristende auswählen und beide Termine getrennt mit der Zweijahresgrenze vergleichen."""
    zugang = _datum(kuendigungszugang_am,'kuendigungszugang_am')
    anzahl = _ganzzahl(fristdauer,'fristdauer',0,3652059)
    _auswahl(fristeinheit,'fristeinheit',('tage','wochen','monate','jahre'))
    _wahrheitswert(nur_zum_geschaeftsjahresende,'nur_zum_geschaeftsjahresende');_text(satzungsnachweis,'satzungsnachweis')
    grenze = _frist(zugang.isoformat(),2,'jahre','ereignis')
    frist = zugang if anzahl==0 else _frist(zugang.isoformat(),anzahl,fristeinheit,'ereignis')
    termin = frist
    if nur_zum_geschaeftsjahresende:
        _vorhanden(geschaeftsjahresenden,'geschaeftsjahresenden')
        if not isinstance(geschaeftsjahresenden,list) or not 1<=len(geschaeftsjahresenden)<=1000:
            _fehler('geschaeftsjahresenden','Geordnete Liste mit1bis1000 Geschäftsjahresenden erforderlich.')
        enden = [_datum(t,'geschaeftsjahresenden') for t in geschaeftsjahresenden]
        if any(t<zugang for t in enden) or any(a>=b for a,b in zip(enden,enden[1:])):
            _fehler('geschaeftsjahresenden','Geschäftsjahresenden streng aufsteigend ab Zugang vorgeben.')
        kandidaten = [t for t in enden if t>=frist]
        if not kandidaten:
            _fehler('geschaeftsjahresenden','Kalender deckt den benötigten Austrittstermin nicht ab.')
        termin = kandidaten[0]
    elif geschaeftsjahresenden is not None:
        _fehler('geschaeftsjahresenden','Ohne Geschäftsjahresbindung ausdrücklich null.')
    wert = dict(rechnerisches_kuendigungsfristende=frist.isoformat(),rechnerischer_austrittstermin=termin.isoformat(),zweijahresgrenze=grenze.isoformat(),kuendigungsfrist_innerhalb_zweijahresgrenze=frist<=grenze,austrittstermin_innerhalb_zweijahresgrenze=termin<=grenze)
    eingaben = dict(kuendigungszugang_am=kuendigungszugang_am, fristdauer=fristdauer, fristeinheit=fristeinheit, nur_zum_geschaeftsjahresende=nur_zum_geschaeftsjahresende, geschaeftsjahresenden=geschaeftsjahresenden, satzungsnachweis=satzungsnachweis)
    ergebnis = _ergebnis(wert,'daten_und_wahrheitswerte','BGB_VEREIN_AUSTRITTSKALENDER',eingaben,[dict(operation='Ereignisfrist und Zweijahresgrenze kalendergenau berechnen; gegebenenfalls erstes einschlägiges Geschäftsjahresende ab Fristende auswählen und beide Termine getrennt mit der Zweijahresgrenze vergleichen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§39II: rechnerischer Vergleich einer satzungsmäßig vorgegebenen Kündigungsfrist mit höchstens zwei Kalenderjahren sowie Auswahl des nächsten einschlägigen Geschäftsjahresendes. Fristdauer0 bedeutet keine zusätzliche Kündigungsfrist. Geschäftsjahr und gegebenenfalls Kombination beider Satzungsbedingungen rechtlich vorqualifizieren; keine automatische Satzungsauslegung. Die beiden Zweijahresvergleiche betreffen getrennt die Kündigungsfrist und den resultierenden Kalendertermin. Eine Überschreitung wird sichtbar gemacht, nicht durch eine erfundene geltungserhaltende Reduktion geheilt; keine automatische Wirksamkeitsentscheidung für die Satzung oder den Austritt. Alle einschlägigen Geschäftsjahresenden ab Zugang bis zum benötigten Termin vollständig und geordnet vorgeben. Keine automatische193-Verschiebung eines Geschäftsjahresendes. Die Zweijahresgrenze wird kalendergenau berechnet, nicht pauschal als730Tage.']
    return ergebnis

