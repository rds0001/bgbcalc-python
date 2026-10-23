"""Fünfjahresgrenze der Verschweigungseinrede (§1974 Absatz1/3)."""
from .betraege import _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler, _frist, _text


def nachlass_spaetglaeubiger(erbfall_am=None, geltendmachung_am=None,
    todeserklaerung_oder_todeszeitfeststellung=None, rechtskraft_am=None,
    erbenkenntnis_am=None, qualifizierte_anmeldung_im_aufgebot=None,
    glaeubiger_nach_1971_ausgenommen=None, einordnungsnachweis=None):
    """Fünf Jahre ab Erbfall, frühestens Rechtskraft, mit Kenntnis-/Anmeldungsausnahmen."""
    erbfall = _datum(erbfall_am, 'erbfall_am')
    geltendmachung = _datum(geltendmachung_am, 'geltendmachung_am')
    if geltendmachung < erbfall:
        _fehler('geltendmachung_am', 'Geltendmachung als Nachlassforderung darf nicht vor Erbfall liegen.')
    _wahrheitswert(todeserklaerung_oder_todeszeitfeststellung, 'todeserklaerung_oder_todeszeitfeststellung')
    rechtskraft = _datum(rechtskraft_am, 'rechtskraft_am') if rechtskraft_am is not None else None
    if todeserklaerung_oder_todeszeitfeststellung and rechtskraft is None:
        _fehler('rechtskraft_am', 'Rechtskraftdatum des qualifizierten Beschlusses erforderlich.', 'EINGABE_FEHLT')
    if not todeserklaerung_oder_todeszeitfeststellung and rechtskraft is not None:
        _fehler('rechtskraft_am', 'Ohne qualifizierten Beschluss kein Rechtskraftdatum angeben.')
    beginn = max(erbfall, rechtskraft) if rechtskraft is not None else erbfall
    ende = _frist(beginn.isoformat(), 5, 'jahre', 'ereignis')
    kenntnis = _datum(erbenkenntnis_am, 'erbenkenntnis_am') if erbenkenntnis_am is not None else None
    if kenntnis is not None and kenntnis > geltendmachung:
        _fehler('erbenkenntnis_am', 'Kenntnisdatum darf nicht nach dem betrachteten Geltendmachungsdatum liegen.')
    _wahrheitswert(qualifizierte_anmeldung_im_aufgebot, 'qualifizierte_anmeldung_im_aufgebot')
    _wahrheitswert(glaeubiger_nach_1971_ausgenommen, 'glaeubiger_nach_1971_ausgenommen')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    eingaben = dict(erbfall_am=erbfall_am, geltendmachung_am=geltendmachung_am,
        todeserklaerung_oder_todeszeitfeststellung=todeserklaerung_oder_todeszeitfeststellung,
        rechtskraft_am=rechtskraft_am, erbenkenntnis_am=erbenkenntnis_am,
        qualifizierte_anmeldung_im_aufgebot=qualifizierte_anmeldung_im_aufgebot,
        glaeubiger_nach_1971_ausgenommen=glaeubiger_nach_1971_ausgenommen,
        einordnungsnachweis=einordnungsnachweis)
    rechtzeitig_bekannt = kenntnis is not None and kenntnis <= ende
    spaet = geltendmachung > ende
    wert = dict(fristbeginnereignis_am=beginn.isoformat(), fuenfjahresfristende=ende.isoformat(),
        geltendmachung_nach_fuenf_jahren=spaet, forderung_rechtzeitig_bekannt=rechtzeitig_bekannt,
        ausgeschlossenem_glaeubiger_gleichgestellt=spaet and not rechtzeitig_bekannt and not qualifizierte_anmeldung_im_aufgebot)
    ergebnis = _ergebnis(wert, 'daten_und_wahrheitswerte', 'BGB_NACHLASS_SPAETGLAEUBIGER', eingaben,
        [dict(operation='Fünf Jahre ab spätestem Start; strikt spätere Geltendmachung, rechtzeitige Erbenkenntnis und qualifizierte Anmeldung prüfen')], eingaben.copy())
    if glaeubiger_nach_1971_ausgenommen:
        ergebnis['wert'] = None
        ergebnis['status'] = 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Taggenaue Prüfung; Kenntnis am letzten Fristtag liegt vor dessen Ablauf. Feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['Nur Gleichstellung nach§1974 Absatz1, kein Erlöschen oder Verjähren der Forderung und keine automatische Einredeausübung. Absatz2-Rangfolgen und Rechtsfolgen§1973 getrennt prüfen. Erbenkenntnis NULL bedeutet bis Geltendmachung nicht bekannt, nicht ungeklärte Kenntnis. Anmeldung muss als die Ausnahme des§1974 Absatz1 tragende Anmeldung rechtlich einschließlich zeitlicher Anforderungen qualifiziert sein; kein beliebiger Schriftsatz. §1971-Ausnahme nur soweit der gesicherte Gegenstand betroffen ist, keine globale Befreiung ungesicherter Restforderungen. Rechtskraftdatum betrifft ausschließlich Todeserklärung/Todeszeitfeststellung nach Verschollenheitsgesetz; keine andere Nachlassentscheidung. Keine automatische Hemmung oder Wochenend-/Feiertagsverschiebung.']
    return ergebnis
