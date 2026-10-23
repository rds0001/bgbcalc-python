"""Haftungsprivileg und Befreiung von Dritthaftung nach §§31a/31b."""
from .betraege import _geld, _wahrheitswert
from .kalender import _auswahl, _ergebnis, _text


def vereins_haftungsprivileg(
    personenrolle=None, jaehrliche_verguetung=None, gesetzlicher_taetigkeitsbezug=None,
    vorsatz=None, grobe_fahrlaessigkeit=None, drittersatzpflicht_besteht=None,
    satzungsabweichung_mitgliederhaftung=None, bewertungsnachweis=None,
):
    """3300-Euro-Grenze und Verschuldens-/Aufgabenbedingungen, keine Schadenshöhe."""
    _auswahl(personenrolle, "personenrolle", ("organmitglied", "besonderer_vertreter", "vereinsmitglied"))
    verguetung = _geld(jaehrliche_verguetung)
    eingaben = dict(personenrolle=personenrolle, jaehrliche_verguetung=jaehrliche_verguetung,
        gesetzlicher_taetigkeitsbezug=gesetzlicher_taetigkeitsbezug, vorsatz=vorsatz,
        grobe_fahrlaessigkeit=grobe_fahrlaessigkeit, drittersatzpflicht_besteht=drittersatzpflicht_besteht,
        satzungsabweichung_mitgliederhaftung=satzungsabweichung_mitgliederhaftung,
        bewertungsnachweis=bewertungsnachweis)
    for name in tuple(eingaben)[2:-1]:
        _wahrheitswert(eingaben[name], name)
    _text(bewertungsnachweis, "bewertungsnachweis")
    grenze = verguetung <= 3300
    beguenstigt = grenze and gesetzlicher_taetigkeitsbezug
    ausschluss = beguenstigt and not vorsatz and not grobe_fahrlaessigkeit
    wert = dict(verguetungsgrenze_eingehalten=grenze,
        haftungsausschluss_gegenueber_verein_nach_31a_31b=ausschluss,
        haftungsausschluss_gegenueber_mitgliedern_nach_31a=(ausschluss and personenrolle != "vereinsmitglied"
            and not satzungsabweichung_mitgliederhaftung),
        befreiung_von_drittersatzpflicht_nach_31a_31b=ausschluss and drittersatzpflicht_besteht)
    ergebnis = _ergebnis(wert, "wahrheitswerte", "BGB_VEREINS_HAFTUNGSPRIVILEG", eingaben,
        [dict(operation="Jahresvergütung bis3300Euro, gesetzliche Aufgabe, Verschuldensgrad und gegebenenfalls Drittersatzpflicht verknüpfen")], eingaben.copy())
    ergebnis["annahmen"] = ["Rolle, relevante Jahresvergütung, konkreter Aufgabenbezug und Verschulden rechtlich bestimmt; Drittersatzpflicht ist eigenständig festgestellt."]
    ergebnis["hinweise"] = ["Nur benannte gesetzliche Privilegien. FALSE begründet nicht automatisch Haftung; TRUE bei Befreiung beseitigt nicht die vorgegebene Haftung gegenüber dem Dritten.",
        "§31b erfasst keine allgemeine Haftungsfreistellung gegenüber anderen Vereinsmitgliedern. Satzungsabweichung von§31a Absatz1 Satz2 führt insoweit aus diesem Standardprivileg; andere vertragliche Ansprüche getrennt.",
        "Keine automatische Vergütungsjahresabgrenzung oder Beweiswürdigung. Beweislastregeln§31a Absatz1 Satz3 und§31b Absatz1 Satz2 gesondert."]
    return ergebnis
