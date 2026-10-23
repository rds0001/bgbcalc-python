from .betraege import _geld, _wahrheitswert
from .kalender import _ergebnis, _fehler, _text
from .zahlen import _addieren, _subtrahieren
from .zinsen import _bruchteile

def widerruf_rueckzahlung_lieferkosten(empfangene_warenzahlung=None, gezahlte_lieferkosten=None, abweichende_lieferart_gewaehlt=None, guenstigste_standardlieferkosten=None, einordnungsnachweis=None):
    """Empfangene Warenzahlung und erstattungsfähige Lieferkosten addieren; bei gewählter abweichender Lieferung nur zusätzliche Liefermehrkosten ausschließen."""
    waren = _geld(empfangene_warenzahlung);lieferung = _geld(gezahlte_lieferkosten)
    _wahrheitswert(abweichende_lieferart_gewaehlt,'abweichende_lieferart_gewaehlt')
    if abweichende_lieferart_gewaehlt:
        standard = _geld(guenstigste_standardlieferkosten)
        erstattbare_lieferung = min(lieferung,standard)
    else:
        if guenstigste_standardlieferkosten is not None:
            _fehler('guenstigste_standardlieferkosten','Ohne gewählte abweichende Lieferart keine Standardkostengrenze einsetzen.')
        erstattbare_lieferung = lieferung
    _text(einordnungsnachweis,'einordnungsnachweis')
    wert = dict(rueckzahlbare_lieferkosten=_bruchteile(erstattbare_lieferung),ausgeschlossene_liefermehrkosten=_bruchteile(_subtrahieren(lieferung,erstattbare_lieferung)),rueckzahlungsgrundbetrag=_bruchteile(_addieren(waren,erstattbare_lieferung)))
    eingaben = dict(empfangene_warenzahlung=empfangene_warenzahlung, gezahlte_lieferkosten=gezahlte_lieferkosten, abweichende_lieferart_gewaehlt=abweichende_lieferart_gewaehlt, guenstigste_standardlieferkosten=guenstigste_standardlieferkosten, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,"EUR",'BGB_WIDERRUF_RUECKZAHLUNG_LIEFERKOSTEN',eingaben,[dict(operation='Empfangene Warenzahlung und erstattungsfähige Lieferkosten addieren; bei gewählter abweichender Lieferung nur zusätzliche Liefermehrkosten ausschließen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§357I/II: grundsätzlich auch Lieferzahlungen zurückgewähren. Nur zusätzliche Kosten infolge gewählter abweichender Lieferart ausschließen; ohne diesen Tatbestand tatsächliche Lieferzahlung vollständig berücksichtigen. Standardvergleich auf denselben widerrufenen Lieferumfang beziehen, keine pauschale Zuordnung bei Teilwiderruf oder mehreren Warenkörben. Rücksendekosten357V/VI/VII, Wertersatz357a, mögliche Zahlungsverweigerung357IV, Rückzahlungsweg357III und Frist getrennt behandeln. Grundbetrag vor weiteren rechtlich zulässigen Anrechnungen; keine automatische Saldierung oder zusätzliche Rückabwicklungsgebühr.']
    return ergebnis
