from .zinsen import _bruchteile
from .teilverguetung import _teilbetrag
from .kalender import _text, _ergebnis

def mieterbe_vorauszahlungsersparnis(vorausgezahlte_abschnittsmiete=None, nach_tod_zugeordneter_anteil_zaehler=None, nach_tod_zugeordneter_anteil_nenner=None, einordnungsnachweis=None):
    """Qualifizierte Vorauszahlung mit dem vollständig ersparten/erlangten Mietanteil nach dem Tod multiplizieren."""
    _text(einordnungsnachweis,'einordnungsnachweis')
    wert = _bruchteile(_teilbetrag(vorausgezahlte_abschnittsmiete,nach_tod_zugeordneter_anteil_zaehler,nach_tod_zugeordneter_anteil_nenner))
    eingaben = dict(vorausgezahlte_abschnittsmiete=vorausgezahlte_abschnittsmiete, nach_tod_zugeordneter_anteil_zaehler=nach_tod_zugeordneter_anteil_zaehler, nach_tod_zugeordneter_anteil_nenner=nach_tod_zugeordneter_anteil_nenner, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_MIETERBE_VORAUSZAHLUNGSERSPARNIS',eingaben,[dict(operation='Qualifizierte Vorauszahlung mit dem vollständig ersparten/erlangten Mietanteil nach dem Tod multiplizieren.')],eingaben.copy())
    ergebnis["hinweise"] = ['§563bII: rechnerischer Erstattungsbetrag gegenüber dem Erben für den qualifizierten Fall, dass die vorausbezahlte Miete im angegebenen Anteil den nach dem Tod liegenden Zeitraum betrifft und den eingetretenen/fortsetzenden Personen vollständig zugutekommt. Der Tod beendet das Mietverhältnis hier nicht. Keine automatische Anwendung der547-Rückforderung gegen den Vermieter. Zeitanteil, tatsächliche Ersparnis/Erlangtes und Zahlungszuordnung vorqualifizieren; bei abweichendem Vorteil ist diese Anteilsrechnung nicht ausreichend. Unterschiedlich bepreiste Abschnitte getrennt berechnen, keine pauschalen30Monatstage. Keine automatische Aufteilung unter mehreren Erben oder mehreren Eingetretenen; keine Addition von Ersparnis und Erlangtem für denselben Vorteil.']
    return ergebnis

