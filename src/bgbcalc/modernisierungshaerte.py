"""Auswahl der Härteabwägung nach §§ 559 und 559c."""

from .betraege import _geld, _wahrheitswert
from .kalender import _ergebnis
from .zahlen import _bruch, _multiplizieren


def modernisierung_haerteberuecksichtigung(
    vereinfachtes_verfahren=None,
    qualifizierter_heizungseinbau=None,
    allgemein_ueblicher_zustand=None,
    umstaende_nicht_zu_vertreten=None,
    haerteumstaende_rechtzeitig_mitgeteilt=None,
    angekuendigter_erhoehungsbetrag=None,
    tatsaechlicher_erhoehungsbetrag=None,
):
    """Ausnahmen der Härteabwägung und strikte Zehnprozentgrenze auswerten."""
    eingaben = dict(
        vereinfachtes_verfahren=vereinfachtes_verfahren,
        qualifizierter_heizungseinbau=qualifizierter_heizungseinbau,
        allgemein_ueblicher_zustand=allgemein_ueblicher_zustand,
        umstaende_nicht_zu_vertreten=umstaende_nicht_zu_vertreten,
        haerteumstaende_rechtzeitig_mitgeteilt=haerteumstaende_rechtzeitig_mitgeteilt,
        angekuendigter_erhoehungsbetrag=angekuendigter_erhoehungsbetrag,
        tatsaechlicher_erhoehungsbetrag=tatsaechlicher_erhoehungsbetrag,
    )
    for name in (
        "vereinfachtes_verfahren", "qualifizierter_heizungseinbau",
        "allgemein_ueblicher_zustand", "umstaende_nicht_zu_vertreten",
        "haerteumstaende_rechtzeitig_mitgeteilt",
    ):
        _wahrheitswert(eingaben[name], name)
    angekuendigt = _geld(angekuendigter_erhoehungsbetrag)
    tatsaechlich = _geld(tatsaechlicher_erhoehungsbetrag)
    ueberschreitung = tatsaechlich > _multiplizieren(angekuendigt, _bruch(11, 10))
    vereinfachungsausschluss = vereinfachtes_verfahren and not qualifizierter_heizungseinbau
    umstandsausschluss = umstaende_nicht_zu_vertreten and not qualifizierter_heizungseinbau
    abwaegung = not (
        vereinfachungsausschluss or allgemein_ueblicher_zustand or umstandsausschluss
    )
    mitteilung = haerteumstaende_rechtzeitig_mitgeteilt or ueberschreitung
    wert = dict(
        abwaegung_vorgesehen=abwaegung,
        umstaende_beruecksichtigungsfaehig=abwaegung and mitteilung,
        zehnprozentgrenze_ueberschritten=ueberschreitung,
    )
    ergebnis = _ergebnis(
        wert, "tatbestand", "BGB_MODERNISIERUNG_HAERTEBERUECKSICHTIGUNG", eingaben,
        [{"operation": "Abwägungsausschluss durch vereinfachtes Verfahren",
          "erfuellt": vereinfachungsausschluss},
         {"operation": "Abwägungsausschluss durch nicht zu vertretende Umstände",
          "erfuellt": umstandsausschluss},
         {"operation": "Abwägungsausschluss durch lediglich allgemein üblichen Zustand",
          "erfuellt": allgemein_ueblicher_zustand},
         {"operation": "Rechtzeitige Mitteilung oder mehr als zehn Prozent Überschreitung",
          "erfuellt": mitteilung}],
        eingaben.copy(),
    )
    ergebnis["annahmen"] = [
        "Feste lokale BGB-Fassung; rechtliche und technische Einordnungen sind ausdrückliche Nutzervorgaben."
    ]
    ergebnis["hinweise"] = [
        "Keine Bewertung der Härte, künftiger Betriebskosten oder berechtigter Vermieterinteressen.",
        "Berücksichtigungsfähigkeit ist kein Beleg einer tatsächlich unzumutbaren Härte oder eines bestimmten Erhöhungsbetrags."
    ]
    return ergebnis
