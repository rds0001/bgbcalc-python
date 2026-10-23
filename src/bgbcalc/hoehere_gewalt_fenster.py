from .kalender import _datum, _ergebnis, _fehler, _frist, _text, _vorhanden
from .verjaehrungshemmung import verjaehrung_gehemmte_kalendertage

def verjaehrung_hoehere_gewalt_fenster(fristlauf_erster_tag=None, grundfrist_letzter_tag=None, fenster_erster_tag=None, fenster_letzter_tag=None, verhinderungszeitraeume=None, einordnungsnachweis=None):
    """Qualifiziertes206-Fenster mit Verhinderungsintervallen schneiden und vorhandenen209-Hemmungskern auf die Schnittintervalle anwenden."""
    erster = _datum(fristlauf_erster_tag,'fristlauf_erster_tag');grundende = _datum(grundfrist_letzter_tag,'grundfrist_letzter_tag')
    von = _datum(fenster_erster_tag,'fenster_erster_tag');bis = _datum(fenster_letzter_tag,'fenster_letzter_tag')
    fenstergrenze = _datum('9999-12-31','datumgrenze') if von.year==9999 and von.month>=7 else _frist(von.isoformat(),6,'monate','tagesbeginn')
    if erster>grundende or von>bis or bis>fenstergrenze:
        _fehler('fenster','Geordneter Fristlauf und Fenster von höchstens sechs Kalendermonaten erforderlich.')
    _text(einordnungsnachweis,'einordnungsnachweis');_vorhanden(verhinderungszeitraeume,'verhinderungszeitraeume')
    if not isinstance(verhinderungszeitraeume,list) or len(verhinderungszeitraeume)>10000:
        _fehler('verhinderungszeitraeume','Unbenannte Liste0..10000 abgeschlossener Intervalle erforderlich.')
    intervalle = []
    for zeit in verhinderungszeitraeume:
        if not isinstance(zeit,dict) or set(zeit)!={'erster_verhinderter_tag','letzter_verhinderter_tag'}:
            _fehler('verhinderungszeitraeume','Genau erster_verhinderter_tag und letzter_verhinderter_tag erforderlich.')
        anfang = _datum(zeit['erster_verhinderter_tag'],'erster_verhinderter_tag');schluss = _datum(zeit['letzter_verhinderter_tag'],'letzter_verhinderter_tag')
        if anfang>schluss:
            _fehler('verhinderungszeitraeume','Ende nicht vor Anfang.')
        if anfang<=bis and schluss>=von:
            intervalle.append(dict(erster_gehemmter_tag=max(anfang,von).isoformat(),letzter_gehemmter_tag=min(schluss,bis).isoformat()))
    wert = verjaehrung_gehemmte_kalendertage(fristlauf_erster_tag,grundfrist_letzter_tag,intervalle,True)['wert']
    eingaben = dict(fristlauf_erster_tag=fristlauf_erster_tag, grundfrist_letzter_tag=grundfrist_letzter_tag, fenster_erster_tag=fenster_erster_tag, fenster_letzter_tag=fenster_letzter_tag, verhinderungszeitraeume=verhinderungszeitraeume, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'datum_und_tage','BGB_VERJAEHRUNG_HOEHERE_GEWALT_FENSTER',eingaben,[dict(operation='Qualifiziertes206-Fenster mit Verhinderungsintervallen schneiden und vorhandenen209-Hemmungskern auf die Schnittintervalle anwenden.')],eingaben.copy())
    ergebnis["hinweise"] = ['§206 mit209: nur Schnittmenge rechtlich qualifizierter Verfolgungshindernisse mit einem ausdrücklich vorgegebenen vollständigen Sechsmonatsfenster; vorhandener209-Kern vereinigt Überschneidungen und rechnet Hemmungstage heraus. Das Fenster wird weder eigenständig rückwärts aus dem Enddatum ermittelt noch dynamisch verschoben. Seine richtige rechtliche Lage und die Anwendbarkeit eines einzelnen abgeschlossenen Fensters sind Voraussetzungen dieser Funktion. Bei ungeklärten, fortdauernden oder mehrfach zu korrigierenden Fensterlagen keine abschließende Verjährung behaupten. Kein allgemeiner Nachlauf von sechs Monaten nach Wegfall des Hindernisses. Höhere Gewalt, Zumutbarkeit und Kausalität sind Rechts-/Tatsachenbewertungen. Alle Grenzen einschließlich, keine untertägige Rundung und keine doppelte Erfassung bereits berücksichtigter Hemmungen. Ablaufhemmung und Neubeginn getrennt.']
    return ergebnis

