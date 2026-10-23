from .betraege import _wahrheitswert
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _text, _vorhanden


def zinskalendertage_nach_ausschluss(erster_betrachteter_tag=None, letzter_betrachteter_tag=None, ausschlusszeitraeume=None, einordnungsnachweis=None):
    """Zinsfreie Kalenderintervalle begrenzen und vereinigen; deren Tage nur einmal vom betrachteten Zeitraum abziehen."""
    erster = _datum(erster_betrachteter_tag,'erster_betrachteter_tag');letzter = _datum(letzter_betrachteter_tag,'letzter_betrachteter_tag')
    if erster>letzter:
        _fehler('letzter_betrachteter_tag','Letzter Tag darf nicht vor erstem Tag liegen.')
    _vorhanden(ausschlusszeitraeume,'ausschlusszeitraeume')
    if not isinstance(ausschlusszeitraeume,list) or len(ausschlusszeitraeume)>10000:
        _fehler('ausschlusszeitraeume','Unbenannte Liste0bis10000 Ausschlussintervalle erforderlich.')
    _text(einordnungsnachweis,'einordnungsnachweis');intervalle=[]
    for zeitraum in ausschlusszeitraeume:
        if not isinstance(zeitraum,dict) or set(zeitraum)!={'erster_zinsfreier_tag','letzter_zinsfreier_tag','ausschlussgrund','hinterlegung_zurueckgenommen'}:
            _fehler('ausschlusszeitraeume','Genau beide Tagesgrenzen, ausschlussgrund und hinterlegung_zurueckgenommen erforderlich.')
        von = _datum(zeitraum['erster_zinsfreier_tag'],'erster_zinsfreier_tag');bis = _datum(zeitraum['letzter_zinsfreier_tag'],'letzter_zinsfreier_tag')
        if von>bis:
            _fehler('ausschlusszeitraeume','Ausschlussende darf nicht vor Ausschlussbeginn liegen.')
        grund = zeitraum['ausschlussgrund']
        _auswahl(grund,'ausschlussgrund',('nutzungen_ohne_verguetung_256','glaeubigerverzug_301','hinterlegung_379'))
        if grund=='hinterlegung_379':
            _wahrheitswert(zeitraum['hinterlegung_zurueckgenommen'],'hinterlegung_zurueckgenommen')
            if zeitraum['hinterlegung_zurueckgenommen']:
                continue
        elif zeitraum['hinterlegung_zurueckgenommen'] is not None:
            _fehler('hinterlegung_zurueckgenommen','Bei anderem Ausschlussgrund zwingendNone/NULL.')
        if bis>=erster and von<=letzter:
            intervalle.append((max(von,erster),min(bis,letzter)))
    vereinigt=[]
    for von,bis in sorted(intervalle):
        if vereinigt and (von-vereinigt[-1][1]).days<=1:
            vereinigt[-1]=(vereinigt[-1][0],max(bis,vereinigt[-1][1]))
        else:
            vereinigt.append((von,bis))
    gesamt=(letzter-erster).days+1;ausgeschlossen=sum((bis-von).days+1 for von,bis in vereinigt)
    wert=dict(kalendertage_gesamt=gesamt,zinsfreie_kalendertage=ausgeschlossen,verzinsliche_kalendertage=gesamt-ausgeschlossen,vereinigte_ausschlusszeitraeume=[dict(erster_zinsfreier_tag=von.isoformat(),letzter_zinsfreier_tag=bis.isoformat()) for von,bis in vereinigt])
    eingaben=dict(erster_betrachteter_tag=erster_betrachteter_tag,letzter_betrachteter_tag=letzter_betrachteter_tag,ausschlusszeitraeume=ausschlusszeitraeume,einordnungsnachweis=einordnungsnachweis)
    ergebnis=_ergebnis(wert,'kalendertage_und_intervalle','BGB_ZINSKALENDERTAGE_NACH_AUSSCHLUSS',eingaben,[dict(operation='Zinsfreie Kalenderintervalle begrenzen und vereinigen; deren Tage nur einmal vom betrachteten Zeitraum abziehen.')],eingaben.copy())
    ergebnis['hinweise']=['§256Satz2: nur Zeiträume, in denen dem Aufwendungsersatzberechtigten Nutzungen/Früchte des herauszugebenden Gegenstands ohne Vergütung verbleiben.301: qualifizierter Gläubigerverzug hinsichtlich der verzinslichen Geldschuld.379II/III: wirksame Hinterlegung; bei Rücknahme gilt diese als nicht erfolgt, deshalb wird ihr gesamtes eingegebenes Intervall nicht als zinsfrei abgezogen. Andere wirksame Ausschlussgründe desselben Tages bleiben bestehen. Tagesgrenzen einschließlich und rechtlich auf ganze Kalendertage normalisiert; untertägige Bruchteile nicht pauschal runden. Zeiträume werden auf den betrachteten Zinsabschnitt begrenzt, Überschneidungen/gleiche Tage nur einmal gezählt. Keine Verlängerung des Abschnitts wie bei Verjährungshemmung. Ergebnis ist tatsächliche Kalendertageszahl, noch kein universeller Jahresbruch oder Zinsbetrag; rechtlich geltende Zinstageskonvention, wechselnde Kapital-/Zinssatzwerte und Jahresgrenzen gesondert behandeln und vorhandene Zinsfunktionen verwenden. Erster/letzter Zinstag und rechtliche Ausschlussgründe müssen vorqualifiziert sein.']
    return ergebnis
