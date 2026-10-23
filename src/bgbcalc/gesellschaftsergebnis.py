from .gesellschaftsgrundquoten import gesellschaft_gewinn_verlust_stimmquoten
from .zahlen import _zahleneingabe, _multiplizieren
from .zinsen import _bruchteile
from .kalender import _ergebnis

def gesellschaft_gewinn_verlust_betraege(gesellschaftsergebnis=None, gesellschafter=None, quotenbasis=None, einordnungsnachweis=None):
    """Vorhandenen709-Quotenkern anwenden; vorzeichenbehaftetes festgestelltes Gesellschaftsergebnis mit jeder Quote exakt multiplizieren."""
    gesamt = _zahleneingabe(gesellschaftsergebnis)
    quoten = gesellschaft_gewinn_verlust_stimmquoten(gesellschafter,quotenbasis,einordnungsnachweis)['wert']
    wert = [dict(gesellschafter_id=person['gesellschafter_id'],quote=person['quote'],ergebnisanteil=_bruchteile(_multiplizieren(gesamt,_zahleneingabe(person['quote'])))) for person in quoten]
    eingaben = dict(gesellschaftsergebnis=gesellschaftsergebnis, gesellschafter=gesellschafter, quotenbasis=quotenbasis, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,"EUR",'BGB_GESELLSCHAFT_GEWINN_VERLUST_BETRAEGE',eingaben,[dict(operation='Vorhandenen709-Quotenkern anwenden; vorzeichenbehaftetes festgestelltes Gesellschaftsergebnis mit jeder Quote exakt multiplizieren.')],eingaben.copy())
    ergebnis["hinweise"] = ['§§709III/718: festgestelltes Gesellschaftsergebnis mit rechtlich ausgewählter Gewinn-/Verlustquote verteilen. Beteiligungsverhältnisse haben Vorrang vor vereinbarten Beitragswerten, sonst gleiche Anteile. Individuelle abweichende Gewinn-/Verlustvereinbarungen und wechselnder Gesellschafterbestand gesondert. Rechnerische Ergebnisanteile sind nicht automatisch fällige Ausschüttungen oder sofortige Nachschusspflichten; keine Vermischung mit Liquidation oder Ausscheiden. Im Zweifel Rechnungsabschluss und Gewinnverteilung zum Kalenderjahresende718; abweichende Vereinbarung vorqualifizieren. Keine Rundung, kein Restcentverfahren.']
    return ergebnis
