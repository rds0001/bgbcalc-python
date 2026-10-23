from .betraege import _geld, _wahrheitswert
from .betreuungsrechnung import _rechnungssumme
from .kalender import _ergebnis, _fehler, _text, _vorhanden
from .zahlen import _addieren, _bruch, _subtrahieren
from .zinsen import _bruchteile


def buergschaft_schuldkomponenten(schuldpositionen=None, einordnungsnachweis=None):
    """Qualifizierte Schuldkomponenten summieren; spätere rechtsgeschäftliche Erweiterungen getrennt ausschließen."""
    _vorhanden(schuldpositionen,'schuldpositionen')
    if not isinstance(schuldpositionen,list) or not 1<=len(schuldpositionen)<=1000:
        _fehler('schuldpositionen','Liste mit1bis1000 eindeutig zugeordneten Schuldpositionen erforderlich.')
    _text(einordnungsnachweis,'einordnungsnachweis');namen=set();einbezogen=_bruch(0);ausgeschlossen=_bruch(0)
    for position in schuldpositionen:
        if not isinstance(position,dict) or set(position)!={'positions_id','betrag','spaetere_rechtsgeschaeftliche_erweiterung'}:
            _fehler('schuldpositionen','Genau positions_id, betrag und spaetere_rechtsgeschaeftliche_erweiterung erforderlich.')
        name=_text(position['positions_id'],'positions_id')
        if name in namen:
            _fehler('positions_id','Schuldposition darf nicht mehrfach erfasst werden.')
        namen.add(name);betrag=_geld(position['betrag']);_wahrheitswert(position['spaetere_rechtsgeschaeftliche_erweiterung'],'spaetere_rechtsgeschaeftliche_erweiterung')
        if not position['spaetere_rechtsgeschaeftliche_erweiterung']:einbezogen=_addieren(einbezogen,betrag)
        else:ausgeschlossen=_addieren(ausgeschlossen,betrag)
    eingaben=dict(schuldpositionen=schuldpositionen,einordnungsnachweis=einordnungsnachweis)
    ergebnis=_ergebnis(dict(schuldumfang_nach_767=_bruchteile(einbezogen),ausgeschlossene_erweiterungen=_bruchteile(ausgeschlossen)),'EUR','BGB_BUERGSCHAFT_SCHULDKOMPONENTEN',eingaben,[dict(operation='Qualifizierte Schuldkomponenten summieren; spätere rechtsgeschäftliche Erweiterungen getrennt ausschließen.')],eingaben.copy())
    ergebnis['hinweise']=['§767I/II: qualifizierter gegenwärtiger Hauptschuldbestand einschließlich zurechenbarer Verschuldens-/Verzugsfolgen und vom Hauptschuldner zu ersetzender Kündigungs-/Rechtsverfolgungskosten. Jede Komponente nur einmal erfassen. Durch ein nach Übernahme der Bürgschaft vorgenommenes Rechtsgeschäft des Hauptschuldners bewirkte Erweiterungen gesondert ausschließen; nur den Erweiterungsanteil als eigene Position kennzeichnen, nicht die unveränderte gesamte Hauptschuld. Ursache, Zeitpunkt, wirksame Bürgschaft und Zuordnung extern qualifizieren. Vertragliche Höchstbeträge, weitere Haftungsgrenzen, Einreden768/770, Mitbürgen769 und bereits geleistete Zahlungen gesondert berücksichtigen. Numerischer Umfang nach767, kein abschließender durchsetzbarer Zahlungsanspruch. Keine Positionen ausdrücklich als einzelne Nullposition eingeben.']
    return ergebnis


