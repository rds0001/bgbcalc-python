"""Numerische Anzeige- und Einstimmigkeitsgrenzen ohne Rechtsfolgenautomatik."""
from .betraege import _geld
from .kalender import _ergebnis, _fehler, _ganzzahl
from .zahlen import GRENZE, _bruch
from .zinsen import _bruchteile


def fund_anzeigewertgrenze(sachenwert=None):
    """§965II: Wert überschreitet10EUR; bei genau10EUR keine Überschreitung."""
    wert = _geld(sachenwert)
    eingaben = dict(sachenwert=sachenwert)
    ergebnis = _ergebnis(dict(wertgrenze=_bruchteile(_bruch(10)),wertgrenze_ueberschritten=wert>10),'EUR_und_wahrheitswert','BGB_FUND_ANZEIGEWERTGRENZE',eingaben,[dict(operation='Sachenwert strikt mit10EUR vergleichen.')],eingaben.copy())
    ergebnis['hinweise'] = ['Nur Wertgrenze für behördliche Fundanzeige nach965Absatz2. Sache und deren Wert rechtlich qualifiziert; Kenntnis/Ermittlung des Empfangsberechtigten und übrige Anzeige-/Verwahrungspflichten gesondert. Bei genau10EUR ist die Grenze nicht überschritten; keine allgemeine Befreiung von sämtlichen Finderpflichten.']
    return ergebnis


def liquidatoren_einstimmigkeitsgrenze(anzahl_liquidatoren=None,zustimmende_liquidatoren=None):
    """§48III: rechnerisch erforderliche Zustimmung aller Liquidatoren im gesetzlichen Grundfall."""
    alle = _ganzzahl(anzahl_liquidatoren,'anzahl_liquidatoren',1,GRENZE)
    ja = _ganzzahl(zustimmende_liquidatoren,'zustimmende_liquidatoren',0,GRENZE)
    if ja > alle:
        _fehler('zustimmende_liquidatoren','Zustimmungen dürfen Zahl der Liquidatoren nicht übersteigen.')
    eingaben = dict(anzahl_liquidatoren=anzahl_liquidatoren,zustimmende_liquidatoren=zustimmende_liquidatoren)
    ergebnis = _ergebnis(dict(erforderliche_zustimmungen=alle,fehlende_zustimmungen=alle-ja,einstimmigkeit_erreicht=ja==alle),'anzahl_und_wahrheitswert','BGB_LIQUIDATOREN_EINSTIMMIGKEITSGRENZE',eingaben,[dict(operation='Erforderlich sind sämtliche Liquidatoren; fehlende Zustimmungen als Anzahl minus Zustimmungen berechnen.')],eingaben.copy())
    ergebnis['hinweise'] = ['Nur gesetzlicher Einstimmigkeitsgrundfall nach48Absatz3 ohne abweichende Bestimmung. Maßgeblicher Liquidatorenkreis und anrechenbare Zustimmungen vorqualifiziert; Liquidatoren nicht mit Vereinsmitgliedern verwechseln. Keine Vertretungs- oder Beschlusswirksamkeitsentscheidung.']
    return ergebnis
