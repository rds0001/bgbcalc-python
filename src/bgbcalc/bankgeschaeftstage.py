"""Bankgeschäftstagsoperationen auf einem ausdrücklich qualifizierten Geschäftskalender."""
from bisect import bisect_left, bisect_right
from .betraege import _wahrheitswert
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _ganzzahl, _text, _vorhanden


def _bankkalender(kalender):
    _vorhanden(kalender,'bankkalender')
    if not isinstance(kalender,dict) or set(kalender)!={'erster_kalendertag','letzter_kalendertag','geschaeftstage'}:
        _fehler('bankkalender','Genau erster_kalendertag, letzter_kalendertag und geschaeftstage erforderlich.')
    erster=_datum(kalender['erster_kalendertag'],'erster_kalendertag');letzter=_datum(kalender['letzter_kalendertag'],'letzter_kalendertag')
    if letzter<erster:
        _fehler('bankkalender','Kalenderende darf nicht vor Kalenderbeginn liegen.')
    tage=kalender['geschaeftstage'];_vorhanden(tage,'geschaeftstage')
    if not isinstance(tage,list) or not 1<=len(tage)<=10000:
        _fehler('geschaeftstage','Geordnete Liste mit1bis10000 Geschäftstagen erforderlich.')
    tage=[_datum(t,'geschaeftstage') for t in tage]
    if any(t<erster or t>letzter for t in tage) or any(a>=b for a,b in zip(tage,tage[1:])):
        _fehler('geschaeftstage','Geschäftstage müssen streng aufsteigend, eindeutig und innerhalb des belegten Kalenders liegen.')
    return erster,letzter,tage


def _banktermin(tag,kalender,richtung,anzahl=1):
    erster,letzter,tage=kalender
    if not erster<=tag<=letzter:
        _fehler('bankkalender','Bezugsdatum liegt außerhalb des belegten Kalenders.')
    index=bisect_left(tage,tag) if richtung=='ab' else bisect_right(tage,tag)+anzahl-1 if richtung=='nach' else bisect_left(tage,tag)-anzahl
    if not 0<=index<len(tage):
        _fehler('bankkalender','Kalender deckt den gesuchten Geschäftstag nicht ab; keine Fortschreibung aus vermuteten Wochenregeln.')
    return tage[index]


def zahlungsauftrag_zugangstage(zugang_am=None, nach_annahmeschluss=None, vereinbarter_ausfuehrungstag_am=None, bankkalender=None, kalendernachweis=None):
    """Wirksamkeitszugang und für die Ausführungsfrist maßgeblichen Zugangstag getrennt bestimmen."""
    tag=_datum(zugang_am,'zugang_am');_wahrheitswert(nach_annahmeschluss,'nach_annahmeschluss');_text(kalendernachweis,'kalendernachweis')
    kalender=_bankkalender(bankkalender);wirksam=_banktermin(tag,kalender,'ab')
    if vereinbarter_ausfuehrungstag_am is not None:
        termin=_datum(vereinbarter_ausfuehrungstag_am,'vereinbarter_ausfuehrungstag_am')
        if termin<tag or nach_annahmeschluss:
            _fehler('vereinbarter_ausfuehrungstag_am','Termin nicht vor tatsächlichem Zugang; Terminauftrag nicht mit ungenutzter Annahmeschlussverschiebung vermischen.')
        ausfuehrung=_banktermin(termin,kalender,'ab')
    elif nach_annahmeschluss:
        if tag not in kalender[2]:
            _fehler('nach_annahmeschluss','Annahmeschlussverschiebung setzt einen tatsächlichen Geschäftstag voraus.')
        ausfuehrung=_banktermin(tag,kalender,'nach')
    else:
        ausfuehrung=wirksam
    eingaben=dict(zugang_am=zugang_am,nach_annahmeschluss=nach_annahmeschluss,vereinbarter_ausfuehrungstag_am=vereinbarter_ausfuehrungstag_am,bankkalender=bankkalender,kalendernachweis=kalendernachweis)
    ergebnis=_ergebnis(dict(wirksamkeitszugangstag=wirksam.isoformat(),zugangstag_fuer_ausfuehrungsfrist=ausfuehrung.isoformat()),'daten','BGB_ZAHLUNGSAUFTRAG_ZUGANGSTAGE',eingaben,[dict(operation='Nichtgeschäftstag auf nächsten Geschäftstag abbilden; wirksamen Annahmeschluss beziehungsweise vereinbarten Termin nur für den Ausführungsfristbeginn berücksichtigen.')],eingaben.copy())
    ergebnis['hinweise']=['§675n: Geschäftskalender des Zahlungsdienstleisters des Zahlers für den konkreten Vorgang vollständig im angegebenen Intervall vorgeben. Keine pauschale Werktags-/Feiertagskonvention. nach_annahmeschluss bedeutet nach einem wirksam festgelegten Zeitpunkt nahe Geschäftstagsende, nicht bloß außerhalb beliebiger Öffnungszeiten. Diese Verschiebung gilt nur für675sI, nicht pauschal für sämtliche Wirkungen des Zugangs. Bei vereinbartem Termin675nII diesen maßgeblichen Tag angeben, nach_annahmeschlussFALSE; tatsächlicher Zugang bleibt getrennt. Uhrzeiten, Zeitzonen und Intraday-Reihenfolge extern qualifizieren.']
    return ergebnis


