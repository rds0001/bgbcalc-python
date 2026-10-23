"""Numerische Teilmodelle der Erbauseinandersetzung (§§2046,2047,2050)."""
from .betraege import _geld, _wahrheitswert
from .kalender import _ergebnis, _fehler, _ganzzahl, _text
from .zahlen import GRENZE, _bruch, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile


def erbnachlass_ueberschussanteil(nachlasswert=None, gemeinsame_verbindlichkeiten=None,
    erforderlicher_rueckbehalt=None, erbquote_zaehler=None, erbquote_nenner=None,
    einfaches_teilungsmodell_qualifiziert=None, bewertungsnachweis=None):
    """Gemeinsame Lasten/Reserve abziehen und positiven Überschuss mit einer Erbquote multiplizieren."""
    nachlass = _geld(nachlasswert)
    lasten = _geld(gemeinsame_verbindlichkeiten)
    reserve = _geld(erforderlicher_rueckbehalt)
    z = _ganzzahl(erbquote_zaehler, 'erbquote_zaehler', 0, GRENZE)
    n = _ganzzahl(erbquote_nenner, 'erbquote_nenner', 1, GRENZE)
    if z > n:
        _fehler('erbquote', 'Erbquote darf eins nicht übersteigen.')
    _wahrheitswert(einfaches_teilungsmodell_qualifiziert, 'einfaches_teilungsmodell_qualifiziert')
    _text(bewertungsnachweis, 'bewertungsnachweis')
    eingaben = dict(nachlasswert=nachlasswert, gemeinsame_verbindlichkeiten=gemeinsame_verbindlichkeiten,
        erforderlicher_rueckbehalt=erforderlicher_rueckbehalt, erbquote_zaehler=erbquote_zaehler, erbquote_nenner=erbquote_nenner,
        einfaches_teilungsmodell_qualifiziert=einfaches_teilungsmodell_qualifiziert, bewertungsnachweis=bewertungsnachweis)
    wert = None
    if einfaches_teilungsmodell_qualifiziert:
        rest = _subtrahieren(_subtrahieren(nachlass, lasten), reserve)
        ueberschuss = max(rest, _bruch(0))
        wert = dict(nettobetrag_nach_lasten_und_reserve=_bruchteile(rest), verteilbarer_ueberschuss=_bruchteile(ueberschuss),
            anteil_am_ueberschuss=_bruchteile(_multiplizieren(ueberschuss, _bruch(z, n))))
    ergebnis = _ergebnis(wert, 'EUR', 'BGB_ERBNACHLASS_UEBERSCHUSSANTEIL', eingaben,
        [dict(operation='Gemeinsame Lasten und getrennte erforderliche Reserve abziehen; positiven Rest nach Erbquote anteilig berechnen')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Vollständig qualifizierte und überschneidungsfreie gemeinsame Lasten/Reserve; einfaches Teilungsmodell ohne Ausgleichung oder abweichende Teilungsanordnung.']
    ergebnis['hinweise'] = ['Nachlasswert vor den eingegebenen Abzügen; bereits daraus bezahlte Lasten nicht erneut abziehen. Reserve für noch nicht fällige/streitige Verbindlichkeiten rechtlich bewerten und nicht zugleich als gemeinsame Verbindlichkeit erfassen. Nur einigen Erben zur Last fallende Verbindlichkeiten2046II nicht von gemeinsamer Masse abziehen; deren Anteil und Deckung separat. Negativer Nettobetrag ist kein negativer Verteilungsanspruch und keine Insolvenzfeststellung. Keine Auszahlungserlaubnis, kein vollständiger Teilungsplan, keine Verwertung in Geld oder Verteilung gemeinschaftlicher Schriftstücke2047II.']
    return ergebnis


def ausgleichung_zuschuss_mehrbetrag(zuwendungswert=None, angemessenes_mass=None,
    zuwendung_nach_2050_abs2_qualifiziert=None, bewertungsnachweis=None):
    """Übermäßigen Anteil qualifizierter Einkünftezuschüsse/Berufsvorbildungskosten berechnen."""
    wert_z = _geld(zuwendungswert)
    mass = _geld(angemessenes_mass)
    _wahrheitswert(zuwendung_nach_2050_abs2_qualifiziert, 'zuwendung_nach_2050_abs2_qualifiziert')
    _text(bewertungsnachweis, 'bewertungsnachweis')
    eingaben = dict(zuwendungswert=zuwendungswert, angemessenes_mass=angemessenes_mass,
        zuwendung_nach_2050_abs2_qualifiziert=zuwendung_nach_2050_abs2_qualifiziert, bewertungsnachweis=bewertungsnachweis)
    wert = _bruchteile(max(_subtrahieren(wert_z, mass), _bruch(0))) if zuwendung_nach_2050_abs2_qualifiziert else None
    ergebnis = _ergebnis(wert, 'EUR', 'BGB_AUSGLEICHUNG_ZUSCHUSS_MEHRBETRAG', eingaben,
        [dict(operation='Qualifizierter Zuwendungswert minus vermögensangemessenes Maß, mindestens null')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Rechtlich qualifizierter Ausgleichungsfall2050II; Zuwendung und angemessenes Maß auf vergleichbarer Wertgrundlage.']
    ergebnis['hinweise'] = ['Angemessenes Maß nach damaligen Vermögensverhältnissen des Erblassers vorgeben; keine feste gesetzliche Prozentgrenze erfinden. Zuschüsse zur Verwendung als Einkünfte und Berufsvorbildungskosten rechtlich abgrenzen. Ergebnis ist ausgleichungsrelevanter Mehrbetrag vor weiterer Bewertung/Ausgleichungsrechnung2055/2056, kein sofortiger Rückzahlungsanspruch. Keine automatische Zusammenfassung verschiedener Lebensabschnitte oder Zuwendungen.']
    return ergebnis
