from .kalender import _ergebnis, _fehler, _text, _vorhanden
from .betraege import _geld
from .zinsen import _bruchteile
from .quotenverteilung import _begrenzte_quotenverteilung

def pflichtteilsergaenzung_gleichzeitige_schenkungen(fehlbetrag=None, beschenkte=None, einordnungsnachweis=None):
    """Fehlbetrag innerhalb einer qualifizierten Gleichzeitigkeitsgruppe proportional nach Schenkungswerten bis zur Summe dieser Werte aufteilen."""
    betrag=_geld(fehlbetrag);_text(einordnungsnachweis,'einordnungsnachweis');_vorhanden(beschenkte,'beschenkte')
    if not isinstance(beschenkte,list) or not 2<=len(beschenkte)<=1000: _fehler('beschenkte','Liste2..1000 erforderlich.')
    namen=[];werte=[]
    for p in beschenkte:
        if not isinstance(p,dict) or set(p)!={'beschenkter_id','massgeblicher_schenkungswert'}: _fehler('beschenkte','Genau Kennung und maßgeblicher Schenkungswert erforderlich.')
        name=_text(p['beschenkter_id'],'beschenkter_id');wert_einzeln=_geld(p['massgeblicher_schenkungswert'])
        if name in namen: _fehler('beschenkter_id','Jede Person genau einmal.')
        if wert_einzeln<=0: _fehler('massgeblicher_schenkungswert','Positiver Wert erforderlich.')
        namen.append(name);werte.append(wert_einzeln)
    zugeordnet,rest=_begrenzte_quotenverteilung(betrag,werte,werte)
    wert=dict(beschenktenanteile=[dict(beschenkter_id=name,rechnerischer_haftungsanteil=_bruchteile(zugeordnet[i])) for i,name in enumerate(namen)],nicht_gedeckter_fehlbetrag=_bruchteile(rest))
    eingaben = dict(fehlbetrag=fehlbetrag, beschenkte=beschenkte, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_PFLICHTTEILSERGAENZUNG_GLEICHZEITIGE_SCHENKUNGEN',eingaben,[dict(operation='Fehlbetrag innerhalb einer qualifizierten Gleichzeitigkeitsgruppe proportional nach Schenkungswerten bis zur Summe dieser Werte aufteilen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§2329III mit ergänzender Primärquelle AG Bielefeld, Urteil17.05.2019,409C30/18,Rn35: gleichzeitige Schenkungen anteilig nach maßgeblichen Schenkungswerten. Nur Grundfall ohne zusätzliche individuelle Haftungsbegrenzungen/Ausfälle und ohne gruppenübergreifende Personenrahmen. Fehlbetrag höchstens bis zur Summe dieser Schenkungswerte proportional zuordnen; größerer Rest bleibt für eine gesonderte Prüfung früherer Schenkungen. Nicht nach Köpfen, keine Gesamtschuld. Werte, Gleichzeitigkeit und Bereicherungs-/Pflichtteilsvoraussetzungen rechtlich qualifizieren; kein automatischer Geldanspruch statt Sachherausgabe. Kein allgemeiner Streitentscheid über Sonderfälle aus einem amtsgerichtlichen Urteil ableiten.']
    return ergebnis

