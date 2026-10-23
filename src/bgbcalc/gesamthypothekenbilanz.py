from .betraege import _geld
from .betreuungsrechnung import _rechnungssumme
from .kalender import _ergebnis, _fehler, _text
from .zahlen import _bruch, _subtrahieren
from .zinsen import _bruchteile

def gesamthypothek_verteilungsrahmen(ausgangsforderung=None, zugeteilte_teilforderungen=None, einordnungsnachweis=None):
    """Zugewiesene Teilforderungen summieren, auf vorhandene Gesamtforderung begrenzen und noch nicht zugeordneten rechnerischen Betrag bestimmen."""
    forderung = _geld(ausgangsforderung)
    summe = _rechnungssumme(zugeteilte_teilforderungen,'zugeteilte_teilforderungen')
    _text(einordnungsnachweis,"einordnungsnachweis")
    if summe>forderung:
        _fehler("zugeteilte_teilforderungen","Summe der Teilforderungen darf die Ausgangsforderung nicht übersteigen.")
    wert = dict(summe_teilforderungen=_bruchteile(summe),noch_nicht_zugeteilter_betrag=_bruchteile(_subtrahieren(forderung,summe)))
    eingaben = dict(ausgangsforderung=ausgangsforderung, zugeteilte_teilforderungen=zugeteilte_teilforderungen, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,"EUR",'BGB_GESAMTHYPOTHEK_VERTEILUNGSRAHMEN',eingaben,[dict(operation='Zugewiesene Teilforderungen summieren, auf vorhandene Gesamtforderung begrenzen und noch nicht zugeordneten rechnerischen Betrag bestimmen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§1132II: numerische Verteilungsplanung mit ausdrücklich zugeordneten Teilbeträgen. Keine proportionale oder gleiche Verteilung erfinden; die rechtlich gewählte Zuordnung bleibt Eingabe. Summe darf die vorhandene Forderung nicht übersteigen. Ein positiver noch nicht zugeteilter Betrag zeigt eine unvollständige Planung, keine automatisch vollzogene teilweise Aufteilung oder Freigabe von Grundstücken. Voraussetzungen875/876/878, Grundbuchvollzug, Rang und Eigentümerrechte außerhalb der Rechnung. Bereits geleistete Zahlungen vorab eindeutig berücksichtigen.']
    return ergebnis

def gesamthypothek_glaeubigerrest(ausgangsforderung=None, befriedigungsbetraege=None, einordnungsnachweis=None):
    """Alle auf dieselbe gesicherte Forderung wirkenden Befriedigungen einmal summieren; Rest beim bisherigen Gläubiger und übersteigenden Zahlbetrag getrennt bestimmen."""
    forderung = _geld(ausgangsforderung)
    summe = _rechnungssumme(befriedigungsbetraege,'befriedigungsbetraege')
    _text(einordnungsnachweis,"einordnungsnachweis")
    wert = dict(beruecksichtigte_befriedigung=_bruchteile(summe),verbleibende_glaeubigerforderung=_bruchteile(max(_subtrahieren(forderung,summe),_bruch(0))),uebersteigender_zahlbetrag=_bruchteile(max(_subtrahieren(summe,forderung),_bruch(0))))
    eingaben = dict(ausgangsforderung=ausgangsforderung, befriedigungsbetraege=befriedigungsbetraege, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,"EUR",'BGB_GESAMTHYPOTHEK_GLAEUBIGERREST',eingaben,[dict(operation='Alle auf dieselbe gesicherte Forderung wirkenden Befriedigungen einmal summieren; Rest beim bisherigen Gläubiger und übersteigenden Zahlbetrag getrennt bestimmen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§1132I: dieselbe Forderung wird nicht mit der Zahl belasteter Grundstücke multipliziert. Qualifizierte Befriedigungen aus verschiedenen Grundstücken und sonstigen Quellen nur einmal auf dieselbe Ausgangsforderung anrechnen. Zahlung auf Kosten/Zinsen oder andere Forderungen zuerst richtig zuordnen; Ausgangsforderung und Beträge müssen denselben Umfang und Zeitraum betreffen. Ergebnis ist der Rest beim bisherigen Gläubiger, kein allgemeines Erlöschensurteil: Forderungs-/Hypothekenübergang insbesondere1143/1150, Ausgleich und verbleibende Eigentümerrechte separat. Übersteigender Zahlbetrag begründet keinen automatisch festgestellten Erstattungsanspruch.']
    return ergebnis

