"""Kauf-, Wiederkauf- und Vorkauf-Sonderbeträge mit qualifizierten Werten."""
from .betraege import _geld, _geld_ergebnis
from .kalender import _text, _fehler
from .zahlen import _addieren, _subtrahieren, _multiplizieren, _dividieren, _bruch


def miete_zeitanteiliger_minderungsbetrag(miete_des_abrechnungsabschnitts=None, qualifizierte_gesamtminderungsquote=None, beruecksichtigungsfaehiger_mangelzeitanteil=None, einordnungsnachweis=None):
    """Miete des homogenen Abrechnungsabschnitts mit qualifizierter Gesamtminderungsquote und berücksichtigungsfähigem Mangelzeitanteil multiplizieren."""
    werte = [_geld(miete_des_abrechnungsabschnitts), _geld(qualifizierte_gesamtminderungsquote), _geld(beruecksichtigungsfaehiger_mangelzeitanteil)]
    _text(einordnungsnachweis, 'einordnungsnachweis')
    if any(q > 1 for q in werte[1:]):
        _fehler('anteile', 'Minderungs- und Zeitanteile dürfen eins nicht übersteigen.')
    eingaben = dict(miete_des_abrechnungsabschnitts=miete_des_abrechnungsabschnitts, qualifizierte_gesamtminderungsquote=qualifizierte_gesamtminderungsquote, beruecksichtigungsfaehiger_mangelzeitanteil=beruecksichtigungsfaehiger_mangelzeitanteil, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(_multiplizieren(_multiplizieren(werte[0],werte[1]),werte[2]), 'BGB_MIETE_ZEITANTEILIGER_MINDERUNGSBETRAG', eingaben, [dict(operation='Miete des homogenen Abrechnungsabschnitts mit qualifizierter Gesamtminderungsquote und berücksichtigungsfähigem Mangelzeitanteil multiplizieren')])
    ergebnis['hinweise'].append('Nur §536 bei rechtlich qualifizierter Mietminderung und homogener Mietpreis-/Minderungsbasis. Quote0..1 extern bestimmen; vollständige Gebrauchsunmöglichkeit gegebenenfalls1. Gleichzeitige Mängel zuerst zu rechtlich angemessener Gesamtquote zusammenführen, nicht einzelne Quoten blind addieren. Zeitanteil0..1 ohne unerhebliche/ausgeschlossene Beeinträchtigungen, insbesondere §536 Absatz1a und sonstige Ausschlüsse. Bei wechselnden Quoten/Mieten disjunkte Abschnitte getrennt berechnen. Keine Minderungstabelle, kein Marktwertverhältnis aus Kaufminderung, keine automatische Monatslänge oder Dreimonatsausnahmeberechnung.')
    return ergebnis


def mietvorauszahlung_zeitanteilige_rueckerstattung(vorausgezahlte_abschnittsmiete=None, nach_beendigung_liegender_zeitanteil=None, einordnungsnachweis=None):
    """Vorausgezahlte Miete eines homogen bepreisten Abschnitts mit dem nach Vertragsende liegenden Zeitanteil multiplizieren."""
    werte = [_geld(vorausgezahlte_abschnittsmiete), _geld(nach_beendigung_liegender_zeitanteil)]
    _text(einordnungsnachweis, 'einordnungsnachweis')
    if any(q > 1 for q in werte[1:]):
        _fehler('anteile', 'Minderungs- und Zeitanteile dürfen eins nicht übersteigen.')
    eingaben = dict(vorausgezahlte_abschnittsmiete=vorausgezahlte_abschnittsmiete, nach_beendigung_liegender_zeitanteil=nach_beendigung_liegender_zeitanteil, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(_multiplizieren(werte[0],werte[1]), 'BGB_MIETVORAUSZAHLUNG_ZEITANTEILIGE_RUECKERSTATTUNG', eingaben, [dict(operation='Vorausgezahlte Miete eines homogen bepreisten Abschnitts mit dem nach Vertragsende liegenden Zeitanteil multiplizieren')])
    ergebnis['hinweise'].append('Nur §547 Absatz1 Satz1 bei qualifiziert vom Vermieter zu vertretender Beendigung und einem gleichmäßig bepreisten Vorauszahlungsabschnitt. Zahlung muss gerade diesen Abschnitt betreffen; Zeitanteil0..1 rechtlich bestimmen. Unterschiedliche Preise/Zahlungszuordnungen abschnittsweise rechnen. Bei nicht zu vertretender Beendigung Bereicherungsrecht nach Satz2 gesondert, kein automatischer identischer Rückbetrag. Gesetzliche Zinsen ab jeweiligem Empfang mit vorhandenem Zinskern separat berechnen; keine automatische pauschale Verzinsung vor Eingang.')
    return ergebnis
