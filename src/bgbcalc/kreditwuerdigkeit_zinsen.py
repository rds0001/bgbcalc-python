from .kalender import _auswahl, _datum, _ergebnis, _text
from .zahlen import _zahleneingabe, _subtrahieren
from .zinsen import _bruchteile, gesetzliche_zinsen

def kreditwuerdigkeit_zinsermaessigung(kapital=None, vertraglicher_sollzins_prozent=None, qualifizierter_marktzins_prozent=None, zinsart=None, marktzins_stichtag_am=None, zeitanteil_zaehler=None, zeitanteil_nenner=None, zeitanteil_nachweis=None, einordnungsnachweis=None):
    """Sollzins auf kleineren qualifizierten Marktzinssatz begrenzen; bestehenden Zinskern für neuen und vertraglichen Abschnitt verwenden und Differenz bilden."""
    _auswahl(zinsart,'zinsart',('gebunden','veraenderlich'))
    _datum(marktzins_stichtag_am,'marktzins_stichtag_am');_text(einordnungsnachweis,'einordnungsnachweis')
    vertrag = _zahleneingabe(vertraglicher_sollzins_prozent)
    markt = _zahleneingabe(qualifizierter_marktzins_prozent)
    satz = min(vertrag,markt)
    zinseingaben = dict(kapital=kapital,zeitanteil_zaehler=zeitanteil_zaehler,zeitanteil_nenner=zeitanteil_nenner,zeitanteil_nachweis=zeitanteil_nachweis,glaeubigerverzug=False)
    neu = gesetzliche_zinsen(**zinseingaben,abweichender_zinssatz_prozent=_bruchteile(satz))['wert']
    alt = gesetzliche_zinsen(**zinseingaben,abweichender_zinssatz_prozent=_bruchteile(vertrag))['wert']
    wert = dict(rechnerischer_sollzins_prozent=_bruchteile(satz),rechnerischer_zinsbetrag=neu,rechnerische_zinsdifferenz=_bruchteile(_subtrahieren(_zahleneingabe(alt),_zahleneingabe(neu))))
    eingaben = dict(kapital=kapital, vertraglicher_sollzins_prozent=vertraglicher_sollzins_prozent, qualifizierter_marktzins_prozent=qualifizierter_marktzins_prozent, zinsart=zinsart, marktzins_stichtag_am=marktzins_stichtag_am, zeitanteil_zaehler=zeitanteil_zaehler, zeitanteil_nenner=zeitanteil_nenner, zeitanteil_nachweis=zeitanteil_nachweis, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'EUR_und_prozent','BGB_KREDITWUERDIGKEIT_ZINSERMAESSIGUNG',eingaben,[dict(operation='Sollzins auf kleineren qualifizierten Marktzinssatz begrenzen; bestehenden Zinskern für neuen und vertraglichen Abschnitt verwenden und Differenz bilden.')],eingaben.copy())
    ergebnis["hinweise"] = ['§505dI1/2: bereits rechtlich feststehende Zinsermäßigung; numerisch kleinerer Vertrags-/Marktzinssatz, keine Zinserhöhung. Gebundener Sollzins: Markt für Hypothekenpfandbriefe/öffentliche Pfandbriefe mit entsprechender Bindungslaufzeit; veränderlicher Sollzins: Euro-Dreimonats-Interbankenmarkt. Marktwerte, Vertragsschluss und vereinbarte Anpassungsstichtage vorqualifizieren. Jeder homogene Kapital-/Zinsabschnitt separat; keine Tilgungsplan- oder Zinseszinsannahme. Vorzeichenbehaftete Ergebnisse sind rechnerische Zinsbeträge, kein automatisch festgestellter Zahlungsanspruch bei Negativzinsen. Eine rechtlich anzuwendende Zinsuntergrenze ist vorab in der qualifizierten Zinsgrundlage zu berücksichtigen und nachzuweisen; keine erfundene Nullgrenze. Ausnahmefälle505dI5/III nicht mit dieser Funktion berechnen. Keine automatische Kreditwürdigkeitsprüfung, Pflichtverletzungsentscheidung oder Marktdatenbeschaffung.']
    return ergebnis

