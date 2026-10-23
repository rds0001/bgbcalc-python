"""Betragsgrenzen und Ersatzrechnungen des Sachenrechts."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _text
from .zahlen import _addieren, _bruch, _subtrahieren

def fund_herausgabebetrag_nach_kosten(herausgabefaehiger_bruttobetrag=None, abzugsfaehige_kosten=None, anwendungsfall_qualifiziert=None, bewertungsnachweis=None):
    """Qualifizierten herauszugebenden Fundbetrag um abzugsfähige Kosten mindern, mindestens null."""
    betrag_eins = _geld(herausgabefaehiger_bruttobetrag)
    betrag_zwei = _geld(abzugsfaehige_kosten)
    _wahrheitswert(anwendungsfall_qualifiziert, "anwendungsfall_qualifiziert")
    _text(bewertungsnachweis, "bewertungsnachweis")
    eingaben = dict(herausgabefaehiger_bruttobetrag=herausgabefaehiger_bruttobetrag, abzugsfaehige_kosten=abzugsfaehige_kosten, anwendungsfall_qualifiziert=anwendungsfall_qualifiziert, bewertungsnachweis=bewertungsnachweis)
    wert = max(_subtrahieren(betrag_eins, betrag_zwei), _bruch(0)) if anwendungsfall_qualifiziert else None
    ergebnis = _geld_ergebnis(wert, "BGB_FUND_HERAUSGABEBETRAG_NACH_KOSTEN", eingaben, [dict(operation='Qualifizierten herauszugebenden Fundbetrag um abzugsfähige Kosten mindern, mindestens null.')])
    ergebnis["hinweise"].append('Nur rechtlich qualifizierter Herausgabebetrag und zugehörige abzugsfähige Kosten nach981Absatz3. Anspruchsperson, Erlöszuordnung und Fristablauf getrennt; übersteigende Kosten ergeben hier keinen negativen Auszahlungsbetrag und keinen neu festgestellten Zahlungsanspruch.')
    return ergebnis

def abtrennung_abwendungsfehlbetrag(bestandteilswert_nach_abtrennung=None, bereits_ersetzter_bestandteilswert=None, anwendungsfall_qualifiziert=None, bewertungsnachweis=None):
    """Wert des Bestandteils nach Abtrennung um bereits ersetzten Wert mindern, mindestens null."""
    betrag_eins = _geld(bestandteilswert_nach_abtrennung)
    betrag_zwei = _geld(bereits_ersetzter_bestandteilswert)
    _wahrheitswert(anwendungsfall_qualifiziert, "anwendungsfall_qualifiziert")
    _text(bewertungsnachweis, "bewertungsnachweis")
    eingaben = dict(bestandteilswert_nach_abtrennung=bestandteilswert_nach_abtrennung, bereits_ersetzter_bestandteilswert=bereits_ersetzter_bestandteilswert, anwendungsfall_qualifiziert=anwendungsfall_qualifiziert, bewertungsnachweis=bewertungsnachweis)
    wert = max(_subtrahieren(betrag_eins, betrag_zwei), _bruch(0)) if anwendungsfall_qualifiziert else None
    ergebnis = _geld_ergebnis(wert, "BGB_ABTRENNUNG_ABWENDUNGSFEHLBETRAG", eingaben, [dict(operation='Wert des Bestandteils nach Abtrennung um bereits ersetzten Wert mindern, mindestens null.')])
    ergebnis["hinweise"].append('Nur numerischer Fehlbetrag der Wertabwendung nach997Absatz2. Wert ist der rechtlich bewertete Nutzen des abgetrennten Bestandteils gerade für den Besitzer; tatsächlicher Ersatz, kein bloß angebotenes Geld. Weitere Ausschlüsse wegen gewöhnlicher Erhaltung oder fehlendem Nutzen sowie258 bleiben separat; Ergebnis allein entscheidet kein Abtrennungsrecht.')
    return ergebnis

