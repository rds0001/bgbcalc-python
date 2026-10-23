"""Einzelanteil aus Gemeinschaftsaufhebung nach gemeinsamen und individuellen Schulden."""
from .betraege import _geld
from .kalender import _text, _fehler, _ergebnis
from .zahlen import _bruch, _subtrahieren, _multiplizieren
from .zinsen import _bruchteile


def gemeinschaft_aufhebungsanteil(gemeinschaftlicher_erloes=None, zu_berichtigende_gemeinsame_schulden=None, teilhaberquote=None, gemeinschaftsbezogene_teilhaberschuld=None, einordnungsnachweis=None):
    """Gemeinsame Schuld vor Quote, gemeinschaftsbezogene Teilhaberschuld aus verfügbarem Einzelanteil berichtigen."""
    erloes,gemeinsam,quote,eigen=[_geld(x) for x in (gemeinschaftlicher_erloes,zu_berichtigende_gemeinsame_schulden,teilhaberquote,gemeinschaftsbezogene_teilhaberschuld)]
    _text(einordnungsnachweis,'einordnungsnachweis')
    if quote>1:
        _fehler('teilhaberquote','Teilhaberquote darf eins nicht übersteigen.')
    masse=max(_subtrahieren(erloes,gemeinsam),_bruch(0)); anteil=_multiplizieren(masse,quote); berichtigung=min(anteil,eigen)
    wert=dict(verteilbare_erloesmasse=_bruchteile(masse),anteil_vor_teilhaberschuld=_bruchteile(anteil),berichtigungsbetrag_teilhaberschuld=_bruchteile(berichtigung),verbleibender_einzelanteil=_bruchteile(_subtrahieren(anteil,berichtigung)),ungedeckte_teilhaberschuld=_bruchteile(_subtrahieren(eigen,berichtigung)),ungedeckte_gemeinsame_schuld=_bruchteile(max(_subtrahieren(gemeinsam,erloes),_bruch(0))))
    eingaben=dict(gemeinschaftlicher_erloes=gemeinschaftlicher_erloes,zu_berichtigende_gemeinsame_schulden=zu_berichtigende_gemeinsame_schulden,teilhaberquote=teilhaberquote,gemeinschaftsbezogene_teilhaberschuld=gemeinschaftsbezogene_teilhaberschuld,einordnungsnachweis=einordnungsnachweis)
    ergebnis=_ergebnis(wert,'EUR','BGB_GEMEINSCHAFT_AUFHEBUNGSANTEIL',eingaben,[dict(operation='Positive Erlösmasse nach gemeinsamen Schulden mit Quote multiplizieren; qualifizierte Teilhaberschuld höchstens bis zu diesem Anteil berichtigen.')],eingaben.copy())
    ergebnis['hinweise']=['Nur §§753/755/756 bei rechtlich qualifizierter Erlösaufteilung. Gemeinsame Schuld muss §755 erfüllen und ihre Berichtigung verlangt sein; individuelle Schuld muss gemeinschaftsbezogener Anspruch eines anderen Teilhabers nach §756 sein und ihre Berichtigung verlangt sein. Beträge auf gleiche Abrechnung beziehen, keine Doppelzählung bereits abgezogener Kosten/Schulden. Einzelanteil des Schuldner-Teilhabers; Berichtigungsbetrag ist dem qualifizierten Gläubiger zusätzlich zu dessen eigenem Erlösanteil zuzuordnen. Mehrere konkurrierende Forderungen, wechselseitige Forderungsnetze und Vorränge zuvor rechtlich bestimmen, nicht unbesehen saldieren. Ungedeckte gemeinsame Schuld ist Gesamtrest, keine automatische persönliche Quote. Keine Wertbewertung, Naturteilung/Losentscheidung oder zusätzliche Haftungsentscheidung.']
    return ergebnis
