"""Mehrere Eigengeschenke mit gemischter Anrechnungsbestimmung (§§2315,2327)."""
from .betraege import _geld, _wahrheitswert
from .kalender import _ergebnis, _fehler, _text, _vorhanden
from .pflichtteil import pflichtteil_betrag
from .zahlen import _addieren, _bruch, _multiplizieren, _subtrahieren, _zahleneingabe
from .zinsen import _bruchteile


def pflichtteilsergaenzung_mehrere_eigengeschenke(pflichtteilsnachlass=None, drittschenkungen_ergaenzungswert=None,
    eigengeschenke=None, gesetzliche_erbquote_zaehler=None, gesetzliche_erbquote_nenner=None,
    kombination_ohne_ausgleichung_qualifiziert=None, bewertungsnachweis=None):
    """Eigengeschenke sammeln,2315-Grundpflichtteil berechnen und2327-Ergänzung mit unterschiedlicher Anrechnungsbestimmung kombinieren."""
    nachlass = _zahleneingabe(pflichtteilsnachlass)
    dritt = _geld(drittschenkungen_ergaenzungswert)
    _vorhanden(eigengeschenke, 'eigengeschenke')
    if not isinstance(eigengeschenke, list) or len(eigengeschenke) > 1000:
        _fehler('eigengeschenke', 'Liste mit höchstens1000 überschneidungsfreien Eigengeschenken erforderlich.')
    namen = set()
    anrechenbar, nur_ergaenzung = _bruch(0), _bruch(0)
    for p in eigengeschenke:
        if not isinstance(p, dict) or set(p) != {'geschenk_id', 'einheitlicher_wert', 'anrechnung_nach_2315'}:
            _fehler('eigengeschenke', 'Genau geschenk_id, einheitlicher_wert und anrechnung_nach_2315 erforderlich.')
        name = _text(p['geschenk_id'], 'geschenk_id')
        if name in namen:
            _fehler('geschenk_id', 'Geschenk nicht doppelt erfassen.')
        namen.add(name)
        betrag = _geld(p['einheitlicher_wert'])
        _wahrheitswert(p['anrechnung_nach_2315'], 'anrechnung_nach_2315')
        if p['anrechnung_nach_2315']:
            anrechenbar = _addieren(anrechenbar, betrag)
        else:
            nur_ergaenzung = _addieren(nur_ergaenzung, betrag)
    _wahrheitswert(kombination_ohne_ausgleichung_qualifiziert, 'kombination_ohne_ausgleichung_qualifiziert')
    _text(bewertungsnachweis, 'bewertungsnachweis')
    ordentlich = _geld(pflichtteil_betrag(pflichtteilsnachlass, gesetzliche_erbquote_zaehler, gesetzliche_erbquote_nenner,
        _bruchteile(anrechenbar), True, True, bewertungsnachweis)['wert'])
    eingaben = dict(pflichtteilsnachlass=pflichtteilsnachlass, drittschenkungen_ergaenzungswert=drittschenkungen_ergaenzungswert,
        eigengeschenke=eigengeschenke, gesetzliche_erbquote_zaehler=gesetzliche_erbquote_zaehler,
        gesetzliche_erbquote_nenner=gesetzliche_erbquote_nenner, kombination_ohne_ausgleichung_qualifiziert=kombination_ohne_ausgleichung_qualifiziert,
        bewertungsnachweis=bewertungsnachweis)
    wert = None
    if kombination_ohne_ausgleichung_qualifiziert:
        eigene = _addieren(anrechenbar, nur_ergaenzung)
        gesamtbasis = max(_addieren(_addieren(nachlass, dritt), eigene), _bruch(0))
        quote = _multiplizieren(_bruch(gesetzliche_erbquote_zaehler, gesetzliche_erbquote_nenner), _bruch(1, 2))
        fiktiv = _multiplizieren(gesamtbasis, quote)
        ergaenzung = max(_subtrahieren(_subtrahieren(fiktiv, eigene), ordentlich), _bruch(0))
        wert = dict(eigengeschenke_mit_2315=_bruchteile(anrechenbar), eigengeschenke_ohne_2315=_bruchteile(nur_ergaenzung),
            ordentlicher_pflichtteil=_bruchteile(ordentlich), pflichtteilsergaenzung=_bruchteile(ergaenzung),
            gesamtanspruch=_bruchteile(_addieren(ordentlich, ergaenzung)))
    ergebnis = _ergebnis(wert, 'EUR', 'BGB_PFLICHTTEILSERGAENZUNG_MEHRERE_EIGENGESCHENKE', eingaben,
        [dict(operation='Eigengeschenke nach2315-Bestimmung summieren; ordentlichen Pflichtteil mit2315-Kern; fiktiven Gesamtpflichtteil minus alle Eigengeschenke minus ordentlichen Pflichtteil, mindestens null')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Je Eigengeschenk ein identischer rechtlich qualifizierter Wert für sämtliche verwendeten Hinzurechnungs-/Anrechnungsschritte; keine2316-Ausgleichung.']
    ergebnis['hinweise'] = ['A=Summe mit2315-Anrechnungsbestimmung,B=Summe ohne;ordentlich=max(q×max(N+A,0)−A,0),Ergänzung=max(q×max(N+D+A+B,0)−A−B−ordentlich,0). B darf ordentlichen Pflichtteil nicht vermindern; keine doppelte2315-Anrechnung vom Gesamtbetrag. Drittschenkungswerte bereits rechtlich bewertet und ggf.abgeschmolzen; Eigengeschenke nicht ungeprüft nach2325III abschmelzen. Unterschiedliche Wertansätze für dasselbe Geschenk nach2315 und2327, weitere reine2315-Zuwendungen außerhalb Geschenkbegriffs,2316-Ausgleichung und2326-Mehrhinterlassung liegen außerhalb dieses Modells. Mehrere unterschiedliche Geschenke dürfen verschiedene Werte und verschiedene Anrechnungsbestimmungen haben. Geschenke nach2327II/2051I gegebenenfalls rechtlich dem Abkömmling zurechnen. Keine automatische Anspruchsdurchsetzbarkeit oder Beschenktenhaftung2329.']
    return ergebnis
