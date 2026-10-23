"""Zweiwöchige Nachfrist und Restschuldandrohung als Teilprüfung des § 498."""

from .betraege import _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler, _frist, _text


def verbraucherdarlehen_kuendigungsnachfrist(
    zugang_fristsetzung=None,
    massgebliches_nachfristende=None,
    prueftag=None,
    nachfristende_nachweis=None,
    fristsetzung_erfolglos=None,
    restschuldandrohung_erklaert=None,
    teilzahlungsdarlehen=None,
):
    """§ 498 Abs. 1 Satz 1 Nr. 2, ohne automatische Kündigung oder Kalenderkorrektur."""
    zugang = _datum(zugang_fristsetzung, "zugang_fristsetzung")
    ende = _datum(massgebliches_nachfristende, "massgebliches_nachfristende")
    tag = _datum(prueftag, "prueftag")
    if ende < zugang or tag < zugang:
        _fehler("nachfrist", "Fristende und Prüftag dürfen nicht vor Zugang liegen.")
    _text(nachfristende_nachweis, "nachfristende_nachweis")
    for name, wert in (
        ("fristsetzung_erfolglos", fristsetzung_erfolglos),
        ("restschuldandrohung_erklaert", restschuldandrohung_erklaert),
        ("teilzahlungsdarlehen", teilzahlungsdarlehen),
    ):
        _wahrheitswert(wert, name)
    eingaben = dict(
        zugang_fristsetzung=zugang_fristsetzung, massgebliches_nachfristende=massgebliches_nachfristende,
        prueftag=prueftag, nachfristende_nachweis=nachfristende_nachweis,
        fristsetzung_erfolglos=fristsetzung_erfolglos,
        restschuldandrohung_erklaert=restschuldandrohung_erklaert,
        teilzahlungsdarlehen=teilzahlungsdarlehen,
    )
    wert = None
    if teilzahlungsdarlehen:
        mindestende = _frist(zugang_fristsetzung, 2, "wochen", "ereignis")
        dauer = ende >= mindestende
        abgelaufen = tag > ende
        wert = dict(
            rechnerisches_mindestende=mindestende.isoformat(),
            nachfrist_mindestdauer_eingehalten=dauer,
            nachfrist_am_prueftag_abgelaufen=abgelaufen,
            voraussetzungen_nummer_2_erfuellt=(
                dauer and abgelaufen and fristsetzung_erfolglos and restschuldandrohung_erklaert
            ),
        )
    ergebnis = _ergebnis(
        wert, "datum_und_wahrheitswerte", "BGB_VERBRAUCHERDARLEHEN_KUENDIGUNGSNACHFRIST", eingaben,
        [dict(operation="Zweiwöchige Mindestdauer, tatsächlichen Ablauf, Erfolglosigkeit und Androhung prüfen",
              ergebnis=wert)], eingaben.copy(),
    )
    ergebnis["status"] = "BERECHNET" if teilzahlungsdarlehen else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = [
        "Feste lokale BGB-Fassung; Verbraucherdarlehensfall und rechtlich maßgeblicher Fristablauf einschließlich erforderlicher Kalenderkorrekturen vorgegeben."
    ]
    ergebnis["hinweise"] = [
        "Nur Nummer 2 des § 498 Absatz 1 Satz 1; Rückstandsvoraussetzungen nach Nummer 1 und weitere Voraussetzungen gesondert prüfen.",
        "Maßgebliches Fristende muss erforderliche Feiertags-/Ortskorrekturen bereits enthalten; rechnerisches_mindestende allein bestätigt keinen Ablauf.",
        "Erfolglosigkeit ist eine bewertete Nutzervorgabe zur konkreten Fristsetzung; Zahlungsledger und Rechtsfolgen verspäteter Zahlungen werden nicht ausgewertet.",
        "Am Fristendtag ist die Frist in dieser taggenauen Prüfung noch nicht abgelaufen; kein untertägiger Kündigungszeitpunkt.",
        "Gesprächsangebot nach § 498 Absatz 1 Satz 2, Kündigungserklärung und Restschuldabrechnung bleiben gesondert.",
    ]
    return ergebnis
