"""Unterhaltsfehlbetrag und nachrangige Geldbeträge bei qualifizierten Schenkungen."""
from .betraege import _geld
from .kalender import _text, _fehler, _vorhanden, _ganzzahl, _ergebnis
from .zahlen import _bruch, _subtrahieren, _addieren
from .zinsen import _bruchteile


def schenkung_unterhaltsrueckforderung(unterhaltsbedarf=None, eigene_deckungsmittel=None, beschenkte=None, einordnungsnachweis=None):
    """Fehlbedarf ermitteln und auf Beschenkte in umgekehrter qualifizierter Schenkungsrangfolge verteilen."""
    bedarf, deckung = _geld(unterhaltsbedarf), _geld(eigene_deckungsmittel)
    _text(einordnungsnachweis,'einordnungsnachweis')
    _vorhanden(beschenkte,'beschenkte')
    if not isinstance(beschenkte,list) or len(beschenkte)>1000:
        _fehler('beschenkte','Liste mit höchstens 1000 Beschenkten erforderlich.')
    geprueft=[]; kennungen=set(); raenge=set()
    for person in beschenkte:
        if not isinstance(person,dict) or set(person)!={'beschenkten_id','schenkungsrang','bereicherungsgrenze','leistungsfaehigkeitsgrenze'}:
            _fehler('beschenkte','Je Beschenktem sind Kennung, eindeutiger Schenkungsrang und beide Betragsgrenzen erforderlich.')
        kennung=_text(person['beschenkten_id'],'beschenkten_id')
        rang=_ganzzahl(person['schenkungsrang'],'schenkungsrang',1,1000000)
        if kennung in kennungen or rang in raenge:
            _fehler('beschenkte','Beschenktenkennungen und rechtlich bestimmte Schenkungsränge müssen eindeutig sein.')
        kennungen.add(kennung); raenge.add(rang)
        geprueft.append((rang,kennung,_geld(person['bereicherungsgrenze']),_geld(person['leistungsfaehigkeitsgrenze'])))
    fehlbetrag=max(_subtrahieren(bedarf,deckung),_bruch(0)); rest=fehlbetrag; verteilung=[]
    for rang,kennung,bereicherung,leistungsfaehigkeit in sorted(geprueft,reverse=True):
        anteil=min(rest,bereicherung,leistungsfaehigkeit)
        rest=_subtrahieren(rest,anteil)
        verteilung.append(dict(beschenkten_id=kennung,rueckforderungsbetrag=_bruchteile(anteil)))
    wert=dict(unterhaltsfehlbetrag=_bruchteile(fehlbetrag),verteilung=verteilung,gesamtbetrag=_bruchteile(_subtrahieren(fehlbetrag,rest)),ungedeckter_fehlbetrag=_bruchteile(rest))
    eingaben=dict(unterhaltsbedarf=unterhaltsbedarf,eigene_deckungsmittel=eigene_deckungsmittel,beschenkte=beschenkte,einordnungsnachweis=einordnungsnachweis)
    ergebnis=_ergebnis(wert,'EUR','BGB_SCHENKUNG_UNTERHALTSRUECKFORDERUNG',eingaben,[dict(operation='Positiven Unterhaltsfehlbetrag in absteigender Schenkungsrangfolge jeweils auf Bereicherungs- und Leistungsfähigkeitsgrenze begrenzen.')],eingaben.copy())
    ergebnis['hinweise']=['Nur qualifizierte Geldbeträge eines einheitlichen Unterhaltszeitraums nach §§528/529. Jede Person genau einmal mit einem eindeutigen Schenkungsrang; höherer Rang bedeutet später beschenkt. Gleichzeitig Beschenkte und mehrere Schenkungen an dieselbe Person mit konkurrierenden Rängen sind nicht erfasst. Bedarf umfasst rechtlich berücksichtigungsfähigen eigenen Unterhalt und gesetzliche Unterhaltspflichten. Bereicherungsgrenze muss Bereicherungsrecht, bereits erfolgte Rückzahlungen und Ausschlüsse nach §529 Absatz1 berücksichtigen; ausgeschlossene Schenkung mit null. Leistungsfähigkeitsgrenze ist nach §529 Absatz2 unter Berücksichtigung sonstiger Verpflichtungen rechtlich bestimmter verfügbarer Geldbetrag. Keine automatische Bewertung von Sachgeschenken, Unterhalt, Leistungsfähigkeit, Bedürftigkeit, Frist oder Anspruchsausschluss; keine wiederholte Nutzung derselben verbleibenden Bereicherung ohne Fortschreibung. Abwendung durch Unterhaltszahlung, Fälligkeit/Rückstände nach §§760/1613 und Tod nach §1615 gesondert qualifizieren.']
    return ergebnis
