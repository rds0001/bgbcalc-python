from .teilverguetung import _teilbetrag
from .betraege import _geld_ergebnis
from .kalender import _text

def verwahrung_vorzeitige_teilverguetung(gesamtverguetung=None, leistungsanteil_zaehler=None, leistungsanteil_nenner=None, leistungsstandsnachweis=None):
    """Gesamtvergütung der vorzeitig beendeten Aufbewahrung mit dem bewerteten Anteil der bis zur Beendigung erbrachten Leistungen multiplizieren."""
    anteilig = _teilbetrag(gesamtverguetung, leistungsanteil_zaehler, leistungsanteil_nenner)
    _text(leistungsstandsnachweis,"leistungsstandsnachweis")
    eingaben = dict(gesamtverguetung=gesamtverguetung, leistungsanteil_zaehler=leistungsanteil_zaehler, leistungsanteil_nenner=leistungsanteil_nenner, leistungsstandsnachweis=leistungsstandsnachweis)
    ergebnis = _geld_ergebnis(anteilig,'BGB_VERWAHRUNG_VORZEITIGE_TEILVERGUETUNG',eingaben,[dict(operation='Gesamtvergütung der vorzeitig beendeten Aufbewahrung mit dem bewerteten Anteil der bis zur Beendigung erbrachten Leistungen multiplizieren.')])
    ergebnis["hinweise"].append('§699II: vorzeitiges Aufbewahrungsende ohne abweichende Vergütungsvereinbarung. Teilbetrag entspricht rechtlich bewerteter bisheriger Leistung; keine ungeprüfte Tagesquote. Keine volle Vergütung nicht erbrachter Leistungen. Bereits geleistete Vergütung, Aufwendungsersatz und Zinsen bei Eigennutzung698 separat abrechnen; keine automatische Aufrechnung.')
    return ergebnis
