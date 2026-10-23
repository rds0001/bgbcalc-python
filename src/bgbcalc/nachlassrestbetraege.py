"""Bereinigungs- und Deckungsbeträge des Erbrechts (§§1980,2046,2288)."""
from .betraege import _geld, _wahrheitswert
from .kalender import _ergebnis, _fehler, _text
from .zahlen import _addieren, _subtrahieren
from .zinsen import _bruchteile


def _nachlassrest_ergebnis(wert, regel, eingaben, operation, hinweis):
    ergebnis = _ergebnis(wert, 'EUR', regel, eingaben, [dict(operation=operation)], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Feste lokale BGB-Fassung; qualifizierte überschneidungsfreie Betragsgrundlagen.']
    ergebnis['hinweise'] = [hinweis]
    return ergebnis


def nachlass_zulaenglichkeitsbetrag(nachlassaktiva=None, gesamte_nachlassverbindlichkeiten=None,
    enthaltene_vermaechtnisverbindlichkeiten=None, enthaltene_auflagenverbindlichkeiten=None, bewertungsnachweis=None):
    """§1980I3: Vermächtnis-/Auflagenlasten aus Schulden entfernen und Aktiva minus Rest bilden."""
    aktiva = _geld(nachlassaktiva)
    gesamt = _geld(gesamte_nachlassverbindlichkeiten)
    vermaechtnisse = _geld(enthaltene_vermaechtnisverbindlichkeiten)
    auflagen = _geld(enthaltene_auflagenverbindlichkeiten)
    ausgeschlossen = _addieren(vermaechtnisse, auflagen)
    if ausgeschlossen > gesamt:
        _fehler('gesamte_nachlassverbindlichkeiten', 'Enthaltene überschneidungsfreie Vermächtnis-/Auflagenlasten dürfen Gesamtverbindlichkeiten nicht übersteigen.')
    _text(bewertungsnachweis, 'bewertungsnachweis')
    schulden = _subtrahieren(gesamt, ausgeschlossen)
    eingaben = dict(nachlassaktiva=nachlassaktiva, gesamte_nachlassverbindlichkeiten=gesamte_nachlassverbindlichkeiten,
        enthaltene_vermaechtnisverbindlichkeiten=enthaltene_vermaechtnisverbindlichkeiten,
        enthaltene_auflagenverbindlichkeiten=enthaltene_auflagenverbindlichkeiten, bewertungsnachweis=bewertungsnachweis)
    wert = dict(beruecksichtigte_verbindlichkeiten=_bruchteile(schulden), zulaenglichkeitsdifferenz=_bruchteile(_subtrahieren(aktiva, schulden)))
    return _nachlassrest_ergebnis(wert, 'BGB_NACHLASS_ZULAENGLICHKEITSBETRAG', eingaben,
        'Gesamtschulden um darin enthaltene Vermächtnis-/Auflagenverbindlichkeiten bereinigen; bereinigte Schulden von Aktiva abziehen',
        'Nur numerische Bereinigung1980I3. Positive oder negative Differenz ist keine automatische Feststellung von Zahlungsfähigkeit, insolvenzrechtlicher Überschuldung oder Antragspflicht. Aktiva/Schulden nach rechtlich einschlägigen Bewertungsmaßstäben qualifizieren; Pflichtteilslasten nicht allein wegen letztwilliger Verfügung als Vermächtnisse ausnehmen. Ausgenommene Lasten müssen bereits in Gesamtschulden enthalten sein und dürfen einander nicht überlappen.')


def erbteil_individuelle_schuldendeckung(zugeteilter_erbteilwert=None, individuell_zugeordnete_nachlassschuld=None,
    last_nach_2046_abs2_qualifiziert=None, bewertungsnachweis=None):
    """§2046II: persönliche Last des betreffenden Erben nur aus seinem Teilungsanteil decken."""
    anteil = _geld(zugeteilter_erbteilwert)
    schuld = _geld(individuell_zugeordnete_nachlassschuld)
    _wahrheitswert(last_nach_2046_abs2_qualifiziert, 'last_nach_2046_abs2_qualifiziert')
    _text(bewertungsnachweis, 'bewertungsnachweis')
    eingaben = dict(zugeteilter_erbteilwert=zugeteilter_erbteilwert, individuell_zugeordnete_nachlassschuld=individuell_zugeordnete_nachlassschuld,
        last_nach_2046_abs2_qualifiziert=last_nach_2046_abs2_qualifiziert, bewertungsnachweis=bewertungsnachweis)
    wert = None
    if last_nach_2046_abs2_qualifiziert:
        deckung = min(anteil, schuld)
        wert = dict(berichtigung_aus_eigenem_anteil=_bruchteile(deckung), verbleibender_erbteilwert=_bruchteile(_subtrahieren(anteil, deckung)),
            nicht_aus_anteil_berichtigter_schuldteil=_bruchteile(_subtrahieren(schuld, deckung)))
    return _nachlassrest_ergebnis(wert, 'BGB_ERBTEIL_INDIVIDUELLE_SCHULDENDECKUNG', eingaben,
        'Individuelle Nachlassschuld bis eigenem Teilungsanteil decken; verbleibenden Anteil und nicht gedeckte Schuld getrennt ausweisen',
        'Nur einigen Miterben obliegende Nachlassverbindlichkeit2046II; hier bereits individuell zugeordneter Anteil der Schuld. Nicht von der gemeinsamen Masse2046I erneut abziehen. Teilungsanteil nach rechtlich zutreffender vorgelagerter Teilung/Ausgleichung bestimmen. Bei mehreren belasteten Erben zunächst deren rechtliche Lastanteile qualifizieren, keine automatische Gleichverteilung. Ungedeckte Schuld erlischt nicht und wird nicht pauschal auf unbelastete Erben umgelegt; sonstige Haftung gesondert.')


def vertragsvermaechtnis_subsidiaerer_fehlbetrag(geschuldeter_ersatzwert=None, vom_erben_erlangbarer_ersatz=None,
    subsidiaerfall_nach_2288_qualifiziert=None, bewertungsnachweis=None):
    """§2288II2: nicht beim Erben erlangbaren Ersatzanteil als subsidiäre Ausgangsgröße berechnen."""
    ersatz = _geld(geschuldeter_ersatzwert)
    erlangbar = _geld(vom_erben_erlangbarer_ersatz)
    if erlangbar > ersatz:
        _fehler('vom_erben_erlangbarer_ersatz', 'Erlangbarer Ersatzanteil darf gesamten geschuldeten Ersatzwert nicht übersteigen.')
    _wahrheitswert(subsidiaerfall_nach_2288_qualifiziert, 'subsidiaerfall_nach_2288_qualifiziert')
    _text(bewertungsnachweis, 'bewertungsnachweis')
    eingaben = dict(geschuldeter_ersatzwert=geschuldeter_ersatzwert, vom_erben_erlangbarer_ersatz=vom_erben_erlangbarer_ersatz,
        subsidiaerfall_nach_2288_qualifiziert=subsidiaerfall_nach_2288_qualifiziert, bewertungsnachweis=bewertungsnachweis)
    wert = _bruchteile(_subtrahieren(ersatz, erlangbar)) if subsidiaerfall_nach_2288_qualifiziert else None
    return _nachlassrest_ergebnis(wert, 'BGB_VERTRAGSVERMAECHTNIS_SUBSIDIAERER_FEHLBETRAG', eingaben,
        'Geschuldeten Ersatzwert um rechtlich vom Erben erlangbaren Ersatzanteil vermindern',
        'Nur beeinträchtigende schenkweise Veräußerung/Belastung eines vertragsmäßig vermachten Gegenstands2288II2; nicht jeder normale Erbvertrags- oder Pflichtteilsergänzungsfall. Erlangbarkeit rechtlich qualifizieren, nicht bloß bisher tatsächlich gezahlten Betrag abziehen. Ergebnis ist subsidiärer Fehlbetrag vor weiteren2287-Bereicherungsgrenzen, kein automatisch endgültiger Zahlungsanspruch gegen Beschenkten. Kein2329-Rangmodell importiert.')
