from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _text

def werkwohnung_kuendigungstermin(fristfall=None, kuendigungszugang_am=None, ueberlassungsbeginn_am=None, qualifizierte_zugangsgrenze_am=None, einordnungsnachweis=None):
    """Werkmietwohnungs-Sonderfrist nach qualifizierter Dritte-Werktag-Grenze und Zehnjahresvergleich zum Monatsendtermin berechnen."""
    _auswahl(fristfall,'fristfall',('ersatzbedarf_576_1_1','arbeitsplatznaehe_576_1_2'))
    zugang=_datum(kuendigungszugang_am,'kuendigungszugang_am');beginn=_datum(ueberlassungsbeginn_am,'ueberlassungsbeginn_am')
    grenze=_datum(qualifizierte_zugangsgrenze_am,'qualifizierte_zugangsgrenze_am');_text(einordnungsnachweis,'einordnungsnachweis')
    if beginn>zugang: _fehler('ueberlassungsbeginn_am','Beginn darf nicht nach Zugang liegen.')
    if (grenze.year,grenze.month)!=(zugang.year,zugang.month) or grenze.day<3: _fehler('qualifizierte_zugangsgrenze_am','Dritte-Werktag-Grenze im Zugangsmonat erforderlich.')
    zehn=_frist(ueberlassungsbeginn_am,10,'jahre','tagesbeginn');unter=zugang<=zehn
    ende=None
    if fristfall=='arbeitsplatznaehe_576_1_2' or unter:
        monate=(1 if fristfall=='arbeitsplatznaehe_576_1_2' else 3)+int(zugang>grenze)
        ende=_frist(zugang.replace(day=1).isoformat(),monate,'monate','tagesbeginn').isoformat()
    wert=dict(zehnjahreszeitraum_letzter_tag=zehn.isoformat(),weniger_als_zehn_jahre_am_zugang=unter,zugangsgrenze_eingehalten=zugang<=grenze,rechnerischer_sonderbeendigungstag=ende)
    eingaben = dict(fristfall=fristfall, kuendigungszugang_am=kuendigungszugang_am, ueberlassungsbeginn_am=ueberlassungsbeginn_am, qualifizierte_zugangsgrenze_am=qualifizierte_zugangsgrenze_am, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'daten_und_wahrheitswerte','BGB_WERKWOHNUNG_KUENDIGUNGSTERMIN',eingaben,[dict(operation='Werkmietwohnungs-Sonderfrist nach qualifizierter Dritte-Werktag-Grenze und Zehnjahresvergleich zum Monatsendtermin berechnen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§576I: Nummer1 nur bei weniger als zehn Jahren Überlassung am Zugangstag; Nummer2 ohne diese Zehnjahresgrenze. Im qualifizierten Nummer1-Fall dritter Werktag zum Ende des übernächsten Monats, Nummer2 zum Ende des laufenden Monats. Bei Zugang nach Monatsgrenze verschiebt sich der früheste Termin um einen Monat. Zehnjahreszeitraum ab rechtlich qualifiziertem Tagesbeginn; intratägige Sonderfälle oder Unterbrechungen extern. Ist Nummer1 zeitlich ausgeschlossen, bleibt SonderterminNULL; daraus folgt keine generelle Unkündbarkeit und kein automatisch ersatzweise berechneter573c-Termin. Dienstverhältnis muss beendet und Ersatzbedarf/Arbeitsplatzbezug rechtlich festgestellt sein. Keine automatische Kündigungswirksamkeit, Widerspruchsentscheidung oder Feiertagsverschiebung des Mietendes.']
    return ergebnis

