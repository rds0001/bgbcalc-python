"""Verjährungsvereinbarungsgrenze und hypothekarischer Zinserweiterungsrahmen."""
from .betraege import _geld
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _text
from .zahlen import _bruch, _subtrahieren
from .zinsen import _bruchteile


def verjaehrung_vereinbarungsobergrenze(gesetzlicher_verjaehrungsbeginn=None, vereinbartes_fristende=None, beginnart=None, einordnungsnachweis=None):
    """§202 Absatz2: vereinbarte Erschwerung höchstens30 Jahre ab gesetzlichem Beginn."""
    beginn = _datum(gesetzlicher_verjaehrungsbeginn, 'gesetzlicher_verjaehrungsbeginn')
    ende = _datum(vereinbartes_fristende, 'vereinbartes_fristende')
    _auswahl(beginnart, 'beginnart', ('ereignis', 'tagesbeginn'))
    _text(einordnungsnachweis, 'einordnungsnachweis')
    if ende < beginn:
        _fehler('vereinbartes_fristende', 'Vereinbartes Ende darf nicht vor dem angegebenen gesetzlichen Beginn liegen.')
    grenze = _frist(gesetzlicher_verjaehrungsbeginn, 30, 'jahre', beginnart)
    eingaben = dict(gesetzlicher_verjaehrungsbeginn=gesetzlicher_verjaehrungsbeginn,
        vereinbartes_fristende=vereinbartes_fristende, beginnart=beginnart, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(dict(dreissigjahres_vereinbarungsgrenze=grenze.isoformat(), vereinbartes_ende_innerhalb_grenze=ende <= grenze),
        'daten_und_wahrheitswerte', 'BGB_VERJAEHRUNG_VEREINBARUNGSOBERGRENZE', eingaben,
        [dict(operation='Gesetzlicher Verjährungsbeginn plus30 Jahre mit qualifizierter Beginnart; vereinbartes Ende darf Grenze nicht überschreiten')], eingaben.copy())
    ergebnis['annahmen'] = ['Gesetzlicher Beginn und Beginnart sowie vereinbartes Ende rechtlich qualifiziert; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['Nur quantitative Vereinbarungsgrenze§202 Absatz2, keine Aussage zur gesamten Wirksamkeit. Ausgangspunkt ist gesetzlicher Verjährungsbeginn, nicht Vertragsabschluss oder frei gewählter späterer Beginn. Bei Jahresschlussbeginn Schlussdatum mit Ereignisbeginn verwenden. Vorsatzhaftung darf nach Absatz1 nicht im Voraus erleichtert werden; das und andere zwingende Verbote gesondert prüfen. Zu langes vereinbartes Ende wird nicht automatisch gekürzt oder geheilt. Hemmung/Ablaufhemmung/Neubeginn und tatsächlicher Ablauf nicht aus dieser Vereinbarungsprüfung ableiten; keine allgemeine absolute30-Jahresgrenze aller Ansprüche behaupten.']
    return ergebnis


def hypothek_zinserweiterungsrahmen(bisheriger_zinssatz=None, vorgesehener_zinssatz=None, einordnungsnachweis=None):
    """§1119 Absatz1: numerischen Zinserweiterungsrahmen bis fünf Prozent prüfen."""
    bisher = _geld(bisheriger_zinssatz)
    neu = _geld(vorgesehener_zinssatz)
    _text(einordnungsnachweis, 'einordnungsnachweis')
    fuenf = _bruch(5)
    spielraum = _subtrahieren(fuenf, bisher) if bisher < fuenf else _bruch(0)
    eingaben = dict(bisheriger_zinssatz=bisheriger_zinssatz, vorgesehener_zinssatz=vorgesehener_zinssatz, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(dict(erweiterungsspielraum_prozentpunkte=_bruchteile(spielraum),
        zinssatz_wird_erhoeht=neu > bisher, erhoehung_innerhalb_fuenfprozentrahmen=bisher < neu <= fuenf),
        'prozentpunkte_und_wahrheitswerte', 'BGB_HYPOTHEK_ZINSERWEITERUNGSRAHMEN', eingaben,
        [dict(operation='Rest bis fünf Prozent=max(5 minus bisheriger Zinssatz,0); tatsächliche Erhöhung muss über bisherigem Satz und höchstens bei fünf Prozent liegen')], eingaben.copy())
    ergebnis['annahmen'] = ['Hypothekarisch gesicherte Forderung und konkrete Zinssätze rechtlich qualifiziert; Prozentwerte als Zahlen, etwa5 für5Prozent; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['Nur numerischer Rahmen§1119 Absatz1 für Erhöhung ohne Zustimmung gleich-/nachrangiger Berechtigter, keine vollständige Änderungswirksamkeit. Bisher unverzinslich als0 eingeben. Genau5Prozent ist Obergrenze, bei bisher5odermehr kein Spielraum für weitere Erhöhung aus dieser Norm. Unveränderter oder gesenkter Zinssatz ist keine hier geprüfte Erhöhung. Zinssatzänderung der Forderung, Einigung/Eintragung und sonstige Voraussetzungen separat. Kein gesetzlicher Zinssatzwechsel auf5Prozent und keine automatische Betrags- oder Zinseszinsberechnung.']
    return ergebnis
