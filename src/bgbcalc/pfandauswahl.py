"""Numerischer Verwertungsbedarf in vorgegebener Pfandreihenfolge (§1230)."""
from .betraege import _geld
from .kalender import _ergebnis, _fehler, _text, _vorhanden
from .zahlen import _addieren, _bruch, _subtrahieren
from .zinsen import _bruchteile


def pfand_verwertungsbedarf(gesicherter_befriedigungsbedarf=None, pfaender_in_auswahlreihenfolge=None, bewertungsnachweis=None):
    """Positive qualifizierte Nettoerlöse bis zur Bedarfsdeckung summieren."""
    bedarf = _geld(gesicherter_befriedigungsbedarf)
    _vorhanden(pfaender_in_auswahlreihenfolge,'pfaender_in_auswahlreihenfolge')
    if not isinstance(pfaender_in_auswahlreihenfolge,list) or not 1 <= len(pfaender_in_auswahlreihenfolge) <= 1000:
        _fehler('pfaender_in_auswahlreihenfolge','Liste mit1bis1000 einzeln verwertbaren Pfändern erforderlich.')
    namen,werte = [],[]
    for pfand in pfaender_in_auswahlreihenfolge:
        if not isinstance(pfand,dict) or set(pfand)!={'pfand_id','verfuegbarer_nettoerloes'}:
            _fehler('pfaender_in_auswahlreihenfolge','Genau pfand_id und verfuegbarer_nettoerloes erforderlich.')
        name = _text(pfand['pfand_id'],'pfand_id')
        if name in namen:
            _fehler('pfand_id','Pfand darf nicht mehrfach eingerechnet werden.')
        namen.append(name);werte.append(_geld(pfand['verfuegbarer_nettoerloes']))
    _text(bewertungsnachweis,'bewertungsnachweis')
    summe = _bruch(0)
    ausgewaehlt,uebrig = [],[]
    for name,wert in zip(namen,werte):
        if summe < bedarf and wert > 0:
            ausgewaehlt.append(name);summe = _addieren(summe,wert)
        else:
            uebrig.append(name)
    wert = dict(bedarfsbezogene_auswahl=ausgewaehlt,nicht_zur_deckung_benoetigt=uebrig,summe_nettoerloese=_bruchteile(summe),gedeckter_bedarf=_bruchteile(min(summe,bedarf)),restbedarf=_bruchteile(max(_subtrahieren(bedarf,summe),_bruch(0))),rechnerischer_ueberschuss=_bruchteile(max(_subtrahieren(summe,bedarf),_bruch(0))))
    eingaben = dict(gesicherter_befriedigungsbedarf=gesicherter_befriedigungsbedarf,pfaender_in_auswahlreihenfolge=pfaender_in_auswahlreihenfolge,bewertungsnachweis=bewertungsnachweis)
    ergebnis = _ergebnis(wert,'EUR_und_Pfandzuordnung','BGB_PFAND_VERWERTUNGSBEDARF',eingaben,[dict(operation='In vorgegebener Reihenfolge positive verfügbare Nettoerlöse bis Bedarfsdeckung summieren; danach keine weiteren Pfänder einbeziehen.')],eingaben.copy())
    ergebnis['hinweise'] = ['Nur numerisches Bedarfsmodell nach1230 für einzeln verwertbare Pfänder mit vorqualifizierter zulässiger Auswahlreihenfolge. Keine Optimierung oder eigene Bestimmung des Wahlrechts. Nettoerlöse sind belastbar bewertete, gerade für diese Forderung verfügbare Beträge nach Kosten und vorrangigen Rechten; Bedarfsbetrag ohne erneute Aufnahme bereits abgezogener Kosten. Keine unsicheren Prognosen als tatsächlich erzielte Erlöse ausgeben. Bei veränderten Erlösen/Bedingungen neu rechnen; Ergebnis erteilt keine Verkaufserlaubnis. Pfänder mit null verfügbarem Erlös tragen zur Deckung nichts bei; dies entscheidet kein sonstiges Verwertungsrecht. Ein Pfand ist hier eine unteilbare Verkaufseinheit; weitere Teilbarkeit, gemeinsamer Mehrerlös, negative Nettoerlöse, weitere Forderungen und abweichende Auswahlvereinbarungen vorab abgrenzen. Überschuss ist nur Rechendifferenz; seine Rechtszuordnung gesondert nach1247.']
    return ergebnis
