"""Aufwandspauschale je unvergüteter Betreuung (§1878 BGB)."""

from .betraege import _geld, _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler, _frist, _text
from .zahlen import _addieren, _bruch, _multiplizieren, _subtrahieren, _zahleneingabe
from .zinsen import _bruchteile


def betreuer_aufwandspauschale(
    hoechststundensatz=None,
    betreuungsjahr_beginn=None,
    amtsende_am=None,
    erhaltener_vorschuss=None,
    erhaltener_aufwendungsersatz=None,
    verhinderungsbetreuung=None,
    taetigkeitszeitanteil=None,
    pauschalenanspruch_qualifiziert=None,
    berechnungsnachweis=None,
):
    """18facher Satz, gegebenenfalls Monats-/Tätigkeitsanteil, abzüglich Vorschuss und Ersatz."""
    satz = _geld(hoechststundensatz)
    if satz <= 0:
        _fehler(
            "hoechststundensatz",
            "Positiver zeitlich maßgeblicher externer Höchststundensatz erforderlich.",
        )
    beginn = _datum(betreuungsjahr_beginn, "betreuungsjahr_beginn")
    jahresende = _frist(betreuungsjahr_beginn, 1, "jahre", "tagesbeginn")
    amtsende = None
    if amtsende_am is not None:
        amtsende = _datum(amtsende_am, "amtsende_am")
        if amtsende < beginn or amtsende > jahresende:
            _fehler(
                "amtsende_am",
                "Amtsende muss innerhalb des betrachteten Betreuungsjahres liegen.",
            )
    vorschuss = _geld(erhaltener_vorschuss)
    ersatz = _geld(erhaltener_aufwendungsersatz)
    _wahrheitswert(verhinderungsbetreuung, "verhinderungsbetreuung")
    _wahrheitswert(pauschalenanspruch_qualifiziert, "pauschalenanspruch_qualifiziert")
    _text(berechnungsnachweis, "berechnungsnachweis")
    taetigkeit = None
    if taetigkeitszeitanteil is not None:
        taetigkeit = _zahleneingabe(taetigkeitszeitanteil)
        if not 0 <= taetigkeit <= 1:
            _fehler(
                "taetigkeitszeitanteil",
                "Qualifizierter Anteil des Betreuungsjahres muss zwischen null und eins liegen.",
            )
    if verhinderungsbetreuung and taetigkeit is None:
        _fehler(
            "taetigkeitszeitanteil",
            "Für Verhinderungsbetreuung ist qualifizierter tatsächlicher Tätigkeitszeitanteil erforderlich.",
            "EINGABE_FEHLT",
        )
    if not verhinderungsbetreuung and taetigkeit is not None:
        _fehler(
            "taetigkeitszeitanteil",
            "Tätigkeitszeitanteil nur für Verhinderungsbetreuung vorgeben.",
        )
    eingaben = dict(
        hoechststundensatz=hoechststundensatz,
        betreuungsjahr_beginn=betreuungsjahr_beginn,
        amtsende_am=amtsende_am,
        erhaltener_vorschuss=erhaltener_vorschuss,
        erhaltener_aufwendungsersatz=erhaltener_aufwendungsersatz,
        verhinderungsbetreuung=verhinderungsbetreuung,
        taetigkeitszeitanteil=taetigkeitszeitanteil,
        pauschalenanspruch_qualifiziert=pauschalenanspruch_qualifiziert,
        berechnungsnachweis=berechnungsnachweis,
    )
    wert = None
    if pauschalenanspruch_qualifiziert:
        monate = None
        if verhinderungsbetreuung:
            anteil = taetigkeit
        else:
            monate = 12
            if amtsende is not None:
                monate = next(
                    n
                    for n in range(1, 13)
                    if amtsende
                    <= _frist(betreuungsjahr_beginn, n, "monate", "tagesbeginn")
                )
            anteil = _bruch(monate, 12)
        jahresbetrag = _multiplizieren(satz, _bruch(18))
        vor_abzug = _multiplizieren(jahresbetrag, anteil)
        abzuege = _addieren(vorschuss, ersatz)
        wert = dict(
            betreuungsjahr_ende=jahresende.isoformat(),
            beruecksichtigte_monate=monate,
            zeitanteil=_bruchteile(anteil),
            jahrespauschale=_bruchteile(jahresbetrag),
            pauschale_vor_abzug=_bruchteile(vor_abzug),
            erhaltener_gesamtbetrag=_bruchteile(abzuege),
            restpauschale=_bruchteile(
                max(_subtrahieren(vor_abzug, abzuege), _bruch(0))
            ),
        )
    ergebnis = _ergebnis(
        wert,
        "EUR",
        "BGB_BETREUER_AUFWANDSPAUSCHALE",
        eingaben,
        [
            dict(
                operation="18fachen externen Höchststundensatz mit Jahresanteil multiplizieren; bei Amtsende begonnene Betreuungsmonate voll zählen, erhaltenen Vorschuss/Ersatz abziehen, Rest mindestens null"
            )
        ],
        eingaben.copy(),
    )
    ergebnis["status"] = "BERECHNET" if wert is not None else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = [
        "Ein einzelnes rechtlich abgegrenztes Betreuungsjahr einer unvergüteten Betreuung und ein Betreuer; Jahresbeginn bezeichnet ersten mitgezählten Abrechnungstag. Externer zeitgültiger JVEG-Satz belegt."
    ]
    ergebnis["hinweise"] = [
        "Je Betreuung und Mitbetreuer gesondert berechnen; Pauschale nicht pauschal zwischen mehreren Betreuern teilen. Ohne Amtsende voller Jahresbetrag, keine Aussage über bereits eingetretene Fälligkeit. Jahresbeginn einschließlich erster/weiterer Betreuungsjahre und Amtswirksamkeit rechtlich bestimmen; Kalendermonate nicht automatisch Januar bis Dezember. Bei Amtsende zählt jeder angefangene Betreuungsmonat voll; keine tägliche Kürzung normaler Betreuung. Bei Verhinderungsbetreuung ist zeitanteilig tatsächlich abgedeckte Tätigkeit als qualifizierter Anteil des ganzen Betreuungsjahres vorzugeben, einschließlich rechtlich gebotener Monatsbehandlung bei Amtsende; dieser Anteil wird nicht nochmals mit Monatsquote multipliziert. Keine selbst erfundene Tagesdivisorregel für§1878 Absatz2. Vorschuss und Ersatz nur für dieselben erfassten Aufwendungen/Periode; übersteigender Empfang ergibt Rest0, keinen automatisch festgestellten Rückzahlungsanspruch. Satzänderungen innerhalb des Jahres und Übergangsrecht vorqualifizieren, nicht automatisch mitteln. Erlöschen nach Absatz4 und Antrag/Fälligkeit sind gesonderte Fristrechnung."
    ]
    return ergebnis


