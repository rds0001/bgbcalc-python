"""Vorempfangsausgleich nach fortgesetzter Gütergemeinschaft."""
from .betraege import _geld
from .erbausgleich import erb_zuwendungen_ausgleichen
from .kalender import _ergebnis, _fehler, _text, _vorhanden
from .zahlen import _subtrahieren
from .zinsen import _bruchteile


def fortgesetzte_guetergemeinschaft_vorempfangsausgleich(abkoemmlings_teilungsmasse=None, abkoemmlinge=None, bewertungsnachweis=None):
    """§1503II: bereits ausgeglichene Vorempfangsteile ausnehmen; verbleibende Werte nach§§2055/2056 ausgleichen."""
    _geld(abkoemmlings_teilungsmasse)
    _text(bewertungsnachweis,'bewertungsnachweis')
    _vorhanden(abkoemmlinge,'abkoemmlinge')
    if not isinstance(abkoemmlinge,list) or not 1 <= len(abkoemmlinge) <= 1000:
        _fehler('abkoemmlinge','Liste mit 1 bis 1000 qualifizierten Abkömmlingen erforderlich.')
    gruppe, reste = [], []
    for person in abkoemmlinge:
        if not isinstance(person,dict) or set(person) != {'person_id','erbquote_zaehler','erbquote_nenner','vorempfangswert','bereits_ausgeglichener_vorempfangswert'}:
            _fehler('abkoemmlinge','Genau person_id, erbquote_zaehler, erbquote_nenner, vorempfangswert und bereits_ausgeglichener_vorempfangswert erforderlich.')
        wert = _geld(person['vorempfangswert']); ausgeglichen = _geld(person['bereits_ausgeglichener_vorempfangswert'])
        if ausgeglichen > wert:
            _fehler('bereits_ausgeglichener_vorempfangswert','Bereits ausgeglichener Teil darf den Vorempfangswert nicht übersteigen.')
        rest = _bruchteile(_subtrahieren(wert,ausgeglichen))
        gruppe.append({k:person[k] for k in ('person_id','erbquote_zaehler','erbquote_nenner')} | dict(ausgleichungswert=rest))
        reste.append(dict(person_id=person['person_id'],verbleibender_ausgleichungswert=rest))
    kern = erb_zuwendungen_ausgleichen(abkoemmlings_teilungsmasse,gruppe,True,bewertungsnachweis)
    eingaben = dict(abkoemmlings_teilungsmasse=abkoemmlings_teilungsmasse,abkoemmlinge=abkoemmlinge,bewertungsnachweis=bewertungsnachweis)
    ergebnis = _ergebnis(dict(verbleibende_vorempfaenge=reste,verteilung=kern['wert']['verteilung'],ausser_ansatz=kern['wert']['ausser_ansatz']),'EUR','BGB_FORTGESETZTE_GUETERGEMEINSCHAFT_VOREMPFANGSAUSGLEICH',eingaben,[dict(operation='Bereits ausgeglichene Vorempfangsteile auf gleicher Wertbasis abziehen; verbleibende Werte im vorhandenen Ausgleichungskern nach§§2055/2056 einschließlich Überempfangausschluss verteilen.')]+kern['rechenschritte'],eingaben.copy())
    ergebnis['hinweise'] = ['§1503II mit§§2055/2056: vollständige rechtlich qualifizierte Ausgleichungsgruppe und relative positive Quoten innerhalb dieser Gruppe mit Summe eins. Teilungsmasse ist ausschließlich der dieser Gruppe zufallende bereinigte Abkömmlingsbetrag, nicht das gesamte Gesamtgut; Halbierung und andere Lasten davor gesondert bestimmen. Vorempfangswert und bereits bei der Nachlassteilung ausgeglichener Teil auf identischer maßgeblicher Bewertungsbasis vorgeben; bereits ausgeglichener Teil ist kein früherer Auszahlungsbetrag und kein nach freier Wahl verrechneter Vorteil. Die rechtliche Ausgleichungspflicht und wertmäßige Abgrenzung/Indexierung werden nicht ermittelt. Keine erneute Anrechnung desselben Vorempfangs. Qualifizierte einfache Ausgleichungsgruppe; Stämme, Nachfolgezuordnungen, Leistungsausgleich§2057a und abweichende Anordnungen nicht automatisch modelliert. §1503III begünstigtenbezogene Abfindungslasten sind hier nicht verteilt. Ausgeschlossene Überempfänger zahlen nach§2056 den Mehrbetrag nicht zurück.']
    return ergebnis
