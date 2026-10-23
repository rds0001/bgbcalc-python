from .kalender import _auswahl, _ergebnis, _fehler, _text
from .betraege import _geld
from .zahlen import _bruch, _multiplizieren
from .zinsen import _bruchteile
from .modernisierungsvereinfachung import modernisierung_vereinfachte_kostenbasis
from .modernisierung import modernisierung_kappungsgrenze

def modernisierung_vereinfachter_foerderfreier_betrag(geltend_gemachte_kosten=None, frueher_geltend_gemachte_kosten=None, wohnflaeche=None, monatliche_miete_je_quadratmeter=None, bisherige_monatliche_erhoehung_gesamt=None, bisherige_monatliche_heizungserhoehung=None, erhoehungsart=None, einordnungsnachweis=None):
    """Förderfreie559c-Kostenbasis mit8%-Jahresumlage und einschlägiger monatlicher Restkappung kombinieren."""
    _text(einordnungsnachweis,'einordnungsnachweis');_auswahl(erhoehungsart,'erhoehungsart',('allgemein','heizung_559'))
    basis=modernisierung_vereinfachte_kostenbasis(geltend_gemachte_kosten,frueher_geltend_gemachte_kosten,True)
    if basis['wert'] is None: _fehler('geltend_gemachte_kosten','Verbleibende559c-Kostengrenze muss eingehalten sein.')
    kappung=modernisierung_kappungsgrenze(wohnflaeche,monatliche_miete_je_quadratmeter,bisherige_monatliche_erhoehung_gesamt,bisherige_monatliche_heizungserhoehung,erhoehungsart,True)
    jahr=_multiplizieren(_geld(basis['wert']['kostenbasis']),_bruch(2,25));monat=_multiplizieren(jahr,_bruch(1,12));grenze=_geld(kappung['wert']['massgebliche_restgrenze']);endbetrag=min(monat,grenze)
    wert=dict(erhaltungspauschale=basis['wert']['erhaltungspauschale'],kostenbasis=basis['wert']['kostenbasis'],jaehrlicher_betrag_vor_kappung=_bruchteile(jahr),monatlicher_betrag_vor_kappung=_bruchteile(monat),monatliche_restkappung=_bruchteile(grenze),monatlicher_betrag_nach_kappung=_bruchteile(endbetrag),jaehrlicher_betrag_nach_kappung=_bruchteile(_multiplizieren(endbetrag,_bruch(12))))
    eingaben = dict(geltend_gemachte_kosten=geltend_gemachte_kosten, frueher_geltend_gemachte_kosten=frueher_geltend_gemachte_kosten, wohnflaeche=wohnflaeche, monatliche_miete_je_quadratmeter=monatliche_miete_je_quadratmeter, bisherige_monatliche_erhoehung_gesamt=bisherige_monatliche_erhoehung_gesamt, bisherige_monatliche_heizungserhoehung=bisherige_monatliche_heizungserhoehung, erhoehungsart=erhoehungsart, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_MODERNISIERUNG_VEREINFACHTER_FOERDERFREIER_BETRAG',eingaben,[dict(operation='Förderfreie559c-Kostenbasis mit8%-Jahresumlage und einschlägiger monatlicher Restkappung kombinieren.')],eingaben.copy())
    ergebnis["hinweise"] = ['§559cI/II mit559I/IIIa: qualifizierte Kosten minus30%Erhaltungspauschale;8%jährliche Umlage, durch12zumMonat, anschließend einschlägige Restkappung. Nur förderfreier Grundfall ohne abzuziehende559a-Beiträge/laufende Zuschüsse; dadurch keine ungeklärte Reihenfolge laufender Förderabzüge gegenüber Kappung. Keine zusätzliche tatsächliche Erhaltungskostenkürzung neben30%Pauschale. Heizungsfall559 zusätzlich50Cent je Quadratmeter;559e nicht hier. Schonzeit, Auskunft/Erklärung559b, Sperre559cIV und gegebenenfalls verbleibende Härteprüfung559cI3 separat. Überschrittene Kostengrenze ist ungültige Eingabe für diesen vorqualifizierten vereinfachten Ablauf, keine automatische Umstellung auf Regelverfahren.']
    return ergebnis

