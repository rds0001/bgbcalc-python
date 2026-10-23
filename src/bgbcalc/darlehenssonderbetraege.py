"""Kauf-, Wiederkauf- und Vorkauf-Sonderbeträge mit qualifizierten Werten."""
from .betraege import _geld, _geld_ergebnis
from .kalender import _text, _fehler
from .zahlen import _addieren, _subtrahieren, _multiplizieren, _dividieren, _bruch


def darlehen_wertbeteiligungsbetrag(immobilienwert_bei_rueckzahlung=None, vertraglicher_wertanteil=None, einordnungsnachweis=None):
    """Qualifizierten Immobilienwert bei Rückzahlung mit vertraglich festgelegter Wertbeteiligungsquote multiplizieren."""
    werte = [_geld(immobilienwert_bei_rueckzahlung), _geld(vertraglicher_wertanteil)]
    _text(einordnungsnachweis, 'einordnungsnachweis')
    eingaben = dict(immobilienwert_bei_rueckzahlung=immobilienwert_bei_rueckzahlung, vertraglicher_wertanteil=vertraglicher_wertanteil, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(_multiplizieren(werte[0],werte[1]), 'BGB_DARLEHEN_WERTBETEILIGUNGSBETRAG', eingaben, [dict(operation='Qualifizierten Immobilienwert bei Rückzahlung mit vertraglich festgelegter Wertbeteiligungsquote multiplizieren')])
    ergebnis['hinweise'].append('Nur Wertbeteiligungsdarlehen im Sinne §492b Absatz1 Nummer3. Immobilienwert für den maßgeblichen Rückzahlungszeitpunkt und vertraglichen Umfang extern bewerten; Quote als Jahres-unabhängiger Anteil (0.2=20Prozent), kein Zinssatz. Keine Bestimmung der Zulässigkeit des Kopplungsgeschäfts oder automatisches Hinzufügen einer ursprünglichen Darlehenssumme. Mehrere Rückzahlungen nach jeweils rechtlich bestimmtem Anteil/Umfang separat, keine Doppelzählung.')
    return ergebnis


def darlehensvermittlung_auslagenobergrenze(entstandene_erforderliche_auslagen=None, vorab_mitgeteilter_hoechstbetrag=None, einordnungsnachweis=None):
    """Qualifiziert vereinbarte entstandene erforderliche Vermittlerauslagen auf vorab mitgeteilten Höchstbetrag begrenzen."""
    werte = [_geld(entstandene_erforderliche_auslagen), _geld(vorab_mitgeteilter_hoechstbetrag)]
    _text(einordnungsnachweis, 'einordnungsnachweis')
    eingaben = dict(entstandene_erforderliche_auslagen=entstandene_erforderliche_auslagen, vorab_mitgeteilter_hoechstbetrag=vorab_mitgeteilter_hoechstbetrag, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(min(werte), 'BGB_DARLEHENSVERMITTLUNG_AUSLAGENOBERGRENZE', eingaben, [dict(operation='Qualifiziert vereinbarte entstandene erforderliche Vermittlerauslagen auf vorab mitgeteilten Höchstbetrag begrenzen')])
    ergebnis['hinweise'].append('Nur §655d Satz2/3: wirksame Vereinbarung über tatsächlich entstandene erforderliche Auslagen vorausgesetzt; nicht Maklervergütung oder Beratungsentgelt. Mitgeteilte Höhe/Höchstgrenze rechtlich bestimmen; bei getrennten Einzelkategorien jede passende Grenze separat anwenden, kein Austausch ungenutzter Grenzen ohne Rechtsgrundlage. Keine automatische Erforderlichkeits- oder Anspruchsprüfung.')
    return ergebnis


def teilzahlung_gesamtbetragskorrektur(vertraglicher_gesamtbetrag=None, angegebener_effektiver_jahreszins=None, tatsaechlicher_effektiver_jahreszins=None, einordnungsnachweis=None):
    """Gesamtbetrag mit eins minus der absoluten Effektivzins-Unterangabe als Zinsquote multiplizieren."""
    werte = [_geld(vertraglicher_gesamtbetrag), _geld(angegebener_effektiver_jahreszins), _geld(tatsaechlicher_effektiver_jahreszins)]
    _text(einordnungsnachweis, 'einordnungsnachweis')
    differenz = _subtrahieren(werte[2],werte[1])
    if not 0 <= differenz <= 1:
        _fehler('effektivzins_unterangabe','Korrekturdomäne verlangt Effektivzins-Unterangabe zwischen null und eins als Zinsquote.')
    eingaben = dict(vertraglicher_gesamtbetrag=vertraglicher_gesamtbetrag, angegebener_effektiver_jahreszins=angegebener_effektiver_jahreszins, tatsaechlicher_effektiver_jahreszins=tatsaechlicher_effektiver_jahreszins, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(_multiplizieren(werte[0],_subtrahieren(_bruch(1),_subtrahieren(werte[2],werte[1]))), 'BGB_TEILZAHLUNG_GESAMTBETRAGSKORREKTUR', eingaben, [dict(operation='Gesamtbetrag mit eins minus der absoluten Effektivzins-Unterangabe als Zinsquote multiplizieren')])
    ergebnis['hinweise'].append('Nur §507 Absatz2 letzter Satz bei qualifiziertem Teilzahlungsgeschäft und zu niedrig angegebenem Effektivzins. Eingaben als Jahresquoten,0.05=5Prozent. Beispielsweise Unterangabe8%-6%=2Prozentpunkte vermindert Gesamtbetrag um2Prozent. Nicht §494III-Sollzinskorrektur; nicht fehlende Zins-/Gesamtbetragsangabe. Sichere Rechendomäne: Unterangabe zwischen0und1 einschließlich; größere Differenzen erfordern gesonderte rechtliche Behandlung und werden nicht automatisch zu negativem Zahlungsanspruch. Tatsächlicher Effektivzins/Vertragsgesamtbetrag extern bestimmen; keine automatische Ratenneuberechnung.')
    return ergebnis
