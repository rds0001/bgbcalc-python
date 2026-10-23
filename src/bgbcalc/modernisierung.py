"""Monatliche Restgrenzen für rechtlich eingeordnete Modernisierungserhöhungen."""

from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _auswahl, _fehler
from .zahlen import _bruch, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile


def modernisierung_kappungsgrenze(
    wohnflaeche=None, monatliche_miete_je_quadratmeter=None,
    bisherige_monatliche_erhoehung_gesamt=None, bisherige_monatliche_heizungserhoehung=None,
    erhoehungsart=None, kappungsregel_anwendbar=None,
):
    """§§ 559 Abs. 3a/559e Abs. 3: allgemeine und zusätzliche Heizungsgrenze."""
    flaeche, qm_miete = _geld(wohnflaeche), _geld(monatliche_miete_je_quadratmeter)
    bisher = _geld(bisherige_monatliche_erhoehung_gesamt)
    heizung_bisher = _geld(bisherige_monatliche_heizungserhoehung)
    if flaeche == 0:
        _fehler("wohnflaeche", "Positive Wohnfläche erforderlich.")
    if heizung_bisher > bisher:
        _fehler("bisherige_monatliche_heizungserhoehung", "Heizungsanteil darf die gesamte berücksichtigte Erhöhung nicht übersteigen.")
    _auswahl(erhoehungsart, "erhoehungsart", ("allgemein", "heizung_559", "heizung_559e"))
    _wahrheitswert(kappungsregel_anwendbar, "kappungsregel_anwendbar")
    ergebnis = _geld_ergebnis(
        _bruch(0) if kappungsregel_anwendbar else None, "BGB_MODERNISIERUNG_KAPPUNGSGRENZE",
        dict(wohnflaeche=wohnflaeche, monatliche_miete_je_quadratmeter=monatliche_miete_je_quadratmeter,
             bisherige_monatliche_erhoehung_gesamt=bisherige_monatliche_erhoehung_gesamt,
             bisherige_monatliche_heizungserhoehung=bisherige_monatliche_heizungserhoehung,
             erhoehungsart=erhoehungsart, kappungsregel_anwendbar=kappungsregel_anwendbar),
        [{"operation": "Kappungsregel im ausgewählten Fall", "anwendbar": kappungsregel_anwendbar}],
    )
    if kappungsregel_anwendbar:
        grenze_je_qm = _bruch(2 if qm_miete < 7 else 3)
        allgemein = max(_subtrahieren(_multiplizieren(flaeche, grenze_je_qm), bisher), _bruch(0))
        heizung = None
        massgeblich = allgemein
        if erhoehungsart != "allgemein":
            heizung = max(_subtrahieren(_multiplizieren(flaeche, _bruch(1, 2)), heizung_bisher), _bruch(0))
            massgeblich = min(allgemein, heizung)
        ergebnis["wert"] = dict(
            allgemeine_restgrenze=_bruchteile(allgemein),
            heizungs_restgrenze=None if heizung is None else _bruchteile(heizung),
            massgebliche_restgrenze=_bruchteile(massgeblich),
        )
        ergebnis["rechenschritte"].append(dict(
            operation="Zwei oder drei Euro je Quadratmeter, bei Heizungsfall zusätzlich fünfzig Cent; bisherige Erhöhungen abziehen",
            allgemeine_grenze_je_quadratmeter=_bruchteile(grenze_je_qm),
        ))
    return ergebnis
