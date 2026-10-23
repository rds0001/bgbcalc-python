"""Gewichtete regelmäßige Arbeitnehmerzahl für §622 Absatz5 Satz1 Nummer2."""
from .betraege import _geld, _wahrheitswert
from .kalender import _ergebnis, _fehler, _text, _vorhanden
from .zahlen import _addieren, _bruch
from .zinsen import _bruchteile


def arbeitnehmerzahl_kuendigungsfrist(beschaeftigte=None, bestandsnachweis=None):
    """Auszubildende ausnehmen, Teilzeit bis20/30 Stunden mit1/2 bzw.3/4 gewichten."""
    _vorhanden(beschaeftigte, "beschaeftigte")
    if not isinstance(beschaeftigte, list) or len(beschaeftigte) > 10000:
        _fehler("beschaeftigte", "Unbenannte Liste mit höchstens10000 Personen erforderlich.")
    _text(bestandsnachweis, "bestandsnachweis")
    gewichte = []
    summe = _bruch(0)
    for person in beschaeftigte:
        if not isinstance(person, dict) or set(person) != {"wochenstunden", "teilzeitbeschaeftigt", "zur_berufsbildung_beschaeftigt"}:
            _fehler("beschaeftigte", "Jede Person benötigt genau wochenstunden, teilzeitbeschaeftigt und zur_berufsbildung_beschaeftigt.")
        stunden = _geld(person["wochenstunden"])
        teilzeit = _wahrheitswert(person["teilzeitbeschaeftigt"], "teilzeitbeschaeftigt")
        ausbildung = _wahrheitswert(person["zur_berufsbildung_beschaeftigt"], "zur_berufsbildung_beschaeftigt")
        if ausbildung:
            gewicht = _bruch(0)
        elif teilzeit and stunden <= 20:
            gewicht = _bruch(1, 2)
        elif teilzeit and stunden <= 30:
            gewicht = _bruch(3, 4)
        else:
            gewicht = _bruch(1)
        gewichte.append(_bruchteile(gewicht))
        summe = _addieren(summe, gewicht)
    wert = dict(gewichtete_arbeitnehmerzahl=_bruchteile(summe), hoechstens_zwanzig=summe <= 20,
        personengewichte=gewichte)
    eingaben = dict(beschaeftigte=beschaeftigte, bestandsnachweis=bestandsnachweis)
    ergebnis = _ergebnis(wert, "gewichtete_personenzahl", "BGB_ARBEITNEHMERZAHL_KUENDIGUNGSFRIST",
        eingaben, [dict(operation="Regelmäßigen Beschäftigtenbestand ohne Berufsbildung und mit gesetzlicher Teilzeitgewichtung summieren")], eingaben.copy())
    ergebnis["annahmen"] = ["Regelmäßiger Arbeitnehmerbestand beim Arbeitgeber und Beschäftigtenstatus rechtlich vorab bestimmt; keine bloße ungeprüfte Tagesaufnahme."]
    ergebnis["hinweise"] = ["Nur Zählregel§622 Absatz5. Höchstens20 Personen erlaubt nicht automatisch jede kürzere Frist: wirksame einzelvertragliche Vereinbarung und mindestens vier Wochen bleiben gesondert zu prüfen.",
        "Teilzeitstatus wird ausdrücklich eingegeben; Vollzeitkräfte zählen auch bei branchenüblich kurzer Vollzeit jeweils1. Keine automatische Übernahme anderer arbeitsrechtlicher Schwellenwertregeln."]
    return ergebnis
