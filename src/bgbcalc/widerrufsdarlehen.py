"""Zins- und Aufwendungsbetrag bei Verbraucherdarlehenswiderruf (§357b Absatz3)."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .zahlen import _addieren, _bruch, _multiplizieren
from .zinsen import _bruchteile, _zeitanteil


def widerruf_verbraucherdarlehen_betrag(
    darlehensbetrag=None, sollzinssatz_prozent=None, zeitanteil_zaehler=None,
    zeitanteil_nenner=None, zeitanteil_nachweis=None, immobiliar_verbraucherdarlehen=None,
    niedrigerer_gebrauchsvorteil_nachgewiesen=None, gebrauchsvorteil_betrag=None,
    nicht_rueckforderbare_oeffentliche_aufwendungen=None, widerruf_anwendbar=None,
):
    """Sollzinsbetrag, gegebenenfalls niedrigerer Gebrauchsvorteil, plus qualifizierte öffentliche Aufwendungen."""
    kapital = _geld(darlehensbetrag)
    zinssatz = _geld(sollzinssatz_prozent)
    anteil = _zeitanteil(zeitanteil_zaehler, zeitanteil_nenner, zeitanteil_nachweis)
    kosten = _geld(nicht_rueckforderbare_oeffentliche_aufwendungen)
    eingaben = dict(darlehensbetrag=darlehensbetrag, sollzinssatz_prozent=sollzinssatz_prozent,
        zeitanteil_zaehler=zeitanteil_zaehler, zeitanteil_nenner=zeitanteil_nenner,
        zeitanteil_nachweis=zeitanteil_nachweis, immobiliar_verbraucherdarlehen=immobiliar_verbraucherdarlehen,
        niedrigerer_gebrauchsvorteil_nachgewiesen=niedrigerer_gebrauchsvorteil_nachgewiesen,
        gebrauchsvorteil_betrag=gebrauchsvorteil_betrag,
        nicht_rueckforderbare_oeffentliche_aufwendungen=nicht_rueckforderbare_oeffentliche_aufwendungen,
        widerruf_anwendbar=widerruf_anwendbar)
    for name in ("immobiliar_verbraucherdarlehen", "niedrigerer_gebrauchsvorteil_nachgewiesen", "widerruf_anwendbar"):
        _wahrheitswert(eingaben[name], name)
    nutzen = None
    if gebrauchsvorteil_betrag is not None or (immobiliar_verbraucherdarlehen and niedrigerer_gebrauchsvorteil_nachgewiesen):
        nutzen = _geld(gebrauchsvorteil_betrag)
    ergebnis = _geld_ergebnis(None, "BGB_WIDERRUF_VERBRAUCHERDARLEHEN_BETRAG", eingaben,
        [dict(operation="Vertraglichen Sollzins über belegten Jahresanteil berechnen; bei Immobiliardarlehen nachgewiesenen niedrigeren Gebrauchsvorteil berücksichtigen; öffentliche Aufwendungen hinzufügen")])
    if widerruf_anwendbar:
        zins = _multiplizieren(_multiplizieren(kapital, _multiplizieren(zinssatz, _bruch(1, 100))), anteil)
        ersatz = min(zins, nutzen) if immobiliar_verbraucherdarlehen and niedrigerer_gebrauchsvorteil_nachgewiesen else zins
        ergebnis["wert"] = dict(vertraglicher_sollzinsbetrag=_bruchteile(zins),
            geschuldeter_nutzungsbetrag=_bruchteile(ersatz),
            oeffentliche_aufwendungen=_bruchteile(kosten), gesamtbetrag=_bruchteile(_addieren(ersatz, kosten)))
        ergebnis["status"] = "BERECHNET"
    ergebnis["hinweise"].append("Nur§357b Absatz3 für Verbraucherdarlehen mit nichtnegativem Sollzinssatz, konstanter Kapitalbasis und konstantem Satz im eingegebenen Abschnitt. Bei Änderungen getrennte Abschnitte bilden und öffentliche Aufwendungen nur einmal erfassen. Jahresanteil betrifft Auszahlung bis Rückzahlung nach belegter Zinskonvention, keine pauschale365-Tage-Annahme. Kapitalrückzahlung ist nicht im gesamtbetrag enthalten. Finanzierungshilfen und weitere Sondervorschriften separat.")
    return ergebnis
