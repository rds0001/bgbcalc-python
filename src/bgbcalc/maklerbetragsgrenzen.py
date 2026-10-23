"""Kauf-, Wiederkauf- und Vorkauf-Sonderbeträge mit qualifizierten Werten."""
from .betraege import _geld, _geld_ergebnis
from .kalender import _text, _fehler
from .zahlen import _addieren, _subtrahieren, _multiplizieren, _dividieren, _bruch


def makler_anderer_partei_hoechstbelastung(qualifizierter_gesamtmaklerlohn=None, einordnungsnachweis=None):
    """Gesamtmaklerlohn durch zwei teilen als maximale auf andere Vertragspartei abwälzbare Belastung."""
    werte = [_geld(qualifizierter_gesamtmaklerlohn)]
    _text(einordnungsnachweis, 'einordnungsnachweis')
    eingaben = dict(qualifizierter_gesamtmaklerlohn=qualifizierter_gesamtmaklerlohn, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(_multiplizieren(werte[0],_bruch(1,2)), 'BGB_MAKLER_ANDERER_PARTEI_HOECHSTBELASTUNG', eingaben, [dict(operation='Gesamtmaklerlohn durch zwei teilen als maximale auf andere Vertragspartei abwälzbare Belastung')])
    ergebnis['hinweise'].append('Nur §656d bei einem Maklervertrag mit einer Partei eines Wohnungs-/Einfamilienhauskaufs und Verbrauchereigenschaft des Käufers nach §656b. Gesamtmaklerlohn ist die rechtlich wirksame einheitliche Kostenbasis beider Parteien nach qualifizierten Ermäßigungen/Erlassen; keine Zusammenzählung zusätzlicher identischer Forderungen. Ergebnis nur Belastungsobergrenze; überschreitende Vereinbarung wird nicht automatisch auf Hälfte reduziert. Fälligkeit verlangt Zahlung und Nachweis nach Satz2; kein automatischer Fälligkeitseintritt.')
    return ergebnis


def makler_gleichwirkender_erlass_restbetrag(bisheriger_gleicher_maklerlohn_je_partei=None, qualifizierter_erlassbetrag=None, einordnungsnachweis=None):
    """Von bisherigem gleichen Maklerlohn je Partei den qualifizierten gleichwirkenden Erlassbetrag abziehen."""
    werte = [_geld(bisheriger_gleicher_maklerlohn_je_partei), _geld(qualifizierter_erlassbetrag)]
    _text(einordnungsnachweis, 'einordnungsnachweis')
    if werte[1] > werte[0]:
        _fehler('qualifizierter_erlassbetrag', 'Erlassbetrag darf bisherigen gleichen Maklerlohn je Partei nicht übersteigen.')
    eingaben = dict(bisheriger_gleicher_maklerlohn_je_partei=bisheriger_gleicher_maklerlohn_je_partei, qualifizierter_erlassbetrag=qualifizierter_erlassbetrag, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(_subtrahieren(werte[0],werte[1]), 'BGB_MAKLER_GLEICHWIRKENDER_ERLASS_RESTBETRAG', eingaben, [dict(operation='Von bisherigem gleichen Maklerlohn je Partei den qualifizierten gleichwirkenden Erlassbetrag abziehen')])
    ergebnis['hinweise'].append('Nur §656c Absatz1 Satz3/4 bei zuvor wirksam gleich hohen Maklerlohnpflichten beider Parteien und Verbraucher-Käufer nach §656b; erlassene Geldsumme wirkt spiegelbildlich auf jeweils gleiche Pflicht. Erlassbetrag höchstens ursprünglicher je-Partei-Betrag. Bei verschiedenen/mehrfachen Erlassen deren rechtliche Wechselwirkung zuerst qualifizieren, nicht mehrfach denselben Erlass abziehen. Keine Heilung anfänglich ungleicher/unwirksamer Verpflichtungen; keine automatische Erstattung bereits gezahlter Provisionen. Entsprechende Anwendung nach §656d Absatz2 nur bei fachlich qualifizierter gleichartiger Berechnungsbasis.')
    return ergebnis
