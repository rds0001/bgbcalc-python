from .kalender import _datum, _ergebnis, _text
from .betraege import _geld
from .zinsen import _bruchteile

def reiseuebertragung_siebentagevergleich(reisebeginn_am=None, erklaerungszugang_am=None, einordnungsnachweis=None):
    """Taggenau qualifizierten Abstand zwischen tatsächlichem Erklärungszugang und Reisebeginn bestimmen und mit sieben Kalendertagen vergleichen."""
    beginn = _datum(reisebeginn_am,'reisebeginn_am')
    zugang = _datum(erklaerungszugang_am,'erklaerungszugang_am');_text(einordnungsnachweis,'einordnungsnachweis')
    tage = (beginn-zugang).days
    wert = dict(kalendertage_vorlauf=tage,mindestens_sieben_kalendertage=tage>=7)
    eingaben = dict(reisebeginn_am=reisebeginn_am, erklaerungszugang_am=erklaerungszugang_am, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'tage_und_wahrheitswert','BGB_REISEUEBERTRAGUNG_SIEBENTAGEVERGLEICH',eingaben,[dict(operation='Taggenau qualifizierten Abstand zwischen tatsächlichem Erklärungszugang und Reisebeginn bestimmen und mit sieben Kalendertagen vergleichen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§651eI2: nur Anzahl der qualifizierten Kalendertage zwischen Zugang und Reisebeginn und Vergleich mit sieben Tagen. Erreichen ist rechnerischer Nachweis der gesetzlichen Siebentage-Sicherheitsgrenze im taggenau qualifizierten Fall. Unterschreiten bedeutet nicht automatisch Unwirksamkeit oder Verspätung: angemessene kürzere Frist nachSatz1 bleibt rechtlich zu prüfen. Dauerhafter Datenträger, tatsächlicher Zugang und Eignung des Dritten extern. Keine pauschale Umrechnung in168Stunden, keine automatische Feiertagsverschiebung und kein untertägiges Zugangs-/Reisebeginnurteil.']
    return ergebnis

def reiseuebertragung_mehrkostenbetrag(tatsaechliche_mehrkosten=None, angemessener_hoechstbetrag=None, einordnungsnachweis=None):
    """Tatsächlich entstandene Übertragungsmehrkosten auf rechtlich angemessenen Höchstbetrag begrenzen."""
    tatsaechlich = _geld(tatsaechliche_mehrkosten);angemessen = _geld(angemessener_hoechstbetrag)
    _text(einordnungsnachweis,'einordnungsnachweis')
    wert = _bruchteile(min(tatsaechlich,angemessen))
    eingaben = dict(tatsaechliche_mehrkosten=tatsaechliche_mehrkosten, angemessener_hoechstbetrag=angemessener_hoechstbetrag, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_REISEUEBERTRAGUNG_MEHRKOSTENBETRAG',eingaben,[dict(operation='Tatsächlich entstandene Übertragungsmehrkosten auf rechtlich angemessenen Höchstbetrag begrenzen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§651eIII2/IV: nur kleinere Zahl aus tatsächlichen nachgewiesenen Mehrkosten und rechtlich angemessener Betragsgrenze. Keine Gebührentabelle oder automatische Angemessenheitsprüfung. Reisepreis nicht nochmals als Mehrkosten zählen. Gesamtschuld von Reisendem und Drittem rechtlich vorausgesetzt; Betrag nicht verdoppeln und nicht automatisch nach Köpfen aufteilen. Andere Zahlungs-/Erfüllungsvorgänge separat.']
    return ergebnis

