"""Dreimonatsvorauszahlung der Geldleibrente mit voller begonnenen Periodenvergütung."""
from .betraege import _geld, _wahrheitswert
from .kalender import _datum, _frist, _text, _ergebnis
from .zahlen import _bruch, _multiplizieren
from .zinsen import _bruchteile


def leibrente_geldvorauszahlung(jahresrentenbetrag=None, vorauszahlungszeitraum_beginnt_am=None, beginn_des_zeitabschnitts_erlebt=None, einordnungsnachweis=None):
    """Geldleibrente für drei Monate im Voraus und ohne Kürzung einer begonnenen Periode berechnen."""
    jahr=_geld(jahresrentenbetrag); beginn=_datum(vorauszahlungszeitraum_beginnt_am,'vorauszahlungszeitraum_beginnt_am')
    _wahrheitswert(beginn_des_zeitabschnitts_erlebt,'beginn_des_zeitabschnitts_erlebt'); _text(einordnungsnachweis,'einordnungsnachweis')
    ende=_frist(vorauszahlungszeitraum_beginnt_am,3,'monate','tagesbeginn')
    regelbetrag=_multiplizieren(jahr,_bruch(1,4)); betrag=regelbetrag if beginn_des_zeitabschnitts_erlebt else _bruch(0)
    wert=dict(vorauszahlungszeitraum_beginnt_am=beginn.isoformat(),vorauszahlungszeitraum_endet_am=ende.isoformat(),dreimonats_regelbetrag=_bruchteile(regelbetrag),fuer_diesen_zeitabschnitt_gebuehrender_betrag=_bruchteile(betrag))
    eingaben=dict(jahresrentenbetrag=jahresrentenbetrag,vorauszahlungszeitraum_beginnt_am=vorauszahlungszeitraum_beginnt_am,beginn_des_zeitabschnitts_erlebt=beginn_des_zeitabschnitts_erlebt,einordnungsnachweis=einordnungsnachweis)
    ergebnis=_ergebnis(wert,'EUR_und_daten','BGB_LEIBRENTE_GELDVORAUSZAHLUNG',eingaben,[dict(operation='Jahresgeldrente durch vier teilen; drei Kalendermonate ab Tagesbeginn; voller Betrag bei qualifiziert erlebtem Beginn, sonst kein Betrag für diese neue Periode.')],eingaben.copy())
    ergebnis['hinweise']=['Nur §§759/760 gesetzlicher Geldleibrentenfall ohne abweichende Vereinbarung: Eingabebetrag ist rechtlich bestimmter Jahresbetrag, Beginn einer regulären Dreimonatsvorausperiode als Tagesbeginn qualifiziert. Nicht Sachrente, abweichende Zahlungsperiode oder besonders geregelte erste Rumpfperiode. Erleben des Beginns ausdrücklich rechtlich/tatsächlich bestimmen; ein bloßes Todesdatum ersetzt bei Grenzfällen keine Feststellung. Tod während einer begonnenen Periode führt hier nicht zu tageweiser Kürzung. Bei nicht erlebtem Beginn null ausschließlich für diese neue Periode, keine Rückforderung früherer Vorauszahlungen. Betrag grundsätzlich im Voraus zu entrichten; keine automatische Feiertagsverschiebung des Periodenendes oder Auslegung abweichender Lebensdauervereinbarungen.']
    return ergebnis
