"""Zeitliche und persönliche Ausschlüsse des Schenkungswiderrufs§§532/534."""
from .betraege import _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler, _frist, _text


def schenkung_widerrufsausschluss(
    kenntnis_widerrufsvoraussetzungen_am=None, massgebliches_jahresfristende=None,
    widerrufserklaerung_am=None, schenker_hat_verziehen=None, beschenkter_bereits_verstorben=None,
    pflicht_oder_anstandsschenkung=None, einordnungsnachweis=None,
):
    """§§532/534: Jahresfrist, Verzeihung, Tod des Beschenkten und privilegierte Schenkung."""
    _datum(kenntnis_widerrufsvoraussetzungen_am, "kenntnis_widerrufsvoraussetzungen_am")
    ende = _datum(massgebliches_jahresfristende, "massgebliches_jahresfristende")
    erklaerung = _datum(widerrufserklaerung_am, "widerrufserklaerung_am")
    grundende = _frist(kenntnis_widerrufsvoraussetzungen_am, 1, "jahre", "ereignis")
    if ende < grundende:
        _fehler("massgebliches_jahresfristende", "Maßgebliches Fristende darf die gesetzliche Jahresgrundfrist nicht verkürzen.")
    eingaben = dict(kenntnis_widerrufsvoraussetzungen_am=kenntnis_widerrufsvoraussetzungen_am,
        massgebliches_jahresfristende=massgebliches_jahresfristende, widerrufserklaerung_am=widerrufserklaerung_am,
        schenker_hat_verziehen=schenker_hat_verziehen, beschenkter_bereits_verstorben=beschenkter_bereits_verstorben,
        pflicht_oder_anstandsschenkung=pflicht_oder_anstandsschenkung, einordnungsnachweis=einordnungsnachweis)
    for name in tuple(eingaben)[3:-1]:
        _wahrheitswert(eingaben[name], name)
    _text(einordnungsnachweis, "einordnungsnachweis")
    abgelaufen = erklaerung > ende
    wert = dict(rechnerisches_jahresfristende=grundende.isoformat(), jahresfrist_ueberschritten=abgelaufen,
        widerruf_nach_532_oder_534_ausgeschlossen=(abgelaufen or schenker_hat_verziehen or
            beschenkter_bereits_verstorben or pflicht_oder_anstandsschenkung))
    ergebnis = _ergebnis(wert, "daten_und_wahrheitswerte", "BGB_SCHENKUNG_WIDERRUFSAUSSCHLUSS", eingaben,
        [dict(operation="Jahresfrist seit Kenntnis der Widerrufsvoraussetzungen und alternative Ausschlüsse Verzeihung, Beschenktentod, Pflicht-/Anstandsschenkung prüfen")], eingaben.copy())
    ergebnis["annahmen"] = ["Konkrete Schenkung, Kenntnis des Widerrufsberechtigten, rechtlich maßgeblicher Erklärungstag und Jahresfristkorrekturen vorgegeben; feste lokale BGB-Fassung."]
    ergebnis["hinweise"] = ["Nur Ausschlüsse§§532/534. FALSE bestätigt keinen Widerruf: grober Undank und Erbenvoraussetzungen§530, Erklärung gegenüber Beschenktem§531, möglicher Verzicht§533 und sonstige Voraussetzungen separat. Kenntnis der Voraussetzungen des Rechts, nicht automatisch Tag der Schenkung oder ersten bloßen Verdachts. Maßgebliches Jahresende nur mit rechtlich zulässigen belegten Kalenderkorrekturen, keine frei wählbare Verlängerung. Verzeihung durch Schenker und Tod des Beschenkten zum maßgeblichen Erklärungszeitpunkt ausdrücklich einordnen; nicht den Tod des Schenkers an dessen Stelle setzen. Taggenaues Modell, untertägige Reihenfolge rechtlich vorab prüfen."]
    return ergebnis
