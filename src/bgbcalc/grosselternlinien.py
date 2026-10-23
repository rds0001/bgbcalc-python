"""Paarweise und stammweise Erbteilung der dritten Ordnung."""
from .betraege import _wahrheitswert
from .erbstaemme import _stammgruppen_pruefen
from .kalender import _ergebnis, _fehler, _ganzzahl, _vorhanden
from .zahlen import GRENZE, _addieren, _bruch, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile


def grosselternlinien_erbquoten(
    grosselternpaare=None, vorrangige_ordnung_vorhanden=None,
    verwandtenanteil_zaehler=None, verwandtenanteil_nenner=None,
):
    """§ 1926: zuerst Großelternpaare, dann Stämme innerhalb jedes Paars teilen."""
    _vorhanden(grosselternpaare, "grosselternpaare")
    linien = ("vaeterlich", "muetterlich")
    if not isinstance(grosselternpaare, dict) or set(grosselternpaare) != set(linien):
        _fehler("grosselternpaare", "Genau vaeterliches und muetterliches Großelternpaar erforderlich.")
    if any(not isinstance(grosselternpaare[linie], list) or len(grosselternpaare[linie]) != 2 for linie in linien):
        _fehler("grosselternpaare", "Je Großelternpaar genau zwei Knoten erforderlich.")
    _wahrheitswert(vorrangige_ordnung_vorhanden, "vorrangige_ordnung_vorhanden")
    _ganzzahl(verwandtenanteil_zaehler, "verwandtenanteil_zaehler", 0, GRENZE)
    _ganzzahl(verwandtenanteil_nenner, "verwandtenanteil_nenner", 1, GRENZE)
    if verwandtenanteil_zaehler > verwandtenanteil_nenner:
        _fehler("verwandtenanteil", "Verwandtenanteil darf 1 nicht überschreiten.")
    gruppen, knotenzahl = _stammgruppen_pruefen([grosselternpaare[linie] for linie in linien])
    besetzt = sum(bool(gruppe) for gruppe in gruppen)
    anwendbar = bool(besetzt) and not vorrangige_ordnung_vorhanden
    verwandtenanteil = _bruch(verwandtenanteil_zaehler, verwandtenanteil_nenner)
    teile, summen = [], {}
    grosselternquote = _bruch(0)

    def verteilen(geschwister, anteil, pfad, linie):
        nonlocal grosselternquote
        stammanteil = _multiplizieren(anteil, _bruch(1, len(geschwister)))
        for knoten in geschwister:
            person = knoten["person_id"]
            stammpfad = pfad + [person]
            if knoten["tritt_ein"]:
                teile.append(dict(person_id=person, grosselternlinie=linie,
                                  stammpfad=stammpfad, quote=_bruchteile(stammanteil)))
                summen[person] = _addieren(summen.get(person, _bruch(0)), stammanteil)
                if not pfad:
                    grosselternquote = _addieren(grosselternquote, stammanteil)
            else:
                verteilen(knoten["abkoemmlinge"], stammanteil, stammpfad, linie)

    wert = None
    if anwendbar:
        paaranteil = _multiplizieren(verwandtenanteil, _bruch(1, besetzt))
        for linie, gruppe in zip(linien, gruppen):
            if gruppe:
                verteilen(gruppe, paaranteil, [], linie)
        wert = dict(erbteile=teile,
                    erbquoten=[dict(person_id=person, quote=_bruchteile(anteil)) for person, anteil in summen.items()],
                    grosselternquote=_bruchteile(grosselternquote),
                    abkoemmlingsquote=_bruchteile(_subtrahieren(verwandtenanteil, grosselternquote)))
    eingaben = dict(grosselternpaare=grosselternpaare,
                    vorrangige_ordnung_vorhanden=vorrangige_ordnung_vorhanden,
                    verwandtenanteil_zaehler=verwandtenanteil_zaehler,
                    verwandtenanteil_nenner=verwandtenanteil_nenner)
    ergebnis = _ergebnis(wert, "erbquote", "BGB_GROSSELTERNLINIEN_ERBQUOTEN", eingaben, [
        {"operation": "Dritte Ordnung und gemeinsame Stammdaten prüfen", "anwendbar": anwendbar,
         "knoten": knotenzahl},
        {"operation": "Besetzte Großelternpaare, dann besetzte Stämme teilen", "besetzte_paare": besetzt},
        {"operation": "Besondere Erbteile und Anteile von Großeltern und Abkömmlingen getrennt nachweisen"},
    ], eingaben.copy())
    ergebnis["status"] = "BERECHNET" if anwendbar else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = ["Abstammung, Erbenstellungen und Verwandtenanteil sind ausdrücklich rechtlich vorgegeben."]
    ergebnis["hinweise"] = ["Ehegattenregel des § 1931 ist in dieser Stammverteilung nicht angewandt.",
                            "Keine automatische Feststellung von Adoption oder Erbausschlüssen; keine Rundung."]
    return ergebnis
