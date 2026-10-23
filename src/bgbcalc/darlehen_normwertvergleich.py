from .kalender import _auswahl, _ergebnis, _text
from .betraege import _geld
from .zahlen import _zahleneingabe, _subtrahieren
from .zinsen import _bruchteile

def darlehen_normwertvergleich(vergleichsfall=None, zu_pruefender_wert=None, massgeblicher_vergleichswert=None, einordnungsnachweis=None):
    """Qualifizierte Zins- oder Betragswerte exakt vergleichen; strikte und einschließlich geltende gesetzliche Grenzen unterscheiden."""
    _auswahl(vergleichsfall,'vergleichsfall',('arbeitgeber_effektivzins_491','oeffentlich_sollzins_491','umschuldung_effektivzins_655c','rueckzahlungsvereinbarung_gesamtbetrag_495'));_text(einordnungsnachweis,'einordnungsnachweis')
    lesen=_geld if vergleichsfall=='rueckzahlungsvereinbarung_gesamtbetrag_495' else _zahleneingabe
    links=lesen(zu_pruefender_wert);rechts=lesen(massgeblicher_vergleichswert)
    streng=vergleichsfall in ('arbeitgeber_effektivzins_491','rueckzahlungsvereinbarung_gesamtbetrag_495')
    wert=dict(differenz=_bruchteile(_subtrahieren(links,rechts)),vergleich='weniger_als' if streng else 'hoechstens',numerische_bedingung_erfuellt=links<rechts if streng else links<=rechts)
    eingaben = dict(vergleichsfall=vergleichsfall, zu_pruefender_wert=zu_pruefender_wert, massgeblicher_vergleichswert=massgeblicher_vergleichswert, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'differenz_und_wahrheitswert','BGB_DARLEHEN_NORMWERTVERGLEICH',eingaben,[dict(operation='Qualifizierte Zins- oder Betragswerte exakt vergleichen; strikte und einschließlich geltende gesetzliche Grenzen unterscheiden.')],eingaben.copy())
    ergebnis["hinweise"] = ['Nur numerische Teilvoraussetzung nach§491II Nr4/5,§495II Nr1 oder§655c. Effektivzinsberechnung nach externem PAngV/EGBGB-Recht nicht neu erfinden; geprüfte Werte eingeben.655c: Vergleichszins des abzulösenden Darlehens ohne Vermittlungskosten, weitere Voraussetzungen Auszahlung/Widerruf/umschuldungsbezogene Vergütung separat.495: Gesamtbetrag nicht bloß neuer Nettodarlehensbetrag; Verfahrensvermeidung und Kündigungsberechtigung gesondert.491: Arbeitgeber-/Personenkreis-/Gemeinwohlbedingungen und weitere günstigere Vertragsbedingungen rechtlich qualifizieren. Zinssätze dürfen negativ sein; EUR-Gesamtbetrag und Restschuld nicht. Keine automatische Entscheidung über Verbraucherschutz oder Vergütungsanspruch.']
    return ergebnis

