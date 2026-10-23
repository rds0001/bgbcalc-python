"""Positionsweise Preis- und Zahlungsabrechnung nach §651lII."""
from .betraege import _geld
from .kalender import _auswahl, _ergebnis, _fehler, _text, _vorhanden
from .zahlen import _addieren, _bruch, _subtrahieren
from .zinsen import _bruchteile


def pauschalreise_beendigung_preisabrechnung(reiseleistungen=None, einordnungsnachweis=None):
    """Behaltenen Preis, entfallenen Preis, Erstattung und offene Zahlung getrennt summieren."""
    _vorhanden(reiseleistungen,'reiseleistungen')
    if not isinstance(reiseleistungen,list) or not 1 <= len(reiseleistungen) <= 1000:
        _fehler('reiseleistungen','Liste mit1bis1000 eindeutig abgegrenzten Preis-/Zahlungspositionen erforderlich.')
    _text(einordnungsnachweis,'einordnungsnachweis')
    namen=[];behalten=_bruch(0);entfallen=_bruch(0);erstattung=_bruch(0);offen=_bruch(0)
    for leistung in reiseleistungen:
        if not isinstance(leistung,dict) or set(leistung)!={'leistung_id','preisanteil','gezahlter_anteil','leistungsstatus'}:
            _fehler('reiseleistungen','Genau leistung_id, preisanteil, gezahlter_anteil und leistungsstatus erforderlich.')
        name=_text(leistung['leistung_id'],'leistung_id')
        if name in namen:
            _fehler('leistung_id','Leistung darf nicht mehrfach abgerechnet werden.')
        namen.append(name)
        preis=_geld(leistung['preisanteil']);bezahlt=_geld(leistung['gezahlter_anteil'])
        _auswahl(leistung['leistungsstatus'],'leistungsstatus',('erbracht','zur_beendigung_noch_zu_erbringen','entfaellt'))
        if bezahlt > preis:
            _fehler('gezahlter_anteil','Preisüberschreitende Zahlungen erfordern gesonderte rechtliche Zuordnung.')
        if leistung['leistungsstatus']=='entfaellt':
            entfallen=_addieren(entfallen,preis);erstattung=_addieren(erstattung,bezahlt)
        else:
            behalten=_addieren(behalten,preis);offen=_addieren(offen,_subtrahieren(preis,bezahlt))
    wert=dict(verbleibender_preisanspruch=_bruchteile(behalten),entfallender_preisanspruch=_bruchteile(entfallen),zu_erstattende_zahlungen=_bruchteile(erstattung),offene_zahlung_auf_verbleibenden_preis=_bruchteile(offen))
    eingaben=dict(reiseleistungen=reiseleistungen,einordnungsnachweis=einordnungsnachweis)
    ergebnis=_ergebnis(wert,'EUR','BGB_PAUSCHALREISE_BEENDIGUNG_PREISABRECHNUNG',eingaben,[dict(operation='Preis-/Zahlungsanteile nach qualifiziertem Leistungsstatus getrennt summieren; keine automatische Aufrechnung.')],eingaben.copy())
    ergebnis['hinweise']=['Nur wirksame Kündigung nach651l; Preis- und Zahlungsanteile sämtlicher Leistungen rechtlich zutreffend und überschneidungsfrei zuordnen. Keine pauschale Tagesquote für unterschiedlich bepreiste Leistungen. Teilweise erbrachte Leistungen in sachgerecht bewertete getrennte Positionen aufteilen. Mehrkosten notwendiger Rückbeförderung trägt nachAbsatz3 der Veranstalter; nicht als zusätzlichen Preisanteil des Reisenden einstellen. Minderung und Schadensersatz bleiben gesondert; keine doppelte Erstattung derselben Zahlung. Offene Preisforderung und Rückzahlung werden getrennt ausgegeben, ohne rechtliche Aufrechnung zu unterstellen. Preisüberschreitende Zahlungen und nicht zuordenbare Zahlungen außerhalb dieses Modells.']
    return ergebnis
