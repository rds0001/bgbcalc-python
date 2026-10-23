"""Bewertungswahl und Mehrhinterlassungsanrechnung bei Pflichtteilsergänzung."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _text
from .zahlen import _bruch, _subtrahieren
from .zinsen import _bruchteile


def pflichtteil_schenkungswert(
    vergleichbarer_schenkungswert=None, wert_beim_erbfall=None,
    verbrauchbare_sache=None, pflicht_oder_anstandsschenkung=None, bewertungsnachweis=None,
):
    """§2325 Absatz2: Schenkungswert bei verbrauchbaren Sachen, sonst Niederstwertprinzip."""
    schenkung = _geld(vergleichbarer_schenkungswert)
    erbfall = _geld(wert_beim_erbfall)
    _wahrheitswert(verbrauchbare_sache, "verbrauchbare_sache")
    _wahrheitswert(pflicht_oder_anstandsschenkung, "pflicht_oder_anstandsschenkung")
    _text(bewertungsnachweis, "bewertungsnachweis")
    eingaben = dict(vergleichbarer_schenkungswert=vergleichbarer_schenkungswert,
        wert_beim_erbfall=wert_beim_erbfall, verbrauchbare_sache=verbrauchbare_sache,
        pflicht_oder_anstandsschenkung=pflicht_oder_anstandsschenkung, bewertungsnachweis=bewertungsnachweis)
    wert = None if pflicht_oder_anstandsschenkung else (schenkung if verbrauchbare_sache else min(schenkung, erbfall))
    ergebnis = _geld_ergebnis(wert, "BGB_PFLICHTTEIL_SCHENKUNGSWERT", eingaben,
        [dict(operation="Pflicht-/Anstandsschenkung ausnehmen; bei verbrauchbarer Sache Schenkungswert, sonst geringeren Vergleichswert wählen")])
    ergebnis["hinweise"].append("Bewertungsstichtage, erforderliche Kaufkraft-/Wertbereinigung und Belastungen vorab rechtlich bestimmen; ungeprüfte Nominalwerte sind nicht automatisch vergleichbar. Nur Bewertungswahl vor zeitlicher Abschmelzung§2325 Absatz3, Pflichtteilsquote und weiteren Anrechnungen; kein fertiger Ergänzungsanspruch. Verbrauchbarkeit rechtlich nach§92 bestimmen.")
    return ergebnis


def pflichtteilsergaenzung_mehrhinterlassung(
    ergaenzungsbetrag_vor_mehrhinterlassung=None, hinterlassener_wert=None,
    ordentlicher_pflichtteilswert=None, bewertungsnachweis=None,
):
    """§2326: Nur den über den ordentlichen Pflichtteil hinaus hinterlassenen Wert abziehen."""
    ergaenzung = _geld(ergaenzungsbetrag_vor_mehrhinterlassung)
    hinterlassen = _geld(hinterlassener_wert)
    pflichtteil = _geld(ordentlicher_pflichtteilswert)
    _text(bewertungsnachweis, "bewertungsnachweis")
    mehr = max(_subtrahieren(hinterlassen, pflichtteil), _bruch(0))
    verbleibt = max(_subtrahieren(ergaenzung, mehr), _bruch(0))
    eingaben = dict(ergaenzungsbetrag_vor_mehrhinterlassung=ergaenzungsbetrag_vor_mehrhinterlassung,
        hinterlassener_wert=hinterlassener_wert, ordentlicher_pflichtteilswert=ordentlicher_pflichtteilswert,
        bewertungsnachweis=bewertungsnachweis)
    ergebnis = _geld_ergebnis(verbleibt, "BGB_PFLICHTTEILSERGAENZUNG_MEHRHINTERLASSUNG", eingaben,
        [dict(operation="Mehrhinterlassung über ordentlichen Pflichtteil ermitteln und Ergänzungsbetrag höchstens bis null vermindern")])
    ergebnis["wert"] = dict(mehrhinterlassung=_bruchteile(mehr),
        angerechneter_betrag=_bruchteile(min(ergaenzung, mehr)), verbleibende_ergaenzung=_bruchteile(verbleibt))
    ergebnis["hinweise"].append("Hinterlassener Wert und ordentlicher Pflichtteilswert rechtlich vergleichbar bewerten. Hälfte des gesetzlichen Erbteils als ordentlicher Pflichtteil; nicht Hälfte einer beliebig gewählten Erbquote. Nur§2326, keine zusätzliche Anrechnung bereits abgezogener Beträge. Eigengeschenke§2327, Erbenschutz§2328 und Beschenktenhaftung§2329 gesondert.")
    return ergebnis
