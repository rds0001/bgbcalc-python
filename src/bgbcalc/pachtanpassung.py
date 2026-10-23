from .betraege import _wahrheitswert
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _tage_addieren, _text

def landpacht_anpassung_zeitgrenzen(pachtbeginn_am=None, letzte_aenderung_wirksam_am=None, beginnart=None, naturereignis_ausnahme=None, aenderungsverlangen_am=None, pachtjahr_beginn_am=None, pachtjahr_ende_am=None, einordnungsnachweis=None):
    """Zweijahreswartezeit und Ausnahme rechnerisch verknüpfen, Erklärungstag vergleichen und Rückwirkungsgrenze des zugeordneten Pachtjahres ausweisen."""
    beginn = _datum(pachtbeginn_am,'pachtbeginn_am')
    verlangen = _datum(aenderungsverlangen_am,'aenderungsverlangen_am')
    bezug = beginn
    if letzte_aenderung_wirksam_am is not None:
        bezug = _datum(letzte_aenderung_wirksam_am,'letzte_aenderung_wirksam_am')
    if not beginn <= bezug <= verlangen:
        _fehler('letzte_aenderung_wirksam_am','Beginn und letzte Änderung müssen spätestens beim Verlangen liegen; Änderung nicht vor Beginn.')
    jahrbeginn = _datum(pachtjahr_beginn_am,'pachtjahr_beginn_am')
    jahrende = _datum(pachtjahr_ende_am,'pachtjahr_ende_am')
    if not jahrbeginn <= verlangen <= jahrende:
        _fehler('pachtjahr_beginn_am','Das qualifizierte Pachtjahr muss den Erklärungstag umfassen.')
    _auswahl(beginnart,'beginnart',('ereignis','tagesbeginn'))
    _wahrheitswert(naturereignis_ausnahme,'naturereignis_ausnahme');_text(einordnungsnachweis,'einordnungsnachweis')
    frueh = None if naturereignis_ausnahme else _tage_addieren(_frist(bezug.isoformat(),2,'jahre',beginnart),1)
    wert = dict(erster_tag_nach_wartezeit=None if frueh is None else frueh.isoformat(),rechnerische_rueckwirkungsgrenze=jahrbeginn.isoformat(),wartezeit_eingehalten=frueh is None or verlangen >= frueh)
    eingaben = dict(pachtbeginn_am=pachtbeginn_am, letzte_aenderung_wirksam_am=letzte_aenderung_wirksam_am, beginnart=beginnart, naturereignis_ausnahme=naturereignis_ausnahme, aenderungsverlangen_am=aenderungsverlangen_am, pachtjahr_beginn_am=pachtjahr_beginn_am, pachtjahr_ende_am=pachtjahr_ende_am, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'daten','BGB_LANDPACHT_ANPASSUNG_ZEITGRENZEN',eingaben,[dict(operation='Zweijahreswartezeit und Ausnahme rechnerisch verknüpfen, Erklärungstag vergleichen und Rückwirkungsgrenze des zugeordneten Pachtjahres ausweisen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§593II/III: Zweijahreswartezeit ab Beginn beziehungsweise letzter wirksamer Vertragsleistungsänderung, außer qualifiziertem verwüstendem Naturereignis ohne üblichen Versicherungsschutz. Beginnart rechtlich bestimmen; beim Tagesbeginn1.Juli2022 endet die Wartezeit30.Juni2024, erster Folgetag1.Juli2024. Ausgewiesene Rückwirkungsgrenze ist der Beginn des Pachtjahres des tatsächlichen Verlangens, nicht automatisch der Erklärungstag oder Kalenderjahresbeginn. Eine rechnerisch verfrühte Erklärung wird weder verschoben noch als wirksam bestätigt. Grundlegende Verhältnisänderung, grobes Missverhältnis, Ausschlüsse und konkrete neue Vertragsleistung bleiben extern qualifiziert. Keine Änderung der Pachtdauer, kein automatisch berechneter angemessener Pachtzins; weitere gerichtliche/vertragliche Wirkungen separat.']
    return ergebnis

