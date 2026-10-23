"""§519: verfügbare Deckung und Vorrang früher entstandener Schenkungsansprüche."""
from .betraege import _geld
from .kalender import _text, _fehler, _vorhanden, _ganzzahl, _ergebnis
from .zahlen import _bruch, _subtrahieren
from .zinsen import _bruchteile


def schenkungsversprechen_deckungsverteilung(verfuegbare_mittel=None, geschuetzter_mittelbedarf=None, schenkungsansprueche=None, einordnungsnachweis=None):
    """Positive Deckung oberhalb qualifizierter Schutzbedarfe auf frühere Ansprüche zuerst verteilen."""
    mittel, bedarf = _geld(verfuegbare_mittel), _geld(geschuetzter_mittelbedarf)
    _text(einordnungsnachweis,'einordnungsnachweis'); _vorhanden(schenkungsansprueche,'schenkungsansprueche')
    if not isinstance(schenkungsansprueche,list) or len(schenkungsansprueche)>1000:
        _fehler('schenkungsansprueche','Liste mit höchstens1000 Ansprüchen erforderlich.')
    geprueft=[]; kennungen=set(); raenge=set()
    for anspruch in schenkungsansprueche:
        if not isinstance(anspruch,dict) or set(anspruch)!={'anspruch_id','entstehungsrang','anspruchsbetrag'}:
            _fehler('schenkungsansprueche','Je Anspruch sind Kennung, eindeutiger Entstehungsrang und Anspruchsbetrag erforderlich.')
        kennung=_text(anspruch['anspruch_id'],'anspruch_id')
        rang=_ganzzahl(anspruch['entstehungsrang'],'entstehungsrang',1,1000000)
        if kennung in kennungen or rang in raenge:
            _fehler('schenkungsansprueche','Anspruchskennungen und rechtlich bestimmte Entstehungsränge müssen eindeutig sein.')
        kennungen.add(kennung); raenge.add(rang)
        geprueft.append((rang,kennung,_geld(anspruch['anspruchsbetrag'])))
    deckung=max(_subtrahieren(mittel,bedarf),_bruch(0)); rest=deckung; verteilung=[]
    for rang,kennung,betrag in sorted(geprueft):
        zahlung=min(rest,betrag); rest=_subtrahieren(rest,zahlung)
        verteilung.append(dict(anspruch_id=kennung,deckungsbetrag=_bruchteile(zahlung),verweigerbarer_fehlbetrag=_bruchteile(_subtrahieren(betrag,zahlung))))
    wert=dict(verfuegbare_deckung=_bruchteile(deckung),verteilung=verteilung,gesamtdeckungsbetrag=_bruchteile(_subtrahieren(deckung,rest)),unverbrauchte_deckung=_bruchteile(rest))
    eingaben=dict(verfuegbare_mittel=verfuegbare_mittel,geschuetzter_mittelbedarf=geschuetzter_mittelbedarf,schenkungsansprueche=schenkungsansprueche,einordnungsnachweis=einordnungsnachweis)
    ergebnis=_ergebnis(wert,'EUR','BGB_SCHENKUNGSV ERSPRECHEN_DECKUNGSVERTEILUNG'.replace(' ',''),eingaben,[dict(operation='Verfügbare Mittel minus qualifizierter Schutzbedarf, mindestens null; in aufsteigender Entstehungsrangfolge bis zur jeweiligen Anspruchshöhe verteilen.')],eingaben.copy())
    ergebnis['hinweise']=['Nur §519 für zusammentreffende qualifizierte noch nicht erfüllte Geldansprüche aus Schenkungsversprechen. Geschützter Mittelbedarf umfasst ohne Doppelzählung sonstige Verpflichtungen, angemessenen Eigenunterhalt und gesetzliche Unterhaltspflichten; alle Werte gleiche rechtlich bestimmte Bewertungsbasis. Höherer Rang bedeutet später entstandener Anspruch, frühere Ansprüche gehen vor. Keine automatische Bestimmung von Bedürftigkeit, Vermögensverwertbarkeit, Leistungszeit oder gesetzlichem Unterhalt. Gleichzeitige Anspruchsentstehung und Sachleistungsbewertung nicht erfasst. Fehlbetrag bezeichnet den bei qualifiziertem §519-Tatbestand verweigerbaren Teil, keine automatische Erlöschung der Forderung. Bereits erfüllte Schenkungen fallen gegebenenfalls unter §528/529, dort umgekehrte Rangfolge.']
    return ergebnis
