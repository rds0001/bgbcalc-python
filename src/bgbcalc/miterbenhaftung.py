"""Quotenbetrag einer Nachlassschuld (§§2059–2061)."""
from .betraege import _geld, _wahrheitswert
from .kalender import _auswahl, _ergebnis, _fehler, _ganzzahl, _text
from .zahlen import GRENZE, _bruch, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile


def miterbe_nachlassschuld_quotenbetrag(nachlassschuld=None, erbquote_zaehler=None, erbquote_nenner=None,
    haftungsfall=None, quotenhaftung_qualifiziert=None, einordnungsnachweis=None):
    """Nachlassschuld mit qualifizierter Erbquote multiplizieren; darüber hinausgehenden Teil getrennt ausweisen."""
    schuld = _geld(nachlassschuld)
    z = _ganzzahl(erbquote_zaehler, 'erbquote_zaehler', 0, GRENZE)
    n = _ganzzahl(erbquote_nenner, 'erbquote_nenner', 1, GRENZE)
    if z > n:
        _fehler('erbquote', 'Erbquote darf eins nicht übersteigen.')
    _auswahl(haftungsfall, 'haftungsfall', ('vor_teilung_unbeschraenkt_2059', 'nach_teilung_2060', 'nach_teilung_aufgebot_2061'))
    _wahrheitswert(quotenhaftung_qualifiziert, 'quotenhaftung_qualifiziert')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    eingaben = dict(nachlassschuld=nachlassschuld, erbquote_zaehler=erbquote_zaehler, erbquote_nenner=erbquote_nenner,
        haftungsfall=haftungsfall, quotenhaftung_qualifiziert=quotenhaftung_qualifiziert, einordnungsnachweis=einordnungsnachweis)
    wert = None
    if quotenhaftung_qualifiziert:
        anteil = _multiplizieren(schuld, _bruch(z, n))
        wert = dict(quotenbetrag=_bruchteile(anteil), ueber_quotenbetrag_hinausgehender_forderungsteil=_bruchteile(_subtrahieren(schuld, anteil)))
    ergebnis = _ergebnis(wert, 'EUR', 'BGB_MITERBE_NACHLASSSCHULD_QUOTENBETRAG', eingaben,
        [dict(operation='Nachlassschuld mit Erbquote multiplizieren; übrigen Forderungsteil als Differenz ausweisen')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Rechtlich qualifizierter individueller Haftungsfall und Erbquote; keine automatische Tatbestands- oder Forderungsprüfung.']
    ergebnis['hinweise'] = ['2059I2: nur unbeschränkt haftender Miterbe vor Teilung; Quotenbetrag ist der vom Verweigerungsrecht für Eigenvermögen ausgenommene Teil. Zugriff auf ungeteilten Nachlass2059II bleibt unberührt.2060: nach Teilung und konkret qualifizierter Ausschluss-, Spätgläubiger- oder beendeter Insolvenzfall; Teilung allein genügt nicht.2061: wirksame öffentliche Aufforderung und Ablauf der Sechsmonatsfrist ab letzter Veröffentlichung, weder rechtzeitige Anmeldung noch diesem Miterben bei Teilung bekannte Forderung. Grundfrist kann erbrecht_weitere_grundfrist liefern, erforderliche Korrekturen rechtlich prüfen. Kenntnis individuell je Miterbe beurteilen. Restforderung erlischt nicht; keine automatische Haftungsquote anderer Miterben oder Vollstreckungsentscheidung. Nicht mit beschränkter Haftung auf den Geldwert eines Erbteils verwechseln: Quote bezieht sich auf Schuld, nicht Nachlasswert.']
    return ergebnis
