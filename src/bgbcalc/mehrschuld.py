"""Gesetzliche Verteilung unter mehreren bereits fälligen Geldschulden."""

from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _fehler, _ganzzahl, _text, _vorhanden
from .zahlen import _addieren, _bruch, _dividieren, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile


def faellige_geldschulden_gesetzlich_tilgen(
    zahlung=None,
    schulden=None,
    tilgungsbestimmung_getroffen=None,
    gesetzliche_reihenfolge_anwendbar=None,
):
    """§ 366 Abs. 2: Sicherheit, Lästigkeit, Alter, zuletzt Verhältnis."""
    betrag = _geld(zahlung)
    _vorhanden(schulden, "schulden")
    if not isinstance(schulden, list) or not 2 <= len(schulden) <= 1000:
        _fehler("schulden", "Liste mit 2 bis 1000 fälligen Geldschulden erforderlich.")
    _wahrheitswert(tilgungsbestimmung_getroffen, "tilgungsbestimmung_getroffen")
    _wahrheitswert(gesetzliche_reihenfolge_anwendbar, "gesetzliche_reihenfolge_anwendbar")
    namen, forderungen, raenge = [], [], []
    gesamt = _bruch(0)
    for schuld in schulden:
        if not isinstance(schuld, dict) or set(schuld) != {
            "schuld_id", "offener_betrag", "sicherheitsrang", "laestigkeitsrang", "altersrang",
        }:
            _fehler("schulden", "Genau schuld_id, offener_betrag und die drei Rangfelder erforderlich.")
        kennung = _text(schuld["schuld_id"], "schuld_id")
        if kennung in namen:
            _fehler("schuld_id", "Schulden dürfen nicht doppelt vorkommen.")
        offen = _geld(schuld["offener_betrag"])
        if offen == 0:
            _fehler("offener_betrag", "Nur positive offene Schulden aufnehmen.")
        rang = tuple(
            _ganzzahl(schuld[name], name, 1, 9007199254740991)
            for name in ("sicherheitsrang", "laestigkeitsrang", "altersrang")
        )
        namen.append(kennung)
        forderungen.append(offen)
        raenge.append(rang)
        gesamt = _addieren(gesamt, offen)
    anwendbar = gesetzliche_reihenfolge_anwendbar and not tilgungsbestimmung_getroffen
    eingaben = dict(
        zahlung=zahlung, schulden=schulden,
        tilgungsbestimmung_getroffen=tilgungsbestimmung_getroffen,
        gesetzliche_reihenfolge_anwendbar=gesetzliche_reihenfolge_anwendbar,
    )
    schritte = [
        dict(operation="Gesetzliche Auffangreihenfolge ohne Tilgungsbestimmung", anwendbar=anwendbar),
        dict(operation="Offene fällige Geldschulden summieren", gesamtbetrag=_bruchteile(gesamt)),
    ]
    wert = None
    if anwendbar:
        rest = betrag
        zugeteilt = [_bruch(0) for _ in namen]
        for rang in sorted(set(raenge)):
            gruppe = [i for i, r in enumerate(raenge) if r == rang]
            gruppenbetrag = _bruch(0)
            for i in gruppe:
                gruppenbetrag = _addieren(gruppenbetrag, forderungen[i])
            gruppenzahlung = min(rest, gruppenbetrag)
            for i in gruppe:
                zugeteilt[i] = _multiplizieren(
                    gruppenzahlung, _dividieren(forderungen[i], gruppenbetrag)
                )
            rest = _subtrahieren(rest, gruppenzahlung)
            schritte.append(dict(
                operation="Ranggruppe bedienen, innerhalb der Gruppe verhältnismäßig",
                sicherheitsrang=rang[0], laestigkeitsrang=rang[1], altersrang=rang[2],
                schuld_ids=[namen[i] for i in gruppe],
                gruppenbetrag=_bruchteile(gruppenbetrag), gruppenzahlung=_bruchteile(gruppenzahlung),
            ))
        wert = dict(
            zuordnungen=[
                dict(schuld_id=kennung, tilgungsbetrag=_bruchteile(zugeteilt[i]),
                     restschuld=_bruchteile(_subtrahieren(forderungen[i], zugeteilt[i])))
                for i, kennung in enumerate(namen)
            ],
            nicht_zugeordnet=_bruchteile(rest),
        )
    ergebnis = _geld_ergebnis(
        _bruch(0) if anwendbar else None, "BGB_FAELLIGE_GELDSCHULDEN_GESETZLICH_TILGEN",
        eingaben, schritte,
    )
    ergebnis["wert"] = wert
    ergebnis["hinweise"] = [
        "Nur bereits fällige Geldschulden desselben Schuldners beim selben Gläubiger in EUR.",
        "Rang 1 bedeutet geringste Sicherheit, größte Lästigkeit beziehungsweise höchstes Alter; Ränge sind bewertete Nutzervorgaben.",
        "Tilgungsbestimmungen, nicht fällige Schulden und vorrangige Spezialregeln sind gesondert zu behandeln.",
        "Innerhalb jeder ausgewählten Schuld ist die Anrechnung auf Kosten, Zinsen und Hauptforderung gesondert zu prüfen.",
        "Keine Cent-Rundung; nicht zugeordnete Zahlung ist kein festgestellter Erstattungsanspruch.",
    ]
    return ergebnis
