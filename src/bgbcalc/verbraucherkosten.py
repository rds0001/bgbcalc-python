"""Numerische Kostenregeln für Verbraucherverträge (§§312a,312e)."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _auswahl, _ergebnis, _fehler, _text, _vorhanden
from .zahlen import _addieren, _bruch, _subtrahieren
from .zinsen import _bruchteile


def verbraucher_informierte_nebenkosten(kostenpositionen=None, regelfall=None,
        kostenregel_anwendbar=None, einordnungsnachweis=None):
    """Nur ordnungsgemäß mitgeteilte, rechtlich berücksichtigungsfähige Kosten addieren."""
    _auswahl(regelfall, 'regelfall', ('praesenz_312a_absatz_2', 'fernabsatz_aussergeschaeftlich_312e'))
    _vorhanden(kostenpositionen, 'kostenpositionen')
    if not isinstance(kostenpositionen, list) or len(kostenpositionen) > 1000:
        _fehler('kostenpositionen', 'Liste mit höchstens1000 Kostenpositionen erforderlich.')
    namen = set()
    summe = _bruch(0)
    for position in kostenpositionen:
        if not isinstance(position, dict) or set(position) != {'position_id', 'betrag', 'ordnungsgemaess_informiert'}:
            _fehler('kostenpositionen', 'Genau position_id, betrag und ordnungsgemaess_informiert erforderlich.')
        name = _text(position['position_id'], 'position_id')
        if name in namen:
            _fehler('position_id', 'Kostenposition darf nicht doppelt aufgeführt werden.')
        namen.add(name)
        betrag = _geld(position['betrag'])
        informiert = _wahrheitswert(position['ordnungsgemaess_informiert'], 'ordnungsgemaess_informiert')
        if informiert:
            summe = _addieren(summe, betrag)
    _wahrheitswert(kostenregel_anwendbar, 'kostenregel_anwendbar')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    eingaben = dict(kostenpositionen=kostenpositionen, regelfall=regelfall,
        kostenregel_anwendbar=kostenregel_anwendbar, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(summe if kostenregel_anwendbar else None,
        'BGB_VERBRAUCHER_INFORMIERTE_NEBENKOSTEN', eingaben,
        [dict(operation='Rechtlich zugehörige Kostenpositionen mit ordnungsgemäßer Information auswählen und addieren')])
    ergebnis['hinweise'].append('Nur Fracht-, Liefer-, Versand- und sonstige Kosten der gewählten Norm. Vereinbarung, Höhe, Verbrauchervertragsbereich und Informationsanforderungen nach einschlägigem EGBGB-Verweis vorab qualifizieren.312a Absatz2 gilt nicht für Fernabsatz, außerhalb von Geschäftsräumen oder Finanzdienstleistungen. Teilweise informierte Positionen rechtlich zutreffend aufteilen, nicht volle Position freigeben. Hauptpreis und zusätzliche Entgeltgrenzen werden nicht berechnet. Leere Liste ergibt null EUR.')
    return ergebnis


def verbraucher_entgeltkostenvergleich(vereinbartes_entgelt=None, massgebliche_kosten=None,
        regelfall=None, vergleich_anwendbar=None, einordnungsnachweis=None):
    """Entgeltüberhang gegenüber Zahlungsmittelkosten oder bloßen Telekommunikationskosten."""
    entgelt = _geld(vereinbartes_entgelt)
    kosten = _geld(massgebliche_kosten)
    _auswahl(regelfall, 'regelfall', ('zahlungsmittel_312a_absatz_4', 'vertragsanruf_312a_absatz_5'))
    _wahrheitswert(vergleich_anwendbar, 'vergleich_anwendbar')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    ueberhang = max(_subtrahieren(entgelt, kosten), _bruch(0))
    eingaben = dict(vereinbartes_entgelt=vereinbartes_entgelt, massgebliche_kosten=massgebliche_kosten,
        regelfall=regelfall, vergleich_anwendbar=vergleich_anwendbar, einordnungsnachweis=einordnungsnachweis)
    wert = dict(kostenobergrenze=_bruchteile(kosten), entgeltueberhang=_bruchteile(ueberhang),
        kostengrenze_ueberschritten=entgelt > kosten) if vergleich_anwendbar else None
    ergebnis = _ergebnis(wert, 'EUR_und_wahrheitswert', 'BGB_VERBRAUCHER_ENTGELTKOSTENVERGLEICH', eingaben,
        [dict(operation='Vereinbartes Entgelt minus maßgebliche Kosten, mindestens null; strikte Überschreitung vergleichen')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if vergleich_anwendbar else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Qualifiziertes Verbraucherentgelt und einschlägige tatsächliche Kostenbasis, feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['Zahlungsmittel: Kosten des Unternehmers durch die konkrete Nutzung; unabhängig davon muss eine gängige zumutbare unentgeltliche Zahlungsmöglichkeit bestehen, und weitere Entgeltverbote etwa§270a bleiben unberührt. Vertragsanruf: Entgelt für bloße Nutzung des Telekommunikationsdienstes, nicht Zusatzvergütung des Unternehmers. Das Ergebnis ist KEIN auf die Obergrenze reduzierter Zahlungsanspruch: Eine überschreitende Vereinbarung ist nach der jeweiligen Norm unwirksam. Beim Vertragsanruf sieht Absatz5 zudem einen Anspruch des Telekommunikationsanbieters gegen den Unternehmer vor; kein solcher Anspruch wird hier automatisch festgestellt.']
    return ergebnis
