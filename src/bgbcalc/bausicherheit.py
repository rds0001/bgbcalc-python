"""Beträge der Bauhandwerkersicherung und Verbraucher-Herstellungssicherheit."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _auswahl, _fehler
from .zahlen import _addieren, _bruch, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile


def bau_sicherungsbetrag(
    offene_verguetung=None, aufrechenbare_gegenforderung=None,
    gegenforderung_unstreitig=None, gegenforderung_rechtskraeftig=None,
    bestellerart=None, baubetreuer_bevollmaechtigt=None,
):
    """§ 650f Abs. 1/6: offene Vergütung zuzüglich zehn Prozent Nebenforderungen."""
    eingaben = dict(offene_verguetung=offene_verguetung,
                    aufrechenbare_gegenforderung=aufrechenbare_gegenforderung,
                    gegenforderung_unstreitig=gegenforderung_unstreitig,
                    gegenforderung_rechtskraeftig=gegenforderung_rechtskraeftig,
                    bestellerart=bestellerart, baubetreuer_bevollmaechtigt=baubetreuer_bevollmaechtigt)
    verguetung, gegenforderung = _geld(offene_verguetung), _geld(aufrechenbare_gegenforderung)
    for parameter in ("gegenforderung_unstreitig", "gegenforderung_rechtskraeftig", "baubetreuer_bevollmaechtigt"):
        _wahrheitswert(eingaben[parameter], parameter)
    _auswahl(bestellerart, "bestellerart",
             ("sonstiger", "oeffentlich_insolvenzunfaehig", "verbraucherbau", "bautraeger_verbraucher"))
    anwendbar = bestellerart != "oeffentlich_insolvenzunfaehig" and (
        bestellerart == "sonstiger" or baubetreuer_bevollmaechtigt)
    abzug = gegenforderung if gegenforderung_unstreitig or gegenforderung_rechtskraeftig else _bruch(0)
    zu_sichern = max(_subtrahieren(verguetung, abzug), _bruch(0))
    wert = _multiplizieren(zu_sichern, _bruch(11, 10)) if anwendbar else None
    return _geld_ergebnis(wert, "BGB_BAU_SICHERUNG", eingaben, [
        {"operation": "Ausnahmen nach Bestellerart und Baubetreuer", "anwendbar": anwendbar},
        {"operation": "Berücksichtigungsfähige Gegenforderung abziehen",
         "abzug": _bruchteile(abzug), "zu_sichernde_verguetung": _bruchteile(zu_sichern)},
        {"operation": "Zehn Prozent Nebenforderungen hinzufügen"},
    ])


def verbraucherbau_herstellungssicherheit(
    urspruengliche_gesamtverguetung=None, zusaetzliche_verguetung=None,
    bereits_gestellte_sicherheit=None, verbraucherbauvertrag=None,
):
    """§ 650m Abs. 2: Grundsicherheit und schwellenabhängige Zusatzsicherheit."""
    eingaben = dict(urspruengliche_gesamtverguetung=urspruengliche_gesamtverguetung,
                    zusaetzliche_verguetung=zusaetzliche_verguetung,
                    bereits_gestellte_sicherheit=bereits_gestellte_sicherheit,
                    verbraucherbauvertrag=verbraucherbauvertrag)
    ursprung, zusatz = _geld(urspruengliche_gesamtverguetung), _geld(zusaetzliche_verguetung)
    gestellt = _geld(bereits_gestellte_sicherheit)
    if ursprung == 0:
        _fehler("urspruengliche_gesamtverguetung", "Positive ursprüngliche Vergütung erforderlich.")
    _wahrheitswert(verbraucherbauvertrag, "verbraucherbauvertrag")
    ergebnis = _geld_ergebnis(
        _bruch(0) if verbraucherbauvertrag else None,
        "BGB_VERBRAUCHERBAU_HERSTELLUNGSSICHERHEIT", eingaben,
        [{"operation": "Verbraucherbauvertrag", "anwendbar": verbraucherbauvertrag}])
    if verbraucherbauvertrag:
        grund = _multiplizieren(ursprung, _bruch(1, 20))
        schwelle_ueberschritten = zusatz > _multiplizieren(ursprung, _bruch(1, 10))
        zusaetzlich = _multiplizieren(zusatz, _bruch(1, 20)) if schwelle_ueberschritten else _bruch(0)
        gesamt = _addieren(grund, zusaetzlich)
        offen = max(_subtrahieren(gesamt, gestellt), _bruch(0))
        ergebnis["wert"] = dict(grundsicherheit=_bruchteile(grund),
                                zusaetzliche_sicherheit=_bruchteile(zusaetzlich),
                                gesamtsicherheit=_bruchteile(gesamt), noch_zu_stellen=_bruchteile(offen))
        ergebnis["rechenschritte"].append(dict(
            operation="Fünf Prozent Grundvergütung plus gegebenenfalls fünf Prozent gesamter Mehrvergütung",
            zehnprozent_schwelle_ueberschritten=schwelle_ueberschritten))
    return ergebnis
