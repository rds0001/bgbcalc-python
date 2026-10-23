"""Schutz des eigenen Pflichtteils des ergänzungspflichtigen Erben (§2328)."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _text
from .zahlen import _addieren, _bruch, _subtrahieren
from .zinsen import _bruchteile


def pflichtteilsergaenzung_eigenpflichtteilsschutz(verfuegbarer_nachlassanteil=None,
    eigener_pflichtteil=None, eigene_pflichtteilsergaenzung=None, fremde_ergaenzungsforderung=None,
    erbe_selbst_pflichtteilsberechtigt=None, bewertungsnachweis=None):
    """§2328: Verweigerungsbetrag, der eigenen Pflichtteil samt Ergänzung schützt."""
    verfuegbar = _geld(verfuegbarer_nachlassanteil)
    pflichtteil = _geld(eigener_pflichtteil)
    ergaenzung = _geld(eigene_pflichtteilsergaenzung)
    forderung = _geld(fremde_ergaenzungsforderung)
    _wahrheitswert(erbe_selbst_pflichtteilsberechtigt, 'erbe_selbst_pflichtteilsberechtigt')
    _text(bewertungsnachweis, 'bewertungsnachweis')
    eingaben = dict(verfuegbarer_nachlassanteil=verfuegbarer_nachlassanteil,
        eigener_pflichtteil=eigener_pflichtteil, eigene_pflichtteilsergaenzung=eigene_pflichtteilsergaenzung,
        fremde_ergaenzungsforderung=fremde_ergaenzungsforderung,
        erbe_selbst_pflichtteilsberechtigt=erbe_selbst_pflichtteilsberechtigt, bewertungsnachweis=bewertungsnachweis)
    ergebnis = _geld_ergebnis(None, 'BGB_PFLICHTTEILSERGAENZUNG_EIGENPFLICHTTEILSSCHUTZ', eingaben,
        [dict(operation='Eigenen Pflichtteil samt eigener Ergänzung schützen; fremde Ergänzungsforderung nur bis darüber hinaus verfügbarem Nachlassanteil belassen')])
    if erbe_selbst_pflichtteilsberechtigt:
        schutz = _addieren(pflichtteil, ergaenzung)
        deckung = max(_bruch(0), _subtrahieren(verfuegbar, schutz))
        verbleibend = min(forderung, deckung)
        ergebnis['wert'] = dict(eigener_schutzbetrag=_bruchteile(schutz),
            nicht_nach_2328_verweigerbarer_betrag=_bruchteile(verbleibend),
            verweigerungsbetrag=_bruchteile(_subtrahieren(forderung, verbleibend)))
        ergebnis['status'] = 'BERECHNET'
    ergebnis['hinweise'].append('Nur betragsmäßiger Schutz nach§2328 und keine automatische Ausübung der Einrede. Eigener Pflichtteil und eigene Ergänzung müssen rechtlich berechnet und anrechnungsbereinigt sein; eigene Ergänzung nicht als voller Geschenkewert eingeben. Verfügbaren Nachlassanteil konsistent vor der betrachteten fremden Ergänzung, aber nach sonstigen rechtlich vorrangigen Belastungen bestimmen. Keine automatische Ermittlung von Nachlassverbindlichkeiten, Schenkungsanrechnung oder Rückgriff. Mehrere fremde Forderungen nicht jeweils gegen denselben ungekürzten verfügbaren Betrag rechnen; Gesamtbetrag vorgeben, dessen Verteilung gesondert prüfen. Nicht nach§2328 verweigerbar bedeutet nicht automatisch tatsächlich geschuldet oder durchsetzbar. Ergänzungshaftung Beschenkter§2329 getrennt; keine Addition zu bereits voll erfüllter Forderung.')
    return ergebnis
