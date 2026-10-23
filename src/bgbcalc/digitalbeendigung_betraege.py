"""Exakte zeitanteilige Beendigungsbeträge für digitale Dauerbereitstellung."""
from .betraege import _geld
from .kalender import _text, _fehler, _ergebnis
from .zahlen import _addieren, _multiplizieren, _dividieren
from .zinsen import _bruchteile

def digitalbeendigung_zeitanteilige_betraege(vereinbarter_abschnittspreis=None, gezahlter_abschnittspreis=None, zeiteinheiten_gesamt=None, zeiteinheiten_mangelhaft=None, zeiteinheiten_nicht_mehr_zu_erbringen=None, einordnungsnachweis=None):
    """Disjunkte mangelhafte und künftig entfallende Zeiteinheiten addieren; durch Gesamtzeit teilen; Abschnittspreis und proportional zugeordneten Zahlungsbetrag mit Quote multiplizieren."""
    werte = [_geld(vereinbarter_abschnittspreis), _geld(gezahlter_abschnittspreis), _geld(zeiteinheiten_gesamt), _geld(zeiteinheiten_mangelhaft), _geld(zeiteinheiten_nicht_mehr_zu_erbringen)]
    _text(einordnungsnachweis, "einordnungsnachweis")
    preis, zahlung, gesamt, mangel, zukunft = werte
    entfall = _addieren(mangel, zukunft)
    if gesamt <= 0 or entfall > gesamt:
        _fehler("zeiteinheiten_gesamt", "Gesamtzeit muss positiv sein und die disjunkten Teilzeiten umfassen.")
    if zahlung > preis:
        _fehler("gezahlter_abschnittspreis", "Zahlung darf Abschnittspreis nicht übersteigen.")
    quote = _dividieren(entfall, gesamt)
    wert = dict(entfallender_zeitanteil=_bruchteile(quote), erloschener_preisanteil=_bruchteile(_multiplizieren(preis,quote)), erstattungsbetrag=_bruchteile(_multiplizieren(zahlung,quote)))
    eingaben = dict(vereinbarter_abschnittspreis=vereinbarter_abschnittspreis, gezahlter_abschnittspreis=gezahlter_abschnittspreis, zeiteinheiten_gesamt=zeiteinheiten_gesamt, zeiteinheiten_mangelhaft=zeiteinheiten_mangelhaft, zeiteinheiten_nicht_mehr_zu_erbringen=zeiteinheiten_nicht_mehr_zu_erbringen, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,"EUR_und_quote","BGB_DIGITALBEENDIGUNG_ZEITANTEILIGE_BETRAEGE",eingaben,[dict(operation='Disjunkte mangelhafte und künftig entfallende Zeiteinheiten addieren; durch Gesamtzeit teilen; Abschnittspreis und proportional zugeordneten Zahlungsbetrag mit Quote multiplizieren.')],eingaben.copy())
    ergebnis["hinweise"] = ['Nur wirksame Beendigung dauerhafter digitaler Bereitstellung nach §327o Absatz2/3. Ein homogen bepreister Abschnitt mit proportional über dessen Zeit verteilter Zahlung. Mangelhafte Zeit nur bereits erbrachte Leistungen, zukünftige Zeit nur nicht mehr geschuldete Leistungen; disjunkt, vollständig qualifiziert. Ungleich bepreiste oder anders bezahlte Zeitbereiche getrennt rechnen; überlappende Mangelintervalle zuvor vereinigen. Keine automatische Mangelbeurteilung, Vertragsbeendigung, Zahlungszuordnung, Berechnung von Wertersatz oder Frist. Ergebnis erloschener_preisanteil ist gesamter entfallener Preis einschließlich bereits bezahlten Teils, keine zusätzliche offene Forderung. Überzahlungen über Abschnittspreis gesondert behandeln.']
    return ergebnis
