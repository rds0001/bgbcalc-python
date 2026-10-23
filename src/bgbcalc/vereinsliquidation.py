"""Vereinsliquidation: Vermögensdifferenz, Sperrjahr und gesetzlicher Gleichanteil."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _datum, _ergebnis, _frist, _ganzzahl, _tage_addieren, _text
from .zahlen import GRENZE, _bruch, _dividieren, _subtrahieren
from .zinsen import _bruchteile


def vereins_liquidationsueberschuss(
    verfuegbares_liquidationsvermoegen=None, noch_zu_befriedigende_verbindlichkeiten=None,
    bestandsnachweis=None,
):
    """§49 Absatz1: Überschuss beziehungsweise Fehlbetrag aus abgegrenztem Bestand."""
    vermoegen = _geld(verfuegbares_liquidationsvermoegen)
    schulden = _geld(noch_zu_befriedigende_verbindlichkeiten)
    _text(bestandsnachweis, "bestandsnachweis")
    eingaben = dict(verfuegbares_liquidationsvermoegen=verfuegbares_liquidationsvermoegen,
        noch_zu_befriedigende_verbindlichkeiten=noch_zu_befriedigende_verbindlichkeiten,
        bestandsnachweis=bestandsnachweis)
    differenz = _subtrahieren(vermoegen, schulden)
    ergebnis = _geld_ergebnis(_bruch(0), "BGB_VEREINS_LIQUIDATIONSUEBERSCHUSS", eingaben,
        [dict(operation="Abgegrenztes verfügbares Vermögen und noch zu befriedigende Verbindlichkeiten gegenüberstellen")])
    ergebnis["wert"] = dict(ueberschuss=_bruchteile(max(differenz, _bruch(0))),
        fehlbetrag=_bruchteile(max(-differenz, _bruch(0))))
    ergebnis["hinweise"].append("Rechnerischer Bestand nach vorgesehenem Gläubigerausgleich, keine Ausantwortungsfreigabe. Sperrjahr, Hinterlegung/Sicherung, tatsächliche Gläubigerbefriedigung und Insolvenzpflichten gesondert.")
    return ergebnis


def vereins_liquidationssperrjahr(erste_einrueckung=None, bekanntmachung_ordnungsgemaess=None,
                               bekanntmachungsnachweis=None):
    """§§50/51: Bekanntmachungswirkung nach zwei Tagen und anschließendes Sperrjahr."""
    einrueckung = _datum(erste_einrueckung, "erste_einrueckung")
    _wahrheitswert(bekanntmachung_ordnungsgemaess, "bekanntmachung_ordnungsgemaess")
    _text(bekanntmachungsnachweis, "bekanntmachungsnachweis")
    eingaben = dict(erste_einrueckung=erste_einrueckung,
        bekanntmachung_ordnungsgemaess=bekanntmachung_ordnungsgemaess,
        bekanntmachungsnachweis=bekanntmachungsnachweis)
    wert = None
    if bekanntmachung_ordnungsgemaess:
        bewirkt = _tage_addieren(einrueckung, 2)
        ende = _frist(bewirkt.isoformat(), 1, "jahre", "ereignis")
        wert = dict(bekanntmachung_bewirkt_mit_tagesablauf=bewirkt.isoformat(),
            sperrjahr_ende=ende.isoformat(), fruehester_tag_nach_sperrjahr=_tage_addieren(ende, 1).isoformat())
    ergebnis = _ergebnis(wert, "kalenderdaten", "BGB_VEREINS_LIQUIDATIONSSPERRJAHR", eingaben,
        [dict(operation="Wirkung mit Ablauf des zweiten Tages nach erster Einrückung; ein Jahr Sperrfrist und ersten Tag danach bestimmen")], eingaben.copy())
    ergebnis["status"] = "BERECHNET" if bekanntmachung_ordnungsgemaess else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = ["Ordnungsgemäße Bekanntmachung nach§50 einschließlich Gläubigeraufforderung und maßgeblichem Veröffentlichungsblatt vorgegeben."]
    ergebnis["hinweise"] = ["Nur Kalendergrenze des§51, keine endgültige Verteilungsfreigabe. Gläubigerbefriedigung, besondere Mitteilungen, Hinterlegung und Sicherheit nach§§50/52/53 bleiben gesondert.",
        "Keine automatische Wochenend-/Feiertagsverschiebung einer Sperrfrist. Wirkung der Bekanntmachung tritt erst mit Tagesablauf ein."]
    return ergebnis


def vereinsvermoegen_mitgliederanteil(
    verteilbarer_ueberschuss=None, mitglieder_bei_aufloesung=None,
    anfallberechtigte_anderweitig_bestimmt=None, ausschliessliche_mitgliederinteressen=None,
    verteilungsnachweis=None,
):
    """§45 Absatz3: gleiche Anteile der maßgeblichen Mitglieder im gesetzlichen Auffangfall."""
    vermoegen = _geld(verteilbarer_ueberschuss)
    anzahl = _ganzzahl(mitglieder_bei_aufloesung, "mitglieder_bei_aufloesung", 1, GRENZE)
    _wahrheitswert(anfallberechtigte_anderweitig_bestimmt, "anfallberechtigte_anderweitig_bestimmt")
    _wahrheitswert(ausschliessliche_mitgliederinteressen, "ausschliessliche_mitgliederinteressen")
    _text(verteilungsnachweis, "verteilungsnachweis")
    eingaben = dict(verteilbarer_ueberschuss=verteilbarer_ueberschuss,
        mitglieder_bei_aufloesung=mitglieder_bei_aufloesung,
        anfallberechtigte_anderweitig_bestimmt=anfallberechtigte_anderweitig_bestimmt,
        ausschliessliche_mitgliederinteressen=ausschliessliche_mitgliederinteressen,
        verteilungsnachweis=verteilungsnachweis)
    wert = None
    if not anfallberechtigte_anderweitig_bestimmt and ausschliessliche_mitgliederinteressen:
        wert = _dividieren(vermoegen, _bruch(anzahl))
    ergebnis = _geld_ergebnis(wert, "BGB_VEREINSVERMOEGEN_MITGLIEDERANTEIL", eingaben,
        [dict(operation="Gesetzlichen Auffangfall prüfen und verteilbaren Überschuss gleichmäßig auf maßgebliche Mitglieder aufteilen")])
    ergebnis["hinweise"].append("Nur Gleichverteilung§45 Absatz3. Bei anderer Bestimmung oder fehlenden ausschließlichen Mitgliederinteressen NICHT_ANWENDBAR; insbesondere kein automatischer Mitgliederanteil beim Fiskalanfall. Ausantwortungsreife und Anfallberechtigte vorab klären.")
    return ergebnis
