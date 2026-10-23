"""Gesetzliche Ehegattenquote mit güterrechtlichen Zuschlägen und Ausschlüssen."""
from .betraege import _wahrheitswert
from .kalender import _auswahl, _ergebnis, _fehler, _ganzzahl
from .zahlen import GRENZE, _addieren, _bruch, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile


def ehegatten_erbquote(
    konstellation=None, gueterstand=None, anzahl_kinderstaemme=None,
    grosselternabkoemmlingsquote_zaehler=None, grosselternabkoemmlingsquote_nenner=None,
    ehe_beim_erbfall=None, scheidungsvoraussetzungen_erfuellt=None,
    erblasser_scheidung_beantragt_oder_zugestimmt=None,
    erblasser_aufhebungsberechtigt=None, erblasser_aufhebung_beantragt=None,
):
    """§§ 1931/1933/1371: Ehegatten- und verbleibende Verwandtenquote bestimmen."""
    eingaben = dict(
        konstellation=konstellation, gueterstand=gueterstand, anzahl_kinderstaemme=anzahl_kinderstaemme,
        grosselternabkoemmlingsquote_zaehler=grosselternabkoemmlingsquote_zaehler,
        grosselternabkoemmlingsquote_nenner=grosselternabkoemmlingsquote_nenner,
        ehe_beim_erbfall=ehe_beim_erbfall, scheidungsvoraussetzungen_erfuellt=scheidungsvoraussetzungen_erfuellt,
        erblasser_scheidung_beantragt_oder_zugestimmt=erblasser_scheidung_beantragt_oder_zugestimmt,
        erblasser_aufhebungsberechtigt=erblasser_aufhebungsberechtigt,
        erblasser_aufhebung_beantragt=erblasser_aufhebung_beantragt,
    )
    _auswahl(konstellation, "konstellation",
             ("erste_ordnung", "zweite_ordnung", "grosseltern", "keine_ersten_zweiten_und_keine_grosseltern"))
    _auswahl(gueterstand, "gueterstand", ("zugewinngemeinschaft", "guetertrennung", "ohne_erbquoten_sonderregel"))
    _ganzzahl(anzahl_kinderstaemme, "anzahl_kinderstaemme", 0, 10000)
    if (konstellation == "erste_ordnung") != (anzahl_kinderstaemme > 0):
        _fehler("anzahl_kinderstaemme", "Positive Stammzahl nur und stets bei erster Ordnung erforderlich.")
    _ganzzahl(grosselternabkoemmlingsquote_zaehler, "grosselternabkoemmlingsquote_zaehler", 0, GRENZE)
    _ganzzahl(grosselternabkoemmlingsquote_nenner, "grosselternabkoemmlingsquote_nenner", 1, GRENZE)
    abkoemmlingsquote = _bruch(grosselternabkoemmlingsquote_zaehler, grosselternabkoemmlingsquote_nenner)
    if abkoemmlingsquote >= 1 or (konstellation != "grosseltern" and abkoemmlingsquote != 0):
        _fehler("grosselternabkoemmlingsquote", "Nur im Großelternfall Quote unter 1, sonst Quote null.")
    for parameter in (
        "ehe_beim_erbfall", "scheidungsvoraussetzungen_erfuellt",
        "erblasser_scheidung_beantragt_oder_zugestimmt",
        "erblasser_aufhebungsberechtigt", "erblasser_aufhebung_beantragt",
    ):
        _wahrheitswert(eingaben[parameter], parameter)
    ausgeschlossen = (scheidungsvoraussetzungen_erfuellt and erblasser_scheidung_beantragt_oder_zugestimmt) or (
        erblasser_aufhebungsberechtigt and erblasser_aufhebung_beantragt)
    anwendbar = ehe_beim_erbfall and not ausgeschlossen
    schritte = [{"operation": "Ehe und Ausschluss nach § 1933", "anwendbar": anwendbar}]
    wert = None
    if anwendbar:
        zug, zusatz = _bruch(0), _bruch(0)
        if konstellation == "keine_ersten_zweiten_und_keine_grosseltern":
            grund = _bruch(1)
        else:
            grund = _bruch(1, 4 if konstellation == "erste_ordnung" else 2)
            if gueterstand == "guetertrennung" and konstellation == "erste_ordnung" and anzahl_kinderstaemme <= 2:
                grund = _bruch(1, anzahl_kinderstaemme + 1)
            if gueterstand == "zugewinngemeinschaft":
                zug = _bruch(1, 4)
            verbleibend = _subtrahieren(_bruch(1), _addieren(grund, zug))
            if konstellation == "grosseltern":
                zusatz = _multiplizieren(verbleibend, abkoemmlingsquote)
        gesamt = _addieren(_addieren(grund, zug), zusatz)
        wert = dict(grundquote=_bruchteile(grund), zugewinnzuschlag=_bruchteile(zug),
                    grosselternabkoemmlingszuschlag=_bruchteile(zusatz),
                    ehegattenquote=_bruchteile(gesamt),
                    verwandtenquote=_bruchteile(_subtrahieren(_bruch(1), gesamt)))
        schritte.extend([
            {"operation": "Grundquote einschließlich Gütertrennung bestimmen"},
            {"operation": "Zugewinnviertel vor Großelternabkömmlingszuschlag berücksichtigen"},
            {"operation": "Zusatz aus verbleibendem Verwandtenanteil; Gesamtquote und Restquote bilden"},
        ])
    ergebnis = _ergebnis(wert, "erbquote", "BGB_EHEGATTEN_ERBQUOTE", eingaben, schritte, eingaben.copy())
    ergebnis["status"] = "BERECHNET" if anwendbar else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = ["Gesetzliche erbrechtliche Lösung; deutsches Erb- und Güterrecht und Fallzuordnung vorgegeben."]
    ergebnis["hinweise"] = [
        "Keine Pflichtteilsberechnung oder güterrechtliche Lösung nach § 1371 Abs. 2/3.",
        "§ 1934-Verwandtenerbteil und Voraus nach § 1932 gesondert; keine Rundung.",
        "Großelternabkömmlingszuschlag aus dem nach Zugewinnviertel verbleibenden Anteil.",
    ]
    return ergebnis
