"""Betragsgrenzen bei Untervermächtnissen und Auflagen (§§2187/2188)."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _auswahl, _fehler, _text
from .zahlen import _bruch, _dividieren, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile


def untervermaechtnis_verweigerungsbetrag(erhaltener_vermaechtniswert=None,
    erforderlicher_erfuellungswert=None, beschwerter_vermaechtnisnehmer=None, bewertungsnachweis=None):
    """§2187 Absatz1: positiver Fehlbetrag der Beschwerung gegenüber erhaltenem Vermächtnis."""
    erhalten = _geld(erhaltener_vermaechtniswert)
    erforderlich = _geld(erforderlicher_erfuellungswert)
    _wahrheitswert(beschwerter_vermaechtnisnehmer, 'beschwerter_vermaechtnisnehmer')
    _text(bewertungsnachweis, 'bewertungsnachweis')
    eingaben = dict(erhaltener_vermaechtniswert=erhaltener_vermaechtniswert,
        erforderlicher_erfuellungswert=erforderlicher_erfuellungswert,
        beschwerter_vermaechtnisnehmer=beschwerter_vermaechtnisnehmer, bewertungsnachweis=bewertungsnachweis)
    wert = max(_bruch(0), _subtrahieren(erforderlich, erhalten)) if beschwerter_vermaechtnisnehmer else None
    ergebnis = _geld_ergebnis(wert, 'BGB_UNTERVERMAECHTNIS_VERWEIGERUNGSBETRAG', eingaben,
        [dict(operation='Erforderlichen Erfüllungswert abzüglich erhaltenem Vermächtniswert auf mindestens null begrenzen')])
    ergebnis['hinweise'].append('Nur betragsmäßiger Umfang des Verweigerungsrechts§2187 Absatz1, auch nach Annahme. Tatsächlich aus Vermächtnis Erhaltenes konsistent bewerten, nicht ungeprüft ungekürzten Nominalanspruch einsetzen. Berechnung übt das Recht nicht aus und ordnet keine automatische Schuldtilgung an. Fälligkeit§2186, Nachrücken§2161/2187 Absatz2 und entsprechende Haftungsregeln§1992/2187 Absatz3 gesondert; bei mehreren Beschwerungen keine unzulässige Einzelverwendung desselben Deckungswerts oder erfundene Rangfolge.')
    return ergebnis


def vermaechtnis_beschwerungskuerzung(ungekuerzter_vermaechtniswert=None,
    verbleibender_vermaechtniswert=None, urspruengliche_beschwerung=None, kuerzungsgrund=None,
    abweichender_erblasserwille=None, beschwerungsregel_anwendbar=None, bewertungsnachweis=None):
    """§2188: Beschwerung proportional zur qualifizierten Kürzung des Vermächtnisses."""
    vorher = _geld(ungekuerzter_vermaechtniswert)
    nachher = _geld(verbleibender_vermaechtniswert)
    belastung = _geld(urspruengliche_beschwerung)
    if vorher == 0:
        _fehler('ungekuerzter_vermaechtniswert', 'Positive ursprüngliche Leistung für Verhältnisrechnung erforderlich.')
    if nachher > vorher:
        _fehler('verbleibender_vermaechtniswert', 'Verbleibende Leistung darf ursprüngliche Leistung nicht übersteigen.')
    _auswahl(kuerzungsgrund, 'kuerzungsgrund', ('erbenhaftungsbeschraenkung', 'pflichtteilsanspruch', 'untervermaechtnis_2187'))
    _wahrheitswert(abweichender_erblasserwille, 'abweichender_erblasserwille')
    _wahrheitswert(beschwerungsregel_anwendbar, 'beschwerungsregel_anwendbar')
    _text(bewertungsnachweis, 'bewertungsnachweis')
    eingaben = dict(ungekuerzter_vermaechtniswert=ungekuerzter_vermaechtniswert,
        verbleibender_vermaechtniswert=verbleibender_vermaechtniswert,
        urspruengliche_beschwerung=urspruengliche_beschwerung, kuerzungsgrund=kuerzungsgrund,
        abweichender_erblasserwille=abweichender_erblasserwille,
        beschwerungsregel_anwendbar=beschwerungsregel_anwendbar, bewertungsnachweis=bewertungsnachweis)
    ergebnis = _geld_ergebnis(None, 'BGB_VERMAECHTNIS_BESCHWERUNGSKUERZUNG', eingaben,
        [dict(operation='Beschwerung mit Verhältnis verbleibender zu ungekürzter Vermächtnisleistung multiplizieren')])
    if beschwerungsregel_anwendbar and not abweichender_erblasserwille:
        faktor = _dividieren(nachher, vorher)
        verbleibend = _multiplizieren(belastung, faktor)
        ergebnis['wert'] = dict(verbleibensquote=_bruchteile(faktor),
            gekuerzte_beschwerung=_bruchteile(verbleibend),
            kuerzungsbetrag=_bruchteile(_subtrahieren(belastung, verbleibend)))
        ergebnis['status'] = 'BERECHNET'
    ergebnis['hinweise'].append('Nur Kürzung aufgrund der drei gesetzlichen Gründe, rechtlich wirksam vorgegeben. Freiwillige Zahlung, Marktwertschwankung oder beliebiger Forderungsverzicht allein genügt nicht. Abweichender Erblasserwille schließt dieses proportionale Modell aus. Ursprünglichen Vermächtniswert und ursprüngliche Beschwerung als gemeinsame unveränderte Basis verwenden; bereits gekürzte Beschwerung nicht nochmals mit kumulierter Quote kürzen. Geldwerte müssen dieselbe Leistung und Bewertungsbasis abbilden. Ergebnis bezeichnet zulässige Kürzung bei Ausübung des Rechts, keine automatische Änderung oder Durchsetzbarkeit der Beschwerung. Andere Ansprüche und Rangfragen gesondert.')
    return ergebnis
