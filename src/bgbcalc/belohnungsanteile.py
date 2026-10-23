from .betraege import _geld_ergebnis
from .kalender import _auswahl, _fehler, _ganzzahl, _text
from .teilverguetung import _teilbetrag


def auslobung_belohnungsanteil(gesamtbelohnung=None, verteilungsart=None, anzahl_berechtigte=None, anteil_zaehler=None, anteil_nenner=None, verteilungsnachweis=None):
    """Teilbare Geldbelohnung gleichmäßig oder nach qualifiziertem Mitwirkungsanteil verteilen."""
    _auswahl(verteilungsart,'verteilungsart',('gleichzeitige_handlung','gleiche_preiswuerdigkeit','mitwirkungsanteil'))
    _text(verteilungsnachweis,'verteilungsnachweis')
    if verteilungsart=='mitwirkungsanteil':
        if anzahl_berechtigte is not None:
            _fehler('anzahl_berechtigte','Bei vorgegebenem Mitwirkungsanteil keine ungenutzte Personenzahl eingeben.')
        betrag=_teilbetrag(gesamtbelohnung,anteil_zaehler,anteil_nenner)
    else:
        _ganzzahl(anzahl_berechtigte,'anzahl_berechtigte',2,9007199254740991)
        if anteil_zaehler is not None or anteil_nenner is not None:
            _fehler('anteil','Gleichverteilung nicht mit vorgegebenen Anteilen vermischen.')
        betrag=_teilbetrag(gesamtbelohnung,1,anzahl_berechtigte)
    eingaben=dict(gesamtbelohnung=gesamtbelohnung,verteilungsart=verteilungsart,anzahl_berechtigte=anzahl_berechtigte,anteil_zaehler=anteil_zaehler,anteil_nenner=anteil_nenner,verteilungsnachweis=verteilungsnachweis)
    ergebnis=_geld_ergebnis(betrag,'BGB_AUSLOBUNG_BELOHNUNGSANTEIL',eingaben,[dict(operation='Geldbelohnung durch Zahl gleichberechtigter Personen teilen beziehungsweise mit qualifiziertem Mitwirkungsanteil multiplizieren.')])
    ergebnis['hinweise'].append('§659II/661III: rechtlich festgestellte Gleichzeitigkeit beziehungsweise gleiche Preiswürdigkeit, teilbare Geldbelohnung und kein Vorbehalt nur eines Empfängers. Losentscheid bei Unteilbarkeit/Einzelempfängervorbehalt außerhalb dieser Berechnung. §660I: verbindlich festgestellter billiger Mitwirkungsanteil; Funktion bewertet Beiträge nicht. Bei mehreren Einzelaufrufen müssen sämtliche qualifizierten Mitwirkungsquoten zusammen eins ergeben, keine mehrfachen Vollbelohnungen. Streitbedingtes Leistungsverweigerungsrecht660II, Hinterlegung und Preisvergabewirksamkeit gesondert. Keine Rundung oder Abrechnung bereits gezahlter Teilbeträge.')
    return ergebnis
