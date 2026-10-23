"""Zeitliche Beweislastvermutungen beim Verbrauchsgüterkauf."""
from .betraege import _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler, _frist, _text


def _beweislast_ergebnis(wert, kennung, eingaben, operation, hinweis):
    ergebnis = _ergebnis(wert, "daten_und_wahrheitswerte", kennung, eingaben,
        [dict(operation=operation)], eingaben.copy())
    ergebnis["status"] = "BERECHNET" if wert is not None else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = ["Konkreter Verbrauchsgüterkauf nach fester lokaler BGB-Fassung; Gefahrübergang und Auftreten des abweichenden Zustands rechtlich bestimmt."]
    ergebnis["hinweise"] = [hinweis, "Nur gesetzliche Beweislastvermutung, keine abschließende Mangelhaftigkeitsentscheidung und keine Verjährungsfrist. Keine automatische Werktagsverschiebung des tatsächlichen Auftretenszeitraums. Ereignistag und gesetzliches Zeitraumende einschließlich; untertägige Besonderheiten rechtlich vorab normalisieren."]
    return ergebnis


def kauf_beweislastvermutung(
    gefahruebergang_am=None, zustand_zeigt_sich_am=None, lebendes_tier=None,
    zustand_abweichend=None, vermutung_mit_art_unvereinbar=None,
    regel_477_absatz_eins_anwendbar=None, einordnungsnachweis=None,
):
    """§477 Absatz1: Jahr beziehungsweise sechs Monate mit Unvereinbarkeitsausnahme."""
    gefahr = _datum(gefahruebergang_am, "gefahruebergang_am")
    zeigt = _datum(zustand_zeigt_sich_am, "zustand_zeigt_sich_am")
    if zeigt < gefahr:
        _fehler("zustand_zeigt_sich_am", "Auftreten darf nicht vor Gefahrübergang liegen.")
    eingaben = dict(gefahruebergang_am=gefahruebergang_am, zustand_zeigt_sich_am=zustand_zeigt_sich_am,
        lebendes_tier=lebendes_tier, zustand_abweichend=zustand_abweichend,
        vermutung_mit_art_unvereinbar=vermutung_mit_art_unvereinbar,
        regel_477_absatz_eins_anwendbar=regel_477_absatz_eins_anwendbar,
        einordnungsnachweis=einordnungsnachweis)
    for name in tuple(eingaben)[2:-1]:
        _wahrheitswert(eingaben[name], name)
    _text(einordnungsnachweis, "einordnungsnachweis")
    wert = None
    if regel_477_absatz_eins_anwendbar:
        ende = _frist(gefahruebergang_am, 6 if lebendes_tier else 12, "monate", "ereignis")
        innerhalb = zeigt <= ende
        wert = dict(vermutungszeitraum_ende=ende.isoformat(), innerhalb_vermutungszeitraum=innerhalb,
            mangel_bei_gefahruebergang_vermutet=innerhalb and zustand_abweichend and not vermutung_mit_art_unvereinbar)
    return _beweislast_ergebnis(wert, "BGB_KAUF_BEWEISLASTVERMUTUNG", eingaben,
        "Ein Jahr seit Gefahrübergang, bei lebendem Tier sechs Monate; abweichenden Zustand und Unvereinbarkeitsausnahme verknüpfen",
        "Abweichung von§434/§475b sowie Unvereinbarkeit mit Art der Ware oder des mangelhaften Zustands ausdrücklich bewerten. Für dauerhaft bereitgestellte digitale Elemente die eigenständige Regel§477 Absatz2 beachten; nicht deren Zeitraum oder Aussage durch diese Funktion ersetzen.")


def kauf_digitale_beweislastvermutung(
    gefahruebergang_am=None, zustand_zeigt_sich_am=None, bereitstellung_ab=None,
    bereitstellung_bis=None, dauerhafte_bereitstellung_vereinbart=None,
    digitaler_zustand_abweichend=None, regel_477_absatz_zwei_anwendbar=None, einordnungsnachweis=None,
):
    """§477 Absatz2: tatsächlicher Bereitstellungszeitraum oder zwei Jahre seit Gefahrübergang."""
    gefahr = _datum(gefahruebergang_am, "gefahruebergang_am")
    zeigt = _datum(zustand_zeigt_sich_am, "zustand_zeigt_sich_am")
    beginn = _datum(bereitstellung_ab, "bereitstellung_ab")
    ende = _datum(bereitstellung_bis, "bereitstellung_bis") if bereitstellung_bis is not None else None
    if zeigt < gefahr:
        _fehler("zustand_zeigt_sich_am", "Auftreten darf nicht vor Gefahrübergang liegen.")
    if ende is not None and ende < beginn:
        _fehler("bereitstellung_bis", "Bereitstellungsende darf nicht vor Beginn liegen.")
    eingaben = dict(gefahruebergang_am=gefahruebergang_am, zustand_zeigt_sich_am=zustand_zeigt_sich_am,
        bereitstellung_ab=bereitstellung_ab, bereitstellung_bis=bereitstellung_bis,
        dauerhafte_bereitstellung_vereinbart=dauerhafte_bereitstellung_vereinbart,
        digitaler_zustand_abweichend=digitaler_zustand_abweichend,
        regel_477_absatz_zwei_anwendbar=regel_477_absatz_zwei_anwendbar,
        einordnungsnachweis=einordnungsnachweis)
    for name in tuple(eingaben)[4:-1]:
        _wahrheitswert(eingaben[name], name)
    _text(einordnungsnachweis, "einordnungsnachweis")
    wert = None
    if regel_477_absatz_zwei_anwendbar:
        zweijahre = _frist(gefahruebergang_am, 2, "jahre", "ereignis")
        innerhalb_zwei = zeigt <= zweijahre
        innerhalb_bereitstellung = zeigt >= beginn and (ende is None or zeigt <= ende)
        wert = dict(zweijahreszeitraum_ende=zweijahre.isoformat(), innerhalb_zweijahreszeitraum=innerhalb_zwei,
            innerhalb_bereitstellungsdauer=innerhalb_bereitstellung,
            mangel_waehrend_bisheriger_bereitstellung_vermutet=(dauerhafte_bereitstellung_vereinbart and
                digitaler_zustand_abweichend and (innerhalb_zwei or innerhalb_bereitstellung)))
    return _beweislast_ergebnis(wert, "BGB_KAUF_DIGITALE_BEWEISLASTVERMUTUNG", eingaben,
        "Auftreten innerhalb zweier Jahre seit Gefahrübergang ODER während vereinbarter dauerhafter Bereitstellung; digitale Abweichung prüfen",
        "Nur digitale Elemente einer Ware mit vereinbarter dauerhafter Bereitstellung; kein allgemeiner Digitalproduktvertrag. NULL beim Bereitstellungsende bedeutet rechtlich unbefristet laufend, nicht unbekannt. Vereinbarte Bereitstellung darf länger oder kürzer als zwei Jahre sein; der Zweijahresweg bleibt eigenständig. Vermutung betrifft die bisherige Bereitstellungsdauer und nicht nur den Gefahrübergang. Keine zusätzliche Unvereinbarkeitsausnahme ausAbsatz1 in den Wortlaut vonAbsatz2 übernehmen.")
