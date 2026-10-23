"""Erlöschensfrist für Verwendungsersatz nach Herausgabe (§1002)."""
from .betraege import _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler, _frist, _text


def verwendungsersatz_erloeschensfrist(
    herausgabe_am=None, grundstueck=None, massgebliches_fristende=None, prueftag=None,
    gerichtliche_geltendmachung_am=None, genehmigung_verwendungen_am=None,
    anspruch_unterliegt_1002=None, einordnungsnachweis=None,
):
    """Ein-/Sechsmonatsgrenze und rechtzeitige gerichtliche Geltendmachung/Genehmigung."""
    herausgabe = _datum(herausgabe_am, 'herausgabe_am')
    _wahrheitswert(grundstueck, 'grundstueck')
    ende = _datum(massgebliches_fristende, 'massgebliches_fristende')
    tag = _datum(prueftag, 'prueftag')
    grundende = _frist(herausgabe_am, 6 if grundstueck else 1, 'monate', 'ereignis')
    if ende < grundende:
        _fehler('massgebliches_fristende', 'Maßgebliches Fristende darf die gesetzliche Grundfrist nicht verkürzen.')
    if tag < herausgabe:
        _fehler('prueftag', 'Prüftag darf nicht vor Herausgabe liegen.')
    eingaben = dict(herausgabe_am=herausgabe_am, grundstueck=grundstueck,
        massgebliches_fristende=massgebliches_fristende, prueftag=prueftag,
        gerichtliche_geltendmachung_am=gerichtliche_geltendmachung_am,
        genehmigung_verwendungen_am=genehmigung_verwendungen_am,
        anspruch_unterliegt_1002=anspruch_unterliegt_1002, einordnungsnachweis=einordnungsnachweis)
    rechtzeitig = []
    for name in ('gerichtliche_geltendmachung_am', 'genehmigung_verwendungen_am'):
        datum = _datum(eingaben[name], name) if eingaben[name] is not None else None
        if datum is not None and datum > tag:
            _fehler(name, 'Erhaltendes Ereignis darf nicht nach dem Prüftag liegen.')
        rechtzeitig.append(datum is not None and datum <= ende)
    _wahrheitswert(anspruch_unterliegt_1002, 'anspruch_unterliegt_1002')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    wert = dict(rechnerisches_fristende=grundende.isoformat(),
        gerichtliche_geltendmachung_rechtzeitig=rechtzeitig[0],
        genehmigung_rechtzeitig=rechtzeitig[1],
        anspruch_nach_1002_erloschen=tag > ende and not any(rechtzeitig)) if anspruch_unterliegt_1002 else None
    ergebnis = _ergebnis(wert, 'daten_und_wahrheitswerte', 'BGB_VERWENDUNGSERSATZ_ERLOESCHENSFRIST', eingaben,
        [dict(operation='Ab Herausgabe ein Monat, bei Grundstück sechs Monate; qualifiziertes Fristende und rechtzeitige gerichtliche Geltendmachung oder Genehmigung prüfen')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Herausgabe an Eigentümer und Anwendungsbereich rechtlich bestimmt; maßgebliches Ende einschließlich zulässiger Korrekturen vorgegeben; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['§1002 Absatz2 verweist auf§§206/210/211: entsprechende Hemmungs-/Ablaufhemmungswirkungen gesondert berechnen und im maßgeblichen Ende belegen; keine frei gewählte Verlängerung. Gerichtliche Geltendmachung muss rechtlich wirksam und diesem Anspruch zugeordnet sein; bloße Mahnung oder außergerichtliche Zahlungsaufforderung genügt nicht. Genehmigung betrifft die Verwendungen durch Eigentümer, nicht eine beliebige Erklärung. NULL bei Ereignisdaten bedeutet bis Prüftag nicht eingetreten, nicht unbekannt. Auch Ereignisse vor Herausgabe können erhalten; spätere Ereignisse nach Fristende beseitigen das hier berechnete Erlöschen nicht automatisch. Erneute Anspruchsbegründung und andere Ansprüche gesondert. FALSE bestätigt weder Anspruchsgrund noch Betrag oder Fälligkeit§1001. Taggenau, Ereignisse am letzten Tag bis Fristablauf rechtzeitig; untertägige Reihenfolge vorab einordnen.']
    return ergebnis
