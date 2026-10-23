"""Dreimonatseinrede des Erben mit Inventar- und Haftungsausschlüssen (§§2014/2016/2017)."""
from .betraege import _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler, _frist, _text


def nachlass_dreimonatseinrede(annahme_erbschaft_am=None, nachlasspflegerbestellung_am=None,
    inventarerrichtung_am=None, prueftag=None, erbe_haftet_unbeschraenkt=None,
    glaeubiger_nach_2016_ausgenommen=None, einordnungsnachweis=None):
    """Drei Monate ab Annahme oder früherer Verwaltungspflegerbestellung, spätestens bis Inventar."""
    tag = _datum(prueftag, 'prueftag')
    annahme = _datum(annahme_erbschaft_am, 'annahme_erbschaft_am') if annahme_erbschaft_am is not None else None
    pfleger = _datum(nachlasspflegerbestellung_am, 'nachlasspflegerbestellung_am') if nachlasspflegerbestellung_am is not None else None
    if annahme is None and pfleger is None:
        _fehler('annahme_erbschaft_am', 'Annahme oder vorherige Bestellung eines Verwaltungspflegers erforderlich.', 'EINGABE_FEHLT')
    for name, datum in [('annahme_erbschaft_am', annahme), ('nachlasspflegerbestellung_am', pfleger)]:
        if datum is not None and datum > tag:
            _fehler(name, 'Eingetragenes Ereignis darf nicht nach dem Prüftag liegen; noch nicht eingetretenes Ereignis als NULL angeben.')
    beginn = min(d for d in (annahme, pfleger) if d is not None)
    ende = _frist(beginn.isoformat(), 3, 'monate', 'ereignis')
    inventar = None
    if inventarerrichtung_am is not None:
        inventar = _datum(inventarerrichtung_am, 'inventarerrichtung_am')
        if inventar > tag:
            _fehler('inventarerrichtung_am', 'Inventarerrichtung darf nicht nach dem Prüftag liegen.')
    _wahrheitswert(erbe_haftet_unbeschraenkt, 'erbe_haftet_unbeschraenkt')
    _wahrheitswert(glaeubiger_nach_2016_ausgenommen, 'glaeubiger_nach_2016_ausgenommen')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    eingaben = dict(annahme_erbschaft_am=annahme_erbschaft_am, nachlasspflegerbestellung_am=nachlasspflegerbestellung_am,
        inventarerrichtung_am=inventarerrichtung_am, prueftag=prueftag,
        erbe_haftet_unbeschraenkt=erbe_haftet_unbeschraenkt,
        glaeubiger_nach_2016_ausgenommen=glaeubiger_nach_2016_ausgenommen, einordnungsnachweis=einordnungsnachweis)
    wert = dict(fristbeginnereignis_am=beginn.isoformat(), dreimonatsfristende=ende.isoformat(),
        inventar_beendet_einrede=inventar is not None,
        verweigerungsrecht_am_prueftag=(tag <= ende and inventar is None and not erbe_haftet_unbeschraenkt
            and not glaeubiger_nach_2016_ausgenommen))
    ergebnis = _ergebnis(wert, 'daten_und_wahrheitswerte', 'BGB_NACHLASS_DREIMONATSEINREDE', eingaben,
        [dict(operation='Drei Monate ab Annahme beziehungsweise früherer Verwaltungspflegerbestellung; Inventarerrichtung und gesetzliche Haftungs-/Gläubigerausnahmen schließen Einrede aus')], eingaben.copy())
    ergebnis['annahmen'] = ['Prüfung zum Ende des Prüftags; wirksame Annahme, Bestellung und Inventarerrichtung sowie Haftung/Gläubigereinordnung rechtlich bestimmt; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['Nachlasspflegerbestellung nur zur Verwaltung des Nachlasses im Sinne§2017, nicht beliebige Betreuung oder spätere Beauftragung. Frühere Bestellung startet Frist auch vor Annahme; spätere Bestellung startet keine neue Frist. NULL bei Annahme/Bestellung/Inventar bedeutet Ereignis bis Prüftag nicht eingetreten, nicht unbekannt. Inventarerrichtung beendet Einrede bereits ab diesem Ereignis, nicht erst nach einem zusätzlich gewährten Tag; taggenau zum Tagesende geprüft. §2016 Absatz2: Gläubigerausnahme§1971 einschließlich Einschränkung für erst nach Erbfall durch Vollstreckung/Arrest erworbene Rechte beziehungsweise einstweilig erworbene Vormerkung qualifizieren. Keine pauschale Gleichsetzung jedes gesicherten Gläubigers mit Ausnahme. FALSE betrifft nur§2014, nicht andere Einreden oder die Anspruchsexistenz. Keine automatische Ausübung der Einrede oder Fristverschiebung wegen Wochenende/Feiertag; keine drei Monate ab Erbfall ohne Annahme/Bestellung.']
    return ergebnis
