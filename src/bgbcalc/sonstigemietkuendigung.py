"""Gesetzliche Kündigungstermine sonstiger Mietsachen nach §580a."""
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _tage_addieren, _text


def sonstige_miete_kuendigungstermin(zugang_kuendigung=None, fristfall=None, qualifizierte_zugangsgrenze_am=None, fristnachweis=None):
    """Tages-, Wochen-, Monats-, Vierteljahres- und Dreitagesgrundregel nach580a."""
    tag=_datum(zugang_kuendigung,'zugang_kuendigung')
    _auswahl(fristfall,'fristfall',('tagesmiete','grundstueck_wochen','grundstueck_monate','gewerblich_unbebaut_monate','geschaeftsraeume','beweglich_digital_laenger'))
    _text(fristnachweis,'fristnachweis')
    grenze=None
    if fristfall in ('tagesmiete','beweglich_digital_laenger'):
        if qualifizierte_zugangsgrenze_am is not None:
            _fehler('qualifizierte_zugangsgrenze_am','Bei fester Tagesfrist keine ungenutzte Werktagsgrenze eingeben.')
        ende=_tage_addieren(tag,1 if fristfall=='tagesmiete' else 3)
    else:
        grenze=_datum(qualifizierte_zugangsgrenze_am,'qualifizierte_zugangsgrenze_am')
        if fristfall=='grundstueck_wochen':
            montag=_tage_addieren(tag,-tag.weekday());samstag=_tage_addieren(montag,5)
            if not montag<=grenze<=samstag:
                _fehler('qualifizierte_zugangsgrenze_am','Erste Werktagsgrenze muss in der Zugangswoche Montag bis Samstag liegen.')
            ende=_tage_addieren(samstag,7 if tag>grenze else 0)
        elif fristfall=='geschaeftsraeume':
            monat=3*((tag.month-1)//3)+1
            if grenze.year!=tag.year or grenze.month!=monat or grenze.day<3:
                _fehler('qualifizierte_zugangsgrenze_am','Dritte Werktagsgrenze im ersten Monat des Zugangsquartals erforderlich.')
            ende=_frist(tag.replace(month=monat,day=1).isoformat(),6+3*int(tag>grenze),'monate','tagesbeginn')
        else:
            if (grenze.year,grenze.month)!=(tag.year,tag.month) or grenze.day<3:
                _fehler('qualifizierte_zugangsgrenze_am','Dritte Werktagsgrenze im Zugangsmonat erforderlich.')
            ende=_frist(tag.replace(day=1).isoformat(),3+int(tag>grenze),'monate','tagesbeginn')
            if fristfall=='gewerblich_unbebaut_monate':
                monat=3*((ende.month-1)//3)+1
                ende=_frist(ende.replace(month=monat,day=1).isoformat(),3,'monate','tagesbeginn')
    eingaben=dict(zugang_kuendigung=zugang_kuendigung,fristfall=fristfall,qualifizierte_zugangsgrenze_am=qualifizierte_zugangsgrenze_am,fristnachweis=fristnachweis)
    wert=dict(fruehester_beendigungstag=ende.isoformat(),zugangsgrenze=None if grenze is None else grenze.isoformat(),zugangsgrenze_eingehalten=None if grenze is None else tag<=grenze)
    ergebnis=_ergebnis(wert,'daten','BGB_SONSTIGE_MIETE_KUENDIGUNGSTERMIN',eingaben,[dict(operation='Normfall580a bestimmt Mindestvorlauf und Bindung an Tages-, Samstags-, Monats- oder Quartalsende; qualifizierte Zugangsschwelle entscheidet aktuellen oder nächsten Ausgangszeitraum.')],eingaben.copy())
    ergebnis['hinweise']=['Nur rechtlich qualifizierte gesetzliche Grundfälle580a, keine allgemeine Wohnraummietkündigung. tagesmiete umfasst580aI1/III1; grundstueck_wochen und grundstueck_monate jeweilsI2/I3, gewerblich_unbebaut_monate zusätzlich Quartalsbindung; geschaeftsraeume stetsAbsatz2; beweglich_digital_laenger Absatz3Nummer2. Bemessungszeitraum ist nicht automatisch Zahlungsrhythmus. Zugangsschwelle anhand einschlägiger örtlicher Werktags-/Feiertags- und Zugangsregeln ausdrücklich vorgeben; kein pauschaler Montag-bis-Freitag-Kalender. Feste Tagesregeln benötigen keine Werktagsschwelle. Beendigungstermine nicht nach193 verschieben. Absatz4 überträgt nurI3/II/III2 auf entsprechende außerordentliche Kündigung mit gesetzlicher Frist; Voraussetzungen extern qualifizieren. Befristung, abweichende Vereinbarungen und spezielle Verbrauchervertragsregeln für digitale Produkte gesondert.']
    return ergebnis
