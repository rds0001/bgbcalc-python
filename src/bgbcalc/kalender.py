"""Kalenderregeln der festen lokalen BGB-Fassung, ohne Netzwerkzugriff."""
from calendar import monthrange
from datetime import date, timedelta
import re

QUELLENFASSUNG = "BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb"


class Berechnungsfehler(ValueError):
    """Strukturierter Fehler ohne scheinbar gültigen Ergebniswert."""

    def __init__(self, status, parameter, meldung):
        self.status = status
        self.parameter = parameter
        super().__init__(meldung)


def _fehler(parameter, meldung, status="EINGABE_UNGUELTIG"):
    raise Berechnungsfehler(status, parameter, meldung)


def _vorhanden(wert, parameter):
    if wert is None:
        _fehler(parameter, "Pflichteingabe fehlt.", "EINGABE_FEHLT")


def _text(wert, parameter):
    _vorhanden(wert, parameter)
    if not isinstance(wert, str) or not wert.strip():
        _fehler(parameter, "Nichtleere Zeichenfolge erforderlich.")
    return wert


def _auswahl(wert, parameter, moeglichkeiten):
    _text(wert, parameter)
    if wert not in moeglichkeiten:
        _fehler(parameter, "Unzulässige Auswahl.")
    return wert


def _ganzzahl(wert, parameter, minimum=0, maximum=3652059):
    _vorhanden(wert, parameter)
    if type(wert) is not int or not minimum <= wert <= maximum:
        _fehler(parameter, f"Ganzzahl zwischen {minimum} und {maximum} erforderlich.")
    return wert


def _datum(wert, parameter):
    _text(wert, parameter)
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", wert):
        _fehler(parameter, "ISO-Datum mit vierstelligem Jahr erforderlich.")
    try:
        return date.fromisoformat(wert)
    except ValueError:
        _fehler(parameter, "Ungültiger Kalendertag.")


def _tage_addieren(datum, tage):
    try:
        return datum + timedelta(days=tage)
    except (OverflowError, ValueError):
        _fehler("datum", "Ergebnis außerhalb des Datumsbereichs 0001..9999.")


def _monatsende(anfang, monate, tagesbeginn):
    zielindex = (anfang.year - 1) * 12 + anfang.month - 1 + monate
    zieljahr, zielmonat = zielindex // 12 + 1, zielindex % 12 + 1
    zieltag = anfang.day - int(tagesbeginn)
    if zieltag == 0:
        zielindex -= 1
        zieljahr, zielmonat = zielindex // 12 + 1, zielindex % 12 + 1
        zieltag = 31
    if not 1 <= zieljahr <= 9999:
        _fehler("anzahl", "Zielmonat außerhalb des Datumsbereichs.")
    return date(zieljahr, zielmonat, min(zieltag, monthrange(zieljahr, zielmonat)[1]))


def _frist(anfangstag, anzahl, einheit, beginnart):
    anfang = _datum(anfangstag, "anfangstag")
    _ganzzahl(anzahl, "anzahl", 1)
    _auswahl(beginnart, "beginnart", ("ereignis", "tagesbeginn"))
    _auswahl(einheit, "einheit", (
        "tage", "wochen", "monate", "jahre", "halbjahre", "vierteljahre", "halber_monat"
    ))
    mitgezaehlt = beginnart == "tagesbeginn"
    if einheit == "halber_monat":
        if anzahl != 1:
            _fehler("anzahl", "Ein halber Monat ist als einzelne 15-Tage-Frist definiert.")
        return _tage_addieren(anfang, 15 - int(mitgezaehlt))
    if einheit in ("tage", "wochen"):
        return _tage_addieren(anfang, anzahl * (7 if einheit == "wochen" else 1) - int(mitgezaehlt))
    monate = anzahl * {"monate": 1, "jahre": 12, "halbjahre": 6, "vierteljahre": 3}[einheit]
    return _monatsende(anfang, monate, mitgezaehlt)


def _ergebnis(wert, einheit, regel_id, eingaben, schritte, nutzervorgaben=None):
    return {
        "wert": wert, "einheit": einheit, "regel_id": regel_id, "regelversion": "1",
        "quellenfassung": QUELLENFASSUNG, "eingaben": eingaben,
        "nutzervorgaben": {} if nutzervorgaben is None else nutzervorgaben,
        "rechenschritte": schritte,
        "annahmen": ["Feste lokale BGB-Fassung; Anwendbarkeit der Auslegungsvorschrift vorausgesetzt."],
        "hinweise": ["Keine automatische Feiertagsverschiebung außerhalb der ausdrücklichen §-193-Funktion."],
        "status": "BERECHNET",
    }


def fristende(anfangstag=None, anzahl=None, einheit=None, beginnart=None):
    """Letzten Fristtag nach §§ 187–189 liefern; Ablauf am Tagesende."""
    wert = _frist(anfangstag, anzahl, einheit, beginnart).isoformat()
    return _ergebnis(wert, "datum", "BGB_FRIST_KALENDER", dict(
        anfangstag=anfangstag, anzahl=anzahl, einheit=einheit, beginnart=beginnart
    ), [{"operation": "Kalenderfrist nach §§ 187–189", "ergebnis": wert}])


def fristende_monate_halb(anfangstag=None, ganze_monate=None, beginnart=None):
    """Ganze Monate zuerst, danach 15 Tage (§ 189 Abs. 2)."""
    zwischen = _frist(anfangstag, ganze_monate, "monate", beginnart)
    wert = _tage_addieren(zwischen, 15).isoformat()
    return _ergebnis(wert, "datum", "BGB_FRIST_MONATE_HALB", dict(
        anfangstag=anfangstag, ganze_monate=ganze_monate, beginnart=beginnart
    ), [{"operation": "Ganze Monate", "ergebnis": zwischen.isoformat()},
        {"operation": "Anschließend 15 Tage", "ergebnis": wert}])


