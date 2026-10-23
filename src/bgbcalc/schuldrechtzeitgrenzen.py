"""Numerische Zeitgrenzen aus dem Schuldrecht, ohne eigenständige Wirksamkeitsprüfung."""
from .betraege import _wahrheitswert
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _text

_ZEITGRENZEN = {
    'zahlungsvereinbarung_271a_absatz_1': (60, 'tage'),
    'oeffentliche_zahlung_271a_absatz_2_nummer_1': (30, 'tage'),
    'oeffentliche_zahlung_271a_absatz_2_nummer_2': (60, 'tage'),
    'abnahme_271a_absatz_3': (30, 'tage'),
    'agb_zahlung_308_nummer_1a': (30, 'tage'),
    'agb_abnahme_308_nummer_1b': (15, 'tage'),
    'agb_preiserhoehung_309_nummer_1': (4, 'monate'),
    'agb_laufzeit_309_nummer_9a': (2, 'jahre'),
    'agb_verlaengerungskuendigung_309_nummer_9b': (1, 'monate'),
    'finanzvorgaenge_312_absatz_5': (1, 'jahre'),
    'leistungsbestimmung_anfechtung_318_absatz_2': (30, 'jahre'),
}


def schuldrechtliche_zeitgrenze(regelfall=None, anfangstag=None, beginnart=None,
        vergleichstag=None, gesetzliche_zeitgrenze_anwendbar=None, einordnungsnachweis=None):
    """Gesetzliche numerische Grenze und Abstand eines Vergleichstags berechnen."""
    _auswahl(regelfall, 'regelfall', tuple(_ZEITGRENZEN))
    anfang = _datum(anfangstag, 'anfangstag')
    _auswahl(beginnart, 'beginnart', ('ereignis', 'tagesbeginn'))
    vergleich = _datum(vergleichstag, 'vergleichstag')
    if vergleich < anfang:
        _fehler('vergleichstag', 'Vergleichstag darf nicht vor dem Anfangstag liegen.')
    _wahrheitswert(gesetzliche_zeitgrenze_anwendbar, 'gesetzliche_zeitgrenze_anwendbar')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    anzahl, einheit = _ZEITGRENZEN[regelfall]
    grenze = _frist(anfangstag, anzahl, einheit, beginnart)
    eingaben = dict(regelfall=regelfall, anfangstag=anfangstag, beginnart=beginnart,
        vergleichstag=vergleichstag, gesetzliche_zeitgrenze_anwendbar=gesetzliche_zeitgrenze_anwendbar,
        einordnungsnachweis=einordnungsnachweis)
    wert = dict(grenztag=grenze.isoformat(), abstand_zur_grenze_tage=(vergleich-grenze).days,
        zeitgrenze_ueberschritten=vergleich > grenze) if gesetzliche_zeitgrenze_anwendbar else None
    ergebnis = _ergebnis(wert, 'datum_tage_und_wahrheitswert', 'BGB_SCHULDRECHTLICHE_ZEITGRENZE', eingaben,
        [dict(operation='Für den gewählten Normfall gesetzliche Dauer ab qualifiziertem Beginn berechnen; Vergleichstag minus Grenztag in Kalendertagen')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if gesetzliche_zeitgrenze_anwendbar else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Qualifizierter Anwendungsfall und Beginn; reine unveränderte Zeitgrenze der lokalen BGB-Fassung.']
    ergebnis['hinweise'] = ['Kein abschließendes Urteil zur Klauselwirksamkeit, Angemessenheit, Anfechtung oder Informationspflicht. Genau am Grenztag ist die Grenze nicht überschritten. Anwendungsbereich, Beginnart, Beweisvermutungen und gesetzliche Ausnahmen anhand des Fachvertrags vorgeben. Kalenderkorrekturen, Hemmung und abweichende Vereinbarungen sind nicht eingerechnet; bei erforderlicher Korrektur diesen Standardfall nicht verwenden.']
    return ergebnis


def digitale_produkte_verjaehrungsgrundfrist(bereitstellung_am=None, bereitstellungsende_am=None,
        aktualisierungsende_am=None, mangel_gezeigt_am=None, unveraenderter_anwendungsfall=None,
        einordnungsnachweis=None):
    """Zweijahresfrist mit anwendbaren Zwölf-/Viermonats-Mindestabläufen nach§327j."""
    beginn = _datum(bereitstellung_am, 'bereitstellung_am')
    daten = {}
    for name, eingabe in [('bereitstellungsende_am', bereitstellungsende_am),
            ('aktualisierungsende_am', aktualisierungsende_am), ('mangel_gezeigt_am', mangel_gezeigt_am)]:
        datum = _datum(eingabe, name) if eingabe is not None else None
        if datum is not None and datum < beginn:
            _fehler(name, 'Datum darf nicht vor der Bereitstellung liegen.')
        daten[name] = datum
    _wahrheitswert(unveraenderter_anwendungsfall, 'unveraenderter_anwendungsfall')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    grundende = _frist(bereitstellung_am, 2, 'jahre', 'ereignis')
    dauerende = _frist(bereitstellungsende_am, 12, 'monate', 'ereignis') if bereitstellungsende_am is not None else None
    updateende = _frist(aktualisierungsende_am, 12, 'monate', 'ereignis') if aktualisierungsende_am is not None else None
    vor_mangel = max(d for d in [grundende, dauerende, updateende] if d is not None)
    mangel = daten['mangel_gezeigt_am']
    mangelzeit = _frist(mangel_gezeigt_am, 4, 'monate', 'ereignis') if mangel is not None and mangel <= vor_mangel else None
    ende = max(vor_mangel, mangelzeit) if mangelzeit is not None else vor_mangel
    eingaben = dict(bereitstellung_am=bereitstellung_am, bereitstellungsende_am=bereitstellungsende_am,
        aktualisierungsende_am=aktualisierungsende_am, mangel_gezeigt_am=mangel_gezeigt_am,
        unveraenderter_anwendungsfall=unveraenderter_anwendungsfall, einordnungsnachweis=einordnungsnachweis)
    wert = dict(zweijahresende=grundende.isoformat(), mindestende_dauerbereitstellung=dauerende.isoformat() if dauerende is not None else None,
        mindestende_aktualisierung=updateende.isoformat() if updateende is not None else None,
        ende_vor_mangelablaufhemmung=vor_mangel.isoformat(), mindestende_mangel=mangelzeit.isoformat() if mangelzeit is not None else None,
        verjaehrungsgrundfristende=ende.isoformat()) if unveraenderter_anwendungsfall else None
    ergebnis = _ergebnis(wert, 'daten', 'BGB_DIGITALE_PRODUKTE_VERJAEHRUNGSGRUNDFRIST', eingaben,
        [dict(operation='Maximum aus2 Jahren nach Bereitstellung und einschlägigen12 Monaten nach Bereitstellungs-/Aktualisierungsende; rechtzeitig gezeigten Mangel mit4 Monaten Mindestablauf berücksichtigen')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if unveraenderter_anwendungsfall else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Qualifizierter Anspruch nach§327i Nummer1 oder3; keine sonstige Friständerung, feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['Optionale Enddaten bedeuten bei NULL, dass der jeweilige Mindestablauf auf diesen Anspruch nicht anwendbar ist; unbekannte erforderliche Enddaten dürfen nicht als NULL ersetzt werden. Aktualisierungsende nur bei Anspruch wegen Verletzung der Aktualisierungspflicht angeben. mangel_gezeigt_am ist erstmaliges Zeigen dieses Mangels; ein erst nach Fristende gezeigter Mangel verlängert nicht. Keine automatische Hemmung, Arglist-, Übergangs- oder Kalenderkorrektur; Rechte nach§327i Nummer2/§218 gesondert. Kein Erlöschen und keine automatische Einrede.']
    return ergebnis
