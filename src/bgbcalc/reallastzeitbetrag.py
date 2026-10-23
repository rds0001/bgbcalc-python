"""Zeitbezogene Summierung persönlicher Reallastverbindlichkeiten (§1108I)."""
from .betraege import _geld
from .kalender import _datum, _ergebnis, _fehler, _text, _vorhanden
from .zahlen import _addieren, _bruch
from .zinsen import _bruchteile


def reallast_persoenlicher_faelligkeitsbetrag(erster_haftungstag=None, letzter_haftungstag=None, leistungen=None, einordnungsnachweis=None):
    """Geldleistungen summieren, deren Fälligkeit im qualifizierten Eigentumszeitraum liegt."""
    erster = _datum(erster_haftungstag,'erster_haftungstag');letzter = _datum(letzter_haftungstag,'letzter_haftungstag')
    if erster > letzter:
        _fehler('letzter_haftungstag','Letzter Haftungstag darf nicht vor erstem liegen.')
    _text(einordnungsnachweis,'einordnungsnachweis');_vorhanden(leistungen,'leistungen')
    if not isinstance(leistungen,list) or len(leistungen)>10000:
        _fehler('leistungen','Liste mit höchstens10000 eindeutig abgegrenzten Geldleistungen erforderlich.')
    namen=[];zugeordnet=[];ausserhalb=[];summe=_bruch(0)
    for leistung in leistungen:
        if not isinstance(leistung,dict) or set(leistung)!={'leistung_id','faellig_am','betrag'}:
            _fehler('leistungen','Genau leistung_id, faellig_am und betrag erforderlich.')
        name=_text(leistung['leistung_id'],'leistung_id');datum=_datum(leistung['faellig_am'],'faellig_am');betrag=_geld(leistung['betrag'])
        if name in namen:
            _fehler('leistung_id','Geldleistung darf nicht mehrfach berücksichtigt werden.')
        namen.append(name)
        if erster <= datum <= letzter:
            zugeordnet.append(name);summe=_addieren(summe,betrag)
        else:
            ausserhalb.append(name)
    eingaben=dict(erster_haftungstag=erster_haftungstag,letzter_haftungstag=letzter_haftungstag,leistungen=leistungen,einordnungsnachweis=einordnungsnachweis)
    wert=dict(persoenlicher_haftungsbetrag=_bruchteile(summe),zugeordnete_leistungen=zugeordnet,zeitlich_nicht_zugeordnete_leistungen=ausserhalb)
    ergebnis=_ergebnis(wert,'EUR_und_Leistungszuordnung','BGB_REALLAST_PERSOENLICHER_FAELLIGKEITSBETRAG',eingaben,[dict(operation='Nur während des qualifizierten Eigentumszeitraums fällige Geldleistungen vollständig summieren; keine zeitanteilige Kürzung nach Leistungsperiode.')],eingaben.copy())
    ergebnis['hinweise']=['§1108I-Grundfall ohne abweichende Bestimmung. Maßgeblich ist Fälligkeit während des Eigentums, nicht anteilige Dauer der Leistungsperiode. Erster und letzter eingeschlossener Haftungstag sind rechtlich normalisierte Grenzen eines abgeschlossenen Eigentumszeitraums; bei Eigentumswechsel am Fälligkeitstag muss die zeitliche Zuordnung eindeutig vorqualifiziert sein. Keine automatischen Grundbuch-/Eigentumsfeststellungen, keine intratägliche Zeitrechnung. Nur bereits bestimmte Geldleistungen; Naturalleistungen nicht eigenmächtig bewerten. Eingangsbeträge sind die rechtlich maßgeblichen noch offenen Leistungen ohne doppelte Positionen. Verjährung, Einreden, dingliche Verwertung und andere Haftungsgründe werden nicht entschieden. Teilgrundstückseigentümer nach1108II nicht durch freie Flächenquote entlasten; Gesamtschuld und Innenausgleich separat.']
    return ergebnis
