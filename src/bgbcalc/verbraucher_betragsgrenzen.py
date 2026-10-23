"""Exakte feste EUR-Schwellen ausgewählter Verbrauchervertragsregeln."""
from .betraege import _geld
from .zahlen import _bruch
from .zinsen import _bruchteile
from .kalender import _auswahl, _ergebnis, _text
_FAELLE = {'sofortgeschaeft_kleinbetrag': (40, 'hoechstens', '§312 Absatz2 Nummer12: Entgelt im qualifizierten sofort erfüllten und bezahlten Außergeschäftsraumvertrag; nur Betragsmerkmal.'), 'einwendungsdurchgriff_mindestentgelt': (200, 'mindestens', '§359 Absatz2: finanziertes Entgelt mindestens200Euro vermeidet nur diesen Kleinbetragsausschluss; andere Ausschlüsse und Voraussetzungen separat.'), 'allgemeindarlehen_kleinbetrag': (200, 'weniger_als', '§491 Absatz2 Satz2 Nummer1: Nettodarlehensbetrag unter200Euro; kein allgemeiner Ausschluss aller Verbraucherschutzrechte.'), 'existenzgruendung_hoechstbetrag': (75000, 'hoechstens', '§513: Nettodarlehensbetrag oder Barzahlungspreis bis75000Euro; Existenzgründungszweck/natürliche Person und EU-Ausnahme separat qualifizieren.'), 'fehlende_sicherheitenangabe_ausnahme': (75000, 'mehr_als', '§494 Absatz6 Satz2: Allgemein-Verbraucherdarlehen mit Nettodarlehensbetrag über75000Euro; nur Betragsmerkmal der Ausnahme bei fehlender Sicherheitenangabe.'), 'reisesicherung_alternative_absicherung_umsatz': (10000000, 'weniger_als', '§651rII2: qualifizierter Umsatz im letzten abgeschlossenen Geschäftsjahr strikt unter10MillionenEUR; nur Zahlenvoraussetzung der alternativen Absicherung im folgenden Geschäftsjahr. Umsatzbegriff nachReisesicherungsfondsgesetz vorqualifiziert. Keine automatische Zulässigkeit eines Versicherers/Kreditinstituts.'), 'reisesicherung_einstandshoechstbetrag_umsatz': (3000000, 'weniger_als', '§651rIII3: qualifizierter Vorjahresumsatz strikt unter3MillionenEUR; nur Umsatzmerkmal einer zulässigen vereinbarten1Million-EUR-Grenze je Insolvenz bei Versicherer/Kreditinstitut. Kein automatischer Deckel oder Schadensbetrag; Reisesicherungsfonds und weitere Voraussetzungen gesondert.')}

def verbraucher_betragsschwelle(schwellenfall=None, massgeblicher_betrag=None, einordnungsnachweis=None):
    """Vergleicht den qualifizierten gesetzlichen Bezugsbetrag ohne automatische Rechtsfolgen."""
    _auswahl(schwellenfall, 'schwellenfall', tuple(_FAELLE))
    betrag = _geld(massgeblicher_betrag)
    _text(einordnungsnachweis, 'einordnungsnachweis')
    grenze, richtung, fallhinweis = _FAELLE[schwellenfall]
    grenze = _bruch(grenze)
    erfuellt = {'hoechstens': betrag <= grenze, 'mindestens': betrag >= grenze, 'weniger_als': betrag < grenze, 'mehr_als': betrag > grenze}[richtung]
    eingaben = dict(schwellenfall=schwellenfall, massgeblicher_betrag=massgeblicher_betrag, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(dict(gesetzlicher_grenzbetrag=_bruchteile(grenze), vergleichsrichtung=richtung, betragsmerkmal_erfuellt=erfuellt), 'eur_und_wahrheitswert', 'BGB_VERBRAUCHER_BETRAGSSCHWELLE', eingaben, [dict(operation='Exakten maßgeblichen EUR-Betrag mit gesetzlicher Schwelle und ausdrücklich fallbezogener Vergleichsrichtung vergleichen')], eingaben.copy())
    ergebnis['annahmen'] = ['Anwendungsbereich und maßgebliche gesetzliche Bezugsgröße einschließlich gegebenenfalls qualifiziertem Vorjahresumsatz rechtlich bestimmt; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['Nur numerische Teilprüfung; kein vollständiger Verbrauchervertrags-/Darlehens-/Einwendungs- oder Sicherheitenentscheid. Kein automatischer Anspruch auf den Grenzbetrag und keine Rundung vor dem Vergleich. Unterschiedliche gesetzliche Bezugsgrößen nicht durch Bruttozahlung oder Restschuld ersetzen.', fallhinweis]
    return ergebnis
