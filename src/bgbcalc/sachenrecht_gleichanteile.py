"""Gleichanteilige Mengen- und Kostenverteilung im Sachenrecht."""
from .betraege import _geld
from .kalender import _ergebnis, _fehler, _ganzzahl, _text
from .zahlen import _bruch, _dividieren
from .zinsen import _bruchteile


def sachenrecht_gleichanteil(gesamtmenge=None, anzahl_berechtigte=None, regelfall=None, verteilungsnachweis=None):
    """§§920/923/1038: qualifizierte Gesamtmenge durch gesetzliche Teilezahl teilen."""
    menge = _geld(gesamtmenge)
    _ganzzahl(anzahl_berechtigte, 'anzahl_berechtigte', 2, 1000)
    _text(regelfall, 'regelfall')
    if regelfall not in ['grenzflaeche_920', 'grenzbaum_fruechte_923', 'grenzbaum_holz_923', 'wirtschaftsplan_kosten_1038']:
        _fehler('regelfall', 'Unbekannter Verteilungsfall.')
    if regelfall == 'wirtschaftsplan_kosten_1038' and anzahl_berechtigte != 2:
        _fehler('anzahl_berechtigte', 'Wirtschaftsplankosten tragen Eigentümer und Nießbraucher je zur Hälfte.')
    _text(verteilungsnachweis, 'verteilungsnachweis')
    eingaben = dict(gesamtmenge=gesamtmenge, anzahl_berechtigte=anzahl_berechtigte, regelfall=regelfall, verteilungsnachweis=verteilungsnachweis)
    wert = dict(anteilsquote=_bruchteile(_bruch(1, anzahl_berechtigte)), einzelanteil=_bruchteile(_dividieren(menge, _bruch(anzahl_berechtigte))))
    ergebnis = _ergebnis(wert, 'menge_oder_EUR', 'BGB_SACHENRECHT_GLEICHANTEIL', eingaben, [dict(operation='Qualifizierte Gesamtmenge durch Anzahl gleichberechtigter Teile teilen.')], eingaben.copy())
    ergebnis['hinweise'] = ['Nur gesetzliche Gleichverteilung:920 streitige Fläche bei nicht ermittelbarer Grenze und nicht feststellbarem Besitzstand ohne abweichende Billigkeitskorrektur;923 Früchte oder gefällter Baum zwischen betroffenen Nachbarn ohne Verzichtsfall;1038 Wirtschaftsplan-/Änderungskosten zwischen Eigentümer und Nießbraucher. Nachbarn bedeuten betroffene Grundstücksseiten, nicht beliebige Zahl ihrer Miteigentümer. Gesamtmenge und Anteil in derselben Eingabeeinheit;1038 ausschließlich EUR. Keine geometrische Grenzziehung oder Bewertung unteilbarer Sachstücke.']
    return ergebnis
