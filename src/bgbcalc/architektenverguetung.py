from .teilverguetung import _teilbetrag
from .betraege import _geld_ergebnis
from .kalender import _text

def architekten_sonderkuendigung_verguetung(gesamtverguetung=None, leistungsanteil_zaehler=None, leistungsanteil_nenner=None, leistungsstandsnachweis=None):
    """Gesamtvergütung des gekündigten Umfangs mit dem bewerteten Anteil der bis zur Kündigung erbrachten Leistungen multiplizieren."""
    anteilig = _teilbetrag(gesamtverguetung, leistungsanteil_zaehler, leistungsanteil_nenner)
    _text(leistungsstandsnachweis,"leistungsstandsnachweis")
    eingaben = dict(gesamtverguetung=gesamtverguetung, leistungsanteil_zaehler=leistungsanteil_zaehler, leistungsanteil_nenner=leistungsanteil_nenner, leistungsstandsnachweis=leistungsstandsnachweis)
    ergebnis = _geld_ergebnis(anteilig,'BGB_ARCHITEKTEN_SONDERKUENDIGUNG_VERGUETUNG',eingaben,[dict(operation='Gesamtvergütung des gekündigten Umfangs mit dem bewerteten Anteil der bis zur Kündigung erbrachten Leistungen multiplizieren.')])
    ergebnis["hinweise"].append('§650rIII bei wirksamer Sonderkündigung nachAbsatz1 oder2. Keine Gleichsetzung mit einer Kündigung aus wichtigem Grund648a und keine Fünfprozentvermutung648. Vertragsvergütung und Leistungsanteil einschließlich eines etwaigen besonderen Vergütungsrechts vorqualifizieren; keine HOAI-Berechnung. Keine Vergütung nicht erbrachter Leistungen; bereits geleistete Zahlungen und gesonderte Ansprüche separat abrechnen.')
    return ergebnis
