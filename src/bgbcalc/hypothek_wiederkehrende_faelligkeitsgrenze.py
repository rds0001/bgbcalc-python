from .kalender import _datum, _ergebnis, _frist, _text, _auswahl

def hypothek_wiederkehrende_faelligkeitsgrenze(beschlagnahme_am=None, faelligkeit_am=None, grenzmethode=None, einordnungsnachweis=None):
    """Drei Kalendermonate ab Beschlagnahme und Fälligkeitslage nach ausdrücklich gewählter Grenztagsmethode berechnen."""
    _datum(beschlagnahme_am,'beschlagnahme_am');f=_datum(faelligkeit_am,'faelligkeit_am');_text(einordnungsnachweis,'einordnungsnachweis')
    _auswahl(grenzmethode,'grenzmethode',('nach_ablauf_dreimonatsfrist','ab_dreimonatsvergleichstag'))
    e=_frist(beschlagnahme_am,3,'monate','ereignis')
    wert=dict(dreimonatsvergleichstag=e.isoformat(),zeitliches_unwirksamkeitsmerkmal=f>e if grenzmethode=='nach_ablauf_dreimonatsfrist' else f>=e,angewandte_grenzmethode=grenzmethode)
    eingaben = dict(beschlagnahme_am=beschlagnahme_am, faelligkeit_am=faelligkeit_am, grenzmethode=grenzmethode, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'datum_und_wahrheitswert','BGB_HYPOTHEK_WIEDERKEHRENDE_FAELLIGKEITSGRENZE',eingaben,[dict(operation='Drei Kalendermonate ab Beschlagnahme und Fälligkeitslage nach ausdrücklich gewählter Grenztagsmethode berechnen.')],eingaben.copy())
    ergebnis["hinweise"] = ['1126Satz3: Vorverfügung über wiederkehrende Leistung, keine Mietzeitraumprüfung nach1124II. Drei Kalendermonate mit bestehendem187/188-Kern rechnen, keine90Tage. Nach_ablauf_dreimonatsfrist vergleicht Fälligkeit streng nach dem letzten Fristtag; ab_dreimonatsvergleichstag bezieht diesen Vergleichstag ein. Die lokale Norm allein klärt die hier strittige Tagesgrenze nicht abschließend; verpflichtende Methodenwahl macht beide bedingten Rechnungen sichtbar, ohne eine allgemein verbindliche Grenztagsauslegung zu behaupten. Übrige rechtliche Unwirksamkeitsvoraussetzungen sind nicht Gegenstand dieser zeitlichen Rechnung. Keine193-Wochenendverschiebung einer Fälligkeitsabgrenzung.']
    return ergebnis

