from .kalender import _ergebnis, _fehler, _text
from .betraege import _geld
from .zahlen import _bruch, _multiplizieren
from .zinsen import _bruchteile

def gesamtgut_anteilsherabsetzung_halbgrenze(ungekuerzter_anteilswert=None, angeordneter_anteilswert=None, einordnungsnachweis=None):
    """Hälfte des ungekürzten Gesamtgutsanteils berechnen, angeordnete Herabsetzung und Unterschreitung dieser Grenze ausweisen."""
    voll=_geld(ungekuerzter_anteilswert);neu=_geld(angeordneter_anteilswert);_text(einordnungsnachweis,'einordnungsnachweis')
    if neu>voll: _fehler('angeordneter_anteilswert','Herabsetzung kann ursprünglichen Anteil nicht erhöhen.')
    haelfte=_multiplizieren(voll,_bruch(1,2))
    wert=dict(halbe_anteilsuntergrenze=_bruchteile(haelfte),angeordneter_minderungsbetrag=_bruchteile(voll-neu),halbgrenze_eingehalten=neu>=haelfte,unterschreitungsbetrag=_bruchteile(max(_geld('0'),haelfte-neu)))
    eingaben = dict(ungekuerzter_anteilswert=ungekuerzter_anteilswert, angeordneter_anteilswert=angeordneter_anteilswert, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'EUR_und_wahrheitswert','BGB_GESAMTGUT_ANTEILSHERABSETZUNG_HALBGRENZE',eingaben,[dict(operation='Hälfte des ungekürzten Gesamtgutsanteils berechnen, angeordnete Herabsetzung und Unterschreitung dieser Grenze ausweisen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§1512: ungekürzten gebührenden Anteil halbieren und angeordneten Wert mit dieser Untergrenze vergleichen. Angeordnete Minderung und positive Grenzunterschreitung getrennt ausweisen. Keine automatische Anhebung einer unwirksamen Anordnung, keine Vermögensbewertung oder Verteilung des freiwerdenden Anteils auf andere Beteiligte. Pflichtteil, Ausschluss1511, Erb-/Gesamtgutsquote und Wirksamkeit der Verfügung gesondert.']
    return ergebnis

def gesamtgut_landgut_uebernahmepreisgrenze(qualifizierter_ertragswert=None, angeordneter_uebernahmepreis=None, einordnungsnachweis=None):
    """Angeordneten Landgut-Übernahmepreis mit qualifiziertem Ertragswert als Untergrenze vergleichen."""
    ertrag=_geld(qualifizierter_ertragswert);preis=_geld(angeordneter_uebernahmepreis);_text(einordnungsnachweis,'einordnungsnachweis')
    wert=dict(ertragswertgrenze_eingehalten=preis>=ertrag,unterschreitungsbetrag=_bruchteile(max(_geld('0'),ertrag-preis)))
    eingaben = dict(qualifizierter_ertragswert=qualifizierter_ertragswert, angeordneter_uebernahmepreis=angeordneter_uebernahmepreis, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'EUR_und_wahrheitswert','BGB_GESAMTGUT_LANDGUT_UEBERNAHMEPREISGRENZE',eingaben,[dict(operation='Angeordneten Landgut-Übernahmepreis mit qualifiziertem Ertragswert als Untergrenze vergleichen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§1515II/III: angeordneten Landgut-Übernahmepreis mit qualifiziertem Ertragswert vergleichen; Gleichheit erreicht die Untergrenze. Ertragswert selbst ist Bewertungsinput nach2049, keine erfundene Kapitalisierungsformel. Keine automatische Anhebung eines unzulässigen Preises, keine Entscheidung über Testamentswirksamkeit, Übernahmeberechtigung oder Ausgleichszahlungsverteilung.']
    return ergebnis

