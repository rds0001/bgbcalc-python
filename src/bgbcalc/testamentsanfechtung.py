"""Jahresfrist und Dreißigjahresgrenze der Testamentsanfechtung (§2082)."""
from .betraege import _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler, _frist, _text


def testament_anfechtungsfrist(
    erbfall_am=None, massgebliche_kenntnis_am=None, massgebliches_jahresfristende=None,
    massgeblicher_anfechtungstag=None, anfechtungsregel_2082_anwendbar=None,
    einordnungsnachweis=None,
):
    """§2082: ein Jahr ab maßgeblicher Kenntnis, höchstens 30 Jahre ab Erbfall."""
    erbfall = _datum(erbfall_am, 'erbfall_am')
    kenntnis = _datum(massgebliche_kenntnis_am, 'massgebliche_kenntnis_am')
    ende = _datum(massgebliches_jahresfristende, 'massgebliches_jahresfristende')
    tag = _datum(massgeblicher_anfechtungstag, 'massgeblicher_anfechtungstag')
    if kenntnis < erbfall:
        _fehler('massgebliche_kenntnis_am', 'Rechtlich maßgeblicher Kenntnisbeginn des Anfechtungsberechtigten darf nicht vor dem Erbfall liegen.')
    if tag < kenntnis:
        _fehler('massgeblicher_anfechtungstag', 'Anfechtungstag darf nicht vor dem maßgeblichen Kenntnisbeginn liegen.')
    _wahrheitswert(anfechtungsregel_2082_anwendbar, 'anfechtungsregel_2082_anwendbar')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    rohende = _frist(massgebliche_kenntnis_am, 1, 'jahre', 'ereignis')
    if ende < rohende:
        _fehler('massgebliches_jahresfristende', 'Maßgebliches Jahresfristende darf die kalendarische Grundfrist nicht verkürzen.')
    hoechst = _frist(erbfall_am, 30, 'jahre', 'ereignis')
    grenze = min(ende, hoechst)
    eingaben = dict(erbfall_am=erbfall_am, massgebliche_kenntnis_am=massgebliche_kenntnis_am,
        massgebliches_jahresfristende=massgebliches_jahresfristende,
        massgeblicher_anfechtungstag=massgeblicher_anfechtungstag,
        anfechtungsregel_2082_anwendbar=anfechtungsregel_2082_anwendbar, einordnungsnachweis=einordnungsnachweis)
    wert = None if not anfechtungsregel_2082_anwendbar else dict(
        rechnerisches_jahresfristende=rohende.isoformat(), dreissigjahresgrenze=hoechst.isoformat(),
        massgebliche_kalendergrenze=grenze.isoformat(), anfechtung_fristgerecht=tag <= grenze)
    ergebnis = _ergebnis(wert, 'daten_und_wahrheitswerte', 'BGB_TESTAMENT_ANFECHTUNGSFRIST', eingaben,
        [dict(operation='Jahresfrist ab maßgeblicher Kenntnis; qualifiziert korrigiertes Jahresende auf 30 Jahre ab Erbfall begrenzen')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if anfechtungsregel_2082_anwendbar else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Maßgeblicher Kenntnisbeginn des Anfechtungsberechtigten, rechtlich maßgeblicher Anfechtungstag und einschlägige Jahresfristkorrekturen qualifiziert vorgegeben; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['Nur Fristprüfung nach§2082: Anfechtungsgrund§§2078/2079, Berechtigung§2080 und Erklärungsempfänger/Form insbesondere§2081 separat prüfen. Kenntnisbeginn meint die rechtlich fristauslösende Kenntnis des Berechtigten; vorheriges Wissen vor Erbfall ist nicht ungeprüft als früherer Fristbeginn einzusetzen. Drohungsende ist hier kein selbständig gesetzlich genannter Fristauslöser wie bei§2283. Maßgebliches Jahresende berücksichtigt fachlich geprüfte§§206/210/211 und zulässige Kalenderkorrekturen; keine pauschale Hemmung oder Feiertagsverschiebung. Diese Korrekturen verlängern nicht automatisch die Dreißigjahresgrenze. Fristwahrung am maßgeblichen Endtag einschließlich; Versanddatum nicht pauschal als Erklärungstag einsetzen. Keine Rückwirkung, Verjährungsentscheidung oder automatische Unwirksamkeit der Verfügung. Erbvertragsanfechtung durch Erblasser§2283 sowie Ausschlagungs-/Annahme-Anfechtung§1954 sind eigene Regeln.']
    return ergebnis
