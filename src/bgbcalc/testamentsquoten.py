"""Rechnerische Auslegungsregeln für testamentarische Erbquoten (§§2088–2092)."""
from .betraege import _wahrheitswert
from .kalender import _ergebnis, _fehler, _text, _vorhanden
from .zahlen import _addieren, _bruch, _dividieren, _multiplizieren, _subtrahieren, _zahleneingabe
from .zinsen import _bruchteile


def testament_erbquoten(erbeinsetzungen=None, alleinige_erben_gewollt=None,
    auslegungsregeln_anwendbar=None, einordnungsnachweis=None):
    """Unter-/Überbelegung und nicht bestimmte Anteile nach gesetzlichen Auslegungsregeln."""
    _vorhanden(erbeinsetzungen, 'erbeinsetzungen')
    if not isinstance(erbeinsetzungen, list) or not 1 <= len(erbeinsetzungen) <= 1000:
        _fehler('erbeinsetzungen', 'Liste mit 1 bis 1000 rechtlich bestimmten Erbeinsetzungen erforderlich.')
    namen, quoten = [], []
    summe = _bruch(0)
    for eintrag in erbeinsetzungen:
        if not isinstance(eintrag, dict) or set(eintrag) != {'erbe_id', 'bestimmter_erbteil'}:
            _fehler('erbeinsetzungen', 'Genau erbe_id und bestimmter_erbteil erforderlich.')
        name = _text(eintrag['erbe_id'], 'erbe_id')
        if name in namen:
            _fehler('erbe_id', 'Erben nicht doppelt aufführen; rechtlich zusammengefasste Einsetzung vorgeben.')
        quote = None
        if eintrag['bestimmter_erbteil'] is not None:
            quote = _zahleneingabe(eintrag['bestimmter_erbteil'])
            if not 0 < quote <= 1:
                _fehler('bestimmter_erbteil', 'Bestimmter Anteil muss positiv und höchstens eins sein.')
            summe = _addieren(summe, quote)
        namen.append(name)
        quoten.append(quote)
    unbekannt = quoten.count(None)
    if len(quoten) == 1 and unbekannt:
        _fehler('erbeinsetzungen', 'Ein einzelner Erbe ohne Bruchteilsbestimmung liegt außerhalb dieses Mehrerben-/Bruchteilsmodells.')
    _wahrheitswert(alleinige_erben_gewollt, 'alleinige_erben_gewollt')
    _wahrheitswert(auslegungsregeln_anwendbar, 'auslegungsregeln_anwendbar')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    eingaben = dict(erbeinsetzungen=erbeinsetzungen, alleinige_erben_gewollt=alleinige_erben_gewollt,
        auslegungsregeln_anwendbar=auslegungsregeln_anwendbar, einordnungsnachweis=einordnungsnachweis)
    wert = None
    if auslegungsregeln_anwendbar:
        rest = _bruch(0)
        if unbekannt == 0:
            if summe > 1 or (summe < 1 and alleinige_erben_gewollt):
                quoten = [_dividieren(q, summe) for q in quoten]
            else:
                rest = _subtrahieren(_bruch(1), summe)
        elif summe < 1:
            unbestimmter_anteil = _dividieren(_subtrahieren(_bruch(1), summe), _bruch(unbekannt))
            quoten = [unbestimmter_anteil if q is None else q for q in quoten]
        else:
            kleinster = min(q for q in quoten if q is not None)
            gesamtgewicht = _addieren(summe, _multiplizieren(kleinster, _bruch(unbekannt)))
            quoten = [_dividieren(kleinster if q is None else q, gesamtgewicht) for q in quoten]
        wert = dict(erbquoten=[dict(erbe_id=n, erbquote=_bruchteile(q)) for n, q in zip(namen, quoten)],
            rest_gesetzliche_erbfolge=_bruchteile(rest))
    ergebnis = _ergebnis(wert, 'erbquoten', 'BGB_TESTAMENT_ERBQUOTEN', eingaben,
        [dict(operation='Bestimmte Quoten verhältnismäßig anpassen oder gesetzlichen Rest belassen; unbestimmte Quoten aus freiem Rest beziehungsweise kleinstem bestimmten Ausgangsanteil bilden')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Wirksame Erbeinsetzungen und anwendbare gesetzliche Auslegungsregeln rechtlich bestimmt; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['NULL bei bestimmter_erbteil bedeutet vom Erblasser nicht bestimmt, nicht unbekannte Aktenlage. Abweichender Wille, Sonderauslegung§§2066–2069, Erbeinsetzung versus Vermächtnis§2087, Wegfall/Ersatzerben und Wirksamkeit vorab prüfen. Alleinige-Erben-Wille beeinflusst Unterbelegung ausschließlich bestimmter Quoten; bei nicht bestimmten Quoten gelten§§2091/2092. Bei erschöpfter oder überbelegter Masse erhalten unbestimmt Bedachte das Gewicht des kleinsten bestimmten Ausgangsanteils; anschließend alle Gewichte gemeinsam normieren. Keine nachträgliche Halbierung bereits normierter Quoten. Gemeinschaftlicher Erbteil§2093 und Anwachsung§2094 nicht automatisch aufgelöst; hier flache Personenliste ohne solche Gruppen. Gesetzlicher Rest wird ausgewiesen, aber nicht auf gesetzliche Erben verteilt. Eine einzelne Einsetzung ohne Bruchteilsbestimmung außerhalb dieses Modells.']
    return ergebnis
