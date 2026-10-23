"""Kenntnisunabhängige Grundfristen nach § 199 Absätzen 2 bis 5."""

from .betraege import _wahrheitswert
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _monatsende


def verjaehrung_kenntnisunabhaengige_grundfrist(
    anspruchsart=None,
    entstehung_oder_zuwiderhandlung_am=None,
    schadensausloesendes_ereignis_am=None,
    kenntnisunabhaengige_frist_anwendbar=None,
):
    """Ausgewählte Frist berechnen; bei Absatz 3 den früheren Ablauf liefern."""
    _auswahl(anspruchsart, "anspruchsart", (
        "leben_koerper_gesundheit_freiheit", "sonstiger_schadensersatz",
        "erbfall", "sonstiger_anspruch",
    ))
    eingaben = dict(
        anspruchsart=anspruchsart,
        entstehung_oder_zuwiderhandlung_am=entstehung_oder_zuwiderhandlung_am,
        schadensausloesendes_ereignis_am=schadensausloesendes_ereignis_am,
        kenntnisunabhaengige_frist_anwendbar=kenntnisunabhaengige_frist_anwendbar,
    )
    anknuepfungen = []
    entstehung = None
    if anspruchsart == "leben_koerper_gesundheit_freiheit":
        if entstehung_oder_zuwiderhandlung_am is not None:
            _fehler("entstehung_oder_zuwiderhandlung_am", "Für diese Fallgruppe nicht anzugeben.")
    else:
        entstehung = _datum(
            entstehung_oder_zuwiderhandlung_am, "entstehung_oder_zuwiderhandlung_am"
        )
        anknuepfungen.append(("entstehung", entstehung, 30 if anspruchsart == "erbfall" else 10))
    if anspruchsart in ("leben_koerper_gesundheit_freiheit", "sonstiger_schadensersatz"):
        ereignis = _datum(schadensausloesendes_ereignis_am, "schadensausloesendes_ereignis_am")
        if entstehung is not None and ereignis > entstehung:
            _fehler("schadensausloesendes_ereignis_am", "Ereignis darf nicht nach Entstehung liegen.")
        anknuepfungen.append(("ereignis", ereignis, 30))
    elif schadensausloesendes_ereignis_am is not None:
        _fehler("schadensausloesendes_ereignis_am", "Für diese Fallgruppe nicht anzugeben.")
    _wahrheitswert(kenntnisunabhaengige_frist_anwendbar, "kenntnisunabhaengige_frist_anwendbar")
    wert = None
    if kenntnisunabhaengige_frist_anwendbar:
        fristen = [
            dict(
                anknuepfung=art, beginnereignis=datum.isoformat(), jahre=jahre,
                rechnerischer_letzter_tag=_monatsende(datum, jahre * 12, False).isoformat(),
            )
            for art, datum, jahre in anknuepfungen
        ]
        wert = dict(
            fristen=fristen,
            rechnerischer_letzter_tag=min(f["rechnerischer_letzter_tag"] for f in fristen),
        )
    ergebnis = _ergebnis(
        wert, "datum", "BGB_VERJAEHRUNG_KENNTNISUNABHAENGIGE_GRUNDFRIST", eingaben,
        [{"operation": "Kenntnisunabhängige Jahresfristen ohne Jahresschlussverschiebung",
          "ergebnis": wert}], eingaben.copy(),
    )
    ergebnis["status"] = (
        "BERECHNET" if kenntnisunabhaengige_frist_anwendbar else "NICHT_ANWENDBAR"
    )
    ergebnis["annahmen"] = [
        "Feste lokale BGB-Fassung; Anspruchsgruppe und rechtlich maßgebliche Ereignisse ausdrücklich vorgegeben."
    ]
    ergebnis["hinweise"] = [
        "Enddaten bezeichnen den Tagesschluss; kein abschließender Verjährungstag.",
        "Frühere kenntnisabhängige Frist, Hemmung, Ablaufhemmung, Neubeginn, Sonderregeln und gegebenenfalls Werktagsverschiebung bleiben gesondert."
    ]
    return ergebnis
