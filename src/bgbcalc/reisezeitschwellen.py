"""Stundengenaue Reiseschwellen auf ausdrücklich normalisierten UTC-Zeitpunkten."""
import re
from datetime import datetime, timezone
from .kalender import _auswahl, _ergebnis, _fehler, _text


def _reise_utc_zeitpunkt(wert,name):
    _text(wert,name)
    if not re.fullmatch(r'[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z',wert):
        _fehler(name,'Sekundengenauer UTC-Zeitpunkt YYYY-MM-DDTHH:MM:SSZ erforderlich; keine stille Zeitzonenannahme oder Rundung.')
    try:
        return datetime.strptime(wert,'%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)
    except ValueError:
        _fehler(name,'Ungültiger UTC-Zeitpunkt im Kalenderbereich0001..9999.')


def reise_stundengrenze(regelfall=None, zeitraum_von_utc=None, zeitraum_bis_utc=None, zeitnachweis=None):
    """UTC-Zeitspanne mit strikter24Stunden-, einschließlich24Stunden- oder48Stunden-Grenze vergleichen."""
    faelle={'tagesreise_dauer':(86400,'weniger_als'),'onlinebuchung_verbund':(86400,'hoechstens'),'veranstalter_ruecktritt_kurzreise':(172800,'mindestens'),'beherbergungsausnahme_vorabinformation':(172800,'mindestens')}
    _auswahl(regelfall,'regelfall',tuple(faelle));von=_reise_utc_zeitpunkt(zeitraum_von_utc,'zeitraum_von_utc');bis=_reise_utc_zeitpunkt(zeitraum_bis_utc,'zeitraum_bis_utc');_text(zeitnachweis,'zeitnachweis')
    if bis<von:
        _fehler('zeitraum_bis_utc','Endzeitpunkt darf nicht vor Anfangszeitpunkt liegen.')
    dauer=bis-von;sekunden=dauer.days*86400+dauer.seconds;grenze,vergleich=faelle[regelfall]
    eingehalten=sekunden<grenze if vergleich=='weniger_als' else sekunden<=grenze if vergleich=='hoechstens' else sekunden>=grenze
    eingaben=dict(regelfall=regelfall,zeitraum_von_utc=zeitraum_von_utc,zeitraum_bis_utc=zeitraum_bis_utc,zeitnachweis=zeitnachweis)
    wert=dict(zeitspanne_sekunden=sekunden,grenzdauer_sekunden=grenze,vergleich=vergleich,grenze_erfuellt=eingehalten)
    ergebnis=_ergebnis(wert,'sekunden_und_wahrheitswert','BGB_REISE_STUNDENGRENZE',eingaben,[dict(operation='Normalisierte UTC-Zeitpunkte mit Standard-Datumsbibliothek voneinander abziehen; strikte oder einschließlich geltende Stundengrenze vergleichen.')],eingaben.copy())
    ergebnis['hinweise']=['tagesreise_dauer:651aV2/651cIII, vom Reisebeginn bis Reiseende strikt weniger als24Stunden; fehlende Übernachtung und gegebenenfalls500EUR-Grenze separat. onlinebuchung_verbund:651cI3, Bestätigung des ersten Vertragsschlusses bis Abschluss des weiteren Vertrags höchstens24Stunden; Datenübermittlung/weitere Voraussetzungen separat. veranstalter_ruecktritt_kurzreise:651hIV1c, maßgeblicher Rücktrittszugang bis Reisebeginn mindestens48Stunden, nur qualifizierte Reisedauer unter zwei Tagen; möglicherweise frühere Vertragsfrist zusätzlich. beherbergungsausnahme_vorabinformation:651kV, qualifizierte Information an Veranstalter bis Reisebeginn mindestens48Stunden; persönliche Voraussetzungen und weitere Ausnahmen separat. Nur nachweislich auf volle Sekunden normalisierte UTC-Zeitpunkte; keine lokale Zeitzone erraten, Subsekunden nicht abschneiden. POSIX-Zeitrechnung ohne Schaltsekundendarstellung, keine Kalender-Tagesfrist in Stunden umdeuten.']
    return ergebnis
