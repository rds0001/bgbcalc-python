"""Nichtunterbrechung der Ersitzung bei unfreiwilligem Besitzverlust (§940 Absatz2)."""
from .betraege import _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler, _frist, _text


def ersitzung_besitzverlust_nichtunterbrechung(
    eigenbesitzverlust_am=None, prueftag=None, massgebliches_jahresfristende=None,
    wiedererlangung_am=None, klageerhebung_am=None,
    eigenbesitz_ohne_willen_verloren=None, wiedererlangung_mittels_klage=None,
    einordnungsnachweis=None,
):
    """Jahresfrist und tatsächliche Wiedererlangung für §940 Absatz2 prüfen."""
    verlust = _datum(eigenbesitzverlust_am, 'eigenbesitzverlust_am')
    tag = _datum(prueftag, 'prueftag')
    if tag < verlust:
        _fehler('prueftag', 'Prüftag darf nicht vor dem Eigenbesitzverlust liegen.')
    rohende = _frist(eigenbesitzverlust_am, 1, 'jahre', 'ereignis')
    ende = _datum(massgebliches_jahresfristende, 'massgebliches_jahresfristende')
    if ende < rohende:
        _fehler('massgebliches_jahresfristende', 'Maßgebliches Fristende darf nicht vor dem kalendarischen Jahresfristende liegen.')
    wieder = _datum(wiedererlangung_am, 'wiedererlangung_am') if wiedererlangung_am is not None else None
    klage = _datum(klageerhebung_am, 'klageerhebung_am') if klageerhebung_am is not None else None
    for name, datum in [('wiedererlangung_am', wieder), ('klageerhebung_am', klage)]:
        if datum is not None and not verlust <= datum <= tag:
            _fehler(name, 'Tatsächliches Ereignis muss zwischen Eigenbesitzverlust und Prüftag liegen.')
    _wahrheitswert(eigenbesitz_ohne_willen_verloren, 'eigenbesitz_ohne_willen_verloren')
    _wahrheitswert(wiedererlangung_mittels_klage, 'wiedererlangung_mittels_klage')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    if wiedererlangung_mittels_klage:
        if wieder is None or klage is None:
            _fehler('wiedererlangung_mittels_klage', 'Wiedererlangung mittels Klage erfordert tatsächliche Wiedererlangung und Klageerhebung.', 'EINGABE_FEHLT')
        if klage > wieder:
            _fehler('klageerhebung_am', 'Ursächliche Klage darf nicht erst nach der Wiedererlangung erhoben sein.')
    direkt = wieder is not None and wieder <= ende
    klageweg = wiedererlangung_mittels_klage and klage <= ende
    eingaben = dict(eigenbesitzverlust_am=eigenbesitzverlust_am, prueftag=prueftag,
        massgebliches_jahresfristende=massgebliches_jahresfristende,
        wiedererlangung_am=wiedererlangung_am, klageerhebung_am=klageerhebung_am,
        eigenbesitz_ohne_willen_verloren=eigenbesitz_ohne_willen_verloren,
        wiedererlangung_mittels_klage=wiedererlangung_mittels_klage, einordnungsnachweis=einordnungsnachweis)
    wert = dict(kalendarisches_jahresfristende=rohende.isoformat(),
        massgebliches_jahresfristende=ende.isoformat(), wiedererlangung_binnen_jahresfrist=direkt,
        wiedererlangung_durch_rechtzeitige_klage=klageweg,
        unterbrechung_gilt_als_nicht_erfolgt=eigenbesitz_ohne_willen_verloren and (direkt or klageweg))
    ergebnis = _ergebnis(wert, 'daten_und_wahrheitswerte', 'BGB_ERSITZUNG_BESITZVERLUST_NICHTUNTERBRECHUNG', eingaben,
        [dict(operation='Unfreiwilliger Eigenbesitzverlust; tatsächliche Wiedererlangung innerhalb Jahresfrist oder mittels innerhalb Jahresfrist erhobener Klage')], eingaben.copy())
    ergebnis['annahmen'] = ['Qualifizierter Verlust und Wiedererlangung gerade des Eigenbesitzes; maßgebliches Fristende und wirksame Klageerhebung rechtlich bestimmt; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['NULL bei Wiedererlangung/Klage bedeutet bis Prüftag nicht eingetreten, nicht unbekannt. Eine rechtzeitige Klage allein genügt nicht: Eigenbesitz muss mittels dieser Klage tatsächlich wiedererlangt sein; spätere Wiedererlangung kann das Ergebnis ändern. Innerhalb der Jahresfrist genügt tatsächliche Wiedererlangung unabhängig vom Klageweg. Untertägige Reihenfolge bei gleichem Datum rechtlich vorgeben. Maßgebliches Jahresfristende separat begründen; ohne gesetzliche Korrektur kalendarisches Ende verwenden, keine pauschale Feiertagsverlängerung. Nur Nichtunterbrechung durch diesen Besitzverlust nach§940 Absatz2; andere Hemmungen§939, Vollstreckungsunterbrechung§941, Rechtsfolgen§942 und vollständiger Eigentumserwerb§937 werden nicht berechnet.']
    return ergebnis
