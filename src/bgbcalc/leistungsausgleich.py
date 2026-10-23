"""Rechnerische Verteilung eines qualifizierten Leistungsausgleichs (§2057a Absatz4)."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _fehler, _text, _vorhanden
from .zahlen import _addieren, _bruch, _multiplizieren, _subtrahieren, _zahleneingabe
from .zinsen import _bruchteile


def erbteilung_leistungsausgleich(nachlasswert_der_ausgleichungsgemeinschaft=None,
    miterben=None, leistungsausgleich_2057a_anwendbar=None, weitere_ausgleichungsposten_vorhanden=None,
    bewertungsnachweis=None):
    """Ausgleichsbeträge abziehen, Rest nach relativen Erbquoten teilen, individuelle Beträge hinzufügen."""
    nachlass = _geld(nachlasswert_der_ausgleichungsgemeinschaft)
    _vorhanden(miterben, 'miterben')
    if not isinstance(miterben, list) or not 2 <= len(miterben) <= 1000:
        _fehler('miterben', 'Liste mit 2 bis 1000 rechtlich bestimmten Miterben der Ausgleichungsgemeinschaft erforderlich.')
    namen, quoten, ausgleiche = [], [], []
    quotensumme, ausgleichssumme = _bruch(0), _bruch(0)
    for eintrag in miterben:
        if not isinstance(eintrag, dict) or set(eintrag) != {'miterbe_id', 'relative_erbquote', 'leistungs_ausgleichsbetrag'}:
            _fehler('miterben', 'Genau miterbe_id, relative_erbquote und leistungs_ausgleichsbetrag erforderlich.')
        name = _text(eintrag['miterbe_id'], 'miterbe_id')
        if name in namen:
            _fehler('miterbe_id', 'Miterben dürfen nicht doppelt vorkommen.')
        quote = _zahleneingabe(eintrag['relative_erbquote'])
        if not 0 < quote <= 1:
            _fehler('relative_erbquote', 'Positive Erbquote höchstens eins erforderlich.')
        ausgleich = _geld(eintrag['leistungs_ausgleichsbetrag'])
        quotensumme = _addieren(quotensumme, quote)
        ausgleichssumme = _addieren(ausgleichssumme, ausgleich)
        namen.append(name); quoten.append(quote); ausgleiche.append(ausgleich)
    if quotensumme != 1:
        _fehler('miterben', 'Relative Erbquoten innerhalb der Ausgleichungsgemeinschaft müssen zusammen eins ergeben.')
    if ausgleichssumme > nachlass:
        _fehler('miterben', 'Ausgleichsbeträge oberhalb des zugeordneten Nachlasswerts liegen außerhalb dieses Verteilungsmodells; rechtliche Bewertung zuerst klären.')
    _wahrheitswert(leistungsausgleich_2057a_anwendbar, 'leistungsausgleich_2057a_anwendbar')
    _wahrheitswert(weitere_ausgleichungsposten_vorhanden, 'weitere_ausgleichungsposten_vorhanden')
    _text(bewertungsnachweis, 'bewertungsnachweis')
    eingaben = dict(nachlasswert_der_ausgleichungsgemeinschaft=nachlasswert_der_ausgleichungsgemeinschaft,
        miterben=miterben, leistungsausgleich_2057a_anwendbar=leistungsausgleich_2057a_anwendbar,
        weitere_ausgleichungsposten_vorhanden=weitere_ausgleichungsposten_vorhanden, bewertungsnachweis=bewertungsnachweis)
    ergebnis = _geld_ergebnis(None, 'BGB_ERBTEILUNG_LEISTUNGSAUSGLEICH', eingaben,
        [dict(operation='Summe rechtlich bestimmter Leistungsausgleichsbeträge vom zugehörigen Nachlass abziehen; Rest nach Erbquoten und individuelle Ausgleiche zusätzlich zuteilen')])
    if leistungsausgleich_2057a_anwendbar and not weitere_ausgleichungsposten_vorhanden:
        rest = _subtrahieren(nachlass, ausgleichssumme)
        ergebnis['wert'] = dict(verteilungsrest=_bruchteile(rest), zuteilungen=[
            dict(miterbe_id=n, erbteil_nach_leistungsausgleich=_bruchteile(_addieren(_multiplizieren(rest, q), a)))
            for n, q, a in zip(namen, quoten, ausgleiche)])
        ergebnis['status'] = 'BERECHNET'
    ergebnis['hinweise'].append('Nur rechnerische Verteilung nach§2057a Absatz4 im isolierten Leistungsausgleichsfall. Nachlasswert umfasst ausschließlich den Anteil, der den ausgleichenden Miterben zusteht; andere Erben nicht mitbelasten. Relative Erbquoten beziehen sich auf diese Gemeinschaft, nicht ungeprüft Gesamtnachlass. Anspruchsberechtigte Abkömmlinge und gesetzliche Erbfolge beziehungsweise§2052 rechtlich bestimmen. Ausgleichsbeträge müssen nach Absatz3 unter Berücksichtigung von Dauer, Umfang und Nachlasswert billig bemessen sein; keine automatische Pflegevergütung oder erfundener Stundensatz. Angemessenes gewährtes/vereinbartes Entgelt und anderweitige Ansprüche schließen nach Absatz2 entsprechend aus; Eingabebeträge müssen dies bereits berücksichtigen. Weitere auszugleichende Zuwendungen oder sonstige Ausgleichungsposten erfordern ein kombiniertes Modell und ergeben hier NICHT_ANWENDBAR. Ausgleichssumme über zugehörigem Nachlass wird nicht durch erfundene Kürzung geheilt. Ergebnis ist wertmäßige Teilung, keine Übertragung bestimmter Nachlassgegenstände.')
    return ergebnis
