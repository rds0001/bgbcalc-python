from .kalender import _auswahl, _datum, _ergebnis, _frist, _text

def miete_erwerber_monatsgrenze(regelfall=None, massgebliches_ereignis_am=None, einordnungsnachweis=None):
    """Bis einschließlich Tag15 das laufende Monatsende, ab Tag16 das Ende des Folgemonats als zeitliche Mietgrenze bestimmen."""
    _auswahl(regelfall,'regelfall',('vorausverfuegung_566b','mietergeschaeft_566c'))
    tag = _datum(massgebliches_ereignis_am,'massgebliches_ereignis_am')
    _text(einordnungsnachweis,'einordnungsnachweis')
    erweitert = tag.day>15
    ende = _frist(tag.replace(day=1).isoformat(),2 if erweitert else 1,'monate','tagesbeginn')
    eingaben = dict(regelfall=regelfall, massgebliches_ereignis_am=massgebliches_ereignis_am, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(dict(zeitliche_mietgrenze=ende.isoformat(),folgemonat_einbezogen=erweitert),"datum_und_wahrheitswert",'BGB_MIETE_ERWERBER_MONATSGRENZE',eingaben,[dict(operation='Bis einschließlich Tag15 das laufende Monatsende, ab Tag16 das Ende des Folgemonats als zeitliche Mietgrenze bestimmen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§566bI und566cSatz1/2: nur zeitliche Grundgrenze der erfassten Mietzeiträume. Ereignis am15. verlängert nicht, am16. verlängert um einen Kalendermonat. Bei566bII kann Kenntnis des Erwerbers weitergehende Vorausverfügungen wirksam werden lassen; bei566cSatz3 kann ein nach Eigentumsübergang mit Kenntnis vorgenommenes Mietergeschaft trotz dieses Zeitfensters unwirksam sein. Diese Ausnahmen nicht aus dem Datumsresultat ableiten. Für566d ist die zeitliche Grenze nur ein Bestandteil; Erwerbs-/Fälligkeitschronologie der Gegenforderung separat. Keine Kündigungsfrist, keine automatische193Verschiebung und kein Wirksamkeitsentscheid.']
    return ergebnis
