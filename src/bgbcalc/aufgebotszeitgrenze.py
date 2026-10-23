from .kalender import _datum, _ergebnis, _frist, _text

def grundstuecksaufgebot_kombinierte_zeitgrenze(berechnetes_eigenbesitzfristende=None, letzte_massgebliche_zustimmungseintragung_am=None, einordnungsnachweis=None):
    """30Jährige Grundbuchruhe seit qualifizierter Zustimmungseintragung berechnen und mit bereits berechneter Besitzfrist als spätestes Ende verknüpfen."""
    besitz = _datum(berechnetes_eigenbesitzfristende,'berechnetes_eigenbesitzfristende');_text(einordnungsnachweis,'einordnungsnachweis')
    ruhe = None if letzte_massgebliche_zustimmungseintragung_am is None else _frist(letzte_massgebliche_zustimmungseintragung_am,30,'jahre','ereignis')
    wert = dict(grundbuchruhefristende=None if ruhe is None else ruhe.isoformat(),rechnerische_kombinierte_zeitgrenze=(besitz if ruhe is None else max(besitz,ruhe)).isoformat())
    eingaben = dict(berechnetes_eigenbesitzfristende=berechnetes_eigenbesitzfristende, letzte_massgebliche_zustimmungseintragung_am=letzte_massgebliche_zustimmungseintragung_am, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'daten','BGB_GRUNDSTUECKSAUFGEBOT_KOMBINIERTE_ZEITGRENZE',eingaben,[dict(operation='30Jährige Grundbuchruhe seit qualifizierter Zustimmungseintragung berechnen und mit bereits berechneter Besitzfrist als spätestes Ende verknüpfen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§927I: berechnetes Ende der30jährigen Eigenbesitzzeit mit gegebenenfalls zusätzlicher30jähriger Grundbuchruhe seit letzter eigentümerzustimmungsbedürftiger Eintragung als späteste Zeitgrenze verknüpfen. Besitzfrist zuvor einschließlich rechtlich wirksamer Hemmung, Unterbrechung und Zurechnung berechnen; ersitzung_anrechenbare_zeitkette stellt den numerischen Kern bereit. Grundbuchruhe nicht unbesehen um die Besitzhemmung verlängern. Null bei Eintragung darf keine ungeprüfte oder unbekannte Historie verdecken. Ausschließlich Zeitrechnung; kein Urteil über Tod/Verschollenheit, Aufgebotszulässigkeit, Ausschließungsbeschluss oder Eigentumserwerb. Erfüllung erst nach vollständigem Ablauf des jeweiligen Endtags; keine automatische193-Verschiebung.']
    return ergebnis

