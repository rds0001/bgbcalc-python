from .kalender import _ergebnis, _text, _vorhanden, _fehler
from .betraege import _geld
from .zahlen import _bruch, _addieren
from .fortsetzung_beguenstigtenbezogene_lasten import fortsetzung_beguenstigtenbezogene_lasten

def fortsetzung_interne_schuldanteile(gesamtgutschuld=None, abkoemmlinge=None, haftungsnachweis=None):
    """Gesamtgutschuld intern nach relativen qualifizierten Gesamtgutsanteilen verteilen; gegenstaendliche Haftungsgrenze nicht in Gelddeckel umdeuten."""
    _text(haftungsnachweis,'haftungsnachweis');_geld(gesamtgutschuld);_vorhanden(abkoemmlinge,'abkoemmlinge')
    if not isinstance(abkoemmlinge,list) or not 1<=len(abkoemmlinge)<=1000: _fehler('abkoemmlinge','Begrenzte nichtleere Liste erforderlich.')
    basis=[];gewichte=[];summe=_bruch(0)
    for a in abkoemmlinge:
        if not isinstance(a,dict) or set(a)!={'abkoemmling_id','anteil_gesamtgut'}: _fehler('abkoemmlinge','Kennung und Gesamtgutsanteil erforderlich.')
        q=_geld(a['anteil_gesamtgut']);summe=_addieren(summe,q)
        basis.append(dict(abkoemmling_id=a['abkoemmling_id'],grundanteilswert='0'));gewichte.append(dict(abkoemmling_id=a['abkoemmling_id'],lastgewicht=a['anteil_gesamtgut']))
    if summe>1: _fehler('anteil_gesamtgut','Anteilssumme darf eins nicht uebersteigen.')
    k=fortsetzung_beguenstigtenbezogene_lasten(basis,[dict(last_id='1504',betrag=gesamtgutschuld,beguenstigte=gewichte)],haftungsnachweis)['wert']
    wert=[dict(abkoemmling_id=a['abkoemmling_id'],interner_schuldanteil=a['lastensumme']) for a in k['abkoemmlingssalden']]
    eingaben = dict(gesamtgutschuld=gesamtgutschuld, abkoemmlinge=abkoemmlinge, haftungsnachweis=haftungsnachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_FORTSETZUNG_INTERNE_SCHULDANTEILE',eingaben,[dict(operation='Gesamtgutschuld intern nach relativen qualifizierten Gesamtgutsanteilen verteilen; gegenstaendliche Haftungsgrenze nicht in Gelddeckel umdeuten.')],eingaben.copy())
    ergebnis["hinweise"] = ['§1504 interne Verteilung der qualifizierten Gesamtgutschuld nach relativer Groesse der Gesamtgutsanteile der anteilsberechtigten Abkoemmlinge. Vorhandenen exakten Beguenstigten-Gewichtskern rein rechnerisch wiederverwenden; keine Anwendung1503III auf Glaeubigerschulden behaupten. Die Verpflichtung beschraenkt sich auf zugeteilte Gegenstaende: kein pauschaler Gelddeckel in Hoehe ihres Schaetzwerts und keine allgemeine persoenliche Nachschusspflicht. Ergebnis ist interne Schuldzuordnung vor gegenstaendlicher Vollstreckungs-/Haftungspruefung, kein bezifferter individuell durchsetzbarer Zahlungsanspruch. Keine automatische Ausfallumlage.']
    return ergebnis

