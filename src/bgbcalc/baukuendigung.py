from .betraege import _geld, _geld_ergebnis
from .kalender import _auswahl, _fehler, _text
from .zahlen import _addieren, _bruch, _multiplizieren, _subtrahieren

def bau_sicherheitskuendigung_verguetung(erbrachte_verguetung=None, nicht_erbrachte_verguetung=None, abrechnungsart=None, ersparte_aufwendungen=None, anderweitiger_erwerb=None, boeswillig_unterlassener_erwerb=None, einordnungsnachweis=None):
    """Erbrachte Vergütung plus fünf Prozent des nicht erbrachten Anteils oder gesamte Vergütung abzüglich qualifizierter Ersparnis und Erwerbsbeträge."""
    erbracht, offen = _geld(erbrachte_verguetung), _geld(nicht_erbrachte_verguetung)
    erspart, anderweitig, unterlassen = _geld(ersparte_aufwendungen), _geld(anderweitiger_erwerb), _geld(boeswillig_unterlassener_erwerb)
    _auswahl(abrechnungsart,'abrechnungsart',('vermutung','konkret'))
    _text(einordnungsnachweis,'einordnungsnachweis')
    if abrechnungsart == 'vermutung':
        if any(x != 0 for x in (erspart,anderweitig,unterlassen)):
            _fehler('abrechnungsart','Vermutung nicht mit konkreten Abzügen vermischen.')
        wert = _addieren(erbracht,_multiplizieren(offen,_bruch(1,20)))
    else:
        abzug = _addieren(_addieren(erspart,anderweitig),unterlassen)
        wert = max(_subtrahieren(_addieren(erbracht,offen),abzug),_bruch(0))
    eingaben = dict(erbrachte_verguetung=erbrachte_verguetung, nicht_erbrachte_verguetung=nicht_erbrachte_verguetung, abrechnungsart=abrechnungsart, ersparte_aufwendungen=ersparte_aufwendungen, anderweitiger_erwerb=anderweitiger_erwerb, boeswillig_unterlassener_erwerb=boeswillig_unterlassener_erwerb, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(wert,'BGB_BAU_SICHERHEITSKUENDIGUNG_VERGUETUNG',eingaben,[dict(operation='Erbrachte Vergütung plus fünf Prozent des nicht erbrachten Anteils oder gesamte Vergütung abzüglich qualifizierter Ersparnis und Erwerbsbeträge.')])
    ergebnis["hinweise"].append('§650fV: Unternehmerkündigung nach erfolgloser angemessener Frist zur Sicherheitsleistung; nicht mit freier Bestellerkündigung648 gleichsetzen.650fVI-Ausnahmen und gegebenenfalls Baubetreuerfall vorqualifizieren. Gesetzliche5Prozent sind widerlegliche Vermutung ausschließlich für den nicht erbrachten Vergütungsanteil; konkrete Abzüge nicht zusätzlich zur Vermutung einsetzen. Konkrete Rechnung: Gesamtvergütung minus kausal zurechenbare Ersparnis, anderweitiger Erwerb und böswillig unterlassener Erwerb, mindestens0. Abzüge überschneidungsfrei, Brutto-/Nettobezug konsistent; keine automatisch negative Vergütungsforderung oder Rückerstattung aus Abzugsüberschuss. Bereits geleistete Zahlungen und sonstige Ansprüche separat.')
    return ergebnis
