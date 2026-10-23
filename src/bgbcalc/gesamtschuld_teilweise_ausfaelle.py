from .betraege import _geld
from .kalender import _ergebnis, _fehler, _text, _vorhanden
from .zahlen import _addieren, _bruch, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile
from .quotenverteilung import _begrenzte_quotenverteilung

def gesamtschuld_quoten_mit_teilausfaellen(gesamtbetrag=None, gesamtschuldner=None, einordnungsnachweis=None):
    """Grundanteile mit vollständigen Innenquoten berechnen; Teilausfall nach qualifizierten Gewichten unter verbleibenden Gesamtgrenzen wiederholt nachverteilen."""
    betrag = _geld(gesamtbetrag);_text(einordnungsnachweis,'einordnungsnachweis');_vorhanden(gesamtschuldner,'gesamtschuldner')
    if not isinstance(gesamtschuldner,list) or not 2<=len(gesamtschuldner)<=1000:
        _fehler('gesamtschuldner','Liste2..1000 vollständiger Schuldnereinträge erforderlich.')
    namen=[];quoten=[];grenzen=[];gewichte=[];zahlungen=[];summe=_bruch(0)
    for person in gesamtschuldner:
        if not isinstance(person,dict) or set(person)!={'schuldner_id','innenquote','einbringlicher_gesamtbeitrag','ausfallgewicht','geleisteter_beitrag'}:
            _fehler('gesamtschuldner','Genau schuldner_id, innenquote, einbringlicher_gesamtbeitrag, ausfallgewicht und geleisteter_beitrag erforderlich.')
        name=_text(person['schuldner_id'],'schuldner_id');quote=_geld(person['innenquote'])
        if name in namen or quote>1:
            _fehler('gesamtschuldner','Eindeutige Kennungen und Quoten0..1 erforderlich.')
        namen.append(name);quoten.append(quote);grenzen.append(_geld(person['einbringlicher_gesamtbeitrag']));gewichte.append(_geld(person['ausfallgewicht']));zahlungen.append(_geld(person['geleisteter_beitrag']));summe=_addieren(summe,quote)
    if summe!=1:
        _fehler('innenquote','Vollständige Innenquoten müssen eins ergeben.')
    bezahlt=_bruch(0)
    for zahlung in zahlungen:bezahlt=_addieren(bezahlt,zahlung)
    if bezahlt>betrag:
        _fehler('geleisteter_beitrag','Summe zugeordneter Beiträge darf den Gesamtbetrag nicht überschreiten.')
    grund=[_multiplizieren(betrag,q) for q in quoten];erlangbar=[min(g,c) for g,c in zip(grund,grenzen)]
    deckung=_bruch(0)
    for g in erlangbar:deckung=_addieren(deckung,g)
    ausfall=_subtrahieren(betrag,deckung)
    zusatz,rest=_begrenzte_quotenverteilung(ausfall,gewichte,[_subtrahieren(c,g) for c,g in zip(grenzen,erlangbar)])
    wert=dict(verteilung=[dict(schuldner_id=name,urspruenglicher_beitrag=_bruchteile(g),beibringbarer_grundbeitrag=_bruchteile(bg),zusaetzliche_ausfalllast=_bruchteile(z),gesamt_beibringbar=_bruchteile(_addieren(bg,z)),rechnerischer_ueberbeitrag=_bruchteile(max(_subtrahieren(gez,_addieren(bg,z)),_bruch(0))),rechnerischer_beitragsrest=_bruchteile(max(_subtrahieren(_addieren(bg,z),gez),_bruch(0)))) for name,g,bg,z,gez in zip(namen,grund,erlangbar,zusatz,zahlungen)],urspruenglicher_ausfall=_bruchteile(ausfall),ungedeckter_ausfall=_bruchteile(rest),gesamt_gezahlter_beitrag=_bruchteile(bezahlt),gegenueber_glaeubiger_noch_offen=_bruchteile(_subtrahieren(betrag,bezahlt)))
    eingaben = dict(gesamtbetrag=gesamtbetrag, gesamtschuldner=gesamtschuldner, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_GESAMTSCHULD_QUOTEN_MIT_TEILAUSFAELLEN',eingaben,[dict(operation='Grundanteile mit vollständigen Innenquoten berechnen; Teilausfall nach qualifizierten Gewichten unter verbleibenden Gesamtgrenzen wiederholt nachverteilen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§426I: zunächst Gesamtbetrag nach rechtlich bestimmten Innenquoten, daraus nur erlangbare Grundbeiträge. Nicht erlangbaren Rest nach ausdrücklich qualifizierten Ausfallgewichten auf übrige noch verfügbare Beiträge verteilen, bei weiterer Begrenzung wiederholt proportional nachverteilen. Vorhandener begrenzter Quotenkern wird wiederverwendet. Gesetzlicher Gleichanteilsfall mit gleichen Quoten/Gewichten; abweichende Bestimmung muss rechtlich belegt sein. Keine automatische Annahme, dass beliebige Innenquote stets dieselbe Ausfallquote vorgibt. Grenzen sind tatsächlich/rechtlich erlangbare Gesamtbeiträge und keine bloßen Zahlungsangebote. Ursprüngliche Beitragspflicht ausgefallener Schuldner wird nicht erlassen. Keine Begrenzung der Außenhaftung, kein automatischer Forderungsübergang426II oder individueller Anspruchszuordnung zwischen bereits leistenden Schuldnern. Kein Gesamtvermögens- oder Insolvenzmodell und keine Cent-Rundung. Bereits erbrachte, auf diese Abrechnung zugeordnete Beiträge werden mit der rechnerischen Gesamtlast verglichen. Über-/Restbeitrag sind Rechensalden, keine automatisch fälligen Einzelansprüche gegen bestimmte Mitschuldner. Teilbefriedigung lässt einen gesondert ausgewiesenen Gläubigerrest; Gesamtüberzahlung an den Gläubiger außerhalb.']
    return ergebnis

