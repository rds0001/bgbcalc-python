from .kalender import _datum, _ergebnis, _fehler, _text

def betreuung_genehmigung_ablaufgrenze(rechnerisches_fristende_ohne_genehmigungsverfahren=None, genehmigungsverfahren_beginn_am=None, genehmigung_rechtskraft_am=None, einordnungsnachweis=None):
    """Rechtzeitig begonnenes Genehmigungsverfahren prüfen; bisherigen letzten Fristtag frühestens auf die Rechtskraft der Erteilung verschieben, ohne Verfahrenstage zu addieren."""
    grund = _datum(rechnerisches_fristende_ohne_genehmigungsverfahren,'rechnerisches_fristende_ohne_genehmigungsverfahren')
    beginn = _datum(genehmigungsverfahren_beginn_am,'genehmigungsverfahren_beginn_am')
    ende = _datum(genehmigung_rechtskraft_am,'genehmigung_rechtskraft_am')
    _text(einordnungsnachweis,'einordnungsnachweis')
    if beginn>grund:
        _fehler('genehmigungsverfahren_beginn_am','Keine Wiederbelebung einer vor Verfahrensbeginn abgelaufenen Frist.')
    if ende<beginn:
        _fehler('genehmigung_rechtskraft_am','Rechtskraft darf nicht vor Verfahrensbeginn liegen.')
    wert = dict(rechnerisches_fristende=max(grund,ende).isoformat())
    eingaben = dict(rechnerisches_fristende_ohne_genehmigungsverfahren=rechnerisches_fristende_ohne_genehmigungsverfahren, genehmigungsverfahren_beginn_am=genehmigungsverfahren_beginn_am, genehmigung_rechtskraft_am=genehmigung_rechtskraft_am, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'datum','BGB_BETREUUNG_GENEHMIGUNG_ABLAUFGRENZE',eingaben,[dict(operation='Rechtzeitig begonnenes Genehmigungsverfahren prüfen; bisherigen letzten Fristtag frühestens auf die Rechtskraft der Erteilung verschieben, ohne Verfahrenstage zu addieren.')],eingaben.copy())
    ergebnis["hinweise"] = ['§1858III: qualifiziertes einseitiges Rechtsgeschäft gegenüber Gericht oder Behörde, für das eine nachträgliche betreuungsgerichtliche Genehmigung rechtskräftig erteilt wird. Gesetzlicher Fristablauf während des wirksamen Genehmigungsverfahrens gehemmt; keine Addition sämtlicher Verfahrenstage nach209 und keine neue volle Frist ab Rechtskraft. Verfahrensbeginn und Rechtskraft der Erteilung bereits rechtlich bestimmt. Rechtskraft einer Versagung, nichtgesetzliche Fristen und andere Genehmigungslagen sind nicht Gegenstand dieses Bausteins. Ein bereits vor Verfahrensbeginn außerhalb des Schutzes eingetretener Fristablauf wird nicht wiederbelebt. Bei laufendem Verfahren ohne Rechtskraft kein fiktiver Endtag. Ereignisse auf rechtlich maßgebliche Kalendertage normalisieren; weitere Fristkorrekturen gesondert.']
    return ergebnis

