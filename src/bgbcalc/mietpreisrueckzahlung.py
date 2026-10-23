from .kalender import _ergebnis, _fehler, _text, _vorhanden
from .betraege import _geld, _wahrheitswert
from .zahlen import _addieren
from .zinsen import _bruchteile
from .reisezeitschwellen import _reise_utc_zeitpunkt

def mietpreisbremse_rueckzahlungsbetraege(ruegezugang_utc=None, rueckforderung_auf_spaetere_faelligkeit_beschraenkt=None, mietabschnitte=None, bereits_erstatteter_betrag=None, einordnungsnachweis=None):
    """Mietüberzahlungen nach qualifizierter Rüge-Fälligkeitsbeschränkung auswählen, abschnittsweise positive Differenzen summieren und geleistete Erstattung abziehen."""
    ruege=_reise_utc_zeitpunkt(ruegezugang_utc,'ruegezugang_utc');_wahrheitswert(rueckforderung_auf_spaetere_faelligkeit_beschraenkt,'rueckforderung_auf_spaetere_faelligkeit_beschraenkt');erstattet=_geld(bereits_erstatteter_betrag)
    _text(einordnungsnachweis,'einordnungsnachweis');_vorhanden(mietabschnitte,'mietabschnitte')
    if not isinstance(mietabschnitte,list) or len(mietabschnitte)>1000: _fehler('mietabschnitte','Liste0..1000 erforderlich.')
    namen=set();ids=[];summe=_geld('0')
    for p in mietabschnitte:
        if not isinstance(p,dict) or set(p)!={'abschnitt_id','faelligkeit_utc','tatsaechlich_gezahlte_miete','zulaessige_miete'}: _fehler('mietabschnitte','Genau Kennung, Fälligkeit, gezahlte und zulässige Miete erforderlich.')
        name=_text(p['abschnitt_id'],'abschnitt_id')
        if name in namen: _fehler('abschnitt_id','Jeden Mietabschnitt nur einmal angeben.')
        namen.add(name);faellig=_reise_utc_zeitpunkt(p['faelligkeit_utc'],'faelligkeit_utc');gezahlt=_geld(p['tatsaechlich_gezahlte_miete']);zulaessig=_geld(p['zulaessige_miete'])
        if not rueckforderung_auf_spaetere_faelligkeit_beschraenkt or faellig>ruege:
            ids.append(name);summe=_addieren(summe,max(_geld('0'),gezahlt-zulaessig))
    wert=dict(beruecksichtigte_abschnitt_ids=ids,ueberzahlung_vor_erstattung=_bruchteile(summe),verbleibender_rueckzahlungsbetrag=_bruchteile(max(_geld('0'),summe-erstattet)))
    eingaben = dict(ruegezugang_utc=ruegezugang_utc, rueckforderung_auf_spaetere_faelligkeit_beschraenkt=rueckforderung_auf_spaetere_faelligkeit_beschraenkt, mietabschnitte=mietabschnitte, bereits_erstatteter_betrag=bereits_erstatteter_betrag, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_MIETPREISBREMSE_RUECKZAHLUNGSBETRAEGE',eingaben,[dict(operation='Mietüberzahlungen nach qualifizierter Rüge-Fälligkeitsbeschränkung auswählen, abschnittsweise positive Differenzen summieren und geleistete Erstattung abziehen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§556gI/II: je qualifiziertem Mietabschnitt positive Differenz aus tatsächlich gezahlter und zulässiger Miete. Im Beschränkungsfall nur nach Rügezugang fällig gewordene Miete auswählen; Zahlungsdatum ersetzt Fälligkeit nicht. Bei identischem qualifiziertem Zeitpunkt liegt keine spätere Fälligkeit vor. Ausgewählte Überzahlungen addieren und zugehörige Erstattung bis auf null abziehen. Keine Verrechnung einer Unterzahlung in einem anderen Abschnitt, keine automatische Zins-/Verjährungsrechnung.30Monatsgrenze und Beendigung bei Rüge sind hier vorqualifiziert, nicht als automatisch gelöste Fristableitung ausgeben. Kein Aufsummieren mehrerer Vollmietgrenzen für Teilzahlungen desselben Abschnitts. UTC-Sekunden nur bei ausreichend genauer Normalisierung.']
    return ergebnis

