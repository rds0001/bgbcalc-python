"""Gleiche interne Grundanteile und vollständig ausgefallene Beiträge nach § 426."""

from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _ganzzahl
from .zahlen import _addieren, _bruch, _dividieren, _multiplizieren
from .zinsen import _bruchteile


def gesamtschuld_gleichanteile_mit_ausfall(
    gesamtbetrag=None,
    anzahl_gesamtschuldner=None,
    anzahl_vollstaendig_ausfallender_beitraege=None,
    gleichanteiliger_ausgleich_anwendbar=None,
):
    """§ 426 Abs. 1 im Fall gleicher Anteile und ausschließlich vollständiger Ausfälle."""
    betrag = _geld(gesamtbetrag)
    anzahl = _ganzzahl(anzahl_gesamtschuldner, "anzahl_gesamtschuldner", 2, 9007199254740991)
    ausfaelle = _ganzzahl(
        anzahl_vollstaendig_ausfallender_beitraege,
        "anzahl_vollstaendig_ausfallender_beitraege", 0, anzahl - 1,
    )
    _wahrheitswert(gleichanteiliger_ausgleich_anwendbar, "gleichanteiliger_ausgleich_anwendbar")
    eingaben = dict(
        gesamtbetrag=gesamtbetrag, anzahl_gesamtschuldner=anzahl_gesamtschuldner,
        anzahl_vollstaendig_ausfallender_beitraege=anzahl_vollstaendig_ausfallender_beitraege,
        gleichanteiliger_ausgleich_anwendbar=gleichanteiliger_ausgleich_anwendbar,
    )
    wert = None
    if gleichanteiliger_ausgleich_anwendbar:
        quote = _bruch(1, anzahl)
        grundbeitrag = _multiplizieren(betrag, quote)
        ausfallbetrag = _multiplizieren(grundbeitrag, _bruch(ausfaelle))
        zusatz = _dividieren(ausfallbetrag, _bruch(anzahl - ausfaelle))
        wert = dict(
            urspruenglicher_innenanteil=_bruchteile(quote),
            urspruenglicher_beitrag=_bruchteile(grundbeitrag),
            gesamter_ausfallbetrag=_bruchteile(ausfallbetrag),
            zusaetzlicher_beitrag_je_uebrigem=_bruchteile(zusatz),
            gesamtbelastung_je_uebrigem=_bruchteile(_addieren(grundbeitrag, zusatz)),
            anzahl_uebrige=anzahl - ausfaelle,
        )
    ergebnis = _geld_ergebnis(
        _bruch(0) if gleichanteiliger_ausgleich_anwendbar else None,
        "BGB_GESAMTSCHULD_GLEICHANTEILE_MIT_AUSFALL", eingaben,
        [dict(operation="Gleichen Grundbeitrag berechnen und vollständige Ausfälle auf die Übrigen verteilen",
              ergebnis=wert)],
    )
    ergebnis["wert"] = wert
    ergebnis["hinweise"] = [
        "Nur gleiche interne Grundanteile und vollständig nicht erlangbare Beiträge; teilweise Ausfälle und abweichende Innenquoten sind gesondert.",
        "Die ursprüngliche Verpflichtung eines ausfallenden Schuldners wird durch diese Rechnung nicht aufgehoben.",
        "Zusätzliche Ausfalltragung der übrigen Schuldner, keine Begrenzung ihrer Außenhaftung gegenüber dem Gläubiger.",
        "Bereits geleistete Beiträge, Fälligkeit des Ausgleichs und Forderungsübergang nach § 426 Absatz 2 sind nicht abgerechnet.",
        "Alle Geldbeträge in EUR und exakt ohne automatische Cent-Rundung; Innenanteil dimensionslos.",
    ]
    return ergebnis
