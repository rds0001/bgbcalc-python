from .kalender import _ergebnis, _text, _fehler
from .betraege import _wahrheitswert
from .reisezeitschwellen import _reise_utc_zeitpunkt

def bereicherung_haftungszeitpunkte(empfang_utc=None, kenntnis_rechtsgrundmangel_utc=None, rechtshaengigkeit_utc=None, haftung_ab_empfang_qualifiziert=None, sonderfall_820_qualifiziert=None, kenntnis_erfolgsverfehlung_utc=None, einordnungsnachweis=None):
    """Frühestes qualifiziertes Haftungsereignis ab Empfang bestimmen; getrennten820II-Kenntniszeitpunkt ausweisen."""
    e=_reise_utc_zeitpunkt(empfang_utc,'empfang_utc');ab=_wahrheitswert(haftung_ab_empfang_qualifiziert,'haftung_ab_empfang_qualifiziert');s=_wahrheitswert(sonderfall_820_qualifiziert,'sonderfall_820_qualifiziert');_text(einordnungsnachweis,'einordnungsnachweis')
    if s and not ab:_fehler('haftung_ab_empfang_qualifiziert','820I setzt Empfangshaftung voraus.')
    if not s and kenntnis_erfolgsverfehlung_utc is not None:_fehler('kenntnis_erfolgsverfehlung_utc','Nur im820-Sonderfall verwenden.')
    zeiten=[(e,empfang_utc)] if ab else []
    for name,z in [('kenntnis_rechtsgrundmangel_utc',kenntnis_rechtsgrundmangel_utc),('rechtshaengigkeit_utc',rechtshaengigkeit_utc)]:
        if z is not None:
            t=_reise_utc_zeitpunkt(z,name);zeiten.append((max(e,t),empfang_utc if t<e else z))
    zins=None
    if s and kenntnis_erfolgsverfehlung_utc is not None:
        t=_reise_utc_zeitpunkt(kenntnis_erfolgsverfehlung_utc,'kenntnis_erfolgsverfehlung_utc');zins=empfang_utc if t<e else kenntnis_erfolgsverfehlung_utc
    wert=dict(beginn_verschaerfter_haftung_utc=min(zeiten)[1] if zeiten else None,zins_und_nutzungskenntnis_820_utc=zins)
    eingaben = dict(empfang_utc=empfang_utc, kenntnis_rechtsgrundmangel_utc=kenntnis_rechtsgrundmangel_utc, rechtshaengigkeit_utc=rechtshaengigkeit_utc, haftung_ab_empfang_qualifiziert=haftung_ab_empfang_qualifiziert, sonderfall_820_qualifiziert=sonderfall_820_qualifiziert, kenntnis_erfolgsverfehlung_utc=kenntnis_erfolgsverfehlung_utc, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'utc_zeitpunkte','BGB_BEREICHERUNG_HAFTUNGSZEITPUNKTE',eingaben,[dict(operation='Frühestes qualifiziertes Haftungsereignis ab Empfang bestimmen; getrennten820II-Kenntniszeitpunkt ausweisen.')],eingaben.copy())
    ergebnis["hinweise"] = ['818IV/819: frühesten einschlägigen Haftungszeitpunkt aus Rechtshängigkeit,819I-Kenntnis und qualifiziertem Empfangstatbestand berechnen; keine Haftung vor Empfang.820I setzt Haftung ab Empfang voraus;820II-Zins-/Nutzungsgrenze bleibt davon getrennt beim tatsächlichen Kenntniszeitpunkt. Fehlende Kenntnis erzeugt keinen fiktiven Zinsstart. Keine automatische Gleichsetzung mit dem Folgetag eines291-Prozesszinsbeginns; Umrechnung auf rechtlich qualifizierte Zinstage mit vorhandener Kalender-/Zinsrechnung gesondert. Keine pauschale Streichung jeder Entreicherung nach einem Datum: allgemeine Haftungsregeln, Zurechnung und820II-Nutzungsentreicherung unterscheiden.821-Verjährungseinrede hat keine weitere Betragsformel.822-Herausgabe des Dritten nur im rechtlich festgestellten Umfang des durch unentgeltliche Weitergabe verursachten Haftungsausschlusses, keine doppelte Forderung für denselben Vermögenswert.']
    return ergebnis

