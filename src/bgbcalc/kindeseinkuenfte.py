"""Rechnerische Verwendungskaskade qualifizierter Kindeseinkünfte nach§1649."""
from .betraege import _geld
from .kalender import _ergebnis, _text
from .zahlen import _bruch, _subtrahieren
from .zinsen import _bruchteile


def kindeseinkuenfte_verwendungsbetraege(vermoegenseinkuenfte=None, verwaltungsbedarf=None, kindesunterhalt=None, erwerbseinkuenfte=None, billiger_familienbedarf=None, bewertungsnachweis=None):
    """Verwaltungsbedarf, Kindesbedarf und qualifizierten Familienbedarf in gesetzlicher Reihenfolge berücksichtigen."""
    vermoegen = _geld(vermoegenseinkuenfte)
    verwaltung = _geld(verwaltungsbedarf)
    kind = _geld(kindesunterhalt)
    erwerb = _geld(erwerbseinkuenfte)
    familie = _geld(billiger_familienbedarf)
    _text(bewertungsnachweis, 'bewertungsnachweis')
    verfuegbar = max(_subtrahieren(vermoegen, verwaltung), _bruch(0))
    verm_kind = min(verfuegbar, kind)
    rest_kind = _subtrahieren(kind, verm_kind)
    erw_kind = min(erwerb, rest_kind)
    ueberschuss = _subtrahieren(verfuegbar, verm_kind)
    familienbetrag = min(ueberschuss, familie)
    eingaben = dict(vermoegenseinkuenfte=vermoegenseinkuenfte, verwaltungsbedarf=verwaltungsbedarf, kindesunterhalt=kindesunterhalt, erwerbseinkuenfte=erwerbseinkuenfte, billiger_familienbedarf=billiger_familienbedarf, bewertungsnachweis=bewertungsnachweis)
    wert = {k:_bruchteile(v) for k,v in dict(verfuegbare_vermoegenseinkuenfte=verfuegbar, vermoegenseinkuenfte_fuer_kind=verm_kind, erwerbseinkuenfte_fuer_kind_einsetzbar=erw_kind, ungedeckter_kindesbedarf=_subtrahieren(rest_kind, erw_kind), vermoegenseinkuenfte_fuer_familie_einsetzbar=familienbetrag, verbleibende_vermoegenseinkuenfte=_subtrahieren(ueberschuss, familienbetrag), verbleibende_erwerbseinkuenfte=_subtrahieren(erwerb, erw_kind)).items()}
    ergebnis = _ergebnis(wert, 'EUR', 'BGB_KINDESEINKUENFTE_VERWENDUNGSBETRAEGE', eingaben, [dict(operation='Verwaltungsbedarf vor Kindesunterhalt aus Vermögenseinkünften; Erwerb nur bis verbleibendem Kindesbedarf, Familie nur aus überschüssigen Vermögenseinkünften.')], eingaben.copy())
    ergebnis['hinweise'] = ['Alle Einkünfte und Bedarfe beziehen sich auf denselben qualifizierten Zeitraum. Erwerbseinkünfte nur aus Arbeit oder nach§112 gestattetem Geschäft. Verwaltungsbedarf nicht automatisch auf Erwerbseinkünfte verlagern. Erwerbseinsatz und Familienverwendung sind zulässige rechnerische Höchstbeträge, keine Anordnung einer tatsächlichen Verwendung. Billiger Familienbedarf ist bereits rechtlich qualifiziert für Eltern und minderjährige Geschwister; Billigkeit und Verteilung zwischen Personen werden nicht erfunden. Kindesunterhalt und Kosten sind bewertete Eingaben; verbleibende Beträge unterstellen vollständigen Einsatz bis zum berechneten zulässigen Betrag. Vermögensstamm ist keine Einkunft.']
    return ergebnis
