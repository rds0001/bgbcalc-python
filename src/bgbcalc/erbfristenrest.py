"""Feste erbrechtliche Fristlängen und Mindestabläufe aus§§1965,1981,1998,2031,2034,2061."""
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _text


def erbrecht_weitere_grundfrist(fristart=None, fristbeginnereignis_am=None, einordnungsnachweis=None):
    """Drei Monate Nachweis, zwei Jahre Verwaltung, zwei Monate Vorkauf oder sechs Monate Anmeldung."""
    _auswahl(fristart, 'fristart', ('erbrechtsnachweis_1965', 'nachlassverwaltung_1981', 'erbteilvorkauf_2034', 'glaeubigeranmeldung_2061'))
    beginn = _datum(fristbeginnereignis_am, 'fristbeginnereignis_am')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    anzahl, einheit = {'erbrechtsnachweis_1965': (3, 'monate'), 'nachlassverwaltung_1981': (2, 'jahre'),
        'erbteilvorkauf_2034': (2, 'monate'), 'glaeubigeranmeldung_2061': (6, 'monate')}[fristart]
    ende = _frist(beginn.isoformat(), anzahl, einheit, 'ereignis')
    eingaben = dict(fristart=fristart, fristbeginnereignis_am=fristbeginnereignis_am, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(dict(grundfristende=ende.isoformat(), anzahl=anzahl, einheit=einheit), 'datum_und_fristlaenge',
        'BGB_ERBRECHT_WEITERE_GRUNDFRIST', eingaben,
        [dict(operation='Gesetzliche Fristlänge auswählen und Ereignisfrist mit vorhandenem Kalenderkern berechnen')], eingaben.copy())
    ergebnis['annahmen'] = ['Feste lokale BGB-Fassung; ausschließlich rohe gesetzliche Grundfrist ab rechtlich qualifiziertem Ereignis.']
    ergebnis['hinweise'] = ['§1965 Absatz2: Beginn nach Ablauf der öffentlichen Anmeldungsfrist, ohne öffentliche Aufforderung gerichtliche Aufforderung zum Nachweis des Erbrechts oder Klage. §1981 Absatz2: Annahme der Erbschaft, betrifft Antrag eines Nachlassgläubigers. §2034 Absatz2: Empfang der rechtlich ausreichenden Mitteilung des Vertragsinhalts nach§469, nicht pauschal Kaufvertrag oder Anteilsübertragung. §2061 Absatz2: letzte erforderliche Veröffentlichung, nicht die erste. Keine automatische Zulässigkeits-/Erklärungsprüfung, Hemmung oder Wochenend-/Feiertagsverschiebung; Grundfristende nicht ungeprüft als endgültigen letzten Handlungstag verwenden. §2061-Haftungsquote ist gesonderte Betragsregel.']
    return ergebnis


def inventarfrist_erbentod_mindestende(bisheriges_fristende=None, erbe_gestorben_am=None,
    ausschlagungsfristende_erbeserbe=None, einordnungsnachweis=None):
    """§1998: frühestens Ende der Ausschlagungsfrist für den verstorbenen Erben, wenn Tod vor Ablauf."""
    bisher = _datum(bisheriges_fristende, 'bisheriges_fristende')
    tod = _datum(erbe_gestorben_am, 'erbe_gestorben_am')
    ausschlagung = _datum(ausschlagungsfristende_erbeserbe, 'ausschlagungsfristende_erbeserbe')
    if ausschlagung < tod:
        _fehler('ausschlagungsfristende_erbeserbe', 'Ausschlagungsfrist für Erbschaft des verstorbenen Erben darf nicht vor dessen Tod enden.')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    ende = max(bisher, ausschlagung) if tod <= bisher else bisher
    eingaben = dict(bisheriges_fristende=bisheriges_fristende, erbe_gestorben_am=erbe_gestorben_am,
        ausschlagungsfristende_erbeserbe=ausschlagungsfristende_erbeserbe, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(dict(massgebliches_fristende=ende.isoformat()), 'datum', 'BGB_INVENTARFRIST_ERBENTOD_MINDESTENDE',
        eingaben, [dict(operation='Tod vor Tagesablauf prüfen; Frist auf späteres bisheriges oder einschlägiges Ausschlagungsende setzen')], eingaben.copy())
    ergebnis['annahmen'] = ['Feste lokale BGB-Fassung; Ereignis am letzten Fristtag liegt vor dessen Ablauf.']
    ergebnis['hinweise'] = ['Nur§1998 für Inventarfrist oder Zweiwochenfrist§1996 Absatz2; nicht absolute Jahresgrenze verlängern. Eingaben sind bereits rechtlich maßgebliche Fristenden einschließlich jeweils einschlägiger Korrekturen. Tod nach Ablauf belebt Frist nicht wieder. Keine Addition oder neue volle Inventarfrist ab Tod. Für mehrere Erbeserben deren jeweilige Ausschlagungsfrist und Rechtsstellung gesondert bestimmen; keine automatische gemeinsame Maximalfrist aller Personen.']
    return ergebnis


def totgeglaubter_verjaehrung_mindestende(bisheriges_verjaehrungsende=None,
    kenntnis_todesannahme_am=None, einordnungsnachweis=None):
    """§2031: solange Betroffener lebt, mindestens ein Jahr nach Kenntnis der falschen Todesannahme."""
    bisher = _datum(bisheriges_verjaehrungsende, 'bisheriges_verjaehrungsende')
    kenntnis = _datum(kenntnis_todesannahme_am, 'kenntnis_todesannahme_am')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    minimum = _frist(kenntnis.isoformat(), 1, 'jahre', 'ereignis')
    ende = max(bisher, minimum)
    eingaben = dict(bisheriges_verjaehrungsende=bisheriges_verjaehrungsende,
        kenntnis_todesannahme_am=kenntnis_todesannahme_am, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(dict(einjaehriges_mindestende=minimum.isoformat(), massgebliches_verjaehrungsende=ende.isoformat()),
        'daten', 'BGB_TOTGEGLAUBTER_VERJAEHRUNG_MINDESTENDE', eingaben,
        [dict(operation='Einjähriges Kenntnismindestende berechnen und Maximum mit bisherigem Verjährungsende bilden')], eingaben.copy())
    ergebnis['annahmen'] = ['Feste lokale BGB-Fassung;§2031-Anwendungsfall rechtlich bestimmt, betroffene Person lebt für den betrachteten Zeitraum fort.']
    ergebnis['hinweise'] = ['Qualifizierter Anspruch der tatsächlich lebenden, fälschlich für tot erklärten oder als tot angenommenen Person; keine beliebige Erbenkenntnis. Mindestgrenze gilt nur solange diese Person lebt; Tod während des betrachteten Zeitraums ist außerhalb dieses Modells. Vorhandenes Verjährungsende rechtlich bestimmt, nicht beliebiges Anspruchsdatum. Keine neue einjährige Verjährungsfrist anstelle einer längeren Frist, kein pauschaler Jahresendbeginn. Weitere Hemmungen/Kalenderkorrekturen und Einredeausübung separat.']
    return ergebnis
