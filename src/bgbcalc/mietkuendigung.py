"""Gesetzliche Monatsendtermine der Wohnraummietkündigung."""
from .betraege import _wahrheitswert
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _text


def wohnraummiete_kuendigungstermin(zugang_kuendigung=None, fristfall=None, qualifizierte_zugangsgrenze_am=None, ueberlassungsbeginn_am=None, kuendigung_nach_573a=None, fristnachweis=None):
    """§§573a/b/c/d: Monatsendtermin nach Zugangsschwelle und Vermieter-Jahresstaffel berechnen."""
    zugang=_datum(zugang_kuendigung,'zugang_kuendigung')
    _auswahl(fristfall,'fristfall',('mieter_standard','vermieter_standard','nebenraum_573b','moebliert_549_2_2','ausserordentlich_gesetzlich','ausserordentlich_moebliert'))
    _wahrheitswert(kuendigung_nach_573a,'kuendigung_nach_573a');_text(fristnachweis,'fristnachweis')
    if kuendigung_nach_573a and fristfall!='vermieter_standard':
        _fehler('kuendigung_nach_573a','Dreimonatsverlängerung nur im qualifizierten Vermieterfall.')
    jahre=None;zuschlag=0
    if fristfall=='vermieter_standard':
        beginn=_datum(ueberlassungsbeginn_am,'ueberlassungsbeginn_am')
        if beginn>zugang:
            _fehler('ueberlassungsbeginn_am','Überlassung darf nicht nach Kündigungszugang beginnen.')
        jahre=zugang.year-beginn.year-int((zugang.month,zugang.day)<(beginn.month,beginn.day))
        zuschlag=3*int(jahre>=5)+3*int(jahre>=8)+3*int(kuendigung_nach_573a)
    elif ueberlassungsbeginn_am is not None:
        _fehler('ueberlassungsbeginn_am','Überlassungsdauer nur im Vermieter-Standardfall angeben.')
    if fristfall in ('moebliert_549_2_2','ausserordentlich_moebliert'):
        if qualifizierte_zugangsgrenze_am is not None:
            _fehler('qualifizierte_zugangsgrenze_am','Im möblierten Sonderfall gilt die feste Grenze15, kein dritter Werktag.')
        grenze=zugang.replace(day=15);monate=1+int(zugang>grenze)
    else:
        grenze=_datum(qualifizierte_zugangsgrenze_am,'qualifizierte_zugangsgrenze_am')
        if (grenze.year,grenze.month)!=(zugang.year,zugang.month) or grenze.day<3:
            _fehler('qualifizierte_zugangsgrenze_am','Rechtlich maßgebliche dritte Werktagsgrenze im Zugangsmonat, frühestens am3.Tag, erforderlich.')
        monate=3+zuschlag+int(zugang>grenze)
    ende=_frist(zugang.replace(day=1).isoformat(),monate,'monate','tagesbeginn')
    eingaben=dict(zugang_kuendigung=zugang_kuendigung,fristfall=fristfall,qualifizierte_zugangsgrenze_am=qualifizierte_zugangsgrenze_am,ueberlassungsbeginn_am=ueberlassungsbeginn_am,kuendigung_nach_573a=kuendigung_nach_573a,fristnachweis=fristnachweis)
    wert=dict(zugangsgrenze_im_monat=grenze.isoformat(),zugangsgrenze_eingehalten=zugang<=grenze,vollendete_ueberlassungsjahre=jahre,verlaengerungsmonate=zuschlag,fruehester_beendigungstag=ende.isoformat())
    ergebnis=_ergebnis(wert,'datum_und_monate','BGB_WOHNRAUMMIETE_KUENDIGUNGSTERMIN',eingaben,[dict(operation='Zugangsgrenze3.Werktag oder15.prüfen; Monatsendtermin und gesetzliche Vermieterzuschläge5/8Jahre sowie573a berechnen.')],eingaben.copy())
    ergebnis['hinweise']=['Nur gesetzliche Standardfälle nach573bII/573cI,III und qualifizierter573a-Verlängerung. Rechtliche Voraussetzungen, Wirksamkeit, Sperrfristen, abweichende Vereinbarungen und574ff-Fortsetzung getrennt. qualifizierte_zugangsgrenze_am bezeichnet den rechtlich bestimmten letzten Zugangstag der Dritte-Werktag-Regel nach einschlägiger örtlicher Werktags-/Feiertagskonvention; ausdrücklich vorgeben, keine Annahme Montag bis Freitag. Fristnachweis muss diese Grenze belegen; keine automatische193Verschiebung. Überlassungsbeginn bildet einen rechtlich anrechenbaren zusammenhängenden Zeitraum ab Tagesbeginn ab; intratägige Grenzfälle/abweichender Anrechnungsbeginn gesondert qualifizieren. Vermieterzuschläge nach5/8vollendeten Jahren jeweils3Monate,573a zusätzlich3Monate. Keine Staffelverlängerung des gesonderten573bII-Teilkündigungstermins; Bauverzögerung nach573bIII separat. Möblierter549II2-Fall: Zugang bis15.einschließlich zum selben Monatsende, später zum nächsten. Beendigungstermin nicht wegen Wochenende/Feiertag verschieben. §573dII: ausserordentlich_gesetzlich verwendet unabhängig von der Überlassungsdauer die Dreimonatsgrundregel; ausserordentlich_moebliert verwendet die feste15-Tage-Zugangsschwelle. Keine Vermieterverlängerung nach5/8Jahren und keine zusätzliche573a-Dreimonatsfrist. Ein Grund für die außerordentliche Kündigung mit gesetzlicher Frist muss bereits vorliegen, etwa nach544 erst nach Ablauf der Dreißigjahreswartefrist. Beide Parteien können diese qualifizierten573d-Fälle verwenden; Voraussetzungen und573dI bleiben gesondert.']
    return ergebnis
