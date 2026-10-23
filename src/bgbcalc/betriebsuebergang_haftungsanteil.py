from .kalender import _datum, _ergebnis, _fehler, _frist, _text
from .betraege import _geld, _wahrheitswert
from .zahlen import _dividieren, _multiplizieren
from .zinsen import _bruchteile

def betriebsuebergang_bisheriger_arbeitgeber_haftungsbetrag(betriebsuebergang_am=None, faellig_am=None, nach_uebergang_faellig=None, verpflichtungsbetrag=None, abgelaufene_bemessungseinheiten=None, gesamte_bemessungseinheiten=None, einordnungsnachweis=None):
    """Fälligkeitszeitgrenze und zeitanteiligen Haftungsumfang des bisherigen Arbeitgebers berechnen."""
    uebergang=_datum(betriebsuebergang_am,'betriebsuebergang_am');faellig=_datum(faellig_am,'faellig_am');_wahrheitswert(nach_uebergang_faellig,'nach_uebergang_faellig');_text(einordnungsnachweis,'einordnungsnachweis')
    betrag=_geld(verpflichtungsbetrag);teil=_geld(abgelaufene_bemessungseinheiten);gesamt=_geld(gesamte_bemessungseinheiten)
    if gesamt<=0 or teil>gesamt: _fehler('bemessungseinheiten','Positiver Gesamtumfang und Teil höchstens Gesamtumfang erforderlich.')
    if (nach_uebergang_faellig and faellig<uebergang) or (not nach_uebergang_faellig and faellig>uebergang): _fehler('nach_uebergang_faellig','Zeitliche Einordnung widerspricht Kalendertagen.')
    ende=_frist(betriebsuebergang_am,1,'jahre','ereignis')
    haftung=betrag if not nach_uebergang_faellig else (_multiplizieren(betrag,_dividieren(teil,gesamt)) if faellig<=ende else _geld('0'))
    wert=dict(einjahresgrenze_letzter_tag=ende.isoformat(),haftungsbetrag_bisheriger_arbeitgeber=_bruchteile(haftung))
    eingaben = dict(betriebsuebergang_am=betriebsuebergang_am, faellig_am=faellig_am, nach_uebergang_faellig=nach_uebergang_faellig, verpflichtungsbetrag=verpflichtungsbetrag, abgelaufene_bemessungseinheiten=abgelaufene_bemessungseinheiten, gesamte_bemessungseinheiten=gesamte_bemessungseinheiten, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'datum_und_EUR','BGB_BETRIEBSUEBERGANG_BISHERIGER_ARBEITGEBER_HAFTUNGSBETRAG',eingaben,[dict(operation='Fälligkeitszeitgrenze und zeitanteiligen Haftungsumfang des bisherigen Arbeitgebers berechnen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§613aII: Vor Übergang fällige qualifizierte Verpflichtung in voller Höhe; später fällige nur bis zur gesetzlichen Einjahresgrenze und im Verhältnis des bereits abgelaufenen zum gesamten Bemessungszeitraum. Fristende nach187I/188; Datumsgleichheit zum letzten Tag gilt nur bei rechtlich qualifizierter Fälligkeit vor dessen Ablauf. Ausgabe ist Umfang der gesamtschuldnerischen Haftung des bisherigen Arbeitgebers; keine hälftige Aufteilung und kein zusätzlicher Anspruch neben dem Gesamtbetrag. Übrige Haftungsgrundlagen und Innenausgleich nicht entschieden. Beide Zeiteinheiten auch im Vollhaftungsfall angeben; keine automatische Bewertung oder zeitliche Entstehung der Verpflichtung.']
    return ergebnis

