"""Altersabhängige Voraussetzungen; weitere rechtliche Einordnung bleibt getrennt."""

from .betraege import _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler


def _vollendete_jahre(geburtsdatum, stichtag, stichtag_parameter="stichtag"):
    geburt = _datum(geburtsdatum, "geburtsdatum")
    tag = _datum(stichtag, stichtag_parameter)
    if tag < geburt:
        _fehler(stichtag_parameter, "Stichtag darf nicht vor der Geburt liegen.")
    # Im Nichtschaltjahr ist der 28. Februar noch vor dem Geburtstag 29. Februar;
    # ab 1. März ist das Lebensjahr vollendet. Kein zukünftiges Datum nötig.
    return tag.year - geburt.year - int((tag.month, tag.day) < (geburt.month, geburt.day))


def geschaeftsfaehigkeit_altersvoraussetzungen(geburtsdatum=None, stichtag=None):
    """Altersstufen der §§ 104 Nr. 1 und 106, kein vollständiger Geschäftsfähigkeitsstatus."""
    alter = _vollendete_jahre(geburtsdatum, stichtag)
    eingaben = dict(geburtsdatum=geburtsdatum, stichtag=stichtag)
    wert = dict(
        vollendete_lebensjahre=alter, unter_sieben=alter < 7,
        minderjaehrig_ab_sieben=7 <= alter < 18, volljaehrig=alter >= 18,
    )
    ergebnis = _ergebnis(
        wert, "lebensjahre_und_wahrheitswerte", "BGB_GESCHAEFTSFAEHIGKEIT_ALTERSVORAUSSETZUNGEN",
        eingaben, [dict(operation="Vollendetes Lebensalter mit sieben und achtzehn Jahren vergleichen",
                        ergebnis=wert)], eingaben.copy(),
    )
    ergebnis["annahmen"] = ["Feste lokale BGB-Fassung; Geburtsdatum und Stichtag ausdrücklich vorgegeben."]
    ergebnis["hinweise"] = [
        "Nur Altersvoraussetzungen; volljaehrig ist keine Bestätigung uneingeschränkter Geschäftsfähigkeit.",
        "§ 104 Nummer 2, Zustände nach § 105 Absatz 2 sowie die Regeln der §§ 107 bis 113 sind gesondert.",
        "Keine Entscheidung über die Wirksamkeit einer konkreten Willenserklärung.",
    ]
    return ergebnis


def delikt_altersvoraussetzungen(
    geburtsdatum=None,
    handlungstag=None,
    unfallprivileg_sachlich_anwendbar=None,
    verletzung_vorsaetzlich=None,
    erforderliche_einsicht_vorhanden=None,
):
    """Alters- und Ausnahmekette des § 828 anhand ausdrücklich bewerteter Tatsachen."""
    alter = _vollendete_jahre(geburtsdatum, handlungstag, "handlungstag")
    eingaben = dict(
        geburtsdatum=geburtsdatum, handlungstag=handlungstag,
        unfallprivileg_sachlich_anwendbar=unfallprivileg_sachlich_anwendbar,
        verletzung_vorsaetzlich=verletzung_vorsaetzlich,
        erforderliche_einsicht_vorhanden=erforderliche_einsicht_vorhanden,
    )
    for name in ("unfallprivileg_sachlich_anwendbar", "verletzung_vorsaetzlich",
                 "erforderliche_einsicht_vorhanden"):
        _wahrheitswert(eingaben[name], name)
    erster = alter < 7
    zweiter = 7 <= alter < 10 and unfallprivileg_sachlich_anwendbar and not verletzung_vorsaetzlich
    dritter = not (erster or zweiter) and alter < 18 and not erforderliche_einsicht_vorhanden
    wert = dict(
        vollendete_lebensjahre=alter,
        ausschluss_nach_absatz_1=erster, ausschluss_nach_absatz_2=zweiter,
        ausschluss_nach_absatz_3=dritter,
        verantwortlichkeit_nach_828_ausgeschlossen=erster or zweiter or dritter,
    )
    ergebnis = _ergebnis(
        wert, "lebensjahre_und_wahrheitswerte", "BGB_DELIKT_ALTERSVORAUSSETZUNGEN", eingaben,
        [dict(operation="Altersausschluss, Unfallprivileg und subsidiäre Einsichtsausnahme nach § 828",
              ergebnis=wert)], eingaben.copy(),
    )
    ergebnis["annahmen"] = [
        "Feste lokale BGB-Fassung; sachliche Anwendbarkeit des Unfallprivilegs, Vorsatz und erforderliche Einsicht ausdrücklich bewertet."
    ]
    ergebnis["hinweise"] = [
        "FALSE beim Gesamtausschluss begründet keine Haftung; andere Voraussetzungen und Ausschlüsse bleiben zu prüfen.",
        "Unfallprivileg ist eine rechtlich bewertete Nutzervorgabe, keine automatische Einordnung jedes Unfalls mit einem Fahrzeug.",
        "Vorsatz hebt nur den Ausschluss des Absatzes 2 auf; Absatz 3 ist anschließend gesondert zu prüfen.",
        "Keine automatische Feststellung von Einsicht, Vorsatz, Aufsichtspflichtverletzung oder Billigkeitshaftung nach § 829.",
    ]
    return ergebnis
