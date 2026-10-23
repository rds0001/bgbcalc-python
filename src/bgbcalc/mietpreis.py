"""Mietpreisbegrenzung: Ausnahmen und getrennte Betragswege nach §§ 556d–556f."""
from datetime import date

from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _datum, _ergebnis, _text
from .zahlen import _bruch, _multiplizieren


def mietpreisbegrenzung_ausnahmen(
    erstmalige_nutzung=None, erstmalige_vermietung=None,
    erste_vermietung_nach_umfassender_modernisierung=None,
    bewertungsnachweis=None,
):
    """§556f: Datumsgrenze und bewertete umfassende Modernisierung."""
    nutzung = _datum(erstmalige_nutzung, "erstmalige_nutzung")
    vermietung = _datum(erstmalige_vermietung, "erstmalige_vermietung")
    _wahrheitswert(erste_vermietung_nach_umfassender_modernisierung,
                  "erste_vermietung_nach_umfassender_modernisierung")
    _text(bewertungsnachweis, "bewertungsnachweis")
    eingaben = dict(erstmalige_nutzung=erstmalige_nutzung,
        erstmalige_vermietung=erstmalige_vermietung,
        erste_vermietung_nach_umfassender_modernisierung=erste_vermietung_nach_umfassender_modernisierung,
        bewertungsnachweis=bewertungsnachweis)
    neufall = nutzung > date(2014, 10, 1) and vermietung > date(2014, 10, 1)
    wert = dict(ausnahme_nach_satz_1=neufall,
        ausnahme_von_556d=neufall or erste_vermietung_nach_umfassender_modernisierung,
        ausnahme_von_556e_nach_satz_2=erste_vermietung_nach_umfassender_modernisierung)
    ergebnis = _ergebnis(wert, "wahrheitswerte", "BGB_MIETPREISBEGRENZUNG_AUSNAHMEN",
        eingaben, [dict(operation="Erstnutzung und Erstvermietung jeweils nach 01.10.2014 prüfen; Ausnahme der ersten Vermietung nach umfassender Modernisierung ergänzen")], eingaben.copy())
    ergebnis["annahmen"] = ["Feste lokale BGB-Fassung; rechtlich maßgebliche Erstnutzung und Erstvermietung sowie umfassende Modernisierung extern eingeordnet."]
    ergebnis["hinweise"] = ["Nur §556f, keine automatische Prüfung von Übergangsrecht, örtlicher Verordnung oder vorvertraglichen Auskunftspflichten nach §556g.",
        "Satz1 nennt ausdrücklich §556d; ein FALSE für die Ausnahme von §556e nach Satz2 bedeutet nicht, dass §556e ohne seine Voraussetzungen angewendet wird."]
    return ergebnis


def mietpreisbegrenzung_grundbetrag(
    ortsuebliche_vergleichsmiete=None, gebiet_rechtswirksam_bestimmt=None,
    ausnahme_von_556d=None, anwendungsnachweis=None,
):
    """§556d Absatz1: 110 Prozent der vorgegebenen ortsüblichen Vergleichsmiete."""
    vergleich = _geld(ortsuebliche_vergleichsmiete)
    _wahrheitswert(gebiet_rechtswirksam_bestimmt, "gebiet_rechtswirksam_bestimmt")
    _wahrheitswert(ausnahme_von_556d, "ausnahme_von_556d")
    _text(anwendungsnachweis, "anwendungsnachweis")
    eingaben = dict(ortsuebliche_vergleichsmiete=ortsuebliche_vergleichsmiete,
        gebiet_rechtswirksam_bestimmt=gebiet_rechtswirksam_bestimmt,
        ausnahme_von_556d=ausnahme_von_556d, anwendungsnachweis=anwendungsnachweis)
    wert = None
    if gebiet_rechtswirksam_bestimmt and not ausnahme_von_556d:
        wert = _multiplizieren(vergleich, _bruch(11, 10))
    ergebnis = _geld_ergebnis(wert, "BGB_MIETPREISBEGRENZUNG_GRUNDBETRAG", eingaben,
        [dict(operation="Ortsübliche Vergleichsmiete bei Anwendbarkeit mit 110 Prozent multiplizieren")])
    ergebnis["hinweise"].append("Grundbetrag nach §556d Absatz1; höhere Grenzen nach §556e, Auskunftspflichten und Rechtsfolgen nach §556g gesondert. Kein automatisch abschließend zulässiger Mietpreis.")
    return ergebnis


def mietpreisbegrenzung_vormietgrenze(
    grundbetrag_556d=None, beruecksichtigungsfaehige_vormiete=None,
    vormietprivileg_nutzbar=None, vormietnachweis=None,
):
    """§556e Absatz1: höhere bereinigte Vormiete, soweit das Privileg nutzbar ist."""
    grundbetrag = _geld(grundbetrag_556d)
    vormiete = _geld(beruecksichtigungsfaehige_vormiete)
    _wahrheitswert(vormietprivileg_nutzbar, "vormietprivileg_nutzbar")
    _text(vormietnachweis, "vormietnachweis")
    eingaben = dict(grundbetrag_556d=grundbetrag_556d,
        beruecksichtigungsfaehige_vormiete=beruecksichtigungsfaehige_vormiete,
        vormietprivileg_nutzbar=vormietprivileg_nutzbar, vormietnachweis=vormietnachweis)
    wert = max(grundbetrag, vormiete) if vormietprivileg_nutzbar else grundbetrag
    ergebnis = _geld_ergebnis(wert, "BGB_MIETPREISBEGRENZUNG_VORMIETGRENZE", eingaben,
        [dict(operation="Grundbetrag und berücksichtigungsfähige Vormiete vergleichen; ohne nutzbares Privileg beim Grundbetrag bleiben")])
    ergebnis["hinweise"].append("Nur Vormietweg nach §556e Absatz1. Vormiete muss Mietminderungen und im letzten Jahr vor Beendigung vereinbarte Mieterhöhungen bereits gesetzeskonform bereinigen. Kein zusätzlicher Modernisierungsaufschlag auf diese Vormietgrenze.")
    return ergebnis
