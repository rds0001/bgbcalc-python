"""Gesetzliche Vorlegungs- und Verjährungsgrundfristen (§801)."""
from .betraege import _wahrheitswert
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _text


def schuldverschreibung_vorlegungsfrist(
    urkundenart=None, leistungszeit_am=None, leistungszeit_beginnart=None, prueftag=None,
    vorlegung_am=None, gerichtliche_geltendmachung_am=None,
    gesetzlicher_unveraenderter_fristenlauf=None, einordnungsnachweis=None,
):
    """§801: 30 Jahre oder vier Jahre ab Jahresschluss, danach gegebenenfalls zwei Jahre."""
    _auswahl(urkundenart, 'urkundenart', ('hauptschuldverschreibung', 'zinsschein', 'rentenschein', 'gewinnanteilschein'))
    leistung = _datum(leistungszeit_am, 'leistungszeit_am')
    _auswahl(leistungszeit_beginnart, 'leistungszeit_beginnart', ('ereignis', 'tagesbeginn'))
    tag = _datum(prueftag, 'prueftag')
    if tag < leistung:
        _fehler('prueftag', 'Prüftag darf nicht vor Eintritt der Leistungszeit liegen.')
    vorlegung = _datum(vorlegung_am, 'vorlegung_am') if vorlegung_am is not None else None
    gerichtlich = (_datum(gerichtliche_geltendmachung_am, 'gerichtliche_geltendmachung_am')
        if gerichtliche_geltendmachung_am is not None else None)
    for name, datum in [('vorlegung_am', vorlegung), ('gerichtliche_geltendmachung_am', gerichtlich)]:
        if datum is not None and not leistung <= datum <= tag:
            _fehler(name, 'Qualifiziertes Wahrungsereignis muss zwischen Leistungszeit und Prüftag liegen.')
    _wahrheitswert(gesetzlicher_unveraenderter_fristenlauf, 'gesetzlicher_unveraenderter_fristenlauf')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    if urkundenart == 'hauptschuldverschreibung':
        vorlegungsende = _frist(leistungszeit_am, 30, 'jahre', leistungszeit_beginnart)
    else:
        vorlegungsende = _frist(f'{leistung.year:04}-12-31', 4, 'jahre', 'ereignis')
    gewahrt = ((vorlegung is not None and vorlegung <= vorlegungsende)
        or (gerichtlich is not None and gerichtlich <= vorlegungsende))
    verjaehrungsende = (_frist(vorlegungsende.isoformat(), 2, 'jahre', 'ereignis') if gewahrt else None)
    eingaben = dict(urkundenart=urkundenart, leistungszeit_am=leistungszeit_am,
        leistungszeit_beginnart=leistungszeit_beginnart, prueftag=prueftag,
        vorlegung_am=vorlegung_am, gerichtliche_geltendmachung_am=gerichtliche_geltendmachung_am,
        gesetzlicher_unveraenderter_fristenlauf=gesetzlicher_unveraenderter_fristenlauf,
        einordnungsnachweis=einordnungsnachweis)
    wert = None if not gesetzlicher_unveraenderter_fristenlauf else dict(
        vorlegungsfristende=vorlegungsende.isoformat(), vorlegungsfrist_gewahrt=gewahrt,
        anspruch_nach_801_erloschen=not gewahrt and tag >= vorlegungsende,
        verjaehrungsgrundfristende=verjaehrungsende.isoformat() if verjaehrungsende is not None else None,
        verjaehrungsgrundfrist_abgelaufen=verjaehrungsende is not None and tag >= verjaehrungsende)
    ergebnis = _ergebnis(wert, 'daten_und_wahrheitswerte', 'BGB_SCHULDVERSCHREIBUNG_VORLEGUNGSFRIST', eingaben,
        [dict(operation='Haupturkunde30 Jahre ab Leistungszeit; Scheine4 Jahre ab Jahresschluss; bei rechtzeitiger Vorlegung oder gerichtlicher Geltendmachung2 Jahre ab Vorlegungsfristende')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if gesetzlicher_unveraenderter_fristenlauf else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Gesetzlicher unveränderter Fristenlauf, qualifizierte Urkundenart und Leistungszeit; Prüfung zum Ende des Prüftags; rechtzeitige Wahrung am Endtag wird vorrangig berücksichtigt; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['Nur Inhaberschuldverschreibungen und genannte Scheine nach§801. Bei Haupturkunde Beginnart rechtlich bestimmen: festgelegter Tagesbeginn wird mitgezählt, Ereignistag nicht; bei Scheinen zwingender Jahresschlussbeginn unabhängig von dieser Eingabe. Gerichtliche Geltendmachung muss Anspruch aus der Urkunde betreffen; bloße Mahnung oder Verlustanzeige§804 genügt nicht. NULL bedeutet bis Prüftag keine entsprechende Vorlegung/Geltendmachung, nicht unbekannt. Frühere Handlungen vor Leistungszeit werden in diesem Modell nicht bewertet. Zwei Jahre beginnen nach Ende der Vorlegungsfrist, nicht nach tatsächlicher früher Vorlegung. Abweichende Dauer/Beginn in Urkunde§801 Absatz3, Zahlungssperre§802, sonstige Hemmung/Neubeginn und zulässige Kalenderkorrekturen führen aus diesem unveränderten Standardmodell heraus. Keine pauschale Feiertagsverlängerung. Verjährung bedeutet nicht Erlöschen; Einrede/Ausübung und weitere Anspruchsvoraussetzungen gesondert prüfen. Kein automatischer Anspruch aus Verlustanzeige§804 und keine automatische Verbindung von Hauptforderung und selbständigen Zinsscheinen§803.']
    return ergebnis
