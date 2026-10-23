import re
from .kalender import _datum, _ergebnis, _fehler, _text, _vorhanden

def vormund_monatliche_besuchszahlen(pruefmonate=None, besuche=None, einordnungsnachweis=None):
    """Tatsächliche Besuchszahlen je ausgewähltem Kalendermonat zählen und mit mindestens einem Besuch vergleichen."""
    _vorhanden(pruefmonate,'pruefmonate');_vorhanden(besuche,'besuche');_text(einordnungsnachweis,'einordnungsnachweis')
    if not isinstance(pruefmonate,list) or not 1<=len(pruefmonate)<=1000: _fehler('pruefmonate','Liste1..1000 erforderlich.')
    if not isinstance(besuche,list) or len(besuche)>10000: _fehler('besuche','Liste0..10000 erforderlich.')
    zahlen={}
    for monat in pruefmonate:
        _text(monat,'pruefmonate')
        if not re.fullmatch('[0-9]{4}-[0-9]{2}',monat) or monat in zahlen: _fehler('pruefmonate','Eindeutige MonateYYYY-MM erforderlich.')
        _datum(monat+'-01','pruefmonate');zahlen[monat]=0
    namen=set();ausserhalb=0
    for besuch in besuche:
        if not isinstance(besuch,dict) or set(besuch)!={'besuch_id','besuch_am'}: _fehler('besuche','Genau Besuchskennung und Datum erforderlich.')
        name=_text(besuch['besuch_id'],'besuch_id');_datum(besuch['besuch_am'],'besuch_am')
        if name in namen: _fehler('besuch_id','Eindeutige Besuche erforderlich.')
        namen.add(name);monat=besuch['besuch_am'][:7]
        if monat in zahlen: zahlen[monat]+=1
        else: ausserhalb+=1
    wert=dict(monate=[dict(monat=m,besuchszahl=zahlen[m],regelmaessiger_mindestbesuch_erreicht=zahlen[m]>=1) for m in sorted(zahlen)],alle_monate_mit_mindestbesuch=all(x>=1 for x in zahlen.values()),besuche_ausserhalb_pruefmonate=ausserhalb)
    eingaben = dict(pruefmonate=pruefmonate, besuche=besuche, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'anzahlen_und_wahrheitswerte','BGB_VORMUND_MONATLICHE_BESUCHSZAHLEN',eingaben,[dict(operation='Tatsächliche Besuchszahlen je ausgewähltem Kalendermonat zählen und mit mindestens einem Besuch vergleichen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§1790III nennt in der Regel einmal im Monat. Die Funktion zählt tatsächliche Besuche je qualifiziertem Kalendermonat und vergleicht mit mindestens1; sie ersetzt dies nicht durch starre30-Tage-Abstände. Alle ausgewählten Monate werden ausgewiesen, auch ohne Besuch. Besuche außerhalb der Prüfmonate werden gesondert gezählt. Kürzere/längere gebotene Besuchsabstände, ein anderer Ort, Beginn/Ende der Vormundschaft und qualitative Kontaktpflichten sind rechtlich zu bestimmen; keine automatische Pflichtverletzungs- oder Haftungsentscheidung. Mehrere Mündel getrennt auswerten.']
    return ergebnis

