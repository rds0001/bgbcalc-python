from .kalender import _auswahl, _datum, _ergebnis, _frist, _tage_addieren, _text

def ankuendigung_vorlaufvergleich(vorlauffall=None, zugang_am=None, beabsichtigter_beginn_am=None, einordnungsnachweis=None):
    """Gesetzlichen Mindestvorlauf ab Zugang berechnen und Beginn nach vollständigem Fristablauf vergleichen."""
    _auswahl(vorlauffall,'vorlauffall',('modernisierung_555c','waermeumstellung_556c','mietaufrechnung_556b','zahlungsdienste_aenderung_675g','urlaubsprodukt_zahlung_486a','gastschul_information_651u','zahlung_vorabinformation_675x'))
    _datum(zugang_am,'zugang_am');beginn=_datum(beabsichtigter_beginn_am,'beabsichtigter_beginn_am');_text(einordnungsnachweis,'einordnungsnachweis')
    faelle={'modernisierung_555c':(3,'monate'),'waermeumstellung_556c':(3,'monate'),'mietaufrechnung_556b':(1,'monate'),'zahlungsdienste_aenderung_675g':(2,'monate'),'urlaubsprodukt_zahlung_486a':(2,'wochen'),'gastschul_information_651u':(2,'wochen'),'zahlung_vorabinformation_675x':(4,'wochen')}
    anzahl,einheit=faelle[vorlauffall];ablauf=_frist(zugang_am,anzahl,einheit,'ereignis');frueh=_tage_addieren(ablauf,1)
    wert=dict(vorlauf_ablauf_am=ablauf.isoformat(),fruehester_beginn_am=frueh.isoformat(),vorlauf_eingehalten=beginn>=frueh)
    eingaben = dict(vorlauffall=vorlauffall, zugang_am=zugang_am, beabsichtigter_beginn_am=beabsichtigter_beginn_am, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'daten_und_wahrheitswert','BGB_ANKUENDIGUNG_VORLAUFVERGLEICH',eingaben,[dict(operation='Gesetzlichen Mindestvorlauf ab Zugang berechnen und Beginn nach vollständigem Fristablauf vergleichen.')],eingaben.copy())
    ergebnis["hinweise"] = ['Mindestvorlauf ab tatsächlichem Zugang nach §§187I/188 vorwärts berechnen; der Zieltagesbeginn muss nach dem Ablaufdatum liegen. Nur kalendertäglicher Vorlauf, keine eigenständige qualitative Wirksamkeitsentscheidung und keine automatische Fristverschiebung nach§193. Bei verspäteter Ankündigung wird der tatsächlich beabsichtigte Beginn nicht automatisch geändert. §555cIV Bagatellausnahme, §556cI sonstige Umstellungsvoraussetzungen, §556bII zulässiger Forderungstyp und Textform, §675gII Zustimmung/Absätze3und4-Ausnahmen, §486a Zahlungsplan und §651uIII vollständige Information/angemessene Vorbereitung gesondert. §675xIII betrifft nur den Vierwochenvorlauf; direkte Zustimmung, wirksame Ausschlussvereinbarung und erforderliche Information sind gesonderte Voraussetzungen, kein automatischer Erstattungsausschluss. Untertägige Zeitpunktvereinbarungen sind nicht durch ein bloßes Datum abgebildet. Keine pauschale30-Tage-Monatsrechnung.']
    return ergebnis

