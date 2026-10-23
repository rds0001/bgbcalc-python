"""Erbrechtliche Betragsbegrenzungen: Doppelersatz vermeiden und Auflagenzweck deckeln."""
from .betraege import _geld, _wahrheitswert
from .kalender import _ergebnis, _fehler, _text
from .zahlen import _subtrahieren
from .zinsen import _bruchteile


def erbschaftsbesitzer_verwendungsrest(ersatzfaehige_verwendungen=None,
    bereits_durch_bereicherungsanrechnung_gedeckt=None, anspruch_nach_2022_qualifiziert=None,
    bewertungsnachweis=None):
    """§2022 Absatz1/2: bereits bereicherungsrechtlich gedeckten Aufwand nicht nochmals ersetzen."""
    aufwand = _geld(ersatzfaehige_verwendungen)
    gedeckt = _geld(bereits_durch_bereicherungsanrechnung_gedeckt)
    if gedeckt > aufwand:
        _fehler('bereits_durch_bereicherungsanrechnung_gedeckt', 'Bereits gedeckter Betrag darf die betrachteten Verwendungen nicht übersteigen.')
    _wahrheitswert(anspruch_nach_2022_qualifiziert, 'anspruch_nach_2022_qualifiziert')
    _text(bewertungsnachweis, 'bewertungsnachweis')
    eingaben = dict(ersatzfaehige_verwendungen=ersatzfaehige_verwendungen,
        bereits_durch_bereicherungsanrechnung_gedeckt=bereits_durch_bereicherungsanrechnung_gedeckt,
        anspruch_nach_2022_qualifiziert=anspruch_nach_2022_qualifiziert, bewertungsnachweis=bewertungsnachweis)
    wert = _bruchteile(_subtrahieren(aufwand, gedeckt)) if anspruch_nach_2022_qualifiziert else None
    ergebnis = _ergebnis(wert, 'EUR', 'BGB_ERBSCHAFTSBESITZER_VERWENDUNGSREST', eingaben,
        [dict(operation='Qualifizierte Verwendungen um den bereits durch Bereicherungsanrechnung gedeckten Teil vermindern')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Feste lokale BGB-Fassung; derselbe rechtlich bestimmte Aufwand und dessen bereits gedeckter Teil, keine doppelte Berücksichtigung.']
    ergebnis['hinweise'] = ['§2022 Absatz2 kann rechtlich qualifizierte Lasten-/Schuldentilgungsaufwendungen einschließen. Bereits gedeckt meint gerade Anrechnung auf die nach§2021 herauszugebende Bereicherung, nicht beliebige Zahlungen ohne Bezug. Weitergehender Ersatz nach§2022 Absatz3 und verschärfte Haftung§§2023–2025 sind separat zu prüfen. Zurückbehaltung sowie§§1000–1003 und Durchsetzbarkeit nicht automatisch entschieden. Keine Bewertung von Verwendungen oder Bereicherung erfunden.']
    return ergebnis


def erbauflage_herausgabebegrenzung(bereicherungsrechtlicher_zuwendungswert=None,
    zur_auflagenvollziehung_erforderlicher_zuwendungsanteil=None,
    herausgabevoraussetzungen_2196_erfuellt=None, bewertungsnachweis=None):
    """§2196: qualifizierten Herausgabewert auf zweckgebundenen Zuwendungsanteil begrenzen."""
    wert_zuwendung = _geld(bereicherungsrechtlicher_zuwendungswert)
    zweckanteil = _geld(zur_auflagenvollziehung_erforderlicher_zuwendungsanteil)
    _wahrheitswert(herausgabevoraussetzungen_2196_erfuellt, 'herausgabevoraussetzungen_2196_erfuellt')
    _text(bewertungsnachweis, 'bewertungsnachweis')
    eingaben = dict(bereicherungsrechtlicher_zuwendungswert=bereicherungsrechtlicher_zuwendungswert,
        zur_auflagenvollziehung_erforderlicher_zuwendungsanteil=zur_auflagenvollziehung_erforderlicher_zuwendungsanteil,
        herausgabevoraussetzungen_2196_erfuellt=herausgabevoraussetzungen_2196_erfuellt,
        bewertungsnachweis=bewertungsnachweis)
    wert = _bruchteile(min(wert_zuwendung, zweckanteil)) if herausgabevoraussetzungen_2196_erfuellt else None
    ergebnis = _ergebnis(wert, 'EUR', 'BGB_ERBAUFLAGE_HERAUSGABEBEGRENZUNG', eingaben,
        [dict(operation='Kleineren Betrag aus bereicherungsrechtlichem Zuwendungswert und auflagenzweckgebundenem Anteil bestimmen')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Feste lokale BGB-Fassung; wertmäßige Begrenzung einer rechtlich qualifizierten Herausgabe, keine automatische Umwandlung von Sachherausgabe in Geldzahlung.']
    ergebnis['hinweise'] = ['Qualifikation umfasst§2196 Absatz1 schuldhaft unmögliche Auflagenvollziehung oder Absatz2 rechtskräftige Vollziehungsverurteilung mit erfolglosen zulässigen Zwangsmitteln bei nicht durch Dritten vollziehbarer Auflage, sowie Berechtigung des vom Wegfall Begünstigten. Bloße Nichtvollziehung genügt nicht. Zweckspezifischer Anteil ist der Teil der Zuwendung, der hätte verwendet werden müssen, keine frei erfundene Pauschale. Bereicherungsrechtliche Bewertung einschließlich einschlägiger Einwendungen vorgeben. Kein automatischer Zahlungsanspruch, keine Frist-/Vollstreckungsprüfung.']
    return ergebnis
