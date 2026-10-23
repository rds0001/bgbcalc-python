from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .teilverguetung import _teilbetrag
from .kalender import _fehler, _text


def verbraucherbau_widerruf_wertersatz(gesamtverguetung=None, leistungsanteil_zaehler=None, leistungsanteil_nenner=None, verguetung_unverhaeltnismaessig_hoch=None, marktwert_erbrachte_leistung=None, einordnungsnachweis=None):
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
    ergebnis = _geld_ergebnis(wert,'BGB_VERBRAUCHERBAU_WIDERRUF_WERTERSATZ',eingaben,[dict(operation='Vertraglichen Vergütungsanteil bestimmen oder auf den Marktwert der bereits erbrachten Leistung umstellen.')])
    ergebnis['hinweise'].append('§357e: qualifizierter wirksamer Widerruf eines Verbraucherbauvertrags und nach ihrer Natur ausgeschlossene Rückgewähr der bis zum Widerruf erbrachten Leistung. Leistungsanteil nach Wert/Umfang, keine automatische Zeitquote. Bei unverhältnismäßig hoher vereinbarter Vergütung bezeichnet marktwert_erbrachte_leistung bereits den Marktwert der erbrachten Leistung; diesen nicht nochmals mit dem Leistungsanteil multiplizieren. Unverhältnismäßigkeit und Bewertung extern bestimmen; keine erfundene feste Prozentschwelle. Keine ungeprüfte Übernahme der zusätzlichen Voraussetzungen357aII. Vorauszahlungen, sonstige Rückgewähr und Aufrechnung gesondert, keine automatische Saldierung.')
    return ergebnis
