"""Wertanteilige interne Last bei Gesamthypothek (§2167)."""

from .betraege import _geld, _wahrheitswert
from .kalender import _ergebnis, _fehler, _text, _vorhanden
from .zahlen import _addieren, _bruch, _dividieren, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile


def gesamthypothekenvermaechtnis_befriedigungsbetrag(
    schuldbetrag=None,
    grundstuecke=None,
    vermachtes_grundstueck_id=None,
    schuld_nach_2166_qualifiziert=None,
    zweifelsregel_anwendbar=None,
    hoechstbetragshypothek=None,
    alle_mithaftenden_grundstuecke_im_nachlass=None,
    drittberichtigung_nach_2166_absatz_2=None,
    bewertungsnachweis=None,
):
    """Bereinigte Grundstückswerte normieren, Schuld zuordnen und auf eigene Wertdeckung begrenzen."""
    schuld = _geld(schuldbetrag)
    ziel = _text(vermachtes_grundstueck_id, "vermachtes_grundstueck_id")
    _vorhanden(grundstuecke, "grundstuecke")
    if not isinstance(grundstuecke, list) or not 2 <= len(grundstuecke) <= 1000:
        _fehler(
            "grundstuecke",
            "Liste mit 2 bis 1000 verschiedenen mithaftenden Grundstücken erforderlich.",
        )
    namen, werte = [], []
    gesamt = _bruch(0)
    for g in grundstuecke:
        if not isinstance(g, dict) or set(g) != {
            "grundstueck_id",
            "grundstueckswert",
            "vorrangige_belastungen",
        }:
            _fehler(
                "grundstuecke",
                "Genau grundstueck_id, grundstueckswert und vorrangige_belastungen erforderlich.",
            )
        name = _text(g["grundstueck_id"], "grundstueck_id")
        if name in namen:
            _fehler("grundstueck_id", "Grundstück nicht doppelt aufführen.")
        wert = max(
            _subtrahieren(
                _geld(g["grundstueckswert"]), _geld(g["vorrangige_belastungen"])
            ),
            _bruch(0),
        )
        namen.append(name)
        werte.append(wert)
        gesamt = _addieren(gesamt, wert)
    if ziel not in namen:
        _fehler(
            "vermachtes_grundstueck_id",
            "Vermachtes Grundstück muss in vollständiger Grundstücksliste vorkommen.",
        )
    eingaben = dict(
        schuldbetrag=schuldbetrag,
        grundstuecke=grundstuecke,
        vermachtes_grundstueck_id=vermachtes_grundstueck_id,
        schuld_nach_2166_qualifiziert=schuld_nach_2166_qualifiziert,
        zweifelsregel_anwendbar=zweifelsregel_anwendbar,
        hoechstbetragshypothek=hoechstbetragshypothek,
        alle_mithaftenden_grundstuecke_im_nachlass=alle_mithaftenden_grundstuecke_im_nachlass,
        drittberichtigung_nach_2166_absatz_2=drittberichtigung_nach_2166_absatz_2,
        bewertungsnachweis=bewertungsnachweis,
    )
    for name in tuple(eingaben)[3:8]:
        _wahrheitswert(eingaben[name], name)
    _text(bewertungsnachweis, "bewertungsnachweis")
    gilt = (
        schuld_nach_2166_qualifiziert
        and zweifelsregel_anwendbar
        and not hoechstbetragshypothek
        and alle_mithaftenden_grundstuecke_im_nachlass
        and not drittberichtigung_nach_2166_absatz_2
    )
    wert = None
    if gilt:
        deckung = werte[namen.index(ziel)]
        quote = _dividieren(deckung, gesamt) if gesamt > 0 else None
        anteilig = _multiplizieren(schuld, quote) if quote is not None else _bruch(0)
        wert = dict(
            bereinigte_grundstueckswerte=[
                dict(grundstueck_id=n, bereinigter_wert=_bruchteile(q))
                for n, q in zip(namen, werte)
            ],
            bereinigter_gesamtwert=_bruchteile(gesamt),
            verteilungsquote=_bruchteile(quote) if quote is not None else None,
            anteilige_schuld=_bruchteile(anteilig) if quote is not None else None,
            befriedigungsbetrag=_bruchteile(min(anteilig, deckung)),
        )
    ergebnis = _ergebnis(
        wert,
        "EUR",
        "BGB_GESAMTHYPOTHEKENVERMAECHTNIS_BEFRIEDIGUNGSBETRAG",
        eingaben,
        [
            dict(
                operation="Je Grundstück rangvorrangige Lasten abziehen und negative Deckung auf null begrenzen; Zielwert durch Gesamtwert teilen, mit Schuld multiplizieren und auf Zieldeckung begrenzen"
            )
        ],
        eingaben.copy(),
    )
    ergebnis["status"] = "BERECHNET" if gilt else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = [
        "Vollständige Liste aller mit derselben Hypothek belasteten Nachlassgrundstücke; eigene beziehungsweise qualifizierte Berichtigungsschuld ohne Drittberichtigungsfall§2166 Absatz2; Werte bei Eigentumsübergang rechtlich vergleichbar bestimmt."
    ]
    ergebnis["hinweise"] = [
        "Nur interne Verpflichtung des Vermächtnisnehmers gegenüber dem Erben; keine Kürzung dinglicher Gläubigerrechte. Rangvorrangige Belastungen je Grundstück berücksichtigen, betrachtete Gesamthypothek nicht nochmals abziehen. Kein frei gewählter Erbfall-/Bewertungsstichtag:§2166 Absatz1 Satz2 verlangt Eigentumsübergang; bei verschiedenen Übergangszeitpunkten Vergleichsbasis fachlich klären. Schuldbetrag ungekürzt vorgeben; bei Drittberichtigung§2166 Absatz2 NICHT_ANWENDBAR, da keine ungeprüfte Reihenfolge mit Anteilsverteilung eingeführt wird. Höchstbetragshypotheken, Nichtnachlassgrundstücke und Gesamtgrund-/Rentenschuld außerhalb dieses Modells. Bei sämtlichen bereinigten Werten null beträgt eigene Deckung und Befriedigung null; verteilungsquote ist NULL, weil0/0 nicht definiert ist; Auch anteilige_schuld ist in diesem Sonderfall NULL, da ohne definierte Quote keine anteilige Schuld ausgewiesen wird. Abweichender Erblasserwille schließt Zweifelsregel aus; keine automatische Grundstücksbewertung oder Fälligkeitsberechnung."
    ]
    return ergebnis
