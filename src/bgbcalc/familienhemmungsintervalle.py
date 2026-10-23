"""Altersbezogener Intervallzuschnitt und Hemmungswirkung nach§207."""
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _tage_addieren, _text, _vorhanden, lebensalter_beginn
from .verjaehrungshemmung import verjaehrung_gehemmte_kalendertage


def verjaehrung_familienzeitraeume(fristlauf_erster_tag=None, grundfrist_letzter_tag=None, beziehungsart=None, beziehungszeitraeume=None, geburtsdatum_kind=None, einordnungsnachweis=None):
    """§207: Beziehungsintervalle gegebenenfalls auf21Jahre begrenzen, dann Hemmung vereinigen."""
    erster = _datum(fristlauf_erster_tag,'fristlauf_erster_tag')
    _datum(grundfrist_letzter_tag,'grundfrist_letzter_tag')
    _auswahl(beziehungsart,'beziehungsart',('ehegatten','lebenspartner','kind_eltern','kind_partner_elternteil','vormund_muendel','betreuer_betreuter','pfleger_pflegling','kind_gegen_beistand'))
    altersfall = beziehungsart in ('kind_eltern','kind_partner_elternteil')
    grenze = None
    if altersfall:
        geburt = _datum(geburtsdatum_kind,'geburtsdatum_kind')
        grenze = _tage_addieren(_datum(lebensalter_beginn(geburtsdatum_kind,21)['wert'],'altersgrenze'),-1)
        if geburt > erster:
            _fehler('geburtsdatum_kind','Geburt darf nicht nach dem ersten Fristlauftag liegen.')
    elif geburtsdatum_kind is not None:
        _fehler('geburtsdatum_kind','Geburtsdatum nur für die beiden altersbegrenzten Kindbeziehungen angeben.')
    _vorhanden(beziehungszeitraeume,'beziehungszeitraeume')
    if not isinstance(beziehungszeitraeume,list) or len(beziehungszeitraeume)>10000:
        _fehler('beziehungszeitraeume','Liste mit höchstens10000 abgeschlossenen Beziehungsintervallen erforderlich.')
    _text(einordnungsnachweis,'einordnungsnachweis')
    intervalle=[]
    for zeitraum in beziehungszeitraeume:
        if not isinstance(zeitraum,dict) or set(zeitraum)!={'erster_beziehungstag','letzter_beziehungstag'}:
            _fehler('beziehungszeitraeume','Genau erster_beziehungstag und letzter_beziehungstag erforderlich.')
        anfang = _datum(zeitraum['erster_beziehungstag'],'erster_beziehungstag')
        ende = _datum(zeitraum['letzter_beziehungstag'],'letzter_beziehungstag')
        if anfang > ende:
            _fehler('beziehungszeitraeume','Beziehungsende liegt vor Beziehungsbeginn.')
        if altersfall and anfang < geburt:
            _fehler('beziehungszeitraeume','Kindbeziehung kann nicht vor Geburt beginnen.')
        if grenze is not None:
            ende = min(ende,grenze)
        if anfang <= ende:
            intervalle.append(dict(erster_gehemmter_tag=anfang.isoformat(),letzter_gehemmter_tag=ende.isoformat()))
    kern = verjaehrung_gehemmte_kalendertage(fristlauf_erster_tag,grundfrist_letzter_tag,intervalle,True)
    eingaben = dict(fristlauf_erster_tag=fristlauf_erster_tag,grundfrist_letzter_tag=grundfrist_letzter_tag,beziehungsart=beziehungsart,beziehungszeitraeume=beziehungszeitraeume,geburtsdatum_kind=geburtsdatum_kind,einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(kern['wert'],'datum_und_tage','BGB_VERJAEHRUNG_FAMILIENZEITRAEUME',eingaben,[dict(operation='Kindbeziehungen auf letzten Tag vor Vollendung21 begrenzen; übrige qualifizierte Beziehungsintervalle unverändert vereinigen und aus Fristlauf herausrechnen.')]+kern['rechenschritte'],eingaben.copy())
    ergebnis['hinweise'] = ['Abgeschlossene rechtlich qualifizierte Beziehungsintervalle mit beiden eingeschlossenen ganzen Kalendertagen. Keine automatische Begründung oder Beendigung von Ehe, Betreuung oder Beistandschaft. Kind-gegen-Beistand nur in dieser Anspruchsrichtung. Alter21 begrenzt ausschließlich Kind-Eltern und Kind-Partner-Elternteil. Ein Zeitpunkt laufender Auswertung darf nicht als tatsächliches Beziehungsende ausgegeben werden. Vor Fristbeginn liegende Tage werden nicht angerechnet; überlappende Intervalle nur einmal. Keine Wiederbelebung bereits abgelaufener Fristen. Andere Hemmungen,208, Ablaufhemmung, Neubeginn und193 gesondert.']
    return ergebnis
