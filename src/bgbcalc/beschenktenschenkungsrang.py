"""Zeitlich eindeutige Schenkungsvorgänge mit wiederholten Empfängern (§2329III)."""
from .beschenktenrang import pflichtteilsergaenzung_beschenktenrang
from .kalender import _ergebnis, _fehler, _text, _vorhanden
from .zahlen import _addieren, _bruch, _zahleneingabe
from .zinsen import _bruchteile


def pflichtteilsergaenzung_schenkungsvorgaenge(fehlbetrag=None, schenkungen=None,
    vorgangsgrenzen_qualifiziert=None, einordnungsnachweis=None):
    """Eindeutig zeitlich geordnete Vorgangsgrenzen abarbeiten und Haftungsbeträge je Empfänger summieren."""
    _vorhanden(schenkungen, 'schenkungen')
    if not isinstance(schenkungen, list) or not 1 <= len(schenkungen) <= 1000:
        _fehler('schenkungen', 'Liste1..1000 zeitlich eindeutig geordneter Schenkungsvorgänge erforderlich.')
    kernliste = []
    empfaenger = []
    for p in schenkungen:
        if not isinstance(p, dict) or set(p) != {'schenkung_id', 'beschenkter_id', 'schenkungsrang', 'haftungsgrenze'}:
            _fehler('schenkungen', 'Genau schenkung_id, beschenkter_id, schenkungsrang und haftungsgrenze erforderlich.')
        empfaenger.append(_text(p['beschenkter_id'], 'beschenkter_id'))
        kernliste.append(dict(beschenkter_id=p['schenkung_id'], schenkungsrang=p['schenkungsrang'], haftungsgrenze=p['haftungsgrenze']))
    kern = pflichtteilsergaenzung_beschenktenrang(fehlbetrag, kernliste, vorgangsgrenzen_qualifiziert, einordnungsnachweis)
    wert = None
    if kern['wert'] is not None:
        summen = {}
        vorgaenge = []
        for p, name, q in zip(schenkungen, empfaenger, kern['wert']['zugeordnete_haftung']):
            betrag = _zahleneingabe(q['haftungsbetrag'])
            summen[name] = _addieren(summen.get(name, _bruch(0)), betrag)
            vorgaenge.append(dict(schenkung_id=p['schenkung_id'], beschenkter_id=name, haftungsbetrag=q['haftungsbetrag']))
        wert = dict(haftung_je_schenkung=vorgaenge, haftung_je_beschenktem=[dict(beschenkter_id=name, haftungsbetrag=_bruchteile(b)) for name, b in summen.items()],
            nicht_gedeckter_fehlbetrag=kern['wert']['nicht_gedeckter_fehlbetrag'])
    eingaben = dict(fehlbetrag=fehlbetrag, schenkungen=schenkungen, vorgangsgrenzen_qualifiziert=vorgangsgrenzen_qualifiziert,
        einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert, 'EUR', 'BGB_PFLICHTTEILSERGAENZUNG_SCHENKUNGSVORGAENGE', eingaben,
        [dict(operation='Zeitlich eindeutige Schenkungsvorgänge spätere zuerst mit vorhandenem Haftungsgrenzenkern verteilen; Vorgangsanteile je wiederholt Beschenktem summieren')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Jede Schenkung mit eindeutiger zeitlicher Rangposition und rechtlich vorqualifizierter eigener überschneidungsfreier Haftungsgrenze; Empfänger dürfen mehrfach vorkommen.']
    ergebnis['hinweise'] = ['schenkung_id und Rang müssen eindeutig sein, beschenkter_id darf wiederholt werden. Höherer Rang bedeutet späterer Vorgang; nicht pauschal alle Geschenke eines Empfängers auf dessen letzten Zeitpunkt zusammenziehen. Grenzen je Vorgang bereits nach Bereicherungsrecht,2319/2328-Schutz soweit einschlägig und sonstigen Einwendungen qualifizieren; eine gemeinsame personenbezogene Haftungsgrenze nicht mehrfach als selbständige Vorgangsgrenze verwenden. Keine bloß tatsächliche Zahlungsunfähigkeit anstelle rechtlicher Nichtverpflichtung. Gleichzeitige Schenkungen und ungeklärte Rangfolge bleiben außerhalb, keine erfundene Gleichquote oder Gesamtschuldregel. Geldwerte nur numerische Haftungs-/Befriedigungsgrenzen, keine automatische Geldschuld aus Sachherausgabe.']
    return ergebnis
