from .kalender import _datum, _ergebnis, _text
from .reisezeitschwellen import _reise_utc_zeitpunkt

def zahlung_gutschrift_wertstellung(eingangsgeschaeftstag=None, wertstellungsdatum=None, einordnungsnachweis=None):
    """Tatsaechliches Gutschrift-Wertstellungsdatum mit Eingangsgeschaeftstag als spaetester Grenze vergleichen."""
    e=_datum(eingangsgeschaeftstag,'eingangsgeschaeftstag');v=_datum(wertstellungsdatum,'wertstellungsdatum');_text(einordnungsnachweis,'einordnungsnachweis')
    wert=dict(spaetestes_wertstellungsdatum=e.isoformat(),wertstellungsgrenze_eingehalten=v<=e)
    eingaben = dict(eingangsgeschaeftstag=eingangsgeschaeftstag, wertstellungsdatum=wertstellungsdatum, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'datum_und_wahrheitswert','BGB_ZAHLUNG_GUTSCHRIFT_WERTSTELLUNG',eingaben,[dict(operation='Tatsaechliches Gutschrift-Wertstellungsdatum mit Eingangsgeschaeftstag als spaetester Grenze vergleichen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§675tI2/III: Gutschriftspaetestens am qualifizierten Eingangsgeschaeftstag wertstellen; Belastung nicht vor tatsaechlichem Auftragszugang, Belastungswertstellung nicht vor tatsaechlicher Kontobelastung. Keine automatische Bankkalender-/Zeitzonenannahme. Eingangsgeschaeftstag nach tatsaechlichem Vorgang und anwendbarem Kalender qualifizieren, kein frei erfundener spaeterer Valutatag. Unverzuegliche Verfuegbarkeit und Verbraucherbareinzahlung675tII1 haben keine feste weitere BGB-Sekundenzahl; nicht als Erlaubnis bis Tagesende ausgeben. Nichtverbraucher-Bareinzahlung verwendet bestehenden Geschaeftstagskern675tII2.675tIVSperrfreigabe unverzueglich, genaue Zustimmungssumme ist qualitative Befugnisgrenze; keine erfundene fixe Haltefrist.675dVI/675tVSonderausnahmen vorqualifizieren.']
    return ergebnis

def zahlung_belastungszeitgrenzen(auftragszugang_utc=None, kontobelastung_utc=None, wertstellung_utc=None, einordnungsnachweis=None):
    """Tatsaechliche Kontobelastung nicht vor Auftragszugang und Wertstellung nicht vor Belastung vergleichen."""
    a=_reise_utc_zeitpunkt(auftragszugang_utc,'auftragszugang_utc');b=_reise_utc_zeitpunkt(kontobelastung_utc,'kontobelastung_utc');v=_reise_utc_zeitpunkt(wertstellung_utc,'wertstellung_utc');_text(einordnungsnachweis,'einordnungsnachweis')
    wert=dict(belastung_nicht_vor_auftragszugang=b>=a,wertstellung_nicht_vor_belastung=v>=b)
    eingaben = dict(auftragszugang_utc=auftragszugang_utc, kontobelastung_utc=kontobelastung_utc, wertstellung_utc=wertstellung_utc, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'wahrheitswerte','BGB_ZAHLUNG_BELASTUNGSZEITGRENZEN',eingaben,[dict(operation='Tatsaechliche Kontobelastung nicht vor Auftragszugang und Wertstellung nicht vor Belastung vergleichen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§675tI2/III: Gutschriftspaetestens am qualifizierten Eingangsgeschaeftstag wertstellen; Belastung nicht vor tatsaechlichem Auftragszugang, Belastungswertstellung nicht vor tatsaechlicher Kontobelastung. Keine automatische Bankkalender-/Zeitzonenannahme. Eingangsgeschaeftstag nach tatsaechlichem Vorgang und anwendbarem Kalender qualifizieren, kein frei erfundener spaeterer Valutatag. Unverzuegliche Verfuegbarkeit und Verbraucherbareinzahlung675tII1 haben keine feste weitere BGB-Sekundenzahl; nicht als Erlaubnis bis Tagesende ausgeben. Nichtverbraucher-Bareinzahlung verwendet bestehenden Geschaeftstagskern675tII2.675tIVSperrfreigabe unverzueglich, genaue Zustimmungssumme ist qualitative Befugnisgrenze; keine erfundene fixe Haltefrist.675dVI/675tVSonderausnahmen vorqualifizieren.']
    return ergebnis

