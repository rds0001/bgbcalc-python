"""Mindestdauer aufeinanderfolgender Mietstaffeln nach §557a Absatz2 Satz1."""
from .kalender import _datum, _ergebnis, _fehler, _frist, _tage_addieren, _text, _vorhanden


def staffelmiete_mindestabstaende(staffeln=None, vereinbarungsnachweis=None):
    """Prüft den Jahresabstand einer vollständig vorgegebenen Folge von Staffelbeginnen."""
    _vorhanden(staffeln, "staffeln")
    if not isinstance(staffeln, list) or not 2 <= len(staffeln) <= 1000:
        _fehler("staffeln", "Liste von zwei bis tausend Staffelbeginnen erforderlich.")
    _text(vereinbarungsnachweis, "vereinbarungsnachweis")
    daten = [_datum(beginn, "staffeln") for beginn in staffeln]
    if any(rechts <= links for links, rechts in zip(daten, daten[1:])):
        _fehler("staffeln", "Staffelbeginne müssen streng aufsteigend sein.")
    pruefungen = []
    for stelle in range(1, len(staffeln)):
        fruehestens = _tage_addieren(_frist(staffeln[stelle - 1], 1, "jahre", "tagesbeginn"), 1)
        pruefungen.append(dict(staffelnummer=stelle + 1, fruehester_beginn=fruehestens.isoformat(),
            jahresabstand_eingehalten=daten[stelle] >= fruehestens))
    wert = dict(alle_jahresabstaende_eingehalten=all(p["jahresabstand_eingehalten"] for p in pruefungen),
        staffelpruefungen=pruefungen)
    eingaben = dict(staffeln=staffeln, vereinbarungsnachweis=vereinbarungsnachweis)
    ergebnis = _ergebnis(wert, "kalenderpruefungen", "BGB_STAFFELMIETE_MINDESTABSTAENDE",
        eingaben, [dict(operation="Für jeden Staffelwechsel frühesten Beginn nach einem vollen Jahr unveränderter Miete bestimmen")], eingaben.copy())
    ergebnis["annahmen"] = ["Staffelbeginne gelten jeweils ab Tagesbeginn; vollständige zeitlich geordnete Folge rechtlich als Staffelmietvereinbarung eingeordnet."]
    ergebnis["hinweise"] = ["Nur Mindestabstände nach §557a Absatz2 Satz1; keine Prüfung von Schriftform, Geldbetragsangaben, Kündigungsausschluss, zulässigen Miethöhen oder Rechtsfolgen fehlerhafter Staffeln.",
        "Beginn einer Mietstaffel wird nicht wegen Sonnabend, Sonntag oder Feiertag verschoben; Zahlungstermine sind gesondert."]
    return ergebnis
