"""Summe nicht zurückgegebener, weiterhin zahlbarer Zinsscheine (§803 Absatz2)."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _fehler, _text, _vorhanden
from .zahlen import _addieren, _bruch


def zinsscheine_zurueckbehaltungsbetrag(
    zinsscheine=None, einloesung_der_hauptschuldverschreibung=None, einordnungsnachweis=None,
):
    """Nur nicht zurückgegebene Zinsscheine mit fortbestehender Zahlungspflicht summieren."""
    _vorhanden(zinsscheine, 'zinsscheine')
    if not isinstance(zinsscheine, list) or len(zinsscheine) > 1000:
        _fehler('zinsscheine', 'Liste mit höchstens1000 eindeutig identifizierten Zinsscheinen erforderlich; leere Liste ist zulässig.')
    namen = set()
    summe = _bruch(0)
    for schein in zinsscheine:
        if not isinstance(schein, dict) or set(schein) != {'schein_id', 'zahlbetrag', 'zurueckgegeben', 'zahlungspflicht_nach_803_absatz_1'}:
            _fehler('zinsscheine', 'Genau schein_id, zahlbetrag, zurueckgegeben und zahlungspflicht_nach_803_absatz_1 erforderlich.')
        name = _text(schein['schein_id'], 'schein_id')
        if name in namen:
            _fehler('schein_id', 'Zinsschein darf nicht doppelt aufgeführt werden.')
        namen.add(name)
        betrag = _geld(schein['zahlbetrag'])
        zurueck = _wahrheitswert(schein['zurueckgegeben'], 'zurueckgegeben')
        pflicht = _wahrheitswert(schein['zahlungspflicht_nach_803_absatz_1'], 'zahlungspflicht_nach_803_absatz_1')
        if not zurueck and pflicht:
            summe = _addieren(summe, betrag)
    _wahrheitswert(einloesung_der_hauptschuldverschreibung, 'einloesung_der_hauptschuldverschreibung')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    eingaben = dict(zinsscheine=zinsscheine, einloesung_der_hauptschuldverschreibung=einloesung_der_hauptschuldverschreibung,
        einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(summe if einloesung_der_hauptschuldverschreibung else None,
        'BGB_ZINSSCHEINE_ZURUECKBEHALTUNGSBETRAG', eingaben,
        [dict(operation='Zahlbeträge nicht zurückgegebener Zinsscheine mit fortbestehender Zahlungspflicht nach§803 Absatz1 addieren')])
    ergebnis['hinweise'].append('Nur Zinsscheine zu dieser einzulösenden Inhaberschuldverschreibung; keine Vermischung mit Renten-/Gewinnanteilscheinen oder fremden Haupturkunden. Zahlungspflicht nach Absatz1 rechtlich vorgeben, einschließlich entgegenstehender Scheinbestimmungen und sonstiger Einwendungen; Erlöschen der Hauptforderung oder Änderung der Verzinsung allein lässt Zinsscheine nicht automatisch entfallen. Zahlbetrag ist tatsächlich geschuldeter Betrag, nicht erfundener Abzinsungs- oder Risikowert. Rückbehaltungsberechtigung wird nicht automatisch ausgeübt. Ergebnis ist die Summe der einschlägigen Scheinbeträge, kein negativer Auszahlungsbetrag, keine zusätzliche Zahlungspflicht des Einlösenden und keine automatische endgültige Kürzung der Hauptforderung. Leere oder vollständig ausgeschlossene Liste ergibt null EUR.')
    return ergebnis
