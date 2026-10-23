"""Reguläre Achtprozentrechnung mit expliziten Abzügen; Kappungsintegration offen."""

from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .zahlen import _addieren, _bruch, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile


def modernisierung_regulaerer_zwischenbetrag(
    kosten_wohnung=None, erforderliche_erhaltungskosten=None, abzuziehende_kostenbeitraege=None,
    jaehrliche_zinsermaessigung=None, jaehrliche_laufende_zuschuesse_und_darlehen=None,
    grundtatbestand_erfuellt=None,
):
    """§§ 559/559a: Kosten bereinigen, acht Prozent jährlich, Abzüge; kein endgültiger Erhöhungsbetrag."""
    eingaben = dict(
        kosten_wohnung=kosten_wohnung, erforderliche_erhaltungskosten=erforderliche_erhaltungskosten,
        abzuziehende_kostenbeitraege=abzuziehende_kostenbeitraege,
        jaehrliche_zinsermaessigung=jaehrliche_zinsermaessigung,
        jaehrliche_laufende_zuschuesse_und_darlehen=jaehrliche_laufende_zuschuesse_und_darlehen,
        grundtatbestand_erfuellt=grundtatbestand_erfuellt,
    )
    kosten, erhaltung = _geld(kosten_wohnung), _geld(erforderliche_erhaltungskosten)
    beitraege, zinsvorteil = _geld(abzuziehende_kostenbeitraege), _geld(jaehrliche_zinsermaessigung)
    laufend = _geld(jaehrliche_laufende_zuschuesse_und_darlehen)
    _wahrheitswert(grundtatbestand_erfuellt, "grundtatbestand_erfuellt")
    ergebnis = _geld_ergebnis(
        _bruch(0) if grundtatbestand_erfuellt else None, "BGB_MODERNISIERUNG_REGULAERER_ZWISCHENBETRAG",
        eingaben, [{"operation": "Ausgewählter Grundtatbestand", "anwendbar": grundtatbestand_erfuellt}],
    )
    if grundtatbestand_erfuellt:
        basis = max(_subtrahieren(_subtrahieren(kosten, erhaltung), beitraege), _bruch(0))
        jahr_vorher = _multiplizieren(basis, _bruch(2, 25))
        jahresabzuege = _addieren(zinsvorteil, laufend)
        jahr = max(_subtrahieren(jahr_vorher, jahresabzuege), _bruch(0))
        monat = _multiplizieren(jahr, _bruch(1, 12))
        ergebnis["wert"] = dict(
            kostenbasis=_bruchteile(basis),
            jahresbetrag_vor_laufenden_abzuegen=_bruchteile(jahr_vorher),
            jaehrlicher_zwischenbetrag=_bruchteile(jahr),
            monatlicher_zwischenbetrag=_bruchteile(monat),
        )
        ergebnis["rechenschritte"].extend([
            {"operation": "Erhaltungsanteil und Kostenbeiträge abziehen, Kostenbasis mindestens null"},
            {"operation": "Acht Prozent jährlich; Zinsvorteil und laufende Jahresförderung abziehen",
             "jahresabzuege": _bruchteile(jahresabzuege)},
            {"operation": "Nichtnegativen Jahresbetrag durch zwölf teilen; Kappung nicht angewendet"},
        ])
    ergebnis["hinweise"].append("Rechnerischer Zwischenbetrag ohne Kappung; Reihenfolge gegenüber § 559 Abs. 3a fachlich noch offen. Kein endgültiger Mieterhöhungsanspruch.")
    return ergebnis
