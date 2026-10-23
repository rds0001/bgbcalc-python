"""Liquidationsgrundbeträge und proportionale Ausfallnachverteilung nach §§736d/737."""
from .quotenverteilung import _begrenzte_quotenverteilung
from .betraege import _geld
from .kalender import _text, _fehler, _vorhanden, _ergebnis
from .zahlen import _bruch, _addieren, _subtrahieren, _multiplizieren, _dividieren
from .zinsen import _bruchteile


def gesellschaft_liquidationsgrundbetraege(gesellschaftsvermoegen=None, zu_berichtigende_verbindlichkeiten=None, erforderliche_rueckbehalte=None, rueckzuerstattende_beitraege=None, einordnungsnachweis=None):
    """Gläubiger- und Reservebedarf vor Beiträgen; Überschuss und gesamten Fehlbetrag berechnen."""
    verm, schulden, reserve, beitraege=[_geld(x) for x in (gesellschaftsvermoegen,zu_berichtigende_verbindlichkeiten,erforderliche_rueckbehalte,rueckzuerstattende_beitraege)]
    _text(einordnungsnachweis,'einordnungsnachweis')
    glaeubiger=_addieren(schulden,reserve); bedarf=_addieren(glaeubiger,beitraege)
    wert=dict(glaeubiger_und_reservebedarf=_bruchteile(glaeubiger),nach_glaeubigern_verbleibend=_bruchteile(max(_subtrahieren(verm,glaeubiger),_bruch(0))),beitragsrueckerstattungsbedarf=_bruchteile(beitraege),verteilbarer_ueberschuss=_bruchteile(max(_subtrahieren(verm,bedarf),_bruch(0))),von_gesellschaftern_zu_deckender_fehlbetrag=_bruchteile(max(_subtrahieren(bedarf,verm),_bruch(0))))
    eingaben=dict(gesellschaftsvermoegen=gesellschaftsvermoegen,zu_berichtigende_verbindlichkeiten=zu_berichtigende_verbindlichkeiten,erforderliche_rueckbehalte=erforderliche_rueckbehalte,rueckzuerstattende_beitraege=rueckzuerstattende_beitraege,einordnungsnachweis=einordnungsnachweis)
    ergebnis=_ergebnis(wert,'EUR','BGB_GESELLSCHAFT_LIQUIDATIONSGRUNDBETRAEGE',eingaben,[dict(operation='Gläubiger und gesonderte Reserven vor Beitragsrückerstattung; Vermögen minus Gesamtbedarf als positiver Überschuss oder umgekehrt als Fehlbetrag.')],eingaben.copy())
    ergebnis['hinweise']=['§736d Absatz4–6/§737: tatsächlich verfügbares Liquidationsvermögen; fällige zu berichtigende Verbindlichkeiten und erforderliche Rückbehalte für nicht fällige/streitige Verbindlichkeiten überschneidungsfrei. Rückzuerstattende Beiträge sind rechtlich qualifiziert: Sachbeiträge zum Einbringungswert, Dienste/Nutzungsüberlassung im Zweifel kein Ersatz. Überschuss nach Gewinn-/Verlustquoten verteilen; Fehlbetrag nach §737 decken. Reicht Vermögen nicht, wird keine freie Quote für teilweise Beitragsrückerstattung oder Rangfolge unter Gläubigern erfunden. Kein Ersatz für Insolvenzprüfung, Bewertung von Sachbeiträgen oder Abrechnung bereits erfolgter Liquidationszahlungen.']
    return ergebnis


def gesellschaft_liquidationsfehlbetrag_verteilen(fehlbetrag=None, gesellschafter=None, einordnungsnachweis=None):
    """Fehlbetrag nach Quoten verteilen und qualifiziert uneinbringliche Teile proportional nachverteilen."""
    fehl=_geld(fehlbetrag); _text(einordnungsnachweis,'einordnungsnachweis'); _vorhanden(gesellschafter,'gesellschafter')
    if not isinstance(gesellschafter,list) or not 2<=len(gesellschafter)<=1000:
        _fehler('gesellschafter','Vollständige Liste mit2bis1000 Gesellschaftern erforderlich.')
    namen=[]; quoten=[]; grenzen=[]; summe=_bruch(0)
    for person in gesellschafter:
        if not isinstance(person,dict) or set(person)!={'gesellschafter_id','gewinn_verlust_anteil','einbringlicher_hoechstbetrag'}:
            _fehler('gesellschafter','Kennung, Gewinn-/Verlustanteil und einbringlicher Höchstbetrag erforderlich.')
        kennung=_text(person['gesellschafter_id'],'gesellschafter_id'); quote=_geld(person['gewinn_verlust_anteil']); grenze=_geld(person['einbringlicher_hoechstbetrag'])
        if kennung in namen or quote>1:
            _fehler('gesellschafter','Eindeutige Kennungen und Quoten höchstens eins erforderlich.')
        namen.append(kennung); quoten.append(quote); grenzen.append(grenze); summe=_addieren(summe,quote)
    if summe!=1:
        _fehler('gewinn_verlust_anteil','Vollständige Gewinn-/Verlustquoten müssen eins ergeben.')
    zugeordnet,rest = _begrenzte_quotenverteilung(fehl,quoten,grenzen)
    verteilung=[]
    for i,n in enumerate(namen):
        regel=_multiplizieren(fehl,quoten[i])
        verteilung.append(dict(gesellschafter_id=n,regelanteil=_bruchteile(regel),beibringbarer_betrag=_bruchteile(zugeordnet[i]),zusaetzliche_ausfalllast=_bruchteile(max(_subtrahieren(zugeordnet[i],regel),_bruch(0)))))
    wert=dict(verteilung=verteilung,gesamt_beibringbar=_bruchteile(_subtrahieren(fehl,rest)),ungedeckter_fehlbetrag=_bruchteile(rest))
    eingaben=dict(fehlbetrag=fehlbetrag,gesellschafter=gesellschafter,einordnungsnachweis=einordnungsnachweis)
    ergebnis=_ergebnis(wert,'EUR','BGB_GESELLSCHAFT_LIQUIDATIONSFEHLBETRAG_VERTEILEN',eingaben,[dict(operation='Fehlbetrag nach vollständigen Gewinn-/Verlustquoten; nicht erlangbare Teile wiederholt nach relativen Quoten der übrigen einbringlichen Gesellschafter verteilen.')],eingaben.copy())
    ergebnis['hinweise']=['Nur §737 bei qualifiziertem Liquidationsfehlbetrag einschließlich Beitragsrückerstattungsbedarf. Einbringlicher Höchstbetrag bezeichnet rechtlich/tatsächlich festgestellten insgesamt noch erlangbaren Betrag für diesen Fehlbetrag, keine beliebige vertragliche Haftungsbegrenzung und keine bereits gezahlte Summe. Beträge auf gemeinsame Abrechnungsbasis bringen; Ausfälle bis zur Ausschöpfung der übrigen Grenzen proportional nachverteilen. Nullquote trägt keine rechnerische Ausfalllast. Uneinbringlicher Rest bleibt offen; kein Erlass und keine freie Beitragsrückzahlungsquote. Keine Feststellung der Insolvenz oder automatischer Vollstreckungsprognosen.']
    return ergebnis
