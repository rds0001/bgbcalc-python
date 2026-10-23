"""Gemeinsame Zuwendungs-/Leistungsrechnung ohne Mehrempfangausschluss (§§2055/2057a)."""
from .betraege import _geld, _wahrheitswert
from .kalender import _ergebnis, _fehler, _text, _vorhanden
from .zahlen import _addieren, _bruch, _multiplizieren, _subtrahieren, _zahleneingabe
from .zinsen import _bruchteile


def erbteilung_gemischter_ausgleich(gruppennachlass=None, miterben=None, gemischter_ausgleich_qualifiziert=None,
    bewertungsnachweis=None):
    """Zuwendungen hinzufügen, Leistungen abziehen; quotieren, individuelle Zuwendung abziehen und Leistung hinzufügen."""
    nachlass = _geld(gruppennachlass)
    _vorhanden(miterben, 'miterben')
    if not isinstance(miterben, list) or not 2 <= len(miterben) <= 1000:
        _fehler('miterben', 'Liste2..1000 rechtlich bestimmter Mitglieder derselben Ausgleichungsgruppe erforderlich.')
    namen, quoten, zuwendungen, leistungen = [], [], [], []
    quotensumme, zuwendungssumme, leistungssumme = _bruch(0), _bruch(0), _bruch(0)
    for p in miterben:
        if not isinstance(p, dict) or set(p) != {'person_id', 'relative_erbquote', 'ausgleichungswert_zuwendungen', 'leistungs_ausgleichsbetrag'}:
            _fehler('miterben', 'Genau person_id, relative_erbquote, ausgleichungswert_zuwendungen und leistungs_ausgleichsbetrag erforderlich.')
        name = _text(p['person_id'], 'person_id')
        if name in namen:
            _fehler('person_id', 'Jedes Gruppenmitglied nur einmal.')
        quote = _zahleneingabe(p['relative_erbquote'])
        if not 0 < quote <= 1:
            _fehler('relative_erbquote', 'Positive relative Quote höchstens eins erforderlich.')
        zuwendung = _geld(p['ausgleichungswert_zuwendungen'])
        leistung = _geld(p['leistungs_ausgleichsbetrag'])
        namen.append(name); quoten.append(quote); zuwendungen.append(zuwendung); leistungen.append(leistung)
        quotensumme = _addieren(quotensumme, quote)
        zuwendungssumme = _addieren(zuwendungssumme, zuwendung)
        leistungssumme = _addieren(leistungssumme, leistung)
    if quotensumme != 1:
        _fehler('relative_erbquote', 'Relative Quoten derselben Ausgleichungsgruppe müssen zusammen eins ergeben.')
    if leistungssumme > nachlass:
        _fehler('leistungs_ausgleichsbetrag', 'Leistungssumme über zugeordnetem Nachlass außerhalb dieses Modells; Billigkeitsbewertung zunächst klären.')
    _wahrheitswert(gemischter_ausgleich_qualifiziert, 'gemischter_ausgleich_qualifiziert')
    _text(bewertungsnachweis, 'bewertungsnachweis')
    masse = _addieren(_subtrahieren(nachlass, leistungssumme), zuwendungssumme)
    betraege = [_addieren(_subtrahieren(_multiplizieren(masse, q), z), l) for q, z, l in zip(quoten, zuwendungen, leistungen)]
    negativ = any(b < 0 for b in betraege)
    eingaben = dict(gruppennachlass=gruppennachlass, miterben=miterben,
        gemischter_ausgleich_qualifiziert=gemischter_ausgleich_qualifiziert, bewertungsnachweis=bewertungsnachweis)
    wert = None
    if gemischter_ausgleich_qualifiziert and not negativ:
        wert = dict(gemischte_rechenmasse=_bruchteile(masse), zuteilungen=[
            dict(person_id=name, erbteil_nach_gemischtem_ausgleich=_bruchteile(b)) for name, b in zip(namen, betraege)])
    ergebnis = _ergebnis(wert, 'EUR', 'BGB_ERBTEILUNG_GEMISCHTER_AUSGLEICH', eingaben,
        [dict(operation='N−SummeLeistungen+SummeZuwendungen; je Mitglied mit relativer Quote multiplizieren−eigeneZuwendung+eigeneLeistung')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Dieselbe vollständige rechtlich bestimmte Ausgleichungsgruppe für Zuwendungen und Leistungen; qualifizierte Werte auf zutreffender Bewertungsbasis.']
    ergebnis['hinweise'] = ['Leistungswerte2057aIII sind rechtlich billig bemessene, bereits um Ausschlüsse2057aII bereinigte Eingaben; keine erfundene Pflegevergütung. Zuwendungswerte2055II rechtlich bewertet. Rechenreihenfolge: Leistungssumme aus Gruppennachlass abziehen, Zuwendungssumme hinzufügen, quotieren, individuelle Zuwendung abziehen und Leistung hinzufügen. Endbeträge ergeben zusammen Gruppennachlass. Sobald ein individueller Endbetrag negativ wird, NICHT_ANWENDBAR: kombinierte2056-Mehrempfangausscheidung ist nicht durch einfache Nullkappung oder ungeprüfte Iteration gelöst. Kein Ersatz zwischen verschiedenen Ausgleichungsgruppen, keine automatische Gruppe/Erbenstatuswahl oder Pflichtteilsanrechnung.']
    return ergebnis


def pflichtteil_gemischte_ausgleichung(gruppennachlass=None, miterben=None, berechtigter_id=None,
    zugleich_anrechenbarer_zuwendungswert=None, hinterlassener_erbteilwert=None,
    fall_nach_2316_qualifiziert=None, bewertungsnachweis=None):
    """Gemischte hypothetische Ausgleichung halbieren; halbe Doppelanrechnung und Mehrbetrag2316II."""
    name = _text(berechtigter_id, 'berechtigter_id')
    anrechnung = _geld(zugleich_anrechenbarer_zuwendungswert)
    hinterlassen = _geld(hinterlassener_erbteilwert)
    _wahrheitswert(fall_nach_2316_qualifiziert, 'fall_nach_2316_qualifiziert')
    teilung = erbteilung_gemischter_ausgleich(gruppennachlass, miterben, True, bewertungsnachweis)
    personen = [p for p in miterben if p['person_id'] == name]
    if not personen:
        _fehler('berechtigter_id', 'Berechtigter muss zur hypothetischen Ausgleichungsgruppe gehören.')
    if anrechnung > _geld(personen[0]['ausgleichungswert_zuwendungen']):
        _fehler('zugleich_anrechenbarer_zuwendungswert', 'Doppelanrechnung höchstens eigener bereits enthaltener Zuwendungswert auf gleicher Wertgrundlage.')
    wert = None
    if fall_nach_2316_qualifiziert and teilung['wert'] is not None:
        anteil = _geld(next(p['erbteil_nach_gemischtem_ausgleich'] for p in teilung['wert']['zuteilungen'] if p['person_id'] == name))
        vor = _multiplizieren(anteil, _bruch(1, 2)); halb = _multiplizieren(anrechnung, _bruch(1, 2))
        pflichtteil = max(_subtrahieren(vor, halb), _bruch(0))
        wert = dict(hypothetischer_gesetzlicher_erbteil=_bruchteile(anteil), pflichtteil_vor_doppelanrechnung=_bruchteile(vor),
            halber_anrechnungswert=_bruchteile(halb), pflichtteilswert=_bruchteile(pflichtteil),
            mehrbetrag_gegenueber_hinterlassenem_erbteil=_bruchteile(max(_subtrahieren(pflichtteil, hinterlassen), _bruch(0))))
    eingaben = dict(gruppennachlass=gruppennachlass, miterben=miterben, berechtigter_id=berechtigter_id,
        zugleich_anrechenbarer_zuwendungswert=zugleich_anrechenbarer_zuwendungswert, hinterlassener_erbteilwert=hinterlassener_erbteilwert,
        fall_nach_2316_qualifiziert=fall_nach_2316_qualifiziert, bewertungsnachweis=bewertungsnachweis)
    ergebnis = _ergebnis(wert, 'EUR', 'BGB_PFLICHTTEIL_GEMISCHTE_AUSGLEICHUNG', eingaben,
        [dict(operation='Gemischte hypothetische Zuteilung halbieren; halbe zugleich2315-anrechenbare Zuwendung abziehen, mindestens null; positiven Mehrbetrag bestimmen')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Hypothetische gesetzliche Ausgleichungsgruppe nach2316 einschließlich Erbverzichtsausschluss und Ausstattungsschutz rechtlich qualifiziert.']
    ergebnis['hinweise'] = ['Grenzen des gemischten Teilungskerns gelten: negative individuelle Zuteilung ergibt NICHT_ANWENDBAR, keine ungeklärte2056-Mischfalliteration. Doppelanrechnungswert ist bereits in eigener Ausgleichungsposition enthalten und auf derselben Wertgrundlage bestimmt; keine weiteren reinen2315-Zuwendungen,2325-Ergänzung oder Vermächtnisanrechnung. Für enterbten Berechtigten hinterlassenen Erbteil null, sonst rechtlich maßgeblichen Wert eingeben. Mehrbetrag2316II hängt nicht von nomineller Halbquote ab.']
    return ergebnis
