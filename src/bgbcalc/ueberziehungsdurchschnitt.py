"""Zeitgewichtete Überziehungsdurchschnitte und gesetzliche Betragsvergleiche."""
from .betraege import _geld
from .kalender import _text, _fehler, _vorhanden, _ganzzahl, _auswahl, _ergebnis
from .zahlen import _bruch, _addieren, _multiplizieren, _dividieren
from .zinsen import _bruchteile


def ueberziehung_durchschnittsvergleich(kontosaldoabschnitte=None, bezugsbetrag=None, vergleichsregel=None, einordnungsnachweis=None):
    """Betragstage mitteln und mit75% Kreditlinie oder einem Sechstel des Dreimonatsgeldeingangs vergleichen."""
    basis=_geld(bezugsbetrag); _auswahl(vergleichsregel,'vergleichsregel',('kreditlinie_504a','geduldete_ueberziehung_505'))
    _text(einordnungsnachweis,'einordnungsnachweis'); _vorhanden(kontosaldoabschnitte,'kontosaldoabschnitte')
    if not isinstance(kontosaldoabschnitte,list) or not 1<=len(kontosaldoabschnitte)<=10000:
        _fehler('kontosaldoabschnitte','Vollständige Liste mit1bis10000 nicht überlappenden Zeitabschnitten erforderlich.')
    tagessumme=0; betragstage=_bruch(0); durchgehend=True
    for abschnitt in kontosaldoabschnitte:
        if not isinstance(abschnitt,dict) or set(abschnitt)!={'kalendertage','ueberziehungsbetrag'}:
            _fehler('kontosaldoabschnitte','Genau kalendertage und ueberziehungsbetrag erforderlich.')
        tage=_ganzzahl(abschnitt['kalendertage'],'kalendertage',1,1000000); betrag=_geld(abschnitt['ueberziehungsbetrag'])
        tagessumme+=tage
        if tagessumme>1000000:
            _fehler('kalendertage','Gesamtzeitraum höchstens eine Million Kalendertage.')
        betragstage=_addieren(betragstage,_multiplizieren(betrag,_bruch(tage)))
        durchgehend= durchgehend and betrag>0
    durchschnitt=_dividieren(betragstage,_bruch(tagessumme))
    grenze=_multiplizieren(basis,_bruch(3,4) if vergleichsregel=='kreditlinie_504a' else _bruch(1,6))
    wert=dict(beobachtete_kalendertage=tagessumme,durchschnittlicher_ueberziehungsbetrag=_bruchteile(durchschnitt),betragsgrenze=_bruchteile(grenze),betragsgrenze_strikt_ueberschritten=durchschnitt>grenze,alle_abschnitte_mit_positiver_ueberziehung=durchgehend)
    eingaben=dict(kontosaldoabschnitte=kontosaldoabschnitte,bezugsbetrag=bezugsbetrag,vergleichsregel=vergleichsregel,einordnungsnachweis=einordnungsnachweis)
    ergebnis=_ergebnis(wert,'EUR_und_tage','BGB_UEBERZIEHUNG_DURCHSCHNITTSVERGLEICH',eingaben,[dict(operation='Summe(Betrag*Kalendertage)/Summe(Kalendertage); Vergleich strikt über3/4 Kreditlinie oder1/6 des gesamten Geldeingangs der letzten drei Monate.')],eingaben.copy())
    ergebnis['hinweise']=['§504a Absatz1/§505 Absatz2: Abschnitte müssen den rechtlich maßgeblichen Beobachtungszeitraum lückenlos und überschneidungsfrei abdecken; jeder Betrag gilt an allen eingegebenen Kalendertagen des Abschnitts. Guthabenzeiten mit Überziehungsbetrag0 einbeziehen, nicht weglassen. Nullabschnitt widerlegt rechnerisch ununterbrochene positive Nutzung; fehlende Tage werden nicht automatisch entdeckt. bezugsbetrag ist bei504a der für den Zeitraum unverändert vereinbarte Höchstbetrag; bei505 der gesamte maßgebliche Geldeingang der letzten drei Monate, dessen Monatsdurchschnitt ein Drittel beträgt, davon Hälfte=ein Sechstel. Geänderte Kreditlinien und andere Bewertungs-/Zeitgewichtungskonventionen gesondert qualifizieren. Beobachtungsdauer allein erfüllt nicht die zusätzlichen gesetzlichen Sechsmonats-/Mehr-als-Dreimonatsbedingungen; Kalendermonate mit Kalenderkern prüfen, niemals pauschal180/90Tage. Maßgeblichen Rechnungsabschluss rechtlich bestimmen. Ergebnis ist Betrags-/Kontinuitätsrechnung, keine automatische Beratungspflicht.']
    return ergebnis
