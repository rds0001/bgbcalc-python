from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _text, _vorhanden

def gesellschaft_fuenfjahresgrundfrist(fristfall=None, ausscheiden_oder_erloeschen_am=None, glaeubigerkenntnis_am=None, registereintragung_am=None, kuerzere_gesellschaftsfrist_letzter_tag=None, einordnungsnachweis=None):
    """Frühere qualifizierte Gläubigerkenntnis oder Registereintragung bestimmen und fünfjährige Ereignisgrundfrist berechnen."""
    _auswahl(fristfall,'fristfall',('nachhaftung_728b','erloeschen_verjaehrung_739'))
    wirksam = _datum(ausscheiden_oder_erloeschen_am,'ausscheiden_oder_erloeschen_am')
    _text(einordnungsnachweis,'einordnungsnachweis')
    anlaesse = []
    for name,eingabe in [('glaeubigerkenntnis_am',glaeubigerkenntnis_am),('registereintragung_am',registereintragung_am)]:
        if eingabe is not None:
            datum = _datum(eingabe,name)
            if datum < wirksam:
                _fehler(name,'Beginnanlass nicht vor rechtlich wirksamem Ausscheiden/Erlöschen eingeben.')
            anlaesse.append(datum)
    if not anlaesse:
        _vorhanden(None,'glaeubigerkenntnis_am_oder_registereintragung_am')
    beginn = min(anlaesse)
    grundende = _frist(beginn.isoformat(),5,'jahre','ereignis')
    vergleich = None
    if kuerzere_gesellschaftsfrist_letzter_tag is not None:
        if fristfall != 'erloeschen_verjaehrung_739':
            _fehler('kuerzere_gesellschaftsfrist_letzter_tag','Zusatzvergleich nur739; bei728b ausdrücklich null.')
        vergleich = min(grundende,_datum(kuerzere_gesellschaftsfrist_letzter_tag,'kuerzere_gesellschaftsfrist_letzter_tag')).isoformat()
    wert = dict(massgeblicher_beginnanlass_am=beginn.isoformat(),rechnerisches_fuenfjahresende=grundende.isoformat(),ende_im_qualifizierten_kuerzeren_grundfall=vergleich)
    eingaben = dict(fristfall=fristfall, ausscheiden_oder_erloeschen_am=ausscheiden_oder_erloeschen_am, glaeubigerkenntnis_am=glaeubigerkenntnis_am, registereintragung_am=registereintragung_am, kuerzere_gesellschaftsfrist_letzter_tag=kuerzere_gesellschaftsfrist_letzter_tag, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'daten','BGB_GESELLSCHAFT_FUENFJAHRESGRUNDFRIST',eingaben,[dict(operation='Frühere qualifizierte Gläubigerkenntnis oder Registereintragung bestimmen und fünfjährige Ereignisgrundfrist berechnen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§728bI3 beziehungsweise739II: frühester feststehender Beginnanlass aus Gläubigerkenntnis und Registereintragung, danach fünf Kalenderjahre ohne Jahresendverschiebung. Ausscheiden oder Erlöschen allein ersetzt weder Kenntnis noch Eintragung. Vorherige bloße Kenntnis einer Absicht beziehungsweise unzutreffender Registereintrag sind nicht qualifiziert. Nur ungestörter Grundlauf:728b-Nachhaftung verlangt zusätzlich rechtzeitig fällige Altverbindlichkeit sowie Feststellung/Vollstreckung oder schriftliches Anerkenntnis; bei Schadensersatz muss Pflichtverletzung vor Ausscheiden liegen.728b-Verweise204/206/210/211/212II/III gesondert.739: Optionaler Minimumvergleich mit rechtlich bestimmtem Ende der kürzeren Gesellschaftsanspruchsfrist ausschließlich für den ungestörten Fünfjahresgrundlauf. Ohne Eingabe bleibt Vergleich null. Bei Hemmung/Neubeginn739III zuvor beide Laufzeiten gesondert korrigieren; ein Vergleich mit unberichtigter Grundfrist wäre dann unzulässig; Ergebnis keinesfalls als abschließende Haftungs-/Verjährungsgrenze verwenden. Kein automatischer Haftungsausschluss.']
    return ergebnis

