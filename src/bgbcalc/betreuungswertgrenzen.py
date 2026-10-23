from .kalender import _auswahl, _ergebnis, _text
from .betraege import _geld
from .zinsen import _bruchteile

def betreuung_numerische_wertgrenze(grenzfall=None, massgeblicher_gesamtwert=None, einordnungsnachweis=None):
    """Qualifizierten betreuungsrechtlichen Gesamtwert mit gesetzlicher3000-/6000-Euro-Grenze einschließlich Gleichheit vergleichen."""
    grenzen={'zahlungsanspruch_1849':3000,'vergleichsgegenstand_1854':6000,'vermoegenswert_1860':6000}
    _auswahl(grenzfall,'grenzfall',tuple(grenzen));betrag=_geld(massgeblicher_gesamtwert);_text(einordnungsnachweis,'einordnungsnachweis');grenze=_geld(str(grenzen[grenzfall]))
    wert=dict(wertgrenze=_bruchteile(grenze),wertgrenze_eingehalten=betrag<=grenze,ueberschreitungsbetrag=_bruchteile(max(_geld('0'),betrag-grenze)))
    eingaben = dict(grenzfall=grenzfall, massgeblicher_gesamtwert=massgeblicher_gesamtwert, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'EUR_und_wahrheitswert','BGB_BETREUUNG_NUMERISCHE_WERTGRENZE',eingaben,[dict(operation='Qualifizierten betreuungsrechtlichen Gesamtwert mit gesetzlicher3000-/6000-Euro-Grenze einschließlich Gleichheit vergleichen.')],eingaben.copy())
    ergebnis["hinweise"] = ['Nur numerische Höchstwertvergleiche1849II1a,1854Nr6 und1860I: nicht mehr als/nicht übersteigt schließt Gleichheit ein. Keine automatische Genehmigungsfreiheit oder gerichtliche Befreiung.1849III-Ausnahmen insbesondere gesperrte Geldanlage/Wertpapiereinlösung gesondert;1854 gerichtlicher Vergleichsvorschlag eigener Ausnahmeweg;1860 Antrag, Ermessen und Gefährdungsprüfung gesondert. Für1849 nicht bloß aktuell abgehobenen Teilbetrag verwenden; für1860 keine Verbindlichkeiten vom Nichtimmobilienvermögen abziehen.']
    return ergebnis

