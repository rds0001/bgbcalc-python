"""Rechnerische persönliche Ausstattungsinnenlast in der Gütergemeinschaft."""
from .betraege import _geld
from .kalender import _ergebnis, _fehler, _text
from .zahlen import _addieren, _bruch, _subtrahieren
from .zinsen import _bruchteile


def ausstattung_persoenliche_innenlast(ausstattungsbetrag=None, gesamtgutangemessener_betrag=None, zugestimmter_mehrbetrag=None, berechnungsfall=None, zuordnungsnachweis=None):
    """§§1444/1466: qualifizierte Ausstattungsinnenlast als Mehr-/Grund-/Zustimmungsbetrag berechnen."""
    ausstattung = _geld(ausstattungsbetrag)
    angemessen = _geld(gesamtgutangemessener_betrag)
    zustimmung = _geld(zugestimmter_mehrbetrag)
    _text(berechnungsfall,'berechnungsfall')
    _text(zuordnungsnachweis,'zuordnungsnachweis')
    faelle = ['gemeinschaftliches_kind_alleinverwalter','nichtgemeinschaftliches_kind_elternteil_alleinverwalter','nichtgemeinschaftliches_kind_elternteil_nichtverwalter','nichtgemeinschaftliches_kind_gemeinschaftliche_verwaltung']
    if berechnungsfall not in faelle:
        _fehler('berechnungsfall','Qualifizierter gesetzlicher Berechnungsfall nach§1444 oder§1466 erforderlich.')
    grundbetrag = min(ausstattung,angemessen)
    mehrbetrag = _subtrahieren(ausstattung,grundbetrag)
    if zustimmung > mehrbetrag:
        _fehler('zugestimmter_mehrbetrag','Zugestimmter Mehrbetrag darf den tatsächlich über dem Gesamtgutmaß liegenden Betrag nicht übersteigen.')
    if berechnungsfall != 'nichtgemeinschaftliches_kind_elternteil_nichtverwalter' and zustimmung != 0:
        _fehler('zugestimmter_mehrbetrag','Zustimmungsmehrbetrag nur im Nichtverwalter-Elternfall verwenden; sonst null.')
    if berechnungsfall == 'gemeinschaftliches_kind_alleinverwalter':
        last = mehrbetrag
    elif berechnungsfall == 'nichtgemeinschaftliches_kind_elternteil_nichtverwalter':
        last = _addieren(grundbetrag,zustimmung)
    else:
        last = ausstattung
    eingaben = dict(ausstattungsbetrag=ausstattungsbetrag,gesamtgutangemessener_betrag=gesamtgutangemessener_betrag,zugestimmter_mehrbetrag=zugestimmter_mehrbetrag,berechnungsfall=berechnungsfall,zuordnungsnachweis=zuordnungsnachweis)
    wert = dict(persoenliche_innenlast=_bruchteile(last),nicht_als_persoenliche_innenlast_erfasst=_bruchteile(_subtrahieren(ausstattung,last)))
    ergebnis = _ergebnis(wert,'EUR','BGB_AUSSTATTUNG_PERSOENLICHE_INNENLAST',eingaben,[dict(operation='Gemeinschaftliches Kind: nur Mehrbetrag des Alleinverwalters; nichtgemeinschaftliches Kind: Elternteil volle Last, bei Nichtverwaltung nur Gesamtgutmaß plus konkret zugestimmtem Mehrbetrag.')],eingaben.copy())
    ergebnis['hinweise'] = ['Gesetzliche Innenlast ohne abweichende Vereinbarung. Bei gemeinschaftlichem Kind nach§1444I ist die persönliche Last des allein verwaltenden Ehegatten gemeint. Bei nichtgemeinschaftlichem Kind ist die persönliche Last des Elternteils gemeint:§1444II bei Alleinverwaltung,§1466 bei gemeinschaftlicher Verwaltung. Umfang der Ausstattung und Gesamtgutmaß rechtlich bewertet; keine automatische Bestimmung von Elternschaft, Kindeseigenschaft, Verwaltungsform oder Angemessenheit. Im Nichtverwalter-Elternfall Zustimmung ausschließlich als tatsächlich zugestimmter Teil des über dem Maß liegenden Mehrbetrags vorgeben; nicht pauschal irgendeinen zugestimmten Gesamtbetrag verwenden, da sonst Überlappungen doppelt zählen. Übriger Betrag wird nur als nicht dieser persönlichen Last zugeordnet ausgewiesen, nicht automatisch dem anderen Ehegatten oder einer Masse auferlegt. Keine Außenhaftung, Erfüllung, Schenkungsbewertung oder Ausgleichsfälligkeit berechnet.']
    return ergebnis
