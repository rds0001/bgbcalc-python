"""Zehnjahresfrist und Kenntnisausschluss beweglicher Ersitzung (§937)."""

from .betraege import _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler, _frist, _text


def ersitzung_bewegliche_sache(
    eigenbesitzbeginn_am=None,
    qualifiziertes_fristende=None,
    prueftag=None,
    kenntnis_fremdeigentum_am=None,
    guter_glaube_bei_eigenbesitzbeginn=None,
    bewegliche_sache=None,
    besitzverlauf_qualifiziert=None,
    sonstige_erwerbsvoraussetzungen_erfuellt=None,
    einordnungsnachweis=None,
):
    """Grundende plus qualifizierte Fristkorrekturen; kein automatisches Besitzverlaufsmodell."""
    beginn = _datum(eigenbesitzbeginn_am, "eigenbesitzbeginn_am")
    ende = _datum(qualifiziertes_fristende, "qualifiziertes_fristende")
    tag = _datum(prueftag, "prueftag")
    grundende = _frist(eigenbesitzbeginn_am, 10, "jahre", "ereignis")
    if ende < grundende:
        _fehler(
            "qualifiziertes_fristende",
            "Qualifiziertes Ende darf die Zehnjahresgrundfrist nicht unterschreiten; Anrechnung fremder Besitzzeiten ist außerhalb dieses Modells.",
        )
    if tag < beginn:
        _fehler("prueftag", "Prüftag darf nicht vor Eigenbesitzbeginn liegen.")
    kenntnis = None
    if kenntnis_fremdeigentum_am is not None:
        kenntnis = _datum(kenntnis_fremdeigentum_am, "kenntnis_fremdeigentum_am")
        if kenntnis < beginn or kenntnis > tag:
            _fehler(
                "kenntnis_fremdeigentum_am",
                "Spätere Kenntnis muss zwischen Eigenbesitzbeginn und Prüftag liegen; Kenntnis bei Beginn über guten Glauben qualifizieren.",
            )
    eingaben = dict(
        eigenbesitzbeginn_am=eigenbesitzbeginn_am,
        qualifiziertes_fristende=qualifiziertes_fristende,
        prueftag=prueftag,
        kenntnis_fremdeigentum_am=kenntnis_fremdeigentum_am,
        guter_glaube_bei_eigenbesitzbeginn=guter_glaube_bei_eigenbesitzbeginn,
        bewegliche_sache=bewegliche_sache,
        besitzverlauf_qualifiziert=besitzverlauf_qualifiziert,
        sonstige_erwerbsvoraussetzungen_erfuellt=sonstige_erwerbsvoraussetzungen_erfuellt,
        einordnungsnachweis=einordnungsnachweis,
    )
    for name in [
        "guter_glaube_bei_eigenbesitzbeginn",
        "bewegliche_sache",
        "besitzverlauf_qualifiziert",
        "sonstige_erwerbsvoraussetzungen_erfuellt",
    ]:
        _wahrheitswert(eingaben[name], name)
    _text(einordnungsnachweis, "einordnungsnachweis")
    ausschluss = not guter_glaube_bei_eigenbesitzbeginn or (
        kenntnis is not None and kenntnis <= ende
    )
    abgelaufen = tag >= ende
    wert = None
    if bewegliche_sache and besitzverlauf_qualifiziert:
        wert = dict(
            zehnjahresgrundfristende=grundende.isoformat(),
            ersitzungsfristende=ende.isoformat(),
            frist_am_prueftag_vollendet=abgelaufen,
            ausschluss_nach_937_absatz_2=ausschluss,
            eigentum_durch_ersitzung_erworben=abgelaufen
            and not ausschluss
            and sonstige_erwerbsvoraussetzungen_erfuellt,
        )
    ergebnis = _ergebnis(
        wert,
        "daten_und_wahrheitswerte",
        "BGB_ERSITZUNG_BEWEGLICHE_SACHE",
        eingaben,
        [
            dict(
                operation="Zehn Jahre ab qualifiziertem Eigenbesitzbeginn; qualifiziertes Ende und Prüftag vergleichen; fehlender Anfangsglaube oder Kenntnis bis Ende schließen Erwerb aus"
            )
        ],
        eingaben.copy(),
    )
    ergebnis["status"] = (
        "BERECHNET"
        if bewegliche_sache and besitzverlauf_qualifiziert
        else "NICHT_ANWENDBAR"
    )
    ergebnis["annahmen"] = [
        "Prüfung zum Ende des Prüftags; Eigenbesitzbeginn als Ereignis. Rechtlich anrechenbarer Besitzverlauf und korrigiertes Ende sind belegt, ohne Anrechnung fremder Besitzzeiten."
    ]
    ergebnis["hinweise"] = [
        "Grundfrist zehn Jahre nach§937, nicht selbst berechnete Hemmung/Unterbrechung. §§939–942 einschließlich relativer Hemmung und Rückerlangung nach§940 Absatz2 sind vorzuprüfen; physisch lückenloser Besitz wird nicht pauschal gefordert. Nach wirksamer Unterbrechung nur zutreffenden Neubeginn verwenden. Anrechnung von Rechtsvorgänger-/Erbschaftsbesitzerzeiten§§943/944 außerhalb dieses Modells. Qualifiziertes Ende einschließlich einschlägiger Hemmung/Ablaufhemmung belegen; keine automatische Wochenendverschiebung. Besitzverlauf bis zum früheren von Prüftag und qualifiziertem Ende rechtlich qualifizieren. Kenntnis NULL bedeutet bis Prüftag nicht eingetreten, nicht unbekannt. Kenntnis am Endtag zählt vor Vollendung am Tagesende; danach erstmals erlangte Kenntnis nimmt bereits vollendeten Erwerb nicht zurück. Bei fehlenden sonstigen Voraussetzungen entsteht auch ohne Kenntnisausschluss kein Erwerb. Keine Aussage über spätere Eigentumsübertragungen oder Erlöschen von Drittrechten nach§945; gutgläubiger Erwerb nach§§932ff. ist eigenständig."
    ]
    return ergebnis
