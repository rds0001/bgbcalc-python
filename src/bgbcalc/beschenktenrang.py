"""Nachrang früher Beschenkter bei Pflichtteilsergänzung (§2329 Absatz3)."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _fehler, _ganzzahl, _text, _vorhanden
from .zahlen import _bruch, _subtrahieren
from .zinsen import _bruchteile


def pflichtteilsergaenzung_beschenktenrang(fehlbetrag=None, beschenkte=None,
    beschenktenhaftung_2329_anwendbar=None, einordnungsnachweis=None):
    """Ergänzungsfehlbetrag zuerst später Beschenkten bis zur qualifizierten Haftungsgrenze zuordnen."""
    rest = _geld(fehlbetrag)
    _vorhanden(beschenkte, 'beschenkte')
    if not isinstance(beschenkte, list) or not 1 <= len(beschenkte) <= 1000:
        _fehler('beschenkte', 'Liste mit 1 bis 1000 unterschiedlich beschenkten Personen und eindeutigen Schenkungsrängen erforderlich.')
    namen, raenge, grenzen = [], [], []
    for eintrag in beschenkte:
        if not isinstance(eintrag, dict) or set(eintrag) != {'beschenkter_id', 'schenkungsrang', 'haftungsgrenze'}:
            _fehler('beschenkte', 'Genau beschenkter_id, schenkungsrang und haftungsgrenze erforderlich.')
        name = _text(eintrag['beschenkter_id'], 'beschenkter_id')
        rang = _ganzzahl(eintrag['schenkungsrang'], 'schenkungsrang', 1, 1000)
        grenze = _geld(eintrag['haftungsgrenze'])
        if name in namen:
            _fehler('beschenkter_id', 'Jede Person nur einmal; wiederholte Schenkungen an dieselbe Person außerhalb dieses Modells.')
        if rang in raenge:
            _fehler('schenkungsrang', 'Zeitliche Reihenfolge muss eindeutig sein; gleichrangige oder ungeklärte Schenkungen außerhalb dieses Modells.')
        namen.append(name)
        raenge.append(rang)
        grenzen.append(grenze)
    _wahrheitswert(beschenktenhaftung_2329_anwendbar, 'beschenktenhaftung_2329_anwendbar')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    eingaben = dict(fehlbetrag=fehlbetrag, beschenkte=beschenkte,
        beschenktenhaftung_2329_anwendbar=beschenktenhaftung_2329_anwendbar,
        einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(None, 'BGB_PFLICHTTEILSERGAENZUNG_BESCHENKTENRANG', eingaben,
        [dict(operation='Später Beschenkte vor früher Beschenkten bis zur jeweiligen rechtlich bestimmten Haftungsgrenze berücksichtigen')])
    if beschenktenhaftung_2329_anwendbar:
        zugeordnet = [_bruch(0)] * len(namen)
        for index in sorted(range(len(namen)), key=lambda i: raenge[i], reverse=True):
            zugeordnet[index] = min(rest, grenzen[index])
            rest = _subtrahieren(rest, zugeordnet[index])
        ergebnis['wert'] = dict(zugeordnete_haftung=[dict(beschenkter_id=n, haftungsbetrag=_bruchteile(b))
            for n, b in zip(namen, zugeordnet)], nicht_gedeckter_fehlbetrag=_bruchteile(rest))
        ergebnis['status'] = 'BERECHNET'
    ergebnis['hinweise'].append('Fehlbetrag nur soweit Erbe rechtlich nicht zur Ergänzung verpflichtet ist oder privilegierter Alleinerbenfall§2329 Absatz1 vorliegt; bloße Nichtzahlung oder Zahlungsunfähigkeit ersetzt diese Prüfung nicht. Haftungsgrenzen je Schenkung nach Bereicherungsrecht und sonstigen Einwendungen bereits rechtlich bestimmen, nicht ungeprüft damaligen Geschenkewert verwenden. Höherer Schenkungsrang bedeutet später beschenkt; nicht Eingabereihenfolge, Fälligkeitsdatum oder Zeitpunkt einer Zahlungsaufforderung. Früher Beschenkter haftet nur soweit später Beschenkter nicht verpflichtet ist, nicht bloß solange dieser nicht zahlt. Modell für unterschiedliche Personen mit je einer zeitlich eindeutig geordneten Schenkung; Gleichzeitigkeit, mehrere Schenkungen derselben Person und fehlende Ranginformationen gesondert lösen. Geldwerte begrenzen eine Herausgabe zum Befriedigungszweck; keine automatische Umwandlung des Sachherausgabeanspruchs in gewöhnliche Geldschuld. Abwendung durch Zahlung§2329 Absatz2 und tatsächliche Erfüllung separat; keine doppelte Befriedigung.')
    return ergebnis
