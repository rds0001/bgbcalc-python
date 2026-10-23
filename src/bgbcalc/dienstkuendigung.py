"""Gesetzliche ordentliche Kündigungstermine sonstiger Dienstverhältnisse (§621)."""
from calendar import monthrange
from datetime import date
from .betraege import _wahrheitswert
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _tage_addieren, _text


def dienstverhaeltnis_kuendigungstermin(zugang_kuendigung=None, verguetungsbemessung=None,
    erwerbstaetigkeit_vollstaendig_oder_hauptsaechlich=None, erster_werktag_der_zugangswoche=None,
    gesetzliche_regel_621_anwendbar=None, einordnungsnachweis=None):
    """§621 Nummern1–5: Tages-, Wochen-, Monats-, Quartals- und sonstige Vergütungsbemessung."""
    zugang = _datum(zugang_kuendigung, 'zugang_kuendigung')
    _auswahl(verguetungsbemessung, 'verguetungsbemessung', ('tage', 'wochen', 'monate', 'vierteljahre_oder_laenger', 'ohne_zeitabschnitte'))
    _wahrheitswert(erwerbstaetigkeit_vollstaendig_oder_hauptsaechlich, 'erwerbstaetigkeit_vollstaendig_oder_hauptsaechlich')
    _wahrheitswert(gesetzliche_regel_621_anwendbar, 'gesetzliche_regel_621_anwendbar')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    erster = None
    if erster_werktag_der_zugangswoche is not None or verguetungsbemessung == 'wochen':
        erster = _datum(erster_werktag_der_zugangswoche, 'erster_werktag_der_zugangswoche')
        montag = _tage_addieren(zugang, -zugang.weekday())
        samstag = _tage_addieren(montag, 5)
        if not montag <= erster <= samstag:
            _fehler('erster_werktag_der_zugangswoche', 'Erster Werktag muss zwischen Montag und Samstag der Zugangswoche liegen.')
    eingaben = dict(zugang_kuendigung=zugang_kuendigung, verguetungsbemessung=verguetungsbemessung,
        erwerbstaetigkeit_vollstaendig_oder_hauptsaechlich=erwerbstaetigkeit_vollstaendig_oder_hauptsaechlich,
        erster_werktag_der_zugangswoche=erster_werktag_der_zugangswoche,
        gesetzliche_regel_621_anwendbar=gesetzliche_regel_621_anwendbar, einordnungsnachweis=einordnungsnachweis)
    wert = None
    if gesetzliche_regel_621_anwendbar:
        if verguetungsbemessung == 'tage':
            ende = _tage_addieren(zugang, 1)
        elif verguetungsbemessung == 'wochen':
            ende = _tage_addieren(zugang, 5 - zugang.weekday() + (0 if zugang <= erster else 7))
        elif verguetungsbemessung == 'monate':
            bezug = zugang if zugang.day <= 15 else _frist(zugang_kuendigung, 1, 'monate', 'ereignis')
            ende = date(bezug.year, bezug.month, monthrange(bezug.year, bezug.month)[1])
        elif verguetungsbemessung == 'vierteljahre_oder_laenger':
            mindestende = _frist(zugang_kuendigung, 6, 'wochen', 'ereignis')
            monat = ((mindestende.month - 1) // 3 + 1) * 3
            ende = date(mindestende.year, monat, monthrange(mindestende.year, monat)[1])
        elif erwerbstaetigkeit_vollstaendig_oder_hauptsaechlich:
            ende = _frist(zugang_kuendigung, 2, 'wochen', 'ereignis')
        else:
            ende = zugang
        wert = dict(fruehester_beendigungstag=ende.isoformat(),
            ohne_kuendigungsfrist=verguetungsbemessung == 'ohne_zeitabschnitte' and not erwerbstaetigkeit_vollstaendig_oder_hauptsaechlich)
    ergebnis = _ergebnis(wert, 'datum_und_wahrheitswert', 'BGB_DIENSTVERHAELTNIS_KUENDIGUNGSTERMIN', eingaben,
        [dict(operation='Vergütungsbemessung bestimmt gesetzlichen frühesten Beendigungstermin ab Kündigungszugang; Woche mit erstem Werktag und Quartal mit sechs Wochen Vorlauf')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Dienstverhältnis außerhalb§622; maßgeblicher Zugang, Vergütungsbemessung und gesetzliche Kündbarkeit rechtlich bestimmt; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['Bemessung der Vergütung ist nicht automatisch Auszahlungsrhythmus. Nur gesetzliche Standardregel§621, keine Arbeitsverhältnisse§622, Sondergesetze oder abweichenden wirksamen Vereinbarungen. Erster Werktag der Zugangswoche ist anhand örtlicher Feiertage rechtlich zu bestimmen; nicht automatisch Montag und nicht erster persönlicher Arbeitstag. Eingabe wird auf dieselbe Kalenderwoche Montag bis Samstag geprüft; Feiertagsvollständigkeit ist durch Nachweis zu sichern. Kündigung spätestens am ersten Werktag wirkt zum folgenden Samstag derselben Woche, danach frühestens Samstag der Folgewoche. Monatsgrenze15 einschließlich; Quartalsregel sechs Wochen zu März/Juni/September/Dezemberende. Keine automatische Verschiebung von Kündigungszugangsgrenzen oder Beendigungsterminen nach§193. Ohne Zeitbemessung und ohne überwiegende Erwerbsbeanspruchung keine Kündigungsfrist; Datum bezeichnet Zugangstag, nicht eine erfundene Bindung bis Tagesende. Kündigungswirksamkeit, Befristung, besondere Verbote und tatsächliche Bestimmung des Termins separat.']
    return ergebnis
