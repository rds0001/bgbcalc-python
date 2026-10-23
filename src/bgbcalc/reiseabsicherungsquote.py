"""Kauf-, Wiederkauf- und Vorkauf-Sonderbeträge mit qualifizierten Werten."""
from .betraege import _geld, _geld_ergebnis
from .kalender import _text, _fehler
from .zahlen import _addieren, _subtrahieren, _multiplizieren, _dividieren, _bruch


def pauschalreise_absicherungsanteil(eigener_leistungsanspruch=None, gesamtleistungsansprueche=None, jahresumsatz_veranstalter=None, einordnungsnachweis=None):
    """Im qualifiziert vereinbarten Ein-Million-Euro-Deckelfall Einzelanspruch mit min(1, eine Million Euro geteilt durch Gesamtleistungsansprüche) multiplizieren."""
    werte = [_geld(eigener_leistungsanspruch), _geld(gesamtleistungsansprueche), _geld(jahresumsatz_veranstalter)]
    _text(einordnungsnachweis, 'einordnungsnachweis')
    if werte[0] > werte[1]:
        _fehler('gesamtleistungsansprueche', 'Gesamtansprüche müssen mindestens dem Einzelanspruch entsprechen.')
    if werte[2] >= 3000000:
        _fehler('jahresumsatz_veranstalter', 'Dieser Deckelfall verlangt Vorjahresumsatz unter drei Millionen EUR.')
    eingaben = dict(eigener_leistungsanspruch=eigener_leistungsanspruch, gesamtleistungsansprueche=gesamtleistungsansprueche, jahresumsatz_veranstalter=jahresumsatz_veranstalter, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(_bruch(0) if werte[1]==0 else _multiplizieren(werte[0],min(_bruch(1),_dividieren(_bruch(1000000),werte[1]))), 'BGB_PAUSCHALREISE_ABSICHERUNGSANTEIL', eingaben, [dict(operation='Im qualifiziert vereinbarten Ein-Million-Euro-Deckelfall Einzelanspruch mit min(1, eine Million Euro geteilt durch Gesamtleistungsansprüche) multiplizieren')])
    ergebnis['hinweise'].append('Nur §651r Absatz3 Satz3/4: qualifiziert wirksam vereinbarte Begrenzung auf genau eine Million EUR je Insolvenz bei Versicherer oder Kreditinstitut nach Absatz2 Satz2 und Vorjahresumsatz strikt unter drei Millionen EUR. Kein Deckel für Reisesicherungsfonds; größere freiwillige Deckungsgrenzen separat qualifizieren. Eigener und Gesamtanspruch betreffen denselben vollständigen Insolvenz-Leistungskreis nach Absatz1, nicht nur die gerade bekannten Anmeldungen; keine Doppelzählung. Gesamtanspruch mindestens Einzelanspruch. Null Gesamtansprüche ergeben null. Keine Bestimmung des versicherten Schadens oder Prüfung der Insolvenz.')
    return ergebnis
