"""Eigentumsquoten bei Verbindung oder Vermischung beweglicher Sachen."""
from .betraege import _geld, _wahrheitswert
from .kalender import _auswahl, _ergebnis, _fehler, _text, _vorhanden
from .zahlen import _addieren, _bruch, _dividieren
from .zinsen import _bruchteile


def sachenverbindung_eigentumsquoten(
    eigentuemer_werte=None, entstehungsart=None, wesentliche_bestandteile=None,
    untrennbar_vermischt=None, trennungskosten_unverhaeltnismaessig=None,
    hauptsachen_eigentuemer=None, bewertungsnachweis=None,
):
    """§§947/948: Eigentumsanteile nach Wertverhältnis oder Alleineigentum der Hauptsache."""
    _vorhanden(eigentuemer_werte, "eigentuemer_werte")
    if not isinstance(eigentuemer_werte, list) or not 2 <= len(eigentuemer_werte) <= 1000:
        _fehler("eigentuemer_werte", "Liste mit 2 bis 1000 unterschiedlichen Eigentümern erforderlich.")
    _auswahl(entstehungsart, "entstehungsart", ("verbindung", "vermischung_vermengung"))
    for name, wert in (("wesentliche_bestandteile", wesentliche_bestandteile),
        ("untrennbar_vermischt", untrennbar_vermischt),
        ("trennungskosten_unverhaeltnismaessig", trennungskosten_unverhaeltnismaessig)):
        _wahrheitswert(wert, name)
    namen, werte = [], []
    summe = _bruch(0)
    for eintrag in eigentuemer_werte:
        if not isinstance(eintrag, dict) or set(eintrag) != {"eigentuemer_id", "sachenwert"}:
            _fehler("eigentuemer_werte", "Genau eigentuemer_id und sachenwert erforderlich.")
        name = _text(eintrag["eigentuemer_id"], "eigentuemer_id")
        if name in namen:
            _fehler("eigentuemer_id", "Eigentümer nicht doppelt aufführen; Werte zuvor zusammenfassen.")
        wert = _geld(eintrag["sachenwert"])
        namen.append(name)
        werte.append(wert)
        summe = _addieren(summe, wert)
    if hauptsachen_eigentuemer is not None:
        _text(hauptsachen_eigentuemer, "hauptsachen_eigentuemer")
        if hauptsachen_eigentuemer not in namen:
            _fehler("hauptsachen_eigentuemer", "Eigentümer der Hauptsache muss in der Liste enthalten sein.")
    elif summe == 0:
        _fehler("eigentuemer_werte", "Ohne Hauptsache ist ein positiver Gesamtwert für das Wertverhältnis erforderlich.")
    _text(bewertungsnachweis, "bewertungsnachweis")
    anwendbar = (wesentliche_bestandteile if entstehungsart == "verbindung" else
        untrennbar_vermischt or trennungskosten_unverhaeltnismaessig)
    quoten = None
    if anwendbar:
        quoten = [dict(eigentuemer_id=name, eigentumsquote=_bruchteile(
            _bruch(int(name == hauptsachen_eigentuemer)) if hauptsachen_eigentuemer is not None else _dividieren(wert, summe)))
            for name, wert in zip(namen, werte)]
    eingaben = dict(eigentuemer_werte=eigentuemer_werte, entstehungsart=entstehungsart,
        wesentliche_bestandteile=wesentliche_bestandteile, untrennbar_vermischt=untrennbar_vermischt,
        trennungskosten_unverhaeltnismaessig=trennungskosten_unverhaeltnismaessig,
        hauptsachen_eigentuemer=hauptsachen_eigentuemer, bewertungsnachweis=bewertungsnachweis)
    ergebnis = _ergebnis(quoten, "eigentumsquoten", "BGB_SACHENVERBINDUNG_EIGENTUMSQUOTEN", eingaben,
        [dict(operation="Verbindung/Vermischungstatbestand prüfen; Hauptsacheneigentümer erhält eins, sonst Werte im Entstehungszeitpunkt proportional verteilen")], eingaben.copy())
    ergebnis["status"] = "BERECHNET" if anwendbar else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = ["Bewegliche Sachen verschiedener Eigentümer, vergleichbare Werte im Zeitpunkt der Verbindung/Vermischung und Hauptsacheneigenschaft rechtlich bestimmt."]
    ergebnis["hinweise"] = ["Keine automatische Hauptsachenwahl allein nach höchstem Wert; Rechtsbegriff als ausdrückliche Eingabe. Vorbestehendes Miteigentum der Hauptsache nicht durch einen einzelnen Eigentümer ersetzen; solches Modell gesondert. Grundstücksverbindung§946, Verarbeitung§950 sowie Ausgleichsansprüche§951 separat. NICHT_ANWENDBAR enthält keine Entscheidung über fortbestehendes Eigentum."]
    return ergebnis
