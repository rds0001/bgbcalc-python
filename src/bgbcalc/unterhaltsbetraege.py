"""Native Unterschiedsbeträge des Familienrechts; Bewertungen sind qualifizierte Eingaben."""
from .betraege import _geld
from .kalender import _datum, _ergebnis, _fehler, _text
from .zahlen import _bruch, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile

def unterhalt_unterschiedsbetrag(voller_unterhalt=None, erwerbsdeckung=None, bewertungsnachweis=None):
    """Gesetzlicher Unterschiedsbetrag nach§1573II/IV2, mindestens null. Angemessenheit, Nachhaltigkeit, Anschlussunterhalt und Ausschluss konkurrierender Ansprüche vorqualifiziert; keine Bedarfsbemessung, Quotenmethode oder vollständige Unterhaltsprüfung."""
    links = _geld(voller_unterhalt)
    rechts = _geld(erwerbsdeckung)
    _text(bewertungsnachweis, "bewertungsnachweis")
    eingaben = dict(voller_unterhalt=voller_unterhalt, erwerbsdeckung=erwerbsdeckung, bewertungsnachweis=bewertungsnachweis)
    ergebnis = _ergebnis(_bruchteile(max(_subtrahieren(links, rechts), _bruch(0))), "EUR", "BGB_UNTERHALT_UNTERSCHIEDSBETRAG", eingaben, [dict(operation="Differenz der qualifizierten Beträge bilden und bei null begrenzen.")], eingaben.copy())
    ergebnis["hinweise"] = ["Gesetzlicher Unterschiedsbetrag nach§1573II/IV2, mindestens null. Angemessenheit, Nachhaltigkeit, Anschlussunterhalt und Ausschluss konkurrierender Ansprüche vorqualifiziert; keine Bedarfsbemessung, Quotenmethode oder vollständige Unterhaltsprüfung."]
    return ergebnis

def unterhalt_beerdigungskostenrest(beerdigungskosten=None, vom_erben_erlangbar=None, bewertungsnachweis=None):
    """§1615II: Kosten abzüglich vom Erben erlangbarem Betrag, mindestens null. Unterhaltspflicht und Umfang der Beerdigungskosten vorqualifiziert; keine automatische Erbenhaftungsprüfung."""
    links = _geld(beerdigungskosten)
    rechts = _geld(vom_erben_erlangbar)
    _text(bewertungsnachweis, "bewertungsnachweis")
    eingaben = dict(beerdigungskosten=beerdigungskosten, vom_erben_erlangbar=vom_erben_erlangbar, bewertungsnachweis=bewertungsnachweis)
    ergebnis = _ergebnis(_bruchteile(max(_subtrahieren(links, rechts), _bruch(0))), "EUR", "BGB_UNTERHALT_BEERDIGUNGSKOSTENREST", eingaben, [dict(operation="Differenz der qualifizierten Beträge bilden und bei null begrenzen.")], eingaben.copy())
    ergebnis["hinweise"] = ["§1615II: Kosten abzüglich vom Erben erlangbarem Betrag, mindestens null. Unterhaltspflicht und Umfang der Beerdigungskosten vorqualifiziert; keine automatische Erbenhaftungsprüfung."]
    return ergebnis

def ausstattung_schenkungsmehrbetrag(ausstattungswert=None, angemessenes_mass=None, bewertungsnachweis=None):
    """§1624I: Ausstattung über dem qualifizierten entsprechenden Maß, mindestens null. Ausstattungseigenschaft und Bewertung vorqualifiziert; keine selbst erfundene Vermögensquote."""
    links = _geld(ausstattungswert)
    rechts = _geld(angemessenes_mass)
    _text(bewertungsnachweis, "bewertungsnachweis")
    eingaben = dict(ausstattungswert=ausstattungswert, angemessenes_mass=angemessenes_mass, bewertungsnachweis=bewertungsnachweis)
    ergebnis = _ergebnis(_bruchteile(max(_subtrahieren(links, rechts), _bruch(0))), "EUR", "BGB_AUSSTATTUNG_SCHENKUNGSMEHRBETRAG", eingaben, [dict(operation="Differenz der qualifizierten Beträge bilden und bei null begrenzen.")], eingaben.copy())
    ergebnis["hinweise"] = ["§1624I: Ausstattung über dem qualifizierten entsprechenden Maß, mindestens null. Ausstattungseigenschaft und Bewertung vorqualifiziert; keine selbst erfundene Vermögensquote."]
    return ergebnis

def unterhalt_monatsgesamtbetrag(monatsbetrag=None, erster_voller_monat=None, beendigung_am=None, zeitraumnachweis=None):
    """Volle Monatsrenten bis einschließlich gesetzlichen Beendigungsmonat summieren."""
    betrag = _geld(monatsbetrag)
    anfang = _datum(erster_voller_monat, "erster_voller_monat")
    ende = _datum(beendigung_am, "beendigung_am")
    _text(zeitraumnachweis, "zeitraumnachweis")
    if anfang.day != 1:
        _fehler("erster_voller_monat", "Ersten Tag des ersten vollständig geschuldeten Monats vorgeben.")
    if ende < anfang:
        _fehler("beendigung_am", "Beendigung liegt vor dem ersten vollständig geschuldeten Monat.")
    monate = (ende.year - anfang.year) * 12 + ende.month - anfang.month + 1
    eingaben = dict(monatsbetrag=monatsbetrag, erster_voller_monat=erster_voller_monat, beendigung_am=beendigung_am, zeitraumnachweis=zeitraumnachweis)
    ergebnis = _ergebnis(dict(monatsanzahl=monate, gesamtbetrag=_bruchteile(_multiplizieren(betrag, _bruch(monate)))), "EUR", "BGB_UNTERHALT_MONATSGESAMTBETRAG", eingaben, [dict(operation="Kalendermonate einschließlich qualifiziertem Anfangs- und Endmonat zählen und mit konstantem vollem Monatsbetrag multiplizieren.")], eingaben.copy())
    ergebnis["hinweise"] = ["Konstanter qualifizierter voller Monatsbetrag und erster vollständig geschuldeter Monat. Letzter Monat ist rechtlich als voll geschuldeter Monat bestimmt: Tod nach§1361IV/1585I/1612III oder Wiederheirat nach§1585I, gegebenenfalls§1586II. Auch bei Beendigung am ersten oder letzten Tag zählt er voll. Keine tägliche Kürzung dieses Endmonats; kein automatischer voller Anfangsmonat bei erstmaliger Entstehung im Monatslauf. Abweichende Vereinbarungen/Bestimmungen nach§1612II und andere Endgründe nicht abgedeckt. Keine Ermittlung der Unterhaltshöhe, Zahlungsrückstände oder Fälligkeit an Bankarbeitstagen."]
    return ergebnis
