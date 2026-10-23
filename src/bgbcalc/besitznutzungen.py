from .kalender import _auswahl, _ergebnis, _fehler, _text, _vorhanden
from .betraege import _geld, _wahrheitswert
from .zahlen import _addieren
from .zinsen import _bruchteile
from .reisezeitschwellen import _reise_utc_zeitpunkt

def besitz_nutzungswerte_im_haftungszeitraum(haftungsbeginn_utc=None, beginn_eingeschlossen=None, abrechnungsende_utc=None, nutzungen=None, einordnungsnachweis=None):
    """Qualifizierte Nutzungspositionen im maßgeblichen Haftungszeitraum auswählen und Werte nach gezogener und schuldhaft nicht gezogener Nutzung getrennt summieren."""
    beginn=_reise_utc_zeitpunkt(haftungsbeginn_utc,'haftungsbeginn_utc');ende=_reise_utc_zeitpunkt(abrechnungsende_utc,'abrechnungsende_utc')
    _wahrheitswert(beginn_eingeschlossen,'beginn_eingeschlossen');_text(einordnungsnachweis,'einordnungsnachweis');_vorhanden(nutzungen,'nutzungen')
    if ende<beginn: _fehler('abrechnungsende_utc','Ende darf nicht vor Beginn liegen.')
    if not isinstance(nutzungen,list) or len(nutzungen)>1000: _fehler('nutzungen','Liste0..1000 erforderlich.')
    namen=set();gewaehlt=[];gezogen=_geld('0');unterlassen=_geld('0')
    for p in nutzungen:
        if not isinstance(p,dict) or set(p)!={'nutzung_id','nutzungszeitpunkt_utc','nutzungsart','nutzungswert'}: _fehler('nutzungen','Genau Kennung, Zeitpunkt, Art und Wert erforderlich.')
        name=_text(p['nutzung_id'],'nutzung_id')
        if name in namen: _fehler('nutzung_id','Doppelte Kennung unzulässig.')
        namen.add(name);zeit=_reise_utc_zeitpunkt(p['nutzungszeitpunkt_utc'],'nutzungszeitpunkt_utc');_auswahl(p['nutzungsart'],'nutzungsart',('gezogen','schuldhaft_nichtgezogen'));betrag=_geld(p['nutzungswert'])
        if (zeit>beginn or beginn_eingeschlossen and zeit==beginn) and zeit<=ende:
            gewaehlt.append(name)
            if p['nutzungsart']=='gezogen': gezogen=_addieren(gezogen,betrag)
            else: unterlassen=_addieren(unterlassen,betrag)
    wert=dict(gezogener_nutzungswert=_bruchteile(gezogen),schuldhaft_nichtgezogener_nutzungswert=_bruchteile(unterlassen),gesamter_nutzungswert=_bruchteile(_addieren(gezogen,unterlassen)),beruecksichtigte_nutzung_ids=gewaehlt)
    eingaben = dict(haftungsbeginn_utc=haftungsbeginn_utc, beginn_eingeschlossen=beginn_eingeschlossen, abrechnungsende_utc=abrechnungsende_utc, nutzungen=nutzungen, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_BESITZ_NUTZUNGSWERTE_IM_HAFTUNGSZEITRAUM',eingaben,[dict(operation='Qualifizierte Nutzungspositionen im maßgeblichen Haftungszeitraum auswählen und Werte nach gezogener und schuldhaft nicht gezogener Nutzung getrennt summieren.')],eingaben.copy())
    ergebnis["hinweise"] = ['§§987/990,gegebenenfalls991I: qualifizierte Nutzungspositionen nach Haftungszeitraum auswählen, tatsächlich gezogene und schuldhaft nicht gezogene Werte getrennt summieren. Anwendungsfall, gegebenenfalls kumulative Verantwortlichkeit mittelbaren Besitzers991I, Bewertungsmaßstab und zeitliche Zuordnung extern. Keine automatische Bösgläubigkeit, Rechtshängigkeit oder Verschuldensentscheidung. Mehrtägige Nutzungsabschnitte an Haftungsgrenzen vorher rechtlich zutreffend aufteilen; kein pauschales Abstellen auf Buchungs-/Zahlungstag. UTC-Sekunden nur bei ausreichend genauer Normalisierung, keine Subsekunden abschneiden. Werte in Euro begründen keinen automatischen Geldersatz statt Naturherausgabe.988/993-Bereicherung und weitergehende Verzugshaftung gesondert.']
    return ergebnis

