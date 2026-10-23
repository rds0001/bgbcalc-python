"""Numerische Dreißigtage-Grundfrist für Entgeltforderungen (§286 Absatz3)."""
from .betraege import _wahrheitswert
from .kalender import _auswahl, _datum, _ergebnis, _frist, _tage_addieren, _text


def entgeltforderung_dreissigtagefrist(faelligkeit_am=None, bezugsereignis_am=None,
        bezugsart=None, dreissigtageregel_anwendbar=None, einordnungsnachweis=None):
    """30Tage ab späterem Datum aus Fälligkeit und qualifiziertem Rechnungs-/Leistungsempfang."""
    faellig = _datum(faelligkeit_am, 'faelligkeit_am')
    bezug = _datum(bezugsereignis_am, 'bezugsereignis_am')
    _auswahl(bezugsart, 'bezugsart', ('rechnungszugang', 'gegenleistungsempfang_bei_unsicherem_zugang'))
    _wahrheitswert(dreissigtageregel_anwendbar, 'dreissigtageregel_anwendbar')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    beginn = max(faellig, bezug)
    ende = _frist(beginn.isoformat(), 30, 'tage', 'ereignis')
    folgetag = _tage_addieren(ende, 1)
    eingaben = dict(faelligkeit_am=faelligkeit_am, bezugsereignis_am=bezugsereignis_am,
        bezugsart=bezugsart, dreissigtageregel_anwendbar=dreissigtageregel_anwendbar,
        einordnungsnachweis=einordnungsnachweis)
    wert = dict(massgeblicher_beginn=beginn.isoformat(), grundfristende=ende.isoformat(),
        tag_nach_grundfrist=folgetag.isoformat()) if dreissigtageregel_anwendbar else None
    ergebnis = _ergebnis(wert, 'daten', 'BGB_ENTGELTFORDERUNG_DREISSIGTAGEFRIST', eingaben,
        [dict(operation='Späteres Datum aus Fälligkeit und qualifiziertem Bezug wählen;30Kalendertage nach Ereignisbeginn und nachfolgenden Tag berechnen')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if dreissigtageregel_anwendbar else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Qualifizierter Fall des§286 Absatz3; unveränderte rechnerische Grundfrist der festen lokalen BGB-Fassung.']
    ergebnis['hinweise'] = ['Rechnungszugang umfasst gleichwertige Zahlungsaufstellung. Bei Verbrauchern ist der besondere Hinweis auf die Folgen erforderlich. Ersatzanknüpfung an Gegenleistungsempfang gilt nur bei unsicherem Rechnungszugang und Nichtverbrauchern. Diese Voraussetzungen sind im Anwendungsnachweis zu bestätigen; die Fristberechnung entscheidet sie nicht selbst. Datum der Fälligkeit nicht durch Rechnungsdatum ersetzen. Tag nach Grundfrist ist kein abschließend festgestellter Verzugsbeginn: frühere Verzugsgründe, Leistung, Vertretenmüssen, zulässige Kalenderkorrekturen und Vereinbarungen gesondert berücksichtigen. Keine automatische Feiertagsverschiebung oder Verzinsung.']
    return ergebnis
