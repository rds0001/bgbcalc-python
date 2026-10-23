from datetime import date
from .kalender import _datum, _ergebnis, _fehler, _frist, _tage_addieren, _text, _vorhanden
from .verjaehrungshemmung import verjaehrung_gehemmte_kalendertage

def anerkennung_fuenfjahresfrist_mit_hemmung(fristausloesung_am=None, ruecknahmezeitraeume=None, aufschiebende_wirkung_zeitraeume=None, einordnungsnachweis=None):
    """Fünfjahresfrist berechnen; gerichtlich angeordnete aufschiebende Wirkungszeiten aus Rücknahmehemmung ausschneiden und verbleibende Hemmungstage vereinigt berücksichtigen."""
    beginn = _datum(fristausloesung_am,'fristausloesung_am')
    _text(einordnungsnachweis,'einordnungsnachweis')
    def intervalle(eingabe,parameter):
        _vorhanden(eingabe,parameter)
        if not isinstance(eingabe,list) or len(eingabe)>1000: _fehler(parameter,'Liste mit höchstens1000Intervallen erforderlich.')
        ergebnis=[]
        for z in eingabe:
            if not isinstance(z,dict) or set(z)!={'erster_tag','letzter_tag'}: _fehler(parameter,'Genau erster_tag und letzter_tag erforderlich.')
            a=_datum(z['erster_tag'],'erster_tag').toordinal();b=_datum(z['letzter_tag'],'letzter_tag').toordinal()
            if a>b: _fehler(parameter,'Intervallende liegt vor Beginn.')
            ergebnis.append((a,b))
        vereinigt=[]
        for a,b in sorted(ergebnis):
            if vereinigt and a<=vereinigt[-1][1]+1: vereinigt[-1]=(vereinigt[-1][0],max(b,vereinigt[-1][1]))
            else: vereinigt.append((a,b))
        return vereinigt
    ruecknahmen=intervalle(ruecknahmezeitraeume,'ruecknahmezeitraeume')
    ausnahmen=intervalle(aufschiebende_wirkung_zeitraeume,'aufschiebende_wirkung_zeitraeume')
    wirksam=[]
    for a,b in ruecknahmen:
        teile=[(a,b)]
        for c,d in ausnahmen:
            neu=[]
            for x,y in teile:
                if d<x or c>y: neu.append((x,y))
                else:
                    if x<c: neu.append((x,c-1))
                    if y>d: neu.append((d+1,y))
            teile=neu
        wirksam.extend(dict(erster_gehemmter_tag=date.fromordinal(x).isoformat(),letzter_gehemmter_tag=date.fromordinal(y).isoformat()) for x,y in teile)
    grundende=_frist(fristausloesung_am,5,'jahre','ereignis')
    kern=verjaehrung_gehemmte_kalendertage(_tage_addieren(beginn,1).isoformat(),grundende.isoformat(),wirksam,True)
    wert=dict(grundfrist_letzter_tag=grundende.isoformat(),**kern['wert'])
    eingaben = dict(fristausloesung_am=fristausloesung_am, ruecknahmezeitraeume=ruecknahmezeitraeume, aufschiebende_wirkung_zeitraeume=aufschiebende_wirkung_zeitraeume, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'daten_und_tage','BGB_ANERKENNUNG_FUENFJAHRESFRIST_MIT_HEMMUNG',eingaben,[dict(operation='Fünfjahresfrist berechnen; gerichtlich angeordnete aufschiebende Wirkungszeiten aus Rücknahmehemmung ausschneiden und verbleibende Hemmungstage vereinigt berücksichtigen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§1598II: Fünfjahresgrundlauf ab qualifiziertem Register-/Beurkundungsereignis. Von den abgeschlossenen qualifizierten Rücknahmeintervallen die Intervalle angeordneter aufschiebender Wirkung abziehen; verbleibende Tage vereinigen und nicht mitzählen. Bloße Rechtsbehelfseinlegung ist keine automatische aufschiebende Wirkung. Alle Intervalle müssen rechtlich taggenau normalisiert sein; offene oder unbekannte Enden nicht durch erfundene Daten ersetzen. Eine nach bereits abgeschlossenem Fristlauf eintretende Rücknahme setzt keine neue Frist in Gang. Keine automatische Anerkennungswirksamkeit, Ausländerbehördenentscheidung oder Feiertagsverschiebung.']
    return ergebnis

