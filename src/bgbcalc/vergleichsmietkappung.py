"""Betragsrahmen der Vergleichsmietenerhöhung ohne Sonderausnahme/Drittmittel."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _text
from .zahlen import _addieren, _bruch, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile


def vergleichsmiete_kappungsrahmen(
    ausgangsmiete_drei_jahre=None, nicht_anzurechnende_erhoehungen=None,
    derzeitige_monatsmiete=None, ortsuebliche_vergleichsmiete=None,
    gueltige_fuenfzehnprozent_verordnung=None, ausgleichszahlungsausnahme=None,
    drittmittelabzug_erforderlich=None, vergleichsmietregel_anwendbar=None, mietnachweis=None,
):
    """§558 Absatz1/3: Vergleichsmiete und20-/15-Prozent-Grenze im regulären Betragsfall verbinden."""
    basis = _geld(ausgangsmiete_drei_jahre)
    ausgenommen = _geld(nicht_anzurechnende_erhoehungen)
    bisher = _geld(derzeitige_monatsmiete)
    vergleich = _geld(ortsuebliche_vergleichsmiete)
    eingaben = dict(ausgangsmiete_drei_jahre=ausgangsmiete_drei_jahre,
        nicht_anzurechnende_erhoehungen=nicht_anzurechnende_erhoehungen,
        derzeitige_monatsmiete=derzeitige_monatsmiete, ortsuebliche_vergleichsmiete=ortsuebliche_vergleichsmiete,
        gueltige_fuenfzehnprozent_verordnung=gueltige_fuenfzehnprozent_verordnung,
        ausgleichszahlungsausnahme=ausgleichszahlungsausnahme, drittmittelabzug_erforderlich=drittmittelabzug_erforderlich,
        vergleichsmietregel_anwendbar=vergleichsmietregel_anwendbar, mietnachweis=mietnachweis)
    for name in tuple(eingaben)[4:-1]:
        _wahrheitswert(eingaben[name], name)
    _text(mietnachweis, "mietnachweis")
    gilt = vergleichsmietregel_anwendbar and not ausgleichszahlungsausnahme and not drittmittelabzug_erforderlich
    ergebnis = _geld_ergebnis(None, "BGB_VERGLEICHSMIETE_KAPPUNGSRAHMEN", eingaben,
        [dict(operation="Dreijahres-Ausgangsmiete um20 oder15Prozent erhöhen, nicht anzurechnende Erhöhungen hinzufügen und durch Vergleichsmiete begrenzen")])
    if gilt:
        prozent = 15 if gueltige_fuenfzehnprozent_verordnung else 20
        kappung = _addieren(_multiplizieren(basis, _bruch(100 + prozent, 100)), ausgenommen)
        obergrenze = min(kappung, vergleich)
        spielraum = max(_subtrahieren(obergrenze, bisher), _bruch(0))
        ergebnis["wert"] = dict(kappungsgrenze_prozent=prozent, kappungsbetrag_monatlich=_bruchteile(kappung),
            obergrenze_monatlich=_bruchteile(obergrenze), maximaler_erhoehungsbetrag=_bruchteile(spielraum),
            miete_nach_maximaler_erhoehung=_bruchteile(_addieren(bisher, spielraum)))
        ergebnis["status"] = "BERECHNET"
    ergebnis["hinweise"].append("Nur regulärer Betragsrahmen ohne Ausnahme§558 Absatz4 und ohne DrittmittelabzugAbsatz5. Drei-Jahres-Ausgangsmiete, Veränderungen und ausgeschlossene Erhöhungen rechtlich konsistent bestimmen; Modernisierungsbeträge nicht zugleich in die Ausgangsmiete einrechnen und addieren. Gültigkeit der örtlichen15Prozent-Verordnung ist Nutzervorgabe. Zeitvoraussetzungen, formgerechtes Verlangen, Zustimmung und Sonderregime separat. Kein automatischer Senkungsanspruch bei bereits höherer Bestandsmiete.")
    return ergebnis
