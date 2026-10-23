from .betraege import _geld
from .kalender import _ergebnis, _fehler, _ganzzahl, _text, _vorhanden
from .zahlen import _subtrahieren
from .zinsen import _bruchteile
from .beschenktenschenkungsrang import pflichtteilsergaenzung_schenkungsvorgaenge

def pflichtteilsergaenzung_personenbegrenzte_schenkungen(fehlbetrag=None, schenkungen=None, personenrahmen=None, einordnungsnachweis=None):
    """Gemeinsamen Personenrahmen einmalig in absteigender Schenkungsrangfolge auf Vorgangsgrenzen verteilen und vorhandenen2329-Rangkern auf begrenzte Vorgänge anwenden."""
    _text(einordnungsnachweis,'einordnungsnachweis');_vorhanden(schenkungen,'schenkungen');_vorhanden(personenrahmen,'personenrahmen')
    if not isinstance(schenkungen,list) or not 1<=len(schenkungen)<=1000 or not isinstance(personenrahmen,list) or not 1<=len(personenrahmen)<=1000:
        _fehler('schenkungen_und_personenrahmen','Beide Listen müssen1..1000 Einträge enthalten.')
    rahmen = {}
    for person in personenrahmen:
        if not isinstance(person,dict) or set(person)!={'beschenkter_id','gemeinsame_haftungsgrenze'}:
            _fehler('personenrahmen','Genau beschenkter_id und gemeinsame_haftungsgrenze erforderlich.')
        name = _text(person['beschenkter_id'],'beschenkter_id')
        if name in rahmen:
            _fehler('personenrahmen','Jede Person genau einmal.')
        rahmen[name] = _geld(person['gemeinsame_haftungsgrenze'])
    vorbereitet = [];namen = set()
    for geschenk in schenkungen:
        if not isinstance(geschenk,dict) or set(geschenk)!={'schenkung_id','beschenkter_id','schenkungsrang','haftungsgrenze'}:
            _fehler('schenkungen','Genau schenkung_id, beschenkter_id, schenkungsrang und haftungsgrenze erforderlich.')
        name = _text(geschenk['beschenkter_id'],'beschenkter_id');namen.add(name)
        _ganzzahl(geschenk['schenkungsrang'],'schenkungsrang',1,1000);_geld(geschenk['haftungsgrenze'])
        vorbereitet.append(geschenk.copy())
    if namen!=set(rahmen):
        _fehler('personenrahmen','Rahmen müssen genau die vorkommenden Beschenkten abdecken.')
    for index in sorted(range(len(vorbereitet)),key=lambda i:vorbereitet[i]['schenkungsrang'],reverse=True):
        p = vorbereitet[index];name = p['beschenkter_id'];grenze = min(_geld(p['haftungsgrenze']),rahmen[name])
        rahmen[name] = _subtrahieren(rahmen[name],grenze);p['haftungsgrenze'] = _bruchteile(grenze)
    wert = pflichtteilsergaenzung_schenkungsvorgaenge(fehlbetrag,vorbereitet,True,einordnungsnachweis)['wert']
    eingaben = dict(fehlbetrag=fehlbetrag, schenkungen=schenkungen, personenrahmen=personenrahmen, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_PFLICHTTEILSERGAENZUNG_PERSONENBEGRENZTE_SCHENKUNGEN',eingaben,[dict(operation='Gemeinsamen Personenrahmen einmalig in absteigender Schenkungsrangfolge auf Vorgangsgrenzen verteilen und vorhandenen2329-Rangkern auf begrenzte Vorgänge anwenden.')],eingaben.copy())
    ergebnis["hinweise"] = ['§2329III: zeitlich eindeutig geordnete Schenkungen, gegebenenfalls mehrfach an dieselbe Person. Gemeinsamen rechtlich bestimmten Personenrahmen nur einmal verwenden und späteren Schenkungen vorrangig zuordnen; anschließend vorhandenen Schenkungsrang-/Empfängersummenkern anwenden. Rahmen müssen für diesen Ergänzungsanspruch tatsächlich rechtlich gelten, etwa nach vorqualifizierter Bereicherungs-/Einwendungsbewertung; keine automatisch erfundene Gesamtvermögens-, Selbstbehalts- oder Zahlungsfähigkeitsgrenze. Einzelgrenzen und gemeinsamer Rahmen dürfen nicht dieselbe Kürzung doppelt enthalten. Bereits geleistete Erfüllung und weitere konkurrierende Berechtigte gesondert. Gleichzeitige Schenkungen weiterhin außerhalb, keine erfundene Gleichquote oder Gesamtschuld. Ausgabe numerische Haftungs-/Befriedigungsgrenzen, kein automatischer gewöhnlicher Geldanspruch aus Sachherausgabe.']
    return ergebnis

