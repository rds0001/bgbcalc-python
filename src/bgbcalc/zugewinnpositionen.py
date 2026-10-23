"""Nettoaggregation privilegierter Erwerbe und datumsbegrenzte Hinzurechnungspositionen."""
from .betraege import _geld, _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler, _frist, _text, _vorhanden
from .zahlen import _addieren, _bruch, _subtrahieren
from .zinsen import _bruchteile


def zugewinn_anfangsvermoegen_positionssumme(anfangsaktivvermoegen=None, anfangsverbindlichkeiten=None, privilegierte_erwerbe=None, bewertungsnachweis=None):
    """§1374IbisIII: anfängliche und privilegierte Nettopositionen ohne Nullkappung addieren."""
    aktiv = _geld(anfangsaktivvermoegen)
    schulden = _geld(anfangsverbindlichkeiten)
    _vorhanden(privilegierte_erwerbe,'privilegierte_erwerbe')
    if not isinstance(privilegierte_erwerbe,list) or not 1 <= len(privilegierte_erwerbe) <= 10000:
        _fehler('privilegierte_erwerbe','Liste mit 1 bis 10000 qualifizierten Erwerbspositionen erforderlich; keine Erwerbe ausdrücklich als eine Nullposition.')
    summe = _bruch(0)
    nettoerwerbe=[]
    for position in privilegierte_erwerbe:
        if not isinstance(position,dict) or set(position) != {'erwerbswert','zugehoerige_verbindlichkeiten'}:
            _fehler('privilegierte_erwerbe','Genau erwerbswert und zugehoerige_verbindlichkeiten je Position erforderlich.')
        wert = _geld(position['erwerbswert'])
        lasten = _geld(position['zugehoerige_verbindlichkeiten'])
        netto = _subtrahieren(wert,lasten)
        nettoerwerbe.append(_bruchteile(netto));summe = _addieren(summe,netto)
    _text(bewertungsnachweis,'bewertungsnachweis')
    anfang = _subtrahieren(aktiv,schulden)
    eingaben = dict(anfangsaktivvermoegen=anfangsaktivvermoegen,anfangsverbindlichkeiten=anfangsverbindlichkeiten,privilegierte_erwerbe=privilegierte_erwerbe,bewertungsnachweis=bewertungsnachweis)
    wert = dict(urspruengliches_nettoanfangsvermoegen=_bruchteile(anfang),nettoerwerbe=nettoerwerbe,hinzuzurechnende_nettoerwerbssumme=_bruchteile(summe),anfangsvermoegenssumme=_bruchteile(_addieren(anfang,summe)))
    ergebnis = _ergebnis(wert,'EUR','BGB_ZUGEWINN_ANFANGSVERMOEGEN_POSITIONSSUMME',eingaben,[dict(operation='Anfängliche Verbindlichkeiten vom Anfangsaktivvermögen und zugehörige Erwerbsverbindlichkeiten von jedem privilegierten Erwerb abziehen; alle Nettowerte ohne Nullkappung addieren.')],eingaben.copy())
    ergebnis['hinweise'] = ['§1374III verlangt ausdrücklich Schuldenabzug auch über die Vermögenshöhe hinaus; ursprünglicher Nettowert, einzelne Nettoerwerbe und Gesamtsumme können negativ sein. Nur rechtlich privilegierte Erwerbe nachAbsatz2 eingeben: von Todes wegen/vorweggenommenes Erbrecht/Schenkung/Ausstattung, nach Güterstandseintritt und nicht den Umständen nach Einkünfte. Anfangsschulden und Erwerbsverbindlichkeiten nicht doppelt zuordnen. Werte und zugehörige Verbindlichkeiten nach rechtlich maßgeblichen Bewertungszeitpunkten und konsistenter gegebenenfalls bereits erforderlicher Kaufkraftanpassung vorqualifizieren; keine automatische Indexierung oder Bewertung nach§1376. Keine Erwerbe durch eine Nullposition mit Erwerbswert0 und Verbindlichkeiten0 ausdrücken. Keine automatische Privilegierungs-/Einkünfteentscheidung, keine§1380-Anrechnung und kein abschließender Zugewinnausgleich.']
    return ergebnis


