from .kalender import _ergebnis, _text
from .reisezeitschwellen import _reise_utc_zeitpunkt

def modernisierung_haerteeinwand_beginnvergleich(mitteilungseingang_utc=None, massnahmenbeginn_utc=None, einordnungsnachweis=None):
    """Mitteilungszugang mit tatsaechlichem Massnahmenbeginn einschliesslich Grenzzeitpunkt vergleichen."""
    m=_reise_utc_zeitpunkt(mitteilungseingang_utc,'mitteilungseingang_utc');b=_reise_utc_zeitpunkt(massnahmenbeginn_utc,'massnahmenbeginn_utc');_text(einordnungsnachweis,'einordnungsnachweis')
    wert=dict(spaetestens_bis_massnahmenbeginn_mitgeteilt=m<=b)
    eingaben = dict(mitteilungseingang_utc=mitteilungseingang_utc, massnahmenbeginn_utc=massnahmenbeginn_utc, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'wahrheitswert','BGB_MODERNISIERUNG_HAERTEEINWAND_BEGINNVERGLEICH',eingaben,[dict(operation='Mitteilungszugang mit tatsaechlichem Massnahmenbeginn einschliesslich Grenzzeitpunkt vergleichen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§555dIV2/V2: wirtschaftliche Haerte spaetestens bis zum Beginn der Modernisierung mitteilen. Zeitvergleich einschliesslich des Beginnzeitpunkts; keine pauschale Frist bis Tagesende, wenn Arbeiten schon morgens beginnen. Ausschliesslich diese zusaetzliche aeusserste Zeitgrenze. Der regulaere Monatsendtermin555dIII wird durch miete_erklaerungs_monatsendtermin berechnet; ordnungsgemaesse Ankuendigung, Hinweis-/Formausnahmen und unverschuldete unverzuegliche Nachholung sind rechtliche Voraussetzungen ohne feste zusaetzliche BGB-Tageszahl. Keine fixe Frist fuer unverzueglich erfinden und keine Uebertragung der wirtschaftlichen Ausschlussgrenze auf jeden Duldungshaertegrund. UTC-Zeitpunkte vorab normalisieren; keine lokalen Zeitzonen raten.']
    return ergebnis

