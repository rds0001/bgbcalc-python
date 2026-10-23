from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _ganzzahl, _tage_addieren, _text

def wohnraum_umwandlung_sperrfrist(massgeblicher_erwerb_am=None, sperrfrist_monate=None, einordnungsnachweis=None):
    """Qualifizierte Sperrfrist von36bis120Monaten ab maßgeblichem Erwerb berechnen und ersten Tag nach Fristablauf ausweisen."""
    _datum(massgeblicher_erwerb_am,'massgeblicher_erwerb_am')
    monate = _ganzzahl(sperrfrist_monate,'sperrfrist_monate',36,120)
    ende = _frist(massgeblicher_erwerb_am,monate,'monate','ereignis')
    wert = dict(sperrfristende=ende.isoformat(),erster_tag_nach_sperrfrist=_tage_addieren(ende,1).isoformat())
    _text(einordnungsnachweis,"einordnungsnachweis")
    eingaben = dict(massgeblicher_erwerb_am=massgeblicher_erwerb_am, sperrfrist_monate=sperrfrist_monate, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,"daten_und_zahlen",'BGB_WOHNRAUM_UMWANDLUNG_SPERRFRIST',eingaben,[dict(operation='Qualifizierte Sperrfrist von36bis120Monaten ab maßgeblichem Erwerb berechnen und ersten Tag nach Fristablauf ausweisen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§577aI/Ia/II/IIa: nur Ende der qualifizierten Kündigungsbeschränkung. Bei späterer Begründung von Wohnungseigentum nachVeräußerung/BelastungIa läuft die Frist bereits ab dem VorgangIa, nicht erneut ab Umwandlung. Nach Ablauf kann erst diese Sperre entfallen; keine automatische Kündigungsberechtigung, kein Mietende und keine Verkürzung gesetzlicher Kündigungsfristen. Einschlägige verlängerte Dauer ausdrücklich eingeben; nicht pauschal zehn Jahre für sämtliche Orte. Keine193Verschiebung, da Schutzzeitraum.']
    return ergebnis

def landpacht_fortsetzungsdauergrenze(pachtbeginn_am=None, vereinbartes_pachtende_am=None, pachtart=None, einordnungsnachweis=None):
    """Zwölf- beziehungsweise Achtzehnjahresgrenze ab Beginn des laufenden Pachtverhältnisses berechnen und vereinbarte Dauer damit vergleichen."""
    beginn = _datum(pachtbeginn_am,'pachtbeginn_am');vertrag = _datum(vereinbartes_pachtende_am,'vereinbartes_pachtende_am')
    if vertrag<beginn:
        _fehler('vereinbartes_pachtende_am','Pachtende darf nicht vor Beginn liegen.')
    _auswahl(pachtart,'pachtart',('betrieb_oder_kultiviertes_moor_oedland','anderes_grundstueck'))
    jahre = 18 if pachtart=='betrieb_oder_kultiviertes_moor_oedland' else 12
    ende = _frist(pachtbeginn_am,jahre,'jahre','tagesbeginn')
    wert = dict(dauergrenze_jahre=jahre,gerichtlicher_hoechsttermin=ende.isoformat(),vereinbarte_dauer_erreicht_grenze=vertrag>=ende)
    _text(einordnungsnachweis,"einordnungsnachweis")
    eingaben = dict(pachtbeginn_am=pachtbeginn_am, vereinbartes_pachtende_am=vereinbartes_pachtende_am, pachtart=pachtart, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,"daten_und_zahlen",'BGB_LANDPACHT_FORTSETZUNGSDAUERGRENZE',eingaben,[dict(operation='Zwölf- beziehungsweise Achtzehnjahresgrenze ab Beginn des laufenden Pachtverhältnisses berechnen und vereinbarte Dauer damit vergleichen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§595III3/VI:18Jahre für Betriebspacht, betriebsbildende Zupachtung oder vom Pächter kultiviertes Moor-/Ödland, sonst12Jahre. Vereinbarte Dauer mindestens dieser Länge ist eine numerische Ausschlussgrenze nachIII3; keine alleinige Entscheidung über alle Fortsetzungsgründe. Gerichtliche Fortsetzung nachVI höchstens bis zum ausgegebenen Termin, gerechnet ab Beginn des laufenden Pachtverhältnisses, nicht je Verlängerung neu. Weitere Ausschlussgründe, angemessene kürzere Dauer, Teilflächen und Bedingungen extern qualifizieren. Ende einschließlich Endtag; keine193Verschiebung.']
    return ergebnis

