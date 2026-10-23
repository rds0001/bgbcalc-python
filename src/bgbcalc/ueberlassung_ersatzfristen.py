"""Sechsmonatige Ersatz-/Verwendungsfristen bei Gebrauchsüberlassung und Pfand."""
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _text
_FAELLE = {'miete_vermieter': (True, '§548 Absatz1: tatsächlicher rechtlich maßgeblicher Rückerhalt der Mietsache; Ersatz wegen Veränderung/Verschlechterung.'), 'miete_mieter': (False, '§548 Absatz2: Beendigung des Mietverhältnisses; Verwendungsersatz/Wegnahmegestattung.'), 'landpacht_verpaechter': (True, '§591b: rechtlich maßgeblicher Rückerhalt der Pachtsache; Ersatz wegen Veränderung/Verschlechterung.'), 'landpacht_paechter': (False, '§591b: Beendigung des Landpachtverhältnisses; Verwendungsersatz/Wegnahmegestattung.'), 'leihe_verleiher': (True, '§606 mit§548: rechtlich maßgeblicher Rückerhalt der Leihsache; Ersatz wegen Veränderung/Verschlechterung.'), 'leihe_entleiher': (False, '§606 mit§548: Beendigung der Leihe; Verwendungsersatz/Wegnahmegestattung.'), 'niessbrauch_eigentuemer': (True, '§1057 mit§548: rechtlich maßgeblicher Rückerhalt der Sache; Eigentümerersatz wegen Veränderung/Verschlechterung.'), 'niessbrauch_berechtigter': (False, '§1057 mit§548: rechtlich maßgebliche Beendigung des Nießbrauchs; Verwendungsersatz/Wegnahmegestattung.'), 'pfand_verpfaender': (True, '§1226 mit§548: rechtlich maßgeblicher Rückerhalt des Pfandes; Verpfänderersatz wegen Veränderung/Verschlechterung.'), 'pfand_pfandglaeubiger': (False, '§1226 mit§548: rechtlich maßgebliche Beendigung des Pfandrechtsverhältnisses; Verwendungsersatz/Wegnahmegestattung.')}

def ueberlassung_ersatzverjaehrungsgrundfrist(anspruchsfall=None, ereignis_am=None, rueckgabeanspruch_fristende=None, einordnungsnachweis=None):
    """Berechnet sechsmonatige Grundfrist und gegebenenfalls ausdrückliche Rückgabeanspruchsgrenze."""
    _auswahl(anspruchsfall, 'anspruchsfall', tuple(_FAELLE))
    _datum(ereignis_am, 'ereignis_am')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    gekoppelt, fallhinweis = _FAELLE[anspruchsfall]
    rueckgabegrenze = None
    if rueckgabeanspruch_fristende is not None:
        rueckgabegrenze = _datum(rueckgabeanspruch_fristende, 'rueckgabeanspruch_fristende')
        if not gekoppelt:
            _fehler('rueckgabeanspruch_fristende', 'Rückgabeanspruchsgrenze ist nur bei Überlasser-/Eigentümerersatzansprüchen zulässig.')
    grundende = _frist(ereignis_am, 6, 'monate', 'ereignis')
    kopplungsende = min(grundende, rueckgabegrenze).isoformat() if rueckgabegrenze is not None else None
    eingaben = dict(anspruchsfall=anspruchsfall, ereignis_am=ereignis_am, rueckgabeanspruch_fristende=rueckgabeanspruch_fristende, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(dict(sechsmonatiges_grundfristende=grundende.isoformat(), rueckgabeanspruchskopplung_erforderlich=gekoppelt, mit_rueckgabeanspruch_begrenztes_grundfristende=kopplungsende), 'daten_und_wahrheitswert', 'BGB_UEBERLASSUNG_ERSATZVERJAEHRUNGSGRUNDFRIST', eingaben, [dict(operation='Sechs Monate ab qualifiziertem Rückerhalt oder Verhältnisende; auf Überlasserseite zusätzlich frühere vorgegebene Rückgabeanspruchsgrenze berücksichtigen')], eingaben.copy())
    ergebnis['annahmen'] = ['Anspruchsart, Rückerhalt oder rechtliches Verhältnisende und gegebenenfalls Rückgabeanspruchsablauf ausdrücklich qualifiziert; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['Grundfrist vor eigener Hemmung/Ablaufhemmung/Neubeginn/Feiertagskorrektur. Auf Überlasser-/Eigentümerseite verjähren Ersatzansprüche spätestens mit dem Rückgabeanspruch: Ohne dessen gesondert bestimmten Fristablauf bleibt die gekoppelte Grenze ausdrücklich unbekannt (null). Eine vorgegebene Grenze ist ein qualifiziertes Datum, keine hier berechnete Verjährung des Rückgabeanspruchs. Keine automatische sechsmonatige Verjährung des Rückgabeanspruchs selbst. Bei Nutzeransprüchen keine solche Kopplung.', fallhinweis]
    return ergebnis
