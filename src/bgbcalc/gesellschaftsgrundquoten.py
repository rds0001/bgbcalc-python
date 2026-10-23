"""§709: normierte Beteiligungs-, Beitragswert- und Gleichanteilsquoten."""
from .betraege import _geld
from .kalender import _text, _fehler, _vorhanden, _auswahl, _ergebnis
from .zahlen import _bruch, _addieren, _dividieren
from .zinsen import _bruchteile


def gesellschaft_gewinn_verlust_stimmquoten(gesellschafter=None, quotenbasis=None, einordnungsnachweis=None):
    """Qualifizierte Beteiligungsverhältnisse oder Beitragswerte normieren, sonst gleiche Anteile."""
    _auswahl(quotenbasis,'quotenbasis',('beteiligungsverhaeltnisse','beitragswerte','gleiche_anteile'))
    _text(einordnungsnachweis,'einordnungsnachweis'); _vorhanden(gesellschafter,'gesellschafter')
    if not isinstance(gesellschafter,list) or not 2<=len(gesellschafter)<=1000:
        _fehler('gesellschafter','Vollständige Liste mit2bis1000 Gesellschaftern erforderlich.')
    namen=[]; gewichte=[]; summe=_bruch(0)
    for person in gesellschafter:
        if not isinstance(person,dict) or set(person)!={'gesellschafter_id','gewicht'}:
            _fehler('gesellschafter','Genau gesellschafter_id und gewicht erforderlich.')
        kennung=_text(person['gesellschafter_id'],'gesellschafter_id')
        if kennung in namen:
            _fehler('gesellschafter_id','Gesellschafterkennungen müssen eindeutig sein.')
        if quotenbasis=='gleiche_anteile':
            if person['gewicht'] is not None:
                _fehler('gewicht','Bei Gleichanteilen muss gewicht ausdrücklich null sein.')
            gewicht=_bruch(1)
        else:
            gewicht=_geld(person['gewicht'])
        namen.append(kennung); gewichte.append(gewicht); summe=_addieren(summe,gewicht)
    if summe==0:
        _fehler('gewicht','Summe der vereinbarten Verhältnisse oder Beitragswerte muss positiv sein.')
    wert=[dict(gesellschafter_id=n,quote=_bruchteile(_dividieren(g,summe))) for n,g in zip(namen,gewichte)]
    eingaben=dict(gesellschafter=gesellschafter,quotenbasis=quotenbasis,einordnungsnachweis=einordnungsnachweis)
    ergebnis=_ergebnis(wert,'quoten','BGB_GESELLSCHAFT_GEWINN_VERLUST_STIMMQUOTEN',eingaben,[dict(operation='Je Gesellschafter vereinbartes Gewicht durch Summe teilen; ohne Beteiligungsverhältnis und vereinbarten Beitragswert je1/Anzahl.')],eingaben.copy())
    ergebnis['hinweise']=['§709 Absatz3: vereinbarte Beteiligungsverhältnisse gehen vor vereinbarten Beitragswerten; nur wenn beides fehlt Gleichanteile. quotenbasis ist rechtlich qualifiziert auszuwählen, kein freies Wahlrecht zur günstigeren Quote. Beteiligungsgewichte sind relative Verhältnisse, Beitragswerte vertraglich vereinbarte gleichartige Werte, keine von der Bibliothek geschätzten tatsächlichen Leistungen. Vollständiger identischer Gesellschafterkreis; individuelle Sondervereinbarungen über Gewinn/Verlust/Stimmkraft gesondert behandeln. Bei fehlender Wertevereinbarung ausdrücklich gewicht=null, nicht unbekannte Aktenlage. Beitragsleistungspflichten nach Absatz2 und Ausschüttungsbetrag nicht berechnet.']
    return ergebnis
