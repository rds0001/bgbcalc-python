from .kalender import _datum, _ergebnis, _fehler, _ganzzahl, _text, _vorhanden

def grundbuch_rangpaarvergleich(erstes_recht=None, zweites_recht=None, einordnungsnachweis=None):
    """Zwei Grundstücksrechte nach abteilungsabhängigem Eintragungsmaßstab paarweise vergleichen."""
    _text(einordnungsnachweis,'einordnungsnachweis')
    def lesen(recht,parameter):
        _vorhanden(recht,parameter)
        if not isinstance(recht,dict) or set(recht)!={'recht_id','abteilung','eintragungsposition','eintragungstag'}: _fehler(parameter,'Genau Kennung, Abteilung, Position und Eintragungstag erforderlich.')
        return (_text(recht['recht_id'],'recht_id'),_text(recht['abteilung'],'abteilung'),_ganzzahl(recht['eintragungsposition'],'eintragungsposition',1,9007199254740991),_datum(recht['eintragungstag'],'eintragungstag'))
    a=lesen(erstes_recht,'erstes_recht');b=lesen(zweites_recht,'zweites_recht')
    if a[0]==b[0]: _fehler('zweites_recht','Verschiedene Rechte erforderlich.')
    if a[1]==b[1]:
        if a[2]==b[2]: _fehler('eintragungsposition','Verschiedene tatsächliche Reihenfolgepositionen innerhalb derselben Abteilung erforderlich.')
        links,rechts=a[2],b[2];massstab='eintragungsreihenfolge'
    else: links,rechts=a[3],b[3];massstab='eintragungstag'
    wert=dict(rangvergleich=-1 if links<rechts else 1 if links>rechts else 0,vergleichsmassstab=massstab)
    eingaben = dict(erstes_recht=erstes_recht, zweites_recht=zweites_recht, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'rangvergleich','BGB_GRUNDBUCH_RANGPAARVERGLEICH',eingaben,[dict(operation='Zwei Grundstücksrechte nach abteilungsabhängigem Eintragungsmaßstab paarweise vergleichen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§879I/II: in derselben Grundbuchabteilung tatsächliche Reihenfolge der Eintragungen vergleichen; in verschiedenen Abteilungen angegebenen Eintragungstag vergleichen, bei gleichem Tag Gleichrang. Zeitpunkt einer späteren dinglichen Einigung ersetzt den Eintragungsmaßstab nicht. Position ist wirkliche Reihenfolge, nicht ungeprüft laufende Nummer eines Rechts oder Antragsnummer. Nur Paarvergleich: bei mehreren Rechten keine transitive globale Ranggruppe aus einzelnen Gleichrangvergleichen erfinden. Abweichende eingetragene Rangbestimmung,880Rangänderung,881Vorbehalt,883Vormerkung und Verwertungsbeträge gesondert. Gleiche Position verschiedener Rechte derselben Abteilung wird mangels eindeutig qualifizierter Reihenfolge nicht angenommen.']
    return ergebnis

