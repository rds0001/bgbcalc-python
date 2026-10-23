"""Unterhaltsrechenregeln mit extern belegten Geldgrößen und Rechtsbewertungen."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _ganzzahl, _text, lebensalter_beginn
from .zahlen import _bruch, _dezimalzahl, _multiplizieren, _runden, _subtrahieren
from .zinsen import _bruchteile


def unterhaltsaltersstufe(geburtsdatum=None, stichtag=None):
    """§ 1612a Abs. 1/3: höhere Minderjährigenstufe ab maßgeblichem Monatsbeginn."""
    geburt = _datum(geburtsdatum, "geburtsdatum")
    tag = _datum(stichtag, "stichtag")
    if geburt > tag:
        _fehler("geburtsdatum", "Geburt muss spätestens am Stichtag liegen.")
    grenzen = {}
    for alter in (6, 12, 18):
        erreicht = lebensalter_beginn(geburtsdatum, alter)["wert"] if geburt.year + alter <= 9999 else None
        grenzen[str(alter)] = erreicht if alter == 18 or erreicht is None else erreicht[:8] + "01"
    stufe = 1
    if grenzen["6"] is not None and stichtag >= grenzen["6"]:
        stufe = 2
    if grenzen["12"] is not None and stichtag >= grenzen["12"]:
        stufe = 3
    minderjaehrig = grenzen["18"] is None or stichtag < grenzen["18"]
    eingaben = dict(geburtsdatum=geburtsdatum, stichtag=stichtag)
    ergebnis = _ergebnis(stufe if minderjaehrig else None, "altersstufe", "BGB_UNTERHALT_ALTERSSTUFE",
                         eingaben, [{"operation": "Altersstufen ab Monatsbeginn; Volljährigkeit taggenau",
                                     "grenzen": grenzen}], eingaben.copy())
    ergebnis["status"] = "BERECHNET" if minderjaehrig else "NICHT_ANWENDBAR"
    ergebnis["hinweise"] = ["Keine automatische Prüfung des Unterhaltsanspruchs oder Feiertagsverschiebung."]
    return ergebnis


def mindestunterhalt_aus_existenzminimum(
    jaehrliches_existenzminimum=None, altersstufe=None, quellenangabe=None,
):
    """§ 1612a Abs. 1/2: Jahresbetrag auf monatlichen Altersbetrag umrechnen."""
    grundlage = _geld(jaehrliches_existenzminimum)
    if grundlage == 0:
        _fehler("jaehrliches_existenzminimum", "Positive Jahresgrundlage erforderlich.")
    _ganzzahl(altersstufe, "altersstufe", 1, 3)
    _text(quellenangabe, "quellenangabe")
    faktor = (87, 100, 117)[altersstufe - 1]
    ungerundet = _multiplizieren(grundlage, _bruch(faktor, 1200))
    wert = _dezimalzahl(_runden(ungerundet, 0, "auf"))
    ergebnis = _geld_ergebnis(wert, "BGB_UNTERHALT_EXISTENZMINIMUM", dict(
        jaehrliches_existenzminimum=jaehrliches_existenzminimum, altersstufe=altersstufe,
        quellenangabe=quellenangabe),
        [{"operation": "Jahresbetrag durch zwölf mal Altersfaktor", "altersfaktor_prozent": faktor,
          "ungerundeter_monatsbetrag": _bruchteile(ungerundet)},
         {"operation": "Auf volle Euro aufrunden"}])
    ergebnis["hinweise"] = ["Rechenrelation aus vorgegebenem Existenzminimum; keine amtliche Festsetzung.",
                            "Maßgebliche Mindestunterhaltsverordnung und Zeitraum gesondert bestimmen.",
                            "Gesetzliche Aufrundung auf volle Euro."]
    return ergebnis


def dynamischer_kindesunterhalt(mindestunterhalt=None, prozentsatz=None, mindestunterhaltsnachweis=None):
    """§ 1612a Abs. 2: Satz abschneiden, dann den Unterhaltsbetrag aufrunden."""
    minimum, satz = _geld(mindestunterhalt), _geld(prozentsatz)
    if minimum <= 0 or minimum.denominator != 1:
        _fehler("mindestunterhalt", "Positiver Mindestunterhalt in vollen Euro erforderlich.")
    _text(mindestunterhaltsnachweis, "mindestunterhaltsnachweis")
    begrenzt = _dezimalzahl(_runden(satz, 1, "gegen_null"))
    ungerundet = _multiplizieren(minimum, _multiplizieren(begrenzt, _bruch(1, 100)))
    wert = _dezimalzahl(_runden(ungerundet, 0, "auf"))
    ergebnis = _geld_ergebnis(wert, "BGB_UNTERHALT_DYNAMISCH", dict(
        mindestunterhalt=mindestunterhalt, prozentsatz=prozentsatz,
        mindestunterhaltsnachweis=mindestunterhaltsnachweis),
        [{"operation": "Prozentsatz nach einer Dezimalstelle abschneiden",
          "begrenzter_prozentsatz": _bruchteile(begrenzt)},
         {"operation": "Mindestunterhalt mal Prozentsatz/100", "ungerundeter_betrag": _bruchteile(ungerundet)},
         {"operation": "Auf volle Euro aufrunden"}])
    ergebnis["hinweise"] = ["Mindestunterhalt, Altersstufe, Zeitraum und Prozentsatz rechtlich vorgegeben.",
                            "Prozentsatz abgeschnitten; Unterhaltsbetrag gesetzlich auf volle Euro aufgerundet.",
                            "Kindergeldanrechnung und Leistungsfähigkeit gesondert."]
    return ergebnis


def kindbezogene_leistung_anrechnen(
    barbedarf=None, leistungsbetrag=None, erhoehung_nichtgemeinschaftliches_kind=None,
    betreuung_durch_elternteil=None, leistungsart=None, regelmaessig_wiederkehrend=None,
    kindergeld_ausgeschlossen=None,
):
    """§§ 1612b/c: kindbezogene Leistung in gesetzlichem Umfang bedarfsmindernd."""
    eingaben = dict(barbedarf=barbedarf, leistungsbetrag=leistungsbetrag,
                    erhoehung_nichtgemeinschaftliches_kind=erhoehung_nichtgemeinschaftliches_kind,
                    betreuung_durch_elternteil=betreuung_durch_elternteil, leistungsart=leistungsart,
                    regelmaessig_wiederkehrend=regelmaessig_wiederkehrend,
                    kindergeld_ausgeschlossen=kindergeld_ausgeschlossen)
    bedarf, leistung = _geld(barbedarf), _geld(leistungsbetrag)
    erhoehung = _geld(erhoehung_nichtgemeinschaftliches_kind)
    if erhoehung > leistung:
        _fehler("erhoehung_nichtgemeinschaftliches_kind", "Erhöhung darf Leistungsbetrag nicht übersteigen.")
    for parameter in ("betreuung_durch_elternteil", "regelmaessig_wiederkehrend", "kindergeld_ausgeschlossen"):
        _wahrheitswert(eingaben[parameter], parameter)
    _auswahl(leistungsart, "leistungsart", ("kindergeld", "ersatzleistung"))
    if leistungsart == "kindergeld" and kindergeld_ausgeschlossen:
        _fehler("kindergeld_ausgeschlossen", "Kindergeld und dessen Ausschluss widersprechen sich.")
    anwendbar = leistungsart == "kindergeld" or (regelmaessig_wiederkehrend and kindergeld_ausgeschlossen)
    ergebnis = _geld_ergebnis(_bruch(0) if anwendbar else None, "BGB_KINDLEISTUNG_ANRECHNUNG",
                             eingaben, [{"operation": "Kindergeld oder einschlägige Ersatzleistung",
                                         "anwendbar": anwendbar}])
    if anwendbar:
        relevant = _multiplizieren(_subtrahieren(leistung, erhoehung),
                                   _bruch(1, 2) if betreuung_durch_elternteil else _bruch(1))
        deckung = min(bedarf, relevant)
        rest = _subtrahieren(bedarf, deckung)
        ergebnis["wert"] = dict(bedarfsrelevante_leistung=_bruchteile(relevant),
                                bedarfsdeckung=_bruchteile(deckung), verbleibender_barbedarf=_bruchteile(rest))
        ergebnis["rechenschritte"].append(dict(
            operation="Nicht relevante Erhöhung abziehen; Leistung hälftig oder voll bis Bedarf anrechnen",
            haelftige_anrechnung=betreuung_durch_elternteil))
    return ergebnis
