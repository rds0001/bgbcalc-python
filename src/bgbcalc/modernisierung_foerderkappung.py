from .kalender import _auswahl, _ergebnis, _text
from .betraege import _geld
from .zahlen import _bruch, _addieren, _subtrahieren, _multiplizieren, _dividieren
from .zinsen import _bruchteile

def modernisierung_kappung_mit_laufenden_abzuegen(jahresbetrag_vor_laufenden_abzuegen=None, jaehrliche_zinsermaessigung=None, jaehrliche_laufende_zuschuesse_und_darlehen=None, monatliche_restkappung=None, abzugsreihenfolge=None, methodennachweis=None):
    """Beide arithmetischen Reihenfolgen jährlicher Förderabzüge und monatlicher Kappung berechnen; Ergebnis nur gemäß ausdrücklich rechtlich vorgegebener Methode auswählen."""
    jahr=_geld(jahresbetrag_vor_laufenden_abzuegen);zins=_geld(jaehrliche_zinsermaessigung);laufend=_geld(jaehrliche_laufende_zuschuesse_und_darlehen);kap=_geld(monatliche_restkappung)
    _auswahl(abzugsreihenfolge,'abzugsreihenfolge',('abzug_vor_kappung','abzug_nach_kappung'));_text(methodennachweis,'methodennachweis')
    abzug=_addieren(zins,laufend);zwischensaldo=_subtrahieren(jahr,abzug)
    vor=min(_dividieren(max(zwischensaldo,_bruch(0)),_bruch(12)),kap)
    nach=max(_subtrahieren(min(_dividieren(jahr,_bruch(12)),kap),_dividieren(abzug,_bruch(12))),_bruch(0))
    monat=vor if abzugsreihenfolge=='abzug_vor_kappung' else nach
    wert=dict(jaehrliche_laufende_abzuege=_bruchteile(abzug),monatsbetrag_abzug_vor_kappung=_bruchteile(vor),monatsbetrag_abzug_nach_kappung=_bruchteile(nach),monatlicher_betrag_nach_vorgegebener_methode=_bruchteile(monat),jaehrlicher_betrag_nach_vorgegebener_methode=_bruchteile(_multiplizieren(monat,_bruch(12))),rechenweg=abzugsreihenfolge)
    eingaben = dict(jahresbetrag_vor_laufenden_abzuegen=jahresbetrag_vor_laufenden_abzuegen, jaehrliche_zinsermaessigung=jaehrliche_zinsermaessigung, jaehrliche_laufende_zuschuesse_und_darlehen=jaehrliche_laufende_zuschuesse_und_darlehen, monatliche_restkappung=monatliche_restkappung, abzugsreihenfolge=abzugsreihenfolge, methodennachweis=methodennachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_MODERNISIERUNG_KAPPUNG_MIT_LAUFENDEN_ABZUEGEN',eingaben,[dict(operation='Beide arithmetischen Reihenfolgen jährlicher Förderabzüge und monatlicher Kappung berechnen; Ergebnis nur gemäß ausdrücklich rechtlich vorgegebener Methode auswählen.')],eingaben.copy())
    ergebnis["hinweise"] = ['Bedingte Zahlenrechnung für das Zusammenwirken von§559IIIa und§559aII. Die allgemeine rechtliche Reihenfolge laufender Förderabzüge gegenüber der Kappung ist in der Quellenarbeit nicht abschließend geklärt; diese Funktion entscheidet sie ausdrücklich nicht. Beide vollständigen Rechenwege werden ausgewiesen, der ausgewählte nur gemäß zwingender begründeter Nutzervorgabe. Vor Kappung: min(max(Jahresbetrag-Abzüge,0)/12,Restkappung). Nach Kappung: max(min(Jahresbetrag/12,Restkappung)-Abzüge/12,0). Null begrenzt nur den hier berechneten positiven Erhöhungsbetrag; keine automatische Senkung bisheriger Miete, Förderungsauszahlung oder Rückforderung. Kostenbasis, zulässige Förderpositionen, Einzelwohnungszuordnung, Härte und Wirksamkeit separat. Keine erneute Anrechnung einmaliger Kostenbeiträge oder früherer Mieterhöhungen.']
    return ergebnis

