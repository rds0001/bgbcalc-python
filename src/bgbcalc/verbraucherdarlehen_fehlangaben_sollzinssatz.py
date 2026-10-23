from .kalender import _ergebnis, _text
from .zahlen import _bruch, _zahleneingabe
from .zinsen import _bruchteile

def verbraucherdarlehen_fehlangaben_sollzinssatz(vertraglicher_sollzinssatz=None, fehlangabennachweis=None):
    """Vertraglichen Jahreszinssatz auf höchstens den gesetzlichen Satz von vier Prozent vermindern."""
    s=_zahleneingabe(vertraglicher_sollzinssatz);_text(fehlangabennachweis,'fehlangabennachweis');wert=_bruchteile(min(s,_bruch(1,25)))
    eingaben = dict(vertraglicher_sollzinssatz=vertraglicher_sollzinssatz, fehlangabennachweis=fehlangabennachweis)
    ergebnis = _ergebnis(wert,'Jahresquote','BGB_VERBRAUCHERDARLEHEN_FEHLANGABEN_SOLLZINSSATZ',eingaben,[dict(operation='Vertraglichen Jahreszinssatz auf höchstens den gesetzlichen Satz von vier Prozent vermindern.')],eingaben.copy())
    ergebnis["hinweise"] = ['494II in Verbindung mit246: Jahresquote auf höchstens0.04 vermindern. Bereits niedrigerer oder negativer vertraglicher Satz wird nicht erhöht. Ergebnis ist nur die Zinsbasis; keine automatische Zahlungspflicht bei negativem Satz. Tatsächliche Zinsbeträge/Teilzahlungen anhand der rechtlich fortbestehenden Vertragsstruktur berechnen. Nicht mit der Differenzkorrektur bei zu niedrig angegebenem Effektivzins494III verwechseln.']
    return ergebnis

