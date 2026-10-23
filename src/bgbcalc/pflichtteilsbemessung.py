"""Numerische Nachlassbemessung und Bedingungsausgleich (§§2311,2313)."""
from .betraege import _geld, _wahrheitswert
from .kalender import _auswahl, _ergebnis, _fehler, _ganzzahl, _text, _vorhanden
from .zahlen import GRENZE, _addieren, _bruch, _multiplizieren, _subtrahieren, _zahleneingabe
from .zinsen import _bruchteile


def pflichtteilsnachlass_positionssumme(nachlasspositionen=None, ehegattenvoraus_wert=None,
    berechtigter_abkoemmling_oder_elternteil=None, bewertungsnachweis=None):
    """Berücksichtigungsfähige Aktiva minus Passiva und einschlägigen Ehegattenvoraus summieren."""
    _vorhanden(nachlasspositionen, 'nachlasspositionen')
    if not isinstance(nachlasspositionen, list) or len(nachlasspositionen) > 1000:
        _fehler('nachlasspositionen', 'Liste mit höchstens1000 eindeutig abgegrenzten Positionen erforderlich.')
    namen = set()
    aktiva, passiva = _bruch(0), _bruch(0)
    for p in nachlasspositionen:
        if not isinstance(p, dict) or set(p) != {'position_id', 'betrag', 'vermoegensseite', 'ansatzart'}:
            _fehler('nachlasspositionen', 'Genau position_id, betrag, vermoegensseite und ansatzart erforderlich.')
        name = _text(p['position_id'], 'position_id')
        if name in namen:
            _fehler('position_id', 'Position nicht doppelt erfassen.')
        namen.add(name)
        betrag = _geld(p['betrag'])
        _auswahl(p['vermoegensseite'], 'vermoegensseite', ('aktiv', 'passiv'))
        _auswahl(p['ansatzart'], 'ansatzart', ('unbedingt', 'aufloesend_offen', 'aufschiebend_offen', 'ungewiss_oder_unsicher'))
        if p['ansatzart'] in ('unbedingt', 'aufloesend_offen'):
            if p['vermoegensseite'] == 'aktiv':
                aktiva = _addieren(aktiva, betrag)
            else:
                passiva = _addieren(passiva, betrag)
    voraus = _geld(ehegattenvoraus_wert)
    _wahrheitswert(berechtigter_abkoemmling_oder_elternteil, 'berechtigter_abkoemmling_oder_elternteil')
    _text(bewertungsnachweis, 'bewertungsnachweis')
    abzug = voraus if berechtigter_abkoemmling_oder_elternteil else _bruch(0)
    netto = _subtrahieren(_subtrahieren(aktiva, passiva), abzug)
    eingaben = dict(nachlasspositionen=nachlasspositionen, ehegattenvoraus_wert=ehegattenvoraus_wert,
        berechtigter_abkoemmling_oder_elternteil=berechtigter_abkoemmling_oder_elternteil, bewertungsnachweis=bewertungsnachweis)
    wert = dict(beruecksichtigte_aktiva=_bruchteile(aktiva), beruecksichtigte_passiva=_bruchteile(passiva),
        abgezogener_ehegattenvoraus=_bruchteile(abzug), pflichtteilsnachlass=_bruchteile(netto))
    ergebnis = _ergebnis(wert, 'EUR', 'BGB_PFLICHTTEILSNACHLASS_POSITIONSSUMME', eingaben,
        [dict(operation='Unbedingte und noch auflösend bedingte Positionen summieren; aufschiebend offene/ungewisse auslassen; Passiva und einschlägigen Voraus abziehen')], eingaben.copy())
    ergebnis['annahmen'] = ['Feste lokale BGB-Fassung; vollständige überschneidungsfreie rechtlich qualifizierte Nachlasspositionen und Werte zum einschlägigen Bewertungsstichtag.']
    ergebnis['hinweise'] = ['Voraus ist nur bei Pflichtteil von Abkömmlingen/Eltern abzuziehen und muss in den eingegebenen Aktiva enthalten sein, nicht bereits dort abgezogen. Ansätze nach2313 unterscheiden noch offene aufschiebende von noch offenen auflösenden Bedingungen. Nach Bedingungseintritt Rechtslage neu qualifizieren: fortbestehende Position unbedingt, endgültig entfallene Position entfernen. Ungewisse/unsichere Rechte und zweifelhafte Verbindlichkeiten zunächst auslassen. Inventar-/Bewertungskosten2314 und sonstige Abzugsfähigkeit rechtlich vorprüfen, nicht jeden Zahlungsbetrag als Passivum behandeln. Ergebnis darf negativ sein; nicht vorschnell vor Schenkungshinzurechnungen auf null setzen. Keine Immobilienbewertung, Landgutkapitalisierung2312, Pflichtteilsquote oder automatische Bedingungsprüfung.']
    return ergebnis


