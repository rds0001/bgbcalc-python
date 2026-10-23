"""Grundfrist der Buchersitzung (§900), ohne automatische Hemmungs- oder Erwerbsprüfung."""
from .betraege import _wahrheitswert
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _text


def buchersitzung_dreissigjahresfrist(eintragung_am=None, besitzbeginn_am=None,
    beginnart=None, rechtsart=None, korrigiertes_fristende=None, prueftag=None,
    zusammenhaengender_zeitraum_qualifiziert=None, einordnungsnachweis=None):
    """Dreißig Jahre ab gleichzeitig bestehender Eintragung und qualifiziertem Besitz."""
    eintragung = _datum(eintragung_am, 'eintragung_am')
    besitz = _datum(besitzbeginn_am, 'besitzbeginn_am')
    _auswahl(beginnart, 'beginnart', ('ereignis', 'tagesbeginn'))
    _auswahl(rechtsart, 'rechtsart', ('eigentum', 'anderes_besitzbezogenes_recht'))
    tag = _datum(prueftag, 'prueftag')
    if eintragung > tag:
        _fehler('eintragung_am', 'Eintragung darf nicht nach dem Prüftag liegen.')
    if besitz > tag:
        _fehler('besitzbeginn_am', 'Besitzbeginn darf nicht nach dem Prüftag liegen.')
    beginn = max(eintragung, besitz)
    grundende = _frist(beginn.isoformat(), 30, 'jahre', beginnart)
    ende = _datum(korrigiertes_fristende, 'korrigiertes_fristende')
    if ende < grundende:
        _fehler('korrigiertes_fristende', 'Korrigiertes Ende darf die ungekürzte Grundfrist dieses Zeitraums nicht unterschreiten.')
    _wahrheitswert(zusammenhaengender_zeitraum_qualifiziert, 'zusammenhaengender_zeitraum_qualifiziert')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    eingaben = dict(eintragung_am=eintragung_am, besitzbeginn_am=besitzbeginn_am,
        beginnart=beginnart, rechtsart=rechtsart, korrigiertes_fristende=korrigiertes_fristende,
        prueftag=prueftag, zusammenhaengender_zeitraum_qualifiziert=zusammenhaengender_zeitraum_qualifiziert,
        einordnungsnachweis=einordnungsnachweis)
    wert = dict(gemeinsamer_beginn_am=beginn.isoformat(), dreissigjahresgrundfristende=grundende.isoformat(),
        massgebliches_fristende=ende.isoformat(), frist_am_prueftag_abgelaufen=tag >= ende)
    ergebnis = _ergebnis(wert, 'daten_und_wahrheitswerte', 'BGB_BUCHERSITZUNG_DREISSIGJAHRESFRIST', eingaben,
        [dict(operation='Späteren Eintragungs-/Besitzbeginn bestimmen; dreißig Jahre nach qualifizierter Beginnart; korrigiertes Ende am Tagesende vergleichen')], eingaben.copy())
    if not zusammenhaengender_zeitraum_qualifiziert:
        ergebnis['wert'] = None
        ergebnis['status'] = 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Fristprüfung nach vollständigem Ablauf des Prüftags, nicht zu dessen Beginn. Feste lokale BGB-Fassung; zusammenhängender qualifizierter Zeitraum ohne anzurechnende Vorgängerzeiten.']
    ergebnis['hinweise'] = ['Nur Fristberechnung, keine abschließende Feststellung eines Eigentums- oder Rechtserwerbs. Eintragung und Eigenbesitz müssen gleichzeitig vorliegen; bei Absatz2 qualifizierter besitzbezogener Rechtszustand. Recht steht dem Eingetragenen ursprünglich nicht zu. Beginnart bezieht sich auf das erstmalige gemeinsame Vorliegen: Ereignis im Tagesverlauf oder rechtlich maßgeblicher Tagesbeginn. Widerspruch gegen die Eintragung hemmt gemäß§900 Absatz1 Satz3; sonstige anwendbare Hemmungs-/Ablaufregeln müssen im begründeten korrigierten Fristende enthalten sein. Bei ungeklärtem oder nicht bestimmbaren Ende keine Berechnung mit einem erfundenen Datum. Unterbrechung, Neustart, Besitzvermutung und Zurechnung fremder Besitzzeiten werden nicht automatisch geprüft; solche Fälle erst rechtlich auf einen zulässigen zusammenhängenden Zeitraum reduzieren. Kein Gutglaubenserfordernis aus§937 Absatz2 übertragen. Rang anderer Rechte nach§900 Absatz2 Satz2 wird nicht berechnet. Keine automatische Wochenend-/Feiertagsverschiebung.']
    return ergebnis
