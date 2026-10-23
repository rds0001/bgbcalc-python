"""Preisabrechnung bei ausgeübtem dinglichem Vorkaufsrecht (§§1100–1102)."""
from .betraege import _geld, _wahrheitswert
from .kalender import _ergebnis, _fehler, _text
from .zahlen import _subtrahieren
from .zinsen import _bruchteile


def dinglicher_vorkauf_preisabrechnung(vereinbarter_kaufpreis=None, bereits_berichtigter_kaufpreis=None,
        anwendungsfall_qualifiziert=None, bewertungsnachweis=None):
    """Berichtigten Kaufpreis erstatten und denselben Betrag beim Vorkaufpreis abziehen."""
    preis = _geld(vereinbarter_kaufpreis)
    berichtigt = _geld(bereits_berichtigter_kaufpreis)
    if berichtigt > preis:
        _fehler('bereits_berichtigter_kaufpreis', 'Berichtigter Kaufpreis darf vereinbarten Kaufpreis nicht übersteigen.')
    _wahrheitswert(anwendungsfall_qualifiziert, 'anwendungsfall_qualifiziert')
    _text(bewertungsnachweis, 'bewertungsnachweis')
    rest = _subtrahieren(preis, berichtigt)
    eingaben = dict(vereinbarter_kaufpreis=vereinbarter_kaufpreis, bereits_berichtigter_kaufpreis=bereits_berichtigter_kaufpreis,
        anwendungsfall_qualifiziert=anwendungsfall_qualifiziert, bewertungsnachweis=bewertungsnachweis)
    wert = dict(erstattung_an_kaeufer=_bruchteile(berichtigt), verbleibender_vorkaufpreis_an_verpflichteten=_bruchteile(rest),
        befreiung_urspruenglicher_kaeufer=_bruchteile(rest)) if anwendungsfall_qualifiziert else None
    ergebnis = _ergebnis(wert, 'EUR', 'BGB_DINGLICHER_VORKAUF_PREISABRECHNUNG', eingaben,
        [dict(operation='Bereits berichtigten Kaufpreis als Erstattung ausweisen; denselben Betrag vom Vorkaufpreis abziehen; ursprünglichen Käufer von unberichtigtem Rest befreien')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if anwendungsfall_qualifiziert else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Qualifizierter dinglicher Vorkaufsfall mit identischem maßgeblichem Kaufpreis und Eigentumsverlust des ursprünglichen Käufers; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['Nur miteinander korrespondierende Preisbeträge nach1100–1102. Neuer Eigentümer ist Käufer oder dessen Rechtsnachfolger, Erstattungsvoraussetzungen und Herausgabezug um Zug sind vorqualifiziert. Der ursprüngliche Käufer wird nur vom noch nicht berichtigten Kaufpreis frei; bereits gezahlten Preis erhält er nach1100 vom Vorkaufsberechtigten, nicht nochmals nach1102 vom Verkäufer. Unberichtigter Rest ist zugleich verbleibender Vorkaufpreis an den Verpflichteten. Abweichende Preisgrundlagen, Überzahlungen, Erfüllung mehrerer Preisforderungen und sonstige Ansprüche nicht vermischen; keine automatische Eigentums-/Grundbuchentscheidung.']
    return ergebnis
