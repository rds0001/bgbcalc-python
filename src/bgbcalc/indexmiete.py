"""Indexverhältnis und zeitliche Teilprüfung nach § 557b."""

from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler, _frist, _monatsende, _tage_addieren, _text
from .zahlen import _bruch, _dividieren, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile


def indexmiete_betrag(
    ausgangsmiete=None,
    ausgangsindex=None,
    neuer_index=None,
    indexnachweis=None,
    wirksame_indexvereinbarung=None,
):
    """Indexierte Mietbasis mal Verhältnis der vergleichbaren Indexwerte."""
    miete = _geld(ausgangsmiete)
    alt = _geld(ausgangsindex)
    neu = _geld(neuer_index)
    if alt == 0 or neu == 0:
        _fehler("index", "Positive Indexstände erforderlich.")
    _text(indexnachweis, "indexnachweis")
    _wahrheitswert(wirksame_indexvereinbarung, "wirksame_indexvereinbarung")
    eingaben = dict(
        ausgangsmiete=ausgangsmiete, ausgangsindex=ausgangsindex,
        neuer_index=neuer_index, indexnachweis=indexnachweis,
        wirksame_indexvereinbarung=wirksame_indexvereinbarung,
    )
    wert = None
    if wirksame_indexvereinbarung:
        verhaeltnis = _dividieren(neu, alt)
        neue_miete = _multiplizieren(miete, verhaeltnis)
        wert = dict(
            indexverhaeltnis=_bruchteile(verhaeltnis),
            neue_miete=_bruchteile(neue_miete),
            mietaenderung=_bruchteile(_subtrahieren(neue_miete, miete)),
        )
    ergebnis = _geld_ergebnis(
        _bruch(0) if wirksame_indexvereinbarung else None, "BGB_INDEXMIETE_BETRAG",
        eingaben, [dict(operation="Mietbasis mit neuem Index geteilt durch Ausgangsindex fortschreiben",
                        ergebnis=wert)],
    )
    ergebnis["wert"] = wert
    ergebnis["hinweise"] = [
        "Nur die zur Indexvereinbarung und zum Ausgangsindex gehörende Mietbasis verwenden; keine Doppelzählung früherer Indexänderungen.",
        "Indexstände müssen derselben amtlichen Reihe und Basis entstammen; keine automatische Datenbeschaffung oder Umbasierung.",
        "Indexverhältnis dimensionslos; Mietbeträge in EUR, negative Mietänderung bedeutet Senkung.",
        "Keine automatische Cent-Rundung; Erklärung, Jahresfrist, Ausgangsmietgrenze und gesonderte Erhöhungen bleiben zu prüfen.",
    ]
    return ergebnis


def indexmiete_aenderungstermin_pruefen(
    zugang_erklaerung=None,
    bisherige_indexmiete_ab=None,
    erklaerung_formell_ordnungsgemaess=None,
):
    """Übernächsten Monat und Mindestjahr unabhängig berechnen und vergleichen."""
    zugang = _datum(zugang_erklaerung, "zugang_erklaerung")
    bisher = _datum(bisherige_indexmiete_ab, "bisherige_indexmiete_ab")
    _wahrheitswert(erklaerung_formell_ordnungsgemaess, "erklaerung_formell_ordnungsgemaess")
    if bisher > zugang:
        _fehler("bisherige_indexmiete_ab", "Beginn der bisher geltenden Indexmiete darf nicht nach Zugang liegen.")
    eingaben = dict(
        zugang_erklaerung=zugang_erklaerung, bisherige_indexmiete_ab=bisherige_indexmiete_ab,
        erklaerung_formell_ordnungsgemaess=erklaerung_formell_ordnungsgemaess,
    )
    wert = None
    if erklaerung_formell_ordnungsgemaess:
        nach_zugang = _monatsende(zugang.replace(day=1), 2, False)
        nach_jahr = _tage_addieren(_frist(bisherige_indexmiete_ab, 1, "jahre", "tagesbeginn"), 1)
        wert = dict(
            beginn_nach_zugang=nach_zugang.isoformat(),
            fruehester_beginn_nach_jahresfrist=nach_jahr.isoformat(),
            jahresfrist_eingehalten=nach_zugang >= nach_jahr,
        )
    ergebnis = _ergebnis(
        wert, "datum_und_wahrheitswert", "BGB_INDEXMIETE_AENDERUNGSTERMIN_PRUEFEN", eingaben,
        [dict(operation="Übernächsten Monatsbeginn mit Ablauf eines unveränderten Mietjahres vergleichen",
              ergebnis=wert)], eingaben.copy(),
    )
    ergebnis["status"] = "BERECHNET" if erklaerung_formell_ordnungsgemaess else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = [
        "Feste lokale BGB-Fassung; wirksame Indexvereinbarung und maßgeblicher Beginn der bisherigen Indexmiete vorgegeben."
    ]
    ergebnis["hinweise"] = [
        "Teilprüfung des Änderungstermins; jahresfrist_eingehalten muss gesondert ausgewertet werden.",
        "Ein zu früher Monatsbeginn wird nicht automatisch verschoben; die Wirkung einer verfrühten Erklärung wird nicht entschieden.",
        "Erhöhungen nach §§ 559 bis 560 sind bei der Jahresfrist gesondert behandelt und setzen den eingegebenen Indexmietbeginn nicht automatisch neu.",
        "Keine Zahlungsfälligkeitsberechnung und keine Feiertagsverschiebung des Mietbeginns.",
    ]
    return ergebnis
