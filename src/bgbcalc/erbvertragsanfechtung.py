"""Anfechtungsfrist des Erblassers beim Erbvertrag (§2283)."""
from .betraege import _wahrheitswert
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _text


def erbvertrag_anfechtungsfrist(
    erbvertrag_geschlossen_am=None, anfechtungsgrund=None, kenntnis_oder_zwangslageende_am=None,
    massgebliches_jahresfristende=None, massgeblicher_anfechtungstag=None,
    sonderfall_2283_absatz_3=None, sechsmonatsnachlauf_beginn_am=None,
    anfechtung_durch_erblasser_anwendbar=None, einordnungsnachweis=None,
):
    """Jahresfrist und gegebenenfalls Sechsmonatsuntergrenze nach §§2283 Absatz3,210."""
    vertrag = _datum(erbvertrag_geschlossen_am, 'erbvertrag_geschlossen_am')
    _auswahl(anfechtungsgrund, 'anfechtungsgrund', ('drohung', 'sonstiger_grund'))
    beginn = _datum(kenntnis_oder_zwangslageende_am, 'kenntnis_oder_zwangslageende_am')
    ende = _datum(massgebliches_jahresfristende, 'massgebliches_jahresfristende')
    tag = _datum(massgeblicher_anfechtungstag, 'massgeblicher_anfechtungstag')
    if beginn < vertrag:
        _fehler('kenntnis_oder_zwangslageende_am', 'Maßgeblicher Fristbeginn darf nicht vor Vertragsschluss liegen.')
    if tag < beginn:
        _fehler('massgeblicher_anfechtungstag', 'Anfechtungstag darf nicht vor dem maßgeblichen Fristbeginn liegen.')
    _wahrheitswert(sonderfall_2283_absatz_3, 'sonderfall_2283_absatz_3')
    _wahrheitswert(anfechtung_durch_erblasser_anwendbar, 'anfechtung_durch_erblasser_anwendbar')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    nachlaufbeginn = (_datum(sechsmonatsnachlauf_beginn_am, 'sechsmonatsnachlauf_beginn_am')
        if sechsmonatsnachlauf_beginn_am is not None or sonderfall_2283_absatz_3 else None)
    if nachlaufbeginn is not None and not vertrag <= nachlaufbeginn <= tag:
        _fehler('sechsmonatsnachlauf_beginn_am', 'Tatsächlicher Nachlaufbeginn muss zwischen Vertragsschluss und Anfechtungstag liegen.')
    rohende = _frist(kenntnis_oder_zwangslageende_am, 1, 'jahre', 'ereignis')
    if ende < rohende:
        _fehler('massgebliches_jahresfristende', 'Maßgebliches Jahresfristende darf die kalendarische Grundfrist nicht verkürzen.')
    nachlaufende = (_frist(sechsmonatsnachlauf_beginn_am, 6, 'monate', 'ereignis')
        if sonderfall_2283_absatz_3 else None)
    grenze = max(ende, nachlaufende) if nachlaufende is not None else ende
    eingaben = dict(erbvertrag_geschlossen_am=erbvertrag_geschlossen_am, anfechtungsgrund=anfechtungsgrund,
        kenntnis_oder_zwangslageende_am=kenntnis_oder_zwangslageende_am,
        massgebliches_jahresfristende=massgebliches_jahresfristende,
        massgeblicher_anfechtungstag=massgeblicher_anfechtungstag,
        sonderfall_2283_absatz_3=sonderfall_2283_absatz_3,
        sechsmonatsnachlauf_beginn_am=sechsmonatsnachlauf_beginn_am,
        anfechtung_durch_erblasser_anwendbar=anfechtung_durch_erblasser_anwendbar,
        einordnungsnachweis=einordnungsnachweis)
    wert = None if not anfechtung_durch_erblasser_anwendbar else dict(
        fristausloeser='ende_der_zwangslage' if anfechtungsgrund == 'drohung' else 'kenntnis_des_anfechtungsgrundes',
        rechnerisches_jahresfristende=rohende.isoformat(),
        sechsmonatsnachlauf_ende=nachlaufende.isoformat() if nachlaufende is not None else None,
        massgebliche_kalendergrenze=grenze.isoformat(), anfechtung_fristgerecht=tag <= grenze)
    ergebnis = _ergebnis(wert, 'daten_und_wahrheitswerte', 'BGB_ERBVERTRAG_ANFECHTUNGSFRIST', eingaben,
        [dict(operation='Drohung: Jahresfrist ab Zwangslageende; sonst ab Kenntnis; qualifizierter Sonderfall§2283 Absatz3 mit Sechsmonatsuntergrenze entsprechend§210')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if anfechtung_durch_erblasser_anwendbar else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Fristgrund und fristauslösender Zeitpunkt, korrigiertes Jahresende sowie gegebenenfalls Sonderfall§2283 Absatz3 und Beginn des Sechsmonatsnachlaufs rechtlich qualifiziert; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['Nur Anfechtung durch den Erblasser nach§2283, nicht durch Dritte nach§§2080/2285. Jahresende berücksichtigt gegebenenfalls§§206/210 und zulässige Kalenderkorrekturen, nicht automatisch§211. Sonderfall Absatz3 setzt voraus, dass der gesetzliche Vertreter nach§2282 Absatz2 nicht rechtzeitig angefochten hat und der Erblasser nach Wegfall der Geschäftsunfähigkeit selbst anfechten kann wie ohne gesetzlichen Vertreter. Nachlaufbeginn ist der rechtlich maßgebliche Zeitpunkt für die Sechsmonatsuntergrenze des§210; bloßer Betreuerwechsel oder ungeprüfte gesundheitliche Besserung genügt nicht. Im Sonderfall späteres Ende aus Jahresende und Sechsmonatsuntergrenze, kein pauschales neues volles Jahr. Ein gegebenenfalls bereits im korrigierten Jahresende enthaltener Nachlauf wird nicht nochmals addiert. Keine automatische Dreißigjahresgrenze aus§2082 und kein Neubeginn ab Erbfall. Anfechtungsgrund§§2078/2079/2281, persönliche Berechtigung, Vertretung, notarielle Beurkundung§2282, Empfänger und Bestätigung§2284 gesondert prüfen. Keine automatische Rückwirkung oder Unwirksamkeit.']
    return ergebnis
