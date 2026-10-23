"""Einrede während eines rechtzeitig beantragten Aufgebotsverfahrens (§§2015–2017)."""
from .betraege import _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler, _frist, _text


def nachlass_aufgebotseinrede(annahme_erbschaft_am=None, nachlasspflegerbestellung_am=None,
    aufgebotsantrag_am=None, massgebliches_jahresfristende=None, antrag_zugelassen=None,
    verfahrensbeendigung_am=None, prueftag=None, erbe_haftet_unbeschraenkt=None,
    glaeubiger_nach_2016_ausgenommen=None, einordnungsnachweis=None):
    """Rechtzeitiger Antrag und Zulassung erhalten Einrede bis rechtlicher Verfahrensbeendigung."""
    tag = _datum(prueftag, 'prueftag')
    annahme = _datum(annahme_erbschaft_am, 'annahme_erbschaft_am') if annahme_erbschaft_am is not None else None
    pfleger = _datum(nachlasspflegerbestellung_am, 'nachlasspflegerbestellung_am') if nachlasspflegerbestellung_am is not None else None
    if annahme is None and pfleger is None:
        _fehler('annahme_erbschaft_am', 'Annahme oder vorherige Bestellung eines Verwaltungspflegers erforderlich.', 'EINGABE_FEHLT')
    antrag = _datum(aufgebotsantrag_am, 'aufgebotsantrag_am')
    ende = _datum(massgebliches_jahresfristende, 'massgebliches_jahresfristende')
    beendet = _datum(verfahrensbeendigung_am, 'verfahrensbeendigung_am') if verfahrensbeendigung_am is not None else None
    for name, datum in [('annahme_erbschaft_am', annahme), ('nachlasspflegerbestellung_am', pfleger),
        ('aufgebotsantrag_am', antrag), ('verfahrensbeendigung_am', beendet)]:
        if datum is not None and datum > tag:
            _fehler(name, 'Eingetragenes tatsächliches Ereignis darf nicht nach dem Prüftag liegen.')
    if beendet is not None and beendet < antrag:
        _fehler('verfahrensbeendigung_am', 'Beendigung desselben Verfahrens darf nicht vor seinem Antrag liegen.')
    beginn = min(d for d in (annahme, pfleger) if d is not None)
    grundende = _frist(beginn.isoformat(), 1, 'jahre', 'ereignis')
    if ende < grundende:
        _fehler('massgebliches_jahresfristende', 'Maßgebliches Jahresfristende darf die Grundfrist nicht verkürzen.')
    eingaben = dict(annahme_erbschaft_am=annahme_erbschaft_am, nachlasspflegerbestellung_am=nachlasspflegerbestellung_am,
        aufgebotsantrag_am=aufgebotsantrag_am, massgebliches_jahresfristende=massgebliches_jahresfristende,
        antrag_zugelassen=antrag_zugelassen, verfahrensbeendigung_am=verfahrensbeendigung_am, prueftag=prueftag,
        erbe_haftet_unbeschraenkt=erbe_haftet_unbeschraenkt,
        glaeubiger_nach_2016_ausgenommen=glaeubiger_nach_2016_ausgenommen, einordnungsnachweis=einordnungsnachweis)
    for name in ('antrag_zugelassen', 'erbe_haftet_unbeschraenkt', 'glaeubiger_nach_2016_ausgenommen'):
        _wahrheitswert(eingaben[name], name)
    _text(einordnungsnachweis, 'einordnungsnachweis')
    wert = None
    if antrag >= beginn:
        rechtzeitig = antrag <= ende
        wert = dict(fristbeginnereignis_am=beginn.isoformat(), rechnerisches_jahresfristende=grundende.isoformat(),
            aufgebotsantrag_rechtzeitig=rechtzeitig, verfahren_beendet=beendet is not None,
            verweigerungsrecht_am_prueftag=rechtzeitig and antrag_zugelassen and beendet is None
                and not erbe_haftet_unbeschraenkt and not glaeubiger_nach_2016_ausgenommen)
    ergebnis = _ergebnis(wert, 'daten_und_wahrheitswerte', 'BGB_NACHLASS_AUFGEBOTSEINREDE', eingaben,
        [dict(operation='Jahresfrist ab Annahme oder früherer Verwaltungspflegerbestellung für Antrag; bei Zulassung bis Verfahrensbeendigung unter gesetzlichen Ausschlüssen verweigern')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Tatsächliche Ereignisse bis Prüftag, rechtliche Verfahrensbeendigung und Gläubiger-/Haftungslage qualifiziert; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['Jahresfrist betrifft Antragstellung, nicht Zulassung oder Ende des Verfahrens; die Einrede kann bei rechtzeitigem Antrag über das Jahr hinaus dauern. Bei Ausschließungsbeschluss oder Zurückweisung gilt nach§2015 Absatz3 erst Rechtskraft als Beendigung, nicht bloßer Erlass. verfahrensbeendigung_am muss diese rechtlich bestimmte Grenze enthalten; NULL bedeutet bis Prüftag nicht beendet, auch wenn ein noch nicht rechtskräftiger Beschluss vorliegt. Zulassung ist zum Prüftag zu beurteilen. Frühere Bestellung eines Pflegers zur Nachlassverwaltung nach§2017 verschiebt den Start vor Annahme, spätere Bestellung startet kein neues Jahr. Anträge vor dem hier bestimmten Fristbeginn sind in diesem Modell gesondert offen und ergeben NICHT_ANWENDBAR, keine Aussage ihrer Unwirksamkeit. Maßgebliches Jahresende nur mit rechtlich zulässigen belegten Korrekturen, nicht frei verlängern. §2016 Absatz2/§1971 samt Einschränkung für erst nach Erbfall erworbene Vollstreckungs-/Arrestrechte und einstweilige Vormerkung qualifizieren. FALSE betrifft nur diese Einrede; keine automatische Ausübung und keine umfassende Forderungsprüfung.']
    return ergebnis
