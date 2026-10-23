"""Finderlohn und gesetzliche Gastwirtshaftung mit getrennten Ausschlusszweigen."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _auswahl, _fehler
from .zahlen import _addieren, _bruch, _multiplizieren, _subtrahieren


def finderlohn_betrag(sachwert=None, tier=None, nur_persoenlicher_wert=None,
                     billiger_finderlohn=None, fundort=None, bediensteter=None,
                     anzeigepflicht_verletzt=None, fund_verheimlicht=None,
                     ablieferungspflicht_verletzt=None):
    """§§ 971/978: Staffel oder Tierquote, öffentlicher Fund mit halbem Betrag."""
    eingaben = dict(
        sachwert=sachwert, tier=tier, nur_persoenlicher_wert=nur_persoenlicher_wert,
        billiger_finderlohn=billiger_finderlohn, fundort=fundort, bediensteter=bediensteter,
        anzeigepflicht_verletzt=anzeigepflicht_verletzt, fund_verheimlicht=fund_verheimlicht,
        ablieferungspflicht_verletzt=ablieferungspflicht_verletzt
    )
    sachbetrag = _geld(sachwert)
    for parameter in ("tier", "nur_persoenlicher_wert", "bediensteter",
                      "anzeigepflicht_verletzt", "fund_verheimlicht", "ablieferungspflicht_verletzt"):
        _wahrheitswert(eingaben[parameter], parameter)
    _auswahl(fundort, "fundort", ("allgemein", "behoerde_oder_verkehrsanstalt"))
    billiger_betrag = _geld(billiger_finderlohn) if nur_persoenlicher_wert else None
    if not nur_persoenlicher_wert and billiger_finderlohn is not None:
        _fehler("billiger_finderlohn", "Bewertung nur bei ausschließlich persönlichem Wert zulässig.")
    oeffentlich = fundort == "behoerde_oder_verkehrsanstalt"
    ausgeschlossen = (
        (sachbetrag < _bruch(50) or bediensteter or ablieferungspflicht_verletzt)
        if oeffentlich else (anzeigepflicht_verletzt or fund_verheimlicht)
    )
    schritte = [{"operation": "Fundortbezogene Ausschlüsse", "ausgeschlossen": ausgeschlossen}]
    wert = None
    if not ausgeschlossen:
        if nur_persoenlicher_wert:
            wert = billiger_betrag
            schritte.append({"operation": "Billige Bemessung als Nutzervorgabe, nicht automatisch ermittelt"})
        elif tier:
            wert = _multiplizieren(sachbetrag, _bruch(3, 100))
            schritte.append({"operation": "Tierwert mal 3/100"})
        else:
            grundwert = min(sachbetrag, _bruch(500))
            mehrwert = max(_subtrahieren(sachbetrag, _bruch(500)), _bruch(0))
            wert = _addieren(_multiplizieren(grundwert, _bruch(5, 100)),
                             _multiplizieren(mehrwert, _bruch(3, 100)))
            schritte.append({"operation": "Bis 500 EUR mal 5/100, Mehrwert mal 3/100"})
        if oeffentlich:
            wert = _multiplizieren(wert, _bruch(1, 2))
            schritte.append({"operation": "Öffentlicher Fund: Betrag halbieren"})
    ergebnis = _geld_ergebnis(wert, "BGB_FINDERLOHN_BETRAG", eingaben, schritte,
                             {"billiger_finderlohn": billiger_finderlohn} if nur_persoenlicher_wert else {})
    ergebnis["hinweise"].append("Betragsberechnung entscheidet nicht Durchsetzbarkeit nach § 1001 oder Erlöschen nach § 978 Abs. 3.")
    return ergebnis


def gastwirt_haftungsbetrag(beherbergungspreis_tag=None, schaden=None,
                           beherbergung_gewerblich=None, eingebracht_nach_701=None,
                           sachenart=None, ursache=None, verschulden_gastwirt_oder_leute=None,
                           aufbewahrung_uebernommen=None, aufbewahrung_pflichtwidrig_abgelehnt=None,
                           anzeige_unverzueglich=None):
    """§§ 701–703: tatsächlichen Schaden begrenzen oder unbeschränkt ersetzen."""
    eingaben = dict(
        beherbergungspreis_tag=beherbergungspreis_tag, schaden=schaden,
        beherbergung_gewerblich=beherbergung_gewerblich, eingebracht_nach_701=eingebracht_nach_701,
        sachenart=sachenart, ursache=ursache,
        verschulden_gastwirt_oder_leute=verschulden_gastwirt_oder_leute,
        aufbewahrung_uebernommen=aufbewahrung_uebernommen,
        aufbewahrung_pflichtwidrig_abgelehnt=aufbewahrung_pflichtwidrig_abgelehnt,
        anzeige_unverzueglich=anzeige_unverzueglich
    )
    preis, schadensbetrag = _geld(beherbergungspreis_tag), _geld(schaden)
    for parameter in ("beherbergung_gewerblich", "eingebracht_nach_701",
                      "verschulden_gastwirt_oder_leute", "aufbewahrung_uebernommen",
                      "aufbewahrung_pflichtwidrig_abgelehnt", "anzeige_unverzueglich"):
        _wahrheitswert(eingaben[parameter], parameter)
    _auswahl(sachenart, "sachenart", ("sonstige", "geld_wertpapiere_kostbarkeiten",
                                     "fahrzeug", "fahrzeuginhalt", "lebendes_tier"))
    _auswahl(ursache, "ursache", ("sonstige", "gast", "begleiter", "aufgenommene_person",
                                 "sachbeschaffenheit", "hoehere_gewalt"))
    ausgeschlossen = (
        not beherbergung_gewerblich or not eingebracht_nach_701 or ursache != "sonstige"
        or sachenart in ("fahrzeug", "fahrzeuginhalt", "lebendes_tier")
    )
    erloschen = not (anzeige_unverzueglich or aufbewahrung_uebernommen or verschulden_gastwirt_oder_leute)
    schritte = [{"operation": "Gesetzlichen Anwendungsbereich und Ausschlüsse prüfen", "ausgeschlossen": ausgeschlossen},
                {"operation": "Anzeige und Ausnahmen nach § 703 prüfen", "erloschen": erloschen}]
    wert = None
    if not ausgeschlossen and not erloschen:
        unbeschraenkt = (verschulden_gastwirt_oder_leute or aufbewahrung_uebernommen
                        or aufbewahrung_pflichtwidrig_abgelehnt)
        if unbeschraenkt:
            wert = schadensbetrag
            schritte.append({"operation": "Unbeschränkte Haftung nach § 702 Abs. 2 bis zum Schaden"})
        else:
            obergrenze = _bruch(800 if sachenart == "geld_wertpapiere_kostbarkeiten" else 3500)
            # Bei ausreichend hohem Preis steht die Kappung bereits fest; unnötiges
            # großes Zwischenprodukt vermeiden.
            grenze = (obergrenze if preis >= obergrenze / 100 else
                      min(max(_multiplizieren(preis, _bruch(100)), _bruch(600)), obergrenze))
            wert = min(schadensbetrag, grenze)
            schritte.append({"operation": "100 Tagespreise, mindestens 600, höchstens 3500/800; Schaden deckeln",
                             "haftungsgrenze": {"zaehler": str(grenze.numerator), "nenner": str(grenze.denominator)}})
    return _geld_ergebnis(wert, "BGB_GASTWIRT_HAFTUNGSBETRAG", eingaben, schritte)
