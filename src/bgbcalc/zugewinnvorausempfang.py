"""Einseitige Vorausempfänge im nicht verlust- oder haftungsbegrenzten Standardfall (§1380)."""

from .betraege import _geld, _wahrheitswert
from .kalender import _ergebnis, _text
from .zahlen import _addieren, _bruch, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile


def zugewinnausgleich_vorausempfang_standardfall(
    zugewinn_zuwendender=None,
    zugewinn_empfaenger=None,
    vorausempfang=None,
    haftungsgrenze_zuwendender=None,
    haftungsgrenze_empfaenger=None,
    standardfall_bestaetigt=None,
    bewertungsnachweis=None,
):
    """Hinzu-/Herausrechnung, gedeckelte Anrechnung und gegebenenfalls Gegenrichtung ohne§1380."""
    geber = _geld(zugewinn_zuwendender)
    empfaenger = _geld(zugewinn_empfaenger)
    zuwendung = _geld(vorausempfang)
    grenze_geber = _geld(haftungsgrenze_zuwendender)
    grenze_empfaenger = _geld(haftungsgrenze_empfaenger)
    _wahrheitswert(standardfall_bestaetigt, "standardfall_bestaetigt")
    _text(bewertungsnachweis, "bewertungsnachweis")
    eingaben = dict(
        zugewinn_zuwendender=zugewinn_zuwendender,
        zugewinn_empfaenger=zugewinn_empfaenger,
        vorausempfang=vorausempfang,
        haftungsgrenze_zuwendender=haftungsgrenze_zuwendender,
        haftungsgrenze_empfaenger=haftungsgrenze_empfaenger,
        standardfall_bestaetigt=standardfall_bestaetigt,
        bewertungsnachweis=bewertungsnachweis,
    )
    wert = None
    if standardfall_bestaetigt:
        geber_bereinigt = _addieren(geber, zuwendung)
        empfaenger_bereinigt = max(_subtrahieren(empfaenger, zuwendung), _bruch(0))
        forderung = _multiplizieren(
            max(_subtrahieren(geber_bereinigt, empfaenger_bereinigt), _bruch(0)),
            _bruch(1, 2),
        )
        gegenforderung = _multiplizieren(
            max(_subtrahieren(empfaenger, geber), _bruch(0)), _bruch(1, 2)
        )
        if grenze_geber >= forderung and grenze_empfaenger >= gegenforderung:
            angerechnet = min(forderung, zuwendung)
            rest = _subtrahieren(forderung, angerechnet)
            richtung = (
                "zuwendender_an_empfaenger"
                if rest > 0
                else "empfaenger_an_zuwendenden"
                if gegenforderung > 0
                else "kein_zahlbetrag"
            )
            wert = dict(
                zugewinn_zuwendender_bereinigt=_bruchteile(geber_bereinigt),
                zugewinn_empfaenger_bereinigt=_bruchteile(empfaenger_bereinigt),
                ausgleichsforderung_vor_anrechnung=_bruchteile(forderung),
                angerechneter_vorausempfang=_bruchteile(angerechnet),
                restforderung_empfaenger=_bruchteile(rest),
                gegenforderung_ohne_1380=_bruchteile(gegenforderung),
                richtung=richtung,
                zahlbetrag=_bruchteile(max(rest, gegenforderung)),
            )
    ergebnis = _ergebnis(
        wert,
        "EUR",
        "BGB_ZUGEWINNAUSGLEICH_VORAUSEMPFANG_STANDARDFALL",
        eingaben,
        [
            dict(
                operation="Einseitigen Vorausempfang dem Geberzugewinn hinzufügen und aus Empfängerzugewinn entfernen; positiven halben Überschuss höchstens bis null anrechnen; Gegenforderung separat ohne§1380 berechnen"
            )
        ],
        eingaben.copy(),
    )
    ergebnis["status"] = "BERECHNET" if wert is not None else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = [
        "Nur einseitige Vorausempfänge, einschließlich verbrauchtem Empfang und Empfängerzugewinn unter Empfang, keine negativen tatsächlichen Vermögensdifferenzen; Haftungsgrenzen greifen auch vor Anrechnung nicht ein."
    ]
    ergebnis["hinweise"] = [
        "Gültige Anrechnungsbestimmung und Bewertung zum Zuwendungszeitpunkt einschließlich rechtlich gebotener Wertanpassung vorgegeben. Standardfall verlangt nichtnegative ungekappt ermittelte Vermögensdifferenzen beider Ehegatten, keine gegenläufigen Vorausempfänge und keine unterschiedlichen Zuwendungs-/Herausrechnungswerte. Empfängerzugewinn wird nach Herausrechnung höchstens bis null gemindert; Verbrauch oder Empfängerzugewinn unter Empfang schließen die Rechnung nicht aus. Keine zusätzliche Behandlung als privilegiertes Anfangsvermögen oder illoyale Hinzurechnung. Bei eingreifender Haftungsgrenze NICHT_ANWENDBAR, keine erfundene Verlust-/Deckelreihenfolge. Empfängerforderung nach§1380 nicht negativ machen; Gegenforderung aus ursprünglichen Zugewinnen nach§1378 getrennt, nicht aus negativem Anrechnungsrest. Haftungsgrenzen beider Seiten nach§1378 Absatz2 qualifiziert vorgeben. Ergebnis schließt Rechenweg dieses Standardfalls, nicht Härteeinrede, Verjährung, Vereinbarung oder andere Modifikationen. Keine Schenkungsteuerberechnung."
    ]
    return ergebnis
