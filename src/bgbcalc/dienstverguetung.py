"""Vergütungsanrechnung bei Dienstausfall und persönlicher Verhinderung."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _text
from .zahlen import _addieren, _bruch, _subtrahieren


def dienstverguetung_annahmeverzug(
    vereinbarte_verguetung=None, ersparte_aufwendungen=None, anderweitiger_erwerb=None,
    boeswillig_unterlassener_erwerb=None, annahmeverzug=None,
    arbeitgeber_traegt_arbeitsausfallrisiko=None, bewertungsnachweis=None,
):
    """§615: Vergütung abzüglich Ersparnis, anderweitigem und böswillig unterlassenem Erwerb."""
    verguetung = _geld(vereinbarte_verguetung)
    ersparnis = _geld(ersparte_aufwendungen)
    erwerb = _geld(anderweitiger_erwerb)
    unterlassen = _geld(boeswillig_unterlassener_erwerb)
    _wahrheitswert(annahmeverzug, "annahmeverzug")
    _wahrheitswert(arbeitgeber_traegt_arbeitsausfallrisiko, "arbeitgeber_traegt_arbeitsausfallrisiko")
    _text(bewertungsnachweis, "bewertungsnachweis")
    eingaben = dict(vereinbarte_verguetung=vereinbarte_verguetung, ersparte_aufwendungen=ersparte_aufwendungen,
        anderweitiger_erwerb=anderweitiger_erwerb, boeswillig_unterlassener_erwerb=boeswillig_unterlassener_erwerb,
        annahmeverzug=annahmeverzug, arbeitgeber_traegt_arbeitsausfallrisiko=arbeitgeber_traegt_arbeitsausfallrisiko,
        bewertungsnachweis=bewertungsnachweis)
    wert = None
    if annahmeverzug or arbeitgeber_traegt_arbeitsausfallrisiko:
        abzug = _addieren(_addieren(ersparnis, erwerb), unterlassen)
        wert = max(_subtrahieren(verguetung, abzug), _bruch(0))
    ergebnis = _geld_ergebnis(wert, "BGB_DIENSTVERGUETUNG_ANNAHMEVERZUG", eingaben,
        [dict(operation="Annahmeverzug oder Arbeitgeber-Arbeitsausfallrisiko; Vergütung um gesetzlich anrechenbare Ersparnis und Erwerbswerte vermindern, mindestens null")])
    ergebnis["hinweise"].append("Nur§615 im rechtlich einschlägigen Fall; keine automatische Annahmeverzugs-/Risikobewertung. Abzüge müssen infolge desselben Dienstausfalls und für denselben Vergütungszeitraum anrechenbar sein, keine Doppelzählung. Brutto-/Nettobezüge rechtlich konsistent bestimmen. Keine automatische Arbeitssuchpflicht oder Schätzung böswillig unterlassenen Erwerbs. Keine Nachleistungspflicht nach§615 Satz1; andere Anspruchsgrundlagen und Sondergesetze gesondert.")
    return ergebnis


def dienstverguetung_persoenliche_verhinderung(
    vereinbarte_verguetung=None, gesetzliche_kranken_unfallversicherungsleistung=None,
    grund_in_der_person=None, ohne_verschulden=None, zeit_verhaeltnismaessig_nicht_erheblich=None,
    regel_616_anwendbar=None, bewertungsnachweis=None,
):
    """§616: kurze unverschuldete persönliche Verhinderung und bestimmte Versicherungsanrechnung."""
    verguetung = _geld(vereinbarte_verguetung)
    versicherung = _geld(gesetzliche_kranken_unfallversicherungsleistung)
    eingaben = dict(vereinbarte_verguetung=vereinbarte_verguetung,
        gesetzliche_kranken_unfallversicherungsleistung=gesetzliche_kranken_unfallversicherungsleistung,
        grund_in_der_person=grund_in_der_person, ohne_verschulden=ohne_verschulden,
        zeit_verhaeltnismaessig_nicht_erheblich=zeit_verhaeltnismaessig_nicht_erheblich,
        regel_616_anwendbar=regel_616_anwendbar, bewertungsnachweis=bewertungsnachweis)
    for name in tuple(eingaben)[2:-1]:
        _wahrheitswert(eingaben[name], name)
    _text(bewertungsnachweis, "bewertungsnachweis")
    gilt = regel_616_anwendbar and grund_in_der_person and ohne_verschulden and zeit_verhaeltnismaessig_nicht_erheblich
    ergebnis = _geld_ergebnis(max(_subtrahieren(verguetung, versicherung), _bruch(0)) if gilt else None,
        "BGB_DIENSTVERGUETUNG_PERSOENLICHE_VERHINDERUNG", eingaben,
        [dict(operation="Persönlichen Grund, fehlendes Verschulden und rechtlich unerhebliche Dauer prüfen; qualifizierte Kranken-/Unfallversicherungsleistung abziehen")])
    ergebnis["hinweise"].append("Keine feste Tageszahl für verhältnismäßig nicht erhebliche Zeit erfunden; rechtliche Einordnung des gesamten Verhinderungsfalls erforderlich. Nicht einen unzulässig abgeschnittenen kurzen Teil einer insgesamt erheblichen Verhinderung einsetzen. Nur auf gesetzlicher Verpflichtung beruhende Kranken-/Unfallversicherung für dieselbe Verhinderungszeit anrechnen. Vertrags-/Tarifausschluss und Sondergesetze vorab prüfen. NICHT_ANWENDBAR schließt andere Vergütungsansprüche nicht aus.")
    return ergebnis
