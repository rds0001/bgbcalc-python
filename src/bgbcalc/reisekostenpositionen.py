from .betraege import _geld, _wahrheitswert
from .betreuungsrechnung import _rechnungssumme
from .kalender import _ergebnis, _fehler, _text, _vorhanden
from .zahlen import _addieren, _bruch, _subtrahieren
from .zinsen import _bruchteile


def pauschalreise_zusatzkosten_informationsgrenze(kostenpositionen=None, einordnungsnachweis=None):
    """Zusatzkosten nach rechtzeitiger ordnungsgemäßer Information auswählen und getrennt summieren."""
    _vorhanden(kostenpositionen,'kostenpositionen')
    if not isinstance(kostenpositionen,list) or not 1<=len(kostenpositionen)<=1000:
        _fehler('kostenpositionen','Liste mit1bis1000 eindeutig zugeordneten Kostenpositionen erforderlich.')
    _text(einordnungsnachweis,'einordnungsnachweis');namen=set();einbezogen=_bruch(0);ausgeschlossen=_bruch(0)
    for position in kostenpositionen:
        if not isinstance(position,dict) or set(position)!={'kosten_id','betrag','rechtzeitig_ordnungsgemaess_informiert'}:
            _fehler('kostenpositionen','Genau kosten_id, betrag und rechtzeitig_ordnungsgemaess_informiert erforderlich.')
        name=_text(position['kosten_id'],'kosten_id')
        if name in namen:
            _fehler('kosten_id','Kostenposition darf nicht mehrfach erfasst werden.')
        namen.add(name);betrag=_geld(position['betrag']);_wahrheitswert(position['rechtzeitig_ordnungsgemaess_informiert'],'rechtzeitig_ordnungsgemaess_informiert')
        if position['rechtzeitig_ordnungsgemaess_informiert']:einbezogen=_addieren(einbezogen,betrag)
        else:ausgeschlossen=_addieren(ausgeschlossen,betrag)
    eingaben=dict(kostenpositionen=kostenpositionen,einordnungsnachweis=einordnungsnachweis)
    ergebnis=_ergebnis(dict(nach_informationsgrenze_einbezogene_kosten=_bruchteile(einbezogen),wegen_information_ausgeschlossene_kosten=_bruchteile(ausgeschlossen)),'EUR','BGB_PAUSCHALREISE_ZUSATZKOSTEN_INFORMATIONSGRENZE',eingaben,[dict(operation='Kosten mit rechtzeitiger ordnungsgemäßer Vorabinformation summieren; ausgeschlossene Kosten gesondert ausweisen.')],eingaben.copy())
    ergebnis['hinweise']=['§651dII: zusätzliche Gebühren, Entgelte und sonstige Kosten; rechtzeitig bedeutet vor Abgabe der Vertragserklärung des Reisenden, nicht bloß vor Bestätigung des Veranstalters. Inhaltlich ordnungsgemäße Information nach dem verwiesenen EGBGB rechtlich vorqualifizieren; die Library prüft kein Informationsformular. Einbeziehung ist nur diese numerische Teilgrenze, kein Nachweis sämtlicher Anspruchsvoraussetzungen oder Vertragswirksamkeit. Positionen müssen im Übrigen der maßgeblichen Reise zugeordnet und überschneidungsfrei sein; bereits gezahlte Beträge separat. Keine Zusatzkosten ausdrücklich als einzelne Nullposition, keine fehlende Liste.']
    return ergebnis


def pauschalreise_notbeherbergungskosten(nachtkosten=None, dreinaechtegrenze_anwendbar=None, einordnungsnachweis=None):
    """Notwendige Nachtkosten chronologisch summieren, gegebenenfalls auf die ersten drei Nächte begrenzen."""
    _vorhanden(nachtkosten,'nachtkosten')
    if not isinstance(nachtkosten,list) or len(nachtkosten)>10000:
        _fehler('nachtkosten','Chronologische Liste mit0bis10000 Nachtbeträgen erforderlich.')
    gesamt=_rechnungssumme(nachtkosten,'nachtkosten') if nachtkosten else _bruch(0)
    _wahrheitswert(dreinaechtegrenze_anwendbar,'dreinaechtegrenze_anwendbar');_text(einordnungsnachweis,'einordnungsnachweis')
    anzahl=min(len(nachtkosten),3) if dreinaechtegrenze_anwendbar else len(nachtkosten)
    beruecksichtigt=_rechnungssumme(nachtkosten[:anzahl],'nachtkosten') if anzahl else _bruch(0)
    eingaben=dict(nachtkosten=nachtkosten,dreinaechtegrenze_anwendbar=dreinaechtegrenze_anwendbar,einordnungsnachweis=einordnungsnachweis)
    wert=dict(anzahl_erfasster_naechte=len(nachtkosten),anzahl_beruecksichtigter_naechte=anzahl,kosten_im_qualifizierten_umfang=_bruchteile(beruecksichtigt),kosten_ausserhalb_dreinaechtegrenze=_bruchteile(_subtrahieren(gesamt,beruecksichtigt)))
    ergebnis=_ergebnis(wert,'EUR_und_naechte','BGB_PAUSCHALREISE_NOTBEHERBERGUNGSKOSTEN',eingaben,[dict(operation='Chronologisch notwendige Nachtkosten summieren; bei anwendbarer Dreinächtebegrenzung nur die ersten drei Nächte berücksichtigen, Rest gesondert.')],eingaben.copy())
    ergebnis['hinweise']=['§651kIV/V: nur qualifizierte notwendige Beherbergung wegen unmöglicher vertraglicher Rückbeförderung infolge unvermeidbarer außergewöhnlicher Umstände. Nachtkosten chronologisch ab erster notwendiger Nacht vollständig eingeben, auch eine kostenlose Nacht als0, damit keine spätere Nacht an ihre Stelle rückt. Bei anwendbarer Begrenzung keine Auswahl der teuersten drei Nächte. FALSE nur nach qualifizierter Ausnahme651kV; dann sämtliche eingegebenen Nächte rechtlich dem anderweitig maßgeblichen notwendigen Umfang zuordnen, keine unbegrenzte Hotelzusage. Vorrangige EU-Regelungen, persönliche Voraussetzungen/48Stundeninformation, Gleichwertigkeit der Unterkunft und bereits gezahlte Kosten separat. Keine Cent-Rundung und keine automatische Rückzahlung oder Verdoppelung schon übernommener Kosten.']
    return ergebnis
