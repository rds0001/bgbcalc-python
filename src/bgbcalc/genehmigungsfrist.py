"""Zweiwöchige Genehmigungsfrist nach Aufforderung§§108/177."""
from .betraege import _wahrheitswert
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _text


def genehmigung_aufforderungsfrist(
    regelbereich=None, aufforderungszugang_am=None, massgebliches_fristende=None,
    prueftag=None, genehmigung_erklaert_am=None, gegenueber_aufforderndem=None,
    genehmigung_durch_berechtigten=None, aufforderung_wirksam=None, einordnungsnachweis=None,
):
    """§108 Absatz2/§177 Absatz2: wirksame rechtzeitige Genehmigung und Verweigerungsfiktion."""
    _auswahl(regelbereich, "regelbereich", ("minderjaehrigenvertrag", "vertretung_ohne_vertretungsmacht"))
    zugang = _datum(aufforderungszugang_am, "aufforderungszugang_am")
    ende = _datum(massgebliches_fristende, "massgebliches_fristende")
    tag = _datum(prueftag, "prueftag")
    genehmigung = _datum(genehmigung_erklaert_am, "genehmigung_erklaert_am") if genehmigung_erklaert_am is not None else None
    if tag < zugang:
        _fehler("prueftag", "Prüftag darf nicht vor Aufforderungszugang liegen.")
    if genehmigung is not None and (genehmigung < zugang or genehmigung > tag):
        _fehler("genehmigung_erklaert_am", "Hier geprüfte Genehmigung muss zwischen Aufforderungszugang und Prüftag liegen.")
    grundende = _frist(aufforderungszugang_am, 2, "wochen", "ereignis")
    if ende < grundende:
        _fehler("massgebliches_fristende", "Maßgebliches Ende darf die gesetzliche Zweiwochenfrist nicht verkürzen.")
    eingaben = dict(regelbereich=regelbereich, aufforderungszugang_am=aufforderungszugang_am,
        massgebliches_fristende=massgebliches_fristende, prueftag=prueftag,
        genehmigung_erklaert_am=genehmigung_erklaert_am, gegenueber_aufforderndem=gegenueber_aufforderndem,
        genehmigung_durch_berechtigten=genehmigung_durch_berechtigten,
        aufforderung_wirksam=aufforderung_wirksam, einordnungsnachweis=einordnungsnachweis)
    for name in tuple(eingaben)[5:-1]:
        _wahrheitswert(eingaben[name], name)
    _text(einordnungsnachweis, "einordnungsnachweis")
    wert = None
    if aufforderung_wirksam:
        rechtzeitig = (genehmigung is not None and genehmigung <= ende and gegenueber_aufforderndem and
            genehmigung_durch_berechtigten)
        abgelaufen = tag > ende
        wert = dict(rechnerisches_zweiwochenende=grundende.isoformat(), frist_abgelaufen=abgelaufen,
            genehmigung_rechtzeitig_erklaert=rechtzeitig,
            genehmigung_gilt_verweigert=abgelaufen and not rechtzeitig)
    ergebnis = _ergebnis(wert, "daten_und_wahrheitswerte", "BGB_GENEHMIGUNG_AUFFORDERUNGSFRIST", eingaben,
        [dict(operation="Zweiwochenmindestfrist prüfen; Genehmigung durch Berechtigten gegenüber aufforderndem Teil bis zum maßgeblichen Fristende; sonst Verweigerungsfiktion nach Ablauf")], eingaben.copy())
    ergebnis["status"] = "BERECHNET" if aufforderung_wirksam else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = ["Wirksame Aufforderung im konkreten gesetzlichen Genehmigungstatbestand und rechtlich maßgebliches Fristende einschließlich erforderlicher Kalenderkorrekturen vorgegeben."]
    ergebnis["hinweise"] = ["Nur Frist-/Empfängerprüfung der Genehmigung nach Aufforderung, keine vollständige Vertragswirksamkeit. Vorher gegenüber Minderjährigem beziehungsweise Vertreter erklärte Genehmigung/Verweigerung wird durch qualifizierte Aufforderung unwirksam; solche vorherigen Erklärungen hier nicht als spätere Genehmigung eingeben. Bereits wirksam gegenüber dem anderen Vertragsteil erklärte Genehmigung nicht automatisch rückgängig machen. Minderjähriger nach Eintritt unbeschränkter Geschäftsfähigkeit nach§108 Absatz3 selbst genehmigungsberechtigt; Berechtigung rechtlich bestimmen. Tatsächliche frühere Verweigerung, Widerruf und andere Unwirksamkeitsgründe separat. Erklärungstag muss rechtlich maßgeblichen Zugang abbilden, nicht bloß Versand; untertägige Reihenfolge gesondert. Nach Ablauf fingierte Verweigerung wird durch verspätete Genehmigung nicht automatisch geheilt."]
    return ergebnis
