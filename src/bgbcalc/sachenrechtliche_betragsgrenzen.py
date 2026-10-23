"""Eingetragene Wertgrenzen und Edelmetall-Mindestpreis (§§882/1190/1240)."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _ergebnis, _text
from .zahlen import _addieren, _subtrahieren
from .zinsen import _bruchteile


def grundbuch_wertersatzgrenze(wertersatz=None, eingetragener_hoechstbetrag=None, hoechstbetrag_wirksam_bestimmt=None, bewertungsnachweis=None):
    """§882: Wertersatz auf wirksam eingetragenen Höchstbetrag begrenzen."""
    ersatz = _geld(wertersatz)
    grenze = _geld(eingetragener_hoechstbetrag)
    _wahrheitswert(hoechstbetrag_wirksam_bestimmt, 'hoechstbetrag_wirksam_bestimmt')
    _text(bewertungsnachweis, 'bewertungsnachweis')
    eingaben = dict(wertersatz=wertersatz, eingetragener_hoechstbetrag=eingetragener_hoechstbetrag,
        hoechstbetrag_wirksam_bestimmt=hoechstbetrag_wirksam_bestimmt, bewertungsnachweis=bewertungsnachweis)
    ergebnis = _geld_ergebnis(min(ersatz, grenze) if hoechstbetrag_wirksam_bestimmt else None,
        'BGB_GRUNDBUCH_WERTERSATZGRENZE', eingaben,
        [dict(operation='Qualifizierten Wertersatz auf wirksam eingetragenen Höchstbetrag begrenzen')])
    ergebnis['hinweise'].append('Nur Recht mit Wertersatz aus Versteigerungserlös bei Erlöschen durch Zuschlag im Sinne§882. Wertersatz nach einschlägigen Versteigerungsvorschriften ist qualifizierte Eingabe. Eingetragene Obergrenze schafft keinen Zahlungsanspruch in voller Grenzhöhe. Kein Verteilungsplan und keine Berechnung der Erlösdeckung oder Rangfolge.')
    return ergebnis


def hoechstbetragshypothek_forderung_und_zinsen(hauptforderung=None, zinsen=None, eingetragener_hoechstbetrag=None, hoechstbetragshypothek_anwendbar=None, einordnungsnachweis=None):
    """§1190 Absatz2: Zinsen in den Höchstbetrag einrechnen, nicht darüber aufschlagen."""
    haupt = _geld(hauptforderung)
    zins = _geld(zinsen)
    grenze = _geld(eingetragener_hoechstbetrag)
    _wahrheitswert(hoechstbetragshypothek_anwendbar, 'hoechstbetragshypothek_anwendbar')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    summe = _addieren(haupt, zins)
    gesichert = min(summe, grenze)
    eingaben = dict(hauptforderung=hauptforderung, zinsen=zinsen, eingetragener_hoechstbetrag=eingetragener_hoechstbetrag,
        hoechstbetragshypothek_anwendbar=hoechstbetragshypothek_anwendbar, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(dict(forderung_mit_zinsen=_bruchteile(summe), durch_hoechstbetrag_erfasster_betrag=_bruchteile(gesichert),
        nicht_vom_hoechstbetrag_erfasster_anteil=_bruchteile(_subtrahieren(summe, gesichert))) if hoechstbetragshypothek_anwendbar else None,
        'EUR', 'BGB_HOECHSTBETRAGSHYPOTHEK_FORDERUNG_UND_ZINSEN', eingaben,
        [dict(operation='Hauptforderung und Zinsen addieren, gemeinsame Summe auf eingetragenen Höchstbetrag begrenzen und Überschuss bestimmen')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if hoechstbetragshypothek_anwendbar else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Qualifizierte Hauptforderung, Zinsen und wirksame Höchstbetragshypothek; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['Nur gemeinsame Grenze für Hauptforderung und Zinsen nach§1190 Absatz2. Sonstige Kosten/Nebenleistungen und deren Behandlung gesondert, keine abschließende Gesamthaftungsrechnung. Kein weiterer Zinsaufschlag auf den eingetragenen Höchstbetrag; übersteigender persönlicher Forderungsanteil erlischt nicht automatisch. Keine Verteilung innerhalb der Grenze auf einzelne Anspruchskomponenten und keine Berechnung des Grundstücksverwertungserlöses. Zinsbetrag kommt aus gesonderter qualifizierter Zinsberechnung.']
    return ergebnis


def pfand_edelmetall_mindestpreis(angebotener_preis=None, gold_oder_silberwert=None, gold_oder_silbersache=None, bewertungsnachweis=None):
    """§1240: Gebot oder freihändiger Ersatzverkauf mindestens zum Edelmetallwert."""
    preis = _geld(angebotener_preis)
    metall = _geld(gold_oder_silberwert)
    _wahrheitswert(gold_oder_silbersache, 'gold_oder_silbersache')
    _text(bewertungsnachweis, 'bewertungsnachweis')
    eingaben = dict(angebotener_preis=angebotener_preis, gold_oder_silberwert=gold_oder_silberwert,
        gold_oder_silbersache=gold_oder_silbersache, bewertungsnachweis=bewertungsnachweis)
    ergebnis = _ergebnis(dict(mindestpreis=_bruchteile(metall), mindestpreis_erreicht=preis >= metall) if gold_oder_silbersache else None,
        'EUR_und_wahrheitswert', 'BGB_PFAND_EDELMETALL_MINDESTPREIS', eingaben,
        [dict(operation='Gebot beziehungsweise Preis mit rechtlich bewertetem Gold- oder Silberwert vergleichen')], eingaben.copy())
    ergebnis['status'] = 'BERECHNET' if gold_oder_silbersache else 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Edelmetallwert, Art des Pfandes und einschlägiges gesetzliches Verkaufsregime qualifiziert vorgegeben; feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['Preisuntergrenze gilt für Zuschlag und freihändigen Ersatzverkauf nach§1240 Absatz2. Kein Börsenkursabruf, keine automatische Material-/Feingehaltsbewertung und kein Abschlag wegen fehlender Gebote. Qualifizierten maßgeblichen Gold-/Silberwert vorgeben; andere gesetzliche Verkaufsbedingungen, befugte Verkaufsperson und zulässige Abweichungen gesondert. Erreichter Mindestpreis bedeutet keine vollständige Rechtmäßigkeit des Verkaufs.']
    return ergebnis
