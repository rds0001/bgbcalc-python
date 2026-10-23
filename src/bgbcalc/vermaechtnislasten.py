"""Verteilung derselben Vermächtnis-/Auflagenlast auf mehrere Beschwerte (§§2148/2192)."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _auswahl, _fehler, _text, _vorhanden
from .zahlen import _addieren, _bruch, _dividieren, _multiplizieren, _zahleneingabe
from .zinsen import _bruchteile


def vermaechtnis_lastenanteile(gesamtbelastung=None, beschwerte=None, beschwertenart=None,
    beschwerungsart=None, zweifelsregel_anwendbar=None, bewertungsnachweis=None):
    """Gewichten nach Erbteilen oder Vermächtniswerten im gesetzlich einschlägigen Zweifelsfall."""
    betrag = _geld(gesamtbelastung)
    _auswahl(beschwertenart, 'beschwertenart', ('erben', 'vermaechtnisnehmer'))
    _auswahl(beschwerungsart, 'beschwerungsart', ('vermaechtnis', 'auflage'))
    _vorhanden(beschwerte, 'beschwerte')
    if not isinstance(beschwerte, list) or not 2 <= len(beschwerte) <= 1000:
        _fehler('beschwerte', 'Liste mit 2 bis 1000 rechtlich bestimmten Beschwerten erforderlich.')
    namen, gewichte = [], []
    summe = _bruch(0)
    for eintrag in beschwerte:
        if not isinstance(eintrag, dict) or set(eintrag) != {'beschwerter_id', 'gewicht'}:
            _fehler('beschwerte', 'Genau beschwerter_id und gewicht erforderlich.')
        name = _text(eintrag['beschwerter_id'], 'beschwerter_id')
        if name in namen:
            _fehler('beschwerter_id', 'Beschwerte dürfen nicht doppelt vorkommen.')
        gewicht = _zahleneingabe(eintrag['gewicht'])
        if gewicht < 0 or (beschwertenart == 'erben' and not 0 < gewicht <= 1):
            _fehler('gewicht', 'Erbteile müssen positiv und höchstens eins, Vermächtniswerte nichtnegativ sein.')
        summe = _addieren(summe, gewicht)
        namen.append(name)
        gewichte.append(gewicht)
    if summe == 0 or (beschwertenart == 'erben' and summe > 1):
        _fehler('beschwerte', 'Positive Gewichtssumme erforderlich; Summe tatsächlicher Erbteile darf eins nicht übersteigen.')
    _wahrheitswert(zweifelsregel_anwendbar, 'zweifelsregel_anwendbar')
    _text(bewertungsnachweis, 'bewertungsnachweis')
    eingaben = dict(gesamtbelastung=gesamtbelastung, beschwerte=beschwerte,
        beschwertenart=beschwertenart, beschwerungsart=beschwerungsart,
        zweifelsregel_anwendbar=zweifelsregel_anwendbar, bewertungsnachweis=bewertungsnachweis)
    ergebnis = _geld_ergebnis(None, 'BGB_VERMAECHTNIS_LASTENANTEILE', eingaben,
        [dict(operation='Dieselbe Gesamtlast unter den Beschwerten proportional zu deren Erbteilen oder Vermächtniswerten verteilen')])
    if zweifelsregel_anwendbar:
        anteile = [_dividieren(g, summe) for g in gewichte]
        ergebnis['wert'] = [dict(beschwerter_id=n, lastquote=_bruchteile(q),
            lastbetrag=_bruchteile(_multiplizieren(betrag, q))) for n, q in zip(namen, anteile)]
        ergebnis['status'] = 'BERECHNET'
    ergebnis['hinweise'].append('§2148 ist Zweifelsregel, über§2192 auch für Auflagen. Abweichender Erblasserwille und tatsächliche Beschwerung vorab bestimmen. Nur die mit derselben Last beschwerten Personen einbeziehen; bei Erben dürfen deren tatsächliche Erbteile zusammen unter1 liegen, wenn andere Erben nicht beschwert sind. Dann innerhalb dieser Auswahl normieren. Erben und Vermächtnisnehmer nicht in einer ungeklärten gemischten Gruppe verrechnen. Gewichte bei Erben sind Erbquoten, bei Vermächtnisnehmern konsistent bewertete Vermächtniswerte; kein pauschales Kopfteilprinzip. Nullwerte bei Vermächtnissen führen zu Nullanteilen, ausschließlich Nullwerte liefern kein bestimmbares Verhältnis. Ergebnis verteilt eine qualifizierte EUR-Last, entscheidet aber nicht über Gegenstandsübertragung, Außenhaftung, Erfüllbarkeit oder weitere Kürzungsrechte.')
    return ergebnis
