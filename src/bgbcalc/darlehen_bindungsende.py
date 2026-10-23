from .kalender import _datum, _ergebnis, _frist, _text
from .betraege import _wahrheitswert

def darlehen_kuendigung_zum_sollzinsbindungsende(kuendigungszugang_am=None, sollzinsbindung_endet_am=None, periodische_anpassung_bis_ein_jahr=None, einordnungsnachweis=None):
    """Einmonatige Kündigungsfrist mit Sollzinsbindungsende und gesetzlicher Periodenbeschränkung verbinden."""
    bindung=_datum(sollzinsbindung_endet_am,'sollzinsbindung_endet_am');_wahrheitswert(periodische_anpassung_bis_ein_jahr,'periodische_anpassung_bis_ein_jahr');_text(einordnungsnachweis,'einordnungsnachweis')
    monat=_frist(kuendigungszugang_am,1,'monate','ereignis')
    genug=monat<=bindung
    ende=(bindung if genug else None) if periodische_anpassung_bis_ein_jahr else max(monat,bindung)
    wert=dict(einmonatige_kuendigungsfrist_letzter_tag=monat.isoformat(),monatsfrist_zum_bindungsende_eingehalten=genug,rechnerischer_beendigungstag=ende.isoformat() if ende is not None else None)
    eingaben = dict(kuendigungszugang_am=kuendigungszugang_am, sollzinsbindung_endet_am=sollzinsbindung_endet_am, periodische_anpassung_bis_ein_jahr=periodische_anpassung_bis_ein_jahr, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'daten_und_wahrheitswert','BGB_DARLEHEN_KUENDIGUNG_ZUM_SOLLZINSBINDUNGSENDE',eingaben,[dict(operation='Einmonatige Kündigungsfrist mit Sollzinsbindungsende und gesetzlicher Periodenbeschränkung verbinden.')],eingaben.copy())
    ergebnis["hinweise"] = ['§489I1: Einmonatsfrist ab Zugang mit Sollzinsbindungsende verbinden. Ohne Periodenbeschränkung ist der spätere dieser beiden Tage der rechnerisch früheste Beendigungstag. Bei qualifizierter Anpassung in Zeiträumen bis zu einem Jahr ist ausschließlich der vorgegebene Bindungsendtag erfasst; ist dafür die Monatsfrist nicht eingehalten, kein fristgerechter Termin in dieser Periode (null). Keine nächste Periode oder neue Zinsvereinbarung erfinden. Kündigungsrecht und formelle Wirksamkeit sind vorqualifiziert; keine Feiertagsverschiebung der Kündigungsfrist.']
    return ergebnis

