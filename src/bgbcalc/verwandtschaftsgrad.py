"""Numerischer Verwandtschaftsgrad aus qualifizierten Geburtsschritten."""
from .kalender import _ergebnis, _fehler, _ganzzahl, _text


def verwandtschaftsgrad_geburtsschritte(geburtsschritte_person=None, geburtsschritte_andere=None, abstammungsnachweis=None):
    """§1589I3: beide qualifizierten Abstammungswege zum nächsten gemeinsamen Stamm addieren."""
    erster = _ganzzahl(geburtsschritte_person,'geburtsschritte_person',0,1000)
    zweiter = _ganzzahl(geburtsschritte_andere,'geburtsschritte_andere',0,1000)
    _text(abstammungsnachweis,'abstammungsnachweis')
    if erster + zweiter == 0:
        _fehler('geburtsschritte_person','Mindestens ein vermittelnder Geburtsschritt zwischen verschiedenen Personen erforderlich.')
    eingaben = dict(geburtsschritte_person=geburtsschritte_person,geburtsschritte_andere=geburtsschritte_andere,abstammungsnachweis=abstammungsnachweis)
    ergebnis = _ergebnis(erster+zweiter,'grad','BGB_VERWANDTSCHAFTSGRAD_GEBURTSSCHRITTE',eingaben,[dict(operation='Qualifizierte Geburtsschritte beider Personen zum nächsten gemeinsamen Stamm addieren.')],eingaben.copy())
    ergebnis['hinweise'] = ['§1589I3 zählt die vermittelnden Geburten. Gerade Linie: eine Person ist Vorfahr der anderen, deren eigener Weg zum gemeinsamen Stamm daher0. Seitenlinie: Wege beider Personen zum nächsten gemeinsamen Vorfahren, etwa Geschwister1+1=2 oder Cousins2+2=4. Keine automatische Stammbauermittlung oder rechtliche Abstammungs-/Adoptionsprüfung. Entfernteren gemeinsamen Vorfahren nicht wählen, wenn ein näherer existiert. Nach§1590I2 wird derselbe qualifizierte Grad für die vermittelnde Verwandtschaft übernommen; Ehe selbst fügt keinen Geburtsschritt hinzu. Die Funktion stellt keine Verwandtschaft oder Schwägerschaft fest.']
    return ergebnis
