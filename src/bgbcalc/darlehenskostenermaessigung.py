"""§501: taganteilige Ermäßigung ausdrücklich homogener Zins-/Kostenabschnitte."""
from .betraege import _geld
from .kalender import _datum, _text, _fehler, _vorhanden, _auswahl, _ergebnis
from .zahlen import _bruch, _addieren, _subtrahieren, _multiplizieren
from .zinsen import _bruchteile


def verbraucherdarlehen_kostenabschnitte_ermaessigen(kostenabschnitte=None, ermaessigung_ab=None, ermaessigungsfall=None, einordnungsnachweis=None):
    """Homogene Kalenderkostenabschnitte am qualifizierten Ermäßigungsbeginn teilen und berechtigte Restkosten abziehen."""
    grenze=_datum(ermaessigung_ab,'ermaessigung_ab'); _auswahl(ermaessigungsfall,'ermaessigungsfall',('vorzeitige_erfuellung','kuendigung'))
    _text(einordnungsnachweis,'einordnungsnachweis'); _vorhanden(kostenabschnitte,'kostenabschnitte')
    if not isinstance(kostenabschnitte,list) or not 1<=len(kostenabschnitte)<=1000:
        _fehler('kostenabschnitte','Liste mit1bis1000 eindeutig abgegrenzten Kostenpositionen erforderlich.')
    namen=set(); positionen=[]; gesamt=_bruch(0); ermaessigung=_bruch(0)
    for a in kostenabschnitte:
        if not isinstance(a,dict) or set(a)!={'position_id','beginn_am','ende_am','kostenbetrag','kostenart'}:
            _fehler('kostenabschnitte','Position benötigt Kennung, Beginn, Ende, Kostenbetrag und Kostenart.')
        kennung=_text(a['position_id'],'position_id'); beginn=_datum(a['beginn_am'],'beginn_am'); ende=_datum(a['ende_am'],'ende_am'); betrag=_geld(a['kostenbetrag'])
        _auswahl(a['kostenart'],'kostenart',('zinsen','laufzeitabhaengige_kosten','sonstige_kosten'))
        if kennung in namen or ende<beginn:
            _fehler('kostenabschnitte','Eindeutige Positionen mit Ende frühestens am Beginn erforderlich.')
        namen.add(kennung); tage=(ende-beginn).days+1; resttage=max((ende-max(beginn,grenze)).days+1,0)
        anwendbar=ermaessigungsfall=='vorzeitige_erfuellung' or a['kostenart']!='sonstige_kosten'
        abzug=_multiplizieren(betrag,_bruch(resttage,tage)) if anwendbar else _bruch(0)
        gesamt=_addieren(gesamt,betrag); ermaessigung=_addieren(ermaessigung,abzug)
        positionen.append(dict(position_id=kennung,ermaessigungsbetrag=_bruchteile(abzug),verbleibender_kostenbetrag=_bruchteile(_subtrahieren(betrag,abzug))))
    wert=dict(positionen=positionen,urspruengliche_kostensumme=_bruchteile(gesamt),gesamtermaessigung=_bruchteile(ermaessigung),verbleibende_kostensumme=_bruchteile(_subtrahieren(gesamt,ermaessigung)))
    eingaben=dict(kostenabschnitte=kostenabschnitte,ermaessigung_ab=ermaessigung_ab,ermaessigungsfall=ermaessigungsfall,einordnungsnachweis=einordnungsnachweis)
    ergebnis=_ergebnis(wert,'EUR','BGB_VERBRAUCHERDARLEHEN_KOSTENABSCHNITTE_ERMAESSIGEN',eingaben,[dict(operation='Je homogenem einschließlich datiertem Kostenabschnitt Anteil der Kalendertage ab Kürzungsbeginn ermitteln; bei Kündigung sonstige nicht laufzeitabhängige Kosten ausnehmen; exakte Ermäßigungsbeträge summieren.')],eingaben.copy())
    ergebnis['hinweise']=['Nur qualifizierte §501-Abschnitte mit ausdrücklich gleichmäßiger Zuordnung je tatsächlichem Kalendertag innerhalb jeder Position. Beginn/Ende inklusive; ermaessigung_ab ist der rechtlich bestimmte erste zu kürzende Tag, bei Absatz2 nach Fälligkeit, nicht automatisch der Kündigungszugangstag. Andere Zins-/Zeitkonventionen und nichtlinear innerhalb einer Position gestaffelte Kosten sind nicht erfasst; rechtlich passende kleinere homogene Positionen bilden. Bei vorzeitiger Teilerfüllung ausschließlich Kosten des rechtlich zugeordneten erfüllten Teils eingeben, kein pauschaler Schuldquotenabschlag. Absatz1 umfasst qualifiziert zugeordnete Zinsen/Kosten; Absatz2 nur Zinsen und sonstige laufzeitabhängige Kosten. Identische wirtschaftliche Kosten dürfen nicht mehrfach vorkommen; parallele unterschiedliche Kostenarten sind zulässig. Keine Berechnung des Effektivzinses, keine Tilgungsplan-Neuberechnung, keine Vorfälligkeitsentschädigung und keine automatische Einstufung einer Kostenart. §507 Absatz3 gesetzliche Zinsbasis separat bestimmen.']
    return ergebnis
