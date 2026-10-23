from .kalender import _ergebnis, _fehler, _text, _vorhanden
from .betraege import _geld
from .zahlen import _addieren, _subtrahieren
from .zinsen import _bruchteile

def geldschulden_nach_betragsbestimmung_tilgen(zahlung=None, betragsbestimmungen=None, einordnungsnachweis=None):
    """Ausdrückliche Betragszuordnung je Geldschuld begrenzt anrechnen und verbleibende Beträge berechnen."""
    gesamtzahlung=_geld(zahlung);_text(einordnungsnachweis,'einordnungsnachweis');_vorhanden(betragsbestimmungen,'betragsbestimmungen')
    if not isinstance(betragsbestimmungen,list) or not 1<=len(betragsbestimmungen)<=1000: _fehler('betragsbestimmungen','Liste1..1000 erforderlich.')
    namen=set();bestimmt_summe=_geld('0');angerechnet_summe=_geld('0');zuordnungen=[]
    for p in betragsbestimmungen:
        if not isinstance(p,dict) or set(p)!={'schuld_id','offener_betrag','bestimmter_zahlungsbetrag'}: _fehler('betragsbestimmungen','Genau Kennung,offenerBetrag,bestimmterZahlungsbetrag erforderlich.')
        name=_text(p['schuld_id'],'schuld_id');offen=_geld(p['offener_betrag']);bestimmt=_geld(p['bestimmter_zahlungsbetrag'])
        if name in namen: _fehler('schuld_id','Eindeutige Schulden erforderlich.')
        namen.add(name);bestimmt_summe=_addieren(bestimmt_summe,bestimmt)
        if bestimmt_summe>gesamtzahlung: _fehler('betragsbestimmungen','Bestimmte Beträge überschreiten verfügbare Zahlung.')
        angerechnet=min(offen,bestimmt);angerechnet_summe=_addieren(angerechnet_summe,angerechnet)
        zuordnungen.append(dict(schuld_id=name,angerechneter_betrag=_bruchteile(angerechnet),restforderung=_bruchteile(_subtrahieren(offen,angerechnet))))
    wert=dict(zuordnungen=zuordnungen,nicht_zugeordnet=_bruchteile(_subtrahieren(gesamtzahlung,angerechnet_summe)))
    eingaben = dict(zahlung=zahlung, betragsbestimmungen=betragsbestimmungen, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_GELDSCHULDEN_NACH_BETRAGSBESTIMMUNG_TILGEN',eingaben,[dict(operation='Ausdrückliche Betragszuordnung je Geldschuld begrenzt anrechnen und verbleibende Beträge berechnen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§366I: rechtlich vorgegebene Betragsbestimmung je Schuld bis zur Höhe des offenen Betrags ausführen; verbleibende Forderungen und nicht zugeordneten Teil der Gesamtzahlung ausweisen. Keine zusätzliche Verwendung von Überhängen für andere Schulden entgegen der qualifizierten Bestimmung. Summe der erklärten Betragsbestimmungen größer als Zahlung ist widersprüchliche Eingabe, keine erfundene anteilige Kürzung. Gesetzliche Ersatzreihenfolge366II nur bei fehlender Bestimmung in eigener Funktion;367Bestandteile einer Schuld separat. Nicht zugeordnete Zahlung ist keine automatische Rückforderung. Abweichende Vereinbarungen nur als zuvor rechtlich festgelegte Betragszuordnung, keine freie Vertragsauslegung.']
    return ergebnis

