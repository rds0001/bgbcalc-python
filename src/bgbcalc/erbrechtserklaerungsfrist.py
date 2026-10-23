"""Erbrechtliche Ausschlagungs- und Anfechtungsgrundfristen§§1944/1954/1956."""
from .betraege import _wahrheitswert
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _text


def _erbrechtsfrist(beginn, ausland):
    return _frist(beginn.isoformat(), 6, "monate" if ausland else "wochen", "ereignis")


def _erbrechtsfrist_ergebnis(wert, kennung, eingaben, operation):
    ergebnis = _ergebnis(wert, "fristdaten", kennung, eingaben,
        [dict(operation=operation)], eingaben.copy())
    ergebnis["status"] = "BERECHNET" if wert is not None else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = ["Erbrechtlicher Grundtatbestand und rechtlich maßgebliche Ereignisse/Ortsverhältnisse vorgegeben; feste lokale BGB-Fassung."]
    ergebnis["hinweise"] = ["Nur Grundfrist und gegebenenfalls absolute Grenze; noch keine abschließende Erklärungsmöglichkeit. §1944 verweist auf§§206/210, §1954 zusätzlich auf§211; einschlägige Hemmungen/Ablaufhemmungen und Kalenderkorrekturen gesondert prüfen. Gerichtliche Erklärung/Form/Zugang und etwaige frühere Annahme oder andere Ausschlüsse separat. Ausland bedeutet tatsächlicher rechtlich maßgeblicher Wohnsitz/Aufenthalt, nicht bloß Staatsangehörigkeit oder spätere Reise."]
    return ergebnis


def erbausschlagung_grundfrist(
    erbfall_am=None, kenntnis_anfall_berufungsgrund_am=None,
    berufung_durch_verfuegung=None, gerichtliche_bekanntgabe_am=None,
    erblasser_letzter_wohnsitz_nur_ausland=None, erbe_bei_fristbeginn_im_ausland=None,
    ausschlagungsregel_anwendbar=None, einordnungsnachweis=None,
):
    """§1944: sechs Wochen oder sechs Monate, bei Verfügung Bekanntgabe als zusätzliche Startgrenze."""
    erbfall = _datum(erbfall_am, "erbfall_am")
    kenntnis = _datum(kenntnis_anfall_berufungsgrund_am, "kenntnis_anfall_berufungsgrund_am")
    _wahrheitswert(berufung_durch_verfuegung, "berufung_durch_verfuegung")
    bekanntgabe = None
    if gerichtliche_bekanntgabe_am is not None or berufung_durch_verfuegung:
        bekanntgabe = _datum(gerichtliche_bekanntgabe_am, "gerichtliche_bekanntgabe_am")
    if kenntnis < erbfall:
        _fehler("kenntnis_anfall_berufungsgrund_am", "Kenntnis vom Erbanfall darf nicht vor dem Erbfall liegen.")
    if berufung_durch_verfuegung and bekanntgabe < erbfall:
        _fehler("gerichtliche_bekanntgabe_am", "Maßgebliche Bekanntgabe darf nicht vor dem Erbfall liegen.")
    eingaben = dict(erbfall_am=erbfall_am, kenntnis_anfall_berufungsgrund_am=kenntnis_anfall_berufungsgrund_am,
        berufung_durch_verfuegung=berufung_durch_verfuegung, gerichtliche_bekanntgabe_am=gerichtliche_bekanntgabe_am,
        erblasser_letzter_wohnsitz_nur_ausland=erblasser_letzter_wohnsitz_nur_ausland,
        erbe_bei_fristbeginn_im_ausland=erbe_bei_fristbeginn_im_ausland,
        ausschlagungsregel_anwendbar=ausschlagungsregel_anwendbar, einordnungsnachweis=einordnungsnachweis)
    for name in tuple(eingaben)[4:-1]:
        _wahrheitswert(eingaben[name], name)
    _text(einordnungsnachweis, "einordnungsnachweis")
    wert = None
    if ausschlagungsregel_anwendbar:
        beginn = max(kenntnis, bekanntgabe) if berufung_durch_verfuegung else kenntnis
        ausland = erblasser_letzter_wohnsitz_nur_ausland or erbe_bei_fristbeginn_im_ausland
        wert = dict(fristbeginnereignis_am=beginn.isoformat(), fristdauer=6,
            fristeinheit="monate" if ausland else "wochen",
            rechnerischer_letzter_tag=_erbrechtsfrist(beginn, ausland).isoformat())
    return _erbrechtsfrist_ergebnis(wert, "BGB_ERBAUSSCHLAGUNG_GRUNDFRIST", eingaben,
        "Kenntnis von Anfall und Berufungsgrund; bei Verfügung zusätzlich Bekanntgabe abwarten; mindestens eine gesetzliche Auslandsalternative verlängert sechs Wochen auf sechs Monate")


def erbrecht_anfechtungsgrundfrist(
    anfechtungsfall=None, angefochtenes_ereignis_am=None, fristbeginn_am=None,
    erblasser_letzter_wohnsitz_nur_ausland=None, erbe_bei_fristbeginn_im_ausland=None,
    anfechtungsregel_anwendbar=None, einordnungsnachweis=None,
):
    """§§1954/1956: sechs Wochen/Monate ab Kenntnis oder Zwangsende, dreißigjährige Höchstgrenze."""
    _auswahl(anfechtungsfall, "anfechtungsfall", ("annahme", "ausschlagung", "ausschlagungsfristversaeumung"))
    ereignis = _datum(angefochtenes_ereignis_am, "angefochtenes_ereignis_am")
    beginn = _datum(fristbeginn_am, "fristbeginn_am")
    if beginn < ereignis:
        _fehler("fristbeginn_am", "Hier maßgeblicher Anfechtungsfristbeginn darf nicht vor angefochtenem Ereignis liegen.")
    eingaben = dict(anfechtungsfall=anfechtungsfall, angefochtenes_ereignis_am=angefochtenes_ereignis_am,
        fristbeginn_am=fristbeginn_am, erblasser_letzter_wohnsitz_nur_ausland=erblasser_letzter_wohnsitz_nur_ausland,
        erbe_bei_fristbeginn_im_ausland=erbe_bei_fristbeginn_im_ausland,
        anfechtungsregel_anwendbar=anfechtungsregel_anwendbar, einordnungsnachweis=einordnungsnachweis)
    for name in tuple(eingaben)[3:-1]:
        _wahrheitswert(eingaben[name], name)
    _text(einordnungsnachweis, "einordnungsnachweis")
    wert = None
    if anfechtungsregel_anwendbar:
        ausland = erblasser_letzter_wohnsitz_nur_ausland or erbe_bei_fristbeginn_im_ausland
        grundende = _erbrechtsfrist(beginn, ausland)
        hoechst = _frist(angefochtenes_ereignis_am, 30, "jahre", "ereignis")
        wert = dict(fristdauer=6, fristeinheit="monate" if ausland else "wochen",
            rechnerisches_grundfristende=grundende.isoformat(), dreissigjahresgrenze=hoechst.isoformat(),
            rechnerischer_letzter_tag=min(grundende, hoechst).isoformat())
    return _erbrechtsfrist_ergebnis(wert, "BGB_ERBRECHT_ANFECHTUNGSGRUNDFRIST", eingaben,
        "Sechs Wochen oder bei gesetzlicher Auslandsalternative sechs Monate ab einschlägigem Anfechtungsfristbeginn; zusätzlich dreißig Jahre ab angefochtener Annahme/Ausschlagung begrenzen")
