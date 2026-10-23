"""Numerische Pflichtteilslastgrenzen (§§2319–2322)."""
from .betraege import _geld, _wahrheitswert
from .kalender import _auswahl, _ergebnis, _fehler, _text
from .zahlen import _addieren, _bruch, _subtrahieren
from .zinsen import _bruchteile


def _last_ergebnis(wert, regel, eingaben, operation, hinweis):
    ergebnis = _ergebnis(wert, 'EUR', regel, eingaben, [dict(operation=operation)], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Feste lokale BGB-Fassung; Beträge und Anwendungsfall rechtlich qualifiziert; isolierte numerische Lastgrenze.']
    ergebnis['hinweise'] = [hinweis]
    return ergebnis


def pflichtteil_miterbe_eigenbedarf(erbteilwert_nach_teilung=None, eigener_pflichtteilswert=None,
    verlangter_pflichtteilsbetrag=None, schutz_nach_2319_qualifiziert=None, bewertungsnachweis=None):
    """Nach Teilung eigenen Pflichtteil schützen, verbleibende Forderungsdeckung und Ausfall berechnen."""
    erbteil = _geld(erbteilwert_nach_teilung)
    eigen = _geld(eigener_pflichtteilswert)
    verlangt = _geld(verlangter_pflichtteilsbetrag)
    _wahrheitswert(schutz_nach_2319_qualifiziert, 'schutz_nach_2319_qualifiziert')
    _text(bewertungsnachweis, 'bewertungsnachweis')
    eingaben = dict(erbteilwert_nach_teilung=erbteilwert_nach_teilung, eigener_pflichtteilswert=eigener_pflichtteilswert,
        verlangter_pflichtteilsbetrag=verlangter_pflichtteilsbetrag, schutz_nach_2319_qualifiziert=schutz_nach_2319_qualifiziert,
        bewertungsnachweis=bewertungsnachweis)
    wert = None
    if schutz_nach_2319_qualifiziert:
        deckung = min(verlangt, max(_subtrahieren(erbteil, eigen), _bruch(0)))
        wert = dict(befriedigungsbetrag=_bruchteile(deckung), ausfall_fuer_uebrige_erben=_bruchteile(_subtrahieren(verlangt, deckung)))
    return _last_ergebnis(wert, 'BGB_PFLICHTTEIL_MITERBE_EIGENBEDARF', eingaben,
        'Verlangten Pflichtteil auf positiven Erbteilüberschuss über eigenen Pflichtteil begrenzen; Differenz als Ausfall',
        'Nur pflichtteilsberechtigter Miterbe nach Teilung2319. Erbteilwert und noch zu tragende Pflichtteilslast auf konsistenter Basis, bereits gezahlte Lasten nicht doppelt abziehen. Ausfall trifft übrige Erben, hier keine unbelegte interne Quote oder Rangverteilung. Kein Schutz des gesamten ursprünglichen Erwerbs vor sonstigen Verbindlichkeiten und keine Erhöhung des Erbteils auf eigenen Pflichtteil.')


def pflichtteil_vorteilslast(fallart=None, pflichtteilslast=None, angenommenes_vermaechtnis=None,
    erlangter_vorteil=None, lastzuordnung_qualifiziert=None, bewertungsnachweis=None):
    """Interne Sonderlast nach2320/2321 auf den erlangten Vorteil begrenzen."""
    _auswahl(fallart, 'fallart', ('ersatzerwerb_2320', 'vermaechtnisausschlagung_2321'))
    pflicht = _geld(pflichtteilslast)
    vermaechtnis = _geld(angenommenes_vermaechtnis)
    vorteil = _geld(erlangter_vorteil)
    if fallart == 'vermaechtnisausschlagung_2321' and vermaechtnis != 0:
        _fehler('angenommenes_vermaechtnis', 'Bei ausgeschlagenem Vermächtnis2321 ist angenommener Vermächtniswert null.')
    _wahrheitswert(lastzuordnung_qualifiziert, 'lastzuordnung_qualifiziert')
    _text(bewertungsnachweis, 'bewertungsnachweis')
    eingaben = dict(fallart=fallart, pflichtteilslast=pflichtteilslast, angenommenes_vermaechtnis=angenommenes_vermaechtnis,
        erlangter_vorteil=erlangter_vorteil, lastzuordnung_qualifiziert=lastzuordnung_qualifiziert, bewertungsnachweis=bewertungsnachweis)
    wert = None
    if lastzuordnung_qualifiziert:
        gesamt = _addieren(pflicht, vermaechtnis)
        last = min(gesamt, vorteil)
        wert = dict(zugeordnete_sonderlast=_bruchteile(last), nicht_durch_vorteil_zugeordnete_restlast=_bruchteile(_subtrahieren(gesamt, last)))
    return _last_ergebnis(wert, 'BGB_PFLICHTTEIL_VORTEILSLAST', eingaben,
        'Qualifizierte Pflichtteilslast und gegebenenfalls angenommenen Vermächtniswert addieren; interne Sonderlast auf Vorteil begrenzen',
        '2320: gesetzlicher Ersatzerwerb oder rechtlich entsprechend ausgelegte testamentarische Zuwendung;2321: Begünstigter der Vermächtnisausschlagung. Erlangten Vorteil rechtlich bewerten, nicht automatisch vollen Erbteil einsetzen. Pflichtteilslast und angenommenes Vermächtnis dürfen nicht denselben Anspruchsteil doppelt enthalten:2317/2307-Anrechnung vorher berücksichtigen. Restlast ist nur nicht durch diese Sonderzuordnung gedeckt, keine Feststellung einer konkreten Haftungsquote anderer Erben. Keine Doppelbelastung bei mehreren Begünstigten oder automatische2324-Testamentsauslegung.')


def pflichtteil_deckung_beschwerungskuerzung(erwerbswert_vor_beschwerung=None, beschwerungswert=None,
    zu_deckende_pflichtteilslast=None, kuerzung_nach_2322_qualifiziert=None, bewertungsnachweis=None):
    """Beschwerung eines durch Ausschlagung begünstigten Erwerbs zur Pflichtteilsdeckung kürzen."""
    erwerb = _geld(erwerbswert_vor_beschwerung)
    beschwerung = _geld(beschwerungswert)
    pflicht = _geld(zu_deckende_pflichtteilslast)
    if beschwerung > erwerb:
        _fehler('beschwerungswert', 'Beschwerungen oberhalb Erwerbswert benötigen vorgelagerte andere Kürzungsregeln; außerhalb dieses isolierten Modells.')
    _wahrheitswert(kuerzung_nach_2322_qualifiziert, 'kuerzung_nach_2322_qualifiziert')
    _text(bewertungsnachweis, 'bewertungsnachweis')
    eingaben = dict(erwerbswert_vor_beschwerung=erwerbswert_vor_beschwerung, beschwerungswert=beschwerungswert,
        zu_deckende_pflichtteilslast=zu_deckende_pflichtteilslast, kuerzung_nach_2322_qualifiziert=kuerzung_nach_2322_qualifiziert,
        bewertungsnachweis=bewertungsnachweis)
    wert = None
    if kuerzung_nach_2322_qualifiziert:
        frei = _subtrahieren(erwerb, beschwerung)
        kuerzung = min(beschwerung, max(_subtrahieren(pflicht, frei), _bruch(0)))
        deckung = _addieren(frei, kuerzung)
        wert = dict(kuerzungsbetrag=_bruchteile(kuerzung), verbleibende_beschwerung=_bruchteile(_subtrahieren(beschwerung, kuerzung)),
            nicht_gedeckte_pflichtteilslast=_bruchteile(max(_subtrahieren(pflicht, deckung), _bruch(0))))
    return _last_ergebnis(wert, 'BGB_PFLICHTTEIL_DECKUNG_BESCHWERUNGSKUERZUNG', eingaben,
        'Freien Erwerbsrest vor Kürzung ermitteln; Deckungslücke bis zum Beschwerungswert kürzen; Restbeschwerung und ungedeckte Pflichtteilslast ausweisen',
        'Nur Begünstigter der Ausschlagung einer beschwerten Erbschaft oder eines beschwerten Vermächtnisses2322. Erwerbswert vor gerade dieser Beschwerung und rechtlich zugeordnete Pflichtteilslast qualifizieren. Beschwerungen höchstens Erwerbswert, andernfalls vorgelagerte Haftungs-/Kürzungsregeln klären. Beschwerungswert kann Gesamtblock sein; keine Verteilung auf mehrere Vermächtnisse/Auflagen oder Missachtung eines Vorrangs2189. Keine automatische Geldzahlungspflicht aus Sachvermächtnis. Ungedeckte Last nicht als erloschen ansehen.')
