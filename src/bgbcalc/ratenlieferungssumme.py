from .betraege import _geld
from .kalender import _ergebnis, _fehler, _text, _vorhanden
from .reisezeitschwellen import _reise_utc_zeitpunkt
from .zahlen import _addieren, _bruch
from .zinsen import _bruchteile

def ratenlieferung_massgebliche_teilzahlungssumme(teilzahlungen=None, fruehestmoeglicher_kuendigungszeitpunkt_utc=None, einordnungsnachweis=None):
    """Vertragliche Teilzahlungen mit Fälligkeit bis einschließlich des qualifizierten frühestmöglichen Kündigungszeitpunkts auswählen und exakt summieren."""
    ende = _reise_utc_zeitpunkt(fruehestmoeglicher_kuendigungszeitpunkt_utc,'fruehestmoeglicher_kuendigungszeitpunkt_utc')
    _vorhanden(teilzahlungen,'teilzahlungen')
    if not isinstance(teilzahlungen,list) or not 1<=len(teilzahlungen)<=10000:
        _fehler('teilzahlungen','Liste1bis10000 eindeutiger Teilzahlungen erforderlich.')
    _text(einordnungsnachweis,'einordnungsnachweis')
    namen = set();summe = _bruch(0);anzahl = 0
    for position in teilzahlungen:
        if not isinstance(position,dict) or set(position)!={'zahlungs_id','faellig_utc','betrag'}:
            _fehler('teilzahlungen','Genau zahlungs_id, faellig_utc und betrag erforderlich.')
        name = _text(position['zahlungs_id'],'zahlungs_id')
        if name in namen:
            _fehler('zahlungs_id','Teilzahlung darf nicht mehrfach erfasst werden.')
        namen.add(name)
        faellig = _reise_utc_zeitpunkt(position['faellig_utc'],'faellig_utc');betrag = _geld(position['betrag'])
        if faellig<=ende:
            summe = _addieren(summe,betrag);anzahl += 1
    wert = dict(massgebliche_teilzahlungssumme=_bruchteile(summe),anzahl_einbezogener_teilzahlungen=anzahl,anzahl_spaeter_faelliger_teilzahlungen=len(teilzahlungen)-anzahl)
    eingaben = dict(teilzahlungen=teilzahlungen, fruehestmoeglicher_kuendigungszeitpunkt_utc=fruehestmoeglicher_kuendigungszeitpunkt_utc, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,"EUR_und_anzahlen",'BGB_RATENLIEFERUNG_MASSGEBLICHE_TEILZAHLUNGSSUMME',eingaben,[dict(operation='Vertragliche Teilzahlungen mit Fälligkeit bis einschließlich des qualifizierten frühestmöglichen Kündigungszeitpunkts auswählen und exakt summieren.')],eingaben.copy())
    ergebnis["hinweise"] = ['§510III2: gesetzliche Ersatzbezugsgröße für den Nettodarlehensbetrag491II2Nr1. Alle bis zum maßgeblichen Kündigungszeitpunkt zu entrichtenden Teilzahlungen einbeziehen, auch bereits entrichtete; keine Berechnung bloß des offenen Saldos. Später fällige Raten nicht einbeziehen. Mehrere verschiedene Raten dürfen denselben Fälligkeitszeitpunkt haben, aber jede Zahlung nur einmal erfassen. Kündigungsregel und Zahlungsplan extern qualifizieren; Ergebnis entscheidet keine weiteren491-Ausnahmen, kein Widerrufsrecht und keine tatsächliche Restschuld. Strikte UTC-Zeitpunkte ohne Zeitzonenannahmen; vorhandenen Standard-Datumsparser wiederverwenden.']
    return ergebnis
