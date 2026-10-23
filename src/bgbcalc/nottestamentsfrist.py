"""Kalenderteilmodelle der Nottestamentsfrist (§2252)."""
from .betraege import _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler, _frist, _text


def nottestament_grundfrist(errichtung_am=None, einordnungsnachweis=None):
    """Rohe Dreimonatsfrist ab Errichtung; keine Hemmungs- oder Gültigkeitsprüfung."""
    beginn = _datum(errichtung_am, 'errichtung_am')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    ende = _frist(beginn.isoformat(), 3, 'monate', 'ereignis')
    eingaben = dict(errichtung_am=errichtung_am, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(ende.isoformat(), 'datum', 'BGB_NOTTESTAMENT_GRUNDFRIST', eingaben,
        [dict(operation='Drei Kalendermonate ab Errichtung als Ereignisfrist')], eingaben.copy())
    ergebnis['annahmen'] = ['Nach2249/2250/2251 errichtetes Nottestament rechtlich qualifiziert; rohe Grundfrist nach2252I.']
    ergebnis['hinweise'] = ['Beginn und Lauf sind nach2252II gehemmt, solange notarielle Testamentserrichtung unmöglich ist; dieses Grundfristende daher nicht ungeprüft als tatsächlichen Ablauf verwenden. Neue Seereise2252III kann unterbrechen. Rechtsfolge2252I setzt Fortleben nach Ablauf voraus; Todeserklärung/Todeszeitfeststellung2252IV gesondert prüfen. Keine automatische Unwirksamkeitsfeststellung oder Wochenend-/Feiertagsverlängerung.']
    return ergebnis


def seetestament_reise_neustart(bisheriges_fristende=None, neue_seereise_beginn=None,
    neue_seereise_ende=None, seetestament_nach_2251_qualifiziert=None, einordnungsnachweis=None):
    """Neue volle Dreimonatsgrundfrist nach rechtzeitig angetretener neuer Seereise."""
    bisher = _datum(bisheriges_fristende, 'bisheriges_fristende')
    beginn = _datum(neue_seereise_beginn, 'neue_seereise_beginn')
    ende = _datum(neue_seereise_ende, 'neue_seereise_ende')
    if ende < beginn:
        _fehler('neue_seereise_ende', 'Reiseende darf nicht vor Reisebeginn liegen.')
    _wahrheitswert(seetestament_nach_2251_qualifiziert, 'seetestament_nach_2251_qualifiziert')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    eingaben = dict(bisheriges_fristende=bisheriges_fristende, neue_seereise_beginn=neue_seereise_beginn,
        neue_seereise_ende=neue_seereise_ende, seetestament_nach_2251_qualifiziert=seetestament_nach_2251_qualifiziert,
        einordnungsnachweis=einordnungsnachweis)
    wert = None
    if seetestament_nach_2251_qualifiziert and beginn <= bisher:
        wert = _frist(ende.isoformat(), 3, 'monate', 'ereignis').isoformat()
    ergebnis = _ergebnis(wert, 'datum', 'BGB_SEETESTAMENT_REISE_NEUSTART', eingaben,
        [dict(operation='Reiseantritt vor Ablauf des bisherigen Fristtages prüfen; bei rechtzeitigem Antritt volle drei Monate ab Ende der neuen Reise')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Qualifizierter2251-Fall; bisheriges Fristende einschließlich rechtlich einschlägiger Hemmung/Unterbrechung vollständig bestimmt.']
    ergebnis['hinweise'] = ['Reiseantritt am bisherigen letzten Fristtag erfolgt vor dessen Tagesablauf; späterer Antritt belebt Frist nicht wieder. Ergebnis ist rohe volle neue Grundfrist nach Reiseende, keine bloße Addition der Reisedauer oder Restfrist. Weitere Unmöglichkeit notarieller Errichtung2252II und erneute Reisen gesondert berücksichtigen. Nicht2251-Fälle oder verspäteter Antritt ergeben NICHT_ANWENDBAR. Keine Gültigkeitsentscheidung bei Tod/Todeserklärung2252I/IV.']
    return ergebnis
