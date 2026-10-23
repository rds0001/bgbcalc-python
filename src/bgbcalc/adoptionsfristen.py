"""Gesetzliche Grundfristkombinationen der Adoption; keine Adoptionsentscheidung."""
from .kalender import _datum, _ergebnis, _fehler, _frist, _text


def adoption_ersetzungswartefrist(geburt_am=None, belehrung_oder_erste_handlung_am=None, fristbeginnnachweis=None):
    """§1748II: spätestes Ende aus drei Monaten Wartefrist und fünf Monaten ab Geburt."""
    geburt = _datum(geburt_am, 'geburt_am')
    beginn = _datum(belehrung_oder_erste_handlung_am, 'belehrung_oder_erste_handlung_am')
    _text(fristbeginnnachweis, 'fristbeginnnachweis')
    warteende = _frist(belehrung_oder_erste_handlung_am, 3, 'monate', 'ereignis')
    mindestende = _frist(geburt_am, 5, 'monate', 'ereignis')
    eingaben = dict(geburt_am=geburt_am, belehrung_oder_erste_handlung_am=belehrung_oder_erste_handlung_am, fristbeginnnachweis=fristbeginnnachweis)
    wert = dict(dreimonatsfristende=warteende.isoformat(), fuenfmonatsmindestende=mindestende.isoformat(), wartefristende=max(warteende,mindestende).isoformat())
    ergebnis = _ergebnis(wert,'daten','BGB_ADOPTION_ERSETZUNGSWARTEFRIST',eingaben,[dict(operation='Maximum der Dreimonatsfrist ab qualifiziertem Beginn und der Fünfmonatsgrenze ab Geburt bilden.')],eingaben.copy())
    ergebnis['hinweise'] = ['§1748II betrifft Gleichgültigkeit ohne zugleich anhaltende gröbliche Pflichtverletzung. Beginn ist wirksame Belehrung oder im gesetzlich qualifizierten Ausnahmefall erste Handlung des Jugendamts zur Belehrung/Beratung oder Aufenthaltsermittlung. Beratung, Nachforschungen und Ausnahmevoraussetzungen vorqualifiziert. Ergebnisse sind Ablaufdaten; Ersetzung frühestens nach Ablauf, keine automatische Ersetzungsbefugnis. Keine§193-Verlängerung der bloßen Wartezeit. Andere Ersetzungsgründe nachAbsätzen1/3/4 nicht auf diese Wartezeit reduzieren.']
    return ergebnis


def adoption_aufhebungsgrundfrist(annahme_am=None, relativer_fristbeginn_am=None, fristbeginnnachweis=None):
    """§1762II: Jahresgrundfrist mit dreijähriger Annahmegrenze kombinieren."""
    _datum(annahme_am, 'annahme_am')
    _datum(relativer_fristbeginn_am, 'relativer_fristbeginn_am')
    _text(fristbeginnnachweis, 'fristbeginnnachweis')
    relativ = _frist(relativer_fristbeginn_am, 1, 'jahre', 'ereignis')
    absolut = _frist(annahme_am, 3, 'jahre', 'ereignis')
    eingaben = dict(annahme_am=annahme_am, relativer_fristbeginn_am=relativer_fristbeginn_am, fristbeginnnachweis=fristbeginnnachweis)
    wert = dict(jahresgrundfristende=relativ.isoformat(), dreijahresgrundgrenze=absolut.isoformat(), antragsgrundfristende=min(relativ,absolut).isoformat())
    ergebnis = _ergebnis(wert,'daten','BGB_ADOPTION_AUFHEBUNGSGRUNDFRIST',eingaben,[dict(operation='Minimum der Jahresgrundfrist ab qualifiziertem relativen Beginn und Dreijahresgrundgrenze ab Annahme bilden.')],eingaben.copy())
    ergebnis['hinweise'] = ['Nur ungestörte Grundfristen nach§1762II. Relativen Beginn nach Buchstaben a bis e einschließlich etwaiger Vertreterkenntnis oder Ablaufs der§1747II1-Frist rechtlich vorqualifizieren; nicht allgemein Kenntnis der Annahme einsetzen. §§206/210 und eine einschlägige§193-Korrektur sind hier nicht berechnet, insbesondere keine Behauptung absolut unkorrigierbarer Dreijahresfrist. Liegt relativer Beginn erst nach Dreijahresgrenze, bleibt das errechnete Grundende früher; daraus folgt kein automatisches Erlöschensurteil. Antragsberechtigung, Vertretung, Beurkundung und Aufhebungsgrund gesondert.']
    return ergebnis
