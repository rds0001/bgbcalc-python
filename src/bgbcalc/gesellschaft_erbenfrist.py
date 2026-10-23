from .betraege import _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler, _frist, _text

def gesellschaft_erbenrechtsfrist(erbschaftskenntnis_am=None, ablaufhemmung_mindestende_am=None, ausschlagungsrecht_bei_dreimonatsablauf_noch_offen=None, ausschlagungsfristende_am=None, einordnungsnachweis=None):
    """Dreimonatsgrundfrist mit wirksamer210-Ablaufhemmung und noch offener Ausschlagungsfrist als spätestes Ende verknüpfen."""
    grund = _frist(erbschaftskenntnis_am,3,'monate','ereignis');ende = grund
    _wahrheitswert(ausschlagungsrecht_bei_dreimonatsablauf_noch_offen,'ausschlagungsrecht_bei_dreimonatsablauf_noch_offen')
    _text(einordnungsnachweis,'einordnungsnachweis')
    if ablaufhemmung_mindestende_am is not None:
        ende = max(ende,_datum(ablaufhemmung_mindestende_am,'ablaufhemmung_mindestende_am'))
    if ausschlagungsrecht_bei_dreimonatsablauf_noch_offen:
        ausschlagung = _datum(ausschlagungsfristende_am,'ausschlagungsfristende_am')
        if ausschlagung < grund:
            _fehler('ausschlagungsfristende_am','Offene Ausschlagungsfrist darf nicht bereits vor der Dreimonatsgrundgrenze enden.')
        ende = max(ende,ausschlagung)
    elif ausschlagungsfristende_am is not None:
        _fehler('ausschlagungsfristende_am','Ohne noch bestehendes Ausschlagungsrecht Zusatzende ausdrücklich null.')
    wert = dict(dreimonatsgrundfristende=grund.isoformat(),rechnerisches_ausuebungsfristende=ende.isoformat())
    eingaben = dict(erbschaftskenntnis_am=erbschaftskenntnis_am, ablaufhemmung_mindestende_am=ablaufhemmung_mindestende_am, ausschlagungsrecht_bei_dreimonatsablauf_noch_offen=ausschlagungsrecht_bei_dreimonatsablauf_noch_offen, ausschlagungsfristende_am=ausschlagungsfristende_am, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'daten','BGB_GESELLSCHAFT_ERBENRECHTSFRIST',eingaben,[dict(operation='Dreimonatsgrundfrist mit wirksamer210-Ablaufhemmung und noch offener Ausschlagungsfrist als spätestes Ende verknüpfen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§724III: Drei Monate ab Kenntnis des Erbschaftsanfalls, entsprechend210 bestimmtes Mindestende und gegebenenfalls späteres Ausschlagungsfristende als Maximum. Ob das Ausschlagungsrecht bei Ablauf der Dreimonatsgrundfrist noch besteht, separat rechtlich vorqualifizieren, nicht allein aus einem theoretischen Datum folgern.210-Mindestende mit vorhandener Ablaufhemmungsfunktion berechnen: die maßgebliche Frist beträgt drei Monate, daher210-Nachlauf grundsätzlich entsprechend kürzer als sechs Monate. Offene/ungeklärte Schutzereignisse nicht durch fiktives Enddatum oder null ersetzen. Keine automatische Annahme/Ausschlagung, Kommanditistenstellung, Kündigungswirksamkeit oder Haftungsbeschränkung nachAbsatz4. Keine pauschale Feiertagsverschiebung; gegebenenfalls weitere rechtliche Kalenderkorrektur separat.']
    return ergebnis

