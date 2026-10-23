from .kalender import _ergebnis, _fehler, _text, _vorhanden
from .betraege import _geld
from .zahlen import _bruch, _addieren, _subtrahieren, _multiplizieren, _dividieren
from .zinsen import _bruchteile

def fortsetzung_nichtgemeinsame_abkoemmlinge_gesamtgut(teilungsfaehiges_gesamtgut=None, erbquoten_nichtgemeinsamer_abkoemmlinge=None, einordnungsnachweis=None):
    """Gesamtgut halbieren, nichtgemeinschaftliche Erbquoten auf Nachlasshälfte anwenden und Gesamtgutrest bestimmen."""
    gut=_geld(teilungsfaehiges_gesamtgut);_text(einordnungsnachweis,'einordnungsnachweis');_vorhanden(erbquoten_nichtgemeinsamer_abkoemmlinge,'erbquoten_nichtgemeinsamer_abkoemmlinge')
    if not isinstance(erbquoten_nichtgemeinsamer_abkoemmlinge,list) or len(erbquoten_nichtgemeinsamer_abkoemmlinge)>1000: _fehler('erbquoten_nichtgemeinsamer_abkoemmlinge','Liste0..1000 erforderlich.')
    haelfte=_dividieren(gut,_bruch(2));summe=_bruch(0);quotensumme=_bruch(0);namen=set();anteile=[]
    for p in erbquoten_nichtgemeinsamer_abkoemmlinge:
        if not isinstance(p,dict) or set(p)!={'abkoemmling_id','erbquote'}: _fehler('erbquoten_nichtgemeinsamer_abkoemmlinge','Genau Kennung und Erbquote erforderlich.')
        name=_text(p['abkoemmling_id'],'abkoemmling_id');quote=_geld(p['erbquote'])
        if name in namen: _fehler('abkoemmling_id','Eindeutige Personen erforderlich.')
        namen.add(name);quotensumme=_addieren(quotensumme,quote)
        if quotensumme>1: _fehler('erbquote','Summe der Erbquoten höchstens1.')
        betrag=_multiplizieren(haelfte,quote);summe=_addieren(summe,betrag)
        anteile.append(dict(abkoemmling_id=name,betrag=_bruchteile(betrag)))
    wert=dict(hypothetischer_nachlassanteil_gesamtgut=_bruchteile(haelfte),herauszurechnende_anteile=anteile,herauszurechnender_gesamtbetrag=_bruchteile(summe),verbleibendes_gesamtgut=_bruchteile(_subtrahieren(gut,summe)))
    eingaben = dict(teilungsfaehiges_gesamtgut=teilungsfaehiges_gesamtgut, erbquoten_nichtgemeinsamer_abkoemmlinge=erbquoten_nichtgemeinsamer_abkoemmlinge, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_FORTSETZUNG_NICHTGEMEINSAME_ABKOEMMLINGE_GESAMTGUT',eingaben,[dict(operation='Gesamtgut halbieren, nichtgemeinschaftliche Erbquoten auf Nachlasshälfte anwenden und Gesamtgutrest bestimmen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§1483II: ursprünglichen, bereits bereinigten Gesamtgutwert hälftig dem hypothetischen Nachlass zuordnen; Erbquoten der nichtgemeinschaftlichen Abkömmlinge auf diese Hälfte anwenden und aus dem Gesamtgut herausrechnen. Nur Gesamtgutkomponente ihrer Erbteile; Sondergut/Vorbehaltsgut und sonstige Nachlasspositionen gesondert. Keine automatische Güterstands-, Abstammungs-, Erbquoten- oder Bewertungsentscheidung. Keine erneute Schuldenberichtigung bereits bereinigter Werte, kein negativer Nachlass und keine pauschale Kappung tatsächlicher Außenhaftung. Abweichende ehevertragliche Teilungsverhältnisse nicht mit Halbteilung vermischen.']
    return ergebnis

