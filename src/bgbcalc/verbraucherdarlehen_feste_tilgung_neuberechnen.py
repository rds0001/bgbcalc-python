from .kalender import _ergebnis, _text, _vorhanden, _fehler
from .betraege import _geld
from .zahlen import _bruch, _zahleneingabe, _multiplizieren, _addieren, _subtrahieren
from .zinsen import _bruchteile

def verbraucherdarlehen_feste_tilgung_neuberechnen(anfangskapital=None, korrigierter_sollzinssatz=None, teilzahlungen=None, plannachweis=None):
    """Kapitalsalden aus festen Tilgungen fortschreiben; korrigierte Abschnittszinsen und verbleibende Kosten zur neuen Teilzahlung addieren."""
    rest=_geld(anfangskapital);satz=_zahleneingabe(korrigierter_sollzinssatz);_text(plannachweis,'plannachweis');_vorhanden(teilzahlungen,'teilzahlungen')
    if not isinstance(teilzahlungen,list) or not 1<=len(teilzahlungen)<=1000:_fehler('teilzahlungen','Chronologische Liste1..1000erforderlich.')
    namen=set();zeilen=[];zinsgesamt=kostengesamt=wegfallgesamt=gesamt=_bruch(0)
    for p in teilzahlungen:
        if not isinstance(p,dict) or set(p)!={'zahlung_id','kapitaltilgung','jahresanteil','vereinbarte_kosten','nicht_geschuldete_kosten'}:_fehler('teilzahlungen','Vollständige Teilzahlungsfelder erforderlich.')
        name=_text(p['zahlung_id'],'zahlung_id');tilgung=_geld(p['kapitaltilgung']);zeit=_geld(p['jahresanteil']);kosten=_geld(p['vereinbarte_kosten']);wegfall=_geld(p['nicht_geschuldete_kosten'])
        if name in namen:_fehler('zahlung_id','Jede Zahlung nur einmal.')
        if tilgung>rest or wegfall>kosten:_fehler('teilzahlungen','Tilgung übersteigt Restkapital oder Kostenwegfall übersteigt Kosten.')
        namen.add(name);anfang=rest;zins=_multiplizieren(_multiplizieren(anfang,satz),zeit);geschuldet=_subtrahieren(kosten,wegfall);rate=_addieren(_addieren(tilgung,zins),geschuldet);rest=_subtrahieren(rest,tilgung)
        zinsgesamt=_addieren(zinsgesamt,zins);kostengesamt=_addieren(kostengesamt,geschuldet);wegfallgesamt=_addieren(wegfallgesamt,wegfall);gesamt=_addieren(gesamt,rate)
        zeilen.append(dict(zahlung_id=name,anfangssaldo=_bruchteile(anfang),kapitaltilgung=_bruchteile(tilgung),zinsbetrag=_bruchteile(zins),geschuldete_kosten=_bruchteile(geschuldet),neue_teilzahlung=_bruchteile(rate),restkapital=_bruchteile(rest)))
    if rest!=0:_fehler('teilzahlungen','Vollständiger Tilgungsplan muss das Anfangskapital tilgen.')
    wert=dict(teilzahlungen=zeilen,zinsgesamtbetrag=_bruchteile(zinsgesamt),geschuldete_kosten_gesamt=_bruchteile(kostengesamt),entfallene_kosten_gesamt=_bruchteile(wegfallgesamt),neuer_gesamtbetrag=_bruchteile(gesamt),restkapital=_bruchteile(rest))
    eingaben = dict(anfangskapital=anfangskapital, korrigierter_sollzinssatz=korrigierter_sollzinssatz, teilzahlungen=teilzahlungen, plannachweis=plannachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_VERBRAUCHERDARLEHEN_FESTE_TILGUNG_NEUBERECHNEN',eingaben,[dict(operation='Kapitalsalden aus festen Tilgungen fortschreiben; korrigierte Abschnittszinsen und verbleibende Kosten zur neuen Teilzahlung addieren.')],eingaben.copy())
    ergebnis["hinweise"] = ['494V mit vertraglich unveränderten festen Kapitaltilgungen: jeden Anfangssaldo aus Anfangskapital und vorherigen Tilgungen selbst fortschreiben; Zins=Anfangssaldo*korrigierte Jahresquote*Jahresanteil, geschuldete Kosten=vereinbart-nichtgeschuldet, neue Teilzahlung=Tilgung+Zins+geschuldete Kosten. Summe der Tilgungen muss das Anfangskapital vollständig decken; keine Übertilgung. Negative mathematische Zinsen/Teilzahlungen sichtbar, keine automatische Zahlungspflicht des Darlehensgebers. Keine eigenständige gesetzliche Annuitätenannahme: Verträge mit gleichbleibender Gesamtrate oder verändertem Tilgungsverlauf werden hier nicht in feste Kapitaltilgungen umgedeutet. Jahresanteile und Vertragsstruktur müssen belegt sein; keine Effektivzinsberechnung, keine automatische Rundung, keine Zins-/Kostenkapitalisierung. Rechtliche Folgen494II/III separat in vorhandenen Zinsfunktionen berechnen.']
    return ergebnis

