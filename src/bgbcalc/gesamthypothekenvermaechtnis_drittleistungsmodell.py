from .kalender import _ergebnis, _text, _auswahl, _fehler
from .betraege import _geld
from .zahlen import _subtrahieren, _multiplizieren
from .zinsen import _bruchteile
from .gesamthypothekenvermaechtnis import gesamthypothekenvermaechtnis_befriedigungsbetrag

def gesamthypothekenvermaechtnis_drittleistungsmodell(gesicherter_schuldbetrag=None, interne_berichtigungspflicht=None, vom_dritten_erlangbarer_betrag=None, grundstuecke=None, vermachtes_grundstueck_id=None, quotierungsbasis=None, drittleistungsreihenfolge=None, methodennachweis=None):
    """Gewählte Schuld-/Innenpflichtbasis und Drittleistungsreihenfolge mit vorhandener Grundstückswertquote verbinden; Betrag auf Innenrest und Nettodeckung begrenzen."""
    schuld=_geld(gesicherter_schuldbetrag);innen=_geld(interne_berichtigungspflicht);dritt=_geld(vom_dritten_erlangbarer_betrag);_text(methodennachweis,'methodennachweis');_auswahl(quotierungsbasis,'quotierungsbasis',('gesicherte_schuld','interne_berichtigungspflicht'));_auswahl(drittleistungsreihenfolge,'drittleistungsreihenfolge',('vor_wertquote','nur_innenrestgrenze'))
    if innen>schuld or dritt>innen:_fehler('innenpflicht_und_drittbetrag','Innenpflicht höchstens Schuld, Drittbetrag höchstens Innenpflicht.')
    kern=gesamthypothekenvermaechtnis_befriedigungsbetrag(_bruchteile(schuld),grundstuecke,vermachtes_grundstueck_id,True,True,False,True,False,methodennachweis)['wert']
    if kern['verteilungsquote'] is None:_fehler('grundstuecke','Positive Wertsumme zur Quotierung erforderlich.')
    quote=_geld(kern['verteilungsquote']);deckung=_geld(next(p['bereinigter_wert'] for p in kern['bereinigte_grundstueckswerte'] if p['grundstueck_id']==vermachtes_grundstueck_id));rest=_subtrahieren(innen,dritt);basis=schuld if quotierungsbasis=='gesicherte_schuld' else innen
    if drittleistungsreihenfolge=='vor_wertquote':basis=_subtrahieren(basis,dritt)
    anteil=_multiplizieren(basis,quote)
    wert=dict(wertquote=_bruchteile(quote),nettodeckung=_bruchteile(deckung),verbleibende_innenpflicht=_bruchteile(rest),basis_vor_quotierung=_bruchteile(basis),quotierter_betrag=_bruchteile(anteil),befriedigungsbetrag=_bruchteile(min(anteil,rest,deckung)))
    eingaben = dict(gesicherter_schuldbetrag=gesicherter_schuldbetrag, interne_berichtigungspflicht=interne_berichtigungspflicht, vom_dritten_erlangbarer_betrag=vom_dritten_erlangbarer_betrag, grundstuecke=grundstuecke, vermachtes_grundstueck_id=vermachtes_grundstueck_id, quotierungsbasis=quotierungsbasis, drittleistungsreihenfolge=drittleistungsreihenfolge, methodennachweis=methodennachweis)
    ergebnis = _ergebnis(wert,'EUR_und_Quote','BGB_GESAMTHYPOTHEKENVERMAECHTNIS_DRITTLEISTUNGSMODELL',eingaben,[dict(operation='Gewählte Schuld-/Innenpflichtbasis und Drittleistungsreihenfolge mit vorhandener Grundstückswertquote verbinden; Betrag auf Innenrest und Nettodeckung begrenzen.')],eingaben.copy())
    ergebnis["hinweise"] = ['Bedingte2166II/2167-Rechnung: bestehender Grundstücksquotenkern liefert Nettodeckung und Wertquote. Innenrest=interneBerichtigungspflicht-erlangbareDrittberichtigung. Ausdrücklich gewählte Quotierungsbasis ist Gesamtschuld oder internePflicht. Bei vor_wertquote Drittbetrag von dieser Basis vor Quotierung abziehen; bei nur_innenrestgrenze bleibt die Quote ungekürzt und Drittberichtigung wirkt nur durch den Innenrestdeckel. Betrag=min(quotierterBasis,Innenrest,Nettodeckung). Vier arithmetische Kombinationen sind keine vier als rechtlich zulässig bestätigten Alternativen: keine Standardwahl, zwingende fallbezogene rechtliche Begründung. Modellwahl und ihre allgemeine rechtliche Geltung bleiben getrennt von getesteter Arithmetik.2168IIrechtliche Verweisung nur im qualifizierten Nachlassgruppenfall; Fremdgrundstückswerte nicht aufnehmen.2168Iohne2166II-Verweisung ist kein Anwendungsfall.2168aSchiffshypotheken nur bei qualifizierter entsprechender Anwendung.']
    return ergebnis

