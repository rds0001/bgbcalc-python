from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .teilverguetung import _teilbetrag
from .kalender import _fehler, _text


def finanzwiderruf_leistungswertersatz(gesamtverguetung=None, leistungsanteil_zaehler=None, leistungsanteil_nenner=None, verguetung_unverhaeltnismaessig_hoch=None, marktwert_erbrachte_leistung=None, einordnungsnachweis=None):
    """Vertraglichen Vergütungsanteil bestimmen oder auf den Marktwert der bereits erbrachten Leistung umstellen."""
    anteilig = _teilbetrag(gesamtverguetung,leistungsanteil_zaehler,leistungsanteil_nenner)
    _wahrheitswert(verguetung_unverhaeltnismaessig_hoch,'verguetung_unverhaeltnismaessig_hoch')
    if verguetung_unverhaeltnismaessig_hoch:
        wert = _geld(marktwert_erbrachte_leistung)
    else:
        if marktwert_erbrachte_leistung is not None:
            _fehler('marktwert_erbrachte_leistung','Marktwert nur bei qualifiziert unverhältnismäßig hoher Vergütung einsetzen.')
        wert = anteilig
    _text(einordnungsnachweis,'einordnungsnachweis')
    eingaben = dict(gesamtverguetung=gesamtverguetung,leistungsanteil_zaehler=leistungsanteil_zaehler,leistungsanteil_nenner=leistungsanteil_nenner,verguetung_unverhaeltnismaessig_hoch=verguetung_unverhaeltnismaessig_hoch,marktwert_erbrachte_leistung=marktwert_erbrachte_leistung,einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(wert,'BGB_FINANZWIDERRUF_LEISTUNGSWERTERSATZ',eingaben,[dict(operation='Vertraglichen Vergütungsanteil bestimmen oder auf den Marktwert der bereits erbrachten Leistung umstellen.')])
    ergebnis['hinweise'].append('§357bII undIII4: Wertersatz für bis zum Widerruf erbrachte Finanzdienstleistung beziehungsweise qualifizierte Finanzierungshilfe. Je nach Anwendungsfall erforderliche vorherige Unterrichtung, ausdrückliche Zustimmung zum vorzeitigen Beginn und Sonderverweise auf357a/506IV rechtlich vorqualifizieren. Bei digitalen Inhalten die besonderen Voraussetzungen357bII3 beachten. Keine ungeprüfte Übertragung auf gewöhnliche Darlehensnutzungszinsen357bIII; diese separat berechnen. Vereinbarte Vergütung entsprechend rechtlich bewertetem Leistungsanteil, keine automatische Zeitquote. Bei unverhältnismäßig hohem Gesamtpreis ist der eingegebene Marktwert bereits derjenige der erbrachten Leistung und wird nicht nochmals mit der Quote multipliziert. Keine feste Prozentgrenze für Unverhältnismäßigkeit erfinden; Rückzahlungen und weitere Aufwendungen getrennt, keine automatische Aufrechnung.')
    return ergebnis
