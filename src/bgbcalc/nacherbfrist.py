"""Dreißigjahresgrenze der Nacherbeneinsetzung (§2109)."""
from .betraege import _wahrheitswert
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _text


def nacherbeneinsetzung_dreissigjahresgrenze(erbfall_am=None, prueftag=None,
    nacherbfall_am=None, fortgeltungsgrund=None, ereignistraeger_bei_erbfall_vorhanden=None,
    ereignistraeger_juristische_person=None, einordnungsnachweis=None):
    """Ablauf der Dreißigjahresgrenze mit rechtzeitigem Nacherbfall und gesetzlichen Ausnahmen."""
    erbfall = _datum(erbfall_am, 'erbfall_am')
    tag = _datum(prueftag, 'prueftag')
    if tag < erbfall:
        _fehler('prueftag', 'Prüftag darf nicht vor Erbfall liegen.')
    ende = _frist(erbfall_am, 30, 'jahre', 'ereignis')
    nacherbfall = _datum(nacherbfall_am, 'nacherbfall_am') if nacherbfall_am is not None else None
    if nacherbfall is not None and not erbfall <= nacherbfall <= tag:
        _fehler('nacherbfall_am', 'Nacherbfallereignis muss zwischen Erbfall und Prüftag liegen.')
    _auswahl(fortgeltungsgrund, 'fortgeltungsgrund', ('keiner', 'personenereignis', 'geschwistergeburt'))
    _wahrheitswert(ereignistraeger_bei_erbfall_vorhanden, 'ereignistraeger_bei_erbfall_vorhanden')
    _wahrheitswert(ereignistraeger_juristische_person, 'ereignistraeger_juristische_person')
    if fortgeltungsgrund == 'geschwistergeburt' and ereignistraeger_juristische_person:
        _fehler('ereignistraeger_juristische_person', 'Qualifizierte Geschwistergeburt setzt eine natürliche Bezugsperson voraus.')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    ausnahme = fortgeltungsgrund == 'geschwistergeburt' or (fortgeltungsgrund == 'personenereignis' and
        ereignistraeger_bei_erbfall_vorhanden and not ereignistraeger_juristische_person)
    rechtzeitig = nacherbfall is not None and nacherbfall <= ende
    wert = dict(dreissigjahresfristende=ende.isoformat(), nacherbfall_bis_fristablauf=rechtzeitig,
        fortgeltungsausnahme=ausnahme, unwirksam_wegen_dreissigjahresgrenze=tag >= ende and not rechtzeitig and not ausnahme)
    eingaben = dict(erbfall_am=erbfall_am, prueftag=prueftag, nacherbfall_am=nacherbfall_am,
        fortgeltungsgrund=fortgeltungsgrund, ereignistraeger_bei_erbfall_vorhanden=ereignistraeger_bei_erbfall_vorhanden,
        ereignistraeger_juristische_person=ereignistraeger_juristische_person, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert, 'daten_und_wahrheitswerte', 'BGB_NACHERBENEINSETZUNG_DREISSIGJAHRESGRENZE', eingaben,
        [dict(operation='Dreißig Jahre ab Erbfall; rechtzeitiges Nacherbfallereignis und gesetzliche Fortgeltungsausnahme prüfen')], eingaben.copy())
    ergebnis['annahmen'] = ['Prüfung nach vollständigem Ablauf des Prüftags; Ereignis im Laufe des letzten Fristtags liegt vor dessen Ablauf. Feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['FALSE bei Unwirksamkeit betrifft nur die Dreißigjahresgrenze, nicht die gesamte Wirksamkeit oder den tatsächlichen Erwerb. Maßgebliches Nacherbfallereignis rechtlich aus Verfügung und gegebenenfalls§2106 bestimmen; NULL bedeutet bis Prüftag nicht eingetreten, nicht unbekannt. Spätes Ereignis heilt keine bereits nach§2109 unwirksame Einsetzung. personenereignis verlangt gerade ein angeordnetes Ereignis in der Person des Vor- oder Nacherben; eine bei Erbfall lebende andere Person genügt nicht. Bei juristischem Ereignisträger verbleibt es trotz bereits bestehender Rechtspersönlichkeit bei dreißig Jahren. geschwistergeburt verlangt exakt die Bruder-/Schwester-Nacherbeinsetzung nach§2109 Absatz1 Nummer2; keine zusätzliche Voraussetzung, dass die Bezugsperson bei Erbfall schon lebte. Ereignisträger ist diese natürliche Bezugsperson, nicht irgendein anderer Beteiligter. Keine automatische Testamentsauslegung, Berechnung von Ersatznacherbfolge oder Wochenend-/Feiertagsverschiebung.']
    return ergebnis
