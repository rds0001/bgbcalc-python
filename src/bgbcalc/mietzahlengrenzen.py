"""Numerische Mietrechtsgrenzen ohne automatische Rechtsfolgenentscheidung."""
from .betraege import _geld
from .kalender import _ergebnis, _fehler, _ganzzahl, _text
from .zahlen import _bruch, _subtrahieren
from .zinsen import _bruchteile


def waermelieferung_kosten_und_nutzungsgradgrenzen(bisherige_betriebskosten=None, neue_waermelieferkosten=None, jahresnutzungsgrad_prozent=None, einordnungsnachweis=None):
    """Neue und bisherige Wärmekosten vergleichen; Jahresnutzungsgrad mit80Prozent vergleichen."""
    x = [_geld(bisherige_betriebskosten), _geld(neue_waermelieferkosten), _geld(jahresnutzungsgrad_prozent)]
    _text(einordnungsnachweis,'einordnungsnachweis')
    eingaben = dict(bisherige_betriebskosten=bisherige_betriebskosten, neue_waermelieferkosten=neue_waermelieferkosten, jahresnutzungsgrad_prozent=jahresnutzungsgrad_prozent, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(dict(kostendifferenz=_bruchteile(_subtrahieren(x[1],x[0])),kostenneutralitaetsgrenze_eingehalten=x[1]<=x[0],nutzungsgradgrenze_erreicht=x[2]>=80), "zahlen_und_wahrheitswerte", 'BGB_WAERMELIEFERUNG_KOSTEN_UND_NUTZUNGSGRADGRENZEN', eingaben, [dict(operation='Neue und bisherige Wärmekosten vergleichen; Jahresnutzungsgrad mit80Prozent vergleichen.')], eingaben.copy())
    ergebnis["hinweise"] = ['Nur numerische Teilbedingungen nach556cI. Kosten für denselben rechtlich maßgeblichen Vergleichszeitraum und Versorgungsumfang vorqualifizieren; keine eigenständige Berechnung nach externer Wärmelieferverordnung. Nutzungsgrad in Prozentpunkten,80 bedeutet80Prozent; keine automatische Bewertung der Anlage oder verbesserter Betriebsführung. Grenzwerte einschließlich Gleichheit. Ergebnis entscheidet nicht sämtliche Voraussetzungen der Kostenumlage; Ankündigung556cII separat.']
    return ergebnis


def mietspiegel_spanneneinordnung(spannengrenze_unten=None, spannengrenze_oben=None, verlangte_miete=None, einordnungsnachweis=None):
    """Verlangte Miete einschließlich der Grenzen mit qualifizierter Mietspiegelspanne vergleichen."""
    x = [_geld(spannengrenze_unten), _geld(spannengrenze_oben), _geld(verlangte_miete)]
    _text(einordnungsnachweis,'einordnungsnachweis')
    if x[0]>x[1]:
        _fehler('spannengrenze_oben','Obergrenze darf nicht unter Untergrenze liegen.')
    eingaben = dict(spannengrenze_unten=spannengrenze_unten, spannengrenze_oben=spannengrenze_oben, verlangte_miete=verlangte_miete, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(dict(innerhalb_der_spanne=x[0]<=x[2]<=x[1],unterhalb_unterschreitungsbetrag=_bruchteile(max(_subtrahieren(x[0],x[2]),_bruch(0))),oberhalb_ueberschreitungsbetrag=_bruchteile(max(_subtrahieren(x[2],x[1]),_bruch(0)))), "zahlen_und_wahrheitswerte", 'BGB_MIETSPIEGEL_SPANNENEINORDNUNG', eingaben, [dict(operation='Verlangte Miete einschließlich der Grenzen mit qualifizierter Mietspiegelspanne vergleichen.')], eingaben.copy())
    ergebnis["hinweise"] = ['Nur numerischer Spannenvergleich nach558aIV1; gleiche Miet-/Flächeneinheit und gleicher Zeitraum für alle drei Werte. Keine automatische Auswahl der Vergleichsmerkmale, kein Beweis endgültiger ortsüblicher Vergleichsmiete und keine Prüfung der vollständigen Mieterhöhungsberechtigung nach558. Unter- und Obergrenze zählen mit; keine automatische Erhöhung einer unter der Spanne verlangten Miete.']
    return ergebnis


def vergleichswohnungen_mindestzahl(anzahl_vergleichswohnungen=None, einordnungsnachweis=None):
    """Anzahl qualifizierter Vergleichswohnungen mit drei vergleichen und fehlende Anzahl bestimmen."""
    x = [_ganzzahl(anzahl_vergleichswohnungen,'anzahl_vergleichswohnungen',0,9007199254740991)]
    _text(einordnungsnachweis,'einordnungsnachweis')
    eingaben = dict(anzahl_vergleichswohnungen=anzahl_vergleichswohnungen, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(dict(mindestzahl=3,fehlende_wohnungen=max(3-x[0],0),mindestzahl_erreicht=x[0]>=3), "zahlen_und_wahrheitswerte", 'BGB_VERGLEICHSWOHNUNGEN_MINDESTZAHL', eingaben, [dict(operation='Anzahl qualifizierter Vergleichswohnungen mit drei vergleichen und fehlende Anzahl bestimmen.')], eingaben.copy())
    ergebnis["hinweise"] = ['Nur numerische Mindestzahl nach558aII Nummer4. Wohnungen müssen tatsächlich verschieden und rechtlich vergleichbar sein; Benennung und entsprechende Entgelte vorqualifizieren. Drei Wohnungen genügen als dieser Begründungsweg, entscheiden aber keine materielle Mieterhöhung. Kein Ersatz für notwendige Mietspiegelangaben nachAbsatz3.']
    return ergebnis


def mietspiegel_einwohnerschwelle(einwohnerzahl=None, einordnungsnachweis=None):
    """Gemeindeeinwohnerzahl strikt mit50000 vergleichen."""
    x = [_ganzzahl(einwohnerzahl,'einwohnerzahl',0,9007199254740991)]
    _text(einordnungsnachweis,'einordnungsnachweis')
    eingaben = dict(einwohnerzahl=einwohnerzahl, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(dict(einwohnergrenze=50000,grenze_ueberschritten=x[0]>50000), "zahlen_und_wahrheitswerte", 'BGB_MIETSPIEGEL_EINWOHNERSCHWELLE', eingaben, [dict(operation='Gemeindeeinwohnerzahl strikt mit50000 vergleichen.')], eingaben.copy())
    ergebnis["hinweise"] = ['Nur numerische Schwelle nach558cIV2; rechtlich maßgebliche Einwohnerzahl der betreffenden Gemeinde vorgeben. Genau50000 erfüllt die strikte Überschreitung nicht. Unterhalb der Schwelle kann weiterhin ein Bedürfnis nachAbsatz4Satz1 bestehen; keine allgemeine Befreiung von Aufgaben und keine automatische Mietspiegelerstellung.']
    return ergebnis
