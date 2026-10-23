from .kalender import _datum, _ergebnis, _tage_addieren, _text

def prozesszins_erster_zinstag(rechtshaengigkeit_am=None, faelligkeits_zinsbeginn_am=None, einordnungsnachweis=None):
    """Folgetag der Rechtshängigkeit mit dem qualifizierten fälligkeitsbezogenen ersten Zinstag vergleichen und den späteren Tag wählen."""
    haengig = _datum(rechtshaengigkeit_am,'rechtshaengigkeit_am')
    faellig = _datum(faelligkeits_zinsbeginn_am,'faelligkeits_zinsbeginn_am')
    _text(einordnungsnachweis,'einordnungsnachweis')
    nach_haengigkeit = _tage_addieren(haengig,1)
    wert = dict(rechtshaengigkeits_zinsbeginn=nach_haengigkeit.isoformat(),erster_prozesszinstag=max(nach_haengigkeit,faellig).isoformat())
    eingaben = dict(rechtshaengigkeit_am=rechtshaengigkeit_am, faelligkeits_zinsbeginn_am=faelligkeits_zinsbeginn_am, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,"daten",'BGB_PROZESSZINS_ERSTER_ZINSTAG',eingaben,[dict(operation='Folgetag der Rechtshängigkeit mit dem qualifizierten fälligkeitsbezogenen ersten Zinstag vergleichen und den späteren Tag wählen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§291: kein Schuldnerverzug für Prozesszinsen erforderlich. Rechtshängigkeitsbezogener Beginn am Folgetag entsprechend187I, primär belegt durchBAG6AZR237/15Rn43. Spätere Fälligkeit begrenzt den Beginn zusätzlich; deren erster Zinstag muss bereits rechtlich bestimmt sein, keine pauschale ungeprüfte Behandlung jedes Fälligkeitstags als Ereignis oder Tagesbeginn. Verschiedene Forderungs-/Ratenanteile mit verschiedenen Fälligkeiten getrennt rechnen. Für Betrag vorhandenen Verzugszins-Satzkern entsprechend291/288 verwenden, ohne tatsächlichen Verzug zu unterstellen; Zinsforderungen gemäß289Satz1 nicht einfach mitverzinsen. Andere früher beginnende Zinsansprüche bleiben separat.']
    return ergebnis
