from .kalender import _datum, _ergebnis, _fehler, _text, _vorhanden
from .digitalbeendigung_betraege import digitalbeendigung_zeitanteilige_betraege

def digitalbeendigung_kalenderabschnitt(abschnitt_von=None, abschnitt_bis=None, nicht_mehr_geschuldet_ab=None, mangelzeitraeume=None, vereinbarter_abschnittspreis=None, gezahlter_abschnittspreis=None, einordnungsnachweis=None):
    """Mangelintervalle begrenzen und vereinigen; disjunkte Mangel-/Zukunftstage zählen und vorhandene zeitanteilige Erstattungsrechnung anwenden."""
    von=_datum(abschnitt_von,'abschnitt_von');bis=_datum(abschnitt_bis,'abschnitt_bis');ab=_datum(nicht_mehr_geschuldet_ab,'nicht_mehr_geschuldet_ab');_text(einordnungsnachweis,'einordnungsnachweis')
    if bis<von: _fehler('abschnitt_bis','Abschnittsende liegt vor Beginn.')
    _vorhanden(mangelzeitraeume,'mangelzeitraeume')
    if not isinstance(mangelzeitraeume,list) or len(mangelzeitraeume)>10000: _fehler('mangelzeitraeume','Liste mit hoechstens10000Intervallen erforderlich.')
    intervalle=[]
    for z in mangelzeitraeume:
        if not isinstance(z,dict) or set(z)!={'von','bis'}: _fehler('mangelzeitraeume','Genau von und bis erforderlich.')
        a=_datum(z['von'],'von');e=_datum(z['bis'],'bis')
        if e<a: _fehler('mangelzeitraeume','Intervallende liegt vor Beginn.')
        anfang=max(a.toordinal(),von.toordinal());ende=min(e.toordinal(),bis.toordinal(),ab.toordinal()-1)
        if anfang<=ende: intervalle.append((anfang,ende))
    vereinigt=[]
    for a,e in sorted(intervalle):
        if vereinigt and a<=vereinigt[-1][1]+1: vereinigt[-1]=(vereinigt[-1][0],max(e,vereinigt[-1][1]))
        else: vereinigt.append((a,e))
    gesamt=(bis-von).days+1;mangel=sum(e-a+1 for a,e in vereinigt);zukunft=max(0,(bis-max(ab,von)).days+1)
    wert=digitalbeendigung_zeitanteilige_betraege(vereinbarter_abschnittspreis,gezahlter_abschnittspreis,str(gesamt),str(mangel),str(zukunft),einordnungsnachweis)['wert']
    wert.update(kalendertage_gesamt=gesamt,kalendertage_mangelhaft=mangel,kalendertage_nicht_mehr_geschuldet=zukunft)
    eingaben = dict(abschnitt_von=abschnitt_von, abschnitt_bis=abschnitt_bis, nicht_mehr_geschuldet_ab=nicht_mehr_geschuldet_ab, mangelzeitraeume=mangelzeitraeume, vereinbarter_abschnittspreis=vereinbarter_abschnittspreis, gezahlter_abschnittspreis=gezahlter_abschnittspreis, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'tage_quote_und_eur','BGB_DIGITALBEENDIGUNG_KALENDERABSCHNITT',eingaben,[dict(operation='Mangelintervalle begrenzen und vereinigen; disjunkte Mangel-/Zukunftstage zählen und vorhandene zeitanteilige Erstattungsrechnung anwenden.')],eingaben.copy())
    ergebnis["hinweise"] = ['§327oII/III: nur dauerhafte digitale Bereitstellung und rechtlich qualifizierte ganze Kalendertage bei gleicher Bewertung jedes Tages im Abschnitt. Mangelintervalle werden auf bereits geschuldete Tage im Abschnitt begrenzt und vereinigt. Zukünftig entfallende Tage separat zählen; keine Doppelzählung bei Überschneidungen. Vorhandene exakte Preis-/Erstattungsrechnung verwenden. Unterschiedlich bepreiste oder bezahlte Abschnitte einzeln abrechnen. Untertägige Leistungen nicht runden; hierfür vorhandene Rechnung mit rechtlich bestimmten Zeiteinheiten verwenden. Keine automatische Mangel- oder Beendigungsentscheidung und keine pauschale30-Tage-Monatsannahme. Überzahlungen über Abschnittspreis separat; erloschener Preisanteil ist nicht zusätzlich neben Erstattung zu zahlen.']
    return ergebnis

