from .kalender import _datum, _ergebnis, _fehler, _text, _vorhanden
from .betraege import _geld, _wahrheitswert
from .zahlen import _addieren
from .zinsen import _bruchteile

def hypothek_hinterlegung_forderung_und_zinsen(forderungsbetrag=None, ausschliessungsbeschluss_rechtskraeftig_am=None, zinssatz_im_grundbuch_eingetragen=None, zinsabschnitte=None, einordnungsnachweis=None):
    """Rechtlich qualifizierte Zinsabschnitte nach1171-Kalenderjahresgrenze auswählen und nur bei eingetragenem Zinssatz zum Forderungsbetrag addieren."""
    forderung=_geld(forderungsbetrag);_wahrheitswert(zinssatz_im_grundbuch_eingetragen,'zinssatz_im_grundbuch_eingetragen');_text(einordnungsnachweis,'einordnungsnachweis')
    jahr=_datum(ausschliessungsbeschluss_rechtskraeftig_am,'ausschliessungsbeschluss_rechtskraeftig_am').year
    if jahr<5: _fehler('ausschliessungsbeschluss_rechtskraeftig_am','Vier vorherige Kalenderjahre im Datumsbereich erforderlich.')
    grenze=f'{jahr-4:04d}-01-01'
    grenztag=_datum(grenze,'zinsbeginn');_vorhanden(zinsabschnitte,'zinsabschnitte')
    if not isinstance(zinsabschnitte,list) or len(zinsabschnitte)>1000: _fehler('zinsabschnitte','Liste0..1000 erforderlich.')
    intervalle=[]
    for z in zinsabschnitte:
        if not isinstance(z,dict) or set(z)!={'erster_zinstag','letzter_zinstag','zinsbetrag'}: _fehler('zinsabschnitte','Genau erster_zinstag, letzter_zinstag und zinsbetrag erforderlich.')
        a=_datum(z['erster_zinstag'],'erster_zinstag');b=_datum(z['letzter_zinstag'],'letzter_zinstag');betrag=_geld(z['zinsbetrag'])
        if b<a: _fehler('zinsabschnitte','Ende vor Beginn.')
        if a<grenztag<=b: _fehler('zinsabschnitte','Abschnitt an Kalenderjahresgrenze zuvor rechtlich zutreffend teilen.')
        intervalle.append((a,b,betrag))
    vorher=None;zins=_geld('0')
    for a,b,betrag in sorted(intervalle):
        if vorher is not None and a<=vorher: _fehler('zinsabschnitte','Überlappende Zinsabschnitte unzulässig.')
        vorher=b
        if zinssatz_im_grundbuch_eingetragen and a>=grenztag: zins=_addieren(zins,betrag)
    wert=dict(fruehester_hinterlegungszinsbeginn=grenze,hinterlegungszinsbetrag=_bruchteile(zins),hinterlegungsbetrag=_bruchteile(_addieren(forderung,zins)))
    eingaben = dict(forderungsbetrag=forderungsbetrag, ausschliessungsbeschluss_rechtskraeftig_am=ausschliessungsbeschluss_rechtskraeftig_am, zinssatz_im_grundbuch_eingetragen=zinssatz_im_grundbuch_eingetragen, zinsabschnitte=zinsabschnitte, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_HYPOTHEK_HINTERLEGUNG_FORDERUNG_UND_ZINSEN',eingaben,[dict(operation='Rechtlich qualifizierte Zinsabschnitte nach1171-Kalenderjahresgrenze auswählen und nur bei eingetragenem Zinssatz zum Forderungsbetrag addieren.')],eingaben.copy())
    ergebnis["hinweise"] = ['§1171I: Forderungsbetrag plus erforderliche eingetragene Zinsen, deren Zinszeitraum nicht vor Beginn des vierten Kalenderjahres vor Rechtskraft liegt. Maßgeblich ist Zinszeit, nicht Fälligkeit oder Buchungstag. Abschnittsbeträge nach zutreffendem Satz/Kapital/Zinszeitanteil zuvor berechnen, etwa mit gesetzliche_zinsen; keine pauschale Tageslinearität für beliebig vorgegebene Zinsbeträge. Abschnitt über die Kalenderjahresgrenze muss vorher rechtlich zutreffend geteilt werden. Keine automatische Zinsentstehung, Hinterlegungswirksamkeit oder Erlöschensentscheidung1171II/III. Eingaben sind bereits rechtlich zu hinterlegende abgeschlossene Zinsabschnitte; keine Zukunftszinsen erfinden. Ohne eingetragenen Zinssatz keinen Zinsbetrag zur Hinterlegung addieren.']
    return ergebnis

