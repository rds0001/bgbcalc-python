from .kalender import _ergebnis, _text
from .betraege import _geld
from .zahlen import _bruch
from .zinsen import gesetzliche_zinsen, _bruchteile

def teilzahlung_fehlangaben_zinsbetrag(massgeblicher_barzahlungspreis=None, vertraglicher_zinssatz_prozent=None, zeitanteil_zaehler=None, zeitanteil_nenner=None, zeitanteil_nachweis=None, einordnungsnachweis=None):
    """Vertraglichen Jahreszinssatz auf vier Prozent begrenzen und vorhandenen exakten Zinskern auf qualifizierten Barzahlungs-/Marktpreis anwenden."""
    _text(einordnungsnachweis,'einordnungsnachweis');satz=min(_geld(vertraglicher_zinssatz_prozent),_bruch(4))
    z=gesetzliche_zinsen(massgeblicher_barzahlungspreis,zeitanteil_zaehler,zeitanteil_nenner,zeitanteil_nachweis,False,_bruchteile(satz))
    wert=dict(massgeblicher_zinssatz_prozent=_bruchteile(satz),zinsbetrag=z['wert'])
    eingaben = dict(massgeblicher_barzahlungspreis=massgeblicher_barzahlungspreis, vertraglicher_zinssatz_prozent=vertraglicher_zinssatz_prozent, zeitanteil_zaehler=zeitanteil_zaehler, zeitanteil_nenner=zeitanteil_nenner, zeitanteil_nachweis=zeitanteil_nachweis, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'EUR_und_prozent','BGB_TEILZAHLUNG_FEHLANGABEN_ZINSBETRAG',eingaben,[dict(operation='Vertraglichen Jahreszinssatz auf vier Prozent begrenzen und vorhandenen exakten Zinskern auf qualifizierten Barzahlungs-/Marktpreis anwenden.')],eingaben.copy())
    ergebnis["hinweise"] = ['§507II3: Barzahlungspreis hoechstens mit gesetzlichem246-Jahreszinssatz4Prozent verzinsen. Niedrigerer rechtlich geschuldeter Vertragszins bleibt niedriger, keine Erhoehung auf4Prozent. Bei fehlendem Barzahlungspreis den rechtlich bewerteten Marktpreis nachII4 als gleiche Basis eingeben. Bestehender exakter Zinskern mit min(Vertragszins,4) wird verwendet. Abschnitt mit unveraenderter Basis und belegtem Jahresanteil; Raten-/Tilgungsplaene nach Vertrag abschnittsweise, kein erfundenes Annuitaetenmodell. Nicht die Gesamtbetragskorrektur bei zu niedrig angegebenem Effektivzins507II5 und nicht494II.507III-Kostenermaessigung verwendet246als qualifizierte Zinsbasis in vorhandenen501-Rechenwegen; Vorfaelligkeitsentschaedigung dort ausgeschlossen.']
    return ergebnis