def zahlung_ausfuehrungsfristende(zugangstag_fuer_ausfuehrungsfrist=None, fristfall=None, vereinbarte_geschaeftstage=None, bankkalender=None, kalendernachweis=None):
    """Ein-/Zweitagesregel oder vereinbarte EWR-Nicht-Euro-Frist bis vier Geschäftstage."""
    tag=_datum(zugangstag_fuer_ausfuehrungsfrist,'zugangstag_fuer_ausfuehrungsfrist')
    _auswahl(fristfall,'fristfall',('standard','papier_verlaengerung','ewr_nichteuro_vereinbart'));_text(kalendernachweis,'kalendernachweis')
    if fristfall=='ewr_nichteuro_vereinbart':
        anzahl=_ganzzahl(vereinbarte_geschaeftstage,'vereinbarte_geschaeftstage',1,4)
    else:
        if vereinbarte_geschaeftstage is not None:
            _fehler('vereinbarte_geschaeftstage','Im gesetzlichen Standard-/Papierfall keine ungenutzte vereinbarte Tageszahl eingeben.')
        anzahl=2 if fristfall=='papier_verlaengerung' else 1
    kalender=_bankkalender(bankkalender)
    if tag not in kalender[2]:
        _fehler('zugangstag_fuer_ausfuehrungsfrist','Bereits nach675n qualifizierter Zugangsgeschäftstag erforderlich.')
    ende=_banktermin(tag,kalender,'nach',anzahl)
    eingaben=dict(zugangstag_fuer_ausfuehrungsfrist=zugangstag_fuer_ausfuehrungsfrist,fristfall=fristfall,vereinbarte_geschaeftstage=vereinbarte_geschaeftstage,bankkalender=bankkalender,kalendernachweis=kalendernachweis)
    ergebnis=_ergebnis(dict(anzahl_geschaeftstage=anzahl,spaetester_eingangstag=ende.isoformat()),'datum_und_anzahl','BGB_ZAHLUNG_AUSFUEHRUNGSFRISTENDE',eingaben,[dict(operation='Nach dem qualifizierten Zugangsgeschäftstag die gesetzliche oder wirksam vereinbarte Zahl von Geschäftstagen zählen.')],eingaben.copy())
    ergebnis['hinweise']=['§675sI: spätester Eingang beim Zahlungsdienstleister des Empfängers. standard=ein Geschäftstag; papier_verlaengerung=nur wirksam genutzte Verlängerung der Standardfrist um einen Geschäftstag. ewr_nichteuro_vereinbart=nur wirksame Vereinbarung von1bis4Geschäftstagen im einschlägigen EWR-Nicht-Euro-Fall; kein zusätzlicher Papiertag auf diese Vier-Tages-Frist. Qualifizierter Geschäftskalender und675n-Zugangstag vorgeben.675sII-Empfängerauslösung und Ausnahmen675sIII/675dVI separat; keine automatische Gutschrift-/Wertstellungsentscheidung.']
    return ergebnis


def zahlung_geschaeftstags_grenztermin(fristfall=None, bezugstag_am=None, bankkalender=None, kalendernachweis=None):
    """Vortag, nächster Geschäftstag oder zehnter Geschäftstag im qualifizierten Zahlungsfall."""
    _auswahl(fristfall,'fristfall',('lastschrift_widerruf_675p','terminauftrag_widerruf_675p','nichtautorisiert_erstattung_675u','erstattung_entscheidung_675x','bareinzahlung_nichtverbraucher_675t'))
    tag=_datum(bezugstag_am,'bezugstag_am');_text(kalendernachweis,'kalendernachweis');kalender=_bankkalender(bankkalender)
    vorher=fristfall in ('lastschrift_widerruf_675p','terminauftrag_widerruf_675p')
    ende=_banktermin(tag,kalender,'vor' if vorher else 'nach',10 if fristfall=='erstattung_entscheidung_675x' else 1)
    eingaben=dict(fristfall=fristfall,bezugstag_am=bezugstag_am,bankkalender=bankkalender,kalendernachweis=kalendernachweis)
    ergebnis=_ergebnis(dict(rechnerischer_grenztermin=ende.isoformat()),'datum','BGB_ZAHLUNG_GESCHAEFTSTAGS_GRENZTERMIN',eingaben,[dict(operation='Streng vor beziehungsweise nach dem qualifizierten Bezugstag im belegten Geschäftskalender suchen; kein zusätzlicher Zwischenschritt bei Nichtgeschäftstag.')],eingaben.copy())
    ergebnis['hinweise']=['675pII/III: letzter Geschäftstag vor vereinbarter Fälligkeit beziehungsweise vereinbartem Ausführungstag, nicht vor einem eigenständig verschobenen Termin; spätere Widerrufsvereinbarungen gesondert.675u: Bezugstag ist früheste maßgebliche Anzeige oder anderweitige Kenntnis, äußerste Erstattungs-/Kontokorrekturfrist, unverzüglich bleibt zusätzlich; qualifizierte Betrugsverdachtsausnahme außerhalb.675xV: zehn Geschäftstage nach Zugang des Erstattungsverlangens, Anspruch und Vier-/Achtwochenregeln getrennt.675tII: Nichtverbraucher-Bareinzahlung in Kontowährung, spätestens folgender Geschäftstag; Verbraucherregel unverzüglich nicht übertragen.675dVI-/Spezialausnahmen vorqualifizieren. Jeweils Kalender des verpflichteten Zahlungsdienstleisters für diesen Vorgang vollständig angeben. Ergebnis bezeichnet Tagesablauf; Uhrzeiten/Zeitzonen extern normalisieren.']
    return ergebnis
