from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _text

def digitalprodukt_beweislastzeitvergleich(bereitstellungsart=None, bereitstellung_an_verbraucher_am=None, abweichung_gezeigt_am=None, bereitstellungsende_am=None, einordnungsnachweis=None):
    """Auftreten eines abweichenden Zustands mit Jahresgrundgrenze oder tatsächlichem dauerhaften Bereitstellungszeitraum vergleichen."""
    _auswahl(bereitstellungsart,'bereitstellungsart',('einmalig','befristet_dauerhaft','unbefristet_dauerhaft'))
    beginn=_datum(bereitstellung_an_verbraucher_am,'bereitstellung_an_verbraucher_am');abweichung=_datum(abweichung_gezeigt_am,'abweichung_gezeigt_am');_text(einordnungsnachweis,'einordnungsnachweis')
    if bereitstellungsart=='befristet_dauerhaft':
        ende=_datum(bereitstellungsende_am,'bereitstellungsende_am')
        if ende<beginn: _fehler('bereitstellungsende_am','Ende darf nicht vor Beginn liegen.')
    else:
        if bereitstellungsende_am is not None: _fehler('bereitstellungsende_am','Nur bei befristeter Dauerbereitstellung setzen.')
        ende=_frist(bereitstellung_an_verbraucher_am,1,'jahre','ereignis') if bereitstellungsart=='einmalig' else None
    wert=dict(zeitfenster_beginn_am=beginn.isoformat(),zeitfenster_ende_am=None if ende is None else ende.isoformat(),abweichung_im_zeitfenster=abweichung>=beginn and (ende is None or abweichung<=ende))
    eingaben = dict(bereitstellungsart=bereitstellungsart, bereitstellung_an_verbraucher_am=bereitstellung_an_verbraucher_am, abweichung_gezeigt_am=abweichung_gezeigt_am, bereitstellungsende_am=bereitstellungsende_am, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'daten_und_wahrheitswert','BGB_DIGITALPRODUKT_BEWEISLASTZEITVERGLEICH',eingaben,[dict(operation='Auftreten eines abweichenden Zustands mit Jahresgrundgrenze oder tatsächlichem dauerhaften Bereitstellungszeitraum vergleichen.')],eingaben.copy())
    ergebnis["hinweise"] = ['Bei einmaliger Bereitstellung Jahresgrundgrenze nach§327kI/§§187I/188; bei dauerhafter Bereitstellung tatsächlicher qualifizierter Bereitstellungszeitraum nach§327kII. Beginn jeweils Bereitstellung an den Verbraucher, auch nach§327uIII. Abweichung muss innerhalb einschließlich Anfangs-/Endtag auftreten; tatsächliche Reihenfolge am selben Tag ist qualifiziert. Unbefristete Bereitstellung hat keine erfundene maximale Jahresgrenze. Ergebnis bezeichnet ausschließlich zeitliche Voraussetzung, keine automatische Beweislast-, Mangel- oder Haftungsentscheidung. Technische Umgebung, Mitwirkung und Belehrung nachAbsätzen3/4 separat; keine193Verlängerung des Beobachtungszeitraums.']
    return ergebnis

