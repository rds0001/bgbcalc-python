"""Interne exakte Bruchrechnung mit gemeinsamem Python-/R-Wertebereich."""
from fractions import Fraction
from math import gcd
import re

from .kalender import _fehler, _ganzzahl, _text, _auswahl

GRENZE = 9007199254740991


def _begrenzt(wert):
    if abs(wert) > GRENZE:
        _fehler("zahl", "Exakter gemeinsamer Zahlenbereich überschritten.")
    return wert


def _bruch(zaehler, nenner=1):
    _ganzzahl(zaehler, "zaehler", -GRENZE, GRENZE)
    _ganzzahl(nenner, "nenner", -GRENZE, GRENZE)
    if nenner == 0:
        _fehler("nenner", "Nenner darf nicht null sein.")
    return Fraction(zaehler, nenner)


def _pruefe_bruch(wert):
    if not isinstance(wert, Fraction):
        _fehler("zahl", "Interne rationale Zahl erforderlich.")
    _begrenzt(wert.numerator)
    _begrenzt(wert.denominator)
    return wert


def _zahleneingabe(wert):
    """Dezimaltext oder serialisiertes exaktes Ergebnis ohne Rundung einlesen."""
    if not isinstance(wert, dict):
        return _dezimalzahl(wert)
    if set(wert) != {"zaehler", "nenner"}:
        _fehler("zahl", "Bruchobjekt benötigt genau zaehler und nenner.")
    ganzzahlen = []
    for parameter in ("zaehler", "nenner"):
        text = _text(wert[parameter], parameter)
        muster = r"(?:0|-?[1-9][0-9]*)" if parameter == "zaehler" else r"[1-9][0-9]*"
        if len(text.lstrip("-")) > 16 or not re.fullmatch(muster, text):
            _fehler(parameter, "Kanonische Ganzzahlzeichenfolge erforderlich; Nenner positiv.")
        ganzzahlen.append(_begrenzt(int(text)))
    return _bruch(*ganzzahlen)


def _dezimalzahl(wert):
    _text(wert, "dezimalzahl")
    if not re.fullmatch(r"[+-]?[0-9]+(?:\.[0-9]+)?", wert):
        _fehler("dezimalzahl", "Dezimalzeichenfolge ohne Exponent oder Trenner erforderlich.")
    negativ = wert.startswith("-")
    teile = wert.lstrip("+-").split(".")
    nachkomma = teile[1].rstrip("0") if len(teile) == 2 else ""
    if len(nachkomma) > 15:
        _fehler("dezimalzahl", "Höchstens 15 erhebliche Nachkommastellen erlaubt.")
    zaehler = 0
    for ziffer in teile[0] + nachkomma:
        zaehler = _begrenzt(zaehler * 10 + int(ziffer))
    return _bruch(-zaehler if negativ else zaehler, 10 ** len(nachkomma))


def _addieren(links, rechts):
    _pruefe_bruch(links)
    _pruefe_bruch(rechts)
    teiler = gcd(links.denominator, rechts.denominator)
    linksfaktor = rechts.denominator // teiler
    rechtsfaktor = links.denominator // teiler
    zaehler = _begrenzt(_begrenzt(links.numerator * linksfaktor) +
                       _begrenzt(rechts.numerator * rechtsfaktor))
    nenner = _begrenzt(links.denominator * linksfaktor)
    return _bruch(zaehler, nenner)


def _subtrahieren(links, rechts):
    _pruefe_bruch(rechts)
    return _addieren(links, -rechts)


def _multiplizieren(links, rechts):
    _pruefe_bruch(links)
    _pruefe_bruch(rechts)
    teiler_links = gcd(abs(links.numerator), rechts.denominator)
    teiler_rechts = gcd(abs(rechts.numerator), links.denominator)
    return _bruch(
        _begrenzt((links.numerator // teiler_links) * (rechts.numerator // teiler_rechts)),
        _begrenzt((links.denominator // teiler_rechts) * (rechts.denominator // teiler_links)),
    )


def _dividieren(links, rechts):
    _pruefe_bruch(rechts)
    if rechts == 0:
        _fehler("divisor", "Division durch null.")
    return _multiplizieren(links, _bruch(rechts.denominator, rechts.numerator))


def _vergleichen(links, rechts):
    _pruefe_bruch(links)
    _pruefe_bruch(rechts)
    # Fraction vergleicht beliebig große Integer; keine Gleitkommakonvertierung.
    return (links > rechts) - (links < rechts)


def _bruchtext(wert):
    _pruefe_bruch(wert)
    return f"{wert.numerator}/{wert.denominator}"


def _runden(wert, stellen, modus):
    _pruefe_bruch(wert)
    _ganzzahl(stellen, "stellen", 0, 15)
    _auswahl(modus, "modus", ("gegen_null", "ab", "auf", "kaufmaennisch", "gerade"))
    skaliert = _multiplizieren(wert, _bruch(10 ** stellen))
    ganz, rest = divmod(abs(skaliert.numerator), skaliert.denominator)
    negativ = skaliert < 0
    erhoehen = (
        (modus == "ab" and negativ and rest > 0) or
        (modus == "auf" and not negativ and rest > 0) or
        (modus == "kaufmaennisch" and rest >= skaliert.denominator - rest) or
        (modus == "gerade" and (rest > skaliert.denominator - rest or
                               (rest == skaliert.denominator - rest and ganz % 2 == 1)))
    )
    ganz = _begrenzt(ganz + int(erhoehen))
    ziffern = str(ganz).rjust(stellen + 1, "0")
    if stellen:
        ziffern = ziffern[:-stellen] + "." + ziffern[-stellen:]
    return ("-" if negativ and ganz != 0 else "") + ziffern
