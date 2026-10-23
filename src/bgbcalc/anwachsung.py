"""Anwachsung eines einzelnen Erbteils mit Gruppenvorrang (§§2094,2095,2099)."""
from .betraege import _wahrheitswert
from .kalender import _ergebnis, _fehler, _text, _vorhanden
from .zahlen import _addieren, _bruch, _dividieren, _multiplizieren, _zahleneingabe
from .zinsen import _bruchteile


def erbteil_anwachsungsquoten(eingesetzte_erben=None, weggefallener_erbe_id=None,
    gesetzliche_erbfolge_ausgeschlossen=None, anwachsung_testamentarisch_ausgeschlossen=None,
    vorrangiges_ersatzerbrecht=None, einordnungsnachweis=None):
    """Einen wegfallenden Originalerbteil proportional, vorrangig innerhalb seiner Gruppe verteilen."""
    _vorhanden(eingesetzte_erben, 'eingesetzte_erben')
    if not isinstance(eingesetzte_erben, list) or not 2 <= len(eingesetzte_erben) <= 1000:
        _fehler('eingesetzte_erben', 'Liste mit 2 bis 1000 eingesetzten Erben erforderlich.')
    namen, quoten, gruppen = [], [], []
    summe = _bruch(0)
    for erbe in eingesetzte_erben:
        if not isinstance(erbe, dict) or set(erbe) != {'erbe_id', 'erbquote', 'gemeinschaft_id'}:
            _fehler('eingesetzte_erben', 'Genau erbe_id, erbquote und gemeinschaft_id erforderlich.')
        name = _text(erbe['erbe_id'], 'erbe_id')
        if name in namen:
            _fehler('erbe_id', 'Erben dürfen nicht doppelt vorkommen.')
        quote = _zahleneingabe(erbe['erbquote'])
        if not 0 < quote <= 1:
            _fehler('erbquote', 'Positive Originalquote höchstens eins erforderlich.')
        gruppe = erbe['gemeinschaft_id']
        if gruppe is not None:
            _text(gruppe, 'gemeinschaft_id')
        namen.append(name)
        quoten.append(quote)
        gruppen.append(gruppe)
        summe = _addieren(summe, quote)
    weg = _text(weggefallener_erbe_id, 'weggefallener_erbe_id')
    if weg not in namen:
        _fehler('weggefallener_erbe_id', 'Weggefallener Erbe muss genau einmal in der Originalliste stehen.')
    _wahrheitswert(gesetzliche_erbfolge_ausgeschlossen, 'gesetzliche_erbfolge_ausgeschlossen')
    _wahrheitswert(anwachsung_testamentarisch_ausgeschlossen, 'anwachsung_testamentarisch_ausgeschlossen')
    _wahrheitswert(vorrangiges_ersatzerbrecht, 'vorrangiges_ersatzerbrecht')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    if summe > 1 or (gesetzliche_erbfolge_ausgeschlossen and summe != 1) or (not gesetzliche_erbfolge_ausgeschlossen and summe >= 1):
        _fehler('eingesetzte_erben', 'Bei vollständigem Ausschluss gesetzlicher Erbfolge Quotensumme eins, bei verbleibendem gesetzlichen Erbteil strikt unter eins erforderlich.')
    index = namen.index(weg)
    uebrige = [i for i in range(len(namen)) if i != index]
    empfaenger = [i for i in uebrige if gruppen[index] is not None and gruppen[i] == gruppen[index]]
    if not empfaenger and gesetzliche_erbfolge_ausgeschlossen:
        empfaenger = uebrige
    if anwachsung_testamentarisch_ausgeschlossen or vorrangiges_ersatzerbrecht:
        empfaenger = []
    verteilungssumme = _bruch(0)
    for i in empfaenger:
        verteilungssumme = _addieren(verteilungssumme, quoten[i])
    anteile = []
    for i in uebrige:
        zusatz = _multiplizieren(quoten[index], _dividieren(quoten[i], verteilungssumme)) if i in empfaenger else _bruch(0)
        anteile.append(dict(erbe_id=namen[i], urspruenglicher_erbteil=_bruchteile(quoten[i]),
            angewachsener_erbteil=_bruchteile(zusatz), gesamter_erbteil=_bruchteile(_addieren(quoten[i], zusatz))))
    wert = dict(anwachsung_erfolgt=bool(empfaenger), erbteile=anteile,
        nicht_angewachsener_wegfallender_erbteil=_bruchteile(_bruch(0) if empfaenger else quoten[index]))
    eingaben = dict(eingesetzte_erben=eingesetzte_erben, weggefallener_erbe_id=weggefallener_erbe_id,
        gesetzliche_erbfolge_ausgeschlossen=gesetzliche_erbfolge_ausgeschlossen,
        anwachsung_testamentarisch_ausgeschlossen=anwachsung_testamentarisch_ausgeschlossen,
        vorrangiges_ersatzerbrecht=vorrangiges_ersatzerbrecht, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert, 'erbquoten', 'BGB_ERBTEIL_ANWACHSUNGSQUOTEN', eingaben,
        [dict(operation='Empfängerkreis mit Gruppenvorrang und Ausschlüssen bestimmen; weggefallene Quote proportional zu Originalquoten verteilen')], eingaben.copy())
    ergebnis['annahmen'] = ['Ein einzelner rechtlich qualifizierter Wegfall; vollständig bestimmte Originalquoten und einfache, nicht verschachtelte gemeinschaftliche Erbteile; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['Alle eingesetzten Erben einschließlich weggefallenem Erben mit Originalquoten angeben. gemeinschaft_id bezeichnet gemeinsame Einsetzung auf denselben Erbteil, keine familiäre Nähe; NULL bedeutet keine Gruppe. Vorrang innerhalb der Gruppe des Weggefallenen; ohne verbleibendes Gruppenmitglied nur bei Ausschluss gesetzlicher Erbfolge allgemeine Anwachsung. Ausschluss nach§2094 Absatz3 bezieht sich hier auf die gesamte untersuchte Anwachsung; vorrangiges Ersatzerbrecht§2099 sperrt sie. Nicht angewachsene Quote wird weder einem gesetzlichen Erben noch einem Ersatzerben automatisch zugeteilt. Mehrere Wegfälle, verschachtelte Gruppen, individuelle Teil-Ausschlüsse und bereits angewachsene Sondererbteile außerhalb dieses Einzelschrittmodells. Angewachsener Teil bleibt für Vermächtnisse, Auflagen und Ausgleichung nach§2095 gesondert ausgewiesen; Gesamtquote beseitigt diese Trennung nicht.']
    return ergebnis
