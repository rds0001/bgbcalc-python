"""Dreißigjahresgrenze je Aufschubgrund eines Vermächtnisses (§§2162/2163)."""

from .betraege import _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler, _frist, _text


def vermaechtnis_dreissigjahresgrenze(
    erbfall_am=None,
    aufschubgrund=None,
    massgebliches_ereignis_am=None,
    prueftag=None,
    bestimmtes_personenereignis_angeordnet=None,
    ereignisperson_lebt_beim_erbfall=None,
    ereignisperson_juristische_person=None,
    geschwistervermaechtnis_nach_2163=None,
    einordnungsnachweis=None,
):
    """Ablauf und Ausnahmen für einen qualifizierten Aufschubgrund; keine allgemeine Wirksamkeitsprüfung."""
    erbfall = _datum(erbfall_am, "erbfall_am")
    grund = _text(aufschubgrund, "aufschubgrund")
    if grund not in [
        "bedingung",
        "anfangstermin",
        "zeugung",
        "persoenlichkeitsbestimmung",
    ]:
        _fehler(
            "aufschubgrund",
            "Bedingung, Anfangstermin, Zeugung oder Persönlichkeitsbestimmung als gesetzlich qualifizierten Aufschubgrund wählen.",
        )
    tag = _datum(prueftag, "prueftag")
    if tag < erbfall:
        _fehler("prueftag", "Prüftag darf nicht vor Erbfall liegen.")
    ende = _frist(erbfall_am, 30, "jahre", "ereignis")
    ereignis = None
    if massgebliches_ereignis_am is not None:
        ereignis = _datum(massgebliches_ereignis_am, "massgebliches_ereignis_am")
        if ereignis > tag:
            _fehler(
                "massgebliches_ereignis_am",
                "Nur bis Prüftag tatsächlich eingetretenes Ereignis vorgeben; künftiger Termin als noch nicht eingetreten behandeln.",
            )
        if grund in ["zeugung", "persoenlichkeitsbestimmung"] and ereignis < erbfall:
            _fehler(
                "massgebliches_ereignis_am",
                "Bei§2162 Absatz2 muss das maßgebliche Ereignis nach dem Erbfall liegen; am selben Kalendertag tatsächliche Reihenfolge belegen.",
            )
    eingaben = dict(
        erbfall_am=erbfall_am,
        aufschubgrund=aufschubgrund,
        massgebliches_ereignis_am=massgebliches_ereignis_am,
        prueftag=prueftag,
        bestimmtes_personenereignis_angeordnet=bestimmtes_personenereignis_angeordnet,
        ereignisperson_lebt_beim_erbfall=ereignisperson_lebt_beim_erbfall,
        ereignisperson_juristische_person=ereignisperson_juristische_person,
        geschwistervermaechtnis_nach_2163=geschwistervermaechtnis_nach_2163,
        einordnungsnachweis=einordnungsnachweis,
    )
    for name in [
        "bestimmtes_personenereignis_angeordnet",
        "ereignisperson_lebt_beim_erbfall",
        "ereignisperson_juristische_person",
        "geschwistervermaechtnis_nach_2163",
    ]:
        _wahrheitswert(eingaben[name], name)
    _text(einordnungsnachweis, "einordnungsnachweis")
    ausnahme = (
        (bestimmtes_personenereignis_angeordnet and ereignisperson_lebt_beim_erbfall)
        or geschwistervermaechtnis_nach_2163
    ) and not ereignisperson_juristische_person
    rechtzeitig = ereignis is not None and ereignis <= ende
    abgelaufen = tag >= ende
    wert = dict(
        dreissigjahresfristende=ende.isoformat(),
        frist_am_prueftag_abgelaufen=abgelaufen,
        massgebliches_ereignis_rechtzeitig=rechtzeitig,
        ausnahme_nach_2163=ausnahme,
        unwirksam_wegen_geprueften_aufschubgrundes=abgelaufen
        and not rechtzeitig
        and not ausnahme,
    )
    ergebnis = _ergebnis(
        wert,
        "daten_und_wahrheitswerte",
        "BGB_VERMAECHTNIS_DREISSIGJAHRESGRENZE",
        eingaben,
        [
            dict(
                operation="Dreißig Jahre ab Erbfall; tatsächliches maßgebliches Ereignis spätestens am Endtag verhindert Fristunwirksamkeit, ebenso qualifizierte Ausnahme für natürliche Ereignisperson beziehungsweise Geschwistervermächtnis"
            )
        ],
        eingaben.copy(),
    )
    ergebnis["annahmen"] = [
        "Ein rechtlich qualifizierter Aufschubgrund nach§2162; Prüfung zum Ende des Prüftags. Ereignisse am Endtag geschehen vor Fristablauf um Tagesende."
    ]
    ergebnis["hinweise"] = [
        "Bei mehreren gleichzeitig einschlägigen Aufschubgründen jeden einzeln prüfen; FALSE bestätigt nur fehlende Unwirksamkeit aus diesem Grund, nicht Gesamtwirksamkeit oder Anfall. Zeugung ist Fristwahrungsereignis nach§2162 Absatz2, Geburt ist gesondertes Anfallsereignis nach§2178. Bei Bedingung/Anfangstermin kann das Ereignis bereits vor Erbfall liegen. Bei Zeugung/Persönlichkeitsbestimmung setzt Absatz2 noch fehlendes Ereignis im Zeitpunkt des Erbfalls voraus; am selben Kalendertag Reihenfolge belegen. NULL bedeutet Ereignis bis Prüftag nicht eingetreten, nicht unbekannt. Nach Fristablauf eingetretenes Ereignis heilt ohne einschlägige Ausnahme den Ablauf nicht. Personenereignis muss in Beschwertem oder Bedachtem vorgesehen sein; bloßes Ereignis in beliebiger dritter Person genügt nicht. §2163 Absatz2 belässt bei juristischer Ereignisperson die Dreißigjahresgrenze; widersprüchliche Eingaben zu Leben/Geschwisterfall ersetzen keine rechtliche Qualifikation. Keine automatische Fristverlängerung oder Wochenendverschiebung, kein Nacherbfolgemodell§2109."
    ]
    return ergebnis
