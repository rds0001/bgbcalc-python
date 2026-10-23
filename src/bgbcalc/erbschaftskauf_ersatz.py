"""Wertminderung und Verwendungsersatz beim Erbschaftskauf (§§2375,2381)."""
from .betraege import _geld, _wahrheitswert
from .kalender import _ergebnis, _text
from .zahlen import _addieren, _bruch, _subtrahieren
from .zinsen import _bruchteile


def erbschaftskauf_belastungswertminderung(wert_ohne_belastung=None, wert_mit_belastung=None,
    unentgeltliche_belastung_vor_kauf_qualifiziert=None, kaeufer_kennt_belastung_beim_kauf=None,
    bewertungsnachweis=None):
    """§2375 Absatz1: positive vergleichbare Wertdifferenz, bei Käuferkenntnis kein Ersatz."""
    ohne = _geld(wert_ohne_belastung)
    mit = _geld(wert_mit_belastung)
    _wahrheitswert(unentgeltliche_belastung_vor_kauf_qualifiziert, 'unentgeltliche_belastung_vor_kauf_qualifiziert')
    _wahrheitswert(kaeufer_kennt_belastung_beim_kauf, 'kaeufer_kennt_belastung_beim_kauf')
    _text(bewertungsnachweis, 'bewertungsnachweis')
    eingaben = dict(wert_ohne_belastung=wert_ohne_belastung, wert_mit_belastung=wert_mit_belastung,
        unentgeltliche_belastung_vor_kauf_qualifiziert=unentgeltliche_belastung_vor_kauf_qualifiziert,
        kaeufer_kennt_belastung_beim_kauf=kaeufer_kennt_belastung_beim_kauf, bewertungsnachweis=bewertungsnachweis)
    wert = None
    if unentgeltliche_belastung_vor_kauf_qualifiziert:
        minderung = max(_subtrahieren(ohne, mit), _bruch(0))
        wert = dict(wertminderung=_bruchteile(minderung),
            ersatzbetrag=_bruchteile(_bruch(0) if kaeufer_kennt_belastung_beim_kauf else minderung))
    ergebnis = _ergebnis(wert, 'EUR', 'BGB_ERBSCHAFTSKAUF_BELASTUNGSWERTMINDERUNG', eingaben,
        [dict(operation='Wert ohne minus Wert mit Belastung mindestens null; bei Käuferkenntnis bei Kauf kein Ersatz nach2375')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Feste lokale BGB-Fassung; Vergleichswerte derselben Sache und rechtlich desselben Bewertungszeitpunkts, isolierte Wirkung der unentgeltlichen Belastung vor Kauf.']
    ergebnis['hinweise'] = ['Nur unentgeltliche Belastung eines Erbschaftsgegenstands durch Verkäufer vor Erbschaftskauf nach§2375 Absatz1. Vergleichswerte nicht pauschal historische Vorher-/aktuelle Nachherpreise mit anderen Marktbewegungen. Kenntnisse bei Vertragsschluss rechtlich qualifizieren. Verbrauch oder vollständige unentgeltliche Veräußerung und andere Haftungsgrundlagen getrennt; deren bloße Wertvorgabe wäre keine eigene Differenzrechnung. Keine automatische Anwendung auf Schenkung der Erbschaft:§2385 Absatz2 enthält eigene Ausnahme. Wertminderung kann vorhanden sein, obwohl wegen Käuferkenntnis der2375-Ersatzbetrag null ist.']
    return ergebnis


def erbschaftskauf_verwendungsersatz(notwendige_verwendungen_vor_kauf=None,
    andere_aufwendungen_vor_kauf=None, fortbestehende_wertsteigerung_beim_kauf=None,
    aufwendungen_nach_2381_qualifiziert=None, bewertungsnachweis=None):
    """§2381: notwendige Verwendungen plus wertgedeckter Teil anderer Voraufwendungen."""
    notwendig = _geld(notwendige_verwendungen_vor_kauf)
    andere = _geld(andere_aufwendungen_vor_kauf)
    steigerung = _geld(fortbestehende_wertsteigerung_beim_kauf)
    _wahrheitswert(aufwendungen_nach_2381_qualifiziert, 'aufwendungen_nach_2381_qualifiziert')
    _text(bewertungsnachweis, 'bewertungsnachweis')
    eingaben = dict(notwendige_verwendungen_vor_kauf=notwendige_verwendungen_vor_kauf,
        andere_aufwendungen_vor_kauf=andere_aufwendungen_vor_kauf,
        fortbestehende_wertsteigerung_beim_kauf=fortbestehende_wertsteigerung_beim_kauf,
        aufwendungen_nach_2381_qualifiziert=aufwendungen_nach_2381_qualifiziert, bewertungsnachweis=bewertungsnachweis)
    wert = None
    if aufwendungen_nach_2381_qualifiziert:
        andere_ersatz = min(andere, steigerung)
        wert = dict(ersatz_notwendiger_verwendungen=_bruchteile(notwendig),
            ersatz_anderer_aufwendungen=_bruchteile(andere_ersatz),
            gesamter_verwendungsersatz=_bruchteile(_addieren(notwendig, andere_ersatz)))
    ergebnis = _ergebnis(wert, 'EUR', 'BGB_ERBSCHAFTSKAUF_VERWENDUNGSERSATZ', eingaben,
        [dict(operation='Notwendige Vorverwendungen voll; andere Voraufwendungen auf fortbestehende Wertsteigerung beim Kauf begrenzen und addieren')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Feste lokale BGB-Fassung; vom Verkäufer vor Kauf gemachte notwendige und andere Aufwendungen überschneidungsfrei getrennt.']
    ergebnis['hinweise'] = ['Nur§2381: Wertsteigerung gerade durch die anderen Aufwendungen und noch zur Zeit des Verkaufs vorhanden. Notwendige Verwendungen nicht zusätzlich nochmals in anderen Aufwendungen oder deren Wertdeckung zählen. Kein automatischer Ersatz nach Kauf entstandener Aufwendungen. Geldwerte rechtlich bestimmen, keine erfundene Bewertung. Tilgung von Nachlassverbindlichkeiten§2378 Absatz2 und zeitliche Lasten-/Nutzungszuordnung§§2379/2380 sowie sonstige Kaufabrechnung separat.']
    return ergebnis
