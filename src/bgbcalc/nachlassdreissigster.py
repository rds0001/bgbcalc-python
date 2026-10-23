"""Gesetzlicher Dreißigster für Familienangehörige (§1969)."""
from .betraege import _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler, _frist, _tage_addieren, _text


def nachlass_dreissigster_zeitraum(
    erbfall_am=None, prueftag=None, familienangehoeriger=None,
    hausstandszugehoerigkeit_bei_erbfall=None, unterhalt_vom_erblasser_bezogen=None,
    abweichende_letztwillige_anordnung=None, einordnungsnachweis=None,
):
    """Gesetzlichen 30-Tage-Zeitraum und persönliche Voraussetzungen des §1969 prüfen."""
    erbfall = _datum(erbfall_am, 'erbfall_am')
    tag = _datum(prueftag, 'prueftag')
    if tag < erbfall:
        _fehler('prueftag', 'Prüftag darf nicht vor dem Erbfall liegen.')
    eingaben = dict(erbfall_am=erbfall_am, prueftag=prueftag,
        familienangehoeriger=familienangehoeriger,
        hausstandszugehoerigkeit_bei_erbfall=hausstandszugehoerigkeit_bei_erbfall,
        unterhalt_vom_erblasser_bezogen=unterhalt_vom_erblasser_bezogen,
        abweichende_letztwillige_anordnung=abweichende_letztwillige_anordnung,
        einordnungsnachweis=einordnungsnachweis)
    for name in tuple(eingaben)[2:-1]:
        _wahrheitswert(eingaben[name], name)
    _text(einordnungsnachweis, 'einordnungsnachweis')
    beginn = _tage_addieren(erbfall, 1)
    ende = _frist(erbfall_am, 30, 'tage', 'ereignis')
    person = (familienangehoeriger and hausstandszugehoerigkeit_bei_erbfall
        and unterhalt_vom_erblasser_bezogen)
    wert = None if abweichende_letztwillige_anordnung else dict(
        zeitraumbeginn=beginn.isoformat(), zeitraumende=ende.isoformat(),
        persoenliche_voraussetzungen_erfuellt=person,
        prueftag_im_zeitraum=beginn <= tag <= ende,
        gesetzliche_zeit_und_personenvoraussetzungen_erfuellt=person and beginn <= tag <= ende)
    ergebnis = _ergebnis(wert, 'daten_und_wahrheitswerte', 'BGB_NACHLASS_DREISSIGSTER_ZEITRAUM', eingaben,
        [dict(operation='Erbfalltag ausschließen; folgende 30 Kalendertage einschließlich Endtag; Familienzugehörigkeit, Hausstand und Unterhaltsbezug kumulativ prüfen')], eingaben.copy())
    ergebnis['annahmen'] = ['Familienzugehörigkeit, Hausstand im Todeszeitpunkt, Unterhaltsbezug und letztwillige Anordnungen rechtlich qualifiziert; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['Nur gesetzlicher Zeitraum und persönliche Voraussetzungen nach§1969 Absatz1; keine abschließende Anspruchsprüfung. Abweichende letztwillige Anordnung ergibt NICHT_ANWENDBAR, nicht automatisch Anspruchsausschluss: Inhalt individuell auslegen. Unterhalt im bisherigen Umfang sowie Benutzung der Wohnung und Haushaltsgegenstände nicht in erfundene Tagesbeträge umrechnen. Entsprechende Anwendung der Vermächtnisvorschriften nach Absatz2 einschließlich Einwendungen und Haftungsbeschränkungen gesondert prüfen. Keine automatische Verlängerung des Versorgungszeitraums wegen Wochenende/Feiertag. Der Erbfalltag selbst zählt nicht zu den folgenden 30 Tagen.']
    ergebnis['status'] = 'NICHT_ANWENDBAR' if abweichende_letztwillige_anordnung else 'BERECHNET'
    return ergebnis
