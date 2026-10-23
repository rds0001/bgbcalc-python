"""Erbfallbezogener Beginn besonderer dreijähriger Verjährungsfristen."""
from .betraege import _wahrheitswert
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _text


def erbrecht_sonderverjaehrungsfrist(erbfall_am=None, anspruchsart=None,
    korrigiertes_fristende=None, prueftag=None, anspruchsgrundlage_qualifiziert=None,
    einordnungsnachweis=None):
    """§§195,2287II,2332I: drei Jahre unmittelbar ab Erbfall, kein Jahresendbeginn."""
    erbfall = _datum(erbfall_am, 'erbfall_am')
    _auswahl(anspruchsart, 'anspruchsart', ('vertragserbe_schenkung', 'pflichtteil_beschenkter'))
    grundende = _frist(erbfall_am, 3, 'jahre', 'ereignis')
    ende = _datum(korrigiertes_fristende, 'korrigiertes_fristende')
    tag = _datum(prueftag, 'prueftag')
    if ende < grundende:
        _fehler('korrigiertes_fristende', 'Korrigiertes Ende darf die gesetzliche Dreijahresgrundfrist nicht unterschreiten.')
    if tag < erbfall:
        _fehler('prueftag', 'Prüftag darf nicht vor dem Erbfall liegen.')
    _wahrheitswert(anspruchsgrundlage_qualifiziert, 'anspruchsgrundlage_qualifiziert')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    eingaben = dict(erbfall_am=erbfall_am, anspruchsart=anspruchsart,
        korrigiertes_fristende=korrigiertes_fristende, prueftag=prueftag,
        anspruchsgrundlage_qualifiziert=anspruchsgrundlage_qualifiziert, einordnungsnachweis=einordnungsnachweis)
    wert = dict(grundfristende=grundende.isoformat(), massgebliches_fristende=ende.isoformat(),
        frist_am_prueftag_abgelaufen=tag >= ende) if anspruchsgrundlage_qualifiziert else None
    ergebnis = _ergebnis(wert, 'daten_und_wahrheitswerte', 'BGB_ERBRECHT_SONDERVERJAEHRUNGSFRIST', eingaben,
        [dict(operation='Drei Jahre ab Erbfall statt Jahresende; rechtlich korrigiertes Fristende zum Ende des Prüftags vergleichen')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Feste lokale BGB-Fassung; einschlägiger Anspruch gegen Beschenkten und Fristkorrekturen qualifiziert; Ergebnis zum Ende des Prüftags.']
    ergebnis['hinweise'] = ['Anspruchsarten: Herausgabe an Vertragserben nach§2287 oder Pflichtteilsberechtigten gegen Beschenkten nach§2329 mit Sonderbeginn§2332 Absatz1. Keine Übertragung des Sonderbeginns auf gewöhnlichen Pflichtteilsanspruch gegen Erben. Kenntnis und Jahreswechsel verschieben diesen gesetzlichen Beginn nicht. Korrigiertes Ende muss einschlägige Hemmungen, Ablaufhemmungen und zulässige Kalenderkorrekturen berücksichtigen; keine automatische Feiertagsverschiebung. Warten auf notwendige Ausschlagung begründet nach§2332 Absatz2 keine Hemmung; andere Hemmungsgründe bleiben gesondert zu prüfen. Neubeginn, Titulierung und abweichende Vereinbarungen außerhalb dieser ursprünglichen Fristberechnung. Kein automatisches Erlöschen des Anspruchs, keine Aussage zur Erhebung einer Verjährungseinrede.']
    return ergebnis
