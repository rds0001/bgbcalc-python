"""Gesetzliche Voraussetzungen und Obergrenzen der Vorfälligkeitsentschädigung."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _auswahl, _datum, _fehler, fristende
from .zahlen import _bruch, _multiplizieren
from .zinsen import _bruchteile


def vorfaelligkeitsentschaedigung_betrag(
    vorzeitig_zurueckgezahlter_betrag=None, unmittelbarer_schaden=None,
    verbleibende_sollzinsen=None, rueckzahlungstag=None,
    vereinbarter_rueckzahlungstag=None, darlehensart=None, gebundener_sollzins=None,
    bei_abschluss_gebunden=None, versicherung_rueckzahlung=None,
    vertragsangaben_ausreichend=None,
):
    """§ 502: vorgegebenen unmittelbaren Schaden auf gesetzliche Grenzen prüfen."""
    eingaben = dict(
        vorzeitig_zurueckgezahlter_betrag=vorzeitig_zurueckgezahlter_betrag,
        unmittelbarer_schaden=unmittelbarer_schaden, verbleibende_sollzinsen=verbleibende_sollzinsen,
        rueckzahlungstag=rueckzahlungstag, vereinbarter_rueckzahlungstag=vereinbarter_rueckzahlungstag,
        darlehensart=darlehensart, gebundener_sollzins=gebundener_sollzins,
        bei_abschluss_gebunden=bei_abschluss_gebunden, versicherung_rueckzahlung=versicherung_rueckzahlung,
        vertragsangaben_ausreichend=vertragsangaben_ausreichend,
    )
    kapital = _geld(vorzeitig_zurueckgezahlter_betrag)
    schaden, zinsen = _geld(unmittelbarer_schaden), _geld(verbleibende_sollzinsen)
    tag = _datum(rueckzahlungstag, "rueckzahlungstag")
    termin = _datum(vereinbarter_rueckzahlungstag, "vereinbarter_rueckzahlungstag")
    if tag >= termin:
        _fehler("rueckzahlungstag", "Vorzeitige Rückzahlung muss vor vereinbartem Rückzahlungstag liegen.")
    _auswahl(darlehensart, "darlehensart",
             ("allgemein", "immobiliar", "eingeraeumte_ueberziehung", "geduldete_ueberziehung"))
    for parameter in ("gebundener_sollzins", "bei_abschluss_gebunden",
                      "versicherung_rueckzahlung", "vertragsangaben_ausreichend"):
        _wahrheitswert(eingaben[parameter], parameter)
    anwendbar = (
        darlehensart in ("allgemein", "immobiliar") and gebundener_sollzins
        and (darlehensart != "allgemein" or bei_abschluss_gebunden)
        and not versicherung_rueckzahlung and vertragsangaben_ausreichend
    )
    wert = schaden if anwendbar else None
    schritte = [{"operation": "Voraussetzungen und Anspruchsausschlüsse", "anwendbar": anwendbar}]
    if anwendbar and darlehensart == "allgemein":
        # Innerhalb des letzten darstellbaren Kalenderjahres liegt jeder spätere Termin unter einem Jahr.
        jahresende = fristende(rueckzahlungstag, 1, "jahre", "ereignis")["wert"] if tag.year < 9999 else None
        hoechstens_ein_jahr = jahresende is None or vereinbarter_rueckzahlungstag <= jahresende
        grenze = _multiplizieren(kapital, _bruch(1, 200 if hoechstens_ein_jahr else 100))
        wert = min(schaden, grenze, zinsen)
        schritte.append(dict(
            operation="Schaden auf Prozentgrenze und verbleibende Sollzinsen begrenzen",
            hoechstens_ein_jahr=hoechstens_ein_jahr, prozentgrenze=_bruchteile(grenze),
            sollzinsgrenze=_bruchteile(zinsen)))
    return _geld_ergebnis(wert, "BGB_VORFAELLIGKEIT_BETRAG", eingaben, schritte,
                          {"unmittelbarer_schaden": unmittelbarer_schaden,
                           "verbleibende_sollzinsen": verbleibende_sollzinsen})
