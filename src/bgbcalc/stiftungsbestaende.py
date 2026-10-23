from .kalender import _ergebnis, _fehler, _text, _vorhanden
from .betraege import _geld
from .zahlen import _addieren
from .zinsen import _bruchteile

def stiftung_grundstock_soll_ist_vergleich(erforderlicher_erhaltungswert=None, vorhandener_erhaltungswert=None, einordnungsnachweis=None):
    """Qualifizierten Erhaltungs-Sollwert und vorhandenen Grundstockwert vergleichen, Unterdeckung und Mehrbestand getrennt ausweisen."""
    soll=_geld(erforderlicher_erhaltungswert);ist=_geld(vorhandener_erhaltungswert)
    _text(einordnungsnachweis,'einordnungsnachweis')
    wert=dict(rechnerische_unterdeckung=_bruchteile(max(0,soll-ist)),rechnerischer_mehrbestand=_bruchteile(max(0,ist-soll)),sollwert_erreicht=ist>=soll)
    eingaben = dict(erforderlicher_erhaltungswert=erforderlicher_erhaltungswert, vorhandener_erhaltungswert=vorhandener_erhaltungswert, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'EUR_und_wahrheitswert','BGB_STIFTUNG_GRUNDSTOCK_SOLL_IST_VERGLEICH',eingaben,[dict(operation='Qualifizierten Erhaltungs-Sollwert und vorhandenen Grundstockwert vergleichen, Unterdeckung und Mehrbestand getrennt ausweisen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§83cI: ausschließlich numerischer Soll/Ist-Vergleich unter rechtlich qualifiziertem Erhaltungsmaßstab. Keine selbst erfundene Wahl zwischen nominaler, realer oder gegenständlicher Kapitalerhaltung, keine automatische Inflationsindexierung. Positiver Mehrbestand ist weder automatisch verwendbarer Umschichtungsgewinn noch ausschüttbarer Ertrag. Zulässiger Verbrauch und Wiederaufstockung83cII bleiben getrennt.']
    return ergebnis

def stiftung_uebertragene_vermoegensbestaende(grundstock_uebernehmende_stiftung=None, sonstiges_vermoegen_uebernehmende_stiftung=None, uebertragende_stiftungen=None, einordnungsnachweis=None):
    """Grundstock und sonstige Vermögensbestände wirksam übertragender Stiftungen getrennt zum Bestand der übernehmenden Stiftung addieren."""
    grund=_geld(grundstock_uebernehmende_stiftung);sonstig=_geld(sonstiges_vermoegen_uebernehmende_stiftung)
    _text(einordnungsnachweis,'einordnungsnachweis');_vorhanden(uebertragende_stiftungen,'uebertragende_stiftungen')
    if not isinstance(uebertragende_stiftungen,list) or not 1<=len(uebertragende_stiftungen)<=1000: _fehler('uebertragende_stiftungen','Liste1..1000 erforderlich.')
    kennungen=set()
    for s in uebertragende_stiftungen:
        if not isinstance(s,dict) or set(s)!={'stiftung_id','grundstockvermoegen','sonstiges_vermoegen'}: _fehler('uebertragende_stiftungen','Genau Kennung, Grundstock und sonstiger Bestand erforderlich.')
        kennung=_text(s['stiftung_id'],'stiftung_id')
        if kennung in kennungen: _fehler('stiftung_id','Doppelte Stiftung unzulässig.')
        kennungen.add(kennung);grund=_addieren(grund,_geld(s['grundstockvermoegen']));sonstig=_addieren(sonstig,_geld(s['sonstiges_vermoegen']))
    wert=dict(grundstockvermoegen_nach_uebertragung=_bruchteile(grund),sonstiges_vermoegen_nach_uebertragung=_bruchteile(sonstig),gesamtvermoegen_nach_uebertragung=_bruchteile(_addieren(grund,sonstig)))
    eingaben = dict(grundstock_uebernehmende_stiftung=grundstock_uebernehmende_stiftung, sonstiges_vermoegen_uebernehmende_stiftung=sonstiges_vermoegen_uebernehmende_stiftung, uebertragende_stiftungen=uebertragende_stiftungen, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_STIFTUNG_UEBERTRAGENE_VERMOEGENSBESTAENDE',eingaben,[dict(operation='Grundstock und sonstige Vermögensbestände wirksam übertragender Stiftungen getrennt zum Bestand der übernehmenden Stiftung addieren.')],eingaben.copy())
    ergebnis["hinweise"] = ['§86cI2/II und86fI/II: vollständig übertragene qualifizierte Vermögensbestände addieren, Grundstock getrennt als Grundstock fortführen. Kein mehrfaches Einrechnen schon in der übernehmenden Stiftung erfasster Übertragungen. Nichtnegative qualifizierte Vermögenswerte, keine automatische Saldierung von Verbindlichkeiten oder konzerninternen Forderungen, keine rechtliche Übertragungswirksamkeit/Neugründung. Genehmigung, Unanfechtbarkeit und Zahl übertragender Stiftungen bei Zusammenlegung gesondert; keine künstliche Umwidmung sonstigen Vermögens in Grundstock.']
    return ergebnis

