from .kalender import _auswahl, _datum, _ergebnis, _frist, _text


def miete_erklaerungs_monatsendtermin(fristfall=None, zugang_erklaerung_am=None, einordnungsnachweis=None):
    """Kalendermonatsende nach qualifizierter Modernisierungsankündigung oder Erhöhungserklärung."""
    faelle={'modernisierung_haerteeinwand_555d':1,'modernisierung_kuendigungserklaerung_555e':1,'modernisierung_beendigung_555e':2,'mieterhoehung_kuendigungserklaerung_561':2}
    _auswahl(fristfall,'fristfall',tuple(faelle))
    tag=_datum(zugang_erklaerung_am,'zugang_erklaerung_am');_text(einordnungsnachweis,'einordnungsnachweis')
    ende=_frist(tag.replace(day=1).isoformat(),faelle[fristfall]+1,'monate','tagesbeginn')
    eingaben=dict(fristfall=fristfall,zugang_erklaerung_am=zugang_erklaerung_am,einordnungsnachweis=einordnungsnachweis)
    ergebnis=_ergebnis(dict(rechnerischer_monatsendtermin=ende.isoformat()),'datum','BGB_MIETE_ERKLAERUNGS_MONATSENDTERMIN',eingaben,[dict(operation='Ende des ersten oder zweiten Kalendermonats nach dem Zugangsmonat bestimmen; keine tageweise Monatsaddition ab Zugangstag.')],eingaben.copy())
    ergebnis['hinweise']=['Gesetzliche Grundtermine:555dIII Härteeinwand bis Ende des Folgemonats bei ordnungsgemäßer Ankündigung und anwendbarer Frist; Hinweismangel555dV und unverschuldete Verspätung555dIV gesondert.555eI Kündigungserklärung bis Folgemonatsende, Mietende zum Ende des übernächsten Monats bezogen auf Zugang der Modernisierungsankündigung;555cIV-Ausnahme vorqualifizieren.561I hier ausschließlich letzter Grundtermin der Kündigungserklärung nach Erhöhungserklärung558/559; Beendigungstermin und Wegfall der Erhöhung separat. Keine automatische193Verschiebung von Erklärungsfristen; erforderlichenfalls separat mit qualifiziertem Anwendungsbereich prüfen. Mietbeendigungsdatum nicht deshalb verschieben.']
    return ergebnis
