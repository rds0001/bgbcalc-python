"""Wertgrenzen bei übermäßiger/ordnungswidriger Fruchtziehung (§2133)."""
from .betraege import _geld, _wahrheitswert
from .kalender import _ergebnis, _fehler, _text
from .zahlen import _subtrahieren
from .zinsen import _bruchteile


def vorerbe_fruchtwertgrenze(fruchtwert=None, beeintraechtigte_eigene_nutzungen=None,
    wiederherstellungsgebundener_fruchtwert=None, fruchtziehung_nach_2133_qualifiziert=None,
    bewertungsnachweis=None):
    """Wiederherstellungsgebundenen Fruchtwert abziehen; Rest auf beeinträchtigte eigene Nutzungen begrenzen."""
    fruechte = _geld(fruchtwert)
    nutzungen = _geld(beeintraechtigte_eigene_nutzungen)
    gebunden = _geld(wiederherstellungsgebundener_fruchtwert)
    if gebunden > fruechte:
        _fehler('wiederherstellungsgebundener_fruchtwert', 'Gebundener Anteil des Fruchtwerts darf gesamten Fruchtwert nicht übersteigen; nicht ungeprüft gesamte Wiederherstellungskosten einsetzen.')
    _wahrheitswert(fruchtziehung_nach_2133_qualifiziert, 'fruchtziehung_nach_2133_qualifiziert')
    _text(bewertungsnachweis, 'bewertungsnachweis')
    eingaben = dict(fruchtwert=fruchtwert, beeintraechtigte_eigene_nutzungen=beeintraechtigte_eigene_nutzungen,
        wiederherstellungsgebundener_fruchtwert=wiederherstellungsgebundener_fruchtwert,
        fruchtziehung_nach_2133_qualifiziert=fruchtziehung_nach_2133_qualifiziert, bewertungsnachweis=bewertungsnachweis)
    wert = None
    if fruchtziehung_nach_2133_qualifiziert:
        frei = _subtrahieren(fruechte, gebunden)
        eigen = min(frei, nutzungen)
        wert = dict(nicht_wiederherstellungsgebundener_fruchtwert=_bruchteile(frei), dem_vorerben_gebuehrender_fruchtwert=_bruchteile(eigen),
            dem_vorerben_nicht_gebuehrender_fruchtwert=_bruchteile(_subtrahieren(fruechte, eigen)))
    ergebnis = _ergebnis(wert, 'EUR', 'BGB_VORERBE_FRUCHTWERTGRENZE', eingaben,
        [dict(operation='Wiederherstellungsgebundenen Anteil vom Fruchtwert abziehen; freien Rest auf Wert beeinträchtigter eigener Nutzungen begrenzen')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Ordnungswidrige Fruchtziehung oder infolge besonderen Ereignisses notwendiger Übermaßbezug rechtlich qualifiziert; vergleichbare getrennte Wertansätze.']
    ergebnis['hinweise'] = ['Beeinträchtigte eigene Nutzungen sind nur dem Vorerben zustehende Nutzungen, deren Wert gerade durch diesen Fruchtbezug beeinträchtigt wird; kein beliebiger Gesamtschaden. Wiederherstellungsgebundener Fruchtwert ist der nach ordnungsmäßiger Wirtschaft dafür einzusetzende Anteil dieses Fruchtwerts, nicht ungeprüft volle Reparaturkosten. Zwei Grenzen: keine Zuteilung gebundenen Fruchtwerts; übrige Zuteilung höchstens eigene Nutzungsbeeinträchtigung. Nutzungsbeeinträchtigung nicht vorab um denselben gebundenen Betrag kürzen. Nicht dem Vorerben gebührender Wert ist nicht automatisch sofortiger Geldzahlungsanspruch des Nacherben. Keine automatische Bewertung von Bewirtschaftung, Schäden oder Wiederherstellungsbedarf.']
    return ergebnis
