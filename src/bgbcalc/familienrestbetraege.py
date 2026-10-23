"""Qualifizierte Restbeträge und Teilübergang im Familienrecht."""
from .betraege import _geld
from .kalender import _ergebnis, _text
from .zahlen import _addieren, _bruch, _subtrahieren
from .zinsen import _bruchteile


def zugewinnausgleich_sachanrechnungsrest(ausgleichsforderung=None, gerichtlicher_anrechnungsbetrag=None, anrechnungsnachweis=None):
    """§1383I: gerichtlich festgesetzte Sachanrechnung auf Ausgleichsforderung berücksichtigen."""
    forderung = _geld(ausgleichsforderung)
    sachbetrag = _geld(gerichtlicher_anrechnungsbetrag)
    _text(anrechnungsnachweis,'anrechnungsnachweis')
    eingaben = dict(ausgleichsforderung=ausgleichsforderung,gerichtlicher_anrechnungsbetrag=gerichtlicher_anrechnungsbetrag,anrechnungsnachweis=anrechnungsnachweis)
    ergebnis = _ergebnis(_bruchteile(max(_subtrahieren(forderung,sachbetrag),_bruch(0))),'EUR','BGB_ZUGEWINNAUSGLEICH_SACHANRECHNUNGSREST',eingaben,[dict(operation='Gerichtlich festgesetzten und rechtlich wirksam anzurechnenden Sachbetrag von Ausgleichsforderung abziehen; Rest mindestens null.')],eingaben.copy())
    ergebnis['hinweise'] = ['Nur§1383I-Anrechnungsrechnung: Ausgleichsforderung bereits bestimmt, Anrechnungsbetrag gerichtlich festgesetzt und seine tatsächliche Anrechnungsvoraussetzung qualifiziert. Keinen Marktwert anstelle des festgesetzten Betrags einsetzen. Ob Anordnung/Übertragung/Erfüllung wirksam ist und wann anzurechnen ist, nicht automatisch entschieden. Übersteigt Anrechnungsbetrag die betrachtete Forderung, Rest0; kein automatisch festgestellter Überschuss-/Rückzahlungsanspruch. Keine erneute Zugewinn-, Sachwert- oder Billigkeitsbewertung.']
    return ergebnis


def minderjaehrigen_unterhaltsfehlbetrag(unterhaltsbedarf=None, anrechenbare_vermoegenseinkuenfte=None, anrechenbarer_arbeitsertrag=None, bewertungsnachweis=None):
    """§1602II: Bedarf nach qualifizierten Einkünften decken, Vermögensstamm nicht einbeziehen."""
    bedarf = _geld(unterhaltsbedarf)
    vermoegensertrag = _geld(anrechenbare_vermoegenseinkuenfte)
    arbeit = _geld(anrechenbarer_arbeitsertrag)
    _text(bewertungsnachweis,'bewertungsnachweis')
    deckung = _addieren(vermoegensertrag,arbeit)
    eingaben = dict(unterhaltsbedarf=unterhaltsbedarf,anrechenbare_vermoegenseinkuenfte=anrechenbare_vermoegenseinkuenfte,anrechenbarer_arbeitsertrag=anrechenbarer_arbeitsertrag,bewertungsnachweis=bewertungsnachweis)
    ergebnis = _ergebnis(_bruchteile(max(_subtrahieren(bedarf,deckung),_bruch(0))),'EUR','BGB_MINDERJAEHRIGEN_UNTERHALTSFEHLBETRAG',eingaben,[dict(operation='Qualifizierte anrechenbare Vermögenseinkünfte und Arbeitserträge addieren, vom Unterhaltsbedarf abziehen, Fehlbetrag mindestens null.')],eingaben.copy())
    ergebnis['hinweise'] = ['§1602II im Verhältnis des minderjährigen Kindes zu seinen Eltern. Bedürftigkeitsrest, kein abschließender Zahlungsanspruch gegen einzelne Elternteile. Kindesalter, Bedarf, Anrechenbarkeit und identischer Zeitraum rechtlich qualifiziert; Einkünfte nicht ungeprüft brutto einsetzen. Vermögensstamm wird nicht verbraucht und ist keine Eingabe. Rang, Leistungsfähigkeit, Kindergeldbehandlung, weitere Deckungsmittel, Naturalunterhalt und Elternverteilung gesondert und ohne Doppelanrechnung. Nicht ungeprüft auf volljährige Kinder übertragen.']
    return ergebnis


def betreuer_staatskassen_anspruchsuebergang(bestehender_betreueranspruch=None, staatskassenbefriedigung=None, zuordnungsnachweis=None):
    """§1881Satz1: Teilübergang des qualifizierten Anspruchs im Umfang der Staatskassenbefriedigung."""
    anspruch = _geld(bestehender_betreueranspruch)
    zahlung = _geld(staatskassenbefriedigung)
    _text(zuordnungsnachweis,'zuordnungsnachweis')
    uebergang = min(anspruch,zahlung)
    eingaben = dict(bestehender_betreueranspruch=bestehender_betreueranspruch,staatskassenbefriedigung=staatskassenbefriedigung,zuordnungsnachweis=zuordnungsnachweis)
    ergebnis = _ergebnis(dict(uebergegangener_anspruch=_bruchteile(uebergang),verbleibender_betreueranspruch=_bruchteile(_subtrahieren(anspruch,uebergang))),'EUR','BGB_BETREUER_STAATSKASSEN_ANSPRUCHSUEBERGANG',eingaben,[dict(operation='Bestehenden Betreueranspruch höchstens im Umfang zugeordneter Staatskassenbefriedigung übergehen lassen; verbleibenden Anspruch ausweisen.')],eingaben.copy())
    ergebnis['hinweise'] = ['§1881Satz1, ein rechtlich abgegrenzter bestehender Anspruch des Betreuers gegen den Betreuten unmittelbar vor der betrachteten Befriedigung. Zugeordnete Zahlung der Staatskasse für denselben Anspruch; frühere Zahlungen/Übergänge nicht nochmals einrechnen. Überschießende Zahlung erzeugt keinen zusätzlichen Anspruch gegen den Betreuten und keinen automatisch festgestellten Rückzahlungsanspruch. Entstehung/Höhe des Betreueranspruchs und Mittellosigkeit nicht geprüft. Die Erbenhaftung nachSatz2 wird in dieser Funktion nicht berechnet. Der separate Baustein betreuer_erbenhaftungsbetrag berechnet den BGB-Nachlasswertdeckel; externe102III/IV-SGB-XII-Ausnahmen bleiben ausdrücklich rechtlich vorzuqualifizieren.']
    return ergebnis
