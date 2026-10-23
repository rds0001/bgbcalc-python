from .kalender import _datum, _ergebnis, _fehler, _text
from .betraege import _geld
from .reisezeitschwellen import _reise_utc_zeitpunkt
from .rueckwaertsfrist_kalendergrenze import rueckwaertsfrist_kalendergrenze

def reise_veranstalterruecktritt_zeitgrenzen(reisedauer_tage=None, reisebeginn_lokal_am=None, reisebeginn_utc=None, ruecktrittszugang_lokal_am=None, ruecktrittszugang_utc=None, vertraglicher_letzter_ruecktritt_utc=None, zeitnachweis=None):
    """Reisedauerklasse bestimmen, gesetzliche20/7Kalendertage oder48Stunden prüfen und mit vertraglicher Rücktrittszeitgrenze verbinden."""
    dauer=_geld(reisedauer_tage);_text(zeitnachweis,'zeitnachweis')
    if dauer<=0:_fehler('reisedauer_tage','Positive rechtlich maßgebliche Reisedauer erforderlich.')
    _datum(reisebeginn_lokal_am,'reisebeginn_lokal_am');r=_datum(ruecktrittszugang_lokal_am,'ruecktrittszugang_lokal_am');beginn=_reise_utc_zeitpunkt(reisebeginn_utc,'reisebeginn_utc');zugang=_reise_utc_zeitpunkt(ruecktrittszugang_utc,'ruecktrittszugang_utc');vertrag=_reise_utc_zeitpunkt(vertraglicher_letzter_ruecktritt_utc,'vertraglicher_letzter_ruecktritt_utc')
    if dauer<2:art='48_stunden';tage=None;tag=None;gesetz=(beginn-zugang).total_seconds()>=172800
    else:
        art='kalendertage';tage=20 if dauer>6 else 7
        tag=rueckwaertsfrist_kalendergrenze(reisebeginn_lokal_am,tage,'tage','ereignistag','nur_taggleiche_monate',zeitnachweis)['wert']['letzter_voller_tag_vor_grenze']
        gesetz=r<=_datum(tag,'letzter_zugangstag') and zugang<beginn
    v=zugang<=vertrag
    wert=dict(gesetzlicher_vorlauf=art,kalendertage_vorlauf=tage,letzter_voller_zugangstag=tag,gesetzliche_zeitgrenze_eingehalten=gesetz,vertragliche_zeitgrenze_eingehalten=v,beide_zeitgrenzen_eingehalten=gesetz and v)
    eingaben = dict(reisedauer_tage=reisedauer_tage, reisebeginn_lokal_am=reisebeginn_lokal_am, reisebeginn_utc=reisebeginn_utc, ruecktrittszugang_lokal_am=ruecktrittszugang_lokal_am, ruecktrittszugang_utc=ruecktrittszugang_utc, vertraglicher_letzter_ruecktritt_utc=vertraglicher_letzter_ruecktritt_utc, zeitnachweis=zeitnachweis)
    ergebnis = _ergebnis(wert,'daten_und_wahrheitswerte','BGB_REISE_VERANSTALTERRUECKTRITT_ZEITGRENZEN',eingaben,[dict(operation='Reisedauerklasse bestimmen, gesetzliche20/7Kalendertage oder48Stunden prüfen und mit vertraglicher Rücktrittszeitgrenze verbinden.')],eingaben.copy())
    ergebnis["hinweise"] = ['651hIV1: mehrals6Tage→20Kalendertage Vorlauf; mindestens2bis6Tage→7Kalendertage; wenigerals2Tage→48echteStunden. Für Tagesvorläufe ausdrücklich ereignistagbezogene Rückwärtsanalogie: Grenze beginnt am zurückliegenden Vergleichstag, Zugang spätestens bis zum vorhergehenden vollen Tag; keine Umrechnung in480/168Stunden. KurzeReise sekundengenau mindestens48Stunden vor Reisebeginn. Gesetzliche und tatsächliche Vertragsgrenze müssen beide eingehalten sein; vertragliche Frist darf gesetzlichen Mindestschutz nicht verkürzen. Kein automatischer Teilnehmerzahl-/Rücktrittsgrundtest und keine Geldfolge. Reisedauer ist qualifizierte Tagesgröße; Zeitspanne der Reise nicht ungeprüft in24Stunden-Tage umdeuten. Lokaldaten gehören zuUTC-Ereignissen, keine Zeitzone erraten. Keine193-Verlängerung dieses Mindestvorlaufs.651hIV2unverzüglich bleibt qualitative Anforderung, kein erfundener fixer Stundenwert.']
    return ergebnis

