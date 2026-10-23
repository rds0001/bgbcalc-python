"""Gleichteilung nach Personen und Verwandtschaftsgrad ab vierter Erbordnung."""
from .betraege import _wahrheitswert
from .kalender import _ergebnis, _fehler, _ganzzahl, _text, _vorhanden
from .zahlen import GRENZE, _bruch, _multiplizieren
from .zinsen import _bruchteile


def fernere_erbquoten(
    ordnungsnummer=None, voreltern=None, abkoemmlinge=None,
    vorrangige_ordnung_vorhanden=None, verwandtenanteil_zaehler=None, verwandtenanteil_nenner=None,
):
    """§§ 1928/1929: Voreltern, sonst nächste Abkömmlinge zu gleichen Teilen."""
    _ganzzahl(ordnungsnummer, "ordnungsnummer", 4, 10000)
    for parameter, personen in (("voreltern", voreltern), ("abkoemmlinge", abkoemmlinge)):
        _vorhanden(personen, parameter)
        if not isinstance(personen, list) or len(personen) > 10000:
            _fehler(parameter, "Liste mit höchstens 10000 Einträgen erforderlich.")
    _wahrheitswert(vorrangige_ordnung_vorhanden, "vorrangige_ordnung_vorhanden")
    _ganzzahl(verwandtenanteil_zaehler, "verwandtenanteil_zaehler", 0, GRENZE)
    _ganzzahl(verwandtenanteil_nenner, "verwandtenanteil_nenner", 1, GRENZE)
    if verwandtenanteil_zaehler > verwandtenanteil_nenner:
        _fehler("verwandtenanteil", "Verwandtenanteil darf 1 nicht überschreiten.")
    vorfahren = {}
    for person in voreltern:
        _text(person, "person_id")
        vorfahren[person] = True
    grade = {}
    for person in abkoemmlinge:
        if not isinstance(person, dict) or set(person) != {"person_id", "verwandtschaftsgrad"}:
            _fehler("abkoemmlinge", "Objekte mit genau person_id und verwandtschaftsgrad erforderlich.")
        kennung = _text(person["person_id"], "person_id")
        grad = _ganzzahl(person["verwandtschaftsgrad"], "verwandtschaftsgrad", 1, 10000)
        if kennung in vorfahren:
            _fehler("person_id", "Person kann hier nicht zugleich Vorelternteil und Abkömmling sein.")
        grade[kennung] = min(grad, grade.get(kennung, grad))
    auswahl = "voreltern" if vorfahren else "naechste_abkoemmlinge"
    grad = ordnungsnummer - 1 if vorfahren else (min(grade.values()) if grade else None)
    berufene = list(vorfahren) if vorfahren else [person for person, wert in grade.items() if wert == grad]
    anwendbar = bool(berufene) and not vorrangige_ordnung_vorhanden
    wert = None
    if anwendbar:
        quote = _multiplizieren(_bruch(verwandtenanteil_zaehler, verwandtenanteil_nenner),
                                _bruch(1, len(berufene)))
        wert = dict(auswahl=auswahl, massgeblicher_grad=grad,
                    erbquoten=[dict(person_id=person, quote=_bruchteile(quote)) for person in berufene])
    eingaben = dict(ordnungsnummer=ordnungsnummer, voreltern=voreltern, abkoemmlinge=abkoemmlinge,
                    vorrangige_ordnung_vorhanden=vorrangige_ordnung_vorhanden,
                    verwandtenanteil_zaehler=verwandtenanteil_zaehler,
                    verwandtenanteil_nenner=verwandtenanteil_nenner)
    ergebnis = _ergebnis(wert, "erbquote", "BGB_FERNERE_ERBQUOTEN", eingaben, [
        {"operation": "Vorrang früherer Ordnung prüfen", "anwendbar": anwendbar},
        {"operation": "Voreltern, sonst nächste Abkömmlinge auswählen; Personen einmal zählen",
         "auswahl": auswahl, "ausgewaehlte_personen": len(berufene)},
        {"operation": "Verwandtenanteil gleich unter ausgewählten Personen teilen"},
    ], eingaben.copy())
    ergebnis["status"] = "BERECHNET" if anwendbar else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = ["Ordnung, Berufung, Rollen und Verwandtschaftsgrade sind ausdrücklich rechtlich vorgegeben."]
    ergebnis["hinweise"] = ["Ab vierter Ordnung keine Stammteilung oder Mehrfachanteile nach § 1927.",
                            "Ehegattenvorrang nach § 1931 Abs. 2 gesondert beachten; keine Rundung."]
    return ergebnis
