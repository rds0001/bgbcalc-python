"""Zusammensetzung und Wiederaufstockung des Stiftungsvermögens."""
from .betraege import _geld, _geld_ergebnis
from .kalender import _ergebnis, _fehler, _text
from .zahlen import _addieren, _bruch, _subtrahieren
from .zinsen import _bruchteile


def stiftung_vermoegenszusammensetzung(gewidmetes_vermoegen=None, davon_sonstig_gewidmet=None, zustiftungen=None, umgewidmeter_grundstock=None, weiteres_sonstiges_vermoegen=None, zuordnungsnachweis=None):
    """§83b: nicht überlappende Grundstock- und sonstige Vermögensbestandteile addieren."""
    widmung = _geld(gewidmetes_vermoegen)
    sonstig = _geld(davon_sonstig_gewidmet)
    zustiftung = _geld(zustiftungen)
    umwidmung = _geld(umgewidmeter_grundstock)
    weiteres = _geld(weiteres_sonstiges_vermoegen)
    if sonstig > widmung:
        _fehler('davon_sonstig_gewidmet','Sonstig gewidmeter Teil darf gesamte Widmung nicht übersteigen.')
    _text(zuordnungsnachweis,'zuordnungsnachweis')
    grundstock = _addieren(_addieren(_subtrahieren(widmung,sonstig),zustiftung),umwidmung)
    sonstiges = _addieren(sonstig,weiteres)
    eingaben = dict(gewidmetes_vermoegen=gewidmetes_vermoegen,davon_sonstig_gewidmet=davon_sonstig_gewidmet,zustiftungen=zustiftungen,umgewidmeter_grundstock=umgewidmeter_grundstock,weiteres_sonstiges_vermoegen=weiteres_sonstiges_vermoegen,zuordnungsnachweis=zuordnungsnachweis)
    wert = dict(grundstockvermoegen=_bruchteile(grundstock),sonstiges_vermoegen=_bruchteile(sonstiges),stiftungsvermoegen=_bruchteile(_addieren(grundstock,sonstiges)))
    ergebnis = _ergebnis(wert,'EUR','BGB_STIFTUNG_VERMOEGENSZUSAMMENSETZUNG',eingaben,[dict(operation='Sonstige Widmung abziehen, Zustiftungen und Umwidmungen zum Grundstock addieren, getrenntes sonstiges Vermögen und Gesamtbestand berechnen.')],eingaben.copy())
    ergebnis['hinweise'] = ['Stiftung auf unbestimmte Zeit; keine Verbrauchsstiftung. Sämtliche Beträge sind rechtlich bewertete, am selben Stichtag noch vorhandene zugeordnete Bestände, keine unbereinigten historischen Zuflüsse. Zustiftungen und Umwidmungen sind nicht bereits in gewidmetes_vermoegen enthalten. weiteres_sonstiges_vermoegen enthält weder den separat genannten sonstig gewidmeten Teil noch zum Grundstock umgewidmete Werte. Verbrauch/Abgänge/Wertveränderungen vorab richtig zuordnen; keine Vermögensbewertung, Erhaltungsfreigabe oder Bilanzierungsautomatik.']
    return ergebnis


def stiftung_wiederaufstockungsrest(verbrauchter_grundstock=None, bereits_wiederaufgestockt=None, zuordnungsnachweis=None):
    """§83cII: verbliebene Wiederaufstockung als positive Differenz berechnen."""
    verbrauch = _geld(verbrauchter_grundstock)
    auffuellung = _geld(bereits_wiederaufgestockt)
    _text(zuordnungsnachweis,'zuordnungsnachweis')
    eingaben = dict(verbrauchter_grundstock=verbrauchter_grundstock,bereits_wiederaufgestockt=bereits_wiederaufgestockt,zuordnungsnachweis=zuordnungsnachweis)
    ergebnis = _geld_ergebnis(max(_subtrahieren(verbrauch,auffuellung),_bruch(0)),'BGB_STIFTUNG_WIEDERAUFSTOCKUNGSREST',eingaben,[dict(operation='Demselben zulässigen Grundstockverbrauch zugeordnete Wiederaufstockungen abziehen, mindestens null.')])
    ergebnis['hinweise'].append('Nur betragsmäßiger Rest des rechtlich qualifizierten Verbrauchs nach§83cAbsatz2. Gleicher Verbrauchsvorgang und einheitliche Bewertungsbasis; keine mehrfach angerechnete Auffüllung. Zulässigkeit des Verbrauchs, absehbare Zeit und Grundstockerhaltung werden nicht festgestellt; Überschuss begründet keinen automatischen Entnahmeanspruch.')
    return ergebnis
