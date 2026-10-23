from .teilverguetung import _teilbetrag
from .betraege import _geld_ergebnis
from .kalender import _text, _auswahl

def vorenthaltung_abschnittsentschaedigung(regelfall=None, abschnittsentgelt=None, zeitanteil_zaehler=None, zeitanteil_nenner=None, einordnungsnachweis=None):
    """Gewähltes Miet- oder Landpachtentgelt des Abrechnungsabschnitts mit dem qualifizierten Vorenthaltungszeitanteil multiplizieren."""
    _auswahl(regelfall,"regelfall",("miete_vertrag","miete_ortsueblich","landpacht_vertrag"))
    anteilig = _teilbetrag(abschnittsentgelt, zeitanteil_zaehler, zeitanteil_nenner)
    _text(einordnungsnachweis,"einordnungsnachweis")
    eingaben = dict(regelfall=regelfall, abschnittsentgelt=abschnittsentgelt, zeitanteil_zaehler=zeitanteil_zaehler, zeitanteil_nenner=zeitanteil_nenner, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(anteilig,'BGB_VORENTHALTUNG_ABSCHNITTSENTSCHAEDIGUNG',eingaben,[dict(operation='Gewähltes Miet- oder Landpachtentgelt des Abrechnungsabschnitts mit dem qualifizierten Vorenthaltungszeitanteil multiplizieren.')])
    ergebnis["hinweise"].append('§546aI: vereinbarte Miete ODER qualifizierte ortsübliche Miete vergleichbarer Sachen; Alternativen nicht addieren. §597: vereinbarte Landpacht für die Vorenthaltungsdauer, keine ungeprüfte Übertragung der Berechnungsweise584b. Nur ein homogener Abschnitt und dessen zutreffend bestimmter Zeitanteil; für mehrere Abschnitte disjunkte Ergebnisse addieren. Weitere ersatzfähige Schäden546aII/597Satz2 ohne Doppelzählung gesondert, ebenso geleistete Zahlungen. Keine automatische Entschädigung bloß wegen eines behaupteten Rückgabeverzugs; rechtliche Vorenthaltung und sonstige Voraussetzungen vorqualifiziert.')
    return ergebnis
