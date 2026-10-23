"""Langzeitkündigung des Dienstverpflichteten nach§624."""
from .betraege import _wahrheitswert
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _tage_addieren, _text


def dienst_langzeitkuendigungsrahmen(
    dienstbeginn_am=None, beginnart=None, lebenszeitvereinbarung=None,
    vereinbartes_dienstende_am=None, kuendigungszugang_am=None,
    kuendigung_durch_dienstverpflichteten=None, regel_624_anwendbar=None, einordnungsnachweis=None,
):
    """§624: Bindung länger als fünf Jahre/Lebenszeit, Kündigung erst nach fünf Jahren, sechs Monate Frist."""
    beginn = _datum(dienstbeginn_am, "dienstbeginn_am")
    _auswahl(beginnart, "beginnart", ("ereignis", "tagesbeginn"))
    _wahrheitswert(lebenszeitvereinbarung, "lebenszeitvereinbarung")
    ende = None
    if vereinbartes_dienstende_am is not None or not lebenszeitvereinbarung:
        ende = _datum(vereinbartes_dienstende_am, "vereinbartes_dienstende_am")
    zugang = _datum(kuendigungszugang_am, "kuendigungszugang_am")
    if zugang < beginn:
        _fehler("kuendigungszugang_am", "Kündigungszugang darf nicht vor dem hier betrachteten Dienstbeginn liegen.")
    if ende is not None and ende < beginn:
        _fehler("vereinbartes_dienstende_am", "Vereinbartes Ende darf nicht vor Dienstbeginn liegen.")
    _wahrheitswert(kuendigung_durch_dienstverpflichteten, "kuendigung_durch_dienstverpflichteten")
    _wahrheitswert(regel_624_anwendbar, "regel_624_anwendbar")
    _text(einordnungsnachweis, "einordnungsnachweis")
    eingaben = dict(dienstbeginn_am=dienstbeginn_am, beginnart=beginnart,
        lebenszeitvereinbarung=lebenszeitvereinbarung, vereinbartes_dienstende_am=vereinbartes_dienstende_am,
        kuendigungszugang_am=kuendigungszugang_am,
        kuendigung_durch_dienstverpflichteten=kuendigung_durch_dienstverpflichteten,
        regel_624_anwendbar=regel_624_anwendbar, einordnungsnachweis=einordnungsnachweis)
    wert = None
    if regel_624_anwendbar:
        fuenfjahre = _frist(dienstbeginn_am, 5, "jahre", beginnart)
        fruehestens = _tage_addieren(fuenfjahre, 1)
        lange_bindung = lebenszeitvereinbarung or ende > fuenfjahre
        noch_laufend = lebenszeitvereinbarung or zugang <= ende
        moeglich = lange_bindung and noch_laufend and zugang >= fruehestens and kuendigung_durch_dienstverpflichteten
        kuendigungsende = _frist(kuendigungszugang_am, 6, "monate", "ereignis") if moeglich else None
        wert = dict(fuenfjahreszeitraum_ende=fuenfjahre.isoformat(), fruehester_kuendigungstag=fruehestens.isoformat(),
            lange_bindung_erfuellt=lange_bindung, kuendigung_nach_624_zeitlich_moeglich=moeglich,
            rechnerisches_kuendigungsfristende=kuendigungsende.isoformat() if kuendigungsende is not None else None)
    ergebnis = _ergebnis(wert, "daten_und_wahrheitswerte", "BGB_DIENST_LANGZEITKUENDIGUNGSRAHMEN", eingaben,
        [dict(operation="Lebenszeit oder strikt längere Bindung als fünf Jahre; Zugang durch Dienstverpflichteten erst nach Fünfjahresablauf und während laufender Bindung, anschließend sechs Monate")], eingaben.copy())
    ergebnis["status"] = "BERECHNET" if regel_624_anwendbar else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = ["Konkreter langfristiger Dienstvertrag, rechtlicher Beginn und vereinbarte Bindung vorgegeben; feste lokale BGB-Fassung."]
    ergebnis["hinweise"] = ["Recht des Dienstverpflichteten, nicht automatisch des Dienstberechtigten. Genau fünfjährige Bindung genügt nicht. Kündigungszugang vor Ablauf der fünf Jahre nicht automatisch auf frühesten Termin verschieben. Rechnerische Sechsmonatsfrist ist kein Aufschub eines ohnehin früher eintretenden vereinbarten Vertragsendes. Bei Lebenszeitvereinbarung ist ein optionales Kalenderende für diese Prüfung ohne Wirkung; tatsächliches Lebenszeitende oder andere Beendigung vorab gesondert prüfen. Besondere Schutz-/Tarif-/Vertragsregeln, Erklärung und Zugang sowie weitere Wirksamkeitsvoraussetzungen gesondert; keine automatische Werktagsverschiebung einer Kündigungsfrist."]
    return ergebnis
