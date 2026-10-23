"""Anteiliger Änderungsbetrag einer Betriebskostenpauschale nach§560."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _fehler, _ganzzahl, _text
from .zahlen import GRENZE, _bruch, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile


def betriebskostenpauschale_aenderungsbetrag(
    bisherige_betriebskosten=None, neue_betriebskosten=None,
    umlageanteil_zaehler=None, umlageanteil_nenner=None,
    erhoehungsumlage_vertraglich_vereinbart=None, erhoehungserklaerung_ordnungsgemaess=None,
    pauschalenanpassung_anwendbar=None, kostennachweis=None,
):
    """Kostenunterschied anteilig umlegen; bei Erhöhung Vertrags- und Erklärungsvoraussetzungen prüfen."""
    alt = _geld(bisherige_betriebskosten)
    neu = _geld(neue_betriebskosten)
    zaehler = _ganzzahl(umlageanteil_zaehler, "umlageanteil_zaehler", 0, GRENZE)
    nenner = _ganzzahl(umlageanteil_nenner, "umlageanteil_nenner", 1, GRENZE)
    if zaehler > nenner:
        _fehler("umlageanteil_zaehler", "Umlageanteil darf eins nicht übersteigen.")
    eingaben = dict(bisherige_betriebskosten=bisherige_betriebskosten, neue_betriebskosten=neue_betriebskosten,
        umlageanteil_zaehler=umlageanteil_zaehler, umlageanteil_nenner=umlageanteil_nenner,
        erhoehungsumlage_vertraglich_vereinbart=erhoehungsumlage_vertraglich_vereinbart,
        erhoehungserklaerung_ordnungsgemaess=erhoehungserklaerung_ordnungsgemaess,
        pauschalenanpassung_anwendbar=pauschalenanpassung_anwendbar, kostennachweis=kostennachweis)
    for name in tuple(eingaben)[4:-1]:
        _wahrheitswert(eingaben[name], name)
    _text(kostennachweis, "kostennachweis")
    differenz = _subtrahieren(neu, alt)
    gilt = pauschalenanpassung_anwendbar and (differenz <= 0 or
        (erhoehungsumlage_vertraglich_vereinbart and erhoehungserklaerung_ordnungsgemaess))
    ergebnis = _geld_ergebnis(_multiplizieren(differenz, _bruch(zaehler, nenner)) if gilt else None,
        "BGB_BETRIEBSKOSTENPAUSCHALE_AENDERUNGSBETRAG", eingaben,
        [dict(operation="Wirtschaftlich und rechtlich bereinigte Betriebskostendifferenz mit maßgeblichem Umlageanteil multiplizieren",
            betriebskostendifferenz=_bruchteile(differenz))])
    ergebnis["hinweise"].append("Vorzeichenbehafteter Änderungsbetrag für denselben Bezugszeitraum wie die Kosten: positiv Erhöhung, negativ Ermäßigung. Keine automatische Umrechnung von Jahres- auf Monatsbeträge. Nur Betriebskostenpauschale, keine Vorauszahlungsanpassung§560 Absatz4 oder Abrechnung. Wirtschaftlichkeit, Kostenabgrenzung, Umlageschlüssel und geltende Vereinbarungen vorab prüfen. Erhöhungsbeginn/Rückwirkung§560 Absatz2 separat; Ermäßigung ab Kostenminderung§560 Absatz3 und unverzügliche Mitteilung bleiben erforderlich.")
    return ergebnis
