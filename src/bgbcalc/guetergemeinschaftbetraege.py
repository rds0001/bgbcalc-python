"""Proportionale Einbringungsrückerstattung und Freistellungsbeträge der Gütergemeinschaft."""
from .betraege import _geld
from .kalender import _ergebnis, _fehler, _text
from .zahlen import _addieren, _bruch, _dividieren, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile


def guetergemeinschaft_einbringungsrueckerstattung(verfuegbares_gesamtgut=None, einbringungswert_ehegatte=None, einbringungswert_anderer=None, bewertungsnachweis=None):
    """§1478: qualifizierte Einbringungswerte erstatten, Fehlbetrag proportional tragen."""
    gut = _geld(verfuegbares_gesamtgut)
    erster = _geld(einbringungswert_ehegatte)
    zweiter = _geld(einbringungswert_anderer)
    _text(bewertungsnachweis, 'bewertungsnachweis')
    summe = _addieren(erster, zweiter)
    verteilung = min(gut, summe)
    erster_erstattung = _bruch(0) if summe == 0 else _multiplizieren(verteilung, _dividieren(erster, summe))
    zweiter_erstattung = _subtrahieren(verteilung, erster_erstattung)
    eingaben = dict(verfuegbares_gesamtgut=verfuegbares_gesamtgut, einbringungswert_ehegatte=einbringungswert_ehegatte, einbringungswert_anderer=einbringungswert_anderer, bewertungsnachweis=bewertungsnachweis)
    wert = {k:_bruchteile(v) for k,v in dict(rueckerstattung_ehegatte=erster_erstattung,rueckerstattung_anderer=zweiter_erstattung,fehlbetrag_ehegatte=_subtrahieren(erster,erster_erstattung),fehlbetrag_anderer=_subtrahieren(zweiter,zweiter_erstattung),verbleibendes_gesamtgut=_subtrahieren(gut,verteilung)).items()}
    ergebnis = _ergebnis(wert, 'EUR', 'BGB_GUETERGEMEINSCHAFT_EINBRINGUNGSRUECKERSTATTUNG', eingaben, [dict(operation='Verfügbares Gesamtgut höchstens bis Summe der Einbringungswerte proportional zurückerstatten; Fehlbeträge und verbleibendes Gesamtgut gesondert ausweisen.')], eingaben.copy())
    ergebnis['hinweise'] = ['Scheidung vor Abschluss der Auseinandersetzung und erforderliches Verlangen nach§1478I sind vorausgesetzt. Einbringungswerte nachAbsatz2 qualifiziert und nachAbsatz3 zum Zeitpunkt der jeweiligen Einbringung bewertet. Verfügbares Gesamtgut bereits nach vorrangiger Verbindlichkeitenberichtigung und erforderlichen Rückbehalten bestimmt. Ersatzforderungen/Anrechnung nach§1476II und anschließende Überschussverteilung sind gesonderte Berechnungen. Keine Bewertung von Gegenständen oder automatische Güterstandsprüfung. Bei beiden Einbringungswerten null keine Rückerstattung und keine Division durch null.']
    return ergebnis


def guetergemeinschaft_freistellungsbetrag(verbindlichkeit=None, inanspruchnahme=None, verwaltungsfall=None, aus_gesamtgut_erlangt=None, zuordnungsnachweis=None):
    """§1481: über die interne Belastungsgrenze hinausgehenden Betrag berechnen."""
    schuld = _geld(verbindlichkeit)
    anspruch = _geld(inanspruchnahme)
    erlangt = _geld(aus_gesamtgut_erlangt)
    _text(verwaltungsfall, 'verwaltungsfall')
    _text(zuordnungsnachweis, 'zuordnungsnachweis')
    if verwaltungsfall not in ['alleinverwaltung_anderer', 'gemeinschaftlich', 'alleinlast_anderer']:
        _fehler('verwaltungsfall', 'alleinverwaltung_anderer, gemeinschaftlich oder alleinlast_anderer erforderlich.')
    if anspruch > schuld:
        _fehler('inanspruchnahme', 'Inanspruchnahme darf die erfasste Verbindlichkeit nicht übersteigen.')
    grenze = _dividieren(schuld, _bruch(2))
    if verwaltungsfall == 'alleinverwaltung_anderer':
        grenze = min(grenze, erlangt)
    if verwaltungsfall == 'alleinlast_anderer':
        grenze = _bruch(0)
    eingaben = dict(verbindlichkeit=verbindlichkeit, inanspruchnahme=inanspruchnahme, verwaltungsfall=verwaltungsfall, aus_gesamtgut_erlangt=aus_gesamtgut_erlangt, zuordnungsnachweis=zuordnungsnachweis)
    wert = dict(interne_belastungsgrenze=_bruchteile(grenze),freistellungsbetrag=_bruchteile(max(_subtrahieren(anspruch,grenze),_bruch(0))))
    ergebnis = _ergebnis(wert,'EUR','BGB_GUETERGEMEINSCHAFT_FREISTELLUNGSBETRAG',eingaben,[dict(operation='Interne Grenze ist Hälfte der Verbindlichkeit, bei Alleinverwaltung des anderen zusätzlich höchstens Erlangtes, bei Alleinlast des anderen null; darüber liegende Inanspruchnahme freistellen.')],eingaben.copy())
    ergebnis['hinweise'] = ['Ein einzelner noch unberichtigter, vor Berichtigung geteiltem Gesamtgut zugeordneter Schuldposten. Beträge einschließlich rechtlich zugeordneter Nebenforderungen konsistent abgrenzen. alleinverwaltung_anderer bezeichnet den Schutz des nicht allein verwaltenden Ehegatten nachAbsatz1; gemeinschaftlich Absatz2. alleinlast_anderer bezeichnet ausschließlich interne Alleinlast des anderen Ehegatten nachAbsatz3 und geht Verwaltungssituation vor. Qualifizierte Zuordnung ist keine freie Wahl. Erlangtes wird nur inAbsatz1 als zusätzliche Grenze verwendet; inAbsätzen2/3 nicht automatisch anrechnen. Keine Änderung der Außenhaftung gegenüber Gläubigern und keine Mehrschuld-/Gesamthaftungsverrechnung.']
    return ergebnis
