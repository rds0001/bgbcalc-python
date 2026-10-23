from .kalender import _auswahl, _datum, _ergebnis, _frist, _text

def erklaerung_vorlauf_zum_zeitraumende(vorlauffall=None, erklaerungseingang_am=None, beendigung_am=None, einordnungsnachweis=None):
    """Gesetzlichen Vorlauf ab tatsächlichem Erklärungseingang berechnen und mit Beendigung zu Tagesablauf vergleichen."""
    _auswahl(vorlauffall,'vorlauffall',('mietwiderspruch_574b','pachterbenwiderspruch_594d','pachtfortsetzung_595','pachtgerichtsantrag_595','darlehen_zinsbindungsende_493','darlehen_vertragsende_493'))
    _datum(erklaerungseingang_am,'erklaerungseingang_am');ende=_datum(beendigung_am,'beendigung_am');_text(einordnungsnachweis,'einordnungsnachweis')
    monate={'mietwiderspruch_574b':2,'pachterbenwiderspruch_594d':3,'pachtfortsetzung_595':12,'pachtgerichtsantrag_595':9,'darlehen_zinsbindungsende_493':3,'darlehen_vertragsende_493':3}[vorlauffall]
    ablauf=_frist(erklaerungseingang_am,monate,'monate','ereignis')
    wert=dict(vorlauf_ablauf_am=ablauf.isoformat(),vorlauf_zum_zeitraumende_eingehalten=ablauf<=ende)
    eingaben = dict(vorlauffall=vorlauffall, erklaerungseingang_am=erklaerungseingang_am, beendigung_am=beendigung_am, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'datum_und_wahrheitswert','BGB_ERKLAERUNG_VORLAUF_ZUM_ZEITRAUMENDE',eingaben,[dict(operation='Gesetzlichen Vorlauf ab tatsächlichem Erklärungseingang berechnen und mit Beendigung zu Tagesablauf vergleichen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§574bII Zwei-Monats-Vorlauf, §594dII Drei-Monats-Vorlauf, §595V Ein-Jahres-Vorlauf oder §595VII Neun-Monats-Vorlauf. Ereignisbeginn nach§187I und Ablauf nach§188; der volle Vorlauf muss spätestens mit Ablauf des angegebenen letzten Vertragstages enden. Anders als Beginn eines Tages schließt dieser Bezugszeitpunkt den Beendigungstag ein. Keine automatische Anwendung von§193 und keine automatische Unwirksamkeit verspäteter Erklärungen. §574bII2 fehlender rechtzeitiger Vermieterhinweis, §595V/VII Sonderfälle bei höchstens zwölfmonatiger Kündigungsfrist und gerichtliche Nachzulassung gesondert; für diese Sonderfälle existieren eigene Grundfristen. §594dII Bewirtschaftung und vollständige Mitteilung sind rechtliche Voraussetzungen.']
    ergebnis["hinweise"].append('§493I/II: Unterrichtung spaetestens drei Kalendermonate vor dem rechtlich feststehenden Ende der Sollzinsbindung beziehungsweise des Darlehensvertrags zu Tagesablauf. Tatsaechlichen Zugang vorwaerts gegen Endtag pruefen; erforderliche Informationsinhalte und Verhaeltnis von Zinsbindung zu Rueckzahlungszeit bleiben rechtliche Qualifikation. Keine automatische Informationspflicht oder Wirksamkeitsentscheidung.')
    return ergebnis

