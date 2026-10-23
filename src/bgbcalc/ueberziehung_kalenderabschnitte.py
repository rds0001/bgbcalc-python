from .kalender import _datum, _ergebnis, _fehler, _frist, _text, _vorhanden
from .ueberziehungsdurchschnitt import ueberziehung_durchschnittsvergleich

def ueberziehung_kalenderabschnitte(kontosaldoabschnitte=None, bezugsbetrag=None, vergleichsregel=None, einordnungsnachweis=None):
    """Lueckenlose tatsaechliche Kalendertage je Kontosaldoabschnitt bestimmen, Kalender-Monatsgrenzen berechnen und vorhandenen Betragstage-Durchschnittskern verwenden."""
    _text(einordnungsnachweis,'einordnungsnachweis');_vorhanden(kontosaldoabschnitte,'kontosaldoabschnitte')
    if not isinstance(kontosaldoabschnitte,list) or not 1<=len(kontosaldoabschnitte)<=10000: _fehler('kontosaldoabschnitte','Nichtleere begrenzte Liste erforderlich.')
    seg=[]
    for a in kontosaldoabschnitte:
        if not isinstance(a,dict) or set(a)!={'erster_tag','letzter_tag','ueberziehungsbetrag'}: _fehler('kontosaldoabschnitte','Genau beide Tagesgrenzen und Betrag erforderlich.')
        v=_datum(a['erster_tag'],'erster_tag');b=_datum(a['letzter_tag'],'letzter_tag')
        if b<v: _fehler('letzter_tag','Abschnittsende vor Beginn.')
        seg.append((v,b,a['ueberziehungsbetrag']))
    seg.sort(key=lambda a:a[0]);tage=[];vorher=None
    for v,b,x in seg:
        if vorher is not None and (v-vorher).days!=1: _fehler('kontosaldoabschnitte','Luecke oder Ueberschneidung im Beobachtungszeitraum.')
        tage.append(dict(kalendertage=(b-v).days+1,ueberziehungsbetrag=x));vorher=b
    von=seg[0][0];bis=seg[-1][1];gr=[_frist(von.isoformat(),m,'monate','tagesbeginn') for m in (1,3,6)]
    k=ueberziehung_durchschnittsvergleich(tage,bezugsbetrag,vergleichsregel,einordnungsnachweis)['wert']
    wert=dict(erster_beobachteter_tag=von.isoformat(),letzter_beobachteter_tag=bis.isoformat(),einmonatsablauf=gr[0].isoformat(),dreimonatsablauf=gr[1].isoformat(),sechsmonatsablauf=gr[2].isoformat(),mehr_als_ein_monat=bis>gr[0],mehr_als_drei_monate=bis>gr[1],sechs_monate_erreicht=bis>=gr[2],durchschnitt=k)
    eingaben = dict(kontosaldoabschnitte=kontosaldoabschnitte, bezugsbetrag=bezugsbetrag, vergleichsregel=vergleichsregel, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'daten_und_betragsvergleich','BGB_UEBERZIEHUNG_KALENDERABSCHNITTE',eingaben,[dict(operation='Lueckenlose tatsaechliche Kalendertage je Kontosaldoabschnitt bestimmen, Kalender-Monatsgrenzen berechnen und vorhandenen Betragstage-Durchschnittskern verwenden.')],eingaben.copy())
    ergebnis["hinweise"] = ['§504aI/505II: tatsaechliche lueckenlose Tagesabschnitte sortieren, Ueberschneidungen/Luecken ablehnen, Dauer und Betragstage mit bestehendem Durchschnittskern rechnen. Kalendermonate nach187II/188: sechs Monate einschliesslich Ablauf, mehr als ein/drei Monate strikt nach jeweiligem Ablauf; keine180/90/30-Tage-Ersatzregel. Erste Nutzung und Ende als ganze rechtlich qualifizierte Tage, keine Rundung untertaegiger Ereignisse. Nullsaldoabschnitt bleibt in Mittelung enthalten und widerlegt ununterbrochene positive Ueberziehung. Bei vierteljaehrlichem Abschluss ist504aI2am jeweiligen Abschluss zu beurteilen;505II3nennt ausdruecklich die Informationsvoraussetzungen vonSatz1. Datum des bankvertraglichen Abschlusses vorgeben, nicht automatisch Kalenderquartal unterstellen. Die Berechnung am gewaehlten Beobachtungsende ersetzt keine gesetzliche Stichtagsqualifikation.505II2: Bezugsbetrag gesamter Geldeingang der letzten3Monate, Vergleichsgrenze dessen1/6; Bezugseingangsfenster rechtlich separat bestimmen. Veraenderliche Kreditlinie und andere Mittelungskonventionen nicht automatisch behandeln. Keine vollstaendige Beratungs-/Informationsentscheidung aus reinem Zahlenvergleich.']
    return ergebnis

