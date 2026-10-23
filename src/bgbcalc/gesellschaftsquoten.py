from .betraege import _geld
from .kalender import _auswahl, _ergebnis, _fehler, _ganzzahl, _text
from .zahlen import _bruch, _dividieren, _multiplizieren
from .zinsen import _bruchteile


def gesellschaft_vererbter_anteil(gesellschaftsanteil_zaehler=None, gesellschaftsanteil_nenner=None, erbquote_zaehler=None, erbquote_nenner=None, einordnungsnachweis=None):
    """Gesellschaftsanteil des Erblassers mit qualifizierter individueller Erbquote multiplizieren."""
    eingaben=dict(gesellschaftsanteil_zaehler=gesellschaftsanteil_zaehler,gesellschaftsanteil_nenner=gesellschaftsanteil_nenner,erbquote_zaehler=erbquote_zaehler,erbquote_nenner=erbquote_nenner,einordnungsnachweis=einordnungsnachweis)
    quoten=[]
    for basis in ('gesellschaftsanteil','erbquote'):
        z=_ganzzahl(eingaben[basis+'_zaehler'],basis+'_zaehler',0,9007199254740991);n=_ganzzahl(eingaben[basis+'_nenner'],basis+'_nenner',1,9007199254740991)
        if z>n:_fehler(basis,'Anteil darf eins nicht übersteigen.')
        quoten.append(_bruch(z,n))
    _text(einordnungsnachweis,'einordnungsnachweis')
    ergebnis=_ergebnis(_bruchteile(_multiplizieren(quoten[0],quoten[1])),'anteil','BGB_GESELLSCHAFT_VERERBTER_ANTEIL',eingaben,[dict(operation='Bisherigen Gesellschaftsanteil mit individueller Erbquote multiplizieren; vererbten Anteil an der Gesellschaft als dimensionslosen Bruch ausweisen.')],eingaben.copy())
    ergebnis['hinweise']=['§711II: qualifizierte gesellschaftsvertragliche Fortsetzung mit Erben und maßgebliche Erbquote vorausgesetzt. Bei mehreren Erben fällt jedem ein entsprechender Anteil zu; keine Umdeutung in einen einzigen ungeteilten Erbengemeinschaftsanteil. Für mehrere Einzelaufrufe müssen die verwendeten Erbquoten den Erbfall vollständig und ohne Doppelzählung abbilden. Kein EUR-Wert, keine Vertragsauslegung, kein Abfindungsanspruch und keine Berechnung der Erbquote selbst.']
    return ergebnis


def stimmgewichts_mehrheitsgrenze(regelfall=None, zustimmendes_stimmgewicht=None, massgebliches_gesamtgewicht=None, einordnungsnachweis=None):
    """Zustimmungsgewicht mit Dreiviertelmehrheit oder strikter Anteilsmehrheit vergleichen."""
    _auswahl(regelfall,'regelfall',('gesellschaft_aufloesung_732','gesellschaft_fortsetzung_734','gemeinschaft_verwaltung_745'))
    ja=_geld(zustimmendes_stimmgewicht);gesamt=_geld(massgebliches_gesamtgewicht);_text(einordnungsnachweis,'einordnungsnachweis')
    if gesamt==0 or ja>gesamt:
        _fehler('massgebliches_gesamtgewicht','Positives maßgebliches Gesamtgewicht erforderlich; Zustimmungsgewicht darf es nicht übersteigen.')
    quote=_dividieren(ja,gesamt);streng=regelfall=='gemeinschaft_verwaltung_745';grenze=_bruch(1,2) if streng else _bruch(3,4)
    eingaben=dict(regelfall=regelfall,zustimmendes_stimmgewicht=zustimmendes_stimmgewicht,massgebliches_gesamtgewicht=massgebliches_gesamtgewicht,einordnungsnachweis=einordnungsnachweis)
    wert=dict(zustimmungsquote=_bruchteile(quote),grenzquote=_bruchteile(grenze),vergleich='mehr_als' if streng else 'mindestens',mehrheitsgrenze_erreicht=quote>grenze if streng else quote>=grenze)
    ergebnis=_ergebnis(wert,'anteile_und_wahrheitswert','BGB_STIMMGEWICHTS_MEHRHEITSGRENZE',eingaben,[dict(operation='Zustimmendes Gewicht durch passenden Gesamtnenner teilen; mindestens drei Viertel beziehungsweise strikt mehr als die Hälfte vergleichen.')],eingaben.copy())
    ergebnis['hinweise']=['§732/734II: nur bei gesellschaftsvertraglicher Mehrheitsentscheidung; Nenner sind rechtlich maßgebliche abgegebene Stimmen, Stimmgewicht und Behandlung von Enthaltungen/Ungültigkeit vorqualifizieren. §745I: Mehrheit nach Größe sämtlicher maßgeblicher Gemeinschaftsanteile, nicht bloß nach Kopfzahl oder abgegebenen Stimmen; Nenner umfasst die gesamte Anteilsbasis. Keine automatische Beschlusswirksamkeit, Quorums-, Kompetenz- oder Vertragsprüfung.736V und736dI enthalten keine pauschale Dreiviertelregel und sind hier nicht einbezogen. Gleichheit genügt bei drei Vierteln, nicht bei der Hälfte.']
    return ergebnis


def gesellschaft_zustimmungsanzahl(erforderliche_personenzahl=None, zustimmende_personenzahl=None, einordnungsnachweis=None):
    """Zahl noch fehlender Zustimmungen in einem rechtlich qualifizierten vollständigen Personenkreis bestimmen."""
    erforderlich=_ganzzahl(erforderliche_personenzahl,'erforderliche_personenzahl',1,9007199254740991);zugestimmt=_ganzzahl(zustimmende_personenzahl,'zustimmende_personenzahl',0,9007199254740991)
    if zugestimmt>erforderlich:_fehler('zustimmende_personenzahl','Zustimmungen müssen aus demselben erforderlichen Personenkreis stammen.')
    _text(einordnungsnachweis,'einordnungsnachweis')
    eingaben=dict(erforderliche_personenzahl=erforderliche_personenzahl,zustimmende_personenzahl=zustimmende_personenzahl,einordnungsnachweis=einordnungsnachweis)
    wert=dict(fehlende_zustimmungen=erforderlich-zugestimmt,alle_erforderlichen_zustimmungen_erfasst=zugestimmt==erforderlich)
    ergebnis=_ergebnis(wert,'anzahl_und_wahrheitswert','BGB_GESELLSCHAFT_ZUSTIMMUNGSANZAHL',eingaben,[dict(operation='Erforderliche verschiedene Personen abzüglich bereits wirksam zustimmender verschiedener Personen desselben Kreises zählen.')],eingaben.copy())
    ergebnis['hinweise']=['Numerischer Vollständigkeitsvergleich714/715II beziehungsweise gemeinsam erforderlicher Mitwirkung720I. Personenkreis, Stimmberechtigung, Stimmverbote, wirksame Zustimmung/Mitwirkung und abweichender Gesellschaftsvertrag vorqualifizieren. Jede Person nur einmal zählen, Zustimmungen fremder Personen nicht hinzufügen. Bei714 alle Stimmberechtigten, nicht lediglich abgegebene Stimmen als Nenner. Ergebnis begründet allein weder einen wirksamen Beschluss noch eine wirksame Gesamtvertretung; für736V/736dI besondere Beteiligtenkreise nicht ungeprüft übernehmen.']
    return ergebnis
