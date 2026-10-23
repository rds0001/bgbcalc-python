"""Rekursive gemeinschaftliche Erb-/Vermächtnisquoten (§§2093,2157)."""
from .betraege import _wahrheitswert
from .kalender import _auswahl, _ergebnis, _fehler, _text, _vorhanden
from .testamentsquoten import testament_erbquoten
from .zahlen import _multiplizieren, _zahleneingabe
from .zinsen import _bruchteile


def gemeinschaftsquoten_aufloesen(gemeinschaftlicher_anteil=None, gruppenmitglieder=None,
    regelkontext=None, gruppeneinsetzung_qualifiziert=None, einordnungsnachweis=None):
    """Gruppen intern normalisieren und relative Quoten über sämtliche Ebenen multiplizieren."""
    oberquote = _zahleneingabe(gemeinschaftlicher_anteil)
    if not 0 < oberquote <= 1:
        _fehler('gemeinschaftlicher_anteil', 'Positive bereits bestimmte Oberquote höchstens eins erforderlich.')
    _vorhanden(gruppenmitglieder, 'gruppenmitglieder')
    _auswahl(regelkontext, 'regelkontext', ('gemeinschaftlicher_erbteil_2093', 'gemeinschaftliches_vermaechtnis_2157'))
    _wahrheitswert(gruppeneinsetzung_qualifiziert, 'gruppeneinsetzung_qualifiziert')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    namen = set()
    blaetter = []
    def verteilen(mitglieder, faktor, tiefe):
        if tiefe > 20:
            _fehler('gruppenmitglieder', 'Höchstens20 verschachtelte Gruppenebenen.')
        if not isinstance(mitglieder, list) or not 2 <= len(mitglieder) <= 1000:
            _fehler('gruppenmitglieder', 'Je Gemeinschaft2..1000 Mitglieder erforderlich.')
        einsetzungen = []
        for m in mitglieder:
            if not isinstance(m, dict) or set(m) != {'knoten_id', 'bestimmter_anteil', 'untergruppe'}:
                _fehler('gruppenmitglieder', 'Genau knoten_id, bestimmter_anteil, untergruppe erforderlich.')
            name = _text(m['knoten_id'], 'knoten_id')
            if name in namen:
                _fehler('knoten_id', 'Alle Gruppen-/Personenkennungen global eindeutig; keine Zyklen oder Doppelpersonen.')
            namen.add(name)
            if len(namen) > 1000:
                _fehler('gruppenmitglieder', 'Insgesamt höchstens1000 Gruppen-/Personenknoten.')
            einsetzungen.append(dict(erbe_id=name, bestimmter_erbteil=m['bestimmter_anteil']))
        quoten = testament_erbquoten(einsetzungen, True, True, einordnungsnachweis)['wert']['erbquoten']
        for m, q in zip(mitglieder, quoten):
            absolut = _multiplizieren(faktor, _zahleneingabe(q['erbquote']))
            if m['untergruppe'] is None:
                blaetter.append(dict(person_id=m['knoten_id'], anteil=_bruchteile(absolut)))
            else:
                verteilen(m['untergruppe'], absolut, tiefe + 1)
    verteilen(gruppenmitglieder, oberquote, 1)
    eingaben = dict(gemeinschaftlicher_anteil=gemeinschaftlicher_anteil, gruppenmitglieder=gruppenmitglieder,
        regelkontext=regelkontext, gruppeneinsetzung_qualifiziert=gruppeneinsetzung_qualifiziert, einordnungsnachweis=einordnungsnachweis)
    wert = dict(aufgeloeste_anteile=blaetter) if gruppeneinsetzung_qualifiziert else None
    ergebnis = _ergebnis(wert, 'quoten', 'BGB_GEMEINSCHAFTSQUOTEN_AUFLOESEN', eingaben,
        [dict(operation='Je Gruppe vorhandenen2089–2092-Quotenkern anwenden; normierte Binnenquote mit allen Oberquoten multiplizieren')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Rechtlich qualifizierte gemeinschaftliche Einsetzung auf eine bereits bestimmte Oberquote; angegebene Mitglieder bilden jeweils die vollständige Gemeinschaft.']
    ergebnis['hinweise'] = ['Bestimmte Anteile sind relativ zur jeweiligen unmittelbaren Gemeinschaft, nicht bereits absolute Gesamtquoten. NULL bedeutet testamentarisch unbestimmt, nicht unklare Aktenlage. Untergruppe NULL bezeichnet eine Person, sonst deren Untergemeinschaft. Innerhalb vollständiger Gruppe Unter-/Überbelegung nach2089–2092 normalisieren; kein zusätzlicher gesetzlicher Rest innerhalb dieses Gruppenmodells. Oberquote nach vorgelagerter Erbeinsetzungs-/Vermächtnisprüfung bestimmen.2157 betrifft mehrere Bedachte desselben Gegenstands; keine Pflicht zur Teilung unteilbarer Sachen oder2151-Gesamtgläubigerquotierung. Wegfälle/Anwachsung/Ersatzerben und Sonderanteile vorher rechtlich gesondert behandeln; keine gleiche Person in mehreren Zweigen, dafür rechtlich getrennte Anteilstitel separat rechnen.']
    return ergebnis
