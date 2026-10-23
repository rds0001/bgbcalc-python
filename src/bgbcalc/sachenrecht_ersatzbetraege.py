"""Betragsgrenzen und Ersatzrechnungen des Sachenrechts."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _text
from .zahlen import _addieren, _bruch, _subtrahieren

def besitzhaftung_verantwortungsgrenze(schaden_nach_989=None, verantwortungsbetrag_gegenueber_mittelbarem_besitzer=None, anwendungsfall_qualifiziert=None, bewertungsnachweis=None):
    """Schadensbetrag nach§989 auf Verantwortungsbetrag gegenüber dem mittelbaren Besitzer begrenzen."""
    betrag_eins = _geld(schaden_nach_989)
    betrag_zwei = _geld(verantwortungsbetrag_gegenueber_mittelbarem_besitzer)
    _wahrheitswert(anwendungsfall_qualifiziert, "anwendungsfall_qualifiziert")
    _text(bewertungsnachweis, "bewertungsnachweis")
    eingaben = dict(schaden_nach_989=schaden_nach_989, verantwortungsbetrag_gegenueber_mittelbarem_besitzer=verantwortungsbetrag_gegenueber_mittelbarem_besitzer, anwendungsfall_qualifiziert=anwendungsfall_qualifiziert, bewertungsnachweis=bewertungsnachweis)
    wert = min(betrag_eins, betrag_zwei) if anwendungsfall_qualifiziert else None
    ergebnis = _geld_ergebnis(wert, "BGB_BESITZHAFTUNG_VERANTWORTUNGSGRENZE", eingaben, [dict(operation='Schadensbetrag nach§989 auf Verantwortungsbetrag gegenüber dem mittelbaren Besitzer begrenzen.')])
    ergebnis["hinweise"].append('Nur qualifizierter Fall§991 Absatz2 mit bei Besitzerwerb gutgläubigem Besitzer. Beide Beträge betreffen denselben Schaden; keine eigenständige Haftungs-/Verschuldensprüfung.')
    return ergebnis

def niessbrauch_uebermassfruechte_ersatz(wert_der_uebermassfruechte=None, wert_der_beeintraechtigten_eigenen_nutzungen=None, anwendungsfall_qualifiziert=None, bewertungsnachweis=None):
    """Fruchtwert um Beeinträchtigung der dem Nießbraucher gebührenden Nutzungen mindern, mindestens null."""
    betrag_eins = _geld(wert_der_uebermassfruechte)
    betrag_zwei = _geld(wert_der_beeintraechtigten_eigenen_nutzungen)
    _wahrheitswert(anwendungsfall_qualifiziert, "anwendungsfall_qualifiziert")
    _text(bewertungsnachweis, "bewertungsnachweis")
    eingaben = dict(wert_der_uebermassfruechte=wert_der_uebermassfruechte, wert_der_beeintraechtigten_eigenen_nutzungen=wert_der_beeintraechtigten_eigenen_nutzungen, anwendungsfall_qualifiziert=anwendungsfall_qualifiziert, bewertungsnachweis=bewertungsnachweis)
    wert = max(_subtrahieren(betrag_eins, betrag_zwei), _bruch(0)) if anwendungsfall_qualifiziert else None
    ergebnis = _geld_ergebnis(wert, "BGB_NIESSBRAUCH_UEBERMASSFRUECHTE_ERSATZ", eingaben, [dict(operation='Fruchtwert um Beeinträchtigung der dem Nießbraucher gebührenden Nutzungen mindern, mindestens null.')])
    ergebnis["hinweise"].append('Nur wenn Verwendung zur Wiederherstellung nicht verlangt wird. Eingaben rechtlich bewertete, kausal zusammengehörige Werte. Eigenständige Verschuldenshaftung, Sicherheitsleistung und Wiederherstellungsalternative nicht eingerechnet.')
    return ergebnis

def niessbrauch_einloesungskapital(tilgungskapital=None, einloesungspraemie=None, anwendungsfall_qualifiziert=None, bewertungsnachweis=None):
    """Tilgungskapital und Einlösungsprämie zu Kapitalbetrag addieren."""
    betrag_eins = _geld(tilgungskapital)
    betrag_zwei = _geld(einloesungspraemie)
    _wahrheitswert(anwendungsfall_qualifiziert, "anwendungsfall_qualifiziert")
    _text(bewertungsnachweis, "bewertungsnachweis")
    eingaben = dict(tilgungskapital=tilgungskapital, einloesungspraemie=einloesungspraemie, anwendungsfall_qualifiziert=anwendungsfall_qualifiziert, bewertungsnachweis=bewertungsnachweis)
    wert = _addieren(betrag_eins, betrag_zwei) if anwendungsfall_qualifiziert else None
    ergebnis = _geld_ergebnis(wert, "BGB_NIESSBRAUCH_EINLOESUNGSKAPITAL", eingaben, [dict(operation='Tilgungskapital und Einlösungsprämie zu Kapitalbetrag addieren.')])
    ergebnis["hinweise"].append('Nur Einlösung des vom Nießbrauch betroffenen Papiers. Einlösungsprämie wird als Kapital, nicht Zinsertrag behandelt; separat fällige Zinsen nicht als Prämie eingeben. Keine Bewertung oder automatische Auszahlung an den Nießbraucher.')
    return ergebnis

def hypothek_schuldneruebergangsbetrag(hypothekarisch_gesicherte_befriedigung=None, ersatzanspruch_gegen_eigentuemer=None, anwendungsfall_qualifiziert=None, bewertungsnachweis=None):
    """Gesicherten Befriedigungsbetrag auf rechtlich bestehenden Ersatzanspruch begrenzen."""
    betrag_eins = _geld(hypothekarisch_gesicherte_befriedigung)
    betrag_zwei = _geld(ersatzanspruch_gegen_eigentuemer)
    _wahrheitswert(anwendungsfall_qualifiziert, "anwendungsfall_qualifiziert")
    _text(bewertungsnachweis, "bewertungsnachweis")
    eingaben = dict(hypothekarisch_gesicherte_befriedigung=hypothekarisch_gesicherte_befriedigung, ersatzanspruch_gegen_eigentuemer=ersatzanspruch_gegen_eigentuemer, anwendungsfall_qualifiziert=anwendungsfall_qualifiziert, bewertungsnachweis=bewertungsnachweis)
    wert = min(betrag_eins, betrag_zwei) if anwendungsfall_qualifiziert else None
    ergebnis = _geld_ergebnis(wert, "BGB_HYPOTHEK_SCHULDNERUEBERGANGSBETRAG", eingaben, [dict(operation='Gesicherten Befriedigungsbetrag auf rechtlich bestehenden Ersatzanspruch begrenzen.')])
    ergebnis["hinweise"].append('Nur Umfang des Übergangs nach1164, nicht dingliche Rangverteilung. Befriedigung bezeichnet tatsächlich getilgten hypothekarisch gesicherten Betrag, keine ungesicherten Nebenforderungen. Vereinigung von Forderung und Schuld ist als entsprechender qualifizierter Betrag verwendbar. Konkurrierende Eigentümerhypothek darf nicht zum Nachteil des Schuldners geltend gemacht werden; kein Verteilungsplan.')
    return ergebnis

def hypothek_schuldbefreiung_nach_regressverlust(persoenliche_restschuld=None, verlorener_hypothekarischer_regress=None, anwendungsfall_qualifiziert=None, bewertungsnachweis=None):
    """Persönliche Restschuld bis zur Höhe des kausal verlorenen hypothekarischen Ersatzes freistellen."""
    betrag_eins = _geld(persoenliche_restschuld)
    betrag_zwei = _geld(verlorener_hypothekarischer_regress)
    _wahrheitswert(anwendungsfall_qualifiziert, "anwendungsfall_qualifiziert")
    _text(bewertungsnachweis, "bewertungsnachweis")
    eingaben = dict(persoenliche_restschuld=persoenliche_restschuld, verlorener_hypothekarischer_regress=verlorener_hypothekarischer_regress, anwendungsfall_qualifiziert=anwendungsfall_qualifiziert, bewertungsnachweis=bewertungsnachweis)
    wert = min(betrag_eins, betrag_zwei) if anwendungsfall_qualifiziert else None
    ergebnis = _geld_ergebnis(wert, "BGB_HYPOTHEK_SCHULDBEFREIUNG_NACH_REGRESSVERLUST", eingaben, [dict(operation='Persönliche Restschuld bis zur Höhe des kausal verlorenen hypothekarischen Ersatzes freistellen.')])
    ergebnis["hinweise"].append('Qualifizierter Verzicht, Aufhebung oder Vorrangeinräumung durch Gläubiger. Verlorener Regress ist rechtlich bewerteter ohne Verfügung erzielbarer1164-Ersatz, nicht pauschaler Grundstücks- oder Hypothekennennwert.')
    return ergebnis

def hypothek_ausfall_nach_benachrichtigungsschaden(ausfallforderung=None, kausaler_benachrichtigungsschaden=None, anwendungsfall_qualifiziert=None, bewertungsnachweis=None):
    """Ausfallforderung um kausalen Schaden aus unterbliebener Benachrichtigung mindern, mindestens null."""
    betrag_eins = _geld(ausfallforderung)
    betrag_zwei = _geld(kausaler_benachrichtigungsschaden)
    _wahrheitswert(anwendungsfall_qualifiziert, "anwendungsfall_qualifiziert")
    _text(bewertungsnachweis, "bewertungsnachweis")
    eingaben = dict(ausfallforderung=ausfallforderung, kausaler_benachrichtigungsschaden=kausaler_benachrichtigungsschaden, anwendungsfall_qualifiziert=anwendungsfall_qualifiziert, bewertungsnachweis=bewertungsnachweis)
    wert = max(_subtrahieren(betrag_eins, betrag_zwei), _bruch(0)) if anwendungsfall_qualifiziert else None
    ergebnis = _geld_ergebnis(wert, "BGB_HYPOTHEK_AUSFALL_NACH_BENACHRICHTIGUNGSSCHADEN", eingaben, [dict(operation='Ausfallforderung um kausalen Schaden aus unterbliebener Benachrichtigung mindern, mindestens null.')])
    ergebnis["hinweise"].append('Nur nach1166 qualifiziertes Verweigerungsrecht, insbesondere Ersatzberechtigung, vom Gläubiger betriebene Versteigerung und nicht untunliche Benachrichtigung. Ergebnis ist verbleibender nicht durch diesen Schaden abgedeckter Ausfall, kein Erlöschen oder automatische Rechtsausübung.')
    return ergebnis

def pfandrecht_einziehungsgrenze(einziehbare_geldforderung=None, erforderlicher_befriedigungsbetrag=None, anwendungsfall_qualifiziert=None, bewertungsnachweis=None):
    """Einziehbare Geldforderung auf erforderlichen Befriedigungsbetrag begrenzen."""
    betrag_eins = _geld(einziehbare_geldforderung)
    betrag_zwei = _geld(erforderlicher_befriedigungsbetrag)
    _wahrheitswert(anwendungsfall_qualifiziert, "anwendungsfall_qualifiziert")
    _text(bewertungsnachweis, "bewertungsnachweis")
    eingaben = dict(einziehbare_geldforderung=einziehbare_geldforderung, erforderlicher_befriedigungsbetrag=erforderlicher_befriedigungsbetrag, anwendungsfall_qualifiziert=anwendungsfall_qualifiziert, bewertungsnachweis=bewertungsnachweis)
    wert = min(betrag_eins, betrag_zwei) if anwendungsfall_qualifiziert else None
    ergebnis = _geld_ergebnis(wert, "BGB_PFANDRECHT_EINZIEHUNGSGRENZE", eingaben, [dict(operation='Einziehbare Geldforderung auf erforderlichen Befriedigungsbetrag begrenzen.')])
    ergebnis["hinweise"].append('Einziehungsberechtigung gemäß1228Absatz2/1282 und Umfang der gepfändeten Geldforderung vorqualifiziert. Erforderlicher Befriedigungsbetrag enthält ausschließlich gedeckte Ansprüche; keine eigenständige Feststellung der Fälligkeit oder Ermächtigung zu anderen Verfügungen.')
    return ergebnis

