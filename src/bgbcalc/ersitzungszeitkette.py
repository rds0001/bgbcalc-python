from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _tage_addieren, _text, _vorhanden
from .verjaehrungshemmung import verjaehrung_gehemmte_kalendertage

def ersitzung_anrechenbare_zeitkette(fristfall=None, besitzabschnitte=None, hemmungszeitraeume=None, unterbrechungszeitraeume=None, einordnungsnachweis=None):
    """Lückenlose anrechenbare Besitzabschnitte verbinden; wirksame Unterbrechungen verwerfen Vorlauf und starten volle10/30Jahre neu; je Lauf vorhandenen Hemmungskern anwenden."""
    _auswahl(fristfall,'fristfall',('bewegliche_sache_937','buchersitzung_900','grundstuecksaufgebot_927','drittrecht_945'))
    _text(einordnungsnachweis,'einordnungsnachweis');daten = {}
    for name,liste,minimum,maximum in [('besitzabschnitte',besitzabschnitte,1,1000),('hemmungszeitraeume',hemmungszeitraeume,0,1000),('unterbrechungszeitraeume',unterbrechungszeitraeume,0,100)]:
        _vorhanden(liste,name)
        if not isinstance(liste,list) or not minimum<=len(liste)<=maximum:
            _fehler(name,'Unbenannte Intervallliste innerhalb des dokumentierten Umfangs erforderlich.')
        paare = []
        for abschnitt in liste:
            if not isinstance(abschnitt,dict) or set(abschnitt)!={'erster_tag','letzter_tag'}:
                _fehler(name,'Genau erster_tag und letzter_tag erforderlich.')
            von = _datum(abschnitt['erster_tag'],'erster_tag');bis = _datum(abschnitt['letzter_tag'],'letzter_tag')
            if von>bis:
                _fehler(name,'Letzter Tag nicht vor erstem Tag.')
            if paare and name=='besitzabschnitte' and von!=_tage_addieren(paare[-1][1],1):
                _fehler(name,'Rechtlich anrechenbare Besitzkette muss geordnet, lückenlos und ohne doppelte Tage sein.')
            if paare and name=='unterbrechungszeitraeume' and von<=paare[-1][1]:
                _fehler(name,'Unterbrechungen geordnet und überschneidungsfrei eingeben.')
            paare.append((von,bis))
        daten[name] = paare
    erster = daten['besitzabschnitte'][0][0];letzter = daten['besitzabschnitte'][-1][1]
    for name in ['hemmungszeitraeume','unterbrechungszeitraeume']:
        if any(von<erster or bis>letzter for von,bis in daten[name]):
            _fehler(name,'Nur abgeschlossene Intervalle innerhalb der belegten Besitzzeit.')
    hemmung = [dict(erster_gehemmter_tag=von.isoformat(),letzter_gehemmter_tag=bis.isoformat()) for von,bis in daten['hemmungszeitraeume']]
    jahre = 30 if fristfall in ('buchersitzung_900','grundstuecksaufgebot_927') else 10
    beginn = erster
    for von,bis in daten['unterbrechungszeitraeume']:
        vorende = verjaehrung_gehemmte_kalendertage(beginn.isoformat(),_frist(beginn.isoformat(),jahre,'jahre','tagesbeginn').isoformat(),hemmung,True)['wert']['rechnerischer_letzter_tag']
        if von>_datum(vorende,'vorende'):
            _fehler('unterbrechungszeitraeume','Unterbrechung liegt nach bereits rechnerisch vollendetem Lauf.')
        if bis==letzter:
            _vorhanden(None,'belegter_neuer_besitzlauf_nach_unterbrechung')
        beginn = _tage_addieren(bis,1)
    rechnung = verjaehrung_gehemmte_kalendertage(beginn.isoformat(),_frist(beginn.isoformat(),jahre,'jahre','tagesbeginn').isoformat(),hemmung,True)['wert']
    wert = dict(erster_tag_des_massgeblichen_laufs=beginn.isoformat(),rechnerisches_fristende=rechnung['rechnerischer_letzter_tag'],hemmungstage_im_massgeblichen_lauf=rechnung['beruecksichtigte_hemmungstage'],frist_am_letzten_belegten_tag_vollendet=letzter>=_datum(rechnung['rechnerischer_letzter_tag'],'fristende'))
    eingaben = dict(fristfall=fristfall, besitzabschnitte=besitzabschnitte, hemmungszeitraeume=hemmungszeitraeume, unterbrechungszeitraeume=unterbrechungszeitraeume, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'daten_und_tage','BGB_ERSITZUNG_ANRECHENBARE_ZEITKETTE',eingaben,[dict(operation='Lückenlose anrechenbare Besitzabschnitte verbinden; wirksame Unterbrechungen verwerfen Vorlauf und starten volle10/30Jahre neu; je Lauf vorhandenen Hemmungskern anwenden.')],eingaben.copy())
    ergebnis["hinweise"] = ['§§939bis944, bei900/927 entsprechend und945 für gesonderten drittrechtbezogenen Lauf: zehn beziehungsweise dreißig Kalenderjahre ab erstem vollständig anrechenbarem Tag, Vorgängerzeiten ohne Doppelzählung verbinden. Alle Besitzabschnitte müssen rechtlich eine lückenlose anrechenbare Kette bilden;940II-Nichtunterbrechung und Nachfolge943/944 vorqualifizieren. Wirksame Unterbrechung verwirft Vorzeit; neuer voller Lauf erst nach Ende der Unterbrechung und belegtem erneuten anrechenbarem Besitz. Unterbrechung nach bereits rechnerisch vollendetem Lauf wird als widersprüchliche Eingabe abgelehnt. Hemmungen werden vom vorhandenen209-Kern je neuem Lauf verarbeitet; vor dessen Beginn liegende Hemmung wirkt nicht nochmals.939II-Hemmung während210/211-Schutz muss als rechtlich bestimmtes Intervall vorliegen, nicht unbesehen als bloßes Maximaldatum. Nur abgeschlossene Intervalle bis zum letzten belegten Besitztag; Ergebnis danach ist rechnerische Prognose unter Fortdauer der Voraussetzungen. Keine automatische Personen-/Rechtsnachfolge, Wirkung gegenüber Dritten, Ausschließungsentscheidung oder Eigentumsfeststellung;900-Registergleichlauf,927-Zustimmungseintragungsgrenze und945-Bösglauben gesondert.']
    return ergebnis

