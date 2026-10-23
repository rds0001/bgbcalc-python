"""Begrenzter Vertrauensschaden nach §§122 und179 Absatz2."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _text
from .zahlen import _bruch


def vertrauensschaden_nichtigkeit_anfechtung(
    vertrauensschaden=None, gueltigkeitsinteresse=None, nichtigkeit_nach_118=None,
    anfechtung_nach_119_120=None, grund_bekannt_oder_kennen_muessen=None, bewertungsnachweis=None,
):
    """§122: negatives Interesse, begrenzt durch Gültigkeitsinteresse, mit Kenntnisausschluss."""
    schaden, interesse = _geld(vertrauensschaden), _geld(gueltigkeitsinteresse)
    eingaben = dict(vertrauensschaden=vertrauensschaden, gueltigkeitsinteresse=gueltigkeitsinteresse,
        nichtigkeit_nach_118=nichtigkeit_nach_118, anfechtung_nach_119_120=anfechtung_nach_119_120,
        grund_bekannt_oder_kennen_muessen=grund_bekannt_oder_kennen_muessen, bewertungsnachweis=bewertungsnachweis)
    for name in tuple(eingaben)[2:-1]:
        _wahrheitswert(eingaben[name], name)
    _text(bewertungsnachweis, "bewertungsnachweis")
    wert = None
    if nichtigkeit_nach_118 or anfechtung_nach_119_120:
        wert = _bruch(0) if grund_bekannt_oder_kennen_muessen else min(schaden, interesse)
    ergebnis = _geld_ergebnis(wert, "BGB_VERTRAUENSSCHADEN_NICHTIGKEIT_ANFECHTUNG", eingaben,
        [dict(operation="Anwendungsfall§122 prüfen; bei Kenntnis/Kennenmüssen kein Ersatz, sonst Vertrauensschaden auf Gültigkeitsinteresse begrenzen")])
    ergebnis["hinweise"].append("Nur§122, keine Übertragung auf beliebige Nichtigkeit oder Anfechtung nach§123. Geschützter Empfänger/Dritter, Kausalität und Schadenhöhe extern bestimmt; andere Ansprüche gesondert.")
    return ergebnis


def vertrauensschaden_vertretungsmangel(
    vertrauensschaden=None, wirksamkeitsinteresse=None, vertretungsmangel_unbekannt=None,
    vertretungsmacht_nachgewiesen=None, genehmigung_verweigert=None,
    gegner_kennt_oder_kennen_muss=None, vertreter_beschraenkt_geschaeftsfaehig=None,
    mit_zustimmung_des_gesetzlichen_vertreters=None, bewertungsnachweis=None,
):
    """§179 Absatz2/3: unbekannter Vertretungsmangel, Höchstbetrag und Ausschlüsse."""
    schaden, interesse = _geld(vertrauensschaden), _geld(wirksamkeitsinteresse)
    eingaben = dict(vertrauensschaden=vertrauensschaden, wirksamkeitsinteresse=wirksamkeitsinteresse,
        vertretungsmangel_unbekannt=vertretungsmangel_unbekannt, vertretungsmacht_nachgewiesen=vertretungsmacht_nachgewiesen,
        genehmigung_verweigert=genehmigung_verweigert, gegner_kennt_oder_kennen_muss=gegner_kennt_oder_kennen_muss,
        vertreter_beschraenkt_geschaeftsfaehig=vertreter_beschraenkt_geschaeftsfaehig,
        mit_zustimmung_des_gesetzlichen_vertreters=mit_zustimmung_des_gesetzlichen_vertreters,
        bewertungsnachweis=bewertungsnachweis)
    for name in tuple(eingaben)[2:-1]:
        _wahrheitswert(eingaben[name], name)
    _text(bewertungsnachweis, "bewertungsnachweis")
    wert = None
    if vertretungsmangel_unbekannt and not vertretungsmacht_nachgewiesen and genehmigung_verweigert:
        ausgeschlossen = (gegner_kennt_oder_kennen_muss or
            (vertreter_beschraenkt_geschaeftsfaehig and not mit_zustimmung_des_gesetzlichen_vertreters))
        wert = _bruch(0) if ausgeschlossen else min(schaden, interesse)
    ergebnis = _geld_ergebnis(wert, "BGB_VERTRAUENSSCHADEN_VERTRETUNGSMANGEL", eingaben,
        [dict(operation="Unbekannten Vertretungsmangel und verweigerte Genehmigung prüfen; Ausschlüsse anwenden und Vertrauensschaden auf Wirksamkeitsinteresse begrenzen")])
    ergebnis["hinweise"].append("Nur begrenzter Vertrauensschaden§179 Absatz2. Bei bekanntem Vertretungsmangel NICHT_ANWENDBAR, nicht Haftungsfreiheit; Erfüllung/Schadenersatzwahl nach Absatz1 gesondert. Vertragsschluss als Vertreter und weitere Voraussetzungen vorab bestimmen.")
    return ergebnis
