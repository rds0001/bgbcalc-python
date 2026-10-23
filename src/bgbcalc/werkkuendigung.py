"""Vergütungsrechnung bei freier Bestellerkündigung vor Vollendung."""

from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _auswahl, _fehler
from .zahlen import _addieren, _bruch, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile


def werk_bestellerkuendigung_verguetung(
    erbrachte_verguetung=None,
    nicht_erbrachte_verguetung=None,
    abrechnungsart=None,
    ersparte_aufwendungen=None,
    anderweitiger_erwerb=None,
    boeswillig_unterlassener_erwerb=None,
    bestellerkuendigung_wirksam=None,
    werk_vollendet=None,
    bautraegervertrag=None,
):
    """§ 648: konkrete Abrechnung oder gesetzliche Fünfprozentvermutung."""
    eingaben = dict(
        erbrachte_verguetung=erbrachte_verguetung,
        nicht_erbrachte_verguetung=nicht_erbrachte_verguetung,
        abrechnungsart=abrechnungsart,
        ersparte_aufwendungen=ersparte_aufwendungen,
        anderweitiger_erwerb=anderweitiger_erwerb,
        boeswillig_unterlassener_erwerb=boeswillig_unterlassener_erwerb,
        bestellerkuendigung_wirksam=bestellerkuendigung_wirksam,
        werk_vollendet=werk_vollendet,
        bautraegervertrag=bautraegervertrag,
    )
    erbracht, offen = _geld(erbrachte_verguetung), _geld(nicht_erbrachte_verguetung)
    erspart = _geld(ersparte_aufwendungen)
    anderweitig, unterlassen = _geld(anderweitiger_erwerb), _geld(boeswillig_unterlassener_erwerb)
    _auswahl(abrechnungsart, "abrechnungsart", ("vermutung", "konkret"))
    for parameter in ("bestellerkuendigung_wirksam", "werk_vollendet", "bautraegervertrag"):
        _wahrheitswert(eingaben[parameter], parameter)
    if abrechnungsart == "vermutung" and any(x != 0 for x in (erspart, anderweitig, unterlassen)):
        _fehler("abrechnungsart", "Vermutung und konkrete Abzüge nicht vermischen.")
    anwendbar = bestellerkuendigung_wirksam and not werk_vollendet and not bautraegervertrag
    schritte = [{"operation": "Freie Bestellerkündigung vor Vollendung, kein Bauträgervertrag",
                 "anwendbar": anwendbar}]
    wert = None
    if anwendbar:
        if abrechnungsart == "vermutung":
            restverguetung = _multiplizieren(offen, _bruch(1, 20))
            wert = _addieren(erbracht, restverguetung)
            schritte.append({"operation": "Erbrachte Vergütung plus fünf Prozent nicht erbrachter Vergütung",
                             "vermutete_restverguetung": _bruchteile(restverguetung)})
        else:
            gesamt = _addieren(erbracht, offen)
            abzug = _addieren(_addieren(erspart, anderweitig), unterlassen)
            wert = max(_subtrahieren(gesamt, abzug), _bruch(0))
            schritte.append({"operation": "Gesamtvergütung minus ersparte Aufwendungen und zurechenbarer Erwerb",
                             "gesamtverguetung": _bruchteile(gesamt), "anrechnung": _bruchteile(abzug)})
    return _geld_ergebnis(wert, "BGB_WERK_BESTELLERKUENDIGUNG_VERGUETUNG", eingaben, schritte)
