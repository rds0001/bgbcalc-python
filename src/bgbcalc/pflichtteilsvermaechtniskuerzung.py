"""Proportionale Pflichtteilslast und isolierte Schutzgrenzen (§2318/2323)."""
from .betraege import _geld, _wahrheitswert
from .kalender import _auswahl, _ergebnis, _fehler, _text
from .zahlen import _bruch, _dividieren, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile


def vermaechtnis_pflichtteilskuerzung(erwerbswert_vor_vermaechtnis=None, vermaechtniswert=None,
    gesamte_pflichtteilslast=None, anderweitig_getragene_last_2323=None, schutzart=None,
    geschuetzter_pflichtteilswert=None, einzelfall_nach_2318_qualifiziert=None, bewertungsnachweis=None):
    """Einzelvermächtnis proportional kürzen, wahlweise nur einen Pflichtteilsschutz berücksichtigen."""
    erwerb = _geld(erwerbswert_vor_vermaechtnis)
    vermaechtnis = _geld(vermaechtniswert)
    gesamt = _geld(gesamte_pflichtteilslast)
    fremd = _geld(anderweitig_getragene_last_2323)
    schutz = _geld(geschuetzter_pflichtteilswert)
    _auswahl(schutzart, 'schutzart', ('kein_schutz', 'vermaechtnisnehmer', 'erbe'))
    if vermaechtnis > erwerb or gesamt > erwerb:
        _fehler('erwerbswert_vor_vermaechtnis', 'Vermächtnis und gesamte Pflichtteilslast jeweils höchstens Erwerbswert; sonst vorgelagerte Haftungsfragen klären.')
    if fremd > gesamt:
        _fehler('anderweitig_getragene_last_2323', 'Anderweitig getragene Last höchstens gesamte Pflichtteilslast.')
    if schutzart == 'kein_schutz' and schutz != 0:
        _fehler('geschuetzter_pflichtteilswert', 'Ohne Schutzfall Pflichtteilswert null erforderlich.')
    if schutzart == 'erbe' and schutz > _subtrahieren(erwerb, vermaechtnis):
        _fehler('geschuetzter_pflichtteilswert', 'Eigener Pflichtteil muss vor dieser Pflichtteilslast bereits gedeckt sein; sonst vorgelagerte andere Rechte klären.')
    _wahrheitswert(einzelfall_nach_2318_qualifiziert, 'einzelfall_nach_2318_qualifiziert')
    _text(bewertungsnachweis, 'bewertungsnachweis')
    eingaben = dict(erwerbswert_vor_vermaechtnis=erwerbswert_vor_vermaechtnis, vermaechtniswert=vermaechtniswert,
        gesamte_pflichtteilslast=gesamte_pflichtteilslast, anderweitig_getragene_last_2323=anderweitig_getragene_last_2323,
        schutzart=schutzart, geschuetzter_pflichtteilswert=geschuetzter_pflichtteilswert,
        einzelfall_nach_2318_qualifiziert=einzelfall_nach_2318_qualifiziert, bewertungsnachweis=bewertungsnachweis)
    wert = None
    if einzelfall_nach_2318_qualifiziert:
        last = _subtrahieren(gesamt, fremd)
        proportional = _multiplizieren(last, _dividieren(vermaechtnis, erwerb)) if erwerb else _bruch(0)
        kuerzung = proportional
        if schutzart == 'vermaechtnisnehmer':
            kuerzung = min(kuerzung, max(_subtrahieren(vermaechtnis, schutz), _bruch(0)))
        elif schutzart == 'erbe':
            rest = _subtrahieren(_subtrahieren(erwerb, vermaechtnis), last)
            kuerzung = max(kuerzung, min(vermaechtnis, max(_subtrahieren(schutz, rest), _bruch(0))))
        wert = dict(anteilige_grundkuerzung=_bruchteile(proportional), kuerzungsbetrag=_bruchteile(kuerzung),
            verbleibender_vermaechtniswert=_bruchteile(_subtrahieren(vermaechtnis, kuerzung)),
            beim_erben_verbleibende_pflichtteilslast=_bruchteile(_subtrahieren(last, kuerzung)))
    ergebnis = _ergebnis(wert, 'EUR', 'BGB_VERMAECHTNIS_PFLICHTTEILSKUERZUNG', eingaben,
        [dict(operation='Nach2323 selbst zu tragende Last mit Vermächtnis/Erwerb quotieren; isolierten Schutz2318II oderIII berücksichtigen')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Ein Erbe, ein bewertetes Vermächtnis beziehungsweise eine Auflage; keine weiteren Beschwerungen, Vorränge oder gleichzeitigen Schutzrechte beider Beteiligter.']
    ergebnis['hinweise'] = ['Erwerbswert nach sonstigen berücksichtigungsfähigen Verbindlichkeiten, aber vor diesem Vermächtnis und Pflichtteilslast.2323: rechtlich nach2320–2322 anderweitig getragene Last zuerst abziehen. Kein Schutzfall: proportionale Lastverteilung. Nur Vermächtnisnehmer geschützt: Kürzung höchstens positiver Vermächtnisüberschuss über dessen Pflichtteil; ein schon vorher unzureichendes Vermächtnis erzeugt hier keinen zusätzlichen Anspruch. Nur Erbe geschützt: Kürzung zusätzlich bis Erhalt des eigenen Pflichtteils, begrenzt auf Vermächtniswert; eigener Pflichtteil muss vor hinzutretender Pflichtteilslast bereits gedeckt sein. Beide Beteiligten pflichtteilsberechtigt, mehrere Vermächtnisse, Vorränge2189 oder abweichende Anordnungen2324 brauchen gesondertes kombiniertes Modell und dürfen nicht als einer dieser Fälle eingegeben werden. Keine Sachvermächtnis-Geldzahlungsautomatik.']
    return ergebnis
