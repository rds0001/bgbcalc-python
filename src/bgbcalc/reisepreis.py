"""Pauschalreise: Preisänderungsgrenzen und Erstattung nach §§651f/651g."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler, _tage_addieren, _text
from .zahlen import _bruch, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile


def pauschalreise_preiserhoehungsgrenze(
    reisepreis=None, erhoehungsbetrag=None, reisebeginn=None, unterrichtungstag=None,
    aenderungsvorbehalt_ordnungsgemaess=None, zulaessiger_kostengrund=None,
    unterrichtung_formgerecht=None, berechnungsnachweis=None,
):
    """Achtprozentgrenze und zwanzigtägigen Vorlauf aus bewerteten Voraussetzungen prüfen."""
    preis = _geld(reisepreis)
    if preis <= 0:
        _fehler("reisepreis", "Positiver Reisepreis erforderlich.")
    erhoehung = _geld(erhoehungsbetrag)
    beginn = _datum(reisebeginn, "reisebeginn")
    unterrichtung = _datum(unterrichtungstag, "unterrichtungstag")
    _text(berechnungsnachweis, "berechnungsnachweis")
    eingaben = dict(reisepreis=reisepreis, erhoehungsbetrag=erhoehungsbetrag,
        reisebeginn=reisebeginn, unterrichtungstag=unterrichtungstag,
        aenderungsvorbehalt_ordnungsgemaess=aenderungsvorbehalt_ordnungsgemaess,
        zulaessiger_kostengrund=zulaessiger_kostengrund, unterrichtung_formgerecht=unterrichtung_formgerecht,
        berechnungsnachweis=berechnungsnachweis)
    for name in ("aenderungsvorbehalt_ordnungsgemaess", "zulaessiger_kostengrund", "unterrichtung_formgerecht"):
        _wahrheitswert(eingaben[name], name)
    grenze = _multiplizieren(preis, _bruch(2, 25))
    letzter_tag = _tage_addieren(beginn, -20)
    fristgerecht = unterrichtung <= letzter_tag
    ueber_grenze = erhoehung > grenze
    wert = dict(achtprozentbetrag=_bruchteile(grenze), achtprozentgrenze_ueberschritten=ueber_grenze,
        spaetester_unterrichtungstag=letzter_tag.isoformat(), zwanzigtage_vorlauf_eingehalten=fristgerecht,
        einseitige_erhoehungsvoraussetzungen_erfuellt=(aenderungsvorbehalt_ordnungsgemaess
            and zulaessiger_kostengrund and unterrichtung_formgerecht and fristgerecht and not ueber_grenze))
    ergebnis = _ergebnis(wert, "preisgrenze_und_voraussetzungen", "BGB_PAUSCHALREISE_PREISERHOEHUNGSGRENZE",
        eingaben, [dict(operation="Acht Prozent des Reisepreises und Unterrichtung spätestens zwanzig Tage vor Reisebeginn prüfen")], eingaben.copy())
    ergebnis["annahmen"] = ["Pauschalreise und konkrete Preisänderung nach fester BGB-Fassung; Berechnung und Kostenursache rechtlich bewertet vorgegeben."]
    ergebnis["hinweise"] = ["Über8Prozent keine einseitige Erhöhung; mögliches Änderungsangebot nach§651g und dessen weitere Voraussetzungen gesondert. Genau8Prozent überschreitet die Grenze nicht.",
        "Keine automatische Ermittlung von Energie-, Abgaben- oder Wechselkursänderungen und keine freie gesetzliche Aufschlagserlaubnis. Der konkrete Änderungsbetrag folgt dem zulässigen vertraglichen Berechnungsweg.",
        "Taggenauer Vorlauf ohne Verschiebung zugunsten späterer Unterrichtung; tatsächliche rechtzeitige Information auf dauerhaftem Datenträger vorgeben."]
    return ergebnis


def pauschalreise_preissenkung_erstattung(
    reisepreis=None, preissenkungsbetrag=None, geleistete_zahlung=None,
    tatsaechliche_verwaltungsausgaben=None, senkungsvoraussetzungen_erfuellt=None,
    berechnungsnachweis=None,
):
    """§651f Absatz4: gesenkter Preis, Überzahlung und tatsächliche Verwaltungsabzüge."""
    preis, senkung = _geld(reisepreis), _geld(preissenkungsbetrag)
    gezahlt, ausgaben = _geld(geleistete_zahlung), _geld(tatsaechliche_verwaltungsausgaben)
    if senkung > preis:
        _fehler("preissenkungsbetrag", "Preissenkung darf den Reisepreis nicht übersteigen.")
    _wahrheitswert(senkungsvoraussetzungen_erfuellt, "senkungsvoraussetzungen_erfuellt")
    _text(berechnungsnachweis, "berechnungsnachweis")
    eingaben = dict(reisepreis=reisepreis, preissenkungsbetrag=preissenkungsbetrag,
        geleistete_zahlung=geleistete_zahlung, tatsaechliche_verwaltungsausgaben=tatsaechliche_verwaltungsausgaben,
        senkungsvoraussetzungen_erfuellt=senkungsvoraussetzungen_erfuellt, berechnungsnachweis=berechnungsnachweis)
    ergebnis = _geld_ergebnis(None, "BGB_PAUSCHALREISE_PREISSENKUNG_ERSTATTUNG", eingaben,
        [dict(operation="Gesenkten Reisepreis, gezahlten Mehrbetrag und höchstens diesen Mehrbetrag erreichenden Verwaltungsabzug berechnen")])
    if senkungsvoraussetzungen_erfuellt:
        gesenkt = _subtrahieren(preis, senkung)
        mehrbetrag = max(_subtrahieren(gezahlt, gesenkt), _bruch(0))
        abzug = min(mehrbetrag, ausgaben)
        ergebnis["wert"] = dict(gesenkter_reisepreis=_bruchteile(gesenkt), gezahlter_mehrbetrag=_bruchteile(mehrbetrag),
            verwaltungsabzug=_bruchteile(abzug), erstattungsbetrag=_bruchteile(_subtrahieren(mehrbetrag, abzug)))
        ergebnis["status"] = "BERECHNET"
    ergebnis["hinweise"].append("Verwaltungsausgaben nur vom zu erstattenden Mehrbetrag abziehen, nicht den gesenkten Vertragspreis erhöhen. Nur tatsächlich entstandene gesetzlich abzugsfähige Ausgaben; Nachweis auf Verlangen gesondert.")
    return ergebnis
