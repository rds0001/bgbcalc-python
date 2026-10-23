from .betraege import _geld
from .kalender import _auswahl, _ergebnis, _fehler, _text
from .zahlen import _bruch, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile

_FAELLE = {'wohnraum_zwei_aufeinanderfolgende_termine': (1, True, '§543II1Nr3a iVm569III1: Rückstand für genau zwei unmittelbar aufeinanderfolgende Termine bei Wohnraum, der nicht nur zum vorübergehenden Gebrauch vermietet ist; strikt mehr als eine maßgebliche Monatsmiete. Terminzusammenhang und Verzug vorqualifiziert. Für andere Mietarten keine erfundene feste Erheblichkeitsschwelle.'), 'miete_mehr_als_zwei_termine': (2, False, '§543II1Nr3b: qualifizierter Verzugsrückstand aus einem Zeitraum über mehr als zwei Termine; mindestens zwei Monatsmieten. Der mehr als zwei Termine umfassende Zeitraum ist eine zusätzlich vorqualifizierte Voraussetzung, keine bloße Anzahl unbezahlter Raten.'), 'wohnraum_sicherheitsleistung': (2, False, '§569IIa: qualifizierter Verzugsrückstand mit der Sicherheitsleistung551; mindestens zwei Monatsmieten OHNE als Pauschale oder Vorauszahlung ausgewiesene Betriebskosten. Nur fällige, geschuldete Sicherheitsleistung erfassen; Ratenrecht551II beachten, keine gesamte noch nicht fällige Kaution.')}

def miete_rueckstandsbetragsgrenze(regelfall=None, massgebliche_monatsmiete=None, qualifizierter_rueckstand=None, einordnungsnachweis=None):
    """Qualifizierten Verzugsrückstand mit einer beziehungsweise zwei Monatsmieten vergleichen; strikte und einschließlich geltende Grenzen unterscheiden."""
    _auswahl(regelfall,'regelfall',tuple(_FAELLE))
    miete = _geld(massgebliche_monatsmiete)
    rueckstand = _geld(qualifizierter_rueckstand)
    if miete <= 0:
        _fehler('massgebliche_monatsmiete','Positive Bezugsmonatsmiete erforderlich.')
    _text(einordnungsnachweis,'einordnungsnachweis')
    faktor, strikt, fallhinweis = _FAELLE[regelfall]
    grenze = _multiplizieren(miete,_bruch(faktor))
    wert = dict(betragsgrenze=_bruchteile(grenze),vergleichsoperator='>' if strikt else '>=',rueckstand_abzueglich_grenze=_bruchteile(_subtrahieren(rueckstand,grenze)),betragsvoraussetzung_erfuellt=rueckstand>grenze if strikt else rueckstand>=grenze)
    eingaben = dict(regelfall=regelfall, massgebliche_monatsmiete=massgebliche_monatsmiete, qualifizierter_rueckstand=qualifizierter_rueckstand, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,"EUR_und_wahrheitswert",'BGB_MIETE_RUECKSTANDSBETRAGSGRENZE',eingaben,[dict(operation='Qualifizierten Verzugsrückstand mit einer beziehungsweise zwei Monatsmieten vergleichen; strikte und einschließlich geltende Grenzen unterscheiden.')],eingaben.copy())
    ergebnis["hinweise"] = ['Nur betragsmäßige Teilgrenze, kein Kündigungsentscheid. Maßgebliche Monatsmiete und Rückstandsbestand zum Prüfzeitpunkt rechtlich bestimmen, insbesondere Mietminderung, Betriebskostenabgrenzung, Zahlungszuordnung und Mietänderungen. Verzug, Frist-/Terminzusammenhang, Anwendungsbereich und Wirksamkeit der Kündigung gesondert; vorherige Befriedigung, Aufrechnung und Schonfristheilung werden nicht aus dem Zahlenvergleich abgeleitet. Für die Kautionsgrenze Betriebskosten ausschließen; diese Nettobasis nicht pauschal auf Mietrückstände übertragen.',fallhinweis]
    return ergebnis
