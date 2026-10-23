"""Gemeinsame Zuwendungs-/Leistungsrechnung ohne Mehrempfangausschluss (§§2055/2057a)."""
from .betraege import _geld, _wahrheitswert
from .kalender import _ergebnis, _fehler, _text, _vorhanden
from .zahlen import _addieren, _bruch, _multiplizieren, _subtrahieren, _zahleneingabe
from .zinsen import _bruchteile


from .getrennter_erbausgleich import erbteilung_getrennter_zuwendungs_leistungsausgleich

def pflichtteil_getrennter_zuwendungs_leistungsausgleich(gruppennachlass=None, miterben=None, berechtigter_id=None,
    zugleich_anrechenbarer_zuwendungswert=None, hinterlassener_erbteilwert=None,
    fall_nach_2316_qualifiziert=None, bewertungsnachweis=None):
    """Getrennte Zuwendungs-/Leistungsempfänger einschließlich2056: hypothetische Zuteilung halbieren und2316IV berücksichtigen."""
    name = _text(berechtigter_id, 'berechtigter_id')
    anrechnung = _geld(zugleich_anrechenbarer_zuwendungswert)
    hinterlassen = _geld(hinterlassener_erbteilwert)
    _wahrheitswert(fall_nach_2316_qualifiziert, 'fall_nach_2316_qualifiziert')
    teilung = erbteilung_getrennter_zuwendungs_leistungsausgleich(gruppennachlass, miterben, True, bewertungsnachweis)
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
    ergebnis = _ergebnis(wert, 'EUR', 'BGB_PFLICHTTEIL_GETRENNTER_ZUWENDUNGS_LEISTUNGSAUSGLEICH', eingaben,
        [dict(operation='Gemischte hypothetische Zuteilung halbieren; halbe zugleich2315-anrechenbare Zuwendung abziehen, mindestens null; positiven Mehrbetrag bestimmen')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Hypothetische gesetzliche Ausgleichungsgruppe nach2316 einschließlich Erbverzichtsausschluss,Ausstattungsschutz,getrennter Empfänger und Leistungsvorwegabzugsreihenfolge rechtlich qualifiziert.']
    ergebnis['hinweise'] = ['Nur fachlich qualifizierter Leistungsvorwegabzug mit getrennten Zuwendungs-/Leistungsempfängern: vorhandene2056-Ausscheidung ausschließlich Nichtleistender. Positive Zuwendung und positive Leistung derselben Person ergeben NICHT_ANWENDBAR; zugleich leistende Überempfänger bleiben ungelöst. Doppelanrechnungswert ist bereits in eigener Ausgleichungsposition enthalten und auf derselben Wertgrundlage bestimmt; keine weiteren reinen2315-Zuwendungen,2325-Ergänzung oder Vermächtnisanrechnung. Für enterbten Berechtigten hinterlassenen Erbteil null, sonst rechtlich maßgeblichen Wert eingeben. Mehrbetrag2316II hängt nicht von nomineller Halbquote ab.']
    return ergebnis
