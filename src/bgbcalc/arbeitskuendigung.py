"""Gesetzliche Standardfristen des §622 Absätze1–3 mit tatsächlichem Zugang."""
from calendar import monthrange
from datetime import date

from .betraege import _wahrheitswert
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _text


def arbeitsverhaeltnis_kuendigungstermin(
    beschaeftigungsbeginn=None, zugang_kuendigung=None, kuendigende_partei=None,
    probezeit_vereinbart=None, vereinbartes_probezeitende=None,
    gesetzliche_standardregel_anwendbar=None, fristnachweis=None,
):
    """§622: vier Wochen, Arbeitgeberstaffel oder höchstens sechsmonatige Probezeit."""
    beginn = _datum(beschaeftigungsbeginn, "beschaeftigungsbeginn")
    zugang = _datum(zugang_kuendigung, "zugang_kuendigung")
    if zugang < beginn:
        _fehler("zugang_kuendigung", "Kündigung vor Beschäftigungsbeginn außerhalb dieses Modells.")
    _auswahl(kuendigende_partei, "kuendigende_partei", ("arbeitnehmer", "arbeitgeber"))
    _wahrheitswert(probezeit_vereinbart, "probezeit_vereinbart")
    _wahrheitswert(gesetzliche_standardregel_anwendbar, "gesetzliche_standardregel_anwendbar")
    _text(fristnachweis, "fristnachweis")
    probeende = None
    if vereinbartes_probezeitende is not None or probezeit_vereinbart:
        probeende = _datum(vereinbartes_probezeitende, "vereinbartes_probezeitende")
        if probeende < beginn:
            _fehler("vereinbartes_probezeitende", "Probezeitende darf nicht vor Beschäftigungsbeginn liegen.")
    eingaben = dict(beschaeftigungsbeginn=beschaeftigungsbeginn,
        zugang_kuendigung=zugang_kuendigung, kuendigende_partei=kuendigende_partei,
        probezeit_vereinbart=probezeit_vereinbart, vereinbartes_probezeitende=vereinbartes_probezeitende,
        gesetzliche_standardregel_anwendbar=gesetzliche_standardregel_anwendbar,
        fristnachweis=fristnachweis)
    wert = None
    if gesetzliche_standardregel_anwendbar:
        jahre = zugang.year - beginn.year - int((zugang.month, zugang.day) < (beginn.month, beginn.day))
        probe = False
        if probezeit_vereinbart and zugang <= probeende:
            probe = zugang <= _frist(beschaeftigungsbeginn, 6, "monate", "tagesbeginn")
        monate = sum(jahre >= grenze for grenze in (2, 5, 8, 10, 12, 15, 20))
        if probe:
            anzahl, einheit, bindung = 2, "wochen", "jeder_tag"
        elif kuendigende_partei == "arbeitgeber" and monate:
            anzahl, einheit, bindung = monate, "monate", "monatsende"
        else:
            anzahl, einheit, bindung = 4, "wochen", "fuenfzehnter_oder_monatsende"
        ende = _frist(zugang_kuendigung, anzahl, einheit, "ereignis")
        mindestende = ende
        if bindung == "monatsende" or (bindung == "fuenfzehnter_oder_monatsende" and ende.day > 15):
            ende = date(ende.year, ende.month, monthrange(ende.year, ende.month)[1])
        elif bindung == "fuenfzehnter_oder_monatsende":
            ende = date(ende.year, ende.month, 15)
        wert = dict(vollendete_beschaeftigungsjahre=jahre, probezeitfrist_anwendbar=probe,
            fristanzahl=anzahl, fristeinheit=einheit, terminbindung=bindung,
            rechnerisches_mindestende=mindestende.isoformat(), fruehester_beendigungstag=ende.isoformat())
    ergebnis = _ergebnis(wert, "kuendigungsfrist_und_datum", "BGB_ARBEITSVERHAELTNIS_KUENDIGUNGSTERMIN",
        eingaben, [dict(operation="Probezeitgrenze und Arbeitgeberstaffel bestimmen; Frist ab Zugang und gesetzlichen Beendigungstermin berechnen")], eingaben.copy())
    ergebnis["status"] = "BERECHNET" if gesetzliche_standardregel_anwendbar else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = ["Beschäftigung ab Tagesbeginn; Zugang rechtlich festgestellt. Beschäftigungsbeginn bildet anrechenbare Betriebs-/Unternehmenszugehörigkeit ohne gesondert zu verrechnende Unterbrechungen ab."]
    ergebnis["hinweise"] = ["Nur gesetzliche Standardfristen§622 Absätze1–3. Tarifvertrag, einzelvertragliche längere oder wirksam kürzere Frist, Sondergesetze, Kündigungsverbote und Wirksamkeit der Erklärung gesondert prüfen.",
        "Probezeitfrist nur bei Zugang innerhalb der vereinbarten Probezeit und höchstens sechs Monaten; das Vertragsende darf danach liegen. Keine automatische Verlängerung einer kürzer vereinbarten Probezeit.",
        "Beendigungstermine werden nicht wegen Wochenenden oder Feiertagen verschoben. Keine Berechnung eines letzten Versandtags oder einer Zugangsfiktion."]
    return ergebnis
