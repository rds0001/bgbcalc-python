"""Zeitliche Teilprüfung der Vergleichsmietenerhöhung nach §§ 558 und 558b."""

from .betraege import _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler, _frist, _monatsende, _tage_addieren


def vergleichsmiete_zeitvoraussetzungen(
    letzte_massgebliche_miete_ab=None,
    zugang_erhoehungsverlangen=None,
    verlangen_formell_ordnungsgemaess=None,
):
    """Jahres- und Wartefrist sowie rechnerische Monatsfristen getrennt prüfen."""
    bisher = _datum(letzte_massgebliche_miete_ab, "letzte_massgebliche_miete_ab")
    zugang = _datum(zugang_erhoehungsverlangen, "zugang_erhoehungsverlangen")
    _wahrheitswert(verlangen_formell_ordnungsgemaess, "verlangen_formell_ordnungsgemaess")
    if bisher > zugang:
        _fehler("letzte_massgebliche_miete_ab", "Beginn der bisherigen Miete darf nicht nach Zugang liegen.")
    eingaben = dict(
        letzte_massgebliche_miete_ab=letzte_massgebliche_miete_ab,
        zugang_erhoehungsverlangen=zugang_erhoehungsverlangen,
        verlangen_formell_ordnungsgemaess=verlangen_formell_ordnungsgemaess,
    )
    wert = None
    if verlangen_formell_ordnungsgemaess:
        nach_jahr = _tage_addieren(_frist(letzte_massgebliche_miete_ab, 1, "jahre", "tagesbeginn"), 1)
        nach_wartefrist = _tage_addieren(_frist(letzte_massgebliche_miete_ab, 15, "monate", "tagesbeginn"), 1)
        erster = zugang.replace(day=1)
        mietbeginn = _monatsende(erster, 3, False)
        wert = dict(
            fruehester_zugang_nach_jahresfrist=nach_jahr.isoformat(),
            fruehester_mietbeginn_nach_wartefrist=nach_wartefrist.isoformat(),
            mietbeginn_bei_zustimmung=mietbeginn.isoformat(),
            rechnerisches_ende_zustimmungsfrist=_tage_addieren(mietbeginn, -1).isoformat(),
            rechnerisches_ende_klagefrist=_tage_addieren(_monatsende(erster, 6, False), -1).isoformat(),
            jahresfrist_eingehalten=zugang >= nach_jahr,
            wartefrist_eingehalten=mietbeginn >= nach_wartefrist,
        )
    ergebnis = _ergebnis(
        wert, "daten_und_wahrheitswerte", "BGB_VERGLEICHSMIETE_ZEITVORAUSSETZUNGEN", eingaben,
        [dict(operation="Unveränderte Mietdauer und zugangsbezogene Monatsfristen getrennt prüfen",
              ergebnis=wert)], eingaben.copy(),
    )
    ergebnis["status"] = "BERECHNET" if verlangen_formell_ordnungsgemaess else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = [
        "Feste lokale BGB-Fassung; Anwendungsbereich des Vergleichsmietenverfahrens und maßgeblicher bisheriger Mietbeginn vorgegeben."
    ]
    ergebnis["hinweise"] = [
        "Jahresfrist und Wartefrist sind getrennte Prüfergebnisse; BERECHNET bestätigt keinen Mieterhöhungsanspruch.",
        "Erhöhungen nach §§ 559 bis 560 setzen den maßgeblichen bisherigen Mietbeginn für diese Fristen nicht automatisch neu.",
        "Mietbeginn setzt Zustimmung und weitere materielle Voraussetzungen voraus; keine automatische Verschiebung eines verfrühten Verlangens.",
        "Fristenden sind kalendarische Ausgangswerte; eine anwendbare Sonnabend-, Sonn- oder Feiertagsverschiebung ist gesondert zu prüfen.",
        "Klagefrist folgt dem regulären Ablauf ohne Zustimmung; Nachholung oder Heilung nach § 558b Absatz 3 erfordert den maßgeblichen neuen Zugang.",
    ]
    return ergebnis
