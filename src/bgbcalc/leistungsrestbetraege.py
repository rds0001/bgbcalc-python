"""Kauf-, Wiederkauf- und Vorkauf-Sonderbeträge mit qualifizierten Werten."""
from .betraege import _geld, _geld_ergebnis
from .kalender import _text, _fehler
from .zahlen import _addieren, _subtrahieren, _multiplizieren, _dividieren, _bruch


def miete_nach_ersparnis_und_verwertung(zeitraumsmiete=None, ersparte_aufwendungen=None, anderweitiger_verwertungsvorteil=None, einordnungsnachweis=None):
    """Vom qualifizierten Mietbetrag ersparte Aufwendungen und anderweitigen Verwertungsvorteil abziehen, Rest mindestens null."""
    werte = [_geld(zeitraumsmiete), _geld(ersparte_aufwendungen), _geld(anderweitiger_verwertungsvorteil)]
    _text(einordnungsnachweis, 'einordnungsnachweis')
    eingaben = dict(zeitraumsmiete=zeitraumsmiete, ersparte_aufwendungen=ersparte_aufwendungen, anderweitiger_verwertungsvorteil=anderweitiger_verwertungsvorteil, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(max(_subtrahieren(_subtrahieren(werte[0],werte[1]),werte[2]),_bruch(0)), 'BGB_MIETE_NACH_ERSPARNIS_UND_VERWERTUNG', eingaben, [dict(operation='Vom qualifizierten Mietbetrag ersparte Aufwendungen und anderweitigen Verwertungsvorteil abziehen, Rest mindestens null')])
    ergebnis['hinweise'].append('Nur §537 Absatz1 bei persönlicher Gebrauchshinderung des Mieters. Zeitraumsmiete muss Zeiträume nach Absatz2 ausschließen, für die wegen Drittüberlassung kein Mietanspruch besteht. Abzüge für denselben Zeitraum rechtlich bewerten und überschneidungsfrei eingeben. Kein zusätzlicher Anspruch auf einen negativen Rest; Mietminderung und andere Einwendungen gesondert.')
    return ergebnis


def pacht_vorenthaltung_nutzungsanteil(vereinbarte_jahrespacht=None, nutzungswert_vorenthaltung=None, nutzungswert_pachtjahr=None, einordnungsnachweis=None):
    """Vereinbarte Jahrespacht mal qualifizierter Nutzungswert der Vorenthaltung geteilt durch positiven Nutzungswert des ganzen Pachtjahrs."""
    werte = [_geld(vereinbarte_jahrespacht), _geld(nutzungswert_vorenthaltung), _geld(nutzungswert_pachtjahr)]
    _text(einordnungsnachweis, 'einordnungsnachweis')
    if werte[2] <= 0 or werte[1] > werte[2]:
        _fehler('nutzungswert_pachtjahr', 'Jahresnutzungswert muss positiv sein und den Vorenthaltungsanteil umfassen.')
    eingaben = dict(vereinbarte_jahrespacht=vereinbarte_jahrespacht, nutzungswert_vorenthaltung=nutzungswert_vorenthaltung, nutzungswert_pachtjahr=nutzungswert_pachtjahr, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(_multiplizieren(werte[0],_dividieren(werte[1],werte[2])), 'BGB_PACHT_VORENTHALTUNG_NUTZUNGSANTEIL', eingaben, [dict(operation='Vereinbarte Jahrespacht mal qualifizierter Nutzungswert der Vorenthaltung geteilt durch positiven Nutzungswert des ganzen Pachtjahrs')])
    ergebnis['hinweise'].append('Nur §584b für einen Abschnitt innerhalb eines Pachtjahrs; gezogene oder objektiv erzielbare Nutzungen gleichartig bewerten. Keine automatische Gleichsetzung des Nutzungsanteils mit einem Tagesanteil. Bei mehreren Pachtjahren getrennt rechnen. Weiterer Schaden und Anspruchsvoraussetzungen gesondert; nicht §597-Landpachtrechnung.')
    return ergebnis


def werk_abschlagsrestbetrag(wert_geschuldeter_erbrachter_leistungen=None, bereits_gezahlte_abschlaege=None, qualifizierter_zurueckbehaltungsbetrag=None, einordnungsnachweis=None):
    """Kumulierten Wert geschuldeter erbrachter Leistungen um bereits gezahlte Abschläge und qualifizierten Zurückbehaltungsbetrag vermindern, Rest mindestens null."""
    werte = [_geld(wert_geschuldeter_erbrachter_leistungen), _geld(bereits_gezahlte_abschlaege), _geld(qualifizierter_zurueckbehaltungsbetrag)]
    _text(einordnungsnachweis, 'einordnungsnachweis')
    eingaben = dict(wert_geschuldeter_erbrachter_leistungen=wert_geschuldeter_erbrachter_leistungen, bereits_gezahlte_abschlaege=bereits_gezahlte_abschlaege, qualifizierter_zurueckbehaltungsbetrag=qualifizierter_zurueckbehaltungsbetrag, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(max(_subtrahieren(_subtrahieren(werte[0],werte[1]),werte[2]),_bruch(0)), 'BGB_WERK_ABSCHLAGSRESTBETRAG', eingaben, [dict(operation='Kumulierten Wert geschuldeter erbrachter Leistungen um bereits gezahlte Abschläge und qualifizierten Zurückbehaltungsbetrag vermindern, Rest mindestens null')])
    ergebnis['hinweise'].append('Nur §632a kumulierte, nachgewiesene vertragsgeschuldete Leistungen derselben Abrechnung. Nicht bloß Rechnungsnennbetrag. Angemessenen Einbehalt, einschließlich entsprechend §641 Absatz3, extern qualifizieren (vorhandener werk_maengeleinbehalt-Kern). Stoffe/Bauteile nur bei qualifiziert erfüllten Sicherungs-/Eigentumsvoraussetzungen. Keine automatische Rückforderung bei Überzahlung und kein doppelter Abzug schon verrechneter Abschläge oder Mängel. Verbraucherbau-Gesamtgrenze und Herstellungssicherheit nach §650m zusätzlich gesondert anwenden.')
    return ergebnis
