from .betraege import _wahrheitswert
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _text, _vorhanden

def rechtsverfolgung_sondergrundfrist(fristfall=None, ereignis_am=None, einordnungsnachweis=None):
    """Gesetzlich ausgewählte Ein- oder Dreimonats-Ereignisgrundfrist mit vorhandenem Kalenderkern berechnen."""
    faelle = {'eilverfahren_zustellung_204': 1, 'behoerdliche_vorentscheidung_204': 3, 'gerichtsstandsbestimmung_204': 3, 'verbandsunterlassung_zustellung_204a': 1}
    _auswahl(fristfall,'fristfall',tuple(faelle))
    _text(einordnungsnachweis,'einordnungsnachweis')
    wert = dict(rechnerisches_fristende=_frist(ereignis_am,faelle[fristfall],'monate','ereignis').isoformat())
    eingaben = dict(fristfall=fristfall, ereignis_am=ereignis_am, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'datum','BGB_RECHTSVERFOLGUNG_SONDERGRUNDFRIST',eingaben,[dict(operation='Gesetzlich ausgewählte Ein- oder Dreimonats-Ereignisgrundfrist mit vorhandenem Kalenderkern berechnen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§204I9: maßgebliche Verkündung oder Zustellung an Gläubiger, danach Monatsfrist zur Zustellung an Schuldner.204I12: Erledigung des behördlichen Gesuchs, danach drei Monate für Klage/zulässigen Folgeantrag;204I13 entsprechend nach Erledigung des Gerichtsstandsbestimmungsgesuchs.204aI2: maßgebliche Verkündung oder Zustellung der einstweiligen Verfügung an Antragsteller, danach Monat zur Zustellung an Antragsgegner. Fristauslöser rechtlich vorqualifizieren, nicht Antragseinreichung oder Kenntnis frei einsetzen. Nur Grundfristen: entsprechende206/210/211-Korrekturen nach204III für die dort genannten204-Fälle zusätzlich, keine ungeprüfte Übertragung dieses Verweises auf204aI2.193 bei feststehender Anwendung gesondert. Keine automatische Hemmungs-/Rückwirkungsentscheidung, keine Berechnung aus dem KapMuG außerhalb desBGB.']
    return ergebnis

def verbandsklage_hemmungsnachlauf(verfahrensende_am=None, teilnahmefall=None, teilnahmeende_am=None, einordnungsnachweis=None):
    """Frühestes einschlägiges Verfahrens-/Teilnahmeende bestimmen und sechsmonatigen Hemmungsnachlauf berechnen."""
    _wahrheitswert(teilnahmefall,'teilnahmefall');_text(einordnungsnachweis,'einordnungsnachweis')
    ereignisse=[]
    if verfahrensende_am is not None:
        ereignisse.append(_datum(verfahrensende_am,'verfahrensende_am'))
    if teilnahmeende_am is not None:
        if not teilnahmefall:
            _fehler('teilnahmeende_am','Teilnahmeende nur im qualifizierten Teilnahmefall eingeben.')
        ereignisse.append(_datum(teilnahmeende_am,'teilnahmeende_am'))
    if not ereignisse:
        _vorhanden(None,'beendendes_ereignis')
    wert = dict(rechnerisches_nachlaufende=_frist(min(ereignisse).isoformat(),6,'monate','ereignis').isoformat())
    eingaben = dict(verfahrensende_am=verfahrensende_am, teilnahmefall=teilnahmefall, teilnahmeende_am=teilnahmeende_am, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'datum','BGB_VERBANDSKLAGE_HEMMUNGSNACHLAUF',eingaben,[dict(operation='Frühestes einschlägiges Verfahrens-/Teilnahmeende bestimmen und sechsmonatigen Hemmungsnachlauf berechnen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§204aIII: sechsmonatiger Nachlauf ab rechtskräftiger Entscheidung/anderweitigem Verfahrensende entsprechend204II1; im qualifizierten Teilnahmefall auch ab Ende der Teilnahme, insbesondere Rücknahme der Registeranmeldung. Wenn beide einschlägigen Ereignisse feststehen, maßgeblich ist das frühere Nachlaufende. Kein Stillstand durch Nichtbetreiben als zusätzlicher204a-Auslöser: der Verweis nennt nur204II1. Teilnahmefall ausschließlich204aI1Nr3/4 oderII2, gegebenenfalls gleichgestellte UnternehmerIV; keine beliebige Nichtteilnahme bei Unterlassungsklage. Ohne bekanntes Endereignis kein fiktives Ende des laufenden Schutzes. Keine automatische Addition des Ergebnisses zur Verjährungsfrist: normierte tatsächliche Hemmungstage und209 gesondert berechnen.']
    return ergebnis