def betreuer_pauschalenfristen(bestellung_am=None, anspruchsentstehung_am=None):
    """Erstes Jahresfristende und sechsmonatige Erlöschensgrundfrist nach Entstehungsjahresende."""
    bestellung = _datum(bestellung_am, 'bestellung_am')
    entstehung = _datum(anspruchsentstehung_am, 'anspruchsentstehung_am')
    if entstehung < bestellung:
        _fehler('anspruchsentstehung_am', 'Anspruchsentstehung darf nicht vor Bestellung liegen.')
    erstende = _frist(bestellung_am, 1, 'jahre', 'ereignis')
    erloeschen = _frist(f'{entstehung.year:04d}-12-31', 6, 'monate', 'ereignis')
    eingaben = dict(bestellung_am=bestellung_am, anspruchsentstehung_am=anspruchsentstehung_am)
    ergebnis = _ergebnis(dict(erstes_jahresfristende=erstende.isoformat(), erloeschensgrundfristende=erloeschen.isoformat()),
        'daten', 'BGB_BETREUER_PAUSCHALENFRISTEN', eingaben,
        [dict(operation='Ein Jahr ab Bestellung; sechs Monate ab Ablauf des qualifizierten Anspruchsentstehungsjahres')], eingaben.copy())
    ergebnis['annahmen'] = ['Bestellung als Ereignis; tatsächlicher Anspruchsentstehungstag rechtlich bestimmt. Grundfristen ohne gesonderte Ablaufkorrektur.']
    ergebnis['hinweise'] = ['Erste Jahresfrist ab Bestellung, nicht Kalenderjahresende. Anspruchsentstehung kann bei vorherigem Amtsende vor erster Jahresfrist liegen und ist ausdrücklich vorgegeben. Erlöschensgrundfrist läuft sechs Monate nach Ende dieses Entstehungsjahres. Rechtzeitige gerichtliche Geltendmachung, Wirkung des Jahresberichts nach einmaligem ausdrücklichem Antrag, Verzicht, Zuständigkeit und etwaige§193-Verschiebung gesondert rechtlich prüfen; kein automatisches Erlöschensurteil. Anspruchsentstehung nach Satzänderungen/Übergangsrecht nicht automatisch bestimmt.']
    return ergebnis
