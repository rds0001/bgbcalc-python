"""Zahlen- und Bekanntmachungsfristen bei Stiftungszusammenlegung (§§86a/86g/86h)."""
from .kalender import _datum, _ergebnis, _fehler, _frist, _ganzzahl, _tage_addieren, _text
from .zahlen import GRENZE


def stiftung_uebergang_bekanntmachungsfristen(wirkungen_am=None, veroeffentlichung_am=None, einordnungsnachweis=None):
    """Ein Monat Veröffentlichung, zwei Tage Bekanntmachungswirkung, sechs Monate Anmeldung."""
    wirkung = _datum(wirkungen_am, 'wirkungen_am')
    veroeffentlichung = _datum(veroeffentlichung_am, 'veroeffentlichung_am')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    if veroeffentlichung < wirkung:
        _fehler('veroeffentlichung_am', 'Dieses Modell verlangt Veröffentlichung ab Eintritt der Wirkungen nach§86f.')
    bekanntmachungsfrist = _frist(wirkungen_am, 1, 'monate', 'ereignis')
    bewirkt = _tage_addieren(veroeffentlichung, 2)
    anmeldung = _frist(bewirkt.isoformat(), 6, 'monate', 'ereignis')
    eingaben = dict(wirkungen_am=wirkungen_am, veroeffentlichung_am=veroeffentlichung_am, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(dict(rechnerisches_bekanntmachungsfristende=bekanntmachungsfrist.isoformat(),
        bekanntmachung_bewirkt_mit_ablauf=bewirkt.isoformat(), rechnerisches_anmeldefristende=anmeldung.isoformat()),
        'daten_und_wahrheitswerte', 'BGB_STIFTUNG_UEBERGANG_BEKANNTMACHUNGSFRISTEN', eingaben,
        [dict(operation='Wirkungsereignis plus ein Monat; tatsächliche Veröffentlichung plus zwei Tage; bewirkte Bekanntmachung plus sechs Monate')], eingaben.copy())
    ergebnis['annahmen'] = ['Rechtlich wirksame Zulegung/Zusammenlegung und ordnungsgemäße Bundesanzeigerveröffentlichung vorgegeben; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['Grundfristen§§86g/86h, keine umfassende Sicherungsberechtigung. Wirkungsereignis nach§86f ist Unanfechtbarkeit der maßgeblichen Genehmigung/Entscheidung, nicht bloße Vertragsunterzeichnung. Bekanntmachungswirkung mit Ablauf des zweiten Tages; Gläubigeranmeldefrist ab dieser Wirkung, nicht unmittelbar ab Veröffentlichung. Auch verspätete Veröffentlichung erzeugt eigene tatsächliche Bekanntmachungswirkung, kein Rückdatieren auf Bekanntmachungsfristende. Fristwahrung/§193 oder sonstige einschlägige Korrekturen separat prüfen. Anspruch vor Wirkungsereignis entstanden, noch nicht fällig, schriftliche Anmeldung nach Grund/Höhe und glaubhaft gemachte Gefährdung sind rechtliche Voraussetzungen, keine automatischen Geldbeträge. Frühere Veröffentlichungen vor Wirkungsereignis außerhalb dieses Modells.']
    return ergebnis


def stiftung_zusammenlegung_mindestzahl(anzahl_uebertragender_stiftungen=None):
    """§86a: mindestens zwei übertragende Stiftungen; neue übernehmende Stiftung nicht mitzählen."""
    anzahl = _ganzzahl(anzahl_uebertragender_stiftungen, 'anzahl_uebertragender_stiftungen', 0, GRENZE)
    eingaben = dict(anzahl_uebertragender_stiftungen=anzahl_uebertragender_stiftungen)
    ergebnis = _ergebnis(dict(mindestzahl=2, mindestzahl_erreicht=anzahl >= 2),
        'anzahl_und_wahrheitswert', 'BGB_STIFTUNG_ZUSAMMENLEGUNG_MINDESTZAHL', eingaben,
        [dict(operation='Zahl übertragender Stiftungen mit Mindestzahl zwei vergleichen')], eingaben.copy())
    ergebnis['annahmen'] = ['Gezählt werden ausschließlich rechtlich bestimmte übertragende Stiftungen; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['Neue übernehmende Stiftung nicht als weitere übertragende Stiftung mitzählen. Nur Zahlenvoraussetzung§86a, keine Genehmigungs- oder Zulässigkeitsentscheidung und keine Prüfung der Nummern1bis3. Zulegung auf bestehende Stiftung ist anderer Fall.']
    return ergebnis
