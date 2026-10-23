from .kalender import _ergebnis, _fehler, _text, _vorhanden
from .betraege import _geld, _wahrheitswert
from .zahlen import _bruch, _addieren, _subtrahieren
from .zinsen import _bruchteile

def mietpreisbegrenzung_vormiete_bereinigen(letzte_geschuldete_monatsmiete=None, minderungsbetrag=None, auszunehmende_erhoehungsbetraege=None, bereinigungsnachweis=None):
    """Minderungsbetrag hinzurechnen, ausgeschlossene Erhöhungsanteile summieren und abziehen."""
    _text(bereinigungsnachweis,'bereinigungsnachweis');_vorhanden(auszunehmende_erhoehungsbetraege,'auszunehmende_erhoehungsbetraege')
    if not isinstance(auszunehmende_erhoehungsbetraege,list) or len(auszunehmende_erhoehungsbetraege)>1000: _fehler('auszunehmende_erhoehungsbetraege','Liste mit höchstens1000Beträgen erforderlich.')
    u=_addieren(_geld(letzte_geschuldete_monatsmiete),_geld(minderungsbetrag));s=_bruch(0)
    for v in auszunehmende_erhoehungsbetraege:s=_addieren(s,_geld(v))
    if s>u:_fehler('auszunehmende_erhoehungsbetraege','Erhöhungsanteile übersteigen ungeminderte Miete.')
    wert=dict(ungeminderte_monatsmiete=_bruchteile(u),ausgeschlossene_erhoehungssumme=_bruchteile(s),bereinigte_vormiete=_bruchteile(_subtrahieren(u,s)))
    eingaben = dict(letzte_geschuldete_monatsmiete=letzte_geschuldete_monatsmiete, minderungsbetrag=minderungsbetrag, auszunehmende_erhoehungsbetraege=auszunehmende_erhoehungsbetraege, bereinigungsnachweis=bereinigungsnachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_MIETPREISBEGRENZUNG_VORMIETE_BEREINIGEN',eingaben,[dict(operation='Minderungsbetrag hinzurechnen, ausgeschlossene Erhöhungsanteile summieren und abziehen.')],eingaben.copy())
    ergebnis["hinweise"] = ['556eI2: zunächst Minderung aus letzter geschuldeter Monatsmiete herausrechnen, dann Summe der rechtlich ausgeschlossenen Erhöhungsanteile abziehen. Das Ergebnis ist Eingabe für vorhandenen Vormietgrenzenkern. Erhöhungsanteile nach tatsächlicher Wirkung in der ungeminderten letzten Miete bestimmen; verkettete Prozentänderungen oder später aufgehobene Erhöhungen nicht doppelt zählen. Rechtswirksamkeit, zeitliche Einordnung ins letzte Jahr, Staffel-/Indexsonderfälle und Nutzbarkeit nach556g sind vorqualifiziert. Keine automatische Vertragszeitreihenbewertung. Abzüge oberhalb ungeminderter Miete sind widersprüchliche Eingaben und werden nicht still auf null gekappt.']
    return ergebnis

def mietpreisbegrenzung_modernisierungsalternative(grund_oder_vormietgrenze=None, grundbetrag_ohne_modernisierung=None, modernisierung_monatlich=None, modernisierungsprivileg_nutzbar=None, einordnungsnachweis=None):
    """Eigenständigen Modernisierungsweg berechnen und bei rechtlicher Nutzbarkeit mit bisheriger Monatsgrenze vergleichen."""
    g=_geld(grund_oder_vormietgrenze);a=_geld(grundbetrag_ohne_modernisierung);m=_geld(modernisierung_monatlich);ja=_wahrheitswert(modernisierungsprivileg_nutzbar,'modernisierungsprivileg_nutzbar');_text(einordnungsnachweis,'einordnungsnachweis')
    alternative=_addieren(a,m) if ja else None
    wert=dict(modernisierungsweg_monatsgrenze=None if alternative is None else _bruchteile(alternative),nutzbare_monatsgrenze=_bruchteile(max(g,alternative) if ja else g))
    eingaben = dict(grund_oder_vormietgrenze=grund_oder_vormietgrenze, grundbetrag_ohne_modernisierung=grundbetrag_ohne_modernisierung, modernisierung_monatlich=modernisierung_monatlich, modernisierungsprivileg_nutzbar=modernisierungsprivileg_nutzbar, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_MIETPREISBEGRENZUNG_MODERNISIERUNGSALTERNATIVE',eingaben,[dict(operation='Eigenständigen Modernisierungsweg berechnen und bei rechtlicher Nutzbarkeit mit bisheriger Monatsgrenze vergleichen.')],eingaben.copy())
    ergebnis["hinweise"] = ['556eII-Alternativweg: Grundbetrag auf unmodernisierter Vergleichsmiete plus hypothetischer559/559a-Erhöhung; anschließend höherer nutzbarer Betrag gegenüber eigenständigem Grund-/Vormietweg. Niemals Modernisierungszuschlag zusätzlich auf die Vormiete aufschlagen. Bei nicht nutzbarem Privileg bleibt nur bisheriger Weg; hypothetischer Alternativbetrag wird dann nicht ausgegeben. Keine doppelte Einbeziehung der Modernisierung in Vergleichsmiete und Zuschlag. Zeitliche Dreijahreszuordnung, Maßnahmenqualifikation und556g-Auskunft sind rechtliche Eingaben. Die rechtliche Förderabzugs-/Kappungsreihenfolge bleibt bei einschlägiger Konkurrenz ausdrücklich vorzugeben; kein neuer Standard dafür.']
    return ergebnis

