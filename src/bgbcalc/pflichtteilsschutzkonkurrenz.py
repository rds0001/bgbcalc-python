"""Numerische2318-Schutzkonkurrenz bei ausdrücklich qualifiziertem Erbenvorrang."""
from .betraege import _geld, _wahrheitswert
from .kalender import _ergebnis, _text
from .pflichtteilsvermaechtniskuerzung import vermaechtnis_pflichtteilskuerzung
from .zahlen import _bruch, _subtrahieren, _zahleneingabe
from .zinsen import _bruchteile


def vermaechtniskuerzung_bei_qualifiziertem_erbenvorrang(erwerbswert_vor_vermaechtnis=None, vermaechtniswert=None,
    gesamte_pflichtteilslast=None, anderweitig_getragene_last_2323=None,
    pflichtteilswert_erbe=None, pflichtteilswert_vermaechtnisnehmer=None,
    erbenvorrang_und_einzelfall_qualifiziert=None, rechts_und_bewertungsnachweis=None):
    """Bedachtenschutz und qualifizierten vorrangigen Erbenschutz kombinieren, Vorbeeinträchtigung nicht reparieren."""
    n = _geld(erwerbswert_vor_vermaechtnis)
    v = _geld(vermaechtniswert)
    eigen = _geld(pflichtteilswert_erbe)
    _wahrheitswert(erbenvorrang_und_einzelfall_qualifiziert, 'erbenvorrang_und_einzelfall_qualifiziert')
    _text(rechts_und_bewertungsnachweis, 'rechts_und_bewertungsnachweis')
    args = (erwerbswert_vor_vermaechtnis, vermaechtniswert, gesamte_pflichtteilslast, anderweitig_getragene_last_2323)
    bedacht = vermaechtnis_pflichtteilskuerzung(*args, 'vermaechtnisnehmer', pflichtteilswert_vermaechtnisnehmer, True, rechts_und_bewertungsnachweis)['wert']
    geschuetzt = min(eigen, _subtrahieren(n, v))
    # Nur der zusätzliche Erbenbedarf darf den Bedachtenschutz übergehen.
    last = _subtrahieren(_geld(gesamte_pflichtteilslast), _geld(anderweitig_getragene_last_2323))
    bedarf = min(v, max(_subtrahieren(geschuetzt, _subtrahieren(_subtrahieren(n, v), last)), _bruch(0)))
    kuerzung = max(_zahleneingabe(bedacht['kuerzungsbetrag']), bedarf)
    eingaben = dict(erwerbswert_vor_vermaechtnis=erwerbswert_vor_vermaechtnis, vermaechtniswert=vermaechtniswert,
        gesamte_pflichtteilslast=gesamte_pflichtteilslast, anderweitig_getragene_last_2323=anderweitig_getragene_last_2323,
        pflichtteilswert_erbe=pflichtteilswert_erbe, pflichtteilswert_vermaechtnisnehmer=pflichtteilswert_vermaechtnisnehmer,
        erbenvorrang_und_einzelfall_qualifiziert=erbenvorrang_und_einzelfall_qualifiziert, rechts_und_bewertungsnachweis=rechts_und_bewertungsnachweis)
    wert = dict(anteilige_grundkuerzung=bedacht['anteilige_grundkuerzung'], geschuetzter_vorbestehender_erbenwert=_bruchteile(geschuetzt),
        kuerzung_nach_bedachtenschutz=bedacht['kuerzungsbetrag'], vorrangiger_erbenbedarf=_bruchteile(bedarf),
        kuerzungsbetrag=_bruchteile(kuerzung), verbleibender_vermaechtniswert=_bruchteile(_subtrahieren(v, kuerzung)),
        verbleibender_erbenwert=_bruchteile(_subtrahieren(_subtrahieren(n, _subtrahieren(v, kuerzung)), last))) if erbenvorrang_und_einzelfall_qualifiziert else None
    ergebnis = _ergebnis(wert, 'EUR', 'BGB_VERMAECHTNISKUERZUNG_BEI_QUALIFIZIERTEM_ERBENVORRANG', eingaben,
        [dict(operation='Bedachtenschutz begrenzt proportionale Kürzung; nur fachlich qualifizierter vorrangiger Erbenbedarf hebt diese Grenze an; Schutz höchstens vorbestehender Erbenwert')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Ein Erbe und ein Vermächtnis; Erbenvorrang in konkreter2318-Schutzkonkurrenz ausdrücklich rechtlich qualifiziert.']
    ergebnis['hinweise'] = ['Keine automatische Entscheidung der Auslegungskonkurrenz2318II/III: Erbenvorrang muss fachlich vorgegeben sein. Vorbestehende Beeinträchtigung durch Vermächtnis wird nicht beseitigt; geschützt ist höchstens min(eigenerPflichtteil,Erwerb−Vermächtnis). Nur zusätzliche selbst zu tragende Pflichtteilslast nach2323 wird verteilt. Beide Beteiligten mit vergleichbar bewerteten Pflichtteilen; null als qualifizierter Schutzbetrag zulässig. Keine Mehrvermächtnisse,2189-Vorränge,2324-Anordnungen oder vorgelagerte Haftungsbeschränkungen. Erwerb,Vermächtnis und gesamteLast wie im Grundkern begrenzt; negativer verbleibender Erbenwert ist kein automatisch festgestellter Zahlungsanspruch.']
    return ergebnis
