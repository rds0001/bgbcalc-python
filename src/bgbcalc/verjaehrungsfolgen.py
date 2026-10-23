"""Aufrechnungs-/Zurückbehaltungsprivileg und abhängige Nebenleistungen."""
from .betraege import _wahrheitswert
from .kalender import _auswahl, _datum, _ergebnis, _text


def verjaehrung_aufrechnung_zurueckbehaltung(
    letzter_tag_vor_verjaehrung=None, erstmals_ausuebbar_am=None,
    rechtsart=None, einordnungsnachweis=None,
):
    """§215: ursprüngliche Ausübbarkeit vor Eintritt der Verjährung als Erhaltungsbedingung."""
    fristende = _datum(letzter_tag_vor_verjaehrung, "letzter_tag_vor_verjaehrung")
    moeglich = _datum(erstmals_ausuebbar_am, "erstmals_ausuebbar_am")
    _auswahl(rechtsart, "rechtsart", ("aufrechnung", "zurueckbehaltung"))
    _text(einordnungsnachweis, "einordnungsnachweis")
    eingaben = dict(letzter_tag_vor_verjaehrung=letzter_tag_vor_verjaehrung,
        erstmals_ausuebbar_am=erstmals_ausuebbar_am, rechtsart=rechtsart, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(moeglich <= fristende, "wahrheitswert", "BGB_VERJAEHRUNG_AUFRECHNUNG_ZURUECKBEHALTUNG", eingaben,
        [dict(operation="Erstmalige rechtliche Ausübbarkeit mit letztem Tag vor Verjährung vergleichen")], eingaben.copy())
    ergebnis["annahmen"] = ["Rechtlich abschließend bestimmter letzter unverjährter Tag und tatsächliche erstmalige Ausübbarkeit des ausgewählten Rechts vorgegeben."]
    ergebnis["hinweise"] = ["TRUE bedeutet nur: spätere Verjährung schließt das bezeichnete Recht nach§215 nicht aus. Andere Voraussetzungen und Verbote bleiben bestehen. FALSE entscheidet nicht über andere Ausnahmen. Fristdatum muss alle maßgeblichen Hemmungen, Neubeginne und gegebenenfalls Werktagsverschiebung berücksichtigen; keine rohe Grundfrist einsetzen.", "Taggenau normalisierte Rechtsereignisse; keine automatische Beurteilung untertägiger Verjährungs-/Ausübungszeitpunkte. Einrede§390 nicht ohne Prüfung dieses Privilegs aus bloß späterem Fristablauf ableiten."]
    return ergebnis


def verjaehrung_abhaengige_nebenleistung(
    hauptanspruch_letzter_tag=None, nebenleistung_eigener_letzter_tag=None,
    nebenleistung_abhaengig=None, fristnachweis=None,
):
    """§217: Nebenleistung spätestens mit Hauptanspruch, frühere eigene Verjährung bleibt bestehen."""
    haupt = _datum(hauptanspruch_letzter_tag, "hauptanspruch_letzter_tag")
    neben = _datum(nebenleistung_eigener_letzter_tag, "nebenleistung_eigener_letzter_tag")
    _wahrheitswert(nebenleistung_abhaengig, "nebenleistung_abhaengig")
    _text(fristnachweis, "fristnachweis")
    eingaben = dict(hauptanspruch_letzter_tag=hauptanspruch_letzter_tag,
        nebenleistung_eigener_letzter_tag=nebenleistung_eigener_letzter_tag,
        nebenleistung_abhaengig=nebenleistung_abhaengig, fristnachweis=fristnachweis)
    wert = min(haupt, neben).isoformat() if nebenleistung_abhaengig else None
    ergebnis = _ergebnis(wert, "datum", "BGB_VERJAEHRUNG_ABHAENGIGE_NEBENLEISTUNG", eingaben,
        [dict(operation="Bei abhängiger Nebenleistung früheren letzten Tag aus Hauptanspruch und eigener Verjährung wählen")], eingaben.copy())
    ergebnis["status"] = "BERECHNET" if nebenleistung_abhaengig else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = ["Abhängigkeit der Nebenleistung und beide maßgeblichen Fristläufe rechtlich geprüft; feste lokale BGB-Fassung."]
    ergebnis["hinweise"] = ["Nicht jede Forderung zwischen denselben Parteien ist abhängige Nebenleistung. Beide eingegebenen letzten Tage müssen ihre jeweiligen Hemmungen, Neubeginne und sonstigen Veränderungen bereits zutreffend berücksichtigen. Keine erneute Addition der Hemmungen zu diesem Minimum; keine automatische Feststellung einer erhobenen Verjährungseinrede."]
    return ergebnis
