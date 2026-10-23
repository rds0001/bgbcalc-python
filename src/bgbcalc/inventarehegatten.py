"""Inventarfrist und Inventarzurechnung bei Gesamtgut (§2008 BGB)."""

from .betraege import _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler, _text


def inventarfrist_ehegatten(
    fristende_erbe=None,
    fristende_anderer_ehegatte=None,
    erbschaft_gehoert_zum_gesamtgut=None,
    anderer_ehegatte_verwaltet_gesamtgut=None,
    frist_auch_gegenueber_anderem_bestimmt=None,
    inventar_durch_anderen_errichtet=None,
    einordnungsnachweis=None,
):
    """Wirksamkeitsbedingung und spätestes qualifiziertes Inventarfristende nach §2008."""
    erbe = _datum(fristende_erbe, "fristende_erbe")
    anderer = (
        _datum(fristende_anderer_ehegatte, "fristende_anderer_ehegatte")
        if fristende_anderer_ehegatte is not None
        else None
    )
    eingaben = dict(
        fristende_erbe=fristende_erbe,
        fristende_anderer_ehegatte=fristende_anderer_ehegatte,
        erbschaft_gehoert_zum_gesamtgut=erbschaft_gehoert_zum_gesamtgut,
        anderer_ehegatte_verwaltet_gesamtgut=anderer_ehegatte_verwaltet_gesamtgut,
        frist_auch_gegenueber_anderem_bestimmt=frist_auch_gegenueber_anderem_bestimmt,
        inventar_durch_anderen_errichtet=inventar_durch_anderen_errichtet,
        einordnungsnachweis=einordnungsnachweis,
    )
    for name in [
        "erbschaft_gehoert_zum_gesamtgut",
        "anderer_ehegatte_verwaltet_gesamtgut",
        "frist_auch_gegenueber_anderem_bestimmt",
        "inventar_durch_anderen_errichtet",
    ]:
        _wahrheitswert(eingaben[name], name)
    _text(einordnungsnachweis, "einordnungsnachweis")
    wirksam = (
        not anderer_ehegatte_verwaltet_gesamtgut
        or frist_auch_gegenueber_anderem_bestimmt
    )
    if (
        erbschaft_gehoert_zum_gesamtgut
        and anderer_ehegatte_verwaltet_gesamtgut
        and wirksam
        and anderer is None
    ):
        _fehler(
            "fristende_anderer_ehegatte",
            "Bei erforderlicher und erfolgter Fristbestimmung gegenüber dem anderen Ehegatten ist dessen qualifiziertes Fristende erforderlich.",
            "EINGABE_FEHLT",
        )
    ende = None
    if wirksam:
        ende = (
            max(erbe, anderer)
            if anderer_ehegatte_verwaltet_gesamtgut and anderer is not None
            else erbe
        )
    wert = None
    if erbschaft_gehoert_zum_gesamtgut:
        wert = dict(
            fristbestimmung_nach_2008_wirksam=wirksam,
            inventarfristende_erbe=ende.isoformat() if ende is not None else None,
            inventar_kommt_erben_zustatten=inventar_durch_anderen_errichtet,
        )
    ergebnis = _ergebnis(
        wert,
        "daten_und_wahrheitswerte",
        "BGB_INVENTARFRIST_EHEGATTEN",
        eingaben,
        [
            dict(
                operation="Erforderliche Fristbestimmung gegenüber verwaltendem Ehegatten prüfen; wirksames Fristende ist Maximum beider qualifizierter Enden; wirksames Inventar des anderen kommt Erben zustatten"
            )
        ],
        eingaben.copy(),
    )
    ergebnis["status"] = (
        "BERECHNET" if erbschaft_gehoert_zum_gesamtgut else "NICHT_ANWENDBAR"
    )
    ergebnis["annahmen"] = [
        "Qualifizierte Inventarfristenden und rechtswirksame Inventarerrichtung vorgegeben; Gesamtgutzugehörigkeit und Verwaltung rechtlich bestimmt. §2008 gilt auch nach Beendigung der Gütergemeinschaft."
    ]
    ergebnis["hinweise"] = [
        "Nur zusätzliche Wirksamkeitsbedingung des §2008, keine Prüfung sämtlicher Voraussetzungen der Fristbestimmung oder unbeschränkter Erbenhaftung. Fristende des Erben ohne die Verlängerung durch §2008 eingeben; Fristende des anderen einschließlich anderweitiger gesetzlicher Verlängerungen. Ohne erforderliche Bestimmung gegenüber dem verwaltenden anderen Ehegatten ergibt sich kein wirksames Fristende, nicht das ursprüngliche Ende. Verwaltet der andere weder allein noch gemeinsam, wird sein Fristende nicht zur Verlängerung verwendet. Inventarzurechnung nach Absatz1 Satz3 wird nicht zusätzlich von dessen Verwaltungsberechtigung abhängig gemacht. Qualifizierte tatsächliche Inventarerrichtung, nicht bloßer Entwurf. Keine automatische Heilung früheren Fristversäumnisses oder abschließende Haftungsbefreiung. Gesamtgutzugehörigkeit und einschlägige Verwaltung nach Beendigung der Gütergemeinschaft entsprechend Absatz2 bestimmen; Beendigung allein schließt die Regel nicht aus."
    ]
    return ergebnis
