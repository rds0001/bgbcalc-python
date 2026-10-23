"""Gesetzliche Kostenverteilungen im Nachbarrecht."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _auswahl, _fehler, _ganzzahl, _text
from .zahlen import GRENZE, _bruch, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile


def nachbarrecht_kostengleichanteil(
    gesamtkosten=None, kostenart=None, beteiligtenzahl=None,
    abweichendes_rechtsverhaeltnis=None, gesetzlicher_kostenfall=None, kostennachweis=None,
):
    """§919 Absatz3: gleiche Abmarkungsanteile;§922: hälftige Unterhaltungskosten zweier Nachbarn."""
    kosten = _geld(gesamtkosten)
    _auswahl(kostenart, "kostenart", ("abmarkung", "grenzeinrichtung_unterhaltung"))
    anzahl = _ganzzahl(beteiligtenzahl, "beteiligtenzahl", 2, GRENZE)
    _wahrheitswert(abweichendes_rechtsverhaeltnis, "abweichendes_rechtsverhaeltnis")
    _wahrheitswert(gesetzlicher_kostenfall, "gesetzlicher_kostenfall")
    _text(kostennachweis, "kostennachweis")
    if kostenart == "grenzeinrichtung_unterhaltung" and anzahl != 2:
        _fehler("beteiligtenzahl", "Unterhaltung zweier Nachbargrundstücke: genau zwei Kostenseiten erforderlich.")
    eingaben = dict(gesamtkosten=gesamtkosten, kostenart=kostenart, beteiligtenzahl=beteiligtenzahl,
        abweichendes_rechtsverhaeltnis=abweichendes_rechtsverhaeltnis,
        gesetzlicher_kostenfall=gesetzlicher_kostenfall, kostennachweis=kostennachweis)
    gilt = gesetzlicher_kostenfall and not abweichendes_rechtsverhaeltnis
    return _geld_ergebnis(_multiplizieren(kosten, _bruch(1, anzahl)) if gilt else None,
        "BGB_NACHBARRECHT_KOSTENGLEICHANTEIL", eingaben,
        [dict(operation="Gesetzlichen Kostenfall ohne abweichende Kostenregelung zu gleichen Teilen auf beteiligte Kostenseiten verteilen")])


def grenzbaum_beseitigungskosten(
    beseitigungskosten=None, anderer_nachbar_verzichtet=None,
    unersetzliches_grenzzeichen=None, grenzbaumregel_anwendbar=None, kostennachweis=None,
):
    """§923 Absatz2: gleiche Kosten, bei Rechtsverzicht des anderen alleinige Kosten des Verlangenden."""
    kosten = _geld(beseitigungskosten)
    eingaben = dict(beseitigungskosten=beseitigungskosten, anderer_nachbar_verzichtet=anderer_nachbar_verzichtet,
        unersetzliches_grenzzeichen=unersetzliches_grenzzeichen, grenzbaumregel_anwendbar=grenzbaumregel_anwendbar,
        kostennachweis=kostennachweis)
    for name in tuple(eingaben)[1:-1]:
        _wahrheitswert(eingaben[name], name)
    _text(kostennachweis, "kostennachweis")
    gilt = grenzbaumregel_anwendbar and not unersetzliches_grenzzeichen
    ergebnis = _geld_ergebnis(None, "BGB_GRENZBAUM_BESEITIGUNGSKOSTEN", eingaben,
        [dict(operation="Gesetzlichen Beseitigungsfall prüfen; bei Verzicht des anderen alleinige, sonst hälftige Kosten des Verlangenden")])
    if gilt:
        verlangender = kosten if anderer_nachbar_verzichtet else _multiplizieren(kosten, _bruch(1, 2))
        ergebnis["wert"] = dict(kosten_verlangender_nachbar=_bruchteile(verlangender),
            kosten_anderer_nachbar=_bruchteile(_subtrahieren(kosten, verlangender)))
        ergebnis["status"] = "BERECHNET"
    ergebnis["hinweise"].append("Nur gesetzlicher Beseitigungsfall§923, auch Grenzstrauch. Dient der Baum als nicht zweckmäßig ersetzbares Grenzzeichen, ist dieser Anspruch ausgeschlossen; freiwillige anderweitige Regelungen separat. Rechtsverzicht am Baum rechtlich belegen. Eigentumsübergang bei Trennung und Früchteverteilung nicht durch Kostenergebnis entschieden.")
    return ergebnis
