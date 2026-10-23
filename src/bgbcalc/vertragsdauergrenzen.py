from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _text


def schuldrecht_vertragsdauergrenze(regelfall=None, vertragsbeginn_am=None, vertragsende_am=None, dauernachweis=None):
    """Qualifizierte feste Vertragsdauer mit Ein-, Zwei- oder Dreijahresgrenze vergleichen."""
    _auswahl(regelfall,'regelfall',('teilzeitwohnrecht_481','urlaubsprodukt_481a','landpacht_textform_585a','landpacht_fortsetzung_594'))
    beginn=_datum(vertragsbeginn_am,'vertragsbeginn_am')
    unbegrenzt=isinstance(vertragsende_am,str) and vertragsende_am=='unbegrenzt_verlaengerbar'
    if unbegrenzt and regelfall not in ('teilzeitwohnrecht_481','urlaubsprodukt_481a'): _fehler('vertragsende_am','Unbegrenzte Verlaengerung nur fuer481/481a verwenden.')
    ende=None if unbegrenzt else _datum(vertragsende_am,'vertragsende_am')
    _text(dauernachweis,'dauernachweis')
    if not unbegrenzt and ende<beginn:
        _fehler('vertragsende_am','Vertragsende darf nicht vor Vertragsbeginn liegen.')
    jahre=3 if regelfall=='landpacht_fortsetzung_594' else 2 if regelfall=='landpacht_textform_585a' else 1
    grenze=_frist(vertragsbeginn_am,jahre,'jahre','tagesbeginn')
    streng=regelfall!='landpacht_fortsetzung_594'
    eingaben=dict(regelfall=regelfall,vertragsbeginn_am=vertragsbeginn_am,vertragsende_am=vertragsende_am,dauernachweis=dauernachweis)
    wert=dict(grenzdauer_jahre=jahre,ende_der_grenzdauer=grenze.isoformat(),vergleich='mehr_als' if streng else 'mindestens',dauergrenze_erfuellt=True if unbegrenzt else (ende>grenze if streng else ende>=grenze))
    ergebnis=_ergebnis(wert,'datum_und_wahrheitswert','BGB_SCHULDRECHT_VERTRAGSDAUERGRENZE',eingaben,[dict(operation='Grenzdauer ab Tagesbeginn berechnen; inklusives Vertragsende streng mit Ein-/Zweijahresende oder einschließlich mit Dreijahresende vergleichen.')],eingaben.copy())
    ergebnis['hinweise']=['Nur numerischer Dauervergleich, keine vollstaendige Vertragsqualifikation oder Formentscheidung. Beginn als rechtlich massgeblicher Tagesbeginn und endlichen letzten Vertragstag einschliesslich Tagesablauf vorgeben. Bei481/481a saemtliche rechtlich vorgesehenen Verlaengerungsmoeglichkeiten beruecksichtigen. Ein endlich bestimmbares maximales Enddatum kann auch aus gestaffelten oder alternativen Optionen stammen; kein automatisches Lesen beliebiger Vertragsklauseln. Nur bei481/481a bezeichnet vertragsende_am=unbegrenzt_verlaengerbar eine rechtlich qualifizierte ohne endliche Gesamtgrenze wiederholbare Verlaengerungsmoeglichkeit: die Einjahresgrenze ist dann ueberschreitbar und damit erfuellt, ohne ein fiktives Enddatum zu erfinden. Nicht gleichbedeutend mit unbekanntem Enddatum oder blosser Unklarheit der Vertragsauslegung. Bei585aTextform und bei594Anfrage/Ablehnungsfrist gesondert. Untertaegige Laufzeiten gesondert qualifizieren.']
    return ergebnis
