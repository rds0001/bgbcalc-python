"""Zuordnung von Zuwendungen aus Gesamtgut nach§2331."""
from .betraege import _geld, _wahrheitswert
from .kalender import _auswahl, _ergebnis, _text
from .zahlen import _bruch, _multiplizieren
from .zinsen import _bruchteile


def gesamtgutszuwendung_anteile(zuwendungswert=None, abstammungszuordnung=None,
    ersatzpflichtzuordnung=None, gesamtgut_anwendbar=None, einordnungsnachweis=None):
    """Hälftige oder gesetzlich ausschließliche Zuordnung, ohne Geschenkbewertung."""
    betrag = _geld(zuwendungswert)
    arten = ('keine', 'ehegatte_1', 'ehegatte_2')
    _auswahl(abstammungszuordnung, 'abstammungszuordnung', arten)
    _auswahl(ersatzpflichtzuordnung, 'ersatzpflichtzuordnung', arten)
    _wahrheitswert(gesamtgut_anwendbar, 'gesamtgut_anwendbar')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    eingaben = dict(zuwendungswert=zuwendungswert, abstammungszuordnung=abstammungszuordnung,
        ersatzpflichtzuordnung=ersatzpflichtzuordnung, gesamtgut_anwendbar=gesamtgut_anwendbar,
        einordnungsnachweis=einordnungsnachweis)
    sonder = {a for a in (abstammungszuordnung, ersatzpflichtzuordnung) if a != 'keine'}
    wert = None
    if gesamtgut_anwendbar and len(sonder) <= 1:
        zuordnung = next(iter(sonder), 'keine')
        quote = _bruch(1, 2) if zuordnung == 'keine' else _bruch(1 if zuordnung == 'ehegatte_1' else 0)
        andere = _bruch(1, 2) if zuordnung == 'keine' else _bruch(1 if zuordnung == 'ehegatte_2' else 0)
        wert = dict(quote_ehegatte_1=_bruchteile(quote), quote_ehegatte_2=_bruchteile(andere),
            betrag_ehegatte_1=_bruchteile(_multiplizieren(betrag, quote)),
            betrag_ehegatte_2=_bruchteile(_multiplizieren(betrag, andere)))
    ergebnis = _ergebnis(wert, 'quoten_und_EUR', 'BGB_GESAMTGUTSZUWENDUNG_ANTEILE', eingaben,
        [dict(operation='Gesamtgutszuwendung hälftig zurechnen; eindeutige Abstammungs- oder Ersatzpflichtausnahme ordnet sie ausschließlich einem Ehegatten zu')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Feste lokale BGB-Fassung; qualifizierter Wert der betrachteten Zuwendung und rechtlich geprüfte Zuordnungstatbestände.']
    ergebnis['hinweise'] = ['Abstammungsausnahme: Empfänger ist Abkömmling nur eines Ehegatten oder Person, von der nur einer der Ehegatten abstammt. Gemeinsame Abstammung begründet diese Ausnahme nicht. Ersatzpflicht betrifft gerade diese Zuwendung gegenüber dem Gesamtgut. Bei widersprechenden Zuordnungen keine erfundene Vorrangregel: NICHT_ANWENDBAR, gesondert klären. Gesamtgut der fortgesetzten Gütergemeinschaft nach Absatz2 eingeschlossen; Ehegatte_1/2 bezeichnet die ursprünglichen Ehegatten. Ergebnis ist Zurechnung für Pflichtteilsrecht, kein Eigentums- oder Zahlungsanspruch und keine Schenkungssteuerregel. Bewertungszeitpunkt, Pflichtteilsquote, Anrechnung und Abschmelzung gesondert berechnen.']
    return ergebnis
