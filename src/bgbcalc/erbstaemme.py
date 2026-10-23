"""Erbfolge nach Stämmen mit Erhaltung besonderer Erbteile nach § 1927."""
from .betraege import _wahrheitswert
from .kalender import _ergebnis, _fehler, _ganzzahl, _text, _vorhanden
from .zahlen import GRENZE, _addieren, _bruch, _multiplizieren
from .zinsen import _bruchteile


def _staemme_pruefen(kinderstaemme):
    _vorhanden(kinderstaemme, "kinderstaemme")
    gruppen, anzahl = _stammgruppen_pruefen([kinderstaemme])
    return gruppen[0], anzahl


def _stammgruppen_pruefen(gruppen):
    stellungen = {}
    anzahl = 0

    def pruefen(geschwister, vorfahren, tiefe):
        nonlocal anzahl
        if not isinstance(geschwister, list) or tiefe > 64:
            _fehler("kinderstaemme", "Listenstruktur mit höchstens 64 Ebenen erforderlich.")
        ergebnis = []
        personen = set()
        for knoten in geschwister:
            anzahl += 1
            if anzahl > 10000:
                _fehler("kinderstaemme", "Höchstens 10000 Knoten erlaubt.")
            if not isinstance(knoten, dict) or set(knoten) != {"person_id", "tritt_ein", "abkoemmlinge"}:
                _fehler("kinderstaemme", "Knoten benötigt genau person_id, tritt_ein und abkoemmlinge.")
            person = _text(knoten["person_id"], "person_id")
            tritt_ein = _wahrheitswert(knoten["tritt_ein"], "tritt_ein")
            if person in personen or person in vorfahren:
                _fehler("person_id", "Doppelte Geschwister oder Selbstabstammung unzulässig.")
            personen.add(person)
            if person in stellungen and stellungen[person] != tritt_ein:
                _fehler("tritt_ein", "Erbenstellung derselben Person muss in allen Stämmen übereinstimmen.")
            stellungen[person] = tritt_ein
            nachkommen = pruefen(knoten["abkoemmlinge"], vorfahren + [person], tiefe + 1) if knoten["abkoemmlinge"] else []
            if not isinstance(knoten["abkoemmlinge"], list):
                _fehler("abkoemmlinge", "Liste erforderlich.")
            if tritt_ein or nachkommen:
                ergebnis.append(dict(person_id=person, tritt_ein=tritt_ein, abkoemmlinge=nachkommen))
        return ergebnis

    geprueft = [pruefen(gruppe, [], 1) for gruppe in gruppen]
    return geprueft, anzahl


def abkoemmlings_erbquoten(
    kinderstaemme=None, verwandtenanteil_zaehler=None, verwandtenanteil_nenner=None,
):
    """§§ 1924/1927: vorgegebenen Verwandtenanteil nach besetzten Stämmen teilen."""
    _ganzzahl(verwandtenanteil_zaehler, "verwandtenanteil_zaehler", 0, GRENZE)
    _ganzzahl(verwandtenanteil_nenner, "verwandtenanteil_nenner", 1, GRENZE)
    if verwandtenanteil_zaehler > verwandtenanteil_nenner:
        _fehler("verwandtenanteil", "Verwandtenanteil darf 1 nicht überschreiten.")
    staemme, knotenzahl = _staemme_pruefen(kinderstaemme)
    teile, summen = [], {}

    def verteilen(geschwister, anteil, pfad):
        stammanteil = _multiplizieren(anteil, _bruch(1, len(geschwister)))
        for knoten in geschwister:
            person = knoten["person_id"]
            stammpfad = pfad + [person]
            if knoten["tritt_ein"]:
                teile.append(dict(person_id=person, stammpfad=stammpfad, quote=_bruchteile(stammanteil)))
                summen[person] = _addieren(summen.get(person, _bruch(0)), stammanteil)
            else:
                verteilen(knoten["abkoemmlinge"], stammanteil, stammpfad)

    if staemme:
        verteilen(staemme, _bruch(verwandtenanteil_zaehler, verwandtenanteil_nenner), [])
    wert = dict(erbteile=teile, erbquoten=[dict(person_id=person, quote=_bruchteile(anteil))
                                       for person, anteil in summen.items()]) if staemme else None
    eingaben = dict(kinderstaemme=kinderstaemme, verwandtenanteil_zaehler=verwandtenanteil_zaehler,
                    verwandtenanteil_nenner=verwandtenanteil_nenner)
    ergebnis = _ergebnis(wert, "erbquote", "BGB_ABKOEMMLINGS_ERBQUOTEN", eingaben, [
        {"operation": "Stammdaten und konsistente Erbenstellungen prüfen", "knoten": knotenzahl},
        {"operation": "Leere Stämme entfernen; besetzte Stämme rekursiv gleich teilen",
         "besetzte_kinderstaemme": len(staemme)},
        {"operation": "Besondere Erbteile erhalten und je Person summieren"},
    ], eingaben.copy())
    ergebnis["status"] = "BERECHNET" if staemme else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = ["Abstammung, Erbenstellungen und Verwandtenanteil sind ausdrücklich rechtlich vorgegeben."]
    ergebnis["hinweise"] = ["Keine automatische Ehegattenquote, Ausgleichung oder Prüfung anderer Erbordnungen.",
                            "Mehrfachzugehörigkeit bleibt als besondere Erbteile sichtbar; keine Rundung."]
    return ergebnis
