"""Rückstand und aufeinanderfolgende Verzugsraten nach § 498."""

from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _fehler, _ganzzahl
from .zahlen import _bruch, _multiplizieren
from .zinsen import _bruchteile


def verbraucherdarlehen_verzugsschwelle(
    nennbetrag=None,
    massgeblicher_rueckstand=None,
    vertragslaufzeit_jahre=None,
    anzahl_aufeinanderfolgender_verzugsraten=None,
    immobiliar_verbraucherdarlehen=None,
    teilzahlungsdarlehen=None,
):
    """§ 498 Abs. 1 Nr. 1 und Abs. 2; Nachfrist und Kündigung gesondert."""
    nennwert = _geld(nennbetrag)
    if nennwert == 0:
        _fehler("nennbetrag", "Positiver Nennbetrag erforderlich.")
    rueckstand = _geld(massgeblicher_rueckstand)
    anzahl = _ganzzahl(
        anzahl_aufeinanderfolgender_verzugsraten,
        "anzahl_aufeinanderfolgender_verzugsraten", 0, 9007199254740991,
    )
    _wahrheitswert(immobiliar_verbraucherdarlehen, "immobiliar_verbraucherdarlehen")
    _wahrheitswert(teilzahlungsdarlehen, "teilzahlungsdarlehen")
    dauer = None
    if not immobiliar_verbraucherdarlehen or vertragslaufzeit_jahre is not None:
        dauer = _geld(vertragslaufzeit_jahre)
        if dauer == 0:
            _fehler("vertragslaufzeit_jahre", "Positive Vertragslaufzeit erforderlich.")
    quote = _bruch(1, 40) if immobiliar_verbraucherdarlehen else (
        _bruch(1, 20) if dauer > 3 else _bruch(1, 10)
    )
    eingaben = dict(
        nennbetrag=nennbetrag, massgeblicher_rueckstand=massgeblicher_rueckstand,
        vertragslaufzeit_jahre=vertragslaufzeit_jahre,
        anzahl_aufeinanderfolgender_verzugsraten=anzahl_aufeinanderfolgender_verzugsraten,
        immobiliar_verbraucherdarlehen=immobiliar_verbraucherdarlehen,
        teilzahlungsdarlehen=teilzahlungsdarlehen,
    )
    wert = None
    if teilzahlungsdarlehen:
        mindestbetrag = _multiplizieren(nennwert, quote)
        erreicht = rueckstand >= mindestbetrag
        wert = dict(
            rueckstandsquote=_bruchteile(quote), mindestrueckstand=_bruchteile(mindestbetrag),
            rueckstandsschwelle_erreicht=erreicht,
            mindestens_zwei_aufeinanderfolgende_raten=anzahl >= 2,
            voraussetzungen_nummer_1_erfuellt=erreicht and anzahl >= 2,
        )
    ergebnis = _geld_ergebnis(
        _bruch(0) if teilzahlungsdarlehen else None, "BGB_VERBRAUCHERDARLEHEN_VERZUGSSCHWELLE",
        eingaben, [dict(operation="Nennbetragsquote und mindestens zwei aufeinanderfolgende Verzugsraten prüfen",
                        ergebnis=wert)],
    )
    ergebnis["wert"] = wert
    ergebnis["hinweise"] = [
        "Nur Rückstandsvoraussetzungen nach § 498 Absatz 1 Satz 1 Nummer 1 und Absatz 2; kein festgestelltes Kündigungsrecht.",
        "Erfolglose zweiwöchige Nachfrist mit Restschuldandrohung nach Nummer 2 und weitere Voraussetzungen gesondert prüfen.",
        "Maßgeblicher Rückstand und aufeinanderfolgende ganz oder teilweise im Verzug befindliche Raten sind rechtlich bewertete Nutzervorgaben.",
        "Gesamte vereinbarte Vertragslaufzeit, keine Restlaufzeit und keine pauschale Umrechnung von Kalendertagen in Jahre.",
        "Mindestrückstand in EUR, Quote dimensionslos; keine automatische Cent-Rundung.",
    ]
    return ergebnis
