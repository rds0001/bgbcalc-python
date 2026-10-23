"""Numerische Zahlungszuordnung vor/nach Erbschaftskauf (§§2378–2380)."""
from .betraege import _geld, _wahrheitswert
from .kalender import _auswahl, _ergebnis, _fehler, _text, _vorhanden
from .zahlen import _addieren, _bruch, _subtrahieren
from .zinsen import _bruchteile


def erbschaftskauf_zahlungsausgleich(abrechnungsposten=None, gesetzliche_lastenverteilung_qualifiziert=None,
    abrechnungsnachweis=None):
    """Vorqualifizierte Nutzungs-/Lastenposten rechtlich zuordnen und kreuzweise empfangene/gezahlte Beträge saldieren."""
    _vorhanden(abrechnungsposten, 'abrechnungsposten')
    if not isinstance(abrechnungsposten, list) or len(abrechnungsposten) > 1000:
        _fehler('abrechnungsposten', 'Liste mit höchstens1000 überschneidungsfreien Abrechnungsposten erforderlich.')
    namen = set()
    kaeufer_soll, verkaeufer_soll = _bruch(0), _bruch(0)
    for p in abrechnungsposten:
        if not isinstance(p, dict) or set(p) != {'posten_id', 'postenart', 'zeitbezug', 'betrag', 'tatsaechliche_partei'}:
            _fehler('abrechnungsposten', 'Genau posten_id, postenart, zeitbezug, betrag, tatsaechliche_partei erforderlich.')
        name = _text(p['posten_id'], 'posten_id')
        if name in namen:
            _fehler('posten_id', 'Abrechnungsposten nicht doppelt erfassen.')
        namen.add(name)
        _auswahl(p['postenart'], 'postenart', ('nutzungen', 'gewoehnliche_lasten', 'schuldzinsen', 'erbschaftsabgaben', 'ausserordentliche_stammwertlasten', 'nachlassschuldtilgung'))
        _auswahl(p['zeitbezug'], 'zeitbezug', ('vor_kauf', 'ab_kauf'))
        _auswahl(p['tatsaechliche_partei'], 'tatsaechliche_partei', ('kaeufer', 'verkaeufer'))
        betrag = _geld(p['betrag'])
        besondere_last = p['postenart'] in ('erbschaftsabgaben', 'ausserordentliche_stammwertlasten', 'nachlassschuldtilgung')
        zustaendig = 'kaeufer' if besondere_last or p['zeitbezug'] == 'ab_kauf' else 'verkaeufer'
        tatsaechlich = p['tatsaechliche_partei']
        if tatsaechlich != zustaendig:
            schuldner = tatsaechlich if p['postenart'] == 'nutzungen' else zustaendig
            if schuldner == 'kaeufer':
                kaeufer_soll = _addieren(kaeufer_soll, betrag)
            else:
                verkaeufer_soll = _addieren(verkaeufer_soll, betrag)
    _wahrheitswert(gesetzliche_lastenverteilung_qualifiziert, 'gesetzliche_lastenverteilung_qualifiziert')
    _text(abrechnungsnachweis, 'abrechnungsnachweis')
    eingaben = dict(abrechnungsposten=abrechnungsposten,
        gesetzliche_lastenverteilung_qualifiziert=gesetzliche_lastenverteilung_qualifiziert, abrechnungsnachweis=abrechnungsnachweis)
    wert = None
    if gesetzliche_lastenverteilung_qualifiziert:
        wert = dict(rechnerischer_ausgleich_kaeufer_an_verkaeufer=_bruchteile(kaeufer_soll),
            rechnerischer_ausgleich_verkaeufer_an_kaeufer=_bruchteile(verkaeufer_soll),
            saldo_zugunsten_verkaeufer=_bruchteile(_subtrahieren(kaeufer_soll, verkaeufer_soll)))
    ergebnis = _ergebnis(wert, 'EUR', 'BGB_ERBSCHAFTSKAUF_ZAHLUNGSAUSGLEICH', eingaben,
        [dict(operation='Nutzungen/gewöhnliche Lasten/Zinsen vor Kauf Verkäufer, ab Kauf Käufer; besondere Käuferlasten zeitunabhängig; tatsächliche Empfänger/Zahler abgleichen und Gegenbeträge saldieren')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Wirksamer Erbschaftskauf mit gesetzlicher Lastenverteilung; vollständig vorqualifizierte zeitlich abgegrenzte, tatsächlich vereinnahmte/bezahlte Geldposten.']
    ergebnis['hinweise'] = ['Bei Nutzungen ist tatsächliche Partei der Empfänger, bei Lasten/Tilgungen der Zahler. Zeitbezug bezeichnet rechtlich zugeordnete Nutzungs-/Lastenperiode, nicht ungeprüft Zahlungstag. Regelmäßige Posten über Kaufstichtag vorher mit fruechte_lasten_betragszuordnung zeitanteilig aufteilen; Zinsen mit vorhandenem Zinskern bestimmen. Käufer trägt auch vor Kauf Erbschaftsabgaben und außerordentliche auf Stammwert gelegte Lasten2379; Tilgungen2378 nur bei rechtlich bestehender Käuferpflicht, nicht Verkäuferhaftung für Nichtbestehen2376. Vorverkaufstilgungen des Verkäufers sind damit Käufererstattung2378II. Eigene unberechtigte Zahlungen/gesonderte Ersatzregime nicht hineinmischen. Kaufpreis,2375-Wertminderung,2381-Verwendungen und Aufrechnungs-/Fälligkeitsvoraussetzungen separat. Signierter Saldo ist rechnerische Abrechnung, keine automatische Aufrechnung oder Anspruchsentstehung allein aufgrund Zahlung.']
    return ergebnis
