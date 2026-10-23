from .kalender import _ergebnis, _fehler, _text, _vorhanden
from .betraege import _geld
from .zinsen import _bruchteile
from .staffelmietzeit import staffelmiete_mindestabstaende

def staffelmiete_aufsteigende_betragsgrenzen(staffeln=None, einordnungsnachweis=None):
    """Für eine vollständige aufsteigende gültige Staffelfolge individuelle Mietgrenzen und Schutz der zuvor wirksam begründeten Miethöhe fortschreiben."""
    _vorhanden(staffeln,'staffeln');_text(einordnungsnachweis,'einordnungsnachweis')
    if not isinstance(staffeln,list) or not 2<=len(staffeln)<=1000: _fehler('staffeln','Liste2..1000 erforderlich.')
    vorher_vereinbart=_geld('0');geschuetzt=_geld('0');daten=[];betraege=[]
    for s in staffeln:
        if not isinstance(s,dict) or set(s)!={'staffelbeginn_am','vereinbarte_monatsmiete','zulaessige_monatsmiete_ohne_vorstaffelschutz'}: _fehler('staffeln','Genau Beginn, vereinbarte Monatsmiete und individuelle Grenze erforderlich.')
        m=_geld(s['vereinbarte_monatsmiete']);g=_geld(s['zulaessige_monatsmiete_ohne_vorstaffelschutz'])
        if m<vorher_vereinbart: _fehler('staffeln','Nur nicht sinkende Vereinbarungsbeträge zugelassen.')
        vorher_vereinbart=m;daten.append(s['staffelbeginn_am']);betraege.append((m,g))
    zeit=staffelmiete_mindestabstaende(daten,einordnungsnachweis)
    if not zeit['wert']['alle_jahresabstaende_eingehalten']: _fehler('staffeln','Gültige Jahresabstände erforderlich.')
    wert=[]
    for datum,(m,g) in zip(daten,betraege):
        grenze=max(g,geschuetzt);geschuetzt=min(m,grenze)
        wert.append(dict(staffelbeginn_am=datum,rechnerische_monatsgrenze=_bruchteile(grenze),rechnerische_monatsmiete=_bruchteile(geschuetzt),monatlicher_ueberhoehungsbetrag=_bruchteile(m-geschuetzt)))
    eingaben = dict(staffeln=staffeln, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_STAFFELMIETE_AUFSTEIGENDE_BETRAGSGRENZEN',eingaben,[dict(operation='Für eine vollständige aufsteigende gültige Staffelfolge individuelle Mietgrenzen und Schutz der zuvor wirksam begründeten Miethöhe fortschreiben.')],eingaben.copy())
    ergebnis["hinweise"] = ['§557aIV in Verbindung556gI2: für jede aufsteigende gültige Staffel Höchstbetrag mit der zuvor wirksam begründeten Miethöhe vergleichen; höhere geschützte Vormietstaffel erhalten, vereinbarte Monatsmiete auf diesen Höchstbetrag begrenzen. Nur rechtlich qualifizierte, vollständig geordnete und nicht sinkende Vereinbarungsbeträge; absteigende/neu verhandelte Folgen benötigen gesonderte Bewertung. Anfängliche Überhöhung wird nicht als geschützte Vorstaffelmiete fortgeschrieben. Die Höchstbeträge müssen556d–g einschließlich relevanter Vormiete/Modernisierung/Auskunft und bei Folgestaffeln Zeitpunkt der ersten Fälligkeit bereits korrekt berücksichtigen. Keine automatische10%-Bewertung aus unqualifizierter Vergleichsmiete. Fehlende Jahresabstände führen zu Eingabefehler für diese vorqualifizierte gültige Folge; keine automatische Ersatzvereinbarung. Rückforderung, Rüge, Verjährung, Kündigungsausschluss und Rundung gesondert.']
    return ergebnis

