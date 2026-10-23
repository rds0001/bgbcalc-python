"""Regulärer Beginn und begrenzte Rückwirkung von Betriebskostenpauschalenerhöhungen."""
from .betraege import _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler, _frist, _monatsende, _text


def betriebskostenpauschale_erhoehungsbeginn(
    erklaerungstag=None, kostenerhoehung_ab=None, kenntnis_am=None,
    massgebliches_dreimonatsfristende=None, kosten_rueckwirkend_erhoeht=None,
    erhoehung_nach_absatz_eins_zulaessig=None, zeitnachweis=None,
):
    """§560 Absatz2: übernächster Monat oder fristgebundene, jahresbegrenzte Rückwirkung."""
    erklaerung = _datum(erklaerungstag, "erklaerungstag")
    kosten = _datum(kostenerhoehung_ab, "kostenerhoehung_ab")
    kenntnis = _datum(kenntnis_am, "kenntnis_am")
    ende = _datum(massgebliches_dreimonatsfristende, "massgebliches_dreimonatsfristende")
    _wahrheitswert(kosten_rueckwirkend_erhoeht, "kosten_rueckwirkend_erhoeht")
    _wahrheitswert(erhoehung_nach_absatz_eins_zulaessig, "erhoehung_nach_absatz_eins_zulaessig")
    _text(zeitnachweis, "zeitnachweis")
    if kenntnis > erklaerung:
        _fehler("kenntnis_am", "Kenntnis darf nicht nach der Erhöhungserklärung liegen.")
    if kosten_rueckwirkend_erhoeht and kosten > kenntnis:
        _fehler("kostenerhoehung_ab", "Eine rückwirkende Erhöhung darf nicht erst nach der Kenntnis beginnen.")
    grundende = _frist(kenntnis_am, 3, "monate", "ereignis")
    if ende < grundende:
        _fehler("massgebliches_dreimonatsfristende", "Maßgebliches Fristende darf die gesetzliche Dreimonatsgrundfrist nicht verkürzen.")
    eingaben = dict(erklaerungstag=erklaerungstag, kostenerhoehung_ab=kostenerhoehung_ab,
        kenntnis_am=kenntnis_am, massgebliches_dreimonatsfristende=massgebliches_dreimonatsfristende,
        kosten_rueckwirkend_erhoeht=kosten_rueckwirkend_erhoeht,
        erhoehung_nach_absatz_eins_zulaessig=erhoehung_nach_absatz_eins_zulaessig,
        zeitnachweis=zeitnachweis)
    wert = None
    if erhoehung_nach_absatz_eins_zulaessig:
        regulaer = _monatsende(erklaerung.replace(day=1), 2, False)
        rechtzeitig = erklaerung <= ende
        rueckwirkung = kosten_rueckwirkend_erhoeht and rechtzeitig
        if rueckwirkung:
            if erklaerung.year == 1:
                _fehler("erklaerungstag", "Vorjahresbeginn liegt außerhalb des unterstützten Kalenderbereichs.")
            untergrenze = erklaerung.replace(year=erklaerung.year - 1, month=1, day=1)
            beginn = max(kosten, untergrenze)
        else:
            beginn = regulaer
        wert = dict(regulaerer_erhoehungsbeginn=regulaer.isoformat(),
            rechnerisches_dreimonatsfristende=grundende.isoformat(),
            dreimonatsfrist_eingehalten=rechtzeitig, rueckwirkung_anwendbar=rueckwirkung,
            erhoehungsbeginn=beginn.isoformat())
    ergebnis = _ergebnis(wert, "daten_und_wahrheitswerte", "BGB_BETRIEBSKOSTENPAUSCHALE_ERHOEHUNGSBEGINN", eingaben,
        [dict(operation="Übernächsten Monatsbeginn berechnen; rechtzeitige rückwirkende Kostensteigerung höchstens bis Vorjahresbeginn zurückbeziehen")], eingaben.copy())
    ergebnis["status"] = "BERECHNET" if erhoehung_nach_absatz_eins_zulaessig else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = ["Rechtlich maßgeblicher Erklärungstag, Kenntnis und qualifizierte rückwirkende Kostensteigerung vorgegeben; wirksame Pauschalenerhöhung nach§560 Absatz1 separat geprüft."]
    ergebnis["hinweise"] = ["Erklärungstag bezeichnet den rechtlich maßgeblichen Tag der Erklärung gegenüber dem Mieter; Versanddatum nicht ungeprüft einsetzen. Maßgebliches Dreimonatsfristende muss zulässige Kalenderkorrekturen bereits berücksichtigen und belegt sein; keine frei wählbare Verlängerung. Am letzten Fristtag ist die Erklärung rechtzeitig. Nur Erhöhungen einer Betriebskostenpauschale; keine Vorauszahlungen und keine rückwirkende Vereinbarung. Bei verspäteter Erklärung entfällt nur der hier geprüfte Rückwirkungsweg. Verschiedene Kostensteigerungen mit verschiedenen Kenntnistagen getrennt berechnen. Kein Rückwirkungsbetrag ohne zusätzliche periodengerechte Betragsrechnung."]
    return ergebnis
