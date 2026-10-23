from .kalender import _datum, _ergebnis, _frist, _text

def vaterschaftsanfechtung_vertretergrundfrist(vertreterkenntnis_am=None, kind_geboren_am=None, berechtigter_geboren_am=None, anerkennung_wirksam_am=None, einordnungsnachweis=None):
    """Vorhandene allgemeine Zweijahresgrundfrist mit Mindestablauf Vollendung21 kombinieren; kein Volljährigkeitsaufschub bei Vertreteranfechtung."""
    _text(einordnungsnachweis,'einordnungsnachweis')
    _datum(berechtigter_geboren_am,'berechtigter_geboren_am')
    ereignisse=[_datum(vertreterkenntnis_am,'vertreterkenntnis_am'),_datum(kind_geboren_am,'kind_geboren_am')]
    if anerkennung_wirksam_am is not None: ereignisse.append(_datum(anerkennung_wirksam_am,'anerkennung_wirksam_am'))
    z=_frist(max(ereignisse).isoformat(),2,'jahre','ereignis');m=_frist(berechtigter_geboren_am,21,'jahre','tagesbeginn')
    wert=dict(zweijahresgrundfristende=z.isoformat(),mindestablauf_vollendung_21=m.isoformat(),anfechtungsgrundfristende=max(z,m).isoformat())
    eingaben = dict(vertreterkenntnis_am=vertreterkenntnis_am, kind_geboren_am=kind_geboren_am, berechtigter_geboren_am=berechtigter_geboren_am, anerkennung_wirksam_am=anerkennung_wirksam_am, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'daten','BGB_VATERSCHAFTSANFECHTUNG_VERTRETERGRUNDFRIST',eingaben,[dict(operation='Vorhandene allgemeine Zweijahresgrundfrist mit Mindestablauf Vollendung21 kombinieren; kein Volljährigkeitsaufschub bei Vertreteranfechtung.')],eingaben.copy())
    ergebnis["hinweise"] = ['1600bII4 nimmt für Vertreteranfechtung nur Satz2 aus, nicht Satz3. Deshalb Zweijahresgrundfrist aus Vertreterkenntnis/Geburt/Anerkennung ohne Volljährigkeitsaufschub, aber Mindestablauf Vollendung21 des Berechtigten. Rechtliche Vertretungsbefugnis und zeitlich anwendbare Fassung sind vorqualifiziert. Keine automatische Hemmung1600bIV,193-Korrektur oder Zulässigkeitsprüfung. Bestehenden Kalenderkern verwenden. Vollendung21 bedeutet Ablauf des nach187II berechneten Vortags, nicht einen zusätzlichen Tag.']
    return ergebnis

