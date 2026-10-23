from .kalender import _ergebnis, _auswahl, _text, _fehler
from .betraege import _geld
from .zahlen import _bruch, _subtrahieren, _multiplizieren
from .zinsen import _bruchteile
from .modernisierungsvereinfachung import modernisierung_vereinfachte_kostenbasis

def modernisierung_vereinfachte_foerderkostenbasis(geltend_gemachte_kosten=None, frueher_geltend_gemachte_kosten=None, abzuziehende_kapitalzuschuesse=None, pauschalenmethode=None, methodennachweis=None):
    """559c-Kostengrenze prüfen, Kapitalbeitrag und30%-Pauschale in ausdrücklich gewählter Reihenfolge abziehen; beide bedingten Rechenwege ausweisen."""
    k=_geld(geltend_gemachte_kosten);z=_geld(abzuziehende_kapitalzuschuesse);_text(methodennachweis,'methodennachweis');_auswahl(pauschalenmethode,'pauschalenmethode',('pauschale_vor_kapitalabzug','kapitalabzug_vor_pauschale'))
    b=modernisierung_vereinfachte_kostenbasis(geltend_gemachte_kosten,frueher_geltend_gemachte_kosten,True)
    if b['wert'] is None:_fehler('geltend_gemachte_kosten','Verbleibende559c-Kostengrenze überschritten.')
    if z>k:_fehler('abzuziehende_kapitalzuschuesse','Kapitalbeitrag höchstens Kosten.')
    vor=max(_subtrahieren(_multiplizieren(k,_bruch(7,10)),z),_bruch(0));nach=_multiplizieren(_subtrahieren(k,z),_bruch(7,10))
    wert=dict(kostenbasis_pauschale_vor_kapitalabzug=_bruchteile(vor),kostenbasis_kapitalabzug_vor_pauschale=_bruchteile(nach),ausgewaehlte_kostenbasis=_bruchteile(vor if pauschalenmethode=='pauschale_vor_kapitalabzug' else nach),pauschalenmethode=pauschalenmethode)
    eingaben = dict(geltend_gemachte_kosten=geltend_gemachte_kosten, frueher_geltend_gemachte_kosten=frueher_geltend_gemachte_kosten, abzuziehende_kapitalzuschuesse=abzuziehende_kapitalzuschuesse, pauschalenmethode=pauschalenmethode, methodennachweis=methodennachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_MODERNISIERUNG_VEREINFACHTE_FOERDERKOSTENBASIS',eingaben,[dict(operation='559c-Kostengrenze prüfen, Kapitalbeitrag und30%-Pauschale in ausdrücklich gewählter Reihenfolge abziehen; beide bedingten Rechenwege ausweisen.')],eingaben.copy())
    ergebnis["hinweise"] = ['Bedingte559c/559aI-Kostenrechnung mit zwingend begründeter Reihenfolge, ohne universelle rechtliche Festlegung. Kostengrenze10000abzüglich relevanter früherer Kosten vor dieser Rechnung mit vorhandenem Kern prüfen. Pauschale_vor_kapitalabzug: max(0,0.7K-Z). Kapitalabzug_vor_pauschale:0.7(K-Z). Beide Ergebnisse ausweisen, ausgewählte Kostenbasis für8%-Umlage verwenden. Nicht den Darlehensnennbetrag als Kapitalzuschuss abziehen.559cI3schließt559aII1bis3(Zinsermäßigung)aus, nicht559aII4(laufende Zuschüsse/Darlehen); letztere nach jährlicher8%-Umlage und rechtlich bestimmter Kappungsreihenfolge mit vorhandenem Förderkappungskern berücksichtigen. Keine tatsächlichen Erhaltungskosten neben30%-Pauschale. Förderzuordnung zu Wohnungen und Erklärungs-/Härtevoraussetzungen separat; keine Förderung automatisch erfinden.']
    return ergebnis

