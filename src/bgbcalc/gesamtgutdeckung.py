"""Vorzeitige Innenlastdeckung und gesetzliche Mittelvorränge im Gesamtgut."""
from .betraege import _geld
from .kalender import _ergebnis, _fehler, _text
from .zahlen import _addieren, _bruch, _subtrahieren
from .zinsen import _bruchteile


def gesamtgut_vorzeitiger_berichtigungsbetrag(schuld=None, verfuegbares_vorbehaltsgut=None, verfuegbares_sondergut=None, zuordnungsnachweis=None):
    """§§1446II/1468: vorzeitig aus Vorbehalts-/Sondergut deckbaren Schuldteil berechnen."""
    betrag = _geld(schuld)
    vorbehalt = _geld(verfuegbares_vorbehaltsgut)
    sonder = _geld(verfuegbares_sondergut)
    _text(zuordnungsnachweis, 'zuordnungsnachweis')
    deckung = _addieren(vorbehalt,sonder)
    vorzeitig = min(betrag,deckung)
    eingaben = dict(schuld=schuld,verfuegbares_vorbehaltsgut=verfuegbares_vorbehaltsgut,verfuegbares_sondergut=verfuegbares_sondergut,zuordnungsnachweis=zuordnungsnachweis)
    ergebnis = _ergebnis(dict(vorzeitiger_berichtigungsbetrag=_bruchteile(vorzeitig),restschuld=_bruchteile(_subtrahieren(betrag,vorzeitig))),'EUR','BGB_GESAMTGUT_VORZEITIGER_BERICHTIGUNGSBETRAG',eingaben,[dict(operation='Verfügbares Vorbehaltsgut und Sondergut addieren, Schuld hierauf begrenzen und ungedeckten Rest ausweisen.')],eingaben.copy())
    ergebnis['hinweise'] = ['Qualifizierte Innenlast gegenüber Gesamtgut oder Vorbehalts-/Sondergut des anderen Ehegatten. §1446II nur für den nicht allein verwaltenden Ehegatten; bei gemeinschaftlicher Verwaltung§1468. Verfügbarkeit der Vermögenswerte und konkurrierende Verpflichtungen rechtlich bereinigt. Keine Pflicht zur vorzeitigen Leistung aus Gesamtgut und keine Rangfolge zwischen Vorbehaltsgut und Sondergut erfunden. Restschuld wird nicht erlassen; gesetzlicher Aufschub bis Beendigung und weitere Fälligkeit rechtlich gesondert. Keine Außenhaftungsentscheidung.']
    return ergebnis


def familienunterhalt_mittelvorrang(bedarf_dieser_mittelstufe=None, gesamtgutsmittel=None, nachrangige_mittel=None, mittelart=None, zuordnungsnachweis=None):
    """§1420: Gesamtgutsmittel vor gleichartig eingeordneten nachrangigen Mitteln einsetzen."""
    bedarf = _geld(bedarf_dieser_mittelstufe)
    vorrang = _geld(gesamtgutsmittel)
    nachrang = _geld(nachrangige_mittel)
    _text(mittelart,'mittelart')
    _text(zuordnungsnachweis,'zuordnungsnachweis')
    if mittelart not in ['einkuenfte','vermoegensstamm']:
        _fehler('mittelart','einkuenfte oder vermoegensstamm erforderlich.')
    aus_gesamtgut = min(bedarf,vorrang)
    rest = _subtrahieren(bedarf,aus_gesamtgut)
    aus_nachrang = min(rest,nachrang)
    eingaben = dict(bedarf_dieser_mittelstufe=bedarf_dieser_mittelstufe,gesamtgutsmittel=gesamtgutsmittel,nachrangige_mittel=nachrangige_mittel,mittelart=mittelart,zuordnungsnachweis=zuordnungsnachweis)
    wert = {k:_bruchteile(v) for k,v in dict(einsatz_gesamtgut=aus_gesamtgut,einsatz_nachrangige_mittel=aus_nachrang,ungedeckter_bedarf=_subtrahieren(rest,aus_nachrang),verbleibende_gesamtgutsmittel=_subtrahieren(vorrang,aus_gesamtgut),verbleibende_nachrangige_mittel=_subtrahieren(nachrang,aus_nachrang)).items()}
    ergebnis = _ergebnis(wert,'EUR','BGB_FAMILIENUNTERHALT_MITTELVORRANG',eingaben,[dict(operation='Qualifizierten Bedarf zunächst aus Gesamtgutsmitteln, Rest erst aus nachrangigen gleichartigen Mitteln decken; Restbedarf und Restmittel ausweisen.')],eingaben.copy())
    ergebnis['hinweise'] = ['§1420 enthält zwei getrennte Vorränge. mittelart=einkuenfte: Gesamtguteinkünfte vor Vorbehaltseinkünften. mittelart=vermoegensstamm: Gesamtgutstamm vor zusammengefasstem Vorbehalts-/Sondergutstamm. Bedarf und verfügbare Mittel für dieselbe qualifizierte Mittelstufe/Periode vorgeben. Keine zusätzliche allgemeine Reihenfolge zwischen Vorbehaltseinkünften und Gesamtgutstamm oder zwischen Vorbehalts-/Sondergutstamm erfunden; diese Funktion allein ist kein vollständiger Familienunterhaltsfinanzierungsplan. Keine Bedarfsermittlung, Verfügbarkeitsermittlung oder freie Vermögensmassenzuordnung.']
    return ergebnis
