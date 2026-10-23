"""2055/2056/2057a bei getrennten Zuwendungs- und Leistungsempfängern."""
from .gemischter_erbausgleich import erbteilung_gemischter_ausgleich
from .erbausgleich import erb_zuwendungen_ausgleichen
from .betraege import _geld, _wahrheitswert
from .kalender import _ergebnis
from .zahlen import _addieren, _bruch, _subtrahieren, _zahleneingabe
from .zinsen import _bruchteile


def erbteilung_getrennter_zuwendungs_leistungsausgleich(gruppennachlass=None, miterben=None,
    getrennte_empfaenger_und_reihenfolge_qualifiziert=None, rechts_und_bewertungsnachweis=None):
    """Leistungsvorwegabzug, vorhandene2056-Ausscheidung ausschließlich Nichtleistender, Leistungszuschlag."""
    _wahrheitswert(getrennte_empfaenger_und_reihenfolge_qualifiziert, 'getrennte_empfaenger_und_reihenfolge_qualifiziert')
    erbteilung_gemischter_ausgleich(gruppennachlass, miterben, True, rechts_und_bewertungsnachweis)
    leistungen = [_geld(p['leistungs_ausgleichsbetrag']) for p in miterben]
    summe = _bruch(0)
    liste = []
    ueberschneidung = False
    for p,l in zip(miterben,leistungen):
        q = _zahleneingabe(p['relative_erbquote'])
        summe = _addieren(summe,l)
        ueberschneidung = ueberschneidung or (l > 0 and _geld(p['ausgleichungswert_zuwendungen']) > 0)
        liste.append(dict(person_id=p['person_id'], erbquote_zaehler=q.numerator, erbquote_nenner=q.denominator, ausgleichungswert=p['ausgleichungswert_zuwendungen']))
    rest = _subtrahieren(_geld(gruppennachlass),summe)
    wert = None
    if getrennte_empfaenger_und_reihenfolge_qualifiziert and not ueberschneidung:
        kern = erb_zuwendungen_ausgleichen(_bruchteile(rest),liste,True,rechts_und_bewertungsnachweis)['wert']
        wert = dict(restnachlass_nach_leistungsvorwegabzug=_bruchteile(rest), ausser_ansatz=kern['ausser_ansatz'], zuteilungen=[dict(person_id=p['person_id'], erbteil_nach_gemischtem_ausgleich=_bruchteile(_addieren(_geld(p['betrag']),l))) for p,l in zip(kern['verteilung'],leistungen)])
    eingaben = dict(gruppennachlass=gruppennachlass,miterben=miterben,getrennte_empfaenger_und_reihenfolge_qualifiziert=getrennte_empfaenger_und_reihenfolge_qualifiziert,rechts_und_bewertungsnachweis=rechts_und_bewertungsnachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_ERBTEILUNG_GETRENNTER_ZUWENDUNGS_LEISTUNGSAUSGLEICH',eingaben,[dict(operation='Leistungssumme vorweg abziehen; bestehende2055/2056-Rechnung auf Rest; individuelleLeistung hinzufügen, nur getrennteEmpfängerkreise')],eingaben.copy())
    ergebnis['status']='BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen']=['Vollständige gleiche Ausgleichungsgruppe, getrennte Zuwendungs-/Leistungsempfänger und konkrete Vorwegabzugsreihenfolge fachlich qualifiziert.']
    ergebnis['hinweise']=['Positive Zuwendung und positive Leistung bei derselben Person ergeben NICHT_ANWENDBAR. Somit keine Ausscheidung eines zugleich Leistenden; deren rechtliche Kombination bleibt offen. Nichtleistende Überempfänger werden mit vorhandener2056-Iteration ausgeschlossen, ohne Rückzahlung. Bereits billig bemessene2057a-Beträge einschließlich Ausschlussgründe und Vergleichsgruppe vorgeben; SummeLeistungen höchstens Gruppennachlass. Keine zusätzliche2315-Anrechnung oder Pflichtteilsergänzung.']
    return ergebnis
