"""Zeitliche Grenze der Verwaltungsanordnung nach §§2209/2210 BGB."""

from .betraege import _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler, _frist, _text


def dauervollstreckung_zeitgrenze(
    erbfall_am=None,
    prueftag=None,
    fortdaueranordnung=None,
    fortdauerereignis_am=None,
    ereignisperson_juristische_person=None,
    verwaltungsanordnung_nach_2209=None,
    einordnungsnachweis=None,
):
    """Dreißigjahresgrenze oder wirksam angeordnete Fortdauer bis qualifiziertem Personenereignis."""
    erbfall = _datum(erbfall_am, "erbfall_am")
    tag = _datum(prueftag, "prueftag")
    if tag < erbfall:
        _fehler("prueftag", "Prüftag darf nicht vor Erbfall liegen.")
    art = _text(fortdaueranordnung, "fortdaueranordnung")
    if art not in [
        "keine",
        "tod_erbe",
        "tod_testamentsvollstrecker",
        "ereignis_erbe",
        "ereignis_testamentsvollstrecker",
    ]:
        _fehler(
            "fortdaueranordnung",
            "Keine Fortdauer oder qualifizierte Anordnung bis Tod/anderem Ereignis in Erben/Testamentsvollstrecker wählen.",
        )
    grundende = _frist(erbfall_am, 30, "jahre", "ereignis")
    ereignis = None
    if fortdauerereignis_am is not None:
        ereignis = _datum(fortdauerereignis_am, "fortdauerereignis_am")
        if ereignis < erbfall or ereignis > tag:
            _fehler(
                "fortdauerereignis_am",
                "Tatsächliches Fortdauerereignis muss zwischen Erbfall und Prüftag liegen; künftiges Ereignis als noch nicht eingetreten behandeln.",
            )
        if art == "keine":
            _fehler(
                "fortdauerereignis_am",
                "Ohne Fortdaueranordnung kein zugehöriges Fortdauerereignis eingeben.",
            )
    _wahrheitswert(
        ereignisperson_juristische_person, "ereignisperson_juristische_person"
    )
    _wahrheitswert(verwaltungsanordnung_nach_2209, "verwaltungsanordnung_nach_2209")
    _text(einordnungsnachweis, "einordnungsnachweis")
    eingaben = dict(
        erbfall_am=erbfall_am,
        prueftag=prueftag,
        fortdaueranordnung=fortdaueranordnung,
        fortdauerereignis_am=fortdauerereignis_am,
        ereignisperson_juristische_person=ereignisperson_juristische_person,
        verwaltungsanordnung_nach_2209=verwaltungsanordnung_nach_2209,
        einordnungsnachweis=einordnungsnachweis,
    )
    fortdauer = art != "keine" and not ereignisperson_juristische_person
    ende = ereignis if fortdauer else grundende
    if not fortdauer and ereignis is not None:
        ende = min(grundende, ereignis)
    wert = None
    if verwaltungsanordnung_nach_2209:
        wert = dict(
            dreissigjahresfristende=grundende.isoformat(),
            fortdauer_ueber_dreissig_jahre_zulaessig=fortdauer,
            massgebliche_zeitgrenze_am=ende.isoformat() if ende is not None else None,
            verwaltung_nach_zeitregel_beendet=ende is not None and tag >= ende,
        )
    ergebnis = _ergebnis(
        wert,
        "daten_und_wahrheitswerte",
        "BGB_DAUERVOLLSTRECKUNG_ZEITGRENZE",
        eingaben,
        [
            dict(
                operation="Dreißig Jahre ab Erbfall; qualifizierte Fortdauer bis Personenereignis ersetzt Grenze, bei juristischer Ereignisperson bleibt spätestens Grundende maßgeblich"
            )
        ],
        eingaben.copy(),
    )
    ergebnis["status"] = "BERECHNET" if wert is not None else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = [
        "Qualifizierte Verwaltungsanordnung nach§2209 und etwaige Fortdaueranordnung nach§2210 Satz2 vorgegeben; Prüfung zum Ende des Prüftags."
    ]
    ergebnis["hinweise"] = [
        "Die Dreißigjahresfrist läuft ab Erbfall, nicht erst ab Amtsantritt oder Beginn alleiniger Verwaltung nach Erledigung anderer Aufgaben. Fortdauer nur gemäß testamentarischer Anordnung bis Tod/anderem Ereignis in Person des Erben oder Testamentsvollstreckers, nicht beliebiger Dritter. Der Wortlaut§2210 Satz2 verlangt anders als§2163 Absatz1 kein gesondertes Leben beim Erbfall; nur Absatz2 wird verwiesen. Welche konkrete Person/Amtsnachfolge eine Anordnung erfasst, ist rechtlich zu bestimmen, nicht durch beliebige Auswechslung oder Nachfolgerkette verlängerbar. Bei natürlicher Ereignisperson ohne bereits eingetretenes Ereignis ist Zeitgrenze NULL (ereignisabhängig, nicht unbeschränkte Gesamtwirksamkeit). Bei juristischer Ereignisperson bleibt spätestes Ende dreißig Jahre; vorher eingetretenes wirksam angeordnetes Ereignis beendet früher. NULL als Ereigniseingabe bedeutet bis Prüftag nicht eingetreten, nicht unbekannt. Prüfung nur dieser Zeitregel, nicht sonstiger Beendigungsgründe, Amtsentlassung oder einzelner Vollstreckerbefugnisse. Tagesgenau zum Tagesende; Ereignis kann innerhalb des Tages früher wirken. Keine automatische Wochenendverschiebung."
    ]
    return ergebnis
