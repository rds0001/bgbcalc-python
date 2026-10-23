"""Zwei-von-drei-Größenvergleich in beiden Vorjahren (§310 Absatz1a)."""
from .betraege import _geld
from .kalender import _ergebnis, _fehler, _ganzzahl, _text, _vorhanden
from .zahlen import _bruch


def grossunternehmen_zweijahresschwelle(vertragsjahr=None, jahreswerte=None, bewertungsnachweis=None):
    """Je Vorjahr250 Beschäftigte,50Millionen Umsatz und43Millionen Bilanzsumme vergleichen."""
    jahr = _ganzzahl(vertragsjahr, 'vertragsjahr', 3, 9999)
    _vorhanden(jahreswerte, 'jahreswerte')
    if not isinstance(jahreswerte, list) or len(jahreswerte) != 2:
        _fehler('jahreswerte', 'Genau zwei Jahresobjekte erforderlich.')
    gesehen = set()
    auswertung = []
    for werte in jahreswerte:
        if not isinstance(werte, dict) or set(werte) != {'kalenderjahr', 'arbeitnehmer_jahresdurchschnitt', 'umsatzerloese', 'bilanzsumme'}:
            _fehler('jahreswerte', 'Genau kalenderjahr, arbeitnehmer_jahresdurchschnitt, umsatzerloese und bilanzsumme erforderlich.')
        kalenderjahr = _ganzzahl(werte['kalenderjahr'], 'kalenderjahr', 1, 9998)
        if kalenderjahr not in {jahr-2, jahr-1} or kalenderjahr in gesehen:
            _fehler('kalenderjahr', 'Beide unmittelbar vorhergehenden Kalenderjahre genau einmal angeben.')
        gesehen.add(kalenderjahr)
        personal = _geld(werte['arbeitnehmer_jahresdurchschnitt'])
        umsatz = _geld(werte['umsatzerloese'])
        bilanz = _geld(werte['bilanzsumme'])
        personal_erfuellt = personal >= _bruch(250)
        umsatz_erfuellt = umsatz > _bruch(50000000)
        bilanz_erfuellt = bilanz > _bruch(43000000)
        anzahl = sum([personal_erfuellt, umsatz_erfuellt, bilanz_erfuellt])
        auswertung.append(dict(kalenderjahr=kalenderjahr, arbeitnehmerschwelle_erfuellt=personal_erfuellt,
            umsatzschwelle_erfuellt=umsatz_erfuellt, bilanzschwelle_erfuellt=bilanz_erfuellt,
            erfuellte_merkmale=anzahl, mindestens_zwei_merkmale=anzahl >= 2))
    _text(bewertungsnachweis, 'bewertungsnachweis')
    auswertung.sort(key=lambda zeile: zeile['kalenderjahr'])
    eingaben = dict(vertragsjahr=vertragsjahr, jahreswerte=jahreswerte, bewertungsnachweis=bewertungsnachweis)
    wert = dict(jahrespruefungen=auswertung, in_beiden_jahren_zwei_merkmale=all(z['mindestens_zwei_merkmale'] for z in auswertung))
    ergebnis = _ergebnis(wert, 'anzahlen_und_wahrheitswerte', 'BGB_GROSSUNTERNEHMEN_ZWEIJAHRESSCHWELLE', eingaben,
        [dict(operation='Je Vorjahr Beschäftigte mindestens250, Umsatz strikt über50Millionen und Bilanzsumme strikt über43Millionen vergleichen; mindestens2 Merkmale in jedem Jahr')], eingaben.copy())
    ergebnis['annahmen'] = ['HGB-gemäß vorqualifizierte Jahreswerte derselben Unternehmenseinheit; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['Nur numerischer Größenvergleich des§310 Absatz1a, keine vollständige Freistellung von AGB-Kontrolle. Geschäftsart, Unternehmerstellung, rechtmäßige gewerbsmäßige Tätigkeit und weitere Tatbestände separat qualifizieren. Umsatz/Bilanz in EUR; Beschäftigten-Jahresdurchschnitt nach§267 Absatz5 HGB und Bilanzsumme nach§267 Absatz4a HGB vorgeben, nicht beliebige Stichtagswerte. Die beiden erfüllten Merkmale dürfen zwischen den Jahren wechseln; kein Zweijahresmittel und keine Addition beider Jahre. Arbeitnehmergrenze einschließlich250; Umsatz und Bilanz strikt größer als jeweilige Grenze.']
    return ergebnis
