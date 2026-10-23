"""Vereinigte Alters- und Gemeinschaftshemmung nach§208."""
from .betraege import _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler, _tage_addieren, _text, lebensalter_beginn
from .verjaehrungshemmung import verjaehrung_gehemmte_kalendertage


def verjaehrung_selbstbestimmungszeitraum(fristlauf_erster_tag=None, grundfrist_letzter_tag=None, geburtsdatum=None, gemeinschaft_bei_fristbeginn=None, letzter_gemeinschaftstag=None, einordnungsnachweis=None):
    """§208: Altershemmung bis21 und anfängliche häusliche Gemeinschaft ohne Doppelzählung."""
    erster = _datum(fristlauf_erster_tag,'fristlauf_erster_tag')
    _datum(grundfrist_letzter_tag,'grundfrist_letzter_tag')
    geburt = _datum(geburtsdatum,'geburtsdatum')
    if geburt > erster:
        _fehler('geburtsdatum','Geburt darf nicht nach erstem Fristlauftag liegen.')
    _wahrheitswert(gemeinschaft_bei_fristbeginn,'gemeinschaft_bei_fristbeginn')
    _text(einordnungsnachweis,'einordnungsnachweis')
    altersende = _tage_addieren(_datum(lebensalter_beginn(geburtsdatum,21)['wert'],'altersgrenze'),-1)
    intervalle=[]
    if erster <= altersende:
        intervalle.append(dict(erster_gehemmter_tag=fristlauf_erster_tag,letzter_gehemmter_tag=altersende.isoformat()))
    if gemeinschaft_bei_fristbeginn:
        gemeinschaftsende = _datum(letzter_gemeinschaftstag,'letzter_gemeinschaftstag')
        if gemeinschaftsende < erster:
            _fehler('letzter_gemeinschaftstag','Bei Fristbeginn bestehende Gemeinschaft kann nicht vorher enden.')
        intervalle.append(dict(erster_gehemmter_tag=fristlauf_erster_tag,letzter_gehemmter_tag=letzter_gemeinschaftstag))
    elif letzter_gemeinschaftstag is not None:
        _fehler('letzter_gemeinschaftstag','Ohne Gemeinschaft bei Fristbeginn kein Gemeinschaftsende angeben.')
    kern = verjaehrung_gehemmte_kalendertage(fristlauf_erster_tag,grundfrist_letzter_tag,intervalle,True)
    eingaben = dict(fristlauf_erster_tag=fristlauf_erster_tag,grundfrist_letzter_tag=grundfrist_letzter_tag,geburtsdatum=geburtsdatum,gemeinschaft_bei_fristbeginn=gemeinschaft_bei_fristbeginn,letzter_gemeinschaftstag=letzter_gemeinschaftstag,einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(kern['wert'],'datum_und_tage','BGB_VERJAEHRUNG_SELBSTBESTIMMUNGSZEITRAUM',eingaben,[dict(operation='Altershemmung bis zum letzten Tag vor21 und bei Fristbeginn bestehende Gemeinschaft vereinigen; tatsächliche Hemmungstage mit vorhandenem209-Kern berücksichtigen.')]+kern['rechenschritte'],eingaben.copy())
    ergebnis['hinweise'] = ['Nur rechtlich qualifizierter Anspruch wegen Verletzung der sexuellen Selbstbestimmung nach§208. Häusliche Gemeinschaft muss bei Beginn der Verjährung bestehen und bis zum angegebenen tatsächlichen Ende ununterbrochen fortbestehen; später neu begründete Gemeinschaft nicht als anfängliche ausgeben. letzter_gemeinschaftstag ist der rechtlich normalisierte letzte eingeschlossene Hemmungstag, kein bloßer Auswertungsstichtag einer noch laufenden Gemeinschaft. Alters- und Gemeinschaftszeit überschneiden sich und werden nicht additiv doppelt gezählt.207, andere Hemmungen, Ablaufhemmung, Neubeginn und193 gesondert.']
    return ergebnis
