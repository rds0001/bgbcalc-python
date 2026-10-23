"""§497 Absatz2: qualifizierter Zinsschaden höchstens gesetzlicher Jahreszinsbetrag."""
from .betraege import _geld, _geld_ergebnis
from .kalender import _text
from .zinsen import gesetzliche_zinsen, _bruchteile


def verbraucherdarlehen_zinsschadensgrenze(gesondert_verbuchte_verzugszinsen=None, nachgewiesener_zinsschaden=None, zeitanteil_zaehler=None, zeitanteil_nenner=None, zeitanteil_nachweis=None, einordnungsnachweis=None):
    """Nachgewiesenen Zinsschaden auf den Vierprozentbetrag des qualifizierten Jahresanteils begrenzen."""
    zinsschuld=_geld(gesondert_verbuchte_verzugszinsen); schaden=_geld(nachgewiesener_zinsschaden)
    _text(einordnungsnachweis,'einordnungsnachweis')
    deckel=gesetzliche_zinsen(kapital=gesondert_verbuchte_verzugszinsen,zeitanteil_zaehler=zeitanteil_zaehler,zeitanteil_nenner=zeitanteil_nenner,zeitanteil_nachweis=zeitanteil_nachweis,glaeubigerverzug=False,abweichender_zinssatz_prozent=None)
    grenze=_geld(deckel['wert'])
    eingaben=dict(gesondert_verbuchte_verzugszinsen=gesondert_verbuchte_verzugszinsen,nachgewiesener_zinsschaden=nachgewiesener_zinsschaden,zeitanteil_zaehler=zeitanteil_zaehler,zeitanteil_nenner=zeitanteil_nenner,zeitanteil_nachweis=zeitanteil_nachweis,einordnungsnachweis=einordnungsnachweis)
    ergebnis=_geld_ergebnis(min(schaden,grenze),'BGB_VERBRAUCHERDARLEHEN_ZINSSCHADENSGRENZE',eingaben,[dict(operation='Vorhandenen gesetzlichen Vierprozent-Zinskern als Schadensobergrenze anwenden; nachgewiesenen Zinsschaden hierauf begrenzen.',gesetzlicher_hoechstbetrag=_bruchteile(grenze))])
    ergebnis['hinweise'].append('Nur §497 Absatz2 Satz2 in Verbindung mit §289 Satz2 für Allgemein-Verbraucherdarlehen; Immobiliar-Verbraucherdarlehen nach Absatz4 ausgenommen. Grundlage sind qualifiziert gesondert verbuchte nach Verzugseintritt anfallende Zinsen, keine gesamte Darlehensrestschuld und kein automatischer Zinseszins. Ein einheitlicher Schadens-/Jahresanteilsabschnitt mit unveränderter Zinsschuldbasis; bei laufend anfallenden Zinsen Teilabschnitte separat qualifizieren, keine Verzinsung vor Entstehung. Nachgewiesener Schaden und Anspruchsvoraussetzungen extern; der Vierprozentbetrag begrenzt nur den Schaden. Jahresanteil aus belegter Zeitkonvention, keine automatische365- oder360-Tage-Annahme.')
    return ergebnis