def zugewinn_endvermoegen_positionssumme(endaktivvermoegen=None, endverbindlichkeiten=None, bezugsstichtag_am=None, vermoegensminderungen=None, bewertungsnachweis=None):
    """§1375: Nettoendvermögen plus qualifizierte nicht ausgeschlossene Minderungspositionen."""
    aktiv = _geld(endaktivvermoegen)
    schulden = _geld(endverbindlichkeiten)
    stichtag = _datum(bezugsstichtag_am,'bezugsstichtag_am')
    _vorhanden(vermoegensminderungen,'vermoegensminderungen')
    if not isinstance(vermoegensminderungen,list) or not 1 <= len(vermoegensminderungen) <= 10000:
        _fehler('vermoegensminderungen','Liste mit 1 bis 10000 qualifizierten Minderungspositionen erforderlich; keine Minderung ausdrücklich als eine Nullposition.')
    summe = _bruch(0)
    positionen=[]
    namen=[]
    for position in vermoegensminderungen:
        felder={'minderung_id','betrag','eingetreten_am','minderungsart','einverstaendnis_anderer'}
        if not isinstance(position,dict) or set(position) != felder:
            _fehler('vermoegensminderungen','Genau minderung_id, betrag, eingetreten_am, minderungsart und einverstaendnis_anderer erforderlich.')
        name = _text(position['minderung_id'],'minderung_id')
        if name in namen:
            _fehler('minderung_id','Denselben Minderungsbetrag nicht mehrfach aufführen.')
        namen.append(name)
        betrag = _geld(position['betrag'])
        datum = _datum(position['eingetreten_am'],'eingetreten_am')
        art = _text(position['minderungsart'],'minderungsart')
        _wahrheitswert(position['einverstaendnis_anderer'],'einverstaendnis_anderer')
        if art not in ['unentgeltliche_zuwendung','verschwendung','benachteiligung']:
            _fehler('minderungsart','Qualifizierte unentgeltliche_zuwendung, verschwendung oder benachteiligung erforderlich.')
        if datum > stichtag:
            _fehler('eingetreten_am','Vermögensminderung darf nicht nach dem maßgeblichen Bezugsstichtag liegen.')
        alt = False
        if stichtag.year-datum.year >= 10:
            alt = _frist(position['eingetreten_am'],10,'jahre','ereignis') <= stichtag
        einverstanden = position['einverstaendnis_anderer'] and art in ['unentgeltliche_zuwendung','verschwendung']
        beruecksichtigt = _bruch(0) if alt or einverstanden else betrag
        summe = _addieren(summe,beruecksichtigt)
        positionen.append(dict(minderung_id=name,hinzurechnungsbetrag=_bruchteile(beruecksichtigt)))
    _text(bewertungsnachweis,'bewertungsnachweis')
    netto = _subtrahieren(aktiv,schulden)
    eingaben = dict(endaktivvermoegen=endaktivvermoegen,endverbindlichkeiten=endverbindlichkeiten,bezugsstichtag_am=bezugsstichtag_am,vermoegensminderungen=vermoegensminderungen,bewertungsnachweis=bewertungsnachweis)
    wert = dict(nettoendvermoegen=_bruchteile(netto),hinzurechnungspositionen=positionen,hinzurechnungssumme=_bruchteile(summe),endvermoegenssumme=_bruchteile(_addieren(netto,summe)))
    ergebnis = _ergebnis(wert,'EUR','BGB_ZUGEWINN_ENDVERMOEGEN_POSITIONSSUMME',eingaben,[dict(operation='Nettoendvermögen auch unter null bilden; Minderungen mindestens zehn Jahre vor Bezugsstichtag sowie einverstandene Zuwendung/Verschwendung ausschließen, übrige qualifizierte Beträge addieren.')],eingaben.copy())
    ergebnis['hinweise'] = ['§1375IbisIII. Tatsächlichen Vermögensminderungsbetrag nach Eintritt des Güterstands und dessen Wert rechtlich qualifizieren, nicht ungeprüft Ausgaben-/Schenkungsbruttobetrag. Einwilligungs-/Einverständnisausschluss nachAbsatz3 gilt ausdrücklich für unentgeltliche Zuwendung und Verschwendung; eine als Nummer3 qualifizierte Benachteiligung wird nicht allein wegen dieses Eingabeflags ausgeschlossen. Qualifikation nachNummer3 muss einschließlich relevanter Umstände bereits belastbar sein. Mindestens zehn Jahre schließt Gleichheit ein; vorhandener Kalenderkern, keine3650-Tage-Pauschale. Bezugsstichtag für die konkrete§1375III-Berechnung rechtlich bestimmen, einschließlich einschlägiger Stichtagsregeln§1384/1387; keine freie Wahl. Minderungen/Schulden nicht mehrfach erfassen, überschneidende Tatbestände einmal. Endschulden dürfen Endaktiva übersteigen. Keine automatische Beweislastentscheidung, Bewertungs-/Kaufkraftanpassung oder Prüfung einer Benachteiligungsabsicht. Keine Minderungen durch eine Nullposition zum Bezugsstichtag ausdrücken. §1380-Sonderanrechnung und eingreifende Haftungsgrenzen nicht gelöst.']
    return ergebnis
