"""Krankenfürsorgezeitraum und Kostenanrechnung im Dienstverhältnis§617."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _text
from .zahlen import _subtrahieren
from .zinsen import _bruchteile


def dienst_krankenfuersorge_zeitraum(
    erkrankungsbeginn_am=None, beginnart=None, dienstverhaeltnis_ende_am=None,
    dauerndes_hauptdienstverhaeltnis=None, in_haeusliche_gemeinschaft_aufgenommen=None,
    erkrankung_vorsaetzlich_oder_grob_fahrlaessig=None, versicherung_oder_oeffentliche_krankenpflege=None,
    krankheitskuendigung_626_durch_dienstberechtigten=None, einordnungsnachweis=None,
):
    """§617: höchstens sechs Wochen, Ende begrenzt außer qualifizierter Krankheitskündigung."""
    beginn = _datum(erkrankungsbeginn_am, "erkrankungsbeginn_am")
    _auswahl(beginnart, "beginnart", ("ereignis", "tagesbeginn"))
    dienstende = _datum(dienstverhaeltnis_ende_am, "dienstverhaeltnis_ende_am") if dienstverhaeltnis_ende_am is not None else None
    if dienstende is not None and dienstende < beginn:
        _fehler("dienstverhaeltnis_ende_am", "Dienstende darf nicht vor hier betrachtetem Erkrankungsbeginn liegen.")
    eingaben = dict(erkrankungsbeginn_am=erkrankungsbeginn_am, beginnart=beginnart,
        dienstverhaeltnis_ende_am=dienstverhaeltnis_ende_am,
        dauerndes_hauptdienstverhaeltnis=dauerndes_hauptdienstverhaeltnis,
        in_haeusliche_gemeinschaft_aufgenommen=in_haeusliche_gemeinschaft_aufgenommen,
        erkrankung_vorsaetzlich_oder_grob_fahrlaessig=erkrankung_vorsaetzlich_oder_grob_fahrlaessig,
        versicherung_oder_oeffentliche_krankenpflege=versicherung_oder_oeffentliche_krankenpflege,
        krankheitskuendigung_626_durch_dienstberechtigten=krankheitskuendigung_626_durch_dienstberechtigten,
        einordnungsnachweis=einordnungsnachweis)
    for name in tuple(eingaben)[3:-1]:
        _wahrheitswert(eingaben[name], name)
    _text(einordnungsnachweis, "einordnungsnachweis")
    gilt = (dauerndes_hauptdienstverhaeltnis and in_haeusliche_gemeinschaft_aufgenommen and
        not erkrankung_vorsaetzlich_oder_grob_fahrlaessig and not versicherung_oder_oeffentliche_krankenpflege)
    wert = None
    if gilt:
        sechswochen = _frist(erkrankungsbeginn_am, 6, "wochen", beginnart)
        ende = min(sechswochen, dienstende) if dienstende is not None and not krankheitskuendigung_626_durch_dienstberechtigten else sechswochen
        wert = dict(sechswochengrenze=sechswochen.isoformat(), fuersorge_spaetestens_bis=ende.isoformat())
    ergebnis = _ergebnis(wert, "fristdaten", "BGB_DIENST_KRANKENFUERSORGE_ZEITRAUM", eingaben,
        [dict(operation="Qualifizierte Krankenfürsorge höchstens sechs Wochen; früheres Dienstende begrenzt, außer krankheitsbedingter Kündigung durch Dienstberechtigten nach§626")], eingaben.copy())
    ergebnis["status"] = "BERECHNET" if gilt else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = ["Dauerndes Dienstverhältnis, häusliche Aufnahme und konkrete Erkrankung rechtlich eingeordnet; feste lokale BGB-Fassung."]
    ergebnis["hinweise"] = ["Nur zeitliche Höchstgrenze erforderlicher Verpflegung/ärztlicher Behandlung; frühere Genesung oder Wegfall der Erforderlichkeit begrenzt tatsächliche Fürsorge. Keine allgemeine Entgeltfortzahlung und kein unbegrenzter Vergütungsanspruch. Ausnahme vom Dienstende nur bei gerade wegen Erkrankung vom Dienstberechtigten erklärter§626-Kündigung. Vorsorge durch Versicherung/öffentliche Krankenpflege muss gerade Verpflegung und Behandlung abdecken. Keine automatische Kalenderverlängerung der tatsächlichen Fürsorgedauer; keine Addition mehrerer Krankheitsfälle ohne rechtliche Prüfung."]
    return ergebnis


def dienst_krankheitskosten_anrechnung(
    verguetung_erkrankungszeit=None, anrechenbare_fuersorgekosten=None,
    kostenanrechnung_nach_617_zulaessig=None, anrechnung_ausgeuebt=None, kostennachweis=None,
):
    """§617 Absatz1 Satz3: qualifizierte Fürsorgekosten höchstens bis zur Periodenvergütung anrechnen."""
    verguetung = _geld(verguetung_erkrankungszeit)
    kosten = _geld(anrechenbare_fuersorgekosten)
    _wahrheitswert(kostenanrechnung_nach_617_zulaessig, "kostenanrechnung_nach_617_zulaessig")
    _wahrheitswert(anrechnung_ausgeuebt, "anrechnung_ausgeuebt")
    _text(kostennachweis, "kostennachweis")
    eingaben = dict(verguetung_erkrankungszeit=verguetung_erkrankungszeit,
        anrechenbare_fuersorgekosten=anrechenbare_fuersorgekosten,
        kostenanrechnung_nach_617_zulaessig=kostenanrechnung_nach_617_zulaessig,
        anrechnung_ausgeuebt=anrechnung_ausgeuebt, kostennachweis=kostennachweis)
    ergebnis = _geld_ergebnis(None, "BGB_DIENST_KRANKHEITSKOSTEN_ANRECHNUNG", eingaben,
        [dict(operation="Bei zulässiger ausgeübter Anrechnung geringeren Betrag aus Periodenvergütung und qualifizierten Fürsorgekosten abziehen")])
    if kostenanrechnung_nach_617_zulaessig:
        anrechnung = min(verguetung, kosten) if anrechnung_ausgeuebt else verguetung * 0
        ergebnis["wert"] = dict(angerechnete_kosten=_bruchteile(anrechnung),
            verbleibende_verguetung=_bruchteile(_subtrahieren(verguetung, anrechnung)))
        ergebnis["status"] = "BERECHNET"
    ergebnis["hinweise"].append("Vergütung und Kosten müssen denselben rechtlich zugehörigen Erkrankungszeitraum betreffen, ohne Doppelanrechnung und mit konsistenter Brutto-/Nettobasis. Kosten gesetzlich erforderlicher Verpflegung/Behandlung vorab bestimmen; keine beliebige Pauschale und keine Anrechnung von bereits durch Versicherung gedeckten Kosten. Anrechnung kann erfolgen, ist keine automatische Lohnkürzung. Keine negative Vergütung oder automatische weitere Erstattungspflicht aus übersteigenden Kosten ableiten; etwaige andere Rechtsgrundlagen bleiben gesondert.")
    return ergebnis
