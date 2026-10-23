"""Widerlegbare Vermutung nach § 559d aus berechneten und bewerteten Tatbeständen."""
from .betraege import _geld, _wahrheitswert
from .kalender import _ergebnis, _fehler, _text


def modernisierung_pflichtverletzungsvermutung(
    monatliche_miete=None, angekuendigte_monatliche_erhoehung=None,
    ankuendigung_nach_555c_absatz_1=None, beginnverzoegerung_nummer_1=None,
    belastungen_nummer_3=None, arbeitsruhe_nummer_4=None,
    objektiver_grund_dargelegt=None, tatbestandsnachweis=None,
):
    """Verdoppelungsschwelle, alternative Vermutungstatbestände und Gegenbeweis."""
    eingaben = dict(monatliche_miete=monatliche_miete,
        angekuendigte_monatliche_erhoehung=angekuendigte_monatliche_erhoehung,
        ankuendigung_nach_555c_absatz_1=ankuendigung_nach_555c_absatz_1,
        beginnverzoegerung_nummer_1=beginnverzoegerung_nummer_1,
        belastungen_nummer_3=belastungen_nummer_3, arbeitsruhe_nummer_4=arbeitsruhe_nummer_4,
        objektiver_grund_dargelegt=objektiver_grund_dargelegt, tatbestandsnachweis=tatbestandsnachweis)
    miete = _geld(monatliche_miete)
    if miete <= 0:
        _fehler("monatliche_miete", "Positive monatliche Vergleichsmiete erforderlich.")
    erhoehung = _geld(angekuendigte_monatliche_erhoehung)
    for name in ("ankuendigung_nach_555c_absatz_1", "beginnverzoegerung_nummer_1",
                 "belastungen_nummer_3", "arbeitsruhe_nummer_4", "objektiver_grund_dargelegt"):
        _wahrheitswert(eingaben[name], name)
    _text(tatbestandsnachweis, "tatbestandsnachweis")
    nummer_2 = ankuendigung_nach_555c_absatz_1 and erhoehung >= miete
    tatbestand = beginnverzoegerung_nummer_1 or nummer_2 or belastungen_nummer_3 or arbeitsruhe_nummer_4
    wert = dict(verdoppelung_nummer_2=nummer_2, vermutungstatbestand_erfuellt=tatbestand,
                pflichtverletzung_wird_vermutet=tatbestand and not objektiver_grund_dargelegt)
    ergebnis = _ergebnis(wert, "wahrheitswerte", "BGB_MODERNISIERUNG_PFLICHTVERLETZUNGSVERMUTUNG",
        eingaben, [dict(operation="Angekündigte Erhöhung mit bisheriger Monatsmiete vergleichen; alternative Tatbestände und objektiven Grund berücksichtigen")], eingaben.copy())
    ergebnis["annahmen"] = ["Feste lokale BGB-Fassung; sachlicher und zeitlicher Anwendungsbereich sowie Tatbestände Nummer 1, 3 und 4 rechtlich vorgegeben."]
    ergebnis["hinweise"] = ["Widerlegbare Vermutung, keine abschließende Feststellung einer Pflichtverletzung oder eines Schadenersatzanspruchs. Ein objektiver Grund muss das relevante Verhalten im Einzelfall abdecken.",
        "Keine Zeitberechnung für Nummer 1 oder 4 und keine automatische Bewertung objektiv nicht notwendiger Belastungen nach Nummer 3."]
    return ergebnis
