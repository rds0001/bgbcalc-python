"""Indexfortschreibung und erste Folgestichtage qualifizierter Mietspiegel."""
from .betraege import _geld, _geld_ergebnis
from .kalender import _datum, _ergebnis, _fehler, _frist, _text
from .zahlen import _dividieren, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile


def mietspiegel_indexfortschreibung(ausgangswert=None, ausgangsindex=None, neuer_index=None, indexnachweis=None):
    """Qualifizierten Mietspiegelwert mit dem Verhältnis vergleichbarer Indexstände fortschreiben."""
    basis = _geld(ausgangswert)
    alt = _geld(ausgangsindex)
    neu = _geld(neuer_index)
    if alt == 0 or neu == 0:
        _fehler('index','Positive vergleichbare amtliche Indexstände erforderlich.')
    _text(indexnachweis,'indexnachweis')
    verhaeltnis = _dividieren(neu,alt)
    fortgeschrieben = _multiplizieren(basis,verhaeltnis)
    wert = dict(indexverhaeltnis=_bruchteile(verhaeltnis),fortgeschriebener_wert=_bruchteile(fortgeschrieben),wertveraenderung=_bruchteile(_subtrahieren(fortgeschrieben,basis)))
    eingaben = dict(ausgangswert=ausgangswert,ausgangsindex=ausgangsindex,neuer_index=neuer_index,indexnachweis=indexnachweis)
    ergebnis = _ergebnis(wert,'EUR_je_qualifizierter_Bezugseinheit','BGB_MIETSPIEGEL_INDEXFORTSCHREIBUNG',eingaben,[dict(operation='Ausgangswert mit neuem Index geteilt durch Ausgangsindex multiplizieren; Differenz zum Ausgangswert getrennt ausweisen.')],eingaben.copy())
    ergebnis['hinweise'] = ['§558dII2: nur qualifizierte Indexanpassung, keine Stichprobenauswertung. Amtliche Indexreihe, identische Basis und rechtlich maßgebliche Bezugszeitpunkte vorgeben; Indexstände nicht selbst beschaffen oder schätzen. Ausgangswert und Ergebnis behalten dieselbe qualifizierte Mietspiegel-Bezugseinheit, beispielsweise EUR je Quadratmeter und Monat. Keine automatische Cent-Rundung, Gültigkeitsfeststellung oder konkrete Mieterhöhung; Anerkennung, Erstellungsmethode und einschlägige Verordnung gesondert. Indexsenkungen werden ebenfalls gerechnet; keine erneute Anwendung bereits berücksichtigter Änderungen.']
    return ergebnis


def mietspiegel_folgestichtage(datenerhebungsstichtag=None, stichtagsnachweis=None):
    """Erste Anpassung und Neuerstellung zwei beziehungsweise vier Jahre nach Erhebungsstichtag."""
    _datum(datenerhebungsstichtag,'datenerhebungsstichtag')
    _text(stichtagsnachweis,'stichtagsnachweis')
    eingaben = dict(datenerhebungsstichtag=datenerhebungsstichtag,stichtagsnachweis=stichtagsnachweis)
    wert = dict(anpassung_stichtag=_frist(datenerhebungsstichtag,2,'jahre','ereignis').isoformat(),neuerstellung_stichtag=_frist(datenerhebungsstichtag,4,'jahre','ereignis').isoformat())
    ergebnis = _ergebnis(wert,'daten','BGB_MIETSPIEGEL_FOLGESTICHTAGE',eingaben,[dict(operation='Vom ursprünglichen Datenerhebungsstichtag aus zwei und vier Kalenderjahre mit dem vorhandenen Fristenkern berechnen.')],eingaben.copy())
    ergebnis['hinweise'] = ['§558dII: erste Zweijahresanpassung und Vierjahresneuerstellung eines qualifizierten Mietspiegels, ausgehend vom Datenerhebungsstichtag der ursprünglichen Erstellung. Eine zwischenzeitliche Indexanpassung setzt die Vierjahresneuerstellung nicht neu in Gang; nicht deren Veröffentlichungsdatum als neuen Ausgangspunkt einsetzen. Keine automatische Feiertagsverschiebung, Gültigkeitsvermutung oder Aussage über verspätete Veröffentlichung. Veröffentlichung und wissenschaftliche/formelle Voraussetzungen gesondert prüfen; keine Fristberechnung aus einem beliebig ausgewählten Indexmonat.']
    return ergebnis
