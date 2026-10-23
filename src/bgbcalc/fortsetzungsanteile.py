"""Rechnerische Grundanteile nach fortgesetzter Gütergemeinschaft."""
from .betraege import _geld
from .kalender import _ergebnis, _fehler, _text, _vorhanden
from .zahlen import _addieren, _bruch, _dividieren, _multiplizieren, _zahleneingabe
from .zinsen import _bruchteile


def fortgesetzte_guetergemeinschaft_grundanteile(teilungswert_gesamtgut=None, abkoemmlinge=None, quotennachweis=None):
    """§1503I: Abkömmlingshälfte nach relativen hypothetischen Erbquoten verteilen;§1505 Wertbasis halbieren."""
    gut = _geld(teilungswert_gesamtgut)
    _vorhanden(abkoemmlinge, 'abkoemmlinge')
    if not isinstance(abkoemmlinge, list) or not 1 <= len(abkoemmlinge) <= 1000:
        _fehler('abkoemmlinge', 'Liste mit 1 bis 1000 qualifizierten anteilsberechtigten Abkömmlingen erforderlich.')
    namen, quoten = [], []
    summe = _bruch(0)
    for eintrag in abkoemmlinge:
        if not isinstance(eintrag, dict) or set(eintrag) != {'abkoemmling_id', 'hypothetischer_erbteil'}:
            _fehler('abkoemmlinge', 'Genau abkoemmling_id und hypothetischer_erbteil erforderlich.')
        name = _text(eintrag['abkoemmling_id'], 'abkoemmling_id')
        if name in namen:
            _fehler('abkoemmling_id', 'Abkömmling nicht mehrfach aufführen.')
        _vorhanden(eintrag['hypothetischer_erbteil'], 'hypothetischer_erbteil')
        quote = _zahleneingabe(eintrag['hypothetischer_erbteil'])
        if not 0 < quote <= 1:
            _fehler('hypothetischer_erbteil', 'Qualifizierter Erbteil muss positiv und höchstens eins sein.')
        namen.append(name); quoten.append(quote)
        summe = _addieren(summe, quote)
    if summe > 1:
        _fehler('abkoemmlinge', 'Hypothetische gesetzliche Erbteile dürfen zusammen eins nicht überschreiten.')
    _text(quotennachweis, 'quotennachweis')
    haelfte = _dividieren(gut, _bruch(2))
    anteile = []
    for name,quote in zip(namen,quoten):
        relativ = _dividieren(quote,summe)
        gesamtquote = _dividieren(relativ,_bruch(2))
        wert = _multiplizieren(haelfte,relativ)
        anteile.append(dict(abkoemmling_id=name,anteil_abkoemmlingshaelfte=_bruchteile(relativ),anteil_gesamtgut=_bruchteile(gesamtquote),grundanteilswert=_bruchteile(wert),pflichtteilswertbasis=_bruchteile(_dividieren(wert,_bruch(2)))))
    eingaben = dict(teilungswert_gesamtgut=teilungswert_gesamtgut,abkoemmlinge=abkoemmlinge,quotennachweis=quotennachweis)
    ergebnis = _ergebnis(dict(ehegattenhaelfte=_bruchteile(haelfte),abkoemmlingshaelfte=_bruchteile(haelfte),abkoemmlingsanteile=anteile),'EUR','BGB_FORTGESETZTE_GUETERGEMEINSCHAFT_GRUNDANTEILE',eingaben,[dict(operation='Gesamtgutswert halbieren; Abkömmlingshälfte nach relativ normalisierten hypothetischen gesetzlichen Erbteilen verteilen; jeweilige Pflichtteilswertbasis nochmals halbieren.')],eingaben.copy())
    ergebnis['hinweise'] = ['Grundanteile nach§1503I und reine Wertbasis nach§1505. Vollständiger qualifizierter Kreis anteilsberechtigter Abkömmlinge; hypothetische gesetzliche Erbfolge beim gedachten Tod des verstorbenen Ehegatten erst zur Beendigung der fortgesetzten Gütergemeinschaft, nicht tatsächlicher ursprünglicher Erbfall. Relative Quoten können zusammen unter eins liegen und werden innerhalb der Abkömmlingsgruppe normalisiert. Teilungswert nach vorrangiger Verbindlichkeiten-/Rückbehaltsbereinigung vorgegeben. Abfindungseinrechnung§1501, Vorempfangsausgleich§1503II, Lastenzuordnung§1503III und abweichende Vereinbarungen nicht berechnet; bei deren Eingreifen keine abschließenden Auszahlungsbeträge. Pflichtteilswertbasis ist kein fertiger Ergänzungsanspruch; Schenkungshinzurechnungen, Abschmelzung und Anrechnungen gesondert.']
    return ergebnis
