from .kalender import _ergebnis, _text, _fehler
from .betraege import _geld
from .zahlen import _bruch, _addieren, _subtrahieren, _multiplizieren
from .zinsen import _bruchteile
from .modernisierung_foerderkappung import modernisierung_kappung_mit_laufenden_abzuegen

def heizungsmodernisierung_mit_jahresfoerderung(kosten_wohnung=None, von_erhaltungspauschale_ausgenommene_kosten=None, kapitalzuschuesse=None, jaehrliche_zinsermaessigung=None, jaehrliche_laufende_foerderung=None, monatliche_restkappung=None, abzugsreihenfolge=None, methodennachweis=None):
    """559e-Kostenbasis und10%-Jahresumlage mit ausdrücklich qualifizierter559aII-Jahresförderung/Kappungsreihenfolge verbinden."""
    k=_geld(kosten_wohnung);e=_geld(von_erhaltungspauschale_ausgenommene_kosten);z=_geld(kapitalzuschuesse);zins=_geld(jaehrliche_zinsermaessigung);laufend=_geld(jaehrliche_laufende_foerderung);_text(methodennachweis,'methodennachweis')
    if e>k or z>k:_fehler('kosten_und_foerderung','Ausnahmeanteil und Kapitalbeitrag jeweils höchstens Kosten.')
    if _addieren(_addieren(z,zins),laufend)<=0:_fehler('foerderung','Tatsächliche positive Förderung erforderlich; ohne Förderung559gesondert.')
    pausch=_multiplizieren(_subtrahieren(k,e),_bruch(3,20));basis=max(_subtrahieren(_subtrahieren(k,pausch),z),_bruch(0));jahr=_multiplizieren(basis,_bruch(1,10))
    foerderung=modernisierung_kappung_mit_laufenden_abzuegen(_bruchteile(jahr),jaehrliche_zinsermaessigung,jaehrliche_laufende_foerderung,monatliche_restkappung,abzugsreihenfolge,methodennachweis)['wert']
    wert=dict(erhaltungspauschale=_bruchteile(pausch),kostenbasis=_bruchteile(basis),jahresbetrag_vor_jahresfoerderung=_bruchteile(jahr),foerderkappung=foerderung)
    eingaben = dict(kosten_wohnung=kosten_wohnung, von_erhaltungspauschale_ausgenommene_kosten=von_erhaltungspauschale_ausgenommene_kosten, kapitalzuschuesse=kapitalzuschuesse, jaehrliche_zinsermaessigung=jaehrliche_zinsermaessigung, jaehrliche_laufende_foerderung=jaehrliche_laufende_foerderung, monatliche_restkappung=monatliche_restkappung, abzugsreihenfolge=abzugsreihenfolge, methodennachweis=methodennachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_HEIZUNGSMODERNISIERUNG_MIT_JAHRESFOERDERUNG',eingaben,[dict(operation='559e-Kostenbasis und10%-Jahresumlage mit ausdrücklich qualifizierter559aII-Jahresförderung/Kappungsreihenfolge verbinden.')],eingaben.copy())
    ergebnis["hinweise"] = ['Bedingte Heizungsrechnung nach559e:15%des nicht nach lokaler559eII2ausgenommenen Kostenanteils als Erhaltungspauschale, dann einmaliger Kapitalbeitrag, positive Kostenbasis*10%jährlich. Qualifizierte559aII-Zins-/laufende Jahresförderung mit bestehendem Förderkappungskern berücksichtigen. Die rechtliche Übertragung dieser Jahresabzugsmethode auf den konkreten559e-Förderfall wird ausdrücklich vorausgesetzt, nicht als allgemein geklärt behauptet. Der Nennbetrag eines rückzahlbaren Darlehens wird nicht ohne Rechtsgrund als verlorener Kapitalzuschuss behandelt. Mindestens eine tatsächliche berücksichtigungsfähige Förderung erforderlich; ohne Förderung ist559-Verfahren gesondert. Kein doppelter Abzug tatsächlicher Erhaltungskosten zusätzlich zur Pauschale; keine automatische Härte-/Förderfähigkeitsentscheidung.']
    return ergebnis

