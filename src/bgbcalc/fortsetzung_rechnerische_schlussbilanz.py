from .kalender import _ergebnis, _text
from .betraege import _geld
from .zahlen import _bruch, _addieren, _subtrahieren, _dividieren
from .zinsen import _bruchteile

def fortsetzung_rechnerische_schlussbilanz(bereinigte_restmasse=None, ersatzschuld_ehegatte=None, anrechnung_abkoemmlinge=None, gezahlte_abfindungen=None, bilanznachweis=None):
    """Qualifizierte Bilanzposten addieren, halbieren und seitengerecht anrechnen; persoenliche ueberschiessende Ersatzpflicht nur beim ueberlebenden Ehegatten ausweisen."""
    r=_geld(bereinigte_restmasse);a=_geld(ersatzschuld_ehegatte);b=_geld(anrechnung_abkoemmlinge);c=_geld(gezahlte_abfindungen);_text(bilanznachweis,'bilanznachweis')
    m=_addieren(_addieren(r,a),_addieren(b,c));h=_dividieren(m,_bruch(2));s=_subtrahieren(h,a);k=_subtrahieren(_subtrahieren(h,b),c)
    wert=dict(rechenmasse=_bruchteile(m),halbteil_vor_anrechnung=_bruchteile(h),ehegattensaldo=_bruchteile(s),abkoemmlingssaldo=_bruchteile(k),abkoemmlingssaldo_vor_abfindungsanrechnung=_bruchteile(_subtrahieren(h,b)),ueberschiessende_ersatzpflicht_ehegatte=_bruchteile(max(_subtrahieren(a,h),_bruch(0))),persoenliche_ersatzpflicht_abkoemmlinge_nach_1476_absatz2_satz2=_bruchteile(_bruch(0)))
    eingaben = dict(bereinigte_restmasse=bereinigte_restmasse, ersatzschuld_ehegatte=ersatzschuld_ehegatte, anrechnung_abkoemmlinge=anrechnung_abkoemmlinge, gezahlte_abfindungen=gezahlte_abfindungen, bilanznachweis=bilanznachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_FORTSETZUNG_RECHNERISCHE_SCHLUSSBILANZ',eingaben,[dict(operation='Qualifizierte Bilanzposten addieren, halbieren und seitengerecht anrechnen; persoenliche ueberschiessende Ersatzpflicht nur beim ueberlebenden Ehegatten ausweisen.')],eingaben.copy())
    ergebnis["hinweise"] = ['Rechnerische Verbindung1498/1476 mit1500/1501: Restmasse plus beide qualifizierten Anrechnungsposten plus tatsaechlich gezahlte Abfindungen halbieren; eigene Lasten jeweils auf die betreffende Haelfte anrechnen. Negative Abkoemmlingssalden begruenden nach1498 gerade keine ueberschiessende persoenliche1476II2-Ersatzpflicht. Nur die ueberschiessende Ersatzschuld des ueberlebenden Ehegatten wird als solche ausgewiesen. Positive Salden sind rechnerische Bilanzpositionen, keine Zusage realisierbarer oder sofort faelliger Barauszahlung; gegenstaendliche Haftung, Deckung, Bewertung und Uneinbringlichkeit gesondert bestimmen. Personenverteilung1503I, Vorempfaenge1503II und ausschliesslich Beguenstigte treffende Lasten1503III/1511III2 anschliessend ohne Doppelabzug normgerecht verbinden. Keine automatische Anrechnung aller Lasten proportional auf jeden Abkoemmling. Keine abschliessende Abwicklung beliebiger Insolvenz-/Haftungskonstellationen.']
    return ergebnis

