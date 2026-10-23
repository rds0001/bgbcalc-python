"""Numerische Anwachsung gemeinschaftlicher Vermächtnisanteile (§§2158/2159/2190)."""
from .anwachsung import erbteil_anwachsungsquoten
from .kalender import _ergebnis, _fehler, _vorhanden


def vermaechtnis_anwachsungsanteile(bedachte=None, weggefallener_bedachter_id=None,
    anwachsung_testamentarisch_ausgeschlossen=None, vorrangiges_ersatzvermaechtnis=None, einordnungsnachweis=None):
    """Einzelwegfall auf übrige Bedachte desselben Gegenstands mit Gruppenvorrang verteilen."""
    _vorhanden(bedachte, 'bedachte')
    if not isinstance(bedachte, list) or not 2 <= len(bedachte) <= 1000:
        _fehler('bedachte', 'Liste2..1000 Bedachter desselben Gegenstands erforderlich.')
    einsetzungen = []
    for p in bedachte:
        if not isinstance(p, dict) or set(p) != {'bedachter_id', 'vermaechtnisanteil', 'gemeinschaft_id'}:
            _fehler('bedachte', 'Genau bedachter_id, vermaechtnisanteil und gemeinschaft_id erforderlich.')
        einsetzungen.append(dict(erbe_id=p['bedachter_id'], erbquote=p['vermaechtnisanteil'], gemeinschaft_id=p['gemeinschaft_id']))
    teilung = erbteil_anwachsungsquoten(einsetzungen, weggefallener_bedachter_id, True,
        anwachsung_testamentarisch_ausgeschlossen, vorrangiges_ersatzvermaechtnis, einordnungsnachweis)['wert']
    wert = dict(anwachsung_erfolgt=teilung['anwachsung_erfolgt'], vermaechtnisanteile=[
        dict(bedachter_id=p['erbe_id'], urspruenglicher_vermaechtnisanteil=p['urspruenglicher_erbteil'],
            angewachsener_vermaechtnisanteil=p['angewachsener_erbteil'], gesamter_vermaechtnisanteil=p['gesamter_erbteil'])
        for p in teilung['erbteile']], nicht_angewachsener_wegfallender_anteil=teilung['nicht_angewachsener_wegfallender_erbteil'])
    eingaben = dict(bedachte=bedachte, weggefallener_bedachter_id=weggefallener_bedachter_id,
        anwachsung_testamentarisch_ausgeschlossen=anwachsung_testamentarisch_ausgeschlossen,
        vorrangiges_ersatzvermaechtnis=vorrangiges_ersatzvermaechtnis, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert, 'vermaechtnisquoten', 'BGB_VERMAECHTNIS_ANWACHSUNGSANTEILE', eingaben,
        [dict(operation='Vorhandenen proportionalen Einzelwegfallkern mit Gruppenvorrang für vollständige Vermächtnisanteile anwenden; angewachsenen Anteil getrennt erhalten')], eingaben.copy())
    ergebnis['annahmen'] = ['Ein rechtlich qualifizierter Wegfall vor oder nach Erbfall; Bedachte desselben Gegenstands mit positiven vollständigen Originalanteilen und einfacher Gemeinschaftszuordnung.']
    ergebnis['hinweise'] = ['Quotensumme eins bezieht sich ausschließlich auf den vermachten Gegenstand, nicht gesamte Erbschaft. Keine Voraussetzung ausgeschlossener gesetzlicher Erbfolge: der interne Wiederverwendungsschalter des Teilungskerns stellt lediglich allgemeine Anwachsung unter verbleibenden Bedachten sicher. Vorrangig verbleibende Mitglieder derselben gemeinschaftlichen Teilquote; sonst alle übrigen. Testamentarischer Ausschluss2158II oder rechtlich vorrangiges Ersatzvermächtnis2190/2099 sperren diese Anwachsung. Angewachsener Teil bleibt nach2159 hinsichtlich Beschwerungen besonderes Vermächtnis. Mehrere Wegfälle, verschachtelte Gruppen, bereits angewachsene Sonderanteile oder individuelle Teilausschlüsse separat; keinen bloßen Tod nach Erwerb automatisch als Wegfall einordnen. Nicht angewachsenen Anteil keinem anderen Bedachten oder Erben automatisch zuordnen.']
    return ergebnis
