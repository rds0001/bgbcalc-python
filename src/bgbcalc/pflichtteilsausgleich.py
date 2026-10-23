"""Pflichtteil nach hypothetischer Erbausgleichung (§2316)."""
from .betraege import _geld, _wahrheitswert
from .erbausgleich import erb_zuwendungen_ausgleichen
from .leistungsausgleich import erbteilung_leistungsausgleich
from .kalender import _auswahl, _ergebnis, _fehler, _text, _vorhanden
from .zahlen import _bruch, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile


def pflichtteil_nach_ausgleichung(gruppennachlass=None, ausgleichungsart=None, miterben=None,
    berechtigter_id=None, zugleich_anrechenbarer_zuwendungswert=None, hinterlassener_erbteilwert=None,
    fall_nach_2316_qualifiziert=None, bewertungsnachweis=None):
    """Hypothetische Gruppenteilung, Halbierung, halbe Doppelanrechnung und Zusatzpflichtteil."""
    _geld(gruppennachlass)
    _auswahl(ausgleichungsart, 'ausgleichungsart', ('zuwendungen', 'leistungen'))
    _vorhanden(miterben, 'miterben')
    if not isinstance(miterben, list) or not 2 <= len(miterben) <= 1000:
        _fehler('miterben', 'Zwei bis1000 hypothetische gesetzliche Miterben erforderlich.')
    name = _text(berechtigter_id, 'berechtigter_id')
    anrechnung = _geld(zugleich_anrechenbarer_zuwendungswert)
    hinterlassen = _geld(hinterlassener_erbteilwert)
    _wahrheitswert(fall_nach_2316_qualifiziert, 'fall_nach_2316_qualifiziert')
    _text(bewertungsnachweis, 'bewertungsnachweis')
    if ausgleichungsart == 'zuwendungen':
        teilung = erb_zuwendungen_ausgleichen(gruppennachlass, miterben, True, bewertungsnachweis)
        zeilen = teilung['wert']['verteilung']
        treffer = [p for p in zeilen if p['person_id'] == name]
        quelle = [p for p in miterben if p['person_id'] == name]
        if quelle and anrechnung > _geld(quelle[0]['ausgleichungswert']):
            _fehler('zugleich_anrechenbarer_zuwendungswert', 'Doppelanrechnung darf den auf gleicher Wertgrundlage erfassten eigenen Ausgleichungswert nicht übersteigen.')
        anteil = _geld(treffer[0]['betrag']) if treffer else None
    else:
        if anrechnung != 0:
            _fehler('zugleich_anrechenbarer_zuwendungswert', 'Isolierter Leistungsausgleich enthält keine zugleich ausgleichungspflichtige Zuwendung; hier null erforderlich.')
        teilung = erbteilung_leistungsausgleich(gruppennachlass, miterben, True, False, bewertungsnachweis)
        treffer = [p for p in teilung['wert']['zuteilungen'] if p['miterbe_id'] == name]
        anteil = _geld(treffer[0]['erbteil_nach_leistungsausgleich']) if treffer else None
    if anteil is None:
        _fehler('berechtigter_id', 'Berechtigter muss zur hypothetischen Ausgleichungsgruppe gehören.')
    eingaben = dict(gruppennachlass=gruppennachlass, ausgleichungsart=ausgleichungsart, miterben=miterben,
        berechtigter_id=berechtigter_id, zugleich_anrechenbarer_zuwendungswert=zugleich_anrechenbarer_zuwendungswert,
        hinterlassener_erbteilwert=hinterlassener_erbteilwert, fall_nach_2316_qualifiziert=fall_nach_2316_qualifiziert,
        bewertungsnachweis=bewertungsnachweis)
    wert = None
    if fall_nach_2316_qualifiziert:
        vor = _multiplizieren(anteil, _bruch(1, 2))
        halb = _multiplizieren(anrechnung, _bruch(1, 2))
        pflichtteil = max(_subtrahieren(vor, halb), _bruch(0))
        wert = dict(hypothetischer_gesetzlicher_erbteil=_bruchteile(anteil), pflichtteil_vor_doppelanrechnung=_bruchteile(vor),
            halber_anrechnungswert=_bruchteile(halb), pflichtteilswert=_bruchteile(pflichtteil),
            mehrbetrag_gegenueber_hinterlassenem_erbteil=_bruchteile(max(_subtrahieren(pflichtteil, hinterlassen), _bruch(0))))
    ergebnis = _ergebnis(wert, 'EUR', 'BGB_PFLICHTTEIL_NACH_AUSGLEICHUNG', eingaben,
        [dict(operation='Vorhandenen hypothetischen Teilungskern anwenden, individuellen Teilungsbetrag halbieren, zugleich anrechenbare Zuwendung nur halb abziehen; positiven Mehrbetrag bilden')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Rechtlich qualifizierte hypothetische gesetzliche Ausgleichungsgruppe; nur isolierte Zuwendungs- oder Leistungsausgleichung, keine Kombination beider Arten.']
    ergebnis['hinweise'] = ['Gruppennachlass umfasst nur den Anteil der ausgleichenden Abkömmlinge; relative Quoten summieren sich auf eins. Durch Erbverzicht ausgeschlossene Abkömmlinge2316I2 vorher entfernen und gesetzliche Gruppe/Quoten neu bestimmen. Ausstattungen2316III trotz Ausschlussanordnung berücksichtigen, soweit sonst Pflichtteilsnachteil; keine automatische Testamentsauslegung. Bei Zuwendungen rechnet vorhandener2055/2056-Kern einschließlich Überempfängerausschluss. Doppelanrechnungswert2316IV muss in eigener Ausgleichungsposition enthalten und auf derselben Wertgrundlage beurteilt sein; andere reine2315-Zuwendungen nicht zusätzlich hineinmischen. Leistungsausgleich nutzt2057a-Kern und setzt Doppelanrechnung null. Hinterlassenen Erbteilwert für enterbten Berechtigten null, für Erben rechtlich maßgeblich bewerten; Mehrbetrag2316II nicht an nominelle Halbquote binden. Keine2325-Ergänzung, Vermächtnisanrechnung oder gemeinsame Anwendung2055/2057a.']
    return ergebnis
