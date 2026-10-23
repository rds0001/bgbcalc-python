"""Mitgliederschwellen und Minderheitenverlangen im Vereinsrecht."""
from .betraege import _wahrheitswert
from .kalender import _ergebnis, _fehler, _ganzzahl, _text
from .zahlen import GRENZE, _bruch, _multiplizieren, _runden, _zahleneingabe
from .zinsen import _bruchteile


def vereins_minderheitenverlangen(
    mitgliederzahl=None, verlangende_mitglieder=None, satzungsquote=None,
    verlangen_schriftlich_begruendet=None, bestandsnachweis=None,
):
    """§37 Absatz1: Satzungsquote, sonst ein Zehntel, auf ganze Mitglieder aufrunden."""
    anzahl = _ganzzahl(mitgliederzahl, "mitgliederzahl", 1, GRENZE)
    verlangend = _ganzzahl(verlangende_mitglieder, "verlangende_mitglieder", 0, anzahl)
    quote = _bruch(1, 10) if satzungsquote is None else _zahleneingabe(satzungsquote)
    if not 0 < quote <= 1:
        _fehler("satzungsquote", "Quote größer null bis einschließlich eins erforderlich.")
    _wahrheitswert(verlangen_schriftlich_begruendet, "verlangen_schriftlich_begruendet")
    _text(bestandsnachweis, "bestandsnachweis")
    minimum = int(_runden(_multiplizieren(_bruch(anzahl), quote), 0, "auf"))
    erreicht = verlangend >= minimum
    wert = dict(massgebliche_quote=_bruchteile(quote), mindestens_verlangende=minimum,
        minderheitenschwelle_erreicht=erreicht,
        verlangen_nach_diesen_voraussetzungen_ausreichend=erreicht and verlangen_schriftlich_begruendet)
    eingaben = dict(mitgliederzahl=mitgliederzahl, verlangende_mitglieder=verlangende_mitglieder,
        satzungsquote=satzungsquote, verlangen_schriftlich_begruendet=verlangen_schriftlich_begruendet,
        bestandsnachweis=bestandsnachweis)
    ergebnis = _ergebnis(wert, "mitgliederquote_und_wahrheitswerte", "BGB_VEREINS_MINDERHEITENVERLANGEN",
        eingaben, [dict(operation="Vorgegebene wirksame Satzungsquote oder ein Zehntel auf Mitgliederzahl anwenden und auf ganze Mitglieder aufrunden")], eingaben.copy())
    ergebnis["annahmen"] = ["Vollständiger maßgeblicher Mitgliederbestand und Wirksamkeit einer gegebenenfalls abweichenden Satzungsquote rechtlich bestimmt."]
    ergebnis["hinweise"] = ["Schriftliches Verlangen muss Zweck und Gründe angeben. Gerichtliche Ermächtigung bei Nichtbefolgung nach§37 Absatz2 ist ein gesonderter Schritt; rechnerischer Schwellenwert ersetzt keine Ermächtigung."]
    return ergebnis


def vereins_mitgliederschwellen(mitgliederzahl=None, satzungsunterzeichner=None):
    """Zahlengrenzen der §§56,59 Absatz3 und73, ohne umfassende Registerentscheidung."""
    mitglieder = _ganzzahl(mitgliederzahl, "mitgliederzahl", 0, GRENZE)
    unterschriften = _ganzzahl(satzungsunterzeichner, "satzungsunterzeichner", 0, GRENZE)
    eingaben = dict(mitgliederzahl=mitgliederzahl, satzungsunterzeichner=satzungsunterzeichner)
    wert = dict(eintragungs_mitgliederzahl_erreicht=mitglieder >= 7,
        satzungsunterschriftenzahl_erreicht=unterschriften >= 7, mitgliederzahl_unter_drei=mitglieder < 3)
    ergebnis = _ergebnis(wert, "wahrheitswerte", "BGB_VEREINS_MITGLIEDERSCHWELLEN",
        eingaben, [dict(operation="Mitgliederzahl mit sieben und drei sowie maßgebliche Satzungsunterschriften mit sieben vergleichen")], eingaben.copy())
    ergebnis["annahmen"] = ["Mitgliederzahl und rechtlich zählende Mitgliedsunterschriften jeweils für ihren maßgeblichen Zeitpunkt vorgegeben."]
    ergebnis["hinweise"] = ["Nur Zahlengrenzen; kein automatischer Eintragungsanspruch und kein automatischer Verlust der Rechtsfähigkeit. Satzungserrichtungsdatum, weitere Registervoraussetzungen, Dreimonatsfrist und gerichtliches Verfahren§73 gesondert."]
    return ergebnis
