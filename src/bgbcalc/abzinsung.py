"""Vorzeitige Befriedigung nach §§ 1133 und 1217 BGB."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _auswahl
from .zahlen import _addieren, _bruch, _dividieren, _multiplizieren
from .zinsen import _bruchteile, _zeitanteil


def vorzeitiger_befriedigungsbetrag(
    forderungsbetrag=None, zeitanteil_zaehler=None, zeitanteil_nenner=None,
    zeitanteil_nachweis=None, unverzinslich=None, noch_nicht_faellig=None,
    befriedigungsgrund=None, voraussetzungen_erfuellt=None,
):
    """Unverzinsliche Forderung um den gesetzlichen Zwischenzins abzinsen."""
    eingaben = dict(
        forderungsbetrag=forderungsbetrag, zeitanteil_zaehler=zeitanteil_zaehler,
        zeitanteil_nenner=zeitanteil_nenner, zeitanteil_nachweis=zeitanteil_nachweis,
        unverzinslich=unverzinslich, noch_nicht_faellig=noch_nicht_faellig,
        befriedigungsgrund=befriedigungsgrund, voraussetzungen_erfuellt=voraussetzungen_erfuellt,
    )
    forderung = _geld(forderungsbetrag)
    anteil = _zeitanteil(zeitanteil_zaehler, zeitanteil_nenner, zeitanteil_nachweis)
    for parameter in ("unverzinslich", "noch_nicht_faellig", "voraussetzungen_erfuellt"):
        _wahrheitswert(eingaben[parameter], parameter)
    _auswahl(befriedigungsgrund, "befriedigungsgrund", ("hypothek_gefaehrdung", "pfand_rueckgabe"))
    anwendbar = unverzinslich and noch_nicht_faellig and voraussetzungen_erfuellt
    schritte = [{"operation": "Voraussetzungen der vorzeitigen Befriedigung", "anwendbar": anwendbar}]
    wert = None
    if anwendbar:
        faktor = _addieren(_bruch(1), _multiplizieren(_bruch(1, 25), anteil))
        wert = _dividieren(forderung, faktor)
        schritte.append({"operation": "Forderungsbetrag durch einfachen Aufzinsungsfaktor teilen",
                         "aufzinsungsfaktor": _bruchteile(faktor)})
    return _geld_ergebnis(wert, "BGB_VORZEITIGE_BEFRIEDIGUNG", eingaben, schritte,
                          {"zeitanteil_nachweis": zeitanteil_nachweis,
                           "voraussetzungen_erfuellt": voraussetzungen_erfuellt})
