from .kalender import _datum, _ergebnis, _fehler, _text
from .betraege import _wahrheitswert

def schuldverschreibung_zahlungssperre_intervall(antrag_zahlungssperre_am=None, zahlungssperre_vor_verfahrenseinleitung=None, sechsmonatsfrist_letzter_tag=None, einleitungsantrag_am=None, verfahren_erledigt_am=None, beobachtung_bis=None, einordnungsnachweis=None):
    """Tatsächliche Erledigung und gegebenenfalls unwahrte Sechsmonatsfrist vergleichen; frühestes bekanntes Hemmungsende oder ausdrücklich begrenztes Beobachtungsintervall bilden."""
    a=_datum(antrag_zahlungssperre_am,'antrag_zahlungssperre_am');b=_datum(beobachtung_bis,'beobachtung_bis');vor=_wahrheitswert(zahlungssperre_vor_verfahrenseinleitung,'zahlungssperre_vor_verfahrenseinleitung');_text(einordnungsnachweis,'einordnungsnachweis')
    if b<a:_fehler('beobachtung_bis','Beobachtung nicht vor Beginn.')
    if not vor and sechsmonatsfrist_letzter_tag is not None:_fehler('sechsmonatsfrist_letzter_tag','Ohne Vorverfahren keine unberücksichtigte Fristangabe.')
    frist=_datum(sechsmonatsfrist_letzter_tag,'sechsmonatsfrist_letzter_tag') if vor else None
    if frist is not None and frist<a:_fehler('sechsmonatsfrist_letzter_tag','Für diesen qualifizierten Ablauf Fristende nicht vor Hemmungsbeginn.')
    einleitung=None if einleitungsantrag_am is None else _datum(einleitungsantrag_am,'einleitungsantrag_am');erledigung=None if verfahren_erledigt_am is None else _datum(verfahren_erledigt_am,'verfahren_erledigt_am')
    if einleitung is not None and einleitung>b:_fehler('einleitungsantrag_am','Tatsächliches Ereignis nicht nach Beobachtung.')
    if erledigung is not None and not a<=erledigung<=b:_fehler('verfahren_erledigt_am','Erledigung zwischen Hemmungsbeginn und Beobachtung erforderlich.')
    enden=[] if erledigung is None else [erledigung]
    if vor and frist<=b and (einleitung is None or einleitung>frist):enden.append(frist)
    ende=min(enden) if enden else None
    wert=dict(feststehendes_hemmungsende=None if ende is None else ende.isoformat(),hemmung_bis_beobachtung_abgeschlossen=ende is not None,hemmungszeitraeume=[dict(erster_gehemmter_tag=a.isoformat(),letzter_gehemmter_tag=(ende or b).isoformat())])
    eingaben = dict(antrag_zahlungssperre_am=antrag_zahlungssperre_am, zahlungssperre_vor_verfahrenseinleitung=zahlungssperre_vor_verfahrenseinleitung, sechsmonatsfrist_letzter_tag=sechsmonatsfrist_letzter_tag, einleitungsantrag_am=einleitungsantrag_am, verfahren_erledigt_am=verfahren_erledigt_am, beobachtung_bis=beobachtung_bis, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'daten_und_intervalle','BGB_SCHULDVERSCHREIBUNG_ZAHLUNGSSPERRE_INTERVALL',eingaben,[dict(operation='Tatsächliche Erledigung und gegebenenfalls unwahrte Sechsmonatsfrist vergleichen; frühestes bekanntes Hemmungsende oder ausdrücklich begrenztes Beobachtungsintervall bilden.')],eingaben.copy())
    ergebnis["hinweise"] = ['802: Beginn mit Zahlungssperrenantrag. Ende mit tatsächlicher Verfahrenserledigung; im qualifizierten Vorverfahren zusätzlich Ablauf der korrigierten Sechsmonatsfrist, sofern bis dahin kein wirksamer Einleitungsantrag gestellt war. Früheres Endereignis maßgeblich. Einleitungsantrag am letzten Fristtag wahrt; späterer Antrag belebt bereits beendete Hemmung nicht rückwirkend wieder. Bei laufender Hemmung nur bis Beobachtung rechnen und Abschluss ausdrücklich verneinen. Keine künstliche Verfahrenserledigung. Hemmung beeinflusst auch Beginn der Vorlegungsfrist; entsprechende Weiterrechnung mit209unter rechtlicher Qualifikation und ohne doppelte Tage. Sechsmonatsgrundfrist/206/210/211werden vorgelagert mit vorhandenen Kernen berechnet. Datumstage sind rechtlich normalisierte eingeschlossene Hemmungstage; untertägige Sonderfälle nicht pauschal runden.']
    return ergebnis

