"""Fünfjährige Sperre weiterer Modernisierungserhöhungen und gesetzliche Ausnahmen."""
from .betraege import _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler, _frist, _tage_addieren, _text


def modernisierung_vereinfachung_sperrfrist(
    zugang_vereinfachte_erhoehung_am=None, neue_geltendmachung_am=None,
    gesetzliche_modernisierungspflicht=None, pflicht_damals_bekannt_oder_kennen_muessen=None,
    modernisierung_auf_weg_beschluss=None, weg_beschluss_am=None,
    vereinfachte_erhoehung_geltend_gemacht=None, einordnungsnachweis=None,
):
    """§559c Absatz4: fünf Jahre Sperre, unbekannte gesetzliche Pflicht oder später WEG-Beschluss."""
    zugang = _datum(zugang_vereinfachte_erhoehung_am, "zugang_vereinfachte_erhoehung_am")
    neu = _datum(neue_geltendmachung_am, "neue_geltendmachung_am")
    if neu < zugang:
        _fehler("neue_geltendmachung_am", "Neue Geltendmachung darf nicht vor dem Ausgangszugang liegen.")
    eingaben = dict(zugang_vereinfachte_erhoehung_am=zugang_vereinfachte_erhoehung_am,
        neue_geltendmachung_am=neue_geltendmachung_am, gesetzliche_modernisierungspflicht=gesetzliche_modernisierungspflicht,
        pflicht_damals_bekannt_oder_kennen_muessen=pflicht_damals_bekannt_oder_kennen_muessen,
        modernisierung_auf_weg_beschluss=modernisierung_auf_weg_beschluss, weg_beschluss_am=weg_beschluss_am,
        vereinfachte_erhoehung_geltend_gemacht=vereinfachte_erhoehung_geltend_gemacht, einordnungsnachweis=einordnungsnachweis)
    for name in ("gesetzliche_modernisierungspflicht", "pflicht_damals_bekannt_oder_kennen_muessen",
        "modernisierung_auf_weg_beschluss", "vereinfachte_erhoehung_geltend_gemacht"):
        _wahrheitswert(eingaben[name], name)
    beschluss = None
    if weg_beschluss_am is not None or modernisierung_auf_weg_beschluss:
        beschluss = _datum(weg_beschluss_am, "weg_beschluss_am")
        if beschluss > neu:
            _fehler("weg_beschluss_am", "Beschluss darf nicht nach neuer Geltendmachung liegen.")
    _text(einordnungsnachweis, "einordnungsnachweis")
    wert = None
    if vereinfachte_erhoehung_geltend_gemacht:
        sperrende = _frist(zugang.isoformat(), 5, "jahre", "ereignis")
        beschluss_fruehestens = _tage_addieren(_frist(zugang.isoformat(), 2, "jahre", "ereignis"), 1)
        pflichtausnahme = gesetzliche_modernisierungspflicht and not pflicht_damals_bekannt_oder_kennen_muessen
        wegausnahme = modernisierung_auf_weg_beschluss and beschluss >= beschluss_fruehestens
        gesperrt = neu <= sperrende and not (pflichtausnahme or wegausnahme)
        wert = dict(sperrfrist_letzter_tag=sperrende.isoformat(), weg_beschluss_fruehestens=beschluss_fruehestens.isoformat(),
            pflichtausnahme=pflichtausnahme, wegausnahme=wegausnahme, neue_erhoehung_nach_559_559e_gesperrt=gesperrt)
    ergebnis = _ergebnis(wert, "fristdaten_und_wahrheitswerte", "BGB_MODERNISIERUNG_VEREINFACHUNG_SPERRFRIST", eingaben,
        [dict(operation="Fünfjährige Ereignisfrist ab Zugang und Zweijahresabstand für WEG-Beschluss berechnen; gesetzliche Ausnahmen prüfen")], eingaben.copy())
    ergebnis["status"] = "BERECHNET" if vereinfachte_erhoehung_geltend_gemacht else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = ["Rechtlich maßgebliche Erklärung im vereinfachten Verfahren und neue Erhöhung nach§559/§559e sowie maßnahmebezogene Ausnahmevoraussetzungen vorgegeben."]
    ergebnis["hinweise"] = ["Pflichtausnahme nur soweit die konkrete Maßnahme während des Zeitraums gesetzlich durchzuführen ist und die Pflicht bei früherer Geltendmachung weder bekannt war noch bekannt sein musste. Gemischte Maßnahmen getrennt beurteilen. WEG-Ausnahme erfordert Durchführung aufgrund des betreffenden Beschlusses; bloße WEG-Zugehörigkeit genügt nicht.", "Fünfjahressperre und frühester Beschluss nach voll abgelaufenen Ereignisjahren, keine automatische Werktagsverschiebung. Nicht gesperrt bedeutet nur keine Sperre aus§559c Absatz4, keinen fertigen Erhöhungsanspruch. Andere Voraussetzungen und spätere neue Sperren gesondert."]
    return ergebnis
