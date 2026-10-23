from .kalender import _datum, _ergebnis, _fehler, _text, _vorhanden
from .betraege import _geld
from .zahlen import _addieren
from .zinsen import _bruchteile
from .hypothekenkalender import hypothek_beschlagnahme_monatsgrenze

def hypothek_mietverfuegung_zeitzuordnung(beschlagnahme_am=None, mietabschnitte=None, einordnungsnachweis=None):
    """Vor Beschlagnahme verfügte Miet-/Pachtabschnittsbeträge nach gesetzlicher Monatsgrenze zeitlich auswählen und getrennt summieren."""
    _text(einordnungsnachweis,'einordnungsnachweis')
    grenze=hypothek_beschlagnahme_monatsgrenze(beschlagnahme_am,einordnungsnachweis)['wert']['letzter_erfasster_monat_endet_am'];tag=_datum(grenze,'monatsgrenze')
    _vorhanden(mietabschnitte,'mietabschnitte')
    if not isinstance(mietabschnitte,list) or len(mietabschnitte)>1000: _fehler('mietabschnitte','Liste0..1000 erforderlich.')
    namen=set();intervalle=[];innen=_geld('0');aussen=_geld('0');ids=[]
    for p in mietabschnitte:
        if not isinstance(p,dict) or set(p)!={'abschnitt_id','erster_miettag','letzter_miettag','verfuegungsbetrag'}: _fehler('mietabschnitte','Genau Kennung, Mietzeitgrenzen und Verfügungsbetrag erforderlich.')
        name=_text(p['abschnitt_id'],'abschnitt_id')
        if name in namen: _fehler('abschnitt_id','Doppelte Kennung unzulässig.')
        namen.add(name);a=_datum(p['erster_miettag'],'erster_miettag');b=_datum(p['letzter_miettag'],'letzter_miettag');betrag=_geld(p['verfuegungsbetrag'])
        if b<a: _fehler('mietabschnitte','Ende vor Beginn.')
        if a<=tag<b: _fehler('mietabschnitte','Grenzüberschreitenden Abschnitt zuvor sachgerecht teilen.')
        intervalle.append((a,b))
        if b<=tag: innen=_addieren(innen,betrag);ids.append(name)
        else: aussen=_addieren(aussen,betrag)
    vorher=None
    for a,b in sorted(intervalle):
        if vorher is not None and a<=vorher: _fehler('mietabschnitte','Keine überlappenden Abschnitte derselben Forderungsgrundlage.')
        vorher=b
    wert=dict(letzter_erfasster_miettag=grenze,betrag_im_zeitlichen_fenster=_bruchteile(innen),betrag_ausserhalb_des_zeitlichen_fensters=_bruchteile(aussen),abschnitt_ids_im_zeitlichen_fenster=ids)
    eingaben = dict(beschlagnahme_am=beschlagnahme_am, mietabschnitte=mietabschnitte, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_HYPOTHEK_MIETVERFUEGUNG_ZEITZUORDNUNG',eingaben,[dict(operation='Vor Beschlagnahme verfügte Miet-/Pachtabschnittsbeträge nach gesetzlicher Monatsgrenze zeitlich auswählen und getrennt summieren.')],eingaben.copy())
    ergebnis["hinweise"] = ['§1124II: vor Beschlagnahme erfolgte Verfügungen nach ihrem Miet-/Pachtzeitraum der Monatsgrenze zuordnen. Beschlagnahme bis einschließlich15.: Ende laufender Monat; nach15.: Ende Folgemonat. Beträge vollständig innerhalb/außerhalb getrennt summieren. Keine pauschale gleichmäßige Tagesaufteilung für einen grenzüberschreitenden Gesamtbetrag. Nur eine Forderungs-/Vertragsgrundlage je Aufruf; mehrere Verträge getrennt behandeln. Zeitliche Zuordnung setzt übrige1124-Voraussetzungen voraus und entscheidet keine sonstigen Wirksamkeitsfragen.1123-Jahresbefreiung sowie1126-Dreimonatsregel nicht durch diesen Monatsvergleich ersetzen.']
    return ergebnis

