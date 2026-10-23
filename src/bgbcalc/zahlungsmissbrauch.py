"""Numerische Zahlerhaftung mit qualifizierten gesetzlichen Ausnahmen."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _text
from .zahlen import _bruch


def zahlungsmissbrauch_zahlerhaftungsbetrag(schadensbetrag=None, betruegerische_absicht=None, qualifizierte_pflichtverletzung=None, ausschluss_absatz_2=None, ausschluss_absatz_4_oder_5=None, einordnungsnachweis=None):
    """Betrugsvorrang, qualifizierte Haftungsausschlüsse und Fünfzig-Euro-Grundgrenze anwenden."""
    schaden=_geld(schadensbetrag)
    for name,wert in [('betruegerische_absicht',betruegerische_absicht),('qualifizierte_pflichtverletzung',qualifizierte_pflichtverletzung),('ausschluss_absatz_2',ausschluss_absatz_2),('ausschluss_absatz_4_oder_5',ausschluss_absatz_4_oder_5)]:
        _wahrheitswert(wert,name)
    _text(einordnungsnachweis,'einordnungsnachweis')
    if betruegerische_absicht:
        betrag=schaden
    elif ausschluss_absatz_4_oder_5:
        betrag=_bruch(0)
    elif qualifizierte_pflichtverletzung:
        betrag=schaden
    elif ausschluss_absatz_2:
        betrag=_bruch(0)
    else:
        betrag=min(schaden,_bruch(50))
    eingaben=dict(schadensbetrag=schadensbetrag,betruegerische_absicht=betruegerische_absicht,qualifizierte_pflichtverletzung=qualifizierte_pflichtverletzung,ausschluss_absatz_2=ausschluss_absatz_2,ausschluss_absatz_4_oder_5=ausschluss_absatz_4_oder_5,einordnungsnachweis=einordnungsnachweis)
    ergebnis=_geld_ergebnis(betrag,'BGB_ZAHLUNGSMISSBRAUCH_ZAHLERHAFTUNGSBETRAG',eingaben,[dict(operation='Bei Betrug voller Schaden; sonst vorrangiger Ausschluss Absatz4/5 null; sonst qualifizierte Pflichtverletzung voller Schaden; sonst Absatz2 null; sonst höchstens50EUR.')])
    ergebnis['hinweise'].append('Nur §675v im qualifizierten Anwendungsbereich nicht autorisierter Zahlungsvorgänge/Zahlungsinstrumente. Betrug und qualifizierte vorsätzliche/grob fahrlässige kausale Pflichtverletzung nach Absatz3 getrennt bewerten. Absatz2 betrifft unbemerkbaren Missbrauch bzw. dienstleisterseitigen Verlust; Absatz4/5 betrifft qualifiziert fehlende starke Authentifizierung oder nach Anzeige entstandene Schäden bzw. fehlende Anzeigemöglichkeit. Ausschlussflag Absatz4/5 bezeichnet den Grundtatbestand vor Betrugsausnahme. Schaden muss derselben rechtlich einheitlichen Haftungseinheit angehören;50EUR nicht automatisch je Einzelbuchung erneut ausschöpfen. Keine automatische Betrugs-/Verschuldensbeurteilung, Kontokorrektur nach §675u oder Haftung des Zahlungsempfängers.')
    return ergebnis
