"""Numerische Reisegrenzen ohne automatische Vertragsqualifikation."""
from .betraege import _geld
from .kalender import _ergebnis, _fehler, _ganzzahl, _text
from .zahlen import _bruch, _subtrahieren, _dividieren, _multiplizieren
from .zinsen import _bruchteile


def reiseleistungsarten_mindestzahl(anzahl_verschiedener_reiseleistungsarten=None, einordnungsnachweis=None):
    """Zahl rechtlich verschiedener Reiseleistungsarten mit mindestens zwei vergleichen."""
    x = [_ganzzahl(anzahl_verschiedener_reiseleistungsarten,'anzahl_verschiedener_reiseleistungsarten',0,9007199254740991)]
    _text(einordnungsnachweis,'einordnungsnachweis')
    eingaben = dict(anzahl_verschiedener_reiseleistungsarten=anzahl_verschiedener_reiseleistungsarten, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(dict(mindestzahl=2,fehlende_arten=max(2-x[0],0),mindestzahl_erreicht=x[0]>=2), "zahlen_und_wahrheitswerte", 'BGB_REISELEISTUNGSARTEN_MINDESTZAHL', eingaben, [dict(operation='Zahl rechtlich verschiedener Reiseleistungsarten mit mindestens zwei vergleichen.')], eingaben.copy())
    ergebnis["hinweise"] = ['Nur numerische Mindestzahl651aII/651bI; rechtlich verschiedene Arten nach651aIII für dieselbe Reise vorqualifizieren. Mehrere Hotels sind nicht automatisch mehrere Arten. Wesensmäßige Bestandteile anderer Leistungen nicht doppelt zählen. Weitere Voraussetzungen, touristische Nebenleistungsgrenzen und Ausnahmen separat; Ergebnis ist keine abschließende Pauschalreiseentscheidung.']
    return ergebnis


def touristische_leistung_wertanteil(touristischer_teilwert=None, gesamtwert_zusammenstellung=None, einordnungsnachweis=None):
    """Touristischen Teilwert durch positiven Gesamtwert teilen; Anteil strikt mit25Prozent vergleichen."""
    x = [_geld(touristischer_teilwert), _geld(gesamtwert_zusammenstellung)]
    _text(einordnungsnachweis,'einordnungsnachweis')
    if x[1]==0 or x[0]>x[1]:
        _fehler('gesamtwert_zusammenstellung','Positiver Gesamtwert erforderlich; touristischer Teilwert darf ihn nicht übersteigen.')
    eingaben = dict(touristischer_teilwert=touristischer_teilwert, gesamtwert_zusammenstellung=gesamtwert_zusammenstellung, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(dict(wertanteil=_bruchteile(_dividieren(x[0],x[1])),wertanteil_prozent=_bruchteile(_multiplizieren(_dividieren(x[0],x[1]),_bruch(100))),unter_25_prozent=_dividieren(x[0],x[1])<_bruch(1,4)), "zahlen_und_wahrheitswerte", 'BGB_TOURISTISCHE_LEISTUNG_WERTANTEIL', eingaben, [dict(operation='Touristischen Teilwert durch positiven Gesamtwert teilen; Anteil strikt mit25Prozent vergleichen.')], eingaben.copy())
    ergebnis["hinweise"] = ['§651aIV: nur rechnerischer touristischer Wertanteil in einer qualifizierten Zusammenstellung aus einer Art651aIII1bis3 und zusätzlichen touristischen Leistungen. Genau25Prozent ist nicht weniger als25Prozent. Teil-/Gesamtwerte derselben Bewertungsbasis, Gesamtwert strikt positiv, Teilwert höchstens Gesamtwert. Wesentliches Merkmal/Bewerbung sowie spätere Auswahl bleiben gesondert; ein kleiner Anteil allein schließt Pauschalreiserecht nicht aus. Keine automatische Bewertung aus unbekannten Einzelpreisen.']
    return ergebnis


def tagesreise_reisepreisgrenze(reisepreis=None, einordnungsnachweis=None):
    """Reisepreis einschließlich Gleichheit mit500EUR vergleichen und Überschreitungsbetrag berechnen."""
    x = [_geld(reisepreis)]
    _text(einordnungsnachweis,'einordnungsnachweis')
    eingaben = dict(reisepreis=reisepreis, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(dict(preisgrenze_euro=_bruchteile(_bruch(500)),preisgrenze_eingehalten=x[0]<=500,ueberschreitungsbetrag=_bruchteile(max(_subtrahieren(x[0],_bruch(500)),_bruch(0)))), "zahlen_und_wahrheitswerte", 'BGB_TAGESREISE_REISEPREISGRENZE', eingaben, [dict(operation='Reisepreis einschließlich Gleichheit mit500EUR vergleichen und Überschreitungsbetrag berechnen.')], eingaben.copy())
    ergebnis["hinweise"] = ['Nur Preisgrenze651aV2, nicht gesamte Tagesreiseausnahme. Reisedauer strikt unter24Stunden und keine Übernachtung zusätzlich qualifizieren. Im besonderen651cIII-Fall ist die Tagesreiseausnahme unabhängig vom Preis anzuwenden; dort keinen500EUR-Filter erfinden.']
    return ergebnis
