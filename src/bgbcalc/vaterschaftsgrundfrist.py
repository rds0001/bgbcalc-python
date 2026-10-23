"""Gesetzliche Beginn- und Mindestablaufkombinationen der Vaterschaftsanfechtung."""
from .kalender import _datum, _ergebnis, _fehler, _frist, _text, _tage_addieren


def vaterschaftsanfechtung_grundfrist(kenntnis_am=None, kind_geboren_am=None, fristfall=None, berechtigter_geboren_am=None, anerkennung_wirksam_am=None, fristbeginnnachweis=None):
    """§1600bI/II: Kenntnis, Geburt, Anerkennung und eigene Minderjährigen-Altersgrenzen kombinieren."""
    kenntnis = _datum(kenntnis_am,'kenntnis_am');geburt = _datum(kind_geboren_am,'kind_geboren_am')
    fall = _text(fristfall,'fristfall')
    if fall not in {'allgemein','minderjaehriger_selbst'}:
        _fehler('fristfall','allgemein oder minderjaehriger_selbst erforderlich.')
    _text(fristbeginnnachweis,'fristbeginnnachweis')
    ereignisse = [kenntnis,geburt]
    if anerkennung_wirksam_am is not None:
        ereignisse.append(_datum(anerkennung_wirksam_am,'anerkennung_wirksam_am'))
    ereignis = max(ereignisse)
    zweijahresende = _frist(ereignis.isoformat(),2,'jahre','ereignis')
    volljaehrigkeit = None; mindestende = None
    if fall == 'minderjaehriger_selbst':
        berechtigtengeburt = _datum(berechtigter_geboren_am,'berechtigter_geboren_am')
        if kenntnis < berechtigtengeburt:
            _fehler('kenntnis_am','Eigene Kenntnis kann nicht vor eigener Geburt liegen.')
        volljaehrigkeit = _tage_addieren(_frist(berechtigter_geboren_am,18,'jahre','tagesbeginn'),1)
        zweijahresende = max(zweijahresende,_frist(volljaehrigkeit.isoformat(),2,'jahre','tagesbeginn'))
        mindestende = _frist(berechtigter_geboren_am,21,'jahre','tagesbeginn')
    elif berechtigter_geboren_am is not None:
        _datum(berechtigter_geboren_am,'berechtigter_geboren_am')
        _fehler('berechtigter_geboren_am','Im allgemeinen Fristfall keine unberücksichtigte Altersangabe zulässig.')
    eingaben = dict(kenntnis_am=kenntnis_am,kind_geboren_am=kind_geboren_am,fristfall=fristfall,berechtigter_geboren_am=berechtigter_geboren_am,anerkennung_wirksam_am=anerkennung_wirksam_am,fristbeginnnachweis=fristbeginnnachweis)
    ende = max(zweijahresende,mindestende) if mindestende is not None else zweijahresende
    wert = dict(fruehestes_ereignisbezogenes_beginn_datum=ereignis.isoformat(),volljaehrigkeitsbeginn=None if volljaehrigkeit is None else volljaehrigkeit.isoformat(),zweijahresgrundfristende=zweijahresende.isoformat(),mindestablauf_vollendung_21=None if mindestende is None else mindestende.isoformat(),anfechtungsgrundfristende=ende.isoformat())
    ergebnis = _ergebnis(wert,'daten','BGB_VATERSCHAFTSANFECHTUNG_GRUNDFRIST',eingaben,[dict(operation='Spätestes Ereignis aus Kenntnis, Kindesgeburt und gegebenenfalls wirksamer Anerkennung für Zweijahresfrist wählen; bei eigener Minderjährigenanfechtung Volljährigkeit als Tagesbeginn und Vollendung21 als Mindestablauf berücksichtigen.')],eingaben.copy())
    ergebnis['hinweise'] = ['§1600bI/II der lokalen Fassung: ungestörte Grundfrist, keine abschließende Anfechtungszulässigkeit. allgemein setzt rechtlich qualifiziert voraus, dass die besondere eigene Minderjährigenfrist nicht eingreift. minderjaehriger_selbst erfasst die eigene Anfechtung nach Absatz2Sätze2/3; Kenntnis ist eigene Kenntnis, nicht Vertreterkenntnis. Die Auswahl ersetzt keine Prüfung der gesetzlichen Fallvoraussetzungen. anerkennung_wirksam_am nur bei maßgeblicher Anerkennung; bei anderweitiger Vaterschaftszuordnung null. Kindesgeburt und Kenntnis können vor Wirksamkeit der Anerkennung liegen. Altersgrenzen nach§187II2 ab Tagesbeginn: Ablauf am Vortag des21.Geburtstags bedeutet Vollendung21 mit Ablauf dieses Tages, nicht einen Tag früher. Geburtsdaten/Wirksamkeitszeitpunkte rechtlich qualifiziert. Vertreteranfechtung Minderjähriger, Wiederanfechtung nach Geschäftsunfähigkeit(Absatz3), Neubeginn bei Unzumutbarkeit(Absatz5), sämtliche Hemmungen/§§204,206,210 und§193-Korrekturen nicht berechnet. Fristende daher nicht ungeprüft als tatsächlichen letzten Antragstag verwenden.']
    return ergebnis
