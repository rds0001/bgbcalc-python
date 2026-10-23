"""Kauf- und werkvertragliche Mängelgrundfristen einschließlich Arglistvorrang."""
from .betraege import _wahrheitswert
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _text


def maengel_verjaehrungsgrundfrist(
    regelbereich=None, fristgruppe=None, fristbeginnereignis_am=None,
    arglistig_verschwiegen=None, regelmaessiger_weg_letzter_tag=None,
    abweichende_sonderregel=None, einordnungsnachweis=None,
):
    """§§438/634a: 30/5/2Jahre oder regelmäßiger Weg, bei arglistigem Bauwerksmangel Mindestfrist."""
    _auswahl(regelbereich, "regelbereich", ("kauf", "werk"))
    _auswahl(fristgruppe, "fristgruppe", ("dingliches_drittrecht", "bauwerk", "sonstige_sache", "sonstiges_werk"))
    if (regelbereich == "kauf" and fristgruppe == "sonstiges_werk") or (regelbereich == "werk" and fristgruppe == "dingliches_drittrecht"):
        _fehler("fristgruppe", "Fristgruppe passt nicht zum gewählten Regelbereich.")
    _wahrheitswert(arglistig_verschwiegen, "arglistig_verschwiegen")
    _wahrheitswert(abweichende_sonderregel, "abweichende_sonderregel")
    _text(einordnungsnachweis, "einordnungsnachweis")
    regelmaessig = fristgruppe == "sonstiges_werk" or (arglistig_verschwiegen and fristgruppe != "dingliches_drittrecht")
    beginn = None
    if fristbeginnereignis_am is not None or not regelmaessig or fristgruppe == "bauwerk":
        beginn = _datum(fristbeginnereignis_am, "fristbeginnereignis_am")
    regelende = None
    if regelmaessiger_weg_letzter_tag is not None or regelmaessig:
        regelende = _datum(regelmaessiger_weg_letzter_tag, "regelmaessiger_weg_letzter_tag")
    eingaben = dict(regelbereich=regelbereich, fristgruppe=fristgruppe,
        fristbeginnereignis_am=fristbeginnereignis_am, arglistig_verschwiegen=arglistig_verschwiegen,
        regelmaessiger_weg_letzter_tag=regelmaessiger_weg_letzter_tag,
        abweichende_sonderregel=abweichende_sonderregel, einordnungsnachweis=einordnungsnachweis)
    wert = None
    if not abweichende_sonderregel:
        if regelmaessig:
            ende = regelende
            weg = "regelmaessige_verjaehrung"
            if fristgruppe == "bauwerk":
                ende = max(ende, _frist(beginn.isoformat(), 5, "jahre", "ereignis"))
                weg = "regelmaessige_verjaehrung_mindestens_fuenf_jahre"
        else:
            jahre = {"dingliches_drittrecht": 30, "bauwerk": 5, "sonstige_sache": 2}[fristgruppe]
            ende = _frist(beginn.isoformat(), jahre, "jahre", "ereignis")
            weg = {30: "dreissig_jahre", 5: "fuenf_jahre", 2: "zwei_jahre"}[jahre]
        wert = dict(verjaehrungsweg=weg, rechnerischer_letzter_tag=ende.isoformat())
    ergebnis = _ergebnis(wert, "fristdaten", "BGB_MAENGEL_VERJAEHRUNGSGRUNDFRIST", eingaben,
        [dict(operation="Gesetzlichen Mängelverjährungsweg wählen; Arglist verdrängt Zweijahresweg, Bauwerksweg bleibt Mindestfrist und dinglicher Dreißigjahresweg bleibt unberührt")], eingaben.copy())
    ergebnis["status"] = "BERECHNET" if wert is not None else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = ["Konkreter Anspruch nach§437 Nummer1/3 oder§634 Nummer1/2/4, Fristgruppe und gesetzliches Beginnereignis rechtlich eingeordnet; feste lokale BGB-Fassung."]
    ergebnis["hinweise"] = ["Kauf: Grundstücksübergabe, sonst Ablieferung; Werk: Abnahme für Zwei-/Fünfjahresweg. Regelmäßigen Weg einschließlich zutreffender Entstehung/Kenntnis und einschlägiger Höchstgrenzen vorab gesondert bestimmen. Grundfristen ohne Hemmung, Ablaufhemmung, Neubeginn oder abschließende Kalenderkorrektur vergleichen; solche Veränderungen danach in rechtlich zutreffender Reihenfolge prüfen. Arglist lässt Dreißigjahresweg§438 Absatz1 Nummer1 unberührt. Keine automatische Verjährung des Rücktritts oder der Minderung: hierfür§218 undAbsätze4/5 beachten. Verbrauchsgüter-, Digital-, Vertrags- und sonstige Sonderregeln separat, insbesondere§475e."]
    return ergebnis
