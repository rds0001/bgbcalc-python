"""Eigengeschenk bei Pflichtteilsergänzung mit getrennter§2315-Anrechnung (§2327)."""
from .betraege import _geld, _wahrheitswert
from .kalender import _ergebnis, _fehler, _ganzzahl, _text
from .zahlen import GRENZE, _addieren, _bruch, _multiplizieren, _subtrahieren, _zahleneingabe
from .zinsen import _bruchteile


def pflichtteilsergaenzung_eigengeschenk(pflichtteilsnachlass=None,
    hinzuzurechnende_drittschenkungen=None, eigengeschenk_wert=None,
    gesetzliche_erbquote_zaehler=None, gesetzliche_erbquote_nenner=None,
    eigengeschenk_nach_2315_anzurechnen=None, einheitlicher_wert_qualifiziert=None,
    grundmodell_ohne_ausgleichung_anwendbar=None, bewertungsnachweis=None):
    """Ein einheitlich bewertetes Eigengeschenk hinzurechnen und nur am gesetzlichen Ziel anrechnen."""
    nachlass = _zahleneingabe(pflichtteilsnachlass)
    dritte = _geld(hinzuzurechnende_drittschenkungen)
    eigen = _geld(eigengeschenk_wert)
    zaehler = _ganzzahl(gesetzliche_erbquote_zaehler, 'gesetzliche_erbquote_zaehler', 0, GRENZE)
    nenner = _ganzzahl(gesetzliche_erbquote_nenner, 'gesetzliche_erbquote_nenner', 1, GRENZE)
    if zaehler > nenner:
        _fehler('gesetzliche_erbquote', 'Gesetzliche Erbquote darf eins nicht übersteigen.')
    _wahrheitswert(eigengeschenk_nach_2315_anzurechnen, 'eigengeschenk_nach_2315_anzurechnen')
    _wahrheitswert(einheitlicher_wert_qualifiziert, 'einheitlicher_wert_qualifiziert')
    _wahrheitswert(grundmodell_ohne_ausgleichung_anwendbar, 'grundmodell_ohne_ausgleichung_anwendbar')
    _text(bewertungsnachweis, 'bewertungsnachweis')
    eingaben = dict(pflichtteilsnachlass=pflichtteilsnachlass,
        hinzuzurechnende_drittschenkungen=hinzuzurechnende_drittschenkungen, eigengeschenk_wert=eigengeschenk_wert,
        gesetzliche_erbquote_zaehler=gesetzliche_erbquote_zaehler, gesetzliche_erbquote_nenner=gesetzliche_erbquote_nenner,
        eigengeschenk_nach_2315_anzurechnen=eigengeschenk_nach_2315_anzurechnen,
        einheitlicher_wert_qualifiziert=einheitlicher_wert_qualifiziert,
        grundmodell_ohne_ausgleichung_anwendbar=grundmodell_ohne_ausgleichung_anwendbar,
        bewertungsnachweis=bewertungsnachweis)
    wert = None
    if einheitlicher_wert_qualifiziert and grundmodell_ohne_ausgleichung_anwendbar:
        quote = _multiplizieren(_bruch(zaehler, nenner), _bruch(1, 2))
        ordentlich_grundlage = _addieren(nachlass, eigen) if eigengeschenk_nach_2315_anzurechnen else nachlass
        ordentlich_vor = _multiplizieren(max(ordentlich_grundlage, _bruch(0)), quote)
        ordentlich = max(_subtrahieren(ordentlich_vor, eigen), _bruch(0)) if eigengeschenk_nach_2315_anzurechnen else ordentlich_vor
        fiktiv = _multiplizieren(max(_addieren(_addieren(nachlass, dritte), eigen), _bruch(0)), quote)
        if eigengeschenk_nach_2315_anzurechnen:
            gesamt = max(_subtrahieren(fiktiv, eigen), _bruch(0))
            # Nichtnegative Drittschenkungen: gesamt ist mindestens ordentlich.
            ergaenzung = _subtrahieren(gesamt, ordentlich)
        else:
            ergaenzung = max(_subtrahieren(_subtrahieren(fiktiv, ordentlich), eigen), _bruch(0))
            gesamt = _addieren(ordentlich, ergaenzung)
        wert = dict(ordentlicher_pflichtteilsbetrag=_bruchteile(ordentlich),
            erhoehter_pflichtteilswert_vor_anrechnung=_bruchteile(fiktiv),
            ergaenzungsbetrag_nach_eigengeschenk=_bruchteile(ergaenzung),
            gesamtbetrag_nach_eigengeschenk=_bruchteile(gesamt))
    ergebnis = _ergebnis(wert, 'EUR', 'BGB_PFLICHTTEILSERGAENZUNG_EIGENGESCHENK', eingaben,
        [dict(operation='Eigengeschenk zur fiktiven Masse addieren; ohne2315 nur Ergänzung mindern, mit2315 einmal Gesamtbetrag mindern und ordentlichen Pflichtteil gesondert abgrenzen')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if wert is not None else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Feste lokale BGB-Fassung; ein Eigengeschenk mit rechtlich identischem Wert für erforderliche Hinzurechnung und Anrechnung; Pflichtteilsgrundmodell ohne Ausgleichung oder andere Eigengeschenke.']
    ergebnis['hinweise'] = ['Eigengeschenkwert ist bereits rechtlich bewertet; keine automatische Anwendung der Drittschenkungs-Abschmelzung§2325 Absatz3 auf Eigengeschenke und keine Annahme, dass alte Eigengeschenke ohne Weiteres unberücksichtigt bleiben. Bei2315 muss einheitlicher Wert zugleich dessen Bewertung und der Bewertung nach2327 genügen; abweichende Werte oder Mischgeschenke außerhalb dieses Modells. Ohne2315 bleibt ordentlicher Pflichtteil von der Eigengeschenkanrechnung unberührt; negative Ergänzung erzeugt keine Rückzahlung. Mit2315 Geschenk nicht zuerst von Ergänzung und dann nochmals vom Gesamtbetrag abziehen. Ordentlicher Pflichtteil wird aus Nachlass plus2315-Geschenk berechnet und um dieses vermindert; fiktiver Gesamtbetrag umfasst Drittschenkungen und dasselbe Eigengeschenk genau einmal. Negative Nachlasswerte werden erst nach jeweils erforderlicher Hinzurechnung auf null begrenzt. Drittschenkungen enthalten das Eigengeschenk nicht und müssen bereits rechtlich bewertete, berücksichtigungsfähige Werte sein. §2327 Absatz2/§2051 Absatz1 bei Nachrücken gesondert; kein bloßes Geschenk an einen anderen Abkömmling als eigenes behandeln. Mehrhinterlassung2326, Ausgleichung2316, Erbenschutz2328, Beschenktenhaftung2329 und tatsächliche Zahlungserfüllung separat; kein abschließender Zahlungsanspruch.']
    return ergebnis
