"""Wiederholte Verfahrensabschnitte mit Sechsmonatsnachlauf nach§204II."""
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _text, _vorhanden
from .verjaehrungshemmung import verjaehrung_gehemmte_kalendertage


def verjaehrung_verfahrenshemmungskette(fristlauf_erster_tag=None, grundfrist_letzter_tag=None, verfahrensabschnitte=None, einordnungsnachweis=None):
    """Qualifizierte Beginn-/Weiterbetriebsabschnitte mit Nachlauf bilden und vereinigen."""
    _datum(fristlauf_erster_tag,'fristlauf_erster_tag')
    _datum(grundfrist_letzter_tag,'grundfrist_letzter_tag')
    _vorhanden(verfahrensabschnitte,'verfahrensabschnitte')
    if not isinstance(verfahrensabschnitte,list) or len(verfahrensabschnitte)>10000:
        _fehler('verfahrensabschnitte','Liste mit höchstens10000 abgeschlossenen Verfahrensabschnitten erforderlich.')
    _text(einordnungsnachweis,'einordnungsnachweis')
    intervalle=[]
    for abschnitt in verfahrensabschnitte:
        if not isinstance(abschnitt,dict) or set(abschnitt)!={'hemmungsbeginn_am','nachlaufereignis_am','nachlaufgrund'}:
            _fehler('verfahrensabschnitte','Genau hemmungsbeginn_am, nachlaufereignis_am und nachlaufgrund erforderlich.')
        beginn = _datum(abschnitt['hemmungsbeginn_am'],'hemmungsbeginn_am')
        ereignis = _datum(abschnitt['nachlaufereignis_am'],'nachlaufereignis_am')
        _auswahl(abschnitt['nachlaufgrund'],'nachlaufgrund',('rechtskraeftige_entscheidung','anderweitige_beendigung','stillstand_letzte_verfahrenshandlung'))
        if ereignis < beginn:
            _fehler('verfahrensabschnitte','Nachlaufereignis darf nicht vor Beginn desselben Hemmungsabschnitts liegen.')
        ende = _frist(abschnitt['nachlaufereignis_am'],6,'monate','ereignis')
        intervalle.append(dict(erster_gehemmter_tag=beginn.isoformat(),letzter_gehemmter_tag=ende.isoformat()))
    kern = verjaehrung_gehemmte_kalendertage(fristlauf_erster_tag,grundfrist_letzter_tag,intervalle,True)
    eingaben = dict(fristlauf_erster_tag=fristlauf_erster_tag,grundfrist_letzter_tag=grundfrist_letzter_tag,verfahrensabschnitte=verfahrensabschnitte,einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(kern['wert'],'datum_und_tage','BGB_VERJAEHRUNG_VERFAHRENSHEMMUNGSKETTE',eingaben,[dict(operation='Je qualifiziertem Abschnitt sechs Monate Nachlauf berechnen; Anfangs-/Weiterbetriebsintervalle ohne Doppelzählung mit vorhandenem209-Kern verrechnen.')]+kern['rechenschritte'],eingaben.copy())
    ergebnis['hinweise'] = ['§204Absatz2: Beginn des ersten Abschnitts ist rechtlich wirksamer Hemmungsbeginn; nach Stillstand ist Beginn des nächsten Abschnitts das qualifizierte Weiterbetreiben durch eine Partei. Stillstandsereignis ist letzte maßgebliche Verfahrenshandlung, nicht beliebiger späterer Beobachtungstag. Vollständige abgeschlossene Abschnitte und auf ganze Kalendertage normalisierte Grenzen erforderlich. Nachläufe können sich überschneiden; Überlappungen zählen nur einmal. Zwischen Abschnitten läuft die Frist weiter; bereits eingetretene Verjährung wird nicht wiederbelebt. Kein endlos laufendes Verfahren mit künstlichem Enddatum eingeben. Keine automatische Qualifikation von Zustellung, Rechtskraft, Stillstand oder Weiterbetreiben. Besondere Fristen nach204Absatz1/3, weitere Hemmungen, Neubeginn und193 gesondert.']
    return ergebnis
