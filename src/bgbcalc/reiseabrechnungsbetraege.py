"""Numerische Reiseabrechnungen nach §§651uIV und651pIII."""
from .betraege import _geld, _geld_ergebnis
from .kalender import _text, _fehler
from .zahlen import _addieren, _subtrahieren, _bruch


def gastschulaufenthalt_kuendigungsbetrag(vereinbarter_reisepreis=None, ersparte_aufwendungen=None, notwendige_mehrkosten=None, einordnungsnachweis=None):
    """Vereinbarten Reisepreis um ersparte Aufwendungen mindern und notwendige Mehrkosten hinzufügen."""
    werte = [_geld(vereinbarter_reisepreis), _geld(ersparte_aufwendungen), _geld(notwendige_mehrkosten)]
    _text(einordnungsnachweis,'einordnungsnachweis')
    if werte[1] > werte[0]:
        _fehler('ersparte_aufwendungen','Ersparte Aufwendungen dürfen in diesem Modell den vereinbarten Reisepreis nicht übersteigen.')
    eingaben = dict(vereinbarter_reisepreis=vereinbarter_reisepreis, ersparte_aufwendungen=ersparte_aufwendungen, notwendige_mehrkosten=notwendige_mehrkosten, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(_addieren(_subtrahieren(werte[0],werte[1]),werte[2]), 'BGB_GASTSCHULAUFENTHALT_KUENDIGUNGSBETRAG', eingaben, [dict(operation='Vereinbarten Reisepreis um ersparte Aufwendungen mindern und notwendige Mehrkosten hinzufügen.')])
    ergebnis["hinweise"].append('Nur §651uIV außerhalb einer Kündigung nach §651l. Ersparnis und notwendige Mehrkosten rechtlich bewerten, ohne doppelte Kostenpositionen. Ergebnis ist der Anspruch vor bereits geleisteten Zahlungen, kein automatischer Zahlungssaldo. Bei Ersparnis über dem Preis ist dieser abgegrenzte Fall nicht modelliert; keine erfundene negative Preisforderung.')
    return ergebnis


def pauschalreise_ereignisentschaedigung_anrechnen(anspruch_vor_anrechnung=None, bereits_erhaltene_ereignisentschaedigung=None, einordnungsnachweis=None):
    """Bereits erhaltene anrechenbare Ereignisentschädigung vom Anspruch abziehen, mindestens null."""
    werte = [_geld(anspruch_vor_anrechnung), _geld(bereits_erhaltene_ereignisentschaedigung)]
    _text(einordnungsnachweis,'einordnungsnachweis')
    eingaben = dict(anspruch_vor_anrechnung=anspruch_vor_anrechnung, bereits_erhaltene_ereignisentschaedigung=bereits_erhaltene_ereignisentschaedigung, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(max(_subtrahieren(werte[0],werte[1]),_bruch(0)), 'BGB_PAUSCHALREISE_EREIGNISENTSCHAEDIGUNG_ANRECHNEN', eingaben, [dict(operation='Bereits erhaltene anrechenbare Ereignisentschädigung vom Anspruch abziehen, mindestens null.')])
    ergebnis["hinweise"].append('§651pIII in einer ausdrücklich vorqualifizierten Anrechnungsrichtung. Externe Verordnungen/Übereinkünfte liefern den bewerteten Anspruch und die anrechenbare bereits erhaltene Zahlung; deren Berechnung wird hier nicht erfunden. Mehrere Anspruchspositionen vorab überschneidungsfrei zuordnen; dieselbe Entschädigung nicht mehrfach abziehen. Überschießende Entschädigung begründet hier keinen Rückzahlungsanspruch.')
    return ergebnis
