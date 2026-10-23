"""Besondere Verjährungsnachläufe und einmalige Nachbesserungsverlängerung§475e."""
from .betraege import _wahrheitswert
from .kalender import _auswahl, _datum, _ergebnis, _frist, _text


def verbrauchsgueterkauf_verjaehrungsnachlauf(
    nachlaufgrund=None, anknuepfung_am=None, bisheriger_letzter_tag=None,
    tatbestand_erfuellt=None, einordnungsnachweis=None,
):
    """§475e Absätze1–4: sachgerechten Mindestnachlauf berechnen und späteres Ende wählen."""
    _auswahl(nachlaufgrund, "nachlaufgrund", ("ende_digitaler_bereitstellung", "ende_aktualisierungspflicht",
        "erstmaliges_zeigen_des_mangels", "rueckgabe_nach_nacherfuellung_garantie"))
    anknuepfung = _datum(anknuepfung_am, "anknuepfung_am")
    bisher = _datum(bisheriger_letzter_tag, "bisheriger_letzter_tag")
    _wahrheitswert(tatbestand_erfuellt, "tatbestand_erfuellt")
    _text(einordnungsnachweis, "einordnungsnachweis")
    eingaben = dict(nachlaufgrund=nachlaufgrund, anknuepfung_am=anknuepfung_am,
        bisheriger_letzter_tag=bisheriger_letzter_tag, tatbestand_erfuellt=tatbestand_erfuellt,
        einordnungsnachweis=einordnungsnachweis)
    gilt = tatbestand_erfuellt and (nachlaufgrund != "erstmaliges_zeigen_des_mangels" or anknuepfung <= bisher)
    wert = None
    if gilt:
        monate = {"ende_digitaler_bereitstellung": 12, "ende_aktualisierungspflicht": 12,
            "erstmaliges_zeigen_des_mangels": 4, "rueckgabe_nach_nacherfuellung_garantie": 2}[nachlaufgrund]
        mindest = _frist(anknuepfung_am, monate, "monate", "ereignis")
        wert = dict(nachlauf_monate=monate, mindestablauf=mindest.isoformat(),
            rechnerischer_letzter_tag=max(bisher, mindest).isoformat())
    ergebnis = _ergebnis(wert, "fristdaten", "BGB_VERBRAUCHSGUETERKAUF_VERJAEHRUNGSNACHLAUF", eingaben,
        [dict(operation="Gesetzlichen Nachlauf vom jeweiligen Anknüpfungsereignis berechnen und mit bisherigem letzten Tag maximieren")], eingaben.copy())
    ergebnis["status"] = "BERECHNET" if gilt else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = ["Konkreter Mangelanspruch und gesetzlicher Nachlauftatbestand rechtlich eingeordnet; feste lokale BGB-Fassung."]
    ergebnis["hinweise"] = ["Keine pauschale Addition zum bisherigen Fristende: Mindestnachlauf ab dem gesetzlich bezeichneten Ereignis. Beim erstmaligen Zeigen muss das Ereignis innerhalb der maßgeblichen bisherigen Frist liegen; spätere weitere Erscheinungen nicht als erneutes Erstzeigen einsetzen. Bei Rückgabe muss die vorausgehende Übergabe zur Nacherfüllung/Garantie an Unternehmer oder auf dessen Veranlassung an Dritten rechtlich qualifiziert sein; kein automatisches Wiederaufleben verjährter Ansprüche. Digitale Bereitstellung und Aktualisierungspflicht haben unterschiedliche rechtliche Endzeitpunkte. Weitere Hemmungen, Neubeginne, konkurrierende Nachläufe und erforderliche Kalenderkorrekturen gesondert prüfen."]
    return ergebnis


def verbrauchsgueterkauf_nachbesserungsverlaengerung(
    urspruenglicher_letzter_tag=None, nachbesserung_nach_439_geleistet=None,
    regel_475e_absatz_fuenf_anwendbar=None, einordnungsnachweis=None,
):
    """§475e Absatz5: ursprüngliche Frist einmalig um zwölf Monate verlängern."""
    ursprung = _datum(urspruenglicher_letzter_tag, "urspruenglicher_letzter_tag")
    _wahrheitswert(nachbesserung_nach_439_geleistet, "nachbesserung_nach_439_geleistet")
    _wahrheitswert(regel_475e_absatz_fuenf_anwendbar, "regel_475e_absatz_fuenf_anwendbar")
    _text(einordnungsnachweis, "einordnungsnachweis")
    eingaben = dict(urspruenglicher_letzter_tag=urspruenglicher_letzter_tag,
        nachbesserung_nach_439_geleistet=nachbesserung_nach_439_geleistet,
        regel_475e_absatz_fuenf_anwendbar=regel_475e_absatz_fuenf_anwendbar,
        einordnungsnachweis=einordnungsnachweis)
    wert = None
    if regel_475e_absatz_fuenf_anwendbar:
        ende = _frist(urspruenglicher_letzter_tag, 12, "monate", "ereignis") if nachbesserung_nach_439_geleistet else ursprung
        wert = dict(verlaengerung_monate=12 if nachbesserung_nach_439_geleistet else 0,
            rechnerischer_letzter_tag=ende.isoformat())
    ergebnis = _ergebnis(wert, "fristdaten", "BGB_VERBRAUCHSGUETERKAUF_NACHBESSERUNGSVERLAENGERUNG", eingaben,
        [dict(operation="Bei geleisteter Nachbesserung zwölf Monate genau einmal an die unveränderte ursprüngliche Frist anschließen")], eingaben.copy())
    ergebnis["status"] = "BERECHNET" if regel_475e_absatz_fuenf_anwendbar else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = ["Absatz5 aus der festen lokalen BGB-Fassung einschließlich zeitlichem Anwendungsbereich geprüft; unveränderte ursprüngliche Frist vorgegeben."]
    ergebnis["hinweise"] = ["Nur Nacherfüllung durch geleistete Nachbesserung gemäß§439; bloße Anforderung, Versuch ohne rechtlich geleistete Nachbesserung oder Ersatzlieferung nicht automatisch gleichsetzen. Immer dieselbe ursprüngliche Grundfrist eingeben, niemals das bereits verlängerte Ergebnis; weitere Nachbesserungen lösen keine zusätzlichen Zwölfmonatsverlängerungen aus. Keine zwölf Monate ab Reparaturdatum und kein neuer vollständiger Fristlauf. Andere Hemmungen, Neubeginne und Nachläufe rechtlich gesondert kombinieren; kein automatisches Wiederaufleben verjährter Ansprüche. Bei alten Fällen die zeitliche Geltung der lokal vorliegenden Absatz5-Fassung ausdrücklich prüfen."]
    return ergebnis
