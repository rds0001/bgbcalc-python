"""Digitale Vertragsfristen mit qualifizierter Ereigniswahl (§§327k/n/o/r/u)."""
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _text
_FAELLE = {'minderung_erstattung': (14, 'tage', '§327n Absatz4: Zugang der Minderungserklärung beim Unternehmer; Höchstfrist ersetzt nicht unverzügliche Erstattung.'), 'beendigung_erstattung': (14, 'tage', '§327o Absatz4 mit§327n Absatz4: Zugang der Beendigungserklärung; Höchstfrist ersetzt nicht unverzügliche Erstattung.'), 'datentraeger_rueckforderung': (14, 'tage', '§327o Absatz5: rechtlich wirksame Vertragsbeendigung; Frist für das Rücksendeverlangen des Unternehmers, nicht Rücksendefrist des Verbrauchers.'), 'aenderung_beendigung': (30, 'tage', '§327r Absatz3: Zugang der qualifizierten Änderungsinformation, bei späterer Änderung deren Zeitpunkt; AusnahmenAbsatz4/6 und Beeinträchtigung gesondert.'), 'regress_nichtbereitstellung': (6, 'monate', '§327u Absatz2 Nummer1: Ausübung des Verbraucherrechts nach§327c Absatz1 Satz1; nicht erst Erstattung oder spätere Beschwerde.'), 'regress_nacherfuellung': (6, 'monate', '§327u Absatz2 Nummer2: Erfüllung der Verbraucheransprüche nach§327l Absatz1; keine automatische Hemmung oder Neubeginn.'), 'beweislast_einmalbereitstellung': (1, 'jahre', '§327k Absatz1: Bereitstellung an Verbraucher, auch im Rückgriff327u Absatz3; nur zeitliche Einjahresgrenze, keine Beweis-/Mangelentscheidung. DauerbereitstellungAbsatz2 gesondert.')}

def digitale_vertragsgrundfrist(fristfall=None, ereignis_am=None, aenderung_am=None, einordnungsnachweis=None):
    """Rechnerische Grundfrist, im Änderungsfall ab späterem Information-/Änderungstag."""
    _auswahl(fristfall, 'fristfall', tuple(_FAELLE))
    ausloeser = _datum(ereignis_am, 'ereignis_am')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    if fristfall == 'aenderung_beendigung':
        aenderung = _datum(aenderung_am, 'aenderung_am')
        ausloeser = max(ausloeser, aenderung)
    elif aenderung_am is not None:
        _fehler('aenderung_am', 'Änderungstag ist ausschließlich im Änderungsbeendigungsfall zulässig.')
    anzahl, einheit, fallhinweis = _FAELLE[fristfall]
    ende = _frist(ausloeser.isoformat(), anzahl, einheit, 'ereignis')
    eingaben = dict(fristfall=fristfall, ereignis_am=ereignis_am, aenderung_am=aenderung_am, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(dict(massgeblicher_ausloesertag=ausloeser.isoformat(), rechnerisches_fristende=ende.isoformat()), 'daten', 'BGB_DIGITALE_VERTRAGSGRUNDFRIST', eingaben, [dict(operation='Gesetzliche Ereignisfrist nach digitalem Vertragsfall; beim Änderungsfall späteres Datum aus Information und Änderung wählen')], eingaben.copy())
    ergebnis['annahmen'] = ['Qualifizierter digitaler Vertrags-/Regressfall und rechtlich maßgeblicher Ereignistag; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['Nur rechnerische Grundfrist. Rechtliche Anspruchsvoraussetzungen und qualifizierte Ereignisse sowie Hemmung, Ablaufhemmung und Feiertagskorrekturen separat. Ende bezeichnet letzten eingeschlossenen Tag bis Tagesablauf, rechtzeitige Handlung am Endtag bleibt möglich. Keine automatische Vertragsbeendigung, Mangelvermutung oder abschließende Verjährung.', fallhinweis]
    return ergebnis