def fristverlaengerung(bisheriges_fristende=None, anzahl=None, einheit=None):
    """Verlängerung vom Ablauf der bisherigen Frist an (§ 190)."""
    wert = _frist(bisheriges_fristende, anzahl, einheit, "ereignis").isoformat()
    return _ergebnis(wert, "datum", "BGB_FRIST_VERLAENGERUNG", dict(
        bisheriges_fristende=bisheriges_fristende, anzahl=anzahl, einheit=einheit
    ), [{"operation": "Voriger Ablauf als neues Ereignis", "ergebnis": wert}])


def zeitraum_tage(anzahl=None, einheit=None, nicht_zusammenhaengend=None):
    """30/365 ausschließlich für nicht zusammenhängende Zeiträume (§ 191)."""
    _ganzzahl(anzahl, "anzahl")
    _auswahl(einheit, "einheit", ("monate", "jahre"))
    _vorhanden(nicht_zusammenhaengend, "nicht_zusammenhaengend")
    if nicht_zusammenhaengend is not True:
        _fehler("nicht_zusammenhaengend", "§ 191 setzt nicht zusammenhängenden Zeitraum voraus.")
    faktor = 30 if einheit == "monate" else 365
    wert = anzahl * faktor
    return _ergebnis(wert, "tage", "BGB_ZEITRAUM_UNZUSAMMENHAENGEND", dict(
        anzahl=anzahl, einheit=einheit, nicht_zusammenhaengend=nicht_zusammenhaengend
    ), [{"operation": "Anzahl mal gesetzliche Tage je Einheit", "faktor": faktor, "ergebnis": wert}])


def monatstermin(jahr=None, monat=None, lage=None):
    """Monatsanfang, Monatsmitte oder Monatsende nach § 192."""
    _ganzzahl(jahr, "jahr", 1, 9999)
    _ganzzahl(monat, "monat", 1, 12)
    _auswahl(lage, "lage", ("anfang", "mitte", "ende"))
    tag = {"anfang": 1, "mitte": 15, "ende": monthrange(jahr, monat)[1]}[lage]
    wert = date(jahr, monat, tag).isoformat()
    return _ergebnis(wert, "datum", "BGB_MONATSTERMIN", dict(
        jahr=jahr, monat=monat, lage=lage
    ), [{"operation": "Monatstermin nach § 192", "ergebnis": wert}])


def werktagsverschiebung(datum=None, anwendungsfall=None, feiertage=None, ort=None,
                        kalenderquelle=None, kalender_von=None, kalender_bis=None):
    """§ 193 mit ausdrücklich bestätigtem örtlichem Feiertagskalender."""
    tag = _datum(datum, "datum")
    _auswahl(anwendungsfall, "anwendungsfall", ("leistung", "willenserklaerung"))
    _text(ort, "ort")
    _text(kalenderquelle, "kalenderquelle")
    von, bis = _datum(kalender_von, "kalender_von"), _datum(kalender_bis, "kalender_bis")
    _vorhanden(feiertage, "feiertage")
    if not isinstance(feiertage, list):
        _fehler("feiertage", "Explizite Liste von Feiertagen erforderlich.")
    feiertagsmenge = {_datum(t, "feiertage") for t in feiertage}
    if not von <= tag <= bis or any(not von <= t <= bis for t in feiertagsmenge):
        _fehler("kalender", "Datum/Feiertag außerhalb des bestätigten Kalenderbereichs.")
    uebersprungen = []
    while tag.weekday() >= 5 or tag in feiertagsmenge:
        uebersprungen.append(tag.isoformat())
        tag = _tage_addieren(tag, 1)
        if tag > bis:
            _fehler("kalender_bis", "Feiertagskalender deckt den nächsten Prüftag nicht ab.")
    wert = tag.isoformat()
    return _ergebnis(wert, "datum", "BGB_WERKTAG_ERSATZ", dict(
        datum=datum, anwendungsfall=anwendungsfall, feiertage=list(feiertage),
        ort=ort, kalenderquelle=kalenderquelle, kalender_von=kalender_von, kalender_bis=kalender_bis
    ), [{"operation": "Unzulässige Tage übersprungen", "tage": uebersprungen, "ergebnis": wert}],
        {"ort": ort, "kalenderquelle": kalenderquelle, "vollstaendigkeit": "Vom Nutzer für den angegebenen Bereich bestätigt."})


def lebensalter_beginn(geburtsdatum=None, lebensjahre=None):
    """Beginn nach Vollendung von Lebensjahren, ohne §-193-Verschiebung."""
    geburt = _datum(geburtsdatum, "geburtsdatum")
    _ganzzahl(lebensjahre, "lebensjahre")
    wert = (geburt if lebensjahre == 0 else
            _tage_addieren(_monatsende(geburt, lebensjahre * 12, True), 1)).isoformat()
    return _ergebnis(wert, "datum", "BGB_LEBENSALTER_BEGINN", dict(
        geburtsdatum=geburtsdatum, lebensjahre=lebensjahre
    ), [{"operation": "Geburtstag mitzählen, Beginn nach Vollendung", "ergebnis": wert}])


def volljaehrigkeitsbeginn(geburtsdatum=None):
    """Vollendung des 18. Lebensjahres nach § 2."""
    wert = lebensalter_beginn(geburtsdatum, 18)["wert"]
    return _ergebnis(wert, "datum", "BGB_VOLLJAEHRIGKEIT",
                     {"geburtsdatum": geburtsdatum},
                     [{"operation": "Vollendung von 18 Lebensjahren", "ergebnis": wert}])
