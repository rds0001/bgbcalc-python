from .reisezeitschwellen import _reise_utc_zeitpunkt
from .kalender import _ergebnis, _fehler, _text
from .betraege import _geld
from .zahlen import _bruch, _multiplizieren
from .zinsen import _bruchteile

def zahlungsdienste_entgeltabschnitt(abschnitt_von_utc=None, abschnitt_bis_utc=None, beendigung_utc=None, abschnittsentgelt=None, vorausgezahltes_entgelt=None, einordnungsnachweis=None):
    """Halb offenen Entgeltabschnitt am Beendigungszeitpunkt schneiden; Zeitanteile exakt bestimmen und Entgelt sowie Vorauszahlung proportional abrechnen."""
    von=_reise_utc_zeitpunkt(abschnitt_von_utc,'abschnitt_von_utc');bis=_reise_utc_zeitpunkt(abschnitt_bis_utc,'abschnitt_bis_utc');ende=_reise_utc_zeitpunkt(beendigung_utc,'beendigung_utc');_text(einordnungsnachweis,'einordnungsnachweis')
    preis=_geld(abschnittsentgelt);zahlung=_geld(vorausgezahltes_entgelt)
    if bis<=von: _fehler('abschnitt_bis_utc','Abschnitt muss positive Dauer haben.')
    if zahlung>preis: _fehler('vorausgezahltes_entgelt','Vorauszahlung darf Abschnittsentgelt nicht uebersteigen.')
    gesamt=int((bis-von).total_seconds());vor=max(0,min(gesamt,int((ende-von).total_seconds())))
    quote=_bruch(vor,gesamt)
    wert=dict(sekunden_gesamt=gesamt,sekunden_bis_beendigung=vor,geschuldeter_zeitanteil=_bruchteile(quote),geschuldetes_entgelt=_bruchteile(_multiplizieren(preis,quote)),erstattungsbetrag=_bruchteile(_multiplizieren(zahlung,_bruch(gesamt-vor,gesamt))))
    eingaben = dict(abschnitt_von_utc=abschnitt_von_utc, abschnitt_bis_utc=abschnitt_bis_utc, beendigung_utc=beendigung_utc, abschnittsentgelt=abschnittsentgelt, vorausgezahltes_entgelt=vorausgezahltes_entgelt, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'sekunden_quote_und_eur','BGB_ZAHLUNGSDIENSTE_ENTGELTABSCHNITT',eingaben,[dict(operation='Halb offenen Entgeltabschnitt am Beendigungszeitpunkt schneiden; Zeitanteile exakt bestimmen und Entgelt sowie Vorauszahlung proportional abrechnen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§675hIII: Entgelt nur bis zur Beendigung; auf danach entfallende Zeit zugeordnete Vorauszahlung erstatten. Berechnung unter ausdrücklich rechtlich bestimmter gleichmäßiger Zeitbewertung in Sekunden; keine automatische Wahl einer Vertrags-/Tageskonvention. Abweichend bewertete Preisperioden getrennt normalisieren und abrechnen. Halb offene Intervalle verhindern doppelte Grenzsekunden. Standardbibliotheken und vorhandener UTC-Parser, keine neue Datumsbibliothek; keine stillschweigende Zeitzone oder Rundung von Subsekunden. Vertragswirksamkeit, zulässige Kündigungsfrist675hI/II und EntgeltverbotIV separat; kein Kündigungsentgelt ergänzen. Geschuldetes Entgelt und Rückerstattung nicht als zwei zusätzliche Ansprüche zusammenzählen.']
    return ergebnis

