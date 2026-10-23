"""Erbquoten der zweiten Ordnung auf Grundlage der beiden Elternlinien."""
from .betraege import _wahrheitswert
from .erbstaemme import abkoemmlings_erbquoten
from .kalender import _fehler, _vorhanden


def elternlinien_erbquoten(
    elternlinien=None, erste_ordnung_vorhanden=None,
    verwandtenanteil_zaehler=None, verwandtenanteil_nenner=None,
):
    """§§ 1925/1927/1930: zweite Ordnung einschließlich mehrfacher Linienanteile."""
    _vorhanden(elternlinien, "elternlinien")
    if not isinstance(elternlinien, list) or len(elternlinien) != 2:
        _fehler("elternlinien", "Genau zwei Elternlinien erforderlich.")
    _wahrheitswert(erste_ordnung_vorhanden, "erste_ordnung_vorhanden")
    ergebnis = abkoemmlings_erbquoten(elternlinien, verwandtenanteil_zaehler, verwandtenanteil_nenner)
    eingaben = dict(elternlinien=elternlinien, erste_ordnung_vorhanden=erste_ordnung_vorhanden,
                    verwandtenanteil_zaehler=verwandtenanteil_zaehler,
                    verwandtenanteil_nenner=verwandtenanteil_nenner)
    ergebnis["regel_id"] = "BGB_ELTERNLINIEN_ERBQUOTEN"
    ergebnis["eingaben"] = eingaben
    ergebnis["nutzervorgaben"] = eingaben.copy()
    schritt = ergebnis["rechenschritte"][1]
    schritt["besetzte_elternlinien"] = schritt.pop("besetzte_kinderstaemme")
    ergebnis["rechenschritte"].insert(0, dict(
        operation="Vorrang der ersten Ordnung prüfen", erste_ordnung_vorhanden=erste_ordnung_vorhanden))
    if erste_ordnung_vorhanden:
        ergebnis["wert"] = None
        ergebnis["status"] = "NICHT_ANWENDBAR"
    ergebnis["hinweise"] = [
        "Elternschaft und Abkömmlingsbeziehungen einschließlich Adoptionsausschlüssen sind rechtlich vorgegeben.",
        "Keine automatische Ehegattenquote oder Prüfung weiterer Erbordnungen.",
        "Mehrfachzugehörigkeit bleibt als besondere Erbteile sichtbar; keine Rundung.",
    ]
    return ergebnis
