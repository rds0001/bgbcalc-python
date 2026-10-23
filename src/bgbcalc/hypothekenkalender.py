"""Besondere Kalendergrenzen des Hypothekenrechts."""
from .kalender import _datum, _ergebnis, _fehler, _frist, _text

def hypothek_beschlagnahme_monatsgrenze(beschlagnahme_am=None, einordnungsnachweis=None):
    """§§1123II/1124II: Monatsende, nach dem15.Tag Ende des Folgemonats."""
    datum = _datum(beschlagnahme_am, 'beschlagnahme_am')
    _text(einordnungsnachweis,"einordnungsnachweis")
    folgemonat = datum.day > 15
    ende = _frist(f"{datum.year:04}-{datum.month:02}-01", 2 if folgemonat else 1, "monate", "tagesbeginn")
    wert = dict(letzter_erfasster_monat_endet_am=ende.isoformat(), folgender_monat_einbezogen=folgemonat)
    eingaben = dict(beschlagnahme_am=beschlagnahme_am,einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,"kalendergrenzen","BGB_HYPOTHEK_BESCHLAGNAHME_MONATSGRENZE",eingaben,[dict(operation='§§1123II/1124II: Monatsende, nach dem15.Tag Ende des Folgemonats.')],eingaben.copy())
    ergebnis["hinweise"] = ['Nur gesetzliche Kalendergrenze für vorqualifizierte Miet-/Pachtfälle.1123 erfordert zusätzlich Fälligkeit, Jahresablauf und Beschlagnahmebezug;1124 vorherige Verfügung. Diese Grenze allein entscheidet weder Haftungsfreiheit noch Wirksamkeit. Nicht auf1126 übertragen; dort gilt eine andere Dreimonatsregel.']
    return ergebnis

def hypothek_hinterlegung_zeitgrenzen(ausschliessungsbeschluss_rechtskraeftig_am=None, einordnungsnachweis=None):
    """§1171: Beginn des vierten vorangegangenen Kalenderjahres und30Jahre ab Rechtskraft."""
    datum = _datum(ausschliessungsbeschluss_rechtskraeftig_am, 'ausschliessungsbeschluss_rechtskraeftig_am')
    _text(einordnungsnachweis,"einordnungsnachweis")
    if datum.year < 5:
        _fehler("ausschliessungsbeschluss_rechtskraeftig_am","Vier vorangehende Kalenderjahre müssen im unterstützten Datumsbereich liegen.")
    ende = _frist(ausschliessungsbeschluss_rechtskraeftig_am,30,"jahre","ereignis")
    wert = dict(fruehester_hinterlegungszinsbeginn=f"{datum.year-4:04}-01-01", meldungsgrundfristende=ende.isoformat())
    eingaben = dict(ausschliessungsbeschluss_rechtskraeftig_am=ausschliessungsbeschluss_rechtskraeftig_am,einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,"kalendergrenzen","BGB_HYPOTHEK_HINTERLEGUNG_ZEITGRENZEN",eingaben,[dict(operation='§1171: Beginn des vierten vorangegangenen Kalenderjahres und30Jahre ab Rechtskraft.')],eingaben.copy())
    ergebnis["hinweise"] = ['Zinsbeginn ist nur früheste zu berücksichtigende Kalendergrenze, kein erfundener Zinsanspruch; Grundbucheintrag des Zinssatzes, tatsächlicher Zinslauf und Höhe gesondert.30Jahre sind Grundfrist für hinterlegten Betrag, keine automatische Erlöschensentscheidung bei vorheriger Meldung. Keine Anwendung anderer Aufgebotsfristen ohne Normprüfung.']
    return ergebnis

