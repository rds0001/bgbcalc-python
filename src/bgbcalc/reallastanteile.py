"""Flächenproportionale Verteilung einer teilbaren Reallast nach §1109."""
from .betraege import _geld
from .kalender import _ergebnis, _fehler, _text, _vorhanden
from .zahlen import _addieren, _bruch, _dividieren, _multiplizieren, _zahleneingabe
from .zinsen import _bruchteile


def reallast_flaechenanteile(teilbare_leistungsmenge=None, grundstuecksteile=None, verteilungsnachweis=None):
    """§1109I: teilbare Reallastleistung nach den Flächen der Grundstücksteile verteilen."""
    bedarf = _geld(teilbare_leistungsmenge)
    _vorhanden(grundstuecksteile, 'grundstuecksteile')
    if not isinstance(grundstuecksteile,list) or not 1 <= len(grundstuecksteile) <= 1000:
        _fehler('grundstuecksteile','Liste mit 1 bis 1000 qualifizierten Grundstücksteilen erforderlich.')
    namen,gewichte = [],[]
    summe = _bruch(0)
    for eintrag in grundstuecksteile:
        if not isinstance(eintrag,dict) or set(eintrag) != {'grundstueck_id','flaeche'}:
            _fehler('grundstuecksteile','Genau grundstueck_id und flaeche erforderlich.')
        name = _text(eintrag['grundstueck_id'],'grundstueck_id')
        if name in namen:
            _fehler('grundstueck_id','Grundstücksteil nicht mehrfach aufführen.')
        _vorhanden(eintrag['flaeche'],'flaeche')
        gewicht = _zahleneingabe(eintrag['flaeche'])
        if gewicht <= 0:
            _fehler('flaeche','Positive Fläche in derselben Einheit erforderlich.')
        namen.append(name);gewichte.append(gewicht);summe = _addieren(summe,gewicht)
    _text(verteilungsnachweis,'verteilungsnachweis')
    anteile=[]
    for name,gewicht in zip(namen,gewichte):
        quote = _dividieren(gewicht,summe)
        anteile.append(dict(grundstueck_id=name,anteilsquote=_bruchteile(quote),leistungsanteil=_bruchteile(_multiplizieren(bedarf,quote))))
    eingaben = dict(teilbare_leistungsmenge=teilbare_leistungsmenge,grundstuecksteile=grundstuecksteile,verteilungsnachweis=verteilungsnachweis)
    ergebnis = _ergebnis(anteile,'leistungseinheiten','BGB_REALLAST_FLAECHENANTEILE',eingaben,[dict(operation='Flächen summieren, einzelne Fläche durch Gesamtfläche teilen und teilbare Leistung damit multiplizieren.')],eingaben.copy())
    ergebnis['hinweise'] = ['Nur qualifizierter Grundfall des§1109Absatz1 nach Teilung des berechtigten Grundstücks. Leistung ist tatsächlich teilbar und in einer gemeinsamen Einheit bewertet; sämtliche betroffenen Teile mit positiver Fläche in derselben Flächeneinheit erfassen. Keine abweichende wirksame Zuordnung nachAbsatz2, keine Beschränkung auf einen allein begünstigten Teil nachAbsatz3. Unteilbare Leistungen nach§432 und Ausübungsmodalitäten bleiben außerhalb dieser Mengenverteilung. Keine automatische Feststellung dinglicher Rechte.']
    return ergebnis
