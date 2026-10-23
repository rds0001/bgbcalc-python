"""Relative Minderung mit ausdrücklich bewerteten Vergleichswerten."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _auswahl, _fehler
from .zahlen import _bruch, _dividieren, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile, _zeitanteil


def minderung_betrag(
    vereinbarter_preis=None, mangelfreier_wert=None, wirklicher_wert=None,
    geleistete_zahlung=None, regelbereich=None, wertzeitpunkt=None,
    mangelzeitanteil_zaehler=None, mangelzeitanteil_nenner=None,
    wert_und_zeitnachweis=None, minderungsrecht=None, minderungserklaerung=None,
    anzeigeausschluss=None,
):
    """§§ 441/638/327n/651m: Preis im bewerteten Wertverhältnis herabsetzen."""
    eingaben = dict(
        vereinbarter_preis=vereinbarter_preis, mangelfreier_wert=mangelfreier_wert,
        wirklicher_wert=wirklicher_wert, geleistete_zahlung=geleistete_zahlung,
        regelbereich=regelbereich, wertzeitpunkt=wertzeitpunkt,
        mangelzeitanteil_zaehler=mangelzeitanteil_zaehler,
        mangelzeitanteil_nenner=mangelzeitanteil_nenner,
        wert_und_zeitnachweis=wert_und_zeitnachweis, minderungsrecht=minderungsrecht,
        minderungserklaerung=minderungserklaerung, anzeigeausschluss=anzeigeausschluss,
    )
    preis, mangelfrei = _geld(vereinbarter_preis), _geld(mangelfreier_wert)
    wirklich, bezahlt = _geld(wirklicher_wert), _geld(geleistete_zahlung)
    if mangelfrei == 0:
        _fehler("mangelfreier_wert", "Positiver Vergleichswert erforderlich.")
    if wirklich > mangelfrei:
        _fehler("wirklicher_wert", "Minderung setzt wirklichen Wert höchstens gleich Vergleichswert voraus.")
    _auswahl(regelbereich, "regelbereich", ("kauf", "werk", "digital_einmal", "digital_dauer", "reise"))
    _auswahl(wertzeitpunkt, "wertzeitpunkt", ("vertragsschluss", "bereitstellung"))
    erwartet = "bereitstellung" if regelbereich.startswith("digital") else "vertragsschluss"
    if wertzeitpunkt != erwartet:
        _fehler("wertzeitpunkt", "Bewertungszeitpunkt passt nicht zum gewählten Regelbereich.")
    anteil = _zeitanteil(mangelzeitanteil_zaehler, mangelzeitanteil_nenner, wert_und_zeitnachweis)
    if anteil > 1 or (regelbereich in ("kauf", "werk", "digital_einmal") and anteil != 1):
        _fehler("mangelzeitanteil", "Anteil 0 bis 1; bei Kauf/Werk/digitaler Einmalbereitstellung genau 1.")
    for parameter in ("minderungsrecht", "minderungserklaerung", "anzeigeausschluss"):
        _wahrheitswert(eingaben[parameter], parameter)
    if anzeigeausschluss and regelbereich != "reise":
        _fehler("anzeigeausschluss", "Dieser Anzeigeausschluss betrifft ausschließlich Reise.")
    anwendbar = minderungsrecht and (
        not anzeigeausschluss if regelbereich == "reise" else minderungserklaerung)
    ergebnis = _geld_ergebnis(
        _bruch(0) if anwendbar else None, "BGB_MINDERUNG_BETRAG", eingaben,
        [{"operation": "Minderungsrecht und bereichsspezifische Voraussetzungen", "anwendbar": anwendbar}],
        {"wert_und_zeitnachweis": wert_und_zeitnachweis})
    if anwendbar:
        wertquote = _dividieren(wirklich, mangelfrei)
        minderung = _multiplizieren(_multiplizieren(preis, _subtrahieren(_bruch(1), wertquote)), anteil)
        verbleibend = _subtrahieren(preis, minderung)
        erstattung = max(_subtrahieren(bezahlt, verbleibend), _bruch(0))
        ergebnis["wert"] = dict(geminderter_preis=_bruchteile(verbleibend),
                                minderungsbetrag=_bruchteile(minderung),
                                erstattungsbetrag=_bruchteile(erstattung))
        ergebnis["rechenschritte"].append(dict(
            operation="Relative Wertminderung auf betroffenen Zeitanteil anwenden; gezahlten Mehrbetrag erstatten",
            wertquote=_bruchteile(wertquote), mangelzeitanteil=_bruchteile(anteil)))
    return ergebnis
