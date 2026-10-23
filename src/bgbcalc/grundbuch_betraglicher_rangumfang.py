from .kalender import _ergebnis, _auswahl, _text
from .betraege import _geld
from .zahlen import _subtrahieren
from .zinsen import _bruchteile

def grundbuch_betraglicher_rangumfang(rechtsbetrag=None, bezifferter_rangumfang=None, rangfall=None, einordnungsnachweis=None):
    """Bezifferten Rangumfang auf Rechtsbetrag begrenzen und beide nicht erfassten Restgrößen getrennt ausweisen."""
    r=_geld(rechtsbetrag);g=_geld(bezifferter_rangumfang);_text(einordnungsnachweis,'einordnungsnachweis');_auswahl(rangfall,'rangfall',('rangvereinbarung_880','rangvorbehalt_881','vormerkungsumfang_883'));teil=min(r,g)
    wert=dict(erfasster_rechtsteil=_bruchteile(teil),nicht_erfasster_rechtsteil=_bruchteile(_subtrahieren(r,teil)),ungenutzter_rangrahmen=_bruchteile(_subtrahieren(g,teil)))
    eingaben = dict(rechtsbetrag=rechtsbetrag, bezifferter_rangumfang=bezifferter_rangumfang, rangfall=rangfall, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_GRUNDBUCH_BETRAGLICHER_RANGUMFANG',eingaben,[dict(operation='Bezifferten Rangumfang auf Rechtsbetrag begrenzen und beide nicht erfassten Restgrößen getrennt ausweisen.')],eingaben.copy())
    ergebnis["hinweise"] = ['Nur numerische Aufteilung eines ausdrücklich bezifferten Rangumfangs: erfasster Teil=min(Rechtsbetrag,Rangumfang), übriger Rechtsteil=Rechtsbetrag-erfassterTeil, ungenutzter Rahmen=Rangumfang-erfassterTeil.880Vschützt Zwischenrechte;881IVschränkt den Vorbehalt bei zusätzlicher Beeinträchtigung ein;883IIbegrenzt relative Unwirksamkeit auf Anspruchsbeeinträchtigung. Diese Vorschriften liefern keine allgemeine gesetzliche Geldverteilungsformel allein aus Nominalbeträgen. Rechtliche Eintragung/Auslegung und Wirkungen auf fremde Rechte sind vorqualifiziert, kein automatischer vollständiger Rangtausch oder selbst erfundene ZVG-Erlösverteilung.883IIImaßgeblicheVormerkungseintragung mit vorhandenem879-Paarvergleich verwendbar. Rechte mit nicht vergleichbaren Zins-/Nebenleistungsbestandteilen nicht in eine einzige Zahl pressen, sondern rechtlich sachgerechte Komponenten getrennt rechnen. Keine künstliche transitive Gesamtranggruppe aus einzelnen879-Vergleichen.']
    return ergebnis

