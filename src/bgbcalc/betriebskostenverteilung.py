"""§556a: positionsweise Betriebskostenquote und korrespondierende Mietherabsetzung."""
from .betraege import _geld, _geld_ergebnis
from .kalender import _text, _fehler, _vorhanden, _auswahl, _ergebnis
from .zahlen import _bruch, _addieren, _subtrahieren, _multiplizieren, _dividieren
from .zinsen import _bruchteile


def betriebskosten_wohnungsanteile(kostenpositionen=None, einordnungsnachweis=None):
    """Je Betriebskostenposition qualifizierten Bezugsanteil berechnen und Wohnungsbeträge summieren."""
    _text(einordnungsnachweis,'einordnungsnachweis'); _vorhanden(kostenpositionen,'kostenpositionen')
    if not isinstance(kostenpositionen,list) or not 1<=len(kostenpositionen)<=1000:
        _fehler('kostenpositionen','Liste mit1bis1000 Kostenpositionen erforderlich.')
    namen=set(); positionen=[]; summe=_bruch(0)
    for p in kostenpositionen:
        if not isinstance(p,dict) or set(p)!={'position_id','gesamtkosten','wohnungsbezugswert','gesamtbezugswert','umlagemassstab'}:
            _fehler('kostenpositionen','Kennung, Gesamtkosten, Wohnungs-/Gesamtbezugswert und Umlagemaßstab erforderlich.')
        name=_text(p['position_id'],'position_id'); kosten=_geld(p['gesamtkosten']); teil=_geld(p['wohnungsbezugswert']); gesamt=_geld(p['gesamtbezugswert'])
        _auswahl(p['umlagemassstab'],'umlagemassstab',('wohnflaeche','verbrauch','verursachung','vereinbarung','wohnungseigentum'))
        if name in namen or gesamt<=0 or teil>gesamt:
            _fehler('kostenpositionen','Eindeutige Positionen, positive Gesamtbezugswerte und Wohnungswerte höchstens Gesamtwert erforderlich.')
        namen.add(name); quote=_dividieren(teil,gesamt); betrag=_multiplizieren(kosten,quote); summe=_addieren(summe,betrag)
        positionen.append(dict(position_id=name,wohnungsquote=_bruchteile(quote),wohnungsbetrag=_bruchteile(betrag)))
    eingaben=dict(kostenpositionen=kostenpositionen,einordnungsnachweis=einordnungsnachweis)
    ergebnis=_ergebnis(dict(positionen=positionen,gesamtwohnungsbetrag=_bruchteile(summe)),'EUR_und_quoten','BGB_BETRIEBSKOSTEN_WOHNUNGSANTEILE',eingaben,[dict(operation='Je Position Gesamtkosten mal Wohnungsbezugswert/Gesamtbezugswert; daraus entstehende Wohnungsbeträge exakt summieren.')],eingaben.copy())
    ergebnis['hinweise']=['Nur §556a mit bereits rechtlich qualifiziertem Umlagemaßstab und umlagefähigen Kosten. Vorrang abweichender Vorschriften/Vereinbarungen, erfasster Verbräuche/Verursachung sowie besonderer WEG-Verteilung rechtlich bestimmen; unbilligen WEG-Schlüssel nicht ungeprüft übernehmen. Bezugswerte je Position müssen denselben vollständigen Abrechnungskreis und Zeitraum betreffen. Einheiten können zwischen Positionen verschieden sein, innerhalb einer Position identisch. Verbrauchsabhängige Mischschlüssel in disjunkte Kostenkomponenten aufteilen, keine Doppelzählung. Keine Bestimmung der Kostenumlagefähigkeit, Messwertschätzung, Leerstands-/Nutzerwechselzuordnung oder Heizkosten-Sondervorschriften.']
    return ergebnis


def betriebskosten_umstellung_mietherabsetzung(bisherige_zeitraummiete=None, bisher_enthaltener_kostenanteil=None, einordnungsnachweis=None):
    """Bisherige Miete um bislang enthaltene künftig gesondert umgelegte Betriebskosten herabsetzen."""
    miete,kosten=_geld(bisherige_zeitraummiete),_geld(bisher_enthaltener_kostenanteil); _text(einordnungsnachweis,'einordnungsnachweis')
    if kosten>miete:
        _fehler('bisher_enthaltener_kostenanteil','Enthaltener Kostenanteil darf bisherige Miete nicht übersteigen.')
    eingaben=dict(bisherige_zeitraummiete=bisherige_zeitraummiete,bisher_enthaltener_kostenanteil=bisher_enthaltener_kostenanteil,einordnungsnachweis=einordnungsnachweis)
    ergebnis=_geld_ergebnis(_subtrahieren(miete,kosten),'BGB_BETRIEBSKOSTEN_UMSTELLUNG_MIETHERABSETZUNG',eingaben,[dict(operation='Qualifiziert bislang enthaltenen künftig gesondert umgelegten Kostenanteil von Miete desselben Zeitraums abziehen.')])
    ergebnis['hinweise'].append('Nur §556a Absatz2 Satz3 nach qualifiziert zulässiger Umstellung der Umlage erfassten Verbrauchs/Verursachung. Kostenanteil und Miete gleiche Zeiteinheit, nicht Jahreskosten unmittelbar von Monatsmiete abziehen. Nur bisher tatsächlich in der Miete enthaltenen künftig gesonderten Anteil abziehen, keine Schätzung durch Bibliothek. Textform, rechtzeitige Erklärung vor Abrechnungsbeginn und Wirksamkeit gesondert.')
    return ergebnis
