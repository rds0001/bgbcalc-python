"""Kauf-, Wiederkauf- und Vorkauf-Sonderbeträge mit qualifizierten Werten."""
from .betraege import _geld, _geld_ergebnis
from .kalender import _text, _fehler
from .zahlen import _addieren, _subtrahieren, _multiplizieren, _dividieren, _bruch


def neuverkauf_kosten_und_mindererloes(urspruenglicher_verkaufspreis=None, neuer_verkaufspreis=None, kosten_neuverkauf=None, einordnungsnachweis=None):
    """Kosten des neuen Verkaufs plus positiver Mindererlös gegenüber ursprünglichem Verkauf."""
    werte = [_geld(urspruenglicher_verkaufspreis), _geld(neuer_verkaufspreis), _geld(kosten_neuverkauf)]
    _text(einordnungsnachweis, 'einordnungsnachweis')
    eingaben = dict(urspruenglicher_verkaufspreis=urspruenglicher_verkaufspreis, neuer_verkaufspreis=neuer_verkaufspreis, kosten_neuverkauf=kosten_neuverkauf, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(_addieren(werte[2], max(_subtrahieren(werte[0], werte[1]), _bruch(0))), 'BGB_NEUVERKAUF_KOSTEN_UND_MINDERERLOES', eingaben, [dict(operation='Kosten des neuen Verkaufs plus positiver Mindererlös gegenüber ursprünglichem Verkauf')])
    ergebnis['hinweise'].append('Nur§451 Absatz2 nach qualifizierter Genehmigungsverweigerung und dadurch veranlasstem Neuverkauf. Mehrerlös wird nicht gegen Neuverkaufskosten aufgerechnet; kein automatischer Gesamtschadensersatz.')
    return ergebnis


def wiederkauf_verwendungsersatz(verwendungsaufwand=None, bewirkte_werterhoehung=None, einordnungsnachweis=None):
    """Qualifizierten Verwendungsaufwand auf dadurch bewirkte Werterhöhung begrenzen."""
    werte = [_geld(verwendungsaufwand), _geld(bewirkte_werterhoehung)]
    _text(einordnungsnachweis, 'einordnungsnachweis')
    eingaben = dict(verwendungsaufwand=verwendungsaufwand, bewirkte_werterhoehung=bewirkte_werterhoehung, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(min(werte), 'BGB_WIEDERKAUF_VERWENDUNGSERSATZ', eingaben, [dict(operation='Qualifizierten Verwendungsaufwand auf dadurch bewirkte Werterhöhung begrenzen')])
    ergebnis['hinweise'].append('Nur§459 Verwendungen vor Wiederkauf; keine Schätzungswertvereinbarung nach§460, die diesen Anspruch ausschließt. Kausale Werterhöhung extern bewerten; Wegnahmerecht und weitere Kosten gesondert.')
    return ergebnis


def vorkauf_preis_mit_nebenleistungswert(kaufpreis=None, zu_ersetzender_nebenleistungswert=None, einordnungsnachweis=None):
    """Kaufpreis um qualifizierten Geldwert der nicht selbst erfüllbaren Nebenleistung erhöhen."""
    werte = [_geld(kaufpreis), _geld(zu_ersetzender_nebenleistungswert)]
    _text(einordnungsnachweis, 'einordnungsnachweis')
    eingaben = dict(kaufpreis=kaufpreis, zu_ersetzender_nebenleistungswert=zu_ersetzender_nebenleistungswert, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(_addieren(werte[0],werte[1]), 'BGB_VORKAUF_PREIS_MIT_NEBENLEISTUNGSWERT', eingaben, [dict(operation='Kaufpreis um qualifizierten Geldwert der nicht selbst erfüllbaren Nebenleistung erhöhen')])
    ergebnis['hinweise'].append('Nur§466 monetär schätzbare und rechtlich zu ersetzende Nebenleistung, die Vorkaufsberechtigter nicht selbst bewirken kann. Keine Wertbestimmung und kein Wert einer nach§466 unbeachtlichen Nebenleistungsvereinbarung. Kaufpreis darf diesen Wert noch nicht enthalten.')
    return ergebnis


def vorkauf_gesamtpreisanteil(gesamtpreis=None, wert_vorkaufsgegenstand=None, wert_gesamtkauf=None, einordnungsnachweis=None):
    """Gesamtpreis mit Wert des Vorkaufsgegenstands geteilt durch positiven Wert des Gesamtkaufs multiplizieren."""
    werte = [_geld(gesamtpreis), _geld(wert_vorkaufsgegenstand), _geld(wert_gesamtkauf)]
    _text(einordnungsnachweis, 'einordnungsnachweis')
    if werte[2] <= 0 or werte[1] > werte[2]:
        _fehler('wert_gesamtkauf', 'Gesamtwert muss positiv und mindestens so hoch wie Gegenstandswert sein.')
    eingaben = dict(gesamtpreis=gesamtpreis, wert_vorkaufsgegenstand=wert_vorkaufsgegenstand, wert_gesamtkauf=wert_gesamtkauf, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(_multiplizieren(werte[0],_dividieren(werte[1],werte[2])), 'BGB_VORKAUF_GESAMTPREISANTEIL', eingaben, [dict(operation='Gesamtpreis mit Wert des Vorkaufsgegenstands geteilt durch positiven Wert des Gesamtkaufs multiplizieren')])
    ergebnis['hinweise'].append('Nur§467 Satz1, rechtlich qualifiziertes Wertverhältnis als Eingabe. Bei Verlangen der Gesamterstreckung nach Satz2 anderen Umfang bewerten; keine automatische Alleinbewertung oder Kopfteilung. Gegenstandswert darf Gesamtwert nicht übersteigen.')
    return ergebnis


def vorkauf_stundungssicherheit(gestundeter_kaufpreis=None, bereits_qualifiziert_gesicherter_teil=None, einordnungsnachweis=None):
    """Gestundeten Kaufpreis um den nach§468 Absatz2 von zusätzlicher Sicherheit befreiten Teil vermindern."""
    werte = [_geld(gestundeter_kaufpreis), _geld(bereits_qualifiziert_gesicherter_teil)]
    _text(einordnungsnachweis, 'einordnungsnachweis')
    if werte[1] > werte[0]:
        _fehler('bereits_qualifiziert_gesicherter_teil', 'Befreiter Teil darf gestundeten Kaufpreis nicht übersteigen.')
    eingaben = dict(gestundeter_kaufpreis=gestundeter_kaufpreis, bereits_qualifiziert_gesicherter_teil=bereits_qualifiziert_gesicherter_teil, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(_subtrahieren(werte[0],werte[1]), 'BGB_VORKAUF_STUNDUNGSSICHERHEIT', eingaben, [dict(operation='Gestundeten Kaufpreis um den nach§468 Absatz2 von zusätzlicher Sicherheit befreiten Teil vermindern')])
    ergebnis['hinweise'].append('Befreiter Teil nur für qualifiziert vereinbarte Hypothek bzw.in Anrechnung auf Kaufpreis übernommene hypothekarische Schuld, entsprechend eingetragenes Schiff/Schiffsbauwerk; sonst0. Keine beliebige vorhandene Sicherheit anrechnen, Überlappungen vorab entfernen. Teil höchstens gestundeter Kaufpreis.')
    return ergebnis
