"""Wertbegrenzter Ersatz nützlicher und landwirtschaftlicher Verwendungen§§996/998."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _text


def besitzer_nuetzlicher_verwendungsersatz(
    verwendungskosten=None, fortbestehende_werterhoehung=None,
    andere_als_notwendige_verwendung=None, vor_rechtshaengigkeit_verwendet=None,
    vor_haftungsbeginn_990_verwendet=None, eigentuemer_besitzer_verhaeltnis_anwendbar=None,
    bewertungsnachweis=None,
):
    """§996: nützliche Verwendung vor beiden Haftungsgrenzen, höchstens fortbestehende Werterhöhung."""
    kosten = _geld(verwendungskosten)
    wert = _geld(fortbestehende_werterhoehung)
    eingaben = dict(verwendungskosten=verwendungskosten, fortbestehende_werterhoehung=fortbestehende_werterhoehung,
        andere_als_notwendige_verwendung=andere_als_notwendige_verwendung,
        vor_rechtshaengigkeit_verwendet=vor_rechtshaengigkeit_verwendet,
        vor_haftungsbeginn_990_verwendet=vor_haftungsbeginn_990_verwendet,
        eigentuemer_besitzer_verhaeltnis_anwendbar=eigentuemer_besitzer_verhaeltnis_anwendbar,
        bewertungsnachweis=bewertungsnachweis)
    for name in tuple(eingaben)[2:-1]:
        _wahrheitswert(eingaben[name], name)
    _text(bewertungsnachweis, "bewertungsnachweis")
    gilt = (andere_als_notwendige_verwendung and vor_rechtshaengigkeit_verwendet and
        vor_haftungsbeginn_990_verwendet and eigentuemer_besitzer_verhaeltnis_anwendbar)
    ergebnis = _geld_ergebnis(min(kosten, wert) if gilt else None, "BGB_BESITZER_NUETZLICHER_VERWENDUNGSERSATZ", eingaben,
        [dict(operation="Andere als notwendige Verwendungen vor Rechtshängigkeit und Haftungsbeginn§990, begrenzt auf bei Wiedererlangung fortbestehende Werterhöhung")])
    ergebnis["hinweise"].append("Werterhöhung muss auf den betrachteten Verwendungen beruhen und gerade bei Wiedererlangung durch Eigentümer fortbestehen; keine automatische Gleichsetzung mit damaligem Aufwand. Beide zeitlichen Voraussetzungen sind kumulativ und rechtlich vorzugeben; untertägige Reihenfolge nicht aus gleichem Datum folgern. Notwendige Verwendungen§994/995 und sonstige Anspruchsgrundlagen separat. Geltendmachung/Fälligkeit§1001 und Erlöschen§1002 nicht mitberechnet; keine doppelte Erstattung desselben Aufwands.")
    return ergebnis


def besitzer_landwirtschaftlicher_verwendungsersatz(
    ordnungsgemaesse_fruchtkosten=None, wert_noch_ungetrennter_fruechte=None,
    landwirtschaftliches_grundstueck_herauszugeben=None, fruechte_noch_ungetrennt=None,
    trennung_vor_wirtschaftsjahresende_ordnungsgemaess=None, bewertungsnachweis=None,
):
    """§998: ordnungsgemäße Fruchtkosten höchstens im Wert rechtzeitig zu trennender Früchte."""
    kosten = _geld(ordnungsgemaesse_fruchtkosten)
    wert = _geld(wert_noch_ungetrennter_fruechte)
    eingaben = dict(ordnungsgemaesse_fruchtkosten=ordnungsgemaesse_fruchtkosten,
        wert_noch_ungetrennter_fruechte=wert_noch_ungetrennter_fruechte,
        landwirtschaftliches_grundstueck_herauszugeben=landwirtschaftliches_grundstueck_herauszugeben,
        fruechte_noch_ungetrennt=fruechte_noch_ungetrennt,
        trennung_vor_wirtschaftsjahresende_ordnungsgemaess=trennung_vor_wirtschaftsjahresende_ordnungsgemaess,
        bewertungsnachweis=bewertungsnachweis)
    for name in tuple(eingaben)[2:-1]:
        _wahrheitswert(eingaben[name], name)
    _text(bewertungsnachweis, "bewertungsnachweis")
    gilt = (landwirtschaftliches_grundstueck_herauszugeben and fruechte_noch_ungetrennt and
        trennung_vor_wirtschaftsjahresende_ordnungsgemaess)
    ergebnis = _geld_ergebnis(min(kosten, wert) if gilt else None, "BGB_BESITZER_LANDWIRTSCHAFTLICHER_VERWENDUNGSERSATZ", eingaben,
        [dict(operation="Bei herauszugebendem landwirtschaftlichem Grundstück ordnungsgemäße Kosten ungetrennter, vor Wirtschaftsjahresende zu trennender Früchte auf Fruchtwert begrenzen")])
    ergebnis["hinweise"].append("Kosten und Fruchtwert müssen dieselben noch ungetrennten Früchte betreffen. Nur wirtschaftlich ordnungsgemäße Kostenanteile eingehen lassen; keine erfundene Angemessenheitsquote. Wirtschaftsjahr ist nicht automatisch Kalenderjahr. Wert und ordnungsgemäß rechtzeitige Trennbarkeit fachlich bestimmen; keine Berechnung zukünftiger Ernteerträge aus frei erfundenen Annahmen. Andere Nutzungs-/Fruchtherausgabe- und Verwendungsansprüche gesondert und ohne Doppelzählung.")
    return ergebnis
