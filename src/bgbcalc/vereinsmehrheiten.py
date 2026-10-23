"""Gesetzliche Standardmehrheiten mit ausdrücklich bestimmter Bezugsmenge."""
from .betraege import _wahrheitswert
from .kalender import _auswahl, _ergebnis, _ganzzahl, _text
from .zahlen import GRENZE


def _vereins_ergebnis(wert, regel_id, eingaben, operation, hinweis):
    ergebnis = _ergebnis(wert, "stimmen_und_wahrheitswerte", regel_id, eingaben,
        [dict(operation=operation)], eingaben.copy())
    ergebnis["status"] = "NICHT_ANWENDBAR" if wert is None else "BERECHNET"
    ergebnis["annahmen"] = ["Rechtlich maßgebliche Mitglieder-/Stimmenzahlen und Satzungslage ausdrücklich vorgegeben; feste lokale BGB-Fassung."]
    ergebnis["hinweise"] = [hinweis, "Rechnerische Mehrheit bestätigt nicht allein die Wirksamkeit eines Beschlusses oder einer Vertretung. Abweichende Satzung führt aus dem gesetzlichen Standardmodell heraus."]
    return ergebnis


def vorstand_vertretungsmehrheit(
    vorstandsmitglieder=None, mitwirkende_vorstandsmitglieder=None,
    rechtsform=None, abweichende_satzungsregel=None, bestandsnachweis=None,
):
    """§26 Absatz2 Satz1 bzw.§84 Absatz2 Satz2: Mehrheit des gesamten Vorstands."""
    anzahl = _ganzzahl(vorstandsmitglieder, "vorstandsmitglieder", 1, GRENZE)
    mitwirkend = _ganzzahl(mitwirkende_vorstandsmitglieder, "mitwirkende_vorstandsmitglieder", 0, anzahl)
    _auswahl(rechtsform, "rechtsform", ("verein", "stiftung"))
    _wahrheitswert(abweichende_satzungsregel, "abweichende_satzungsregel")
    _text(bestandsnachweis, "bestandsnachweis")
    eingaben = dict(vorstandsmitglieder=vorstandsmitglieder,
        mitwirkende_vorstandsmitglieder=mitwirkende_vorstandsmitglieder, rechtsform=rechtsform,
        abweichende_satzungsregel=abweichende_satzungsregel, bestandsnachweis=bestandsnachweis)
    wert = None
    if not abweichende_satzungsregel:
        minimum = anzahl // 2 + 1
        wert = dict(mindestens_mitwirkende=minimum, vertretungsmehrheit_erreicht=mitwirkend >= minimum)
    return _vereins_ergebnis(wert, "BGB_VORSTAND_VERTRETUNGSMEHRHEIT", eingaben,
        "Strikte Mehrheit aller rechtlich maßgeblichen Vorstandsmitglieder bestimmen",
        "Aktive Vertretung, keine Beschlussmehrheit und keine Regel für Zugang einer Erklärung gegenüber dem Vorstand. Satzungsabweichungen nach§40 bzw.§84 Absatz3 gesondert.")


def vereinsbeschluss_stimmenmehrheit(
    beschlussart=None, massgebliche_abgegebene_stimmen=None, ja_stimmen=None,
    abweichende_satzungsregel=None, stimmen_nachweis=None,
):
    """§§32/33/41: einfache oder Dreiviertelmehrheit gültiger maßgeblicher Stimmen."""
    _auswahl(beschlussart, "beschlussart", ("ordentlich", "satzungsaenderung", "aufloesung"))
    stimmen = _ganzzahl(massgebliche_abgegebene_stimmen, "massgebliche_abgegebene_stimmen", 0, GRENZE)
    ja = _ganzzahl(ja_stimmen, "ja_stimmen", 0, stimmen)
    _wahrheitswert(abweichende_satzungsregel, "abweichende_satzungsregel")
    _text(stimmen_nachweis, "stimmen_nachweis")
    eingaben = dict(beschlussart=beschlussart, massgebliche_abgegebene_stimmen=massgebliche_abgegebene_stimmen,
        ja_stimmen=ja_stimmen, abweichende_satzungsregel=abweichende_satzungsregel, stimmen_nachweis=stimmen_nachweis)
    wert = None
    if not abweichende_satzungsregel:
        # ceil(3*n/4)=n-floor(n/4), ohne unnötigen Überlauf bei 3*n.
        minimum = stimmen // 2 + 1 if beschlussart == "ordentlich" else max(1, stimmen - stimmen // 4)
        wert = dict(mindestens_ja_stimmen=minimum, stimmenmehrheit_erreicht=ja >= minimum)
    return _vereins_ergebnis(wert, "BGB_VEREINSBESCHLUSS_STIMMENMEHRHEIT", eingaben,
        "Einfache Mehrheit oder mindestens drei Viertel der maßgeblichen abgegebenen Stimmen berechnen",
        "Zweckänderung und Umlaufbeschluss erfordern gesonderte Zustimmungsprüfung. Bezugsmenge muss gültige Stimmen und zwingende Stimmrechtsausschlüsse§34 bereits korrekt berücksichtigen; kein Beschluss allein aus leerer Stimmenmenge.")


def vereinsbeschluss_zustimmung_aller(
    beschlussart=None, mitgliederzahl=None, zustimmende_mitglieder=None,
    erforderliche_textform_gewahrt=None, abweichende_satzungsregel=None,
    zustimmungsnachweis=None,
):
    """§32 Absatz3 bzw.§33 Absatz1 Satz2: alle Mitglieder und erforderliche Textform."""
    _auswahl(beschlussart, "beschlussart", ("ohne_versammlung", "zweckaenderung"))
    anzahl = _ganzzahl(mitgliederzahl, "mitgliederzahl", 1, GRENZE)
    zustimmungen = _ganzzahl(zustimmende_mitglieder, "zustimmende_mitglieder", 0, anzahl)
    _wahrheitswert(erforderliche_textform_gewahrt, "erforderliche_textform_gewahrt")
    _wahrheitswert(abweichende_satzungsregel, "abweichende_satzungsregel")
    _text(zustimmungsnachweis, "zustimmungsnachweis")
    eingaben = dict(beschlussart=beschlussart, mitgliederzahl=mitgliederzahl,
        zustimmende_mitglieder=zustimmende_mitglieder, erforderliche_textform_gewahrt=erforderliche_textform_gewahrt,
        abweichende_satzungsregel=abweichende_satzungsregel, zustimmungsnachweis=zustimmungsnachweis)
    wert = None
    if not abweichende_satzungsregel:
        alle = zustimmungen == anzahl
        wert = dict(zustimmung_aller_erreicht=alle,
            zustimmungs_und_textformvoraussetzungen_erfuellt=alle and erforderliche_textform_gewahrt)
    return _vereins_ergebnis(wert, "BGB_VEREINSBESCHLUSS_ZUSTIMMUNG_ALLER", eingaben,
        "Zustimmende Mitglieder mit vollständiger Bezugsmenge vergleichen und erforderliche Textform prüfen",
        "Ohne Versammlung Textform sämtlicher Zustimmungen; bei Zweckänderung Textform der nicht erschienenen Mitglieder. Keine bloße Einstimmigkeit nur der Anwesenden. Weitere Beschlussvoraussetzungen gesondert.")
