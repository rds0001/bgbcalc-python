"""Mindestende der vererbten Ausschlagungsfrist (§1952 Absatz2)."""
from .betraege import _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler, _text


def vererbte_ausschlagungsfrist(
    tod_des_erben_am=None, bisheriges_ausschlagungsfristende=None,
    ausschlagungsfristende_erbeserbschaft=None, ausschlagungsrecht_vererblich_vorhanden=None,
    einordnungsnachweis=None,
):
    """Frist des zuerst angefallenen Nachlasses mindestens bis Frist für Nachlass des Erben."""
    tod = _datum(tod_des_erben_am, 'tod_des_erben_am')
    bisher = _datum(bisheriges_ausschlagungsfristende, 'bisheriges_ausschlagungsfristende')
    erbe = _datum(ausschlagungsfristende_erbeserbschaft, 'ausschlagungsfristende_erbeserbschaft')
    if erbe < tod:
        _fehler('ausschlagungsfristende_erbeserbschaft', 'Frist für Erbschaft des Erben darf nicht vor dessen Tod enden.')
    _wahrheitswert(ausschlagungsrecht_vererblich_vorhanden, 'ausschlagungsrecht_vererblich_vorhanden')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    eingaben = dict(tod_des_erben_am=tod_des_erben_am,
        bisheriges_ausschlagungsfristende=bisheriges_ausschlagungsfristende,
        ausschlagungsfristende_erbeserbschaft=ausschlagungsfristende_erbeserbschaft,
        ausschlagungsrecht_vererblich_vorhanden=ausschlagungsrecht_vererblich_vorhanden,
        einordnungsnachweis=einordnungsnachweis)
    gilt = ausschlagungsrecht_vererblich_vorhanden and tod <= bisher
    wert = max(bisher, erbe).isoformat() if gilt else None
    ergebnis = _ergebnis(wert, 'datum', 'BGB_VERERBTE_AUSSCHLAGUNGSFRIST', eingaben,
        [dict(operation='Bei Tod vor Fristablauf Ende der ursprünglichen Ausschlagungsfrist mindestens auf Ende der Frist für Erbschaft des Erben verlängern')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if gilt else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Zwei getrennte Erbfälle und rechtlich bestimmte Ausschlagungsfristen für denselben Erbeserben; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['Bisheriges Fristende gehört zum zuerst angefallenen Nachlass; Vergleichsende zur Erbschaft des verstorbenen Erben. Jeweilige Fristen einschließlich Kenntnis, Bekanntgabe und zulässiger Korrekturen gesondert bestimmen, beispielsweise mit erbausschlagung_grundfrist für Grundfristen. Kein Neubeginn um sechs Wochen ab Tod und keine Addition beider Fristen. Bereits wirksame Annahme oder Ausschlagung und sonstiger Verlust des Rechts verhindern ein vorhandenes vererbliches Ausschlagungsrecht. Tod am letzten Tag liegt im taggenauen Modell vor Ablauf am Tagesende; untertägige Sonderreihenfolge vorab klären. Für mehrere Erbeserben individuell berechnen; Teilrecht nach§1952 Absatz3 nicht durch ein gemeinsames pauschales Datum ersetzen. Fristverlängerung entscheidet nicht über Form/Adressat der Ausschlagung oder spätere Hemmung.']
    return ergebnis
