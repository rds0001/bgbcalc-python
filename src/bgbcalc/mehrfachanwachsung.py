"""Mehrere gleichzeitig qualifizierte Wegfälle mit einfachen Anwachsungsgruppen."""
from .anwachsung import erbteil_anwachsungsquoten
from .betraege import _wahrheitswert
from .kalender import _ergebnis, _fehler, _text, _vorhanden
from .zahlen import _addieren, _bruch, _dividieren, _multiplizieren, _zahleneingabe
from .zinsen import _bruchteile


def erbteile_gleichzeitige_anwachsung(eingesetzte_erben=None, weggefallene_erben_ids=None,
    gesetzliche_erbfolge_ausgeschlossen=None, anwachsung_testamentarisch_ausgeschlossen=None,
    vorrangiges_ersatzerbrecht=None, gemeinsamer_wegfall_qualifiziert=None, einordnungsnachweis=None):
    """Originalanteile gemeinsam Weggefallener auf endgültig verbliebene Empfänger verteilen."""
    _vorhanden(weggefallene_erben_ids, 'weggefallene_erben_ids')
    if not isinstance(weggefallene_erben_ids, list) or not 1 <= len(weggefallene_erben_ids) <= 1000:
        _fehler('weggefallene_erben_ids', 'Liste1..1000 eindeutiger gleichzeitig weggefallener Erben erforderlich.')
    weg = [_text(x, 'weggefallene_erben_ids') for x in weggefallene_erben_ids]
    if len(set(weg)) != len(weg):
        _fehler('weggefallene_erben_ids', 'Weggefallene Erben nicht doppelt angeben.')
    _wahrheitswert(gemeinsamer_wegfall_qualifiziert, 'gemeinsamer_wegfall_qualifiziert')
    # Vorhandener Einzelfallkern prüft vollständige Originalquoten, Gruppen und Sperren.
    erbteil_anwachsungsquoten(eingesetzte_erben, weg[0], gesetzliche_erbfolge_ausgeschlossen,
        anwachsung_testamentarisch_ausgeschlossen, vorrangiges_ersatzerbrecht, einordnungsnachweis)
    namen = {p['erbe_id'] for p in eingesetzte_erben}
    if not set(weg) <= namen:
        _fehler('weggefallene_erben_ids', 'Jeder Wegfall muss in der Originalliste stehen.')
    uebrige = [p for p in eingesetzte_erben if p['erbe_id'] not in weg]
    sonderteile = []
    zusatz = {p['erbe_id']: _bruch(0) for p in uebrige}
    frei = _bruch(0)
    for p in eingesetzte_erben:
        if p['erbe_id'] not in weg:
            continue
        quote = _zahleneingabe(p['erbquote'])
        empfaenger = [q for q in uebrige if p['gemeinschaft_id'] is not None and p['gemeinschaft_id'] == q['gemeinschaft_id']]
        if not empfaenger and gesetzliche_erbfolge_ausgeschlossen:
            empfaenger = uebrige
        if anwachsung_testamentarisch_ausgeschlossen or vorrangiges_ersatzerbrecht:
            empfaenger = []
        summe = _bruch(0)
        for q in empfaenger:
            summe = _addieren(summe, _zahleneingabe(q['erbquote']))
        verteilung = []
        for q in empfaenger:
            anteil = _multiplizieren(quote, _dividieren(_zahleneingabe(q['erbquote']), summe))
            zusatz[q['erbe_id']] = _addieren(zusatz[q['erbe_id']], anteil)
            verteilung.append(dict(erbe_id=q['erbe_id'], angewachsener_erbteil=_bruchteile(anteil)))
        rest = _bruch(0) if empfaenger else quote
        frei = _addieren(frei, rest)
        sonderteile.append(dict(weggefallener_erbe_id=p['erbe_id'], verteilung=verteilung, nicht_angewachsener_erbteil=_bruchteile(rest)))
    wert = dict(sonderteile_nach_ursprung=sonderteile, erbteile=[dict(erbe_id=p['erbe_id'], urspruenglicher_erbteil=_bruchteile(_zahleneingabe(p['erbquote'])),
        angewachsener_erbteil=_bruchteile(zusatz[p['erbe_id']]), gesamter_erbteil=_bruchteile(_addieren(_zahleneingabe(p['erbquote']), zusatz[p['erbe_id']]))) for p in uebrige], nicht_angewachsene_wegfallquote=_bruchteile(frei)) if gemeinsamer_wegfall_qualifiziert else None
    eingaben = dict(eingesetzte_erben=eingesetzte_erben, weggefallene_erben_ids=weggefallene_erben_ids,
        gesetzliche_erbfolge_ausgeschlossen=gesetzliche_erbfolge_ausgeschlossen, anwachsung_testamentarisch_ausgeschlossen=anwachsung_testamentarisch_ausgeschlossen,
        vorrangiges_ersatzerbrecht=vorrangiges_ersatzerbrecht, gemeinsamer_wegfall_qualifiziert=gemeinsamer_wegfall_qualifiziert, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert, 'erbquoten', 'BGB_ERBTEILE_GLEICHZEITIGE_ANWACHSUNG', eingaben,
        [dict(operation='Gemeinsam Weggefallene vor Empfängerauswahl entfernen; jeden Originalteil mit Gruppenvorrang proportional zu verbleibenden Originalquoten verteilen; Sonderteile je Ursprung bewahren')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Ein gemeinsamer rechtlich qualifizierter Wegfallzeitpunkt, einfache nicht verschachtelte Gruppen und sämtliche Originalanteile vor Anwachsung.']
    ergebnis['hinweise'] = ['Keine zeitlich gestaffelte Kaskade: vorher angewachsene Sonderteile dürfen nicht als bloße Gesamtquote eingegeben werden. Gruppenvorrang je weggefallenem Originalteil; mangels überlebendem Gruppenmitglied allgemeine Anwachsung nur bei vollständigem Ausschluss gesetzlicher Erbfolge. Testamentarischer Ausschluss oder Ersatzerbvorrang betrifft hier sämtliche untersuchten Wegfälle einheitlich. Nicht angewachsene Quote wird nicht automatisch gesetzlichen/Ersatzerben zugeteilt. Sonderteile nach2095 bleiben nach Ursprung getrennt; Gesamtquote ist nur Summe. Verschachtelte Gruppen, individuelle Teilsperren und2098-Ersatzerbeneinsetzungen nicht umfasst.']
    return ergebnis
