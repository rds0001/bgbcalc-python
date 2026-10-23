from .kalender import _ergebnis, _text, _ganzzahl, _auswahl, _fehler
from .betraege import _geld
from .zahlen import _bruch, _zahleneingabe, _multiplizieren, _addieren, _subtrahieren, _runden
from .zinsen import _bruchteile

def verbraucherdarlehen_centannuitaet_neuberechnen(anfangskapital=None, korrigierter_periodenzinssatz=None, anzahl_teilzahlungen=None, geschuldete_kosten_je_teilzahlung=None, rundungsmodus=None, plannachweis=None):
    """Kleinste centgenaue nachschüssige Kapitaldienstrate durch monotone Suche bestimmen; Zinsen und Restschulden je Periode mit vorgegebener Rundung fortschreiben."""
    kapital=_geld(anfangskapital);satz=_zahleneingabe(korrigierter_periodenzinssatz);anzahl=_ganzzahl(anzahl_teilzahlungen,'anzahl_teilzahlungen',1,1000);kosten=_geld(geschuldete_kosten_je_teilzahlung);_auswahl(rundungsmodus,'rundungsmodus',('kaufmaennisch','gerade'));_text(plannachweis,'plannachweis')
    if satz<=-1:_fehler('korrigierter_periodenzinssatz','Periodenquote muss größer als-1sein.')
    for x in (kapital,kosten):
        if _zahleneingabe(_runden(x,2,'gerade'))!=x:_fehler('betrag','Centgenaue Beträge erforderlich.')
    def zins(rest):return _zahleneingabe(_runden(_multiplizieren(rest,satz),2,rundungsmodus))
    def rest_nach(rate):
        rest=kapital
        for _ in range(anzahl):
            vorher=rest;rest=max(_subtrahieren(_addieren(rest,zins(rest)),rate),_bruch(0))
            if rest==0:break
            if rest>=vorher:return rest
        return rest
    unter=0;ober=int(_multiplizieren(_addieren(kapital,zins(kapital)),_bruch(100)))
    while unter<ober:
        mitte=(unter+ober)//2
        if rest_nach(_bruch(mitte,100))==0:ober=mitte
        else:unter=mitte+1
    rate=_bruch(unter,100);rest=kapital;zeilen=[];zinsgesamt=gesamt=_bruch(0)
    for i in range(anzahl):
        anfang=rest;z=zins(rest);zahlung=min(rate,_addieren(rest,z));rest=_subtrahieren(_addieren(rest,z),zahlung);teilzahlung=_addieren(zahlung,kosten);zinsgesamt=_addieren(zinsgesamt,z);gesamt=_addieren(gesamt,teilzahlung)
        zeilen.append(dict(zahlungsnummer=i+1,anfangssaldo=_bruchteile(anfang),zinsbetrag=_bruchteile(z),kapitaldienst=_bruchteile(zahlung),geschuldete_kosten=_bruchteile(kosten),neue_teilzahlung=_bruchteile(teilzahlung),restkapital=_bruchteile(rest)))
    wert=dict(regelmaessiger_kapitaldienst=_bruchteile(rate),teilzahlungen=zeilen,zinsgesamtbetrag=_bruchteile(zinsgesamt),neuer_gesamtbetrag=_bruchteile(gesamt),restkapital=_bruchteile(rest))
    eingaben = dict(anfangskapital=anfangskapital, korrigierter_periodenzinssatz=korrigierter_periodenzinssatz, anzahl_teilzahlungen=anzahl_teilzahlungen, geschuldete_kosten_je_teilzahlung=geschuldete_kosten_je_teilzahlung, rundungsmodus=rundungsmodus, plannachweis=plannachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_VERBRAUCHERDARLEHEN_CENTANNUITAET_NEUBERECHNEN',eingaben,[dict(operation='Kleinste centgenaue nachschüssige Kapitaldienstrate durch monotone Suche bestimmen; Zinsen und Restschulden je Periode mit vorgegebener Rundung fortschreiben.')],eingaben.copy())
    ergebnis["hinweise"] = ['Bedingter vertraglicher Annuitätenplan für494V, kein gesetzlich vorgeschriebenes Universalmodell. Bestehenden exakten Rundungskern verwenden. Durch monotone ganzzahlige Intervallsuche kleinste centgenaue Kapitaldienstrate bestimmen, die das Kapital bis zum letzten Termin tilgt. Jede Periode Zins=Anfangssaldo*Periodenquote aufCent runden; Zahlung=min(Regelrate,Saldo+Zins), danach Saldo fortschreiben. Letzte Zahlung kann kleiner sein; bei frühzeitiger Tilgung weitere Kapitaldienstraten0. Explizite gleichbleibende Zusatzkosten separat addieren. Keine Potenz riesiger Brüche, keine Näherungstoleranz, keine Kapitalisierung von Kosten oder Änderung der vorgegebenen Laufzeit. Negative korrigierte Zinsen sind mathematische Rechenwerte, keine automatische rechtliche Pflicht des Darlehensgebers. Nicht erfasst: vorschüssige Zahlung, variable Perioden oder abweichende Rundungs-/Gebührenstruktur; diese Vertragsmodelle nicht stillschweigend ersetzen.']
    return ergebnis

