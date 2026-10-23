"""Mindestablauf nach §§ 210/211 aus ausdrücklich eingeordneten Schutzereignissen."""

from .betraege import _wahrheitswert
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _ganzzahl, _monatsende, _vorhanden


def verjaehrung_ablaufhemmung_mindestablauf(
    schutzfall=None,
    schutzbeendende_ereignisse=None,
    fristdauer=None,
    fristeinheit=None,
    rechnerischer_letzter_tag=None,
    prozessfaehigkeit_bei_beschraenkter_geschaeftsfaehigkeit=None,
    ablaufhemmung_anwendbar=None,
):
    """Frühestes Schutzende und längeren Ablauf aus bisheriger Frist und Mindestnachlauf wählen."""
    _auswahl(schutzfall, "schutzfall", ("vertretungsmangel", "nachlass"))
    _ganzzahl(fristdauer, "fristdauer", 1)
    _auswahl(fristeinheit, "fristeinheit", ("tage", "wochen", "monate", "jahre"))
    bisher = _datum(rechnerischer_letzter_tag, "rechnerischer_letzter_tag")
    _wahrheitswert(
        prozessfaehigkeit_bei_beschraenkter_geschaeftsfaehigkeit,
        "prozessfaehigkeit_bei_beschraenkter_geschaeftsfaehigkeit",
    )
    _wahrheitswert(ablaufhemmung_anwendbar, "ablaufhemmung_anwendbar")
    _vorhanden(schutzbeendende_ereignisse, "schutzbeendende_ereignisse")
    if not isinstance(schutzbeendende_ereignisse, list) or len(schutzbeendende_ereignisse) > 3:
        _fehler("schutzbeendende_ereignisse", "Liste mit höchstens drei Schutzereignissen erforderlich.")
    erlaubt = (
        ("unbeschraenkte_geschaeftsfaehigkeit", "vertretungsmangel_behoben")
        if schutzfall == "vertretungsmangel" else
        ("erbschaft_angenommen", "nachlassinsolvenz_eroeffnet",
         "geltendmachung_durch_oder_gegen_vertreter_moeglich")
    )
    termine = []
    gesehen = set()
    for eintrag in schutzbeendende_ereignisse:
        if not isinstance(eintrag, dict) or set(eintrag) != {"ereignis", "datum"}:
            _fehler("schutzbeendende_ereignisse", "Genau Ereignisart und Datum erforderlich.")
        _auswahl(eintrag["ereignis"], "ereignis", erlaubt)
        if eintrag["ereignis"] in gesehen:
            _fehler("schutzbeendende_ereignisse", "Ereignisart nicht mehrfach angeben.")
        gesehen.add(eintrag["ereignis"])
        termine.append((eintrag["ereignis"], _datum(eintrag["datum"], "datum")))
    eingaben = dict(
        schutzfall=schutzfall, schutzbeendende_ereignisse=schutzbeendende_ereignisse,
        fristdauer=fristdauer, fristeinheit=fristeinheit,
        rechnerischer_letzter_tag=rechnerischer_letzter_tag,
        prozessfaehigkeit_bei_beschraenkter_geschaeftsfaehigkeit=prozessfaehigkeit_bei_beschraenkter_geschaeftsfaehigkeit,
        ablaufhemmung_anwendbar=ablaufhemmung_anwendbar,
    )
    anwendbar = ablaufhemmung_anwendbar and not (
        schutzfall == "vertretungsmangel" and prozessfaehigkeit_bei_beschraenkter_geschaeftsfaehigkeit
    )
    schritte = [{"operation": "Schutzfall und Prozessfähigkeitsausnahme", "anwendbar": anwendbar}]
    wert = None
    if anwendbar:
        if not termine:
            _fehler("schutzbeendende_ereignisse", "Kein Schutzende angegeben.", "EINGABE_FEHLT")
        schutzende = min(datum for _, datum in termine)
        sechsmonatsende = _monatsende(schutzende, 6, False)
        if fristeinheit == "jahre":
            kurz = False
        elif fristeinheit == "monate":
            kurz = fristdauer < 6
        else:
            tage = fristdauer * (7 if fristeinheit == "wochen" else 1)
            kurz = tage < (sechsmonatsende - schutzende).days
        mindest = (
            _frist(schutzende.isoformat(), fristdauer, fristeinheit, "ereignis")
            if kurz else sechsmonatsende
        )
        wert = dict(
            schutzende_am=schutzende.isoformat(),
            nachlauf_kuerzer_als_sechs_monate=kurz,
            mindestablauf=mindest.isoformat(),
            rechnerischer_letzter_tag=max(bisher, mindest).isoformat(),
        )
        schritte.extend([
            {"operation": "Frühestes schutzbeendendes Ereignis",
             "massgebliche_ereignisse": [art for art, datum in termine if datum == schutzende],
             "datum": schutzende.isoformat()},
            {"operation": "Sechs Monate oder kürzere volle Verjährungsfrist; späteren Ablauf auswählen",
             "ergebnis": wert},
        ])
    ergebnis = _ergebnis(
        wert, "datum", "BGB_VERJAEHRUNG_ABLAUFHEMMUNG_MINDESTABLAUF",
        eingaben, schritte, eingaben.copy(),
    )
    ergebnis["status"] = "BERECHNET" if anwendbar else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = [
        "Feste lokale BGB-Fassung; Schutzfall, Fristdauer und sämtliche maßgeblichen Beendigungsereignisse rechtlich vorgegeben."
    ]
    ergebnis["hinweise"] = [
        "Mindestablauf nach §§ 210/211, keine Addition von Hemmungstagen oder sechs Monaten zum bisherigen Fristende.",
        "Weitere Schutzperioden, Neubeginn, konkurrierende Fristen und gegebenenfalls Werktagsverschiebung bleiben gesondert; kein abschließender Verjährungstag."
    ]
    return ergebnis
