"""Verknüpfte Grundfristen für Lieferantenregress und deliktische Restbereicherung."""
from .kalender import _datum, _ergebnis, _fehler, _frist, _text


def lieferantenregress_verjaehrungsgrundfrist(ablieferung_am=None, kaeuferanspruch_erfuellt_am=None, einordnungsnachweis=None):
    """Späteres Ende aus Ablieferung plus zwei Jahre und Erfüllung des Käuferanspruchs plus zwei Monate."""
    erster = _datum(ablieferung_am, 'ablieferung_am')
    zweiter = _datum(kaeuferanspruch_erfuellt_am, 'kaeuferanspruch_erfuellt_am')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    ende1 = _frist(ablieferung_am, 2, 'jahre', 'ereignis')
    ende2 = _frist(kaeuferanspruch_erfuellt_am, 2, 'monate', 'ereignis')
    ende = max(ende1, ende2)
    eingaben = dict(ablieferung_am=ablieferung_am, kaeuferanspruch_erfuellt_am=kaeuferanspruch_erfuellt_am, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(dict(zweijahres_grundfristende=ende1.isoformat(), zweimonats_mindestende=ende2.isoformat(), verknuepftes_grundfristende=ende.isoformat()), 'daten', 'BGB_LIEFERANTENREGRESS_VERJAEHRUNGSGRUNDFRIST', eingaben, [dict(operation='Späteres Ende aus Ablieferung plus zwei Jahre und Erfüllung des Käuferanspruchs plus zwei Monate')], eingaben.copy())
    ergebnis['annahmen'] = ['Qualifizierter gesetzlicher Anwendungsfall und rechtlich bestimmte Ereignistage; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['Nur verknüpfte gesetzliche Grundfristen; keine automatische Hemmung, Ablaufhemmung, Neubeginn oder Feiertagskorrektur. Ende bezeichnet letzten eingeschlossenen Tag bis Tagesablauf. Keine abschließende Feststellung eingetretener Verjährung.', 'Nur§445b Absatz1/2 für qualifizierten Lieferantenregress beim Mangel einer neu hergestellten Sache. Keine historische Fünfjahreskappung. Käuferanspruchserfüllung muss rechtlich bestimmt sein; mehrere Ansprüche/Teilbefriedigungen separat qualifizieren. Nicht digitale Vertriebskette327u. Verjährung anderer437-Ansprüche kann andereGrundfrist haben: hier ausdrücklich zweijährige445a-Aufwendungsersatzgrundfrist.']
    return ergebnis


def delikt_restbereicherung_verjaehrungsgrundfrist(anspruch_entstanden_am=None, verletzungsereignis_am=None, einordnungsnachweis=None):
    """Früheres Ende aus Entstehung des Restbereicherungsanspruchs plus zehn Jahre und Verletzungshandlung/sonstigem auslösendem Ereignis plus dreißig Jahre."""
    erster = _datum(anspruch_entstanden_am, 'anspruch_entstanden_am')
    zweiter = _datum(verletzungsereignis_am, 'verletzungsereignis_am')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    if erster < zweiter:
        _fehler('anspruch_entstanden_am', 'Anspruchsentstehung darf nicht vor dem auslösenden Verletzungsereignis liegen.')
    ende1 = _frist(anspruch_entstanden_am, 10, 'jahre', 'ereignis')
    ende2 = _frist(verletzungsereignis_am, 30, 'jahre', 'ereignis')
    ende = min(ende1, ende2)
    eingaben = dict(anspruch_entstanden_am=anspruch_entstanden_am, verletzungsereignis_am=verletzungsereignis_am, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(dict(zehnjahres_grundfristende=ende1.isoformat(), dreissigjahres_grundfristende=ende2.isoformat(), verknuepftes_grundfristende=ende.isoformat()), 'daten', 'BGB_DELIKT_RESTBEREICHERUNG_VERJAEHRUNGSGRUNDFRIST', eingaben, [dict(operation='Früheres Ende aus Entstehung des Restbereicherungsanspruchs plus zehn Jahre und Verletzungshandlung/sonstigem auslösendem Ereignis plus dreißig Jahre')], eingaben.copy())
    ergebnis['annahmen'] = ['Qualifizierter gesetzlicher Anwendungsfall und rechtlich bestimmte Ereignistage; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['Nur verknüpfte gesetzliche Grundfristen; keine automatische Hemmung, Ablaufhemmung, Neubeginn oder Feiertagskorrektur. Ende bezeichnet letzten eingeschlossenen Tag bis Tagesablauf. Keine abschließende Feststellung eingetretener Verjährung.', 'Nur§852 Restbereicherung nach deliktischem Erlangen auf Kosten des Verletzten, keine allgemeine Schadensersatzverjährung oder Anspruchshöhe. Maßgebliches auslösendes Ereignis rechtlich qualifizieren; Entstehung nicht vor Ereignis. Kenntnis ist hier kein Beginnparameter. Herausgabeumfang nachBereicherungsrecht gesondert.']
    return ergebnis


def lieferantenregress_verjaehrungsnachlauf(bisheriges_fristende=None, kaeuferanspruch_erfuellt_am=None, einordnungsnachweis=None):
    """§445b Absatz2: Zweimonatsminimum mit separat bestimmter Anspruchsfrist verknüpfen."""
    bisher = _datum(bisheriges_fristende, 'bisheriges_fristende')
    _datum(kaeuferanspruch_erfuellt_am, 'kaeuferanspruch_erfuellt_am')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    minimum = _frist(kaeuferanspruch_erfuellt_am, 2, 'monate', 'ereignis')
    eingaben = dict(bisheriges_fristende=bisheriges_fristende, kaeuferanspruch_erfuellt_am=kaeuferanspruch_erfuellt_am, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(dict(bisheriges_fristende=bisheriges_fristende, zweimonats_mindestende=minimum.isoformat(), verknuepftes_fristende=max(bisher, minimum).isoformat()), 'daten', 'BGB_LIEFERANTENREGRESS_VERJAEHRUNGSNACHLAUF', eingaben, [dict(operation='Späteres Ende aus separat bestimmter Anspruchsfrist und Käuferanspruchserfüllung plus zwei Monate')], eingaben.copy())
    ergebnis['annahmen'] = ['Qualifizierter§445b Absatz2-Anspruch und separat bestimmter bisheriger Fristablauf; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['Nur Zweimonats-Ablaufminimum für qualifizierte437-/445a-Ansprüche wegen mangelhafter neu hergestellter Sache, nicht digitale Vertriebskette327u. Bisheriges Ende muss zum konkreten Anspruch passen; keine pauschale Zweijahresfrist für alle437-Ansprüche. Keine historische Fünfjahreskappung. Sonstige Hemmung/Ablaufhemmung/Neubeginn und Kalenderkorrekturen separat qualifizieren. Keine eigenständige Wiederbelebungsentscheidung oder Feststellung von Käuferbefriedigung. Ende jeweils letzter eingeschlossener Tag bis Tagesablauf.']
    return ergebnis
