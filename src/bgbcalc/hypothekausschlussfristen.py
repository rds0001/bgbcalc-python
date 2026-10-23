from .betraege import _wahrheitswert
from .kalender import _datum, _ergebnis, _fehler, _frist, _tage_addieren, _text

def hypothek_glaeubigerausschluss_grenze(letzte_eintragung_am=None, letztes_fristwirksames_anerkenntnis_am=None, kalendertag_zahlung_am=None, inhaberschuldverschreibung=None, vorlegungsfristende_am=None, fristgemaesse_vorlegung_oder_klage=None, verjaehrungsende_am=None, einordnungsnachweis=None):
    """Spätesten qualifizierten1170-Bezugstag bestimmen und zehnjährige Ereignisfrist berechnen; im1188II-Fall zusätzliche Vorlegungs-/Verjährungsgrenzen als Maximum berücksichtigen, ersten Folgetag ausgeben."""
    bezug = _datum(letzte_eintragung_am,'letzte_eintragung_am')
    for name,wert in [('letztes_fristwirksames_anerkenntnis_am',letztes_fristwirksames_anerkenntnis_am),('kalendertag_zahlung_am',kalendertag_zahlung_am)]:
        if wert is not None:
            bezug = max(bezug,_datum(wert,name))
    _wahrheitswert(inhaberschuldverschreibung,'inhaberschuldverschreibung');_text(einordnungsnachweis,'einordnungsnachweis')
    grundende = _frist(bezug.isoformat(),10,'jahre','ereignis');ende = grundende
    if inhaberschuldverschreibung:
        ende = max(ende,_datum(vorlegungsfristende_am,'vorlegungsfristende_am'))
        _wahrheitswert(fristgemaesse_vorlegung_oder_klage,'fristgemaesse_vorlegung_oder_klage')
        if fristgemaesse_vorlegung_oder_klage:
            ende = max(ende,_datum(verjaehrungsende_am,'verjaehrungsende_am'))
        elif verjaehrungsende_am is not None:
            _fehler('verjaehrungsende_am','Ohne fristgemäße Vorlegung/Klage keine ungenutzte Zusatzgrenze eingeben.')
    elif any(x is not None for x in [vorlegungsfristende_am,fristgemaesse_vorlegung_oder_klage,verjaehrungsende_am]):
        _fehler('inhaberschuldverschreibung','Außerhalb1188II alle Zusatzparameter ausdrücklich null.')
    wert = dict(grundfristende_1170=grundende.isoformat(),kombinierte_zeitgrenze=ende.isoformat(),erster_tag_nach_zeitgrenzen=_tage_addieren(ende,1).isoformat())
    eingaben = dict(letzte_eintragung_am=letzte_eintragung_am, letztes_fristwirksames_anerkenntnis_am=letztes_fristwirksames_anerkenntnis_am, kalendertag_zahlung_am=kalendertag_zahlung_am, inhaberschuldverschreibung=inhaberschuldverschreibung, vorlegungsfristende_am=vorlegungsfristende_am, fristgemaesse_vorlegung_oder_klage=fristgemaesse_vorlegung_oder_klage, verjaehrungsende_am=verjaehrungsende_am, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,"daten",'BGB_HYPOTHEK_GLAEUBIGERAUSSCHLUSS_GRENZE',eingaben,[dict(operation='Spätesten qualifizierten1170-Bezugstag bestimmen und zehnjährige Ereignisfrist berechnen; im1188II-Fall zusätzliche Vorlegungs-/Verjährungsgrenzen als Maximum berücksichtigen, ersten Folgetag ausgeben.')],eingaben.copy())
    ergebnis["hinweise"] = ['§1170I/1188II: nur zeitlicher Grundrahmen für Gläubigerausschluss, kein Ausschließungsbeschluss oder automatischer Eigentumserwerb. Zahlungstag wirkt als früheste Fristbeginnschranke; nicht zusätzlich zehn Jahre nach bereits berechnetem Fristende addieren. Anerkenntnis als letzten rechtlich wirksamen Neubeginn vorqualifizieren; frühere Anerkenntnisse vor späterer maßgeblicher Eintragung ändern deren späteren Beginn nicht. Keine automatische Ermittlung beliebiger Anerkenntnisketten. Bei1188II muss Vorlegungsfrist verstrichen sein; nach fristgemäßer Vorlegung/Klage zusätzlich Verjährung abwarten. Zusatzfristen müssen bereits vollständig gerechnet sein. Ergebnis vor etwaigen weiteren rechtlich festgestellten Korrekturen des1170-Grundlaufs; keine pauschale193-Verschiebung. Keine Prüfung der Unbekanntheit des Gläubigers, des Aufgebotsverfahrens oder der Voraussetzungen des Eigentumserwerbs1170II.']
    return ergebnis