def pflichtteil_bemessungsausgleich(frueherer_pflichtteilsnachlass=None, neuer_pflichtteilsnachlass=None,
    gesetzliche_erbquote_zaehler=None, gesetzliche_erbquote_nenner=None,
    grundmodell_ohne_anrechnung_qualifiziert=None, bewertungsnachweis=None):
    """§2313: Differenz der Pflichtteilswerte aus rechtlich alter/neuer Nachlassbemessung."""
    alt = _zahleneingabe(frueherer_pflichtteilsnachlass)
    neu = _zahleneingabe(neuer_pflichtteilsnachlass)
    zaehler = _ganzzahl(gesetzliche_erbquote_zaehler, 'gesetzliche_erbquote_zaehler', 0, GRENZE)
    nenner = _ganzzahl(gesetzliche_erbquote_nenner, 'gesetzliche_erbquote_nenner', 1, GRENZE)
    if zaehler > nenner:
        _fehler('gesetzliche_erbquote', 'Gesetzliche Erbquote darf eins nicht übersteigen.')
    _wahrheitswert(grundmodell_ohne_anrechnung_qualifiziert, 'grundmodell_ohne_anrechnung_qualifiziert')
    _text(bewertungsnachweis, 'bewertungsnachweis')
    eingaben = dict(frueherer_pflichtteilsnachlass=frueherer_pflichtteilsnachlass, neuer_pflichtteilsnachlass=neuer_pflichtteilsnachlass,
        gesetzliche_erbquote_zaehler=gesetzliche_erbquote_zaehler, gesetzliche_erbquote_nenner=gesetzliche_erbquote_nenner,
        grundmodell_ohne_anrechnung_qualifiziert=grundmodell_ohne_anrechnung_qualifiziert, bewertungsnachweis=bewertungsnachweis)
    wert = None
    if grundmodell_ohne_anrechnung_qualifiziert:
        quote = _multiplizieren(_bruch(zaehler, nenner), _bruch(1, 2))
        vorher = _multiplizieren(max(alt, _bruch(0)), quote)
        nachher = _multiplizieren(max(neu, _bruch(0)), quote)
        wert = dict(frueherer_pflichtteilswert=_bruchteile(vorher), neuer_pflichtteilswert=_bruchteile(nachher),
            ausgleichsdifferenz=_bruchteile(_subtrahieren(nachher, vorher)))
    ergebnis = _ergebnis(wert, 'EUR', 'BGB_PFLICHTTEIL_BEMESSUNGSAUSGLEICH', eingaben,
        [dict(operation='Alte/neue Nachlassbasis jeweils mindestens null mit halber gesetzlicher Erbquote multiplizieren; neuer minus alter Pflichtteilswert')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Feste lokale BGB-Fassung; rechtlich begründete Neubemessung nach2313 bei unveränderter gesetzlicher Erbquote und ohne andere Anrechnungs-/Ausgleichungsregime.']
    ergebnis['hinweise'] = ['Positive Differenz bezeichnet höheren, negative Differenz niedrigeren Pflichtteilswert; nicht automatisch Zahlungs- oder Rückzahlungsanspruch in dieser Höhe, tatsächliche Vorleistungen und Einwendungen gesondert. Grundmodell ohne2315-Anrechnung,2316-Ausgleichung,2325-Ergänzung oder Vermächtnisanrechnung. Alte/neue Werte müssen denselben rechtlichen Bewertungsmaßstab mit korrekt geänderter Positionserfassung verwenden; keine willkürliche neue Marktpreisbewertung. Bei negativem Nachlass jede Basis vor Quotierung einzeln auf null setzen, nicht ungeprüft Nettoänderung mal Quote rechnen.']
    return ergebnis
