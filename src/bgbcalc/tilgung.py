"""Zahlungsanrechnung auf Bestandteile einer bereits ausgewählten Schuld."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _fehler
from .zahlen import _bruch, _subtrahieren
from .zinsen import _bruchteile


def _anrechnen(zahlung, forderungen, reihenfolge):
    restzahlung = zahlung
    zuordnungen = []
    for position in reihenfolge:
        forderung = forderungen[position]
        betrag = min(restzahlung, forderung)
        restzahlung = _subtrahieren(restzahlung, betrag)
        zuordnungen.append(dict(position=position, betrag=_bruchteile(betrag),
                               restforderung=_bruchteile(_subtrahieren(forderung, betrag))))
    return dict(zuordnungen=zuordnungen, nicht_zugeordnet=_bruchteile(restzahlung))


def _tilgungsergebnis(zahlung, forderungen, reihenfolge, anwendbar, regel_id, eingaben):
    ergebnis = _geld_ergebnis(
        _bruch(0) if anwendbar else None, regel_id, eingaben,
        [{"operation": "Tilgungsregel anwendbar", "anwendbar": anwendbar},
         {"operation": "Zahlung in Reihenfolge bis zur Forderungshöhe zuordnen",
          "reihenfolge": reihenfolge}])
    ergebnis["wert"] = _anrechnen(zahlung, forderungen, reihenfolge) if anwendbar else None
    ergebnis["hinweise"] = [
        "Schuld und ersatzfähige Bestandteile sind vorab bestimmt; keine automatische Bewertung.",
        "Nicht zugeordnete Zahlung ist rechnerischer Überschuss, keine Entscheidung über Erstattungsansprüche.",
        "Alle Teilbeträge exakt ohne automatische Cent-Rundung.",
    ]
    return ergebnis


def zahlung_anrechnen(zahlung=None, kosten=None, zinsen=None, hauptforderung=None,
                     abweichende_reihenfolge=None, annahme_abgelehnt=None):
    """§ 367: Kosten vor Zinsen vor Hauptforderung, vorbehaltlich Bestimmung."""
    eingaben = dict(zahlung=zahlung, kosten=kosten, zinsen=zinsen, hauptforderung=hauptforderung,
                    abweichende_reihenfolge=abweichende_reihenfolge, annahme_abgelehnt=annahme_abgelehnt)
    betrag = _geld(zahlung)
    reihenfolge = ["kosten", "zinsen", "hauptforderung"]
    forderungen = {name: _geld(eingaben[name]) for name in reihenfolge}
    _wahrheitswert(annahme_abgelehnt, "annahme_abgelehnt")
    if abweichende_reihenfolge is not None:
        if (not isinstance(abweichende_reihenfolge, list)
                or any(not isinstance(x, str) for x in abweichende_reihenfolge)
                or sorted(abweichende_reihenfolge) != sorted(reihenfolge)):
            _fehler("abweichende_reihenfolge", "Jede der drei Positionen genau einmal als Liste erforderlich.")
        abweichend = abweichende_reihenfolge != reihenfolge
        reihenfolge = abweichende_reihenfolge.copy()
    else:
        abweichend = False
    if annahme_abgelehnt and not abweichend:
        _fehler("annahme_abgelehnt", "Ablehnung nach § 367 Abs. 2 setzt abweichende Bestimmung voraus.")
    return _tilgungsergebnis(betrag, forderungen, reihenfolge, not annahme_abgelehnt,
                            "BGB_ZAHLUNG_ANRECHNUNG", eingaben)


def verbraucherdarlehen_zahlung_anrechnen(
    zahlung=None, rechtsverfolgungskosten=None, uebriger_geschuldeter_betrag=None,
    verzugszinsen=None, immobiliar_verbraucherdarlehen=None,
    titel_hauptforderung_zinsen=None, schuldnerverzug=None,
):
    """§ 497: Rechtsverfolgungskosten vor übrigem Betrag vor Verzugszinsen."""
    eingaben = dict(
        zahlung=zahlung, rechtsverfolgungskosten=rechtsverfolgungskosten,
        uebriger_geschuldeter_betrag=uebriger_geschuldeter_betrag, verzugszinsen=verzugszinsen,
        immobiliar_verbraucherdarlehen=immobiliar_verbraucherdarlehen,
        titel_hauptforderung_zinsen=titel_hauptforderung_zinsen, schuldnerverzug=schuldnerverzug,
    )
    betrag = _geld(zahlung)
    reihenfolge = ["rechtsverfolgungskosten", "uebriger_geschuldeter_betrag", "verzugszinsen"]
    forderungen = {name: _geld(eingaben[name]) for name in reihenfolge}
    for parameter in ("immobiliar_verbraucherdarlehen", "titel_hauptforderung_zinsen", "schuldnerverzug"):
        _wahrheitswert(eingaben[parameter], parameter)
    anwendbar = schuldnerverzug and not immobiliar_verbraucherdarlehen and not titel_hauptforderung_zinsen
    return _tilgungsergebnis(betrag, forderungen, reihenfolge, anwendbar,
                            "BGB_DARLEHEN_ZAHLUNG_ANRECHNUNG", eingaben)
