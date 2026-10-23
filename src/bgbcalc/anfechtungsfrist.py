"""Anfechtungsfrist, Jahresfrist und absolute Zehnjahresgrenze§§121/124."""
from .betraege import _wahrheitswert
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _text


def anfechtung_fristpruefung(
    anfechtungsgrund=None, willenserklaerung_abgegeben_am=None, kenntnis_oder_zwangslageende_am=None,
    massgeblicher_anfechtungstag=None, unverzueglich_gehandelt=None,
    massgebliches_jahresfristende=None, anfechtungsregel_anwendbar=None, einordnungsnachweis=None,
):
    """§§121/124: unverzüglich oder Jahresfrist, jeweils zusätzlich absolute Zehnjahresgrenze."""
    _auswahl(anfechtungsgrund, "anfechtungsgrund", ("irrtum", "uebermittlungsfehler", "arglistige_taeuschung", "widerrechtliche_drohung"))
    abgabe = _datum(willenserklaerung_abgegeben_am, "willenserklaerung_abgegeben_am")
    ausloeser = _datum(kenntnis_oder_zwangslageende_am, "kenntnis_oder_zwangslageende_am")
    tag = _datum(massgeblicher_anfechtungstag, "massgeblicher_anfechtungstag")
    if tag < abgabe or tag < ausloeser:
        _fehler("massgeblicher_anfechtungstag", "Anfechtungstag darf nicht vor Abgabe oder angegebenem Fristauslöser liegen.")
    jahresweg = anfechtungsgrund in ("arglistige_taeuschung", "widerrechtliche_drohung")
    jahresende = None
    if massgebliches_jahresfristende is not None or jahresweg:
        jahresende = _datum(massgebliches_jahresfristende, "massgebliches_jahresfristende")
    _wahrheitswert(unverzueglich_gehandelt, "unverzueglich_gehandelt")
    _wahrheitswert(anfechtungsregel_anwendbar, "anfechtungsregel_anwendbar")
    _text(einordnungsnachweis, "einordnungsnachweis")
    eingaben = dict(anfechtungsgrund=anfechtungsgrund, willenserklaerung_abgegeben_am=willenserklaerung_abgegeben_am,
        kenntnis_oder_zwangslageende_am=kenntnis_oder_zwangslageende_am,
        massgeblicher_anfechtungstag=massgeblicher_anfechtungstag, unverzueglich_gehandelt=unverzueglich_gehandelt,
        massgebliches_jahresfristende=massgebliches_jahresfristende,
        anfechtungsregel_anwendbar=anfechtungsregel_anwendbar, einordnungsnachweis=einordnungsnachweis)
    wert = None
    if anfechtungsregel_anwendbar:
        hoechst = _frist(willenserklaerung_abgegeben_am, 10, "jahre", "ereignis")
        grundjahr = None
        ende = hoechst
        if jahresweg:
            grundjahr = _frist(kenntnis_oder_zwangslageende_am, 1, "jahre", "ereignis")
            if jahresende < grundjahr:
                _fehler("massgebliches_jahresfristende", "Maßgebliches Jahresfristende darf die Grundfrist nicht verkürzen.")
            ende = min(hoechst, jahresende)
        rechtzeitig = tag <= ende and (jahresweg or unverzueglich_gehandelt)
        wert = dict(zehnjahresgrenze=hoechst.isoformat(),
            rechnerisches_jahresfristende=grundjahr.isoformat() if grundjahr is not None else None,
            massgebliche_kalendergrenze=ende.isoformat(),
            unverzueglichkeit_erforderlich=not jahresweg, anfechtung_fristgerecht=rechtzeitig)
    ergebnis = _ergebnis(wert, "daten_und_wahrheitswerte", "BGB_ANFECHTUNG_FRISTPRUEFUNG", eingaben,
        [dict(operation="Irrtum/Übermittlung: bewertete Unverzüglichkeit; Täuschung/Drohung: maßgebliche Jahresfrist; stets zusätzliche Zehnjahresgrenze ab Abgabe")], eingaben.copy())
    ergebnis["status"] = "BERECHNET" if anfechtungsregel_anwendbar else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = ["Konkreter Anfechtungstatbestand und rechtlich maßgeblicher Erklärungstag vorgegeben; bei§124 Jahresfrist einschließlich einschlägiger Friständerungen geprüft; feste lokale BGB-Fassung."]
    ergebnis["hinweise"] = ["Unverzüglich bedeutet ohne schuldhaftes Zögern und wird nicht durch eine erfundene feste Tageszahl ersetzt. Bei§121 Absatz1 Satz2 kann unverzügliche Absendung gegenüber Abwesendem maßgeblich sein; tatsächlichen Zugang und Rechtzeitigkeit gegenüber absoluter Grenze gesondert rechtlich normalisieren, Versand nicht pauschal für alle Fristen einsetzen. Jahresbeginn bei Täuschung Entdeckung, bei Drohung Ende der Zwangslage. Maßgebliches Jahresende berücksichtigt gegebenenfalls§§206/210/211 und zulässige Kalenderkorrekturen; diese verlängern nicht automatisch die absolute Zehnjahresgrenze. Eine später erlangte Kenntnis startet diese Höchstgrenze nicht neu. Nur Fristprüfung, keine automatische Feststellung von Anfechtungsgrund, wirksamer Erklärung, Bestätigung§144 oder sonstigen Ausschlüssen."]
    return ergebnis
