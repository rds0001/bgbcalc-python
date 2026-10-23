"""Betragsoperationen aus §§244,270,285 und317 der lokalen BGB-Fassung."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _fehler, _text, _vorhanden
from .zahlen import _addieren, _subtrahieren, _multiplizieren, _dividieren, _bruch

def fremdwaehrung_eurobetrag(fremdwaehrungsbetrag=None, eurokurs=None, eurozahlung_nach_244_zulaessig=None, bewertungsnachweis=None):
    """Fremdwährungsbetrag mit Euro je Einheit Fremdwährung multiplizieren."""
    eingaben = dict(fremdwaehrungsbetrag=fremdwaehrungsbetrag, eurokurs=eurokurs, eurozahlung_nach_244_zulaessig=eurozahlung_nach_244_zulaessig, bewertungsnachweis=bewertungsnachweis)
    a = _geld(fremdwaehrungsbetrag)
    b = _geld(eurokurs)
    _wahrheitswert(eurozahlung_nach_244_zulaessig, "eurozahlung_nach_244_zulaessig")
    _text(bewertungsnachweis, "bewertungsnachweis")
    if b == 0:
        _fehler("eurokurs", "Positiver Eurokurs erforderlich.")
    betrag = None
    if eurozahlung_nach_244_zulaessig:
        betrag = _multiplizieren(a, b)
    ergebnis = _geld_ergebnis(betrag, "BGB_FREMDWAEHRUNG_EUROBETRAG", eingaben, [dict(operation='Fremdwährungsbetrag mit Euro je Einheit Fremdwährung multiplizieren.')])
    ergebnis["hinweise"].append('Kurswert am Zahlungsort zur tatsächlichen Zahlungszeit als belegte Eingabe. Keine Onlinekurse, keine Umkehrung einer Fremdwährung-je-Euro-Notierung. Nur bei zulässiger Eurozahlung im Inland; ausdrücklich vereinbarte ausschließliche Fremdwährungszahlung ausgeschlossen.')
    return ergebnis

def gelduebermittlung_umzugsmehrkosten(kosten_vor_verlegung=None, kosten_nach_verlegung=None, kostenvergleich_nach_270_absatz_3_anwendbar=None, bewertungsnachweis=None):
    """Kosten nach Verlegung minus vergleichbare Kosten ohne Verlegung, mindestens null."""
    eingaben = dict(kosten_vor_verlegung=kosten_vor_verlegung, kosten_nach_verlegung=kosten_nach_verlegung, kostenvergleich_nach_270_absatz_3_anwendbar=kostenvergleich_nach_270_absatz_3_anwendbar, bewertungsnachweis=bewertungsnachweis)
    a = _geld(kosten_vor_verlegung)
    b = _geld(kosten_nach_verlegung)
    _wahrheitswert(kostenvergleich_nach_270_absatz_3_anwendbar, "kostenvergleich_nach_270_absatz_3_anwendbar")
    _text(bewertungsnachweis, "bewertungsnachweis")
    betrag = None
    if kostenvergleich_nach_270_absatz_3_anwendbar:
        betrag = max(_subtrahieren(b, a), _bruch(0))
    ergebnis = _geld_ergebnis(betrag, "BGB_GELDUEBERMITTLUNG_UMZUGSMEHRKOSTEN", eingaben, [dict(operation='Kosten nach Verlegung minus vergleichbare Kosten ohne Verlegung, mindestens null.')])
    ergebnis["hinweise"].append('Nur kausale Mehrkosten der nach Entstehung des Schuldverhältnisses erfolgten Verlegung von Gläubigerwohnsitz oder maßgeblicher Niederlassung. Beträge unter ansonsten gleichen Bedingungen bestimmen; keine Übernahme der gesamten Übermittlungskosten oder Berechnung der Gefahrtragung.')
    return ergebnis

def schadensersatz_nach_ersatzherausgabe(schadensersatz_vor_anrechnung=None, wert_des_erlangten_ersatzes=None, ersatzrecht_nach_285_ausgeuebt=None, bewertungsnachweis=None):
    """Schadensersatz statt der Leistung um den Wert des herausverlangten Ersatzes mindern, mindestens null."""
    eingaben = dict(schadensersatz_vor_anrechnung=schadensersatz_vor_anrechnung, wert_des_erlangten_ersatzes=wert_des_erlangten_ersatzes, ersatzrecht_nach_285_ausgeuebt=ersatzrecht_nach_285_ausgeuebt, bewertungsnachweis=bewertungsnachweis)
    a = _geld(schadensersatz_vor_anrechnung)
    b = _geld(wert_des_erlangten_ersatzes)
    _wahrheitswert(ersatzrecht_nach_285_ausgeuebt, "ersatzrecht_nach_285_ausgeuebt")
    _text(bewertungsnachweis, "bewertungsnachweis")
    betrag = None
    if ersatzrecht_nach_285_ausgeuebt:
        betrag = max(_subtrahieren(a, b), _bruch(0))
    ergebnis = _geld_ergebnis(betrag, "BGB_SCHADENSERSATZ_NACH_ERSATZHERAUSGABE", eingaben, [dict(operation='Schadensersatz statt der Leistung um den Wert des herausverlangten Ersatzes mindern, mindestens null.')])
    ergebnis["hinweise"].append('Wirksamer Schadensersatzanspruch statt der Leistung und Ausübung des Rechts nach§285 Absatz1 fachlich vorgegeben. Ausgangsbetrag noch ohne diese Anrechnung. Keine Rückzahlungsforderung bei höherem Ersatzwert; Herausgabeanspruch und sonstige Anspruchsänderungen separat.')
    return ergebnis

def leistungsbestimmung_durchschnittssumme(bestimmte_summen=None, zweifelsregel_nach_317_anwendbar=None, bewertungsnachweis=None):
    """Gleichgewichteter Durchschnitt der Summen sämtlicher bestimmender Dritter."""
    _vorhanden(bestimmte_summen, "bestimmte_summen")
    if not isinstance(bestimmte_summen, list) or not 2 <= len(bestimmte_summen) <= 1000:
        _fehler("bestimmte_summen", "Liste mit2 bis1000 Bestimmungen erforderlich.")
    namen = set()
    summe = _bruch(0)
    for bestimmung in bestimmte_summen:
        if not isinstance(bestimmung, dict) or set(bestimmung) != {"dritter_id", "summe"}:
            _fehler("bestimmte_summen", "Genau dritter_id und summe erforderlich.")
        name = _text(bestimmung["dritter_id"], "dritter_id")
        if name in namen:
            _fehler("dritter_id", "Jeden Dritten genau einmal einbeziehen.")
        namen.add(name)
        summe = _addieren(summe, _geld(bestimmung["summe"]))
    _wahrheitswert(zweifelsregel_nach_317_anwendbar, "zweifelsregel_nach_317_anwendbar")
    _text(bewertungsnachweis, "bewertungsnachweis")
    eingaben = dict(bestimmte_summen=bestimmte_summen, zweifelsregel_nach_317_anwendbar=zweifelsregel_nach_317_anwendbar, bewertungsnachweis=bewertungsnachweis)
    betrag = _dividieren(summe, _bruch(len(bestimmte_summen))) if zweifelsregel_nach_317_anwendbar else None
    ergebnis = _geld_ergebnis(betrag, "BGB_LEISTUNGSBESTIMMUNG_DURCHSCHNITTSSUMME", eingaben, [dict(operation='Summen sämtlicher bestimmender Dritter gleichgewichtet addieren und durch deren Anzahl teilen.')])
    ergebnis["hinweise"].append('Nur die Zweifelsregel für eine durch mehrere Dritte bestimmte Geldsumme in einheitlicher Währung EUR. Abweichende Vereinbarungen, rechtlich unwirksame Bestimmungen oder nichtmonetäre Leistungen nicht erfasst. Jede Person genau einmal einbeziehen; keine Mehrheitsabstimmung und keine Entfernung von Ausreißern.')
    return ergebnis
